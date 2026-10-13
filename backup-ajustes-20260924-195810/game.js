/**
 * Show das Escrituras - Lógica Principal do Jogo
 */

class ScriptureShowGame {
  constructor() {
    this.selectedCategory = 'all';
    this.gameMode = 'single'; // 'single' ou 'teams'
    this.teamNames = { 1: 'Equipe Néfi', 2: 'Equipe Alma' };
    this.currentTeamTurn = 1;
    this.teamScores = { 1: 0, 2: 0 };

    this.currentLevelIndex = 0; // 0 a 15 (Níveis 1 a 16)
    this.currentQuestion = null;
    this.selectedAnswerIndex = null;
    this.isAnsweringLocked = false;
    this.eliminatedOptions = new Set();

    // Ajudas disponíveis
    this.lifelines = {
      seminary: false, // Usado?
      cards: false,    // Usado?
      gee: false,      // Usado?
      passCount: 3     // 3 pulos
    };

    this.activeQuestionPool = [];
    this.usedQuestionIds = new Set();
    this.totalCorrectAnswers = 0;
    this.accumulatedPrize = 0;

    this.initDOM();
    this.bindEvents();
    this.initCanvasParticles();
  }

  initDOM() {
    // Telas
    this.startScreen = document.getElementById('start-screen');
    this.gameScreen = document.getElementById('game-screen');
    this.gameOverScreen = document.getElementById('game-over-screen');

    // Botões e seletores do menu
    this.btnStart = document.getElementById('btn-start-game');
    this.categoryOptions = document.querySelectorAll('.category-option');
    this.modeButtons = document.querySelectorAll('.mode-btn');
    this.teamInputs = document.getElementById('team-inputs');
    this.team1Input = document.getElementById('team1-name-input');
    this.team2Input = document.getElementById('team2-name-input');

    // Controles de áudio
    this.btnSoundToggle = document.getElementById('btn-sound-toggle');
    this.btnMenuMusicToggle = document.getElementById('btn-menu-music-toggle');
    this.menuMusicLabel = document.getElementById('menu-music-label');

    // Elementos da Arena
    this.categoryBadge = document.getElementById('current-category-badge');
    this.levelBadge = document.getElementById('current-level-badge');
    this.turnBadge = document.getElementById('team-turn-badge');
    this.questionText = document.getElementById('question-text');
    this.answerCards = document.querySelectorAll('.answer-card');
    this.btnConfirm = document.getElementById('btn-confirm-answer');
    this.btnStop = document.getElementById('btn-stop-game');

    // Valores do Show (Acertar / Parar / Errar)
    this.valWin = document.getElementById('val-win');
    this.valStop = document.getElementById('val-stop');
    this.valLose = document.getElementById('val-lose');
    this.ladderList = document.getElementById('ladder-list');

    // Botões das Ajudas
    this.btnSeminary = document.getElementById('btn-lifeline-seminary');
    this.btnCards = document.getElementById('btn-lifeline-cards');
    this.btnGee = document.getElementById('btn-lifeline-gee');
    this.btnPass = document.getElementById('btn-lifeline-pass');
    this.passCountLabel = document.getElementById('pass-count-label');

    // Modais
    this.modalOverlay = document.getElementById('modal-overlay');
    this.seminaryModal = document.getElementById('seminary-modal');
    this.cardsModal = document.getElementById('cards-modal');
    this.geeModal = document.getElementById('gee-modal');
    this.scriptureModal = document.getElementById('scripture-modal');

    // Elementos internos dos modais
    this.seminaryBarsContainer = document.getElementById('seminary-bars-container');
    this.cardsDeckContainer = document.getElementById('cards-deck-container');
    this.geeHintText = document.getElementById('gee-hint-text');
    this.scriptureModalTitle = document.getElementById('scripture-modal-title');
    this.scriptureModalRef = document.getElementById('scripture-modal-ref');
    this.scriptureModalDesc = document.getElementById('scripture-modal-desc');
    this.btnScriptureContinue = document.getElementById('btn-scripture-continue');

    // Tela de Fim de Jogo
    this.gameOverTitle = document.getElementById('game-over-title');
    this.gameOverPrize = document.getElementById('game-over-prize');
    this.statQuestionsAnswered = document.getElementById('stat-questions-answered');
    this.statModeResult = document.getElementById('stat-mode-result');
    this.statCategoryPlayed = document.getElementById('stat-category-played');
    this.btnPlayAgain = document.getElementById('btn-play-again');
  }

  bindEvents() {
    // Início suave da música na primeira interação do usuário na página
    const startAudioOnFirstInteraction = () => {
      soundEngine.init();
      if (this.startScreen.classList.contains('active') && !soundEngine.isMenuMusicPlaying && !soundEngine.muted) {
        soundEngine.startMenuMusic();
        this.updateMenuMusicUI();
      }
    };
    document.addEventListener('pointerdown', startAudioOnFirstInteraction, { once: true });

    // Botão de alternar música da abertura
    if (this.btnMenuMusicToggle) {
      this.btnMenuMusicToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        soundEngine.init();
        if (soundEngine.isMenuMusicPlaying) {
          soundEngine.stopMenuMusic();
        } else {
          soundEngine.startMenuMusic();
        }
        this.updateMenuMusicUI();
      });
    }

    // Escolha de Categoria das Obras-Padrão (Toca acorde temático especial)
    this.categoryOptions.forEach(opt => {
      opt.addEventListener('click', () => {
        this.categoryOptions.forEach(o => o.classList.remove('selected'));
        opt.classList.add('selected');
        this.selectedCategory = opt.dataset.category;

        // Toca o acorde harmônico exclusivo da obra selecionada
        soundEngine.playCategorySelect(this.selectedCategory);

        // Se a música de fundo ainda não começou, inicia agora
        if (!soundEngine.isMenuMusicPlaying && !soundEngine.muted) {
          soundEngine.startMenuMusic();
          this.updateMenuMusicUI();
        }
      });
    });

    // Escolha de Modo (Individual vs Equipes)
    this.modeButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        soundEngine.playClick();
        this.modeButtons.forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        this.gameMode = btn.dataset.mode;
        if (this.gameMode === 'teams') {
          this.teamInputs.classList.add('active');
        } else {
          this.teamInputs.classList.remove('active');
        }
      });
    });

    // Mudo / Som Geral
    this.btnSoundToggle.addEventListener('click', () => {
      const isMuted = soundEngine.toggleMute();
      this.btnSoundToggle.textContent = isMuted ? '🔇' : '🔊';
      this.btnSoundToggle.title = isMuted ? 'Ativar Som' : 'Desativar Som';
      this.updateMenuMusicUI();
    });

    // Iniciar Jogo
    this.btnStart.addEventListener('click', () => {
      soundEngine.playClick();
      if (this.gameMode === 'teams') {
        const t1 = this.team1Input.value.trim();
        const t2 = this.team2Input.value.trim();
        if (t1) this.teamNames[1] = t1;
        if (t2) this.teamNames[2] = t2;
      }
      this.startGame();
    });

    // Seleção de Alternativa
    this.answerCards.forEach(card => {
      card.addEventListener('click', () => {
        if (this.isAnsweringLocked) return;
        const optIndex = parseInt(card.dataset.index, 10);
        if (this.eliminatedOptions.has(optIndex)) return;

        soundEngine.playSelect();
        this.answerCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        this.selectedAnswerIndex = optIndex;
        this.btnConfirm.disabled = false;
      });
    });

    // Confirmar Resposta ("Você está certo disso?")
    this.btnConfirm.addEventListener('click', () => {
      if (this.selectedAnswerIndex === null || this.isAnsweringLocked) return;
      this.confirmAnswer();
    });

    // Parar Jogo
    this.btnStop.addEventListener('click', () => {
      if (this.isAnsweringLocked) return;
      this.stopGame();
    });

    // Botão Continuar após ler a Escritura
    this.btnScriptureContinue.addEventListener('click', () => {
      soundEngine.playClick();
      this.closeModals();
      if (this.isPendingGameOver) {
        this.showGameOver(false, this.pendingPrize);
      } else {
        this.nextQuestion();
      }
    });

    // Ajudas
    this.btnSeminary.addEventListener('click', () => this.useSeminaryLifeline());
    this.btnCards.addEventListener('click', () => this.useCardsLifeline());
    this.btnGee.addEventListener('click', () => this.useGeeLifeline());
    this.btnPass.addEventListener('click', () => this.usePassLifeline());

    // Fechar modais ao clicar no overlay
    this.modalOverlay.addEventListener('click', (e) => {
      if (e.target === this.modalOverlay) {
        // Se for o modal de escritura obrigatória, não fecha direto
        if (this.scriptureModal.style.display === 'block') return;
        this.closeModals();
      }
    });

    // Jogar Novamente
    this.btnPlayAgain.addEventListener('click', () => {
      soundEngine.playClick();
      this.showStartScreen();
    });
  }

  updateMenuMusicUI() {
    if (!this.btnMenuMusicToggle || !this.menuMusicLabel) return;
    if (soundEngine.isMenuMusicPlaying) {
      this.btnMenuMusicToggle.classList.add('active');
      this.menuMusicLabel.textContent = 'Música Tema: Tocando 🎵';
    } else {
      this.btnMenuMusicToggle.classList.remove('active');
      this.menuMusicLabel.textContent = 'Música Tema: Pausada 🔇';
    }
  }

  showStartScreen() {
    this.closeModals();
    soundEngine.stopSuspense();
    this.startScreen.classList.add('active');
    this.gameScreen.classList.remove('active');
    this.gameOverScreen.classList.remove('active');
    if (!soundEngine.muted) {
      soundEngine.startMenuMusic();
    }
    this.updateMenuMusicUI();
  }

  startGame() {
    soundEngine.stopMenuMusic();
    this.updateMenuMusicUI();
    this.currentLevelIndex = 0;
    this.totalCorrectAnswers = 0;
    this.accumulatedPrize = 0;
    this.usedQuestionIds.clear();
    this.teamScores = { 1: 0, 2: 0 };
    this.currentTeamTurn = 1;

    // Resetar Ajudas
    this.lifelines = {
      seminary: false,
      cards: false,
      gee: false,
      passCount: 3
    };
    this.updateLifelinesUI();

    // Renderizar escada lateral
    this.renderLadder();

    // Trocar de tela
    this.startScreen.classList.remove('active');
    this.gameOverScreen.classList.remove('active');
    this.gameScreen.classList.add('active');

    // Carregar primeira pergunta
    this.loadQuestion();
    soundEngine.startSuspense();
  }

  // Filtragem e seleção de pergunta adequada ao nível
  loadQuestion() {
    this.isAnsweringLocked = false;
    this.selectedAnswerIndex = null;
    this.eliminatedOptions.clear();
    this.btnConfirm.disabled = true;

    // Reset visual dos cards de resposta
    this.answerCards.forEach(card => {
      card.className = 'answer-card';
    });

    const currentLadderStep = PRIZE_LADDER[this.currentLevelIndex];
    const targetDifficulty = currentLadderStep.difficulty;

    // Filtrar perguntas disponíveis da categoria e dificuldade
    let candidates = QUESTIONS_DATABASE.filter(q => {
      if (this.usedQuestionIds.has(q.id)) return false;
      const matchCat = (this.selectedCategory === 'all') || (q.category === this.selectedCategory);
      const matchDiff = (q.difficulty === targetDifficulty);
      return matchCat && matchDiff;
    });

    // Se esgotar da categoria específica, busca qualquer categoria da mesma dificuldade para não travar
    if (candidates.length === 0) {
      candidates = QUESTIONS_DATABASE.filter(q => {
        return !this.usedQuestionIds.has(q.id) && (q.difficulty === targetDifficulty);
      });
    }

    // Se ainda assim esgotar (jogo prolongado), reseta histórico do nível
    if (candidates.length === 0) {
      candidates = QUESTIONS_DATABASE.filter(q => q.difficulty === targetDifficulty);
    }

    // Escolhe aleatoriamente
    const randomIndex = Math.floor(Math.random() * candidates.length);
    this.currentQuestion = candidates[randomIndex];
    this.usedQuestionIds.add(this.currentQuestion.id);

    // Atualizar UI
    this.renderQuestionUI();
  }

  renderQuestionUI() {
    const q = this.currentQuestion;
    const ladderStep = PRIZE_LADDER[this.currentLevelIndex];

    // Categoria e Dificuldade
    const catData = CATEGORIES_INFO[q.category] || CATEGORIES_INFO.all;
    this.categoryBadge.textContent = catData.badge;
    this.categoryBadge.style.borderColor = catData.color;

    const levelNum = this.currentLevelIndex + 1;
    this.levelBadge.textContent = levelNum === 16 ? '👑 PERGUNTA DO MILHÃO' : `PERGUNTA ${levelNum} DE 16`;

    // Indicador de Turno para Equipes
    if (this.gameMode === 'teams') {
      this.turnBadge.classList.add('active');
      this.turnBadge.textContent = `🎯 Vez de: ${this.teamNames[this.currentTeamTurn]}`;
    } else {
      this.turnBadge.classList.remove('active');
    }

    // Texto da Pergunta
    this.questionText.textContent = q.question;

    // Alternativas
    this.answerCards.forEach((card, idx) => {
      const textSpan = card.querySelector('.answer-text');
      textSpan.textContent = q.options[idx];
    });

    // Valores do Show (Acertar / Parar / Errar)
    this.valWin.textContent = `${ladderStep.prize.toLocaleString('pt-BR')} Talentos`;
    this.valStop.textContent = `${ladderStep.stop.toLocaleString('pt-BR')} Talentos`;
    this.valLose.textContent = `${ladderStep.wrong.toLocaleString('pt-BR')} Talentos`;

    // Atualizar destaque na escada
    this.updateLadderHighlight();
  }

  renderLadder() {
    this.ladderList.innerHTML = '';
    // Mostra do 16 para o 1 (de cima para baixo)
    for (let i = PRIZE_LADDER.length - 1; i >= 0; i--) {
      const step = PRIZE_LADDER[i];
      const item = document.createElement('div');
      item.className = 'ladder-item';
      item.id = `ladder-step-${i}`;

      if (i === 15) item.classList.add('million');
      else if (i === 4 || i === 9 || i === 14) item.classList.add('milestone');

      item.innerHTML = `
        <span>#${step.level}</span>
        <span>${step.prize.toLocaleString('pt-BR')} Talentos</span>
      `;
      this.ladderList.appendChild(item);
    }
  }

  updateLadderHighlight() {
    for (let i = 0; i < PRIZE_LADDER.length; i++) {
      const item = document.getElementById(`ladder-step-${i}`);
      if (!item) continue;
      item.classList.remove('current', 'passed');

      if (i === this.currentLevelIndex) {
        item.classList.add('current');
        item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      } else if (i < this.currentLevelIndex) {
        item.classList.add('passed');
      }
    }
  }

  updateLifelinesUI() {
    this.btnSeminary.disabled = this.lifelines.seminary;
    this.btnCards.disabled = this.lifelines.cards;
    this.btnGee.disabled = this.lifelines.gee;
    this.btnPass.disabled = this.lifelines.passCount <= 0;
    this.passCountLabel.textContent = `(${this.lifelines.passCount} restantes)`;
  }

  // Confirmação com suspense
  confirmAnswer() {
    this.isAnsweringLocked = true;
    this.btnConfirm.disabled = true;
    this.btnStop.disabled = true;

    // Desativa ajudas durante a resolução
    this.btnSeminary.disabled = true;
    this.btnCards.disabled = true;
    this.btnGee.disabled = true;
    this.btnPass.disabled = true;

    soundEngine.playLockIn();

    // Pausa dramática do Show do Milhão (1.4s)
    setTimeout(() => {
      const isCorrect = (this.selectedAnswerIndex === this.currentQuestion.correct);
      const selectedCard = this.answerCards[this.selectedAnswerIndex];
      const correctCard = this.answerCards[this.currentQuestion.correct];

      if (isCorrect) {
        soundEngine.playCorrect();
        selectedCard.classList.add('correct');
        this.handleCorrectAnswer();
      } else {
        soundEngine.playWrong();
        selectedCard.classList.add('wrong');
        correctCard.classList.add('correct');
        this.handleWrongAnswer();
      }
    }, 1400);
  }

  handleCorrectAnswer() {
    const currentStep = PRIZE_LADDER[this.currentLevelIndex];
    this.accumulatedPrize = currentStep.prize;
    this.totalCorrectAnswers++;

    // Se estiver em equipes, pontua a equipe do turno
    if (this.gameMode === 'teams') {
      this.teamScores[this.currentTeamTurn] += currentStep.prize;
    }

    // Se for a última pergunta (Pergunta do Milhão)
    if (this.currentLevelIndex === 15) {
      setTimeout(() => {
        soundEngine.playMillionVictory();
        this.launchConfetti();
        this.showScriptureModal(true, true);
      }, 1000);
      return;
    }

    setTimeout(() => {
      this.showScriptureModal(true, false);
    }, 1200);
  }

  handleWrongAnswer() {
    const currentStep = PRIZE_LADDER[this.currentLevelIndex];
    const prizeWon = currentStep.wrong;

    this.isPendingGameOver = true;
    this.pendingPrize = prizeWon;

    setTimeout(() => {
      this.showScriptureModal(false, false);
    }, 1400);
  }

  stopGame() {
    const currentStep = PRIZE_LADDER[this.currentLevelIndex];
    const prizeWon = currentStep.stop;
    soundEngine.playClick();
    this.showGameOver(false, prizeWon, true);
  }

  nextQuestion() {
    // Alterna turno se estiver em modo equipes
    if (this.gameMode === 'teams') {
      this.currentTeamTurn = (this.currentTeamTurn === 1) ? 2 : 1;
    }

    this.currentLevelIndex++;
    this.updateLifelinesUI();
    this.btnStop.disabled = false;
    this.loadQuestion();
  }

  // ===================================================================
  // AJUDAS DO JOGO
  // ===================================================================

  // 1. Alunos do Seminário (Votação da classe)
  useSeminaryLifeline() {
    if (this.lifelines.seminary || this.isAnsweringLocked) return;
    this.lifelines.seminary = true;
    this.updateLifelinesUI();

    soundEngine.playSeminaryChime();
    this.openModal(this.seminaryModal);

    // Calcular porcentagens inteligentes
    const correctIdx = this.currentQuestion.correct;
    const diff = this.currentQuestion.difficulty;

    // Conforme a dificuldade, alunos têm maior ou menor certeza
    let correctPct;
    if (diff === 1) correctPct = Math.floor(Math.random() * 16) + 75; // 75% a 90%
    else if (diff === 2) correctPct = Math.floor(Math.random() * 21) + 55; // 55% a 75%
    else if (diff === 3) correctPct = Math.floor(Math.random() * 21) + 40; // 40% a 60%
    else correctPct = Math.floor(Math.random() * 26) + 35; // 35% a 60% no milhão

    let remainingPct = 100 - correctPct;
    const otherPercentages = [0, 0, 0];
    
    // Divide o restante entre as outras 3 opções
    const p1 = Math.floor(Math.random() * (remainingPct - 2));
    const p2 = Math.floor(Math.random() * (remainingPct - p1 - 1));
    const p3 = remainingPct - p1 - p2;
    const splits = [p1, p2, p3];

    const letters = ['A', 'B', 'C', 'D'];
    const pcts = [];
    let splitIdx = 0;
    for (let i = 0; i < 4; i++) {
      if (i === correctIdx) {
        pcts.push(correctPct);
      } else {
        pcts.push(splits[splitIdx++]);
      }
    }

    // Renderizar barras
    this.seminaryBarsContainer.innerHTML = '';
    letters.forEach((letter, i) => {
      const isEliminated = this.eliminatedOptions.has(i);
      const val = isEliminated ? 0 : pcts[i];

      const row = document.createElement('div');
      row.className = 'seminary-bar-row';
      row.innerHTML = `
        <span class="seminary-bar-letter">[${letter}]</span>
        <div class="seminary-bar-track">
          <div class="seminary-bar-fill" id="sem-bar-${i}"></div>
        </div>
        <span class="seminary-bar-pct" id="sem-pct-${i}">0%</span>
      `;
      this.seminaryBarsContainer.appendChild(row);

      // Animação de preenchimento
      setTimeout(() => {
        const fill = document.getElementById(`sem-bar-${i}`);
        const text = document.getElementById(`sem-pct-${i}`);
        if (fill && text) {
          fill.style.width = `${val}%`;
          text.textContent = `${val}%`;
        }
      }, 100 + i * 80);
    });
  }

  // 2. As Cartas (Ás, 2, 3, Rei)
  useCardsLifeline() {
    if (this.lifelines.cards || this.isAnsweringLocked) return;
    this.lifelines.cards = true;
    this.updateLifelinesUI();

    soundEngine.playCardFlip();
    this.openModal(this.cardsModal);

    // Preparar as 4 cartas embaralhadas
    // Rei: 0 erradas eliminadas
    // Ás: 1 errada eliminada
    // 2: 2 erradas eliminadas
    // 3: 3 erradas eliminadas
    const deckCards = [
      { name: 'Rei 👑', eliminate: 0, desc: 'Nenhuma alternativa eliminada' },
      { name: 'Ás 🂡', eliminate: 1, desc: '1 alternativa eliminada' },
      { name: '2 🂢', eliminate: 2, desc: '2 alternativas eliminadas' },
      { name: '3 🂣', eliminate: 3, desc: '3 alternativas eliminadas!' }
    ];

    // Embaralhar
    deckCards.sort(() => Math.random() - 0.5);

    this.cardsDeckContainer.innerHTML = '';
    deckCards.forEach((c) => {
      const cardEl = document.createElement('div');
      cardEl.className = 'card-item';
      cardEl.innerHTML = `
        <div class="card-face card-back"></div>
        <div class="card-face card-front">
          <div class="card-front-value">${c.name}</div>
          <div class="card-front-info">${c.desc}</div>
        </div>
      `;

      cardEl.addEventListener('click', () => {
        if (cardEl.classList.contains('flipped')) return;
        soundEngine.playCardFlip();
        cardEl.classList.add('flipped');

        // Desativa outras cartas
        document.querySelectorAll('.card-item').forEach(other => {
          if (other !== cardEl) {
            setTimeout(() => other.classList.add('flipped'), 600);
          }
        });

        // Aplicar eliminação nas respostas da arena após 1 segundo
        setTimeout(() => {
          this.applyCardElimination(c.eliminate);
          this.closeModals();
        }, 1800);
      });

      this.cardsDeckContainer.appendChild(cardEl);
    });
  }

  applyCardElimination(count) {
    if (count <= 0) return;
    const correctIdx = this.currentQuestion.correct;
    const wrongIndices = [0, 1, 2, 3].filter(idx => idx !== correctIdx && !this.eliminatedOptions.has(idx));
    
    // Embaralha e elimina a quantidade sorteada
    wrongIndices.sort(() => Math.random() - 0.5);
    const toEliminate = wrongIndices.slice(0, count);

    toEliminate.forEach(idx => {
      this.eliminatedOptions.add(idx);
      this.answerCards[idx].classList.add('eliminated');
    });
  }

  // 3. GEE (Guia para Estudo das Escrituras)
  useGeeLifeline() {
    if (this.lifelines.gee || this.isAnsweringLocked) return;
    this.lifelines.gee = true;
    this.updateLifelinesUI();

    soundEngine.playGeeReveal();
    this.geeHintText.textContent = `"${this.currentQuestion.hint}"`;
    this.openModal(this.geeModal);
  }

  // 4. Pular / Passar Pergunta
  usePassLifeline() {
    if (this.lifelines.passCount <= 0 || this.isAnsweringLocked) return;
    this.lifelines.passCount--;
    this.updateLifelinesUI();

    soundEngine.playPass();
    this.loadQuestion();
  }

  // ===================================================================
  // MODAIS & REVELAÇÕES
  // ===================================================================

  openModal(modalElement) {
    this.modalOverlay.classList.add('active');
    [this.seminaryModal, this.cardsModal, this.geeModal, this.scriptureModal].forEach(m => {
      m.style.display = 'none';
    });
    modalElement.style.display = 'block';
  }

  closeModals() {
    this.modalOverlay.classList.remove('active');
    [this.seminaryModal, this.cardsModal, this.geeModal, this.scriptureModal].forEach(m => {
      m.style.display = 'none';
    });
  }

  showScriptureModal(isCorrect, isFinalMillion) {
    const q = this.currentQuestion;

    if (isFinalMillion) {
      this.scriptureModalTitle.textContent = "🏆 VITÓRIA EXTRAORDINÁRIA: 1 MILHÃO DE TALENTOS!";
      this.scriptureModalTitle.style.color = "#ffd700";
    } else if (isCorrect) {
      this.scriptureModalTitle.textContent = "✨ RESPOSTA CORRETA!";
      this.scriptureModalTitle.style.color = "#10b981";
    } else {
      this.scriptureModalTitle.textContent = "❌ RESPOSTA INCORRETA";
      this.scriptureModalTitle.style.color = "#ef4444";
    }

    this.scriptureModalRef.textContent = `📖 ${q.scriptureRef}`;
    this.scriptureModalDesc.textContent = q.explanation;

    this.btnScriptureContinue.textContent = isFinalMillion ? "Ver Premiação Celestial" : "Prosseguir na Jornada";
    this.openModal(this.scriptureModal);
  }

  // ===================================================================
  // FIM DE JOGO E COMEMORAÇÃO
  // ===================================================================
  showGameOver(isMillionWon, finalPrize, playerStopped = false) {
    this.closeModals();
    soundEngine.stopSuspense();
    this.isPendingGameOver = false;

    this.gameScreen.classList.remove('active');
    this.gameOverScreen.classList.add('active');

    if (isMillionWon) {
      this.gameOverTitle.textContent = "VOCÊ CONQUISTOU 1 MILHÃO DE TALENTOS!";
      this.launchConfetti();
    } else if (playerStopped) {
      this.gameOverTitle.textContent = "VOCÊ DECIDIU PARAR!";
    } else {
      this.gameOverTitle.textContent = "FIM DE JOGO!";
    }

    this.gameOverPrize.textContent = `${finalPrize.toLocaleString('pt-BR')} Talentos`;
    this.statQuestionsAnswered.textContent = `${this.totalCorrectAnswers} / 16`;
    
    if (this.gameMode === 'teams') {
      const winner = this.teamScores[1] > this.teamScores[2] 
        ? `${this.teamNames[1]} venceu!` 
        : (this.teamScores[2] > this.teamScores[1] ? `${this.teamNames[2]} venceu!` : 'Empate!');
      this.statModeResult.textContent = winner;
    } else {
      this.statModeResult.textContent = "Jornada Individual";
    }

    const catData = CATEGORIES_INFO[this.selectedCategory] || CATEGORIES_INFO.all;
    this.statCategoryPlayed.textContent = catData.name;
  }

  // Partículas Celestes de Fundo
  initCanvasParticles() {
    const canvas = document.getElementById('particles-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let w = canvas.width = window.innerWidth;
    let h = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      w = canvas.width = window.innerWidth;
      h = canvas.height = window.innerHeight;
    });

    const particles = [];
    const count = 45;

    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * w,
        y: Math.random() * h,
        radius: Math.random() * 2 + 0.8,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        alpha: Math.random() * 0.7 + 0.2,
        gold: Math.random() > 0.4
      });
    }

    function animate() {
      ctx.clearRect(0, 0, w, h);
      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = w;
        if (p.x > w) p.x = 0;
        if (p.y < 0) p.y = h;
        if (p.y > h) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.gold ? `rgba(253, 224, 71, ${p.alpha})` : `rgba(56, 189, 248, ${p.alpha})`;
        ctx.shadowBlur = 8;
        ctx.shadowColor = p.gold ? '#f59e0b' : '#38bdf8';
        ctx.fill();
      });
      requestAnimationFrame(animate);
    }
    animate();
  }

  // Chuva de Confetes para o Milhão
  launchConfetti() {
    const canvas = document.getElementById('particles-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const confettiPieces = [];
    const colors = ['#f59e0b', '#fde047', '#38bdf8', '#10b981', '#ec4899', '#ffffff'];

    for (let i = 0; i < 150; i++) {
      confettiPieces.push({
        x: Math.random() * canvas.width,
        y: Math.random() * -canvas.height,
        w: Math.random() * 10 + 6,
        h: Math.random() * 6 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        vy: Math.random() * 4 + 3,
        vx: (Math.random() - 0.5) * 3,
        rot: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 8
      });
    }

    let frames = 0;
    function renderConfetti() {
      if (frames > 350) return;
      confettiPieces.forEach(c => {
        c.y += c.vy;
        c.x += c.vx;
        c.rot += c.rotSpeed;

        ctx.save();
        ctx.translate(c.x, c.y);
        ctx.rotate((c.rot * Math.PI) / 180);
        ctx.fillStyle = c.color;
        ctx.fillRect(-c.w / 2, -c.h / 2, c.w, c.h);
        ctx.restore();
      });
      frames++;
      requestAnimationFrame(renderConfetti);
    }
    renderConfetti();
  }
}

// Inicializar quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
  window.gameInstance = new ScriptureShowGame();
});
