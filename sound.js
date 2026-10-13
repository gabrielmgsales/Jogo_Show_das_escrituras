/**
 * Show das Escrituras - Sound Engine (Web Audio API)
 * Efeitos sonoros procedurais que não dependem de arquivos externos de áudio.
 */

class SoundEngine {
  constructor() {
    this.ctx = null;
    this.muted = false;
    this.ambientGain = null;
    this.ambientOsc1 = null;
    this.ambientOsc2 = null;
    this.isSuspensePlaying = false;
    this.isMenuMusicPlaying = false;
    this.menuMusicTimer = null;
    this.menuStep = 0;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.ctx = new AudioContext();
      }
    }
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  }

  toggleMute() {
    this.muted = !this.muted;
    if (this.muted) {
      if (this.isSuspensePlaying) this.stopSuspense();
      if (this.isMenuMusicPlaying) this.stopMenuMusic();
    }
    return this.muted;
  }

  playTone(freq, type, duration, gainLevel = 0.2, attack = 0.02, decay = 0.05) {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    try {
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = type;
      osc.frequency.setValueAtTime(freq, now);

      gain.gain.setValueAtTime(0, now);
      gain.gain.linearRampToValueAtTime(gainLevel, now + attack);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + duration + decay);
    } catch (e) {
      console.warn("Audio error:", e);
    }
  }

  // Som de clique nos botões
  playClick() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;
    this.playTone(800, "triangle", 0.04, 0.15, 0.005, 0.02);
  }

  // Som ao selecionar uma alternativa
  playSelect() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    
    // Duas notas rápidas ascendentes
    this.playTone(523.25, "sine", 0.08, 0.2, 0.01); // C5
    setTimeout(() => {
      this.playTone(659.25, "sine", 0.12, 0.2, 0.01); // E5
    }, 70);
  }

  // Som de travamento da resposta ("Você está certo disso?")
  playLockIn() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    // Tensão dramática crescente
    [220, 277.18, 329.63, 440].forEach((f, idx) => {
      setTimeout(() => {
        this.playTone(f, "sawtooth", 0.35, 0.18, 0.04, 0.1);
      }, idx * 90);
    });
  }

  // Fanfarra de resposta correta
  playCorrect() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    const chords = [
      { f: 523.25, time: 0 },    // C5
      { f: 659.25, time: 100 },  // E5
      { f: 783.99, time: 200 },  // G5
      { f: 1046.50, time: 350 }, // C6
      { f: 1318.51, time: 500 }  // E6
    ];

    chords.forEach(c => {
      setTimeout(() => {
        this.playTone(c.f, "sine", 0.45, 0.25, 0.02, 0.1);
        this.playTone(c.f * 0.5, "triangle", 0.4, 0.15, 0.02, 0.1);
      }, c.time);
    });
  }

  // Som de erro dramático
  playWrong() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    // Som de buzina grave/pesada
    const now = this.ctx.currentTime;
    [130.81, 123.47, 116.54, 98.00].forEach((f, idx) => {
      setTimeout(() => {
        this.playTone(f, "sawtooth", 0.5, 0.25, 0.02, 0.2);
        this.playTone(f * 0.5, "square", 0.5, 0.15, 0.02, 0.2);
      }, idx * 120);
    });
  }

  // Som de cartas virando
  playCardFlip() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    for (let i = 0; i < 4; i++) {
      setTimeout(() => {
        this.playTone(400 + i * 150, "sine", 0.05, 0.12, 0.005, 0.02);
      }, i * 40);
    }
  }

  // Som dos alunos do seminário votando
  playSeminaryChime() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    [440, 554.37, 659.25, 880].forEach((f, idx) => {
      setTimeout(() => {
        this.playTone(f, "triangle", 0.2, 0.18, 0.01, 0.05);
      }, idx * 70);
    });
  }

  // Som de revelação do GEE
  playGeeReveal() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    [587.33, 739.99, 880, 1174.66].forEach((f, idx) => {
      setTimeout(() => {
        this.playTone(f, "sine", 0.6, 0.2, 0.05, 0.2);
      }, idx * 80);
    });
  }

  // Som ao pular pergunta
  playPass() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    [300, 450, 600, 750].forEach((f, idx) => {
      setTimeout(() => {
        this.playTone(f, "sine", 0.1, 0.15, 0.01, 0.03);
      }, idx * 50);
    });
  }

  // Grande Fanfarra do Milhão
  playMillionVictory() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    const melody = [
      { f: 523.25, d: 200, delay: 0 },
      { f: 523.25, d: 200, delay: 200 },
      { f: 523.25, d: 200, delay: 400 },
      { f: 659.25, d: 400, delay: 600 },
      { f: 587.33, d: 200, delay: 1000 },
      { f: 659.25, d: 200, delay: 1200 },
      { f: 783.99, d: 800, delay: 1400 },
      { f: 1046.50, d: 1200, delay: 2200 }
    ];

    melody.forEach(m => {
      setTimeout(() => {
        this.playTone(m.f, "sawtooth", m.d / 1000, 0.28, 0.03, 0.1);
        this.playTone(m.f * 0.5, "sine", m.d / 1000, 0.25, 0.03, 0.1);
      }, m.delay);
    });
  }

  // Clima de suspense sutil de fundo
  startSuspense() {
    if (this.muted || this.isSuspensePlaying) return;
    this.init();
    if (!this.ctx) return;

    try {
      const now = this.ctx.currentTime;
      this.ambientGain = this.ctx.createGain();
      this.ambientGain.gain.setValueAtTime(0.001, now);
      this.ambientGain.gain.linearRampToValueAtTime(0.04, now + 1.5);

      this.ambientOsc1 = this.ctx.createOscillator();
      this.ambientOsc2 = this.ctx.createOscillator();

      this.ambientOsc1.type = "sine";
      this.ambientOsc1.frequency.setValueAtTime(65.41, now); // C2

      this.ambientOsc2.type = "triangle";
      this.ambientOsc2.frequency.setValueAtTime(98.00, now); // G2

      this.ambientOsc1.connect(this.ambientGain);
      this.ambientOsc2.connect(this.ambientGain);
      this.ambientGain.connect(this.ctx.destination);

      this.ambientOsc1.start(now);
      this.ambientOsc2.start(now);
      this.isSuspensePlaying = true;
    } catch (e) {
      console.warn("Suspense audio error", e);
    }
  }

  stopSuspense() {
    if (!this.isSuspensePlaying || !this.ctx || !this.ambientGain) return;
    try {
      const now = this.ctx.currentTime;
      this.ambientGain.gain.linearRampToValueAtTime(0.0001, now + 0.5);
      setTimeout(() => {
        if (this.ambientOsc1) {
          this.ambientOsc1.stop();
          this.ambientOsc1.disconnect();
          this.ambientOsc1 = null;
        }
        if (this.ambientOsc2) {
          this.ambientOsc2.stop();
          this.ambientOsc2.disconnect();
          this.ambientOsc2 = null;
        }
        this.isSuspensePlaying = false;
      }, 550);
    } catch (e) {
      this.isSuspensePlaying = false;
    }
  }

  // Acordes harmônicos especiais para cada Obra-Padrão
  playCategorySelect(category) {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    const chordsMap = {
      all: [523.25, 659.25, 783.99, 1046.50], // Dó Maior Dourado
      bom: [587.33, 739.99, 880.00, 1174.66], // Ré Maior Liahona
      nt:  [659.25, 830.61, 987.77, 1318.51], // Mi Maior Celestial
      ot:  [349.23, 440.00, 523.25, 698.46],  // Fá Maior Solene
      dc:  [392.00, 493.88, 587.33, 783.99],  // Sol Maior Revelação
      pgv: [440.00, 554.37, 659.25, 880.00]   // Lá Maior Cólobe / Estelar
    };

    const notes = chordsMap[category] || chordsMap.all;
    notes.forEach((freq, idx) => {
      setTimeout(() => {
        this.playTone(freq, "sine", 0.35, 0.15, 0.01, 0.08);
        this.playTone(freq * 0.5, "triangle", 0.3, 0.1, 0.01, 0.08);
      }, idx * 60);
    });
  }

  // Trilha sonora procedural animada da tela de abertura
  startMenuMusic() {
    if (this.muted || this.isMenuMusicPlaying) return;
    this.init();
    if (!this.ctx) return;

    this.isMenuMusicPlaying = true;
    this.menuStep = 0;

    const chords = [
      // Cmaj7
      { bass: 130.81, notes: [261.63, 329.63, 392.00, 493.88, 523.25] },
      // Am7
      { bass: 110.00, notes: [220.00, 261.63, 329.63, 392.00, 440.00] },
      // Fmaj7
      { bass: 87.31,  notes: [174.61, 220.00, 261.63, 329.63, 392.00] },
      // G9 / G7
      { bass: 98.00,  notes: [196.00, 246.94, 293.66, 349.23, 392.00] }
    ];

    const stepDuration = 240; // ms por nota

    this.menuMusicTimer = setInterval(() => {
      if (!this.isMenuMusicPlaying || this.muted) return;

      const chordIdx = Math.floor(this.menuStep / 8) % chords.length;
      const stepInChord = this.menuStep % 8;
      const currentChord = chords[chordIdx];

      // Toca o baixo no tempo 0 e tempo 4
      if (stepInChord === 0 || stepInChord === 4) {
        this.playTone(currentChord.bass, "triangle", 0.32, 0.09, 0.02, 0.1);
      }

      // Arpejo cintilante melódico
      const pattern = [0, 1, 2, 3, 4, 2, 3, 1];
      const noteIdx = pattern[stepInChord];
      const freq = currentChord.notes[noteIdx];

      // Nota principal da melodia
      this.playTone(freq, "sine", 0.22, 0.08, 0.01, 0.05);

      // Adiciona brilho de sino sutil em tempos ímpares
      if (stepInChord === 2 || stepInChord === 6) {
        this.playTone(freq * 2, "sine", 0.15, 0.03, 0.005, 0.03);
      }

      this.menuStep++;
    }, stepDuration);
  }

  stopMenuMusic() {
    if (this.menuMusicTimer) {
      clearInterval(this.menuMusicTimer);
      this.menuMusicTimer = null;
    }
    this.isMenuMusicPlaying = false;
    this.menuStep = 0;
  }
}

// Instância global de áudio
const soundEngine = new SoundEngine();
