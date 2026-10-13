# -*- coding: utf-8 -*-
"""Gerador do banco PGV; mantém textos revisados e gabaritos distribuídos."""
import json
from pathlib import Path

questions = [
  {
    "id": "pgv_001",
    "category": "pgv",
    "difficulty": 1,
    "question": "Em Moisés 1:39, qual é a célebre declaração que define a obra e o propósito supremo de Deus?",
    "options": [
      "Estabelecer um reino terreno que reúna todas as nações",
      "Fazer toda a humanidade permanecer para sempre no Éden",
      "Conceder a todos o poder de criar mundos antes de serem provados",
      "Realizar Sua obra e glória levando a efeito a imortalidade e a vida eterna do homem"
    ],
    "correct": 3,
    "scriptureRef": "Moisés 1:39",
    "hint": "O Senhor revelou este propósito após mostrar a Moisés todas as criações da Terra e dos céus.",
    "explanation": "Moisés 1:39 é a pedra angular da teologia da salvação, revelando que a glória de Deus é exaltar e salvar Seus filhos."
  },
  {
    "id": "pgv_002",
    "category": "pgv",
    "difficulty": 2,
    "question": "O que Moisés sentiu fisicamente após a presença da glória de Deus se afastar dele em Moisés 1:9-10?",
    "options": [
      "Permaneceu de pé e continuou vendo a glória sem interrupção",
      "Recobrou as forças imediatamente e começou a subir outro monte",
      "Caiu por terra e demorou a recuperar as forças",
      "Adormeceu e só se lembrou da visão depois de voltar ao Egito"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 1:9-10",
    "hint": "Ele percebeu a absoluta pequenez do homem mortal perante a magnificência infinita do Criador.",
    "explanation": "Moisés esteve transfigurado na presença de Deus; ao cessar a glória, sua fraqueza mortal evidenciou a infinita distância entre o homem e a Divindade."
  },
  {
    "id": "pgv_003",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que Moisés ordenou a Satanás quando este apareceu clamando com raiva: 'Moisés, filho do homem, adora-me'?",
    "options": [
      "Recusou adorá-lo e ordenou que se retirasse, lembrando sua relação com o Unigênito",
      "Pediu que Satanás mostrasse primeiro uma prova de seu poder",
      "Aceitou ouvir Satanás antes de decidir a quem deveria adorar",
      "Pediu um sinal aos céus antes de responder à ordem de Satanás"
    ],
    "correct": 0,
    "scriptureRef": "Moisés 1:12-16",
    "hint": "Moisés comparou a escuridão vazia de Satanás com a luz resplandecente da glória de Deus.",
    "explanation": "Moisés repeliu o adversário pelo nome de Jesus Cristo, fazendo Satanás chorar, bramir e tremer antes de fugir."
  },
  {
    "id": "pgv_004",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Moisés 4:1-4, o que Lúcifer exigiu de Deus no conselho pré-mortal em troca de sua proposta de redimir toda a humanidade destruindo o livre-arbítrio?",
    "options": [
      "A própria honra divina, em troca de sua proposta de redimir todos os homens",
      "O direito de escolher quem receberia um corpo",
      "O governo sobre uma parte das hostes celestes",
      "A autoridade sobre os que permanecessem no céu"
    ],
    "correct": 0,
    "scriptureRef": "Moisés 4:1-4",
    "hint": "Em contraste com o Salvador, que disse: 'Pai, faça-se a tua vontade e seja tua a glória para sempre'.",
    "explanation": "A rebelião de Lúcifer nasceu de seu orgulho desmedido em buscar destronar o próprio Deus e aniquilar o arbítrio moral do homem."
  },
  {
    "id": "pgv_005",
    "category": "pgv",
    "difficulty": 2,
    "question": "O que o anjo do Senhor explicou a Adão em Moisés 5:6-7 quando lhe perguntou por que oferecia sacrifícios de animais ao Senhor?",
    "options": [
      "Substituía para sempre a necessidade de arrependimento",
      "Garantia a volta imediata de toda a família ao jardim do Éden",
      "Era uma representação do sacrifício do Unigênito do Pai, cheio de graça e verdade",
      "Reconstituía o convênio feito com Adão antes da criação"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 5:6-7",
    "hint": "Adão respondeu com pura fé: 'Não sei, a não ser que o Senhor me mandou'.",
    "explanation": "O anjo ensinou que os sacrifícios da lei mosaica apontavam simbolicamente para a futura redenção operada na cruz por Jesus Cristo."
  },
  {
    "id": "pgv_006",
    "category": "pgv",
    "difficulty": 3,
    "question": "Qual título diabólico Caim tomou sobre si em Moisés 5:31 ao fazer um pacto secreto com Satanás para matar seu irmão Abel e obter seu rebanho?",
    "options": [
      "Senhor de Canaã",
      "Príncipe de Babel",
      "Guardião de Sião",
      "Mestre Maã"
    ],
    "correct": 3,
    "scriptureRef": "Moisés 5:31",
    "hint": "Ele se gloriou cinicamente dizendo: 'Estou livre; com certeza os rebanhos de meu irmão caem em minhas mãos'.",
    "explanation": "Caim inaugurou as combinações secretas e juramentos abomináveis da história humana motivado pela cobiça e homicídio."
  },
  {
    "id": "pgv_007",
    "category": "pgv",
    "difficulty": 2,
    "question": "Como o jovem profeta Enoque descreveu sua própria fraqueza humana quando o Senhor o chamou para pregar arrependimento ao povo em Moisés 6:31?",
    "options": [
      "Era velho, estava enfermo e não conseguia percorrer as cidades",
      "Era jovem, odiado pelo povo e lento no falar",
      "Era estrangeiro, não conhecia a terra e não falava seu idioma",
      "Não tinha família, não possuía terras e não sabia escrever"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 6:31",
    "hint": "O Senhor respondeu: 'Abre a tua boca e ela encher-se-á, e eu te darei o que falar'.",
    "explanation": "Enoque sentia-se inadequado, mas a graça de Deus o transformou num dos maiores profetas da história universal."
  },
  {
    "id": "pgv_008",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que o Senhor mandou Enoque fazer com barro e água em Moisés 6:35 para que seus olhos espirituais fossem abertos?",
    "options": [
      "Lavar as mãos e colocar barro sobre o altar",
      "Misturar barro na água e ungir a cabeça",
      "Passar barro nos olhos e depois lavá-los, conforme a ordem que recebeu",
      "Untar os pés e atravessar a corrente de água"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 6:35",
    "hint": "Ao lavar os olhos, ele contemplou os espíritos que Deus havia criado e coisas que não eram visíveis a olho nu.",
    "explanation": "Moisés 6:35 manda Enoque ungir os olhos com barro e lavá-los. O texto não identifica a fonte como Siloé."
  },
  {
    "id": "pgv_009",
    "category": "pgv",
    "difficulty": 1,
    "question": "Em Moisés 7:18, quais são as três características sublimes que definiam o povo da Cidade de Sião liderado por Enoque?",
    "options": [
      "Culto no templo, linhagem comum e domínio sobre os vizinhos",
      "Unidade de idioma e governo, prosperidade e força militar",
      "Unidade de coração e mente, retidão e ausência de pobres",
      "Obediência ao rei, riqueza de todos e isolamento das nações"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 7:18",
    "hint": "O padrão supremo do que o Senhor espera de Sua Igreja em todas as dispensações.",
    "explanation": "A pureza e unidade perfeita do povo de Enoque alcançou tal glória que o Senhor chamou seu povo de Sião e o transladou aos céus."
  },
  {
    "id": "pgv_010",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que o profeta Enoque viu o Deus do Céu fazer em Moisés 7:28 que o deixou profundamente atônito e comovido?",
    "options": [
      "Deus ordenando o imediato fim de toda a criação",
      "Viu o Deus do Céu chorar por causa da iniquidade e do sofrimento de Seus filhos",
      "Deus transferindo a Terra para a autoridade dos anjos",
      "Deus retirando para sempre a luz do sol sobre os homens"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 7:28-33",
    "hint": "Enoque perguntou assombrado: 'Como é que os céus choram e suas lágrimas caem como a chuva sobre as montanhas?'.",
    "explanation": "Este capítulo revela o coração compassivo de Deus, que não é um ser impassível, mas um Pai amoroso que chora pelas dores de Seus filhos."
  },
  {
    "id": "pgv_011",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Moisés 7:62-64, qual glorioso encontro de dois povos é profetizado para ocorrer na Segunda Vinda de Jesus Cristo?",
    "options": [
      "A cidade de Jerusalém será unida ao reino dos antigos egípcios",
      "A cidade de Enoque desceria para encontrar e abraçar o povo da Sião terrestre",
      "As tribos do norte se reunirão com os descendentes de Babilônia",
      "Os habitantes de Sião partirão para estabelecer uma cidade em Ur"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 7:63-64",
    "hint": "'E nos lançaremos ao seu pescoço e eles ao nosso, e nos beijaremos mutuamente... e ali será a minha morada'.",
    "explanation": "Uma das mais sublimes visões escatológicas de toda a revelação, antecipando a gloriosa união dos santos de todas as eras."
  },
  {
    "id": "pgv_012",
    "category": "pgv",
    "difficulty": 1,
    "question": "Onde o patriarca Abraão habitava no início de seu registro, antes de fugir por causa da idolatria dos sacerdotes pagãos de Faraó?",
    "options": [
      "Em Mênfis no Egito",
      "Em Ur dos Caldeus",
      "Em Hebrom",
      "Em Damasco"
    ],
    "correct": 1,
    "scriptureRef": "Abraão 1:1; 2:1",
    "hint": "Terra governada por governantes babilônicos/caldeus.",
    "explanation": "Abraão buscou a retidão e as bênçãos dos pais, recusando os deuses pagãos de seus progenitores em Ur."
  },
  {
    "id": "pgv_013",
    "category": "pgv",
    "difficulty": 3,
    "question": "Quais eram os nomes dos quatro deuses pagãos falsos cujos vasos e sacerdotes tentaram oferecer o jovem Abraão sobre o altar da colina de Potifar?",
    "options": [
      "Osíris, Ísis, Hórus e Anúbis",
      "Baal, Aserá, Dagom e Moloque",
      "Elquená, Libna, Mamacra e Coras",
      "Júpiter, Marte, Vênus e Apolo"
    ],
    "correct": 2,
    "scriptureRef": "Abraão 1:9, 13-17; Fac-símile 1",
    "hint": "Representados nas figuras sob a cama de sacrifício no Fac-símile nº 1 do Livro de Abraão.",
    "explanation": "O Senhor enviou Seu anjo, quebrou os altares daqueles deuses estranhos e libertou Abraão com vida."
  },
  {
    "id": "pgv_014",
    "category": "pgv",
    "difficulty": 4,
    "question": "Segundo Abraão 1:21-27, por que o primeiro Faraó do Egito, embora sendo um homem reto e justo que abençoou seu povo, não tinha o direito de possuir o sacerdócio?",
    "options": [
      "Ele rejeitara uma ordenação oferecida pelos sacerdotes de Ur",
      "Seu reino havia perdido a autoridade ao mudar a capital",
      "Segundo o relato, Faraó pertencia à linhagem que não tinha direito ao sacerdócio",
      "Ele precisava primeiro receber a autorização do próprio Abraão"
    ],
    "correct": 2,
    "scriptureRef": "Abraão 1:21-27",
    "hint": "Faraó procurou diligentemente imitar a ordem de sacerdócio patriarcal de Adão, mas não possuía a chave legítima de sucessão.",
    "explanation": "Abraão 1 esclarece a genealogia dos primeiros governantes do Egito preservada através da esposa de Cam, Egyptus."
  },
  {
    "id": "pgv_015",
    "category": "pgv",
    "difficulty": 2,
    "question": "Em Abraão 2:9-11, qual é a promessa universal e eterna concedida no grandioso 'Convênio Abraâmico'?",
    "options": [
      "Sua posteridade herdaria o governo político de todas as nações",
      "Somente seus descendentes nascidos em Canaã receberiam o evangelho",
      "Em sua semente, todas as famílias da Terra receberiam as bênçãos do evangelho",
      "As bênçãos seriam limitadas aos que preservassem sua língua original"
    ],
    "correct": 2,
    "scriptureRef": "Abraão 2:9-11",
    "hint": "Todo aquele que recebe o Evangelho é contado como semente de Abraão.",
    "explanation": "O Convênio Abraâmico é o alicerce pelo qual todo membro da Igreja torna-se participante do sacerdócio e da salvação de Cristo."
  },
  {
    "id": "pgv_016",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual é o nome da estrela que o Senhor mostrou a Abraão pelo Urim e Tumim, descrita como a maior e a mais próxima do trono de Deus?",
    "options": [
      "Kokaubeam",
      "Oliblis",
      "Cólobe",
      "Shineha"
    ],
    "correct": 2,
    "scriptureRef": "Abraão 3:2-3",
    "hint": "Um dia em Cólobe equivale a mil anos na Terra, segundo o cômputo dos tempos do Senhor.",
    "explanation": "Cólobe governa todas as estrelas criadas e simboliza a preeminência suprema de Jesus Cristo sobre toda a criação."
  },
  {
    "id": "pgv_017",
    "category": "pgv",
    "difficulty": 3,
    "question": "No vocabulário astronômico revelado a Abraão no capítulo 3, o que significam as palavras 'Shineha' e 'Kokob'?",
    "options": [
      "Shineha é o Sol, e Kokob é uma Estrela",
      "Shineha é a Lua, e Kokob é a Terra",
      "Shineha é o Céu, e Kokob é o Mar",
      "Shineha é o Dia, e Kokob é a Noite"
    ],
    "correct": 0,
    "scriptureRef": "Abraão 3:13",
    "hint": "E disse-me ele: Isto é Shineha, que é o sol; e disse-me: Kokob, que é estrela.",
    "explanation": "O Livro de Abraão preserva raízes semíticas e egípcias autênticas em suas designações celestes."
  },
  {
    "id": "pgv_018",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Abraão 3:22-23, o que o Senhor mostrou a Abraão antes que o mundo fosse organizado?",
    "options": [
      "Viu as inteligências nobres e grandes e soube que fora escolhido antes de nascer",
      "Os reis que governariam o Egito depois da morte de Abraão",
      "As famílias que sairiam de Jerusalém após o cativeiro babilônico",
      "Os povos que construiriam o templo durante o reinado de Salomão"
    ],
    "correct": 0,
    "scriptureRef": "Abraão 3:22-23",
    "hint": "O mais claro texto das Obras-Padrão sobre a pré-ordenação e existência pré-mortal da alma humana.",
    "explanation": "Esta passagem revela que os profetas e santos foram preparados e escolhidos na presença de Deus antes de nascerem na mortalidade."
  },
  {
    "id": "pgv_019",
    "category": "pgv",
    "difficulty": 2,
    "question": "Em Abraão 3:25, qual é a definição divina do propósito da criação da Terra como um teste probatório para os filhos de Deus?",
    "options": [
      "Conceder a vida eterna antes que fossem provados na mortalidade",
      "Permitir que escolhessem uma lei diferente para cada nação",
      "Demonstrar que a obediência seria possível sem livre-arbítrio",
      "Provar os filhos de Deus para ver se fariam tudo o que o Senhor lhes ordenasse"
    ],
    "correct": 3,
    "scriptureRef": "Abraão 3:25",
    "hint": "Aquele que guardar seu primeiro estado (a vida pré-mortal) receberá um corpo; e quem guardar o segundo estado (a vida mortal) terá glória eterna.",
    "explanation": "A vida mortal é um período probatório deliberado de crescimento, provação e exercício do arbítrio moral."
  },
  {
    "id": "pgv_020",
    "category": "pgv",
    "difficulty": 3,
    "question": "Quem foram os dois que responderam no conselho dos céus quando o Senhor perguntou: 'A quem enviarei?'?",
    "options": [
      "Jesus Cristo e Lúcifer",
      "Pedro e Paulo, os apóstolos",
      "Adão e Noé, os patriarcas",
      "Moisés e Elias, o profeta"
    ],
    "correct": 0,
    "scriptureRef": "Abraão 3:27-28",
    "hint": "E o Senhor disse: 'Enviarei o primeiro', provocando a fúria e rebelião de Lúcifer, que arrastou consigo a terça parte das hostes do céu.",
    "explanation": "A escolha voluntária de Cristo como o Redentor do mundo preservou a liberdade de escolha de todos os homens."
  },
  {
    "id": "pgv_021",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Abraão capítulos 4 e 5, como os criadores do céu e da terra são designados de maneira reverente e plural?",
    "options": [
      "Os Deuses",
      "Os mensageiros celestiais",
      "Os espíritos dos patriarcas",
      "Os filhos dos profetas"
    ],
    "correct": 0,
    "scriptureRef": "Abraão 4:1-3; 5:1",
    "hint": "Refletindo o conselho conjunto dos Deuses sob a liderança do Pai Celestial e de Jesus Cristo.",
    "explanation": "O relato de Abraão usa o termo plural hebraico Elohim ('Os Deuses'), enfatizando a ordem executiva divina da Criação."
  },
  {
    "id": "pgv_022",
    "category": "pgv",
    "difficulty": 4,
    "question": "No Fac-símile nº 1 do Livro de Abraão, o que a Figura 1 retrata na ilustração egípcia?",
    "options": [
      "O sacerdote de Elquená",
      "O anjo do Senhor",
      "Abraão sobre o altar",
      "A ave que representa Abraão"
    ],
    "correct": 1,
    "scriptureRef": "Abraão Fac-símile 1, Fig. 1",
    "hint": "Consulte a legenda da primeira figura, distinguindo-a da figura de Abraão.",
    "explanation": "Na legenda do Fac-símile 1, a figura 1 é o anjo do Senhor; Abraão aparece na figura 2."
  },
  {
    "id": "pgv_023",
    "category": "pgv",
    "difficulty": 4,
    "question": "No Fac-símile nº 2 de Abraão, qual figura representa a estrela Cólobe no centro do disco hipocéfalo recebendo poder de autoridade?",
    "options": [
      "A figura de número 7",
      "A figura de número 12",
      "A figura de número 5",
      "A figura de número 1"
    ],
    "correct": 3,
    "scriptureRef": "Abraão Fac-símile 2, Fig. 1",
    "hint": "Primeira na criação, mais próxima do centro celestial.",
    "explanation": "A Figura 1 central representa Cólobe como o primeiro e maior corpo criado governando as outras ordens."
  },
  {
    "id": "pgv_024",
    "category": "pgv",
    "difficulty": 4,
    "question": "No Fac-símile nº 3 do Livro de Abraão, o que Abraão é retratado fazendo na corte real do Egito?",
    "options": [
      "Sentado no trono, ensinava aos egípcios os princípios da astronomia",
      "Interpretando os sonhos dos servos de Faraó",
      "Recebendo de Faraó o governo sobre as cidades do Egito",
      "Conduzindo um sacrifício perante os sacerdotes reais"
    ],
    "correct": 0,
    "scriptureRef": "Abraão Fac-símile 3, Fig. 1",
    "hint": "Com o príncipe de Faraó e a rainha em pé ao seu lado ouvindo suas instruções de sabedoria celeste.",
    "explanation": "A cena cumpre o encargo divino de Abraão de ensinar a ciência celestial e os caminhos de Deus na corte egípcia."
  },
  {
    "id": "pgv_025",
    "category": "pgv",
    "difficulty": 1,
    "question": "Em que cidade e estado dos Estados Unidos o profeta Joseph Smith nasceu em 23 de dezembro de 1805?",
    "options": [
      "Harmony, na Pensilvânia",
      "Sharon, em Vermont",
      "Boston, em Massachusetts",
      "Palmyra, em Nova York"
    ],
    "correct": 1,
    "scriptureRef": "JS-H 1:3",
    "hint": "A família Smith mudou-se para Palmyra quando Joseph tinha cerca de dez anos de idade.",
    "explanation": "Joseph Smith nasceu em Sharon, Vermont, filho de Joseph Smith Sr. e Lucy Mack Smith."
  },
  {
    "id": "pgv_026",
    "category": "pgv",
    "difficulty": 1,
    "question": "Quantos irmãos e irmãs Joseph Smith tinha em sua família conforme enumerados em Joseph Smith - História 1:4?",
    "options": [
      "Oito irmãos e irmãs",
      "Dez irmãos e irmãs",
      "Doze irmãos e irmãs",
      "Sete irmãos e irmãs"
    ],
    "correct": 1,
    "scriptureRef": "JS-H 1:4",
    "hint": "Alvin, Hyrum, Joseph, Samuel Harrison, Ephraim, William, Don Carlos, Sophronia, Catherine e Lucy.",
    "explanation": "A família Smith era numerosa, unida, honrada e temente a Deus em suas devoções domésticas."
  },
  {
    "id": "pgv_027",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual passagem da Bíblia o jovem Joseph Smith leu em sua Bíblia em Manchester que o levou comovido a orar a Deus no Bosque Sagrado?",
    "options": [
      "Tiago 1:5",
      "Mateus 7:7",
      "João 3:16",
      "Provérbios 3:5"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:11-12; Tiago 1:5",
    "hint": "Ele declarou que nenhum trecho de escritura jamais penetrou com mais força no coração de um homem.",
    "explanation": "Tiago 1:5 foi a fagulha inspirada pelo Espírito que inaugurou a abertura da dispensação da plenitude dos tempos."
  },
  {
    "id": "pgv_028",
    "category": "pgv",
    "difficulty": 2,
    "question": "O que aconteceu com Joseph Smith imediatamente após ele se ajoelhar e começar a orar vocalmente na floresta na primavera de 1820?",
    "options": [
      "Foi envolvido por um poder de trevas que lhe prendeu a língua enquanto orava",
      "Uma voz o mandou voltar para casa antes de continuar",
      "Ele adormeceu e recebeu a resposta somente em sonho",
      "Uma tempestade o obrigou a buscar outro lugar para orar"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:15-16",
    "hint": "Ele reuniu todas as suas forças para clamar a Deus por libertação desse inimigo real do abismo.",
    "explanation": "O adversário tentou destruir o jovem profeta na iminência da abertura dos céus, sendo derrotado pela luz celestial."
  },
  {
    "id": "pgv_029",
    "category": "pgv",
    "difficulty": 1,
    "question": "O que o Pai Celestial disse a Joseph Smith na Primeira Visão ao apontar para o segundo Personagem glorioso ao Seu lado?",
    "options": [
      "Este é o anjo do convênio. Prepara-te para acompanhá-lo!",
      "Este é meu Filho Amado. Ouve-o!",
      "Este é o meu mensageiro. Segue-o até o monte!",
      "Este é o profeta prometido. Recebe seus registros!"
    ],
    "correct": 1,
    "scriptureRef": "JS-H 1:17",
    "hint": "Ele o chamou primeiro pelo seu próprio nome: 'Joseph!'.",
    "explanation": "O Pai introduziu o Salvador Jesus Cristo, que pessoalmente instruiu o jovem Joseph Smith sobre o estado do mundo."
  },
  {
    "id": "pgv_030",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual foi a resposta do Salvador quando Joseph perguntou qual de todas as seções religiosas estava certa para que ele se juntasse a ela?",
    "options": [
      "Que se filiasse à comunidade frequentada por sua mãe",
      "Que escolhesse a igreja com maior número de membros",
      "Que se unisse à congregação mais próxima de sua casa",
      "Não deveria filiar-se a nenhuma delas, pois ensinavam mandamentos de homens"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:19",
    "hint": "Eles se aproximam de mim com a boca e com os lábios me honram, mas o seu coração está longe de mim.",
    "explanation": "A resposta divina atestou a realidade da Grande Apostasia e a indispensável necessidade de restaurar o evangelho puro de Cristo."
  },
  {
    "id": "pgv_031",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual anjo apareceu no quarto de Joseph Smith na noite de 21 de setembro de 1823, anunciando a existência das placas de ouro e das pedras do Urim e Tumim?",
    "options": [
      "O Apóstolo Pedro",
      "O Anjo Gabriel",
      "O Arcanjo Miguel",
      "O Anjo Morôni"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:30-34",
    "hint": "Ele apareceu três vezes durante aquela mesma noite repetindo as mesmíssimas instruções e profecias sagradas.",
    "explanation": "Morôni declarou que Deus tinha uma obra para Joseph realizar e que seu nome seria conhecido para o bem e para o mal em todas as nações."
  },
  {
    "id": "pgv_032",
    "category": "pgv",
    "difficulty": 3,
    "question": "Quantos anos consecutivos Joseph Smith teve que comparecer anualmente no dia 22 de setembro no Monte Cumora para receber instruções do anjo antes de poder levar as placas para casa?",
    "options": [
      "Dez anos consecutivos",
      "Dois anos consecutivos",
      "Sete anos consecutivos",
      "Quatro anos consecutivos"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:53-54",
    "hint": "Ele finalmente recebeu as placas de ouro, o Urim e Tumim e o peitoral em 22 de setembro de 1827.",
    "explanation": "Durante quatro anos de tutoria angélica no monte Cumora, Joseph amadureceu espiritualmente para guardar os anais sagrados com integridade absoluta."
  },
  {
    "id": "pgv_033",
    "category": "pgv",
    "difficulty": 3,
    "question": "Qual professor erudito da Universidade de Columbia em Nova York rasgou seu próprio certificado de autenticidade dos caracteres quando Martin Harris disse que um anjo havia revelado as placas de ouro?",
    "options": [
      "Professor George Bush",
      "Professor Charles Anthon",
      "Dr. John Clark",
      "Dr. Samuel L. Mitchill"
    ],
    "correct": 1,
    "scriptureRef": "JS-H 1:64-65",
    "hint": "Ele disse com arrogância: 'Não posso ler um livro selado', cumprindo textualmente a profecia de Isaías 29:11-12.",
    "explanation": "O incidente com o Professor Anthon fortaleceu imensamente o testemunho de Martin Harris e comprovou a presciência das profecias bíblicas."
  },
  {
    "id": "pgv_034",
    "category": "pgv",
    "difficulty": 2,
    "question": "Quem serviu como escriba principal e incansável de Joseph Smith durante a maior parte da tradução do Livro de Mórmon em Harmonia, de abril a junho de 1829?",
    "options": [
      "Oliver Cowdery",
      "Martin Harris",
      "Emma Smith",
      "David Whitmer"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:67-68",
    "hint": "Um jovem professor primário que fora inspirado por Deus a viajar até a casa de Joseph em Harmonia.",
    "explanation": "Oliver escreveu o texto sagrado que saía da boca do profeta dia após dia sem interrupção."
  },
  {
    "id": "pgv_035",
    "category": "pgv",
    "difficulty": 2,
    "question": "Em Joseph Smith - Mateus 1:22, o que o Salvador profetiza sobre os falsos cristos e falsos profetas dos últimos dias?",
    "options": [
      "Seriam reconhecidos de imediato por todos os que lessem a lei",
      "Só poderiam influenciar quem nunca tivesse ouvido o evangelho",
      "Deixariam de pregar assim que surgissem os primeiros sinais do fim",
      "Fariam sinais capazes de enganar até os eleitos, se possível"
    ],
    "correct": 3,
    "scriptureRef": "JS-M 1:22",
    "hint": "Uma advertência solene para que os santos tesourem a palavra de Deus a fim de não serem enganados pelas astúcias do mundo.",
    "explanation": "Apenas aqueles que guardam seus convênios e dão ouvidos ao Espírito Santo discernem os ardis enganadores do adversário."
  },
  {
    "id": "pgv_036",
    "category": "pgv",
    "difficulty": 1,
    "question": "A qual proeminente jornalista de Chicago Joseph Smith enviou a célebre carta de 1842 contendo a história da Igreja e as treze Regras de Fé?",
    "options": [
      "James Gordon Bennett",
      "Horace Greeley",
      "John Wentworth",
      "Thomas Sharp"
    ],
    "correct": 2,
    "scriptureRef": "A Carta Wentworth (1842)",
    "hint": "Ele era editor do jornal Chicago Democrat e pedira um resumo conciso das origens e crenças dos santos dos últimos dias.",
    "explanation": "A Carta Wentworth gerou o documento imorredouro das 13 Regras de Fé e o célebre Estandarte da Verdade."
  },
  {
    "id": "pgv_037",
    "category": "pgv",
    "difficulty": 1,
    "question": "Qual princípio de responsabilidade moral é ensinado na Segunda Regra de Fé?",
    "options": [
      "Cada um herda a culpa de Adão até oferecer um sacrifício pessoal",
      "Cada um responde por seus pecados, não pela transgressão de Adão",
      "A responsabilidade pelos pecados pertence à família inteira",
      "Somente os pecados cometidos depois do batismo serão julgados"
    ],
    "correct": 1,
    "scriptureRef": "Regra de Fé 2",
    "hint": "Rejeita de forma categórica o dogma tradicional do 'pecado original herdado' que condena criancinhas inocentes.",
    "explanation": "A Segunda Regra de Fé proclama a responsabilidade pessoal individual de cada filho de Deus por suas próprias escolhas morais."
  },
  {
    "id": "pgv_038",
    "category": "pgv",
    "difficulty": 1,
    "question": "Qual é a declaração sublime da Terceira Regra de Fé sobre o alcance salvador de Jesus Cristo?",
    "options": [
      "A salvação se limita aos descendentes literais da casa de Israel",
      "A salvação depende primeiro do conhecimento de todas as escrituras",
      "A Expiação torna possível a salvação mediante as leis do evangelho",
      "A Expiação salva sem relação com as leis e ordenanças do evangelho"
    ],
    "correct": 2,
    "scriptureRef": "Regra de Fé 3",
    "hint": "Une a graça universal e infinita da Expiação com a exigência divina de fé ativa e obediência aos mandamentos.",
    "explanation": "A Expiação estende redenção incondicional da morte física a todos e exaltação condicional aos obedientes."
  },
  {
    "id": "pgv_039",
    "category": "pgv",
    "difficulty": 1,
    "question": "Quais são os quatro primeiros princípios e ordenanças do Evangelho enumerados com precisão na Quarta Regra de Fé?",
    "options": [
      "Fé, jejum, consagração e ordenação ao sacerdócio",
      "Batismo, oração, caridade e casamento no templo",
      "Fé em Cristo, arrependimento, batismo e imposição de mãos para o Espírito Santo",
      "Arrependimento, dízimo, sacramento e bênção patriarcal"
    ],
    "correct": 2,
    "scriptureRef": "Regra de Fé 4",
    "hint": "O caminho estreito e apertado de entrada no reino de Deus delineado por Pedro no Pentecostes e por Néfi em 2 Néfi 31.",
    "explanation": "A Quarta Regra de Fé sintetiza a doutrina elementar e salvadora da porta de entrada no convênio cristão."
  },
  {
    "id": "pgv_040",
    "category": "pgv",
    "difficulty": 2,
    "question": "Segundo a Quinta Regra de Fé, como um homem deve ser chamado por Deus para pregar o Evangelho e administrar suas santas ordenanças?",
    "options": [
      "Por profecia e imposição de mãos de pessoas que possuam autoridade para fazê-lo",
      "Por estudo e aprovação pública dos membros da congregação",
      "Por desejo pessoal e reconhecimento de sua capacidade de ensinar",
      "Por herança familiar e preparação nos costumes dos antepassados"
    ],
    "correct": 0,
    "scriptureRef": "Regra de Fé 5",
    "hint": "Seguindo o padrão eterno de Hebreus 5:4: 'E ninguém toma para si esta honra, senão o que é chamado por Deus, como Arão'.",
    "explanation": "A autoridade do sacerdócio provém de revelação divina transmitida por sucessão legítima sob a imposição física de mãos."
  },
  {
    "id": "pgv_041",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual é a organização eclesiástica que a Sexta Regra de Fé declara existir na Igreja restaurada, igual àquela que existia na Igreja Primitiva do Novo Testamento?",
    "options": [
      "Patriarcas, reis, príncipes, conselheiros e escribas reais",
      "Pastores independentes, leitores, cantores e administradores",
      "A organização com apóstolos, profetas, pastores, mestres e evangelistas",
      "Sacerdotes levitas, escribas, juízes e chefes de sinagoga"
    ],
    "correct": 2,
    "scriptureRef": "Regra de Fé 6; Efésios 4:11",
    "hint": "Citando a mesma estrutura ministerial revelada por Paulo em Efésios 4:11 para o aperfeiçoamento dos santos.",
    "explanation": "A Igreja restaurada de Jesus Cristo possui os mesmíssimos ofícios e ministérios instituídos pelo Salvador no meridiano dos tempos."
  },
  {
    "id": "pgv_042",
    "category": "pgv",
    "difficulty": 2,
    "question": "Quais dons espirituais do Espírito Santo são afirmados na Sétima Regra de Fé?",
    "options": [
      "Memória, eloquência, prudência, riqueza e autoridade civil",
      "Línguas, profecia, revelação, visões, cura e interpretação",
      "Pregação, administração, construção, escrita e comércio",
      "Sacrifício, circuncisão, purificação, jejum e peregrinação"
    ],
    "correct": 1,
    "scriptureRef": "Regra de Fé 7",
    "hint": "Os mesmos dons operantes nos dias dos apóstolos em 1 Coríntios 12 e em Morôni 10.",
    "explanation": "A Sétima Regra de Fé testifica que os dons sobrenaturais e espirituais acompanham os crentes em todos os séculos."
  },
  {
    "id": "pgv_043",
    "category": "pgv",
    "difficulty": 2,
    "question": "Como a Oitava Regra de Fé se expressa a respeito da Bíblia Sagrada e do Livro de Mórmon como palavras de Deus?",
    "options": [
      "A Bíblia é palavra de Deus apenas nas passagens repetidas no Livro de Mórmon",
      "O Livro de Mórmon torna desnecessária a leitura dos registros da Bíblia",
      "A Bíblia, corretamente traduzida, e o Livro de Mórmon são palavra de Deus",
      "A Bíblia e o Livro de Mórmon valem somente como relatos históricos antigos"
    ],
    "correct": 2,
    "scriptureRef": "Regra de Fé 8",
    "hint": "Reconhece o valor inestimável da Bíblia e as falhas históricas de tradução e cópias humanas ao longo dos milênios.",
    "explanation": "A Igreja apoia e reverencia a Bíblia Sagrada, ao mesmo tempo em que reconhece no Livro de Mórmon a pureza virginal de sua tradução pelo dom de Deus."
  },
  {
    "id": "pgv_044",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual princípio fundamental de teologia dinâmica e aberta é proclamado na Nona Regra de Fé?",
    "options": [
      "Deus revelou tudo antes do encerramento do Novo Testamento",
      "Crer em tudo o que Deus revelou, revela agora e ainda revelará a respeito de Seu reino",
      "Deus revela apenas explicações que repetem literalmente a Bíblia",
      "Deus só voltará a revelar depois do início do reinado milenar"
    ],
    "correct": 1,
    "scriptureRef": "Regra de Fé 9",
    "hint": "O princípio inabalável da revelação contínua que guia a Igreja por meio de profetas vivos.",
    "explanation": "Deus continua falando à humanidade, adaptando Suas instruções aos desafios e necessidades de cada geração."
  },
  {
    "id": "pgv_045",
    "category": "pgv",
    "difficulty": 3,
    "question": "Quais três grandes profecias escatológicas são proclamadas na Décima Regra de Fé?",
    "options": [
      "Coligação simbólica, Sião na Europa e governo de um conselho humano",
      "Coligação de Israel, Sião na América e reinado pessoal de Cristo",
      "Retorno a Jerusalém, Sião no Egito e permanência da Terra sem renovação",
      "Dispersão de Israel, Sião na Ásia e reinado dos antigos patriarcas"
    ],
    "correct": 1,
    "scriptureRef": "Regra de Fé 10",
    "hint": "A Terra receberá sua glória paradisíaca no glorioso milênio.",
    "explanation": "A Décima Regra de Fé delineia o destino milenar triunfal da Terra sob o governo pessoal de Jesus Cristo."
  },
  {
    "id": "pgv_046",
    "category": "pgv",
    "difficulty": 2,
    "question": "Em que termos nobres a Décima Primeira Regra de Fé estabelece a santidade irrestrita da liberdade religiosa e de consciência para todos os seres humanos?",
    "options": [
      "Reivindicar liberdade de consciência e conceder a todos a mesma liberdade de adoração",
      "Liberdade de adoração somente para quem aceita a Bíblia",
      "Liberdade para escolher entre as religiões autorizadas pela Igreja",
      "Liberdade religiosa condicionada à aprovação dos ministros locais"
    ],
    "correct": 0,
    "scriptureRef": "Regra de Fé 11",
    "hint": "Um dos mais nobres manifestos de tolerância, respeito mútuo e dignidade humana já redigidos.",
    "explanation": "A Décima Primeira Regra de Fé consagra a liberdade de consciência como um direito inalienável outorgado pelo Criador."
  },
  {
    "id": "pgv_047",
    "category": "pgv",
    "difficulty": 2,
    "question": "Qual é o posicionamento de cidadania e lealdade cívica declarado na Décima Segunda Regra de Fé?",
    "options": [
      "Submeter-se às autoridades civis, obedecendo, honrando e mantendo a lei",
      "Afastar os membros da participação em assuntos do governo",
      "Substituir os magistrados civis por conselhos eclesiásticos",
      "Obedecer apenas às leis aprovadas pelos líderes religiosos"
    ],
    "correct": 0,
    "scriptureRef": "Regra de Fé 12",
    "hint": "Os membros da Igreja são incentivados a serem cidadãos exemplares, patriotas e guardiões da lei em todos os países onde vivem.",
    "explanation": "A Décima Segunda Regra de Fé estabelece a cidadania responsável, o respeito à ordem pública e a preservação do Estado de Direito."
  },
  {
    "id": "pgv_048",
    "category": "pgv",
    "difficulty": 1,
    "question": "Como se inicia o nobre padrão de vida moral e ético cristão da Décima Terceira Regra de Fé?",
    "options": [
      "Ser honestos, verdadeiros, castos, benevolentes e virtuosos",
      "Ser fiéis, silenciosos, independentes, prósperos e reconhecidos",
      "Ser estudiosos, eloquentes, respeitados, fortes e disciplinados",
      "Ser prudentes, reservados, austeros, influentes e instruídos"
    ],
    "correct": 0,
    "scriptureRef": "Regra de Fé 13",
    "hint": "Citando o apóstolo Paulo aos Filipenses: 'Se houver qualquer coisa virtuosa, amável, de boa fama ou louvável, nós a buscaremos'.",
    "explanation": "A Décima Terceira Regra de Fé coroa as declarações de crença dos santos com a busca incansável por tudo o que é nobre, belo e divino."
  },
  {
    "id": "pgv_049",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual célebre declaração profética, conhecida como 'O Estandarte da Verdade', foi inserida por Joseph Smith na mesma Carta Wentworth de 1842 que continha as Regras de Fé?",
    "options": [
      "O estandarte foi erguido, e a verdade avançará por toda a Terra apesar da oposição",
      "O crescimento da Igreja dependerá da aprovação dos reis da Terra",
      "A obra só avançará depois que terminarem todas as perseguições",
      "A pregação permanecerá restrita aos povos do continente americano"
    ],
    "correct": 0,
    "scriptureRef": "A Carta Wentworth (1842)",
    "hint": "Até que os propósitos de Deus sejam cumpridos e o Grande Jeová diga que a obra está concluída.",
    "explanation": "O Estandarte da Verdade é uma das mais inspiradoras e audaciosas declarações de triunfo profético da história universal."
  },
  {
    "id": "pgv_050",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em que ano a Pérola de Grande Valor foi compilada e publicada pela primeira vez em Liverpool, Inglaterra, pelo Élder Franklin D. Richards para os santos britânicos?",
    "options": [
      "1830",
      "1851",
      "1844",
      "1880"
    ],
    "correct": 1,
    "scriptureRef": "Introdução da Pérola de Grande Valor",
    "hint": "Mais tarde, na Conferência Geral de 10 de outubro de 1880, o livro foi formalmente aceito como uma das quatro Obras-Padrão da Igreja.",
    "explanation": "Franklin D. Richards compilou os preciosos escritos de Joseph Smith para fortalecer os santos na Inglaterra, tornando-se canônico em 1880."
  },
  {
    "id": "pgv_051",
    "category": "pgv",
    "difficulty": 3,
    "question": "Que característica de Deus é afirmada em Moisés 1:3?",
    "options": [
      "Seu nome só seria revelado depois da libertação de Israel",
      "Deus é Todo-Poderoso e infinito, não tendo princípio de dias nem fim de anos",
      "Seu domínio começou quando organizou a primeira terra",
      "Suas obras se limitam aos mundos que Moisés pôde observar"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 1:3",
    "hint": "Deus revela Sua natureza infinita e eterna a Moisés antes de mostrar-lhe as visões cósmicas.",
    "explanation": "Esta sublime passagem amplia a perspectiva humana finita para contemplar a eternidade insondável de Deus."
  },
  {
    "id": "pgv_052",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que Moisés viu em Moisés 1:27-28 quando a glória do Senhor descansou sobre ele pela segunda vez após a fuga de Satanás?",
    "options": [
      "Viu toda a Terra e cada um de seus habitantes pelo poder do Espírito de Deus",
      "Somente o Egito e as gerações dos filhos de Israel",
      "A cidade de Jerusalém e os sacerdotes de seu futuro templo",
      "A terra de Canaã e as fronteiras das tribos que a herdariam"
    ],
    "correct": 0,
    "scriptureRef": "Moisés 1:27-28",
    "hint": "E ele contemplou também muitas terras; e cada terra chamava-se terra, e havia habitantes sobre sua face.",
    "explanation": "O Espírito de Deus transfigurou Moisés de modo que sua mente finita pôde contemplar a totalidade dos filhos da Terra."
  },
  {
    "id": "pgv_053",
    "category": "pgv",
    "difficulty": 4,
    "question": "O que o Senhor explicou a Moisés em Moisés 1:35 sobre os muitos outros mundos que foram criados e que já passaram?",
    "options": [
      "Mundos passam, outros permanecem, e Deus conhece todos",
      "Só os mundos vistos por Moisés tinham sido organizados até então",
      "Os mundos que passam deixam de ser conhecidos até por Deus",
      "Todos os mundos terminam ao mesmo tempo que esta Terra"
    ],
    "correct": 0,
    "scriptureRef": "Moisés 1:35",
    "hint": "Assim como uma terra passa e seus céus, assim também outra vem.",
    "explanation": "Esta gloriosa revelação desvenda a imensidão do cosmos e a presença constante do amor e governo de Deus sobre mundos sem número."
  },
  {
    "id": "pgv_054",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Moisés 3:5, que doutrina essencial e consoladora da Criação é revelada com clareza cristalina?",
    "options": [
      "A criação natural não teve relação com a organização espiritual",
      "A criação espiritual se limitou aos seres humanos e aos anjos",
      "Todas as coisas foram criadas espiritualmente antes de existirem naturalmente na Terra",
      "A criação espiritual ocorreu somente depois da criação física"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 3:5",
    "hint": "'Pois eu, o Senhor Deus, criei espiritualmente todas as coisas de que falei, antes que existissem naturalmente...'.",
    "explanation": "A revelação ensina que toda planta, animal e ser humano teve uma prévia existência e organização espiritual antes de sua incorporação física."
  },
  {
    "id": "pgv_055",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Moisés 5:10-11, o que Adão e Eva exclamaram e cantaram com alegria espiritual após a Queda e ao receberem as instruções do anjo?",
    "options": [
      "Decidiram regressar ao jardim antes de ter filhos",
      "Concluíram que não precisavam mais receber mandamentos",
      "Celebraram os olhos abertos, a posteridade, o conhecimento e a alegria da redenção",
      "Lamentaram não haver mais possibilidade de voltar a Deus"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 5:10-11",
    "hint": "Um dos cânticos de louvor mais profundos da teologia da Restauração, demonstrando que a Queda foi um passo progressivo glorioso.",
    "explanation": "Adão e Eva compreenderam com sabedoria sublime que sem a Queda não haveria família, nem redenção, nem a vida eterna em Cristo."
  },
  {
    "id": "pgv_056",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Moisés 6:51-68, qual é o relato impressionante do primeiro batismo de Adão nas águas?",
    "options": [
      "Ele entrou sozinho na água antes de receber qualquer instrução",
      "O Espírito levou Adão à água, ele foi imerso e recebeu o Espírito Santo",
      "Um de seus filhos o aspergiu diante de toda a família",
      "Um anjo derramou água sobre ele junto ao altar"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 6:64-66",
    "hint": "E ouviu uma voz vinda do céu dizendo: 'Tu és batizado com fogo e com o Espírito Santo... Eis que és um em mim, um filho de Deus'.",
    "explanation": "O relato de Moisés comprova que o evangelho com todas as suas ordenanças salvadoras por imersão foi revelado desde os dias de Adão."
  },
  {
    "id": "pgv_057",
    "category": "pgv",
    "difficulty": 4,
    "question": "O que aconteceu com montanhas e rios quando Enoque falou a palavra do Senhor em Moisés 7:13?",
    "options": [
      "O mar se abriu e o povo atravessou a pé enxuto",
      "O sol parou e a lua permaneceu imóvel sobre o vale",
      "Os muros caíram e as portas da cidade foram queimadas",
      "As montanhas fugiram e os rios mudaram de curso"
    ],
    "correct": 3,
    "scriptureRef": "Moisés 7:13",
    "hint": "O relato descreve mudanças na paisagem diante da palavra do profeta.",
    "explanation": "Moisés 7:13 relata que as montanhas fugiram e os rios de água se desviaram de seu curso."
  },
  {
    "id": "pgv_058",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Moisés 7:48, quem clamou em pranto dizendo: 'Ai de mim, mãe dos homens; estou aflita, estou cansada por causa da iniquidade de meus filhos! Quando descansarei e serei limpa da imundície que saiu de mim?'?",
    "options": [
      "A mãe Eva",
      "A esposa de Noé",
      "A cidade de Sião",
      "A própria Terra"
    ],
    "correct": 3,
    "scriptureRef": "Moisés 7:48",
    "hint": "Enoque ouviu a própria mãe Terra gemer pelas transgressões dos homens sobre a sua face.",
    "explanation": "A Terra é uma criação viva que aspira ao seu batismo de água e fogo e ao seu descanso milenar na presença de seu Criador."
  },
  {
    "id": "pgv_059",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual patriarca antediluviano em Moisés 8:1-3 profetizou que de seus lombos brotariam todas as nações da Terra através de seu neto Noé após o dilúvio?",
    "options": [
      "Matusalém",
      "Lameque",
      "Jarede",
      "Mahalaleel"
    ],
    "correct": 0,
    "scriptureRef": "Moisés 8:2-3",
    "hint": "O homem de maior longevidade física registrado nas sagradas escrituras.",
    "explanation": "O Senhor fez convênio com Matusalém de que sua posteridade seria preservada nas águas do grande dilúvio através da arca de Noé."
  },
  {
    "id": "pgv_060",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Abraão 1:18, qual promessa o Senhor faz pessoalmente a Abraão enquanto quebrava os altares pagãos da colina de Potifar?",
    "options": [
      "Estabelecê-lo como rei de todas as cidades dos caldeus",
      "Devolvê-lo à casa paterna sem necessidade de partir de Ur",
      "Torná-lo governante dos sacerdotes que serviam a Faraó",
      "Deus o conduziria pela mão e poria sobre ele Seu nome, o sacerdócio de seus pais"
    ],
    "correct": 3,
    "scriptureRef": "Abraão 1:18",
    "hint": "E meu poder estará sobre ti; como foi com Noé, assim será contigo.",
    "explanation": "O Senhor confirmou o direito de primogenitura sacerdotal sobre Abraão, tornando-o o grande patriarca dos convênios de Deus."
  },
  {
    "id": "pgv_061",
    "category": "pgv",
    "difficulty": 4,
    "question": "Segundo a legenda da figura 5 do Fac-símile 2, que astro é chamado de Enis-go-on-dos?",
    "options": [
      "A Terra",
      "O Sol",
      "A Lua",
      "A estrela Cólobe"
    ],
    "correct": 1,
    "scriptureRef": "Abraão Fac-símile 2, Fig. 5",
    "hint": "A legenda o identifica entre os astros governantes.",
    "explanation": "A explicação da figura 5 associa Enis-go-on-dos ao Sol."
  },
  {
    "id": "pgv_062",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Abraão Fac-símile nº 2, Fig. 6, o que as quatro figuras representam na astronomia do Livro de Abraão?",
    "options": [
      "As quatro partes da Terra",
      "Os quatro rios do jardim do Éden",
      "As quatro gerações anteriores a Noé",
      "As quatro estações do ano"
    ],
    "correct": 0,
    "scriptureRef": "Abraão Fac-símile 2, Fig. 6",
    "hint": "Representadas frequentemente na egiptologia pelos quatro filhos de Hórus.",
    "explanation": "Joseph Smith interpretou corretamente essas quatro figuras como simbolizando os quatro quadrantes ou cantos geográficos da Terra."
  },
  {
    "id": "pgv_063",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual é a estrela ou planeta que 'governa todas aquelas que pertencem à mesma ordem daquela em que te encontras' segundo Abraão 3:9?",
    "options": [
      "Shineha",
      "Oliblis",
      "Kokaubeam",
      "Cólobe"
    ],
    "correct": 3,
    "scriptureRef": "Abraão 3:9",
    "hint": "O Senhor explicou que ela é a maior de todas as Kokaubeam que ele vira.",
    "explanation": "Cólobe é a representação física suprema do poder, majestade e luz do Salvador Jesus Cristo sobre o universo."
  },
  {
    "id": "pgv_064",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Abraão 3:18-19, como o Senhor usa a astronomia e as grandezas das estrelas como metáfora para explicar a preeminência de Deus sobre os espíritos humanos?",
    "options": [
      "Todos os espíritos possuem exatamente a mesma inteligência",
      "A inteligência dos espíritos depende da distância entre as estrelas",
      "Há diferenças de inteligência entre os espíritos, e Deus é mais inteligente que todos",
      "Cada espírito recebe a inteligência de um astro quando nasce"
    ],
    "correct": 2,
    "scriptureRef": "Abraão 3:18-19",
    "hint": "'Eu sou o Senhor teu Deus, sou mais inteligente do que todos eles'.",
    "explanation": "Esta sublime analogia cósmica demonstra a transcendência infinita da mente, luz e santidade de Deus sobre todas as criaturas."
  },
  {
    "id": "pgv_065",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que o Livro de Abraão revela sobre a natureza do Espírito que desceu sobre a face das águas na Criação em Abraão 4:2?",
    "options": [
      "O espírito dos patriarcas",
      "O espírito dos governantes",
      "O espírito dos mensageiros",
      "O Espírito dos Deuses"
    ],
    "correct": 3,
    "scriptureRef": "Abraão 4:2",
    "hint": "Em perfeito alinhamento com a obra conjunta e harmoniosa dos Deuses na organização do cosmos.",
    "explanation": "A criação no Livro de Abraão retrata a obra coordenada e deliberada dos Deuses ao introduzirem a luz e a vida nos mundos."
  },
  {
    "id": "pgv_066",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Abraão 5:13, qual era a medida de tempo computada para o homem antes de sua Queda no Jardim do Éden?",
    "options": [
      "O tempo da Terra, medido pelo movimento do Sol",
      "O tempo do Senhor, segundo Cólobe, antes de se assinalar ao homem seu próprio cômputo",
      "O tempo dos meses, segundo as fases da Lua",
      "O tempo de Abraão, segundo o calendário dos caldeus"
    ],
    "correct": 1,
    "scriptureRef": "Abraão 5:13",
    "hint": "Explicando por que Adão viveu quase mil anos terrenos após comer do fruto antes de morrer espiritualmente e fisicamente no mesmo 'dia' do Senhor.",
    "explanation": "Esta revelação esclarece a harmonia temporal entre Gênesis e a longevidade milenar dos primeiros patriarcas."
  },
  {
    "id": "pgv_067",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Joseph Smith - História 1:28, que esclarecimento humilde e cândido o Profeta faz sobre suas imperfeições humanas na juventude entre 1820 e 1823?",
    "options": [
      "Atribuiu todas as suas faltas à oposição dos ministros religiosos",
      "Declarou que a Primeira Visão eliminara qualquer fraqueza humana",
      "Afirmou ter sido perfeito em todas as decisões desde a infância",
      "Reconheceu fraquezas juvenis, sem pecados graves ou maliciosos"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:28",
    "hint": "Ele admitiu sua disposição alegre e convivência jovial, lamentando ter sido levado por vezes a leviandades.",
    "explanation": "A sincera honestidade de Joseph Smith atesta sua humanidade autêntica, desprovida de qualquer pretensão hipócrita de infalibilidade pessoal."
  },
  {
    "id": "pgv_068",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual profecia do Velho Testamento o Anjo Morôni citou a Joseph Smith em 1823 com pequenas variações significativas, afirmando que ela estava prestes a se cumprir?",
    "options": [
      "Eclesiastes, capítulos 11 e 12",
      "Provérbios, capítulos 10 e 11",
      "Gênesis, capítulos 1 e 2",
      "Malaquias, capítulos 3 e 4"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:36-39",
    "hint": "Ele disse: 'Eis que eu vos revelarei o Sacerdócio, pela mão de Elias, o profeta, antes que venha o grande e terrível dia do Senhor'.",
    "explanation": "A citação modificada de Malaquias ressaltou a natureza de convênio patriarcal e promessas familiares inerentes ao selamento."
  },
  {
    "id": "pgv_069",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual passagem do livro de Joel o Anjo Morôni também citou a Joseph Smith na madrugada de 21 de setembro de 1823?",
    "options": [
      "Joel 2:28–32",
      "Joel 1:13–16",
      "Joel 3:9–12",
      "Joel 1:1–5"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:41",
    "hint": "Morôni disse que essa profecia ainda não estava cumprida, mas que se cumpriria em breve.",
    "explanation": "A profecia de Joel sinalizava a restauração do poder profético e a abundância de revelação espiritual nos últimos dias."
  },
  {
    "id": "pgv_070",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que aconteceu com Joseph Smith no dia seguinte à visita tríplice de Morôni quando tentava trabalhar na colheita com seu pai?",
    "options": [
      "Voltou ao quarto para escrever tudo antes de falar com o pai",
      "Foi diretamente ao monte sem conversar com ninguém",
      "Adormeceu junto às ferramentas antes de começar a colheita",
      "Desmaiou ao tentar atravessar uma cerca"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:48",
    "hint": "Seu pai percebeu sua palidez e mandou que fosse para casa descansar.",
    "explanation": "Enquanto jazia desfalecido junto à cerca, o Anjo Morôni apareceu pela quarta vez ordenando que contasse tudo ao seu pai."
  },
  {
    "id": "pgv_071",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que o pai de Joseph Smith (Joseph Smith Sr.) disse ao filho após ouvir o relato minucioso das visões angélicas de Morôni?",
    "options": [
      "Reconheceu que a mensagem vinha de Deus e aconselhou-o a cumprir a ordem recebida",
      "Que guardasse o relato até a próxima visita do mensageiro",
      "Que só fosse ao monte depois de conversar com toda a família",
      "Que deveria esperar uma confirmação dos ministros locais"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:50",
    "hint": "Um testemunho comovente de fé paternal imediata na vocação profética de seu filho.",
    "explanation": "Joseph Smith Sr. reconheceu a mão divina nas visões do filho e apoiou com fidelidade incondicional a sua missão sagrada."
  },
  {
    "id": "pgv_072",
    "category": "pgv",
    "difficulty": 4,
    "question": "Onde exatamente as placas de ouro, o peitoral e as pedras do Urim e Tumim estavam guardadas no Monte Cumora quando Joseph as viu pela primeira vez?",
    "options": [
      "Numa cavidade aberta na rocha perto da base da colina",
      "Num baú de madeira protegido por uma chapa de metal",
      "Numa caixa feita de pedras, sob uma grande pedra arredondada no monte",
      "Num recipiente de barro enterrado junto a uma árvore"
    ],
    "correct": 2,
    "scriptureRef": "JS-H 1:51-52",
    "hint": "Joseph usou uma alavanca para erguer a pedra da tampa e contemplou os artefatos sagrados exatamente como o anjo descrevera.",
    "explanation": "A caixa de pedra havia sido preparada com cimento e pedras por Morôni séculos antes para preservar os anais até o tempo devido."
  },
  {
    "id": "pgv_073",
    "category": "pgv",
    "difficulty": 4,
    "question": "O que o Anjo Morôni advertiu solenemente a Joseph Smith que aconteceria se ele fosse descuidado ou negligente na guarda das placas após recebê-las em 1827?",
    "options": [
      "Perderia as placas sem qualquer responsabilidade pelo ocorrido",
      "Teria de comprá-las novamente pelo valor do ouro que continham",
      "Receberia outro registro para traduzir caso perdesse o primeiro",
      "Seria cortado se negligente; seriam protegidas se cuidasse delas"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:59",
    "hint": "O anjo cumpriu sua promessa e quando a tradução foi concluída, o mensageiro recolheu as placas sob sua guarda.",
    "explanation": "Apesar de inúmeras tentativas de roubo armadas por vizinhos gananciosos, as placas foram preservadas pela providência divina."
  },
  {
    "id": "pgv_074",
    "category": "pgv",
    "difficulty": 3,
    "question": "Qual foi a primeira coisa extraordinária que aconteceu com Joseph Smith e Oliver Cowdery logo após serem batizados um pelo outro nas águas do Susquehanna em 1829?",
    "options": [
      "Foram conduzidos ao monte para receber outro conjunto de placas",
      "Receberam imediatamente as chaves do selamento das famílias",
      "Ouviram a ordem de organizar a Igreja naquela mesma tarde",
      "Receberam o Espírito, profetizaram e tiveram maior compreensão das escrituras"
    ],
    "correct": 3,
    "scriptureRef": "JS-H 1:73-74",
    "hint": "Nossas mentes foram iluminadas e começamos a compreender as escrituras como nunca antes.",
    "explanation": "O batismo legítimo abriu imediatamente os canais de revelação profética e iluminação espiritual aos dois élderes da Restauração."
  },
  {
    "id": "pgv_075",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual das seguintes frases NÃO faz parte da Décima Terceira Regra de Fé?",
    "options": [
      "'Cremos que todas as igrejas serão unificadas pelos reis da terra'",
      "'Cremos em ser honestos, verdadeiros, castos, benevolentes, virtuosos'",
      "'Temos suportado muitas coisas e confiamos na capacidade de tudo suportar'",
      "'Se houver qualquer coisa virtuosa, amável, de boa fama ou louvável, nós a buscaremos'"
    ],
    "correct": 0,
    "scriptureRef": "Regra de Fé 13",
    "hint": "A Décima Terceira Regra de Fé segue de perto o conselho de Paulo em Filipenses 4:8.",
    "explanation": "A Regra de Fé 13 é um hino à integridade pessoal, bondade universal e busca pelo que é virtuoso e nobre."
  },
  {
    "id": "pgv_076",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Moisés 2:26-27, quem Deus consulta na criação do homem dizendo: 'Façamos o homem à nossa imagem, segundo nossa semelhança'?",
    "options": [
      "Os mensageiros das hostes celestes",
      "Os querubins que guardariam o jardim",
      "Seu Filho Unigênito, Jesus Cristo",
      "Os espíritos dos patriarcas"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 2:26-27",
    "hint": "'E eu, Deus, disse a meu Unigênito, que esteve comigo desde o princípio...'.",
    "explanation": "Moisés 2 revela a conversa íntima e cooperativa entre o Pai Celestial e Seu Filho Amado na criação do homem."
  },
  {
    "id": "pgv_077",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que Eva fez depois de tomar do fruto em Moisés 4:12?",
    "options": [
      "Esperou nova instrução antes de permitir que o marido comesse",
      "Deu o fruto ao marido, e ele comeu",
      "Levou o fruto até o altar antes de oferecê-lo ao marido",
      "Guardou o fruto e voltou sozinha ao centro do jardim"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 4:12",
    "hint": "Eva agiu com discernimento para permitir a continuação da família humana e o progresso eterno.",
    "explanation": "O ato de Eva e a subsequente escolha de Adão de permanecer ao lado de sua esposa abriram as portas para a mortalidade e o plano de salvação."
  },
  {
    "id": "pgv_078",
    "category": "pgv",
    "difficulty": 4,
    "question": "O que aconteceu quando Adão e Eva invocaram o Senhor em Moisés 5:4?",
    "options": [
      "Ouviram a voz do Senhor, mas não o viram",
      "Viram o Senhor e voltaram imediatamente ao jardim",
      "Viram um anjo que retirou a espada da entrada do jardim",
      "Receberam uma mensagem escrita trazida pelos querubins"
    ],
    "correct": 0,
    "scriptureRef": "Moisés 5:1-4",
    "hint": "O texto distingue ouvir a voz e ver quem falava.",
    "explanation": "Adão e Eva ouviram a voz do Senhor, mas não o viram, pois estavam excluídos de Sua presença."
  },
  {
    "id": "pgv_079",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual bisneto de Caim em Moisés 5:43-50 fez juramento com Satanás à semelhança de Caim e assassinou dois homens por causa do segredo?",
    "options": [
      "Tubalcaim",
      "Lameque",
      "Irad",
      "Meujael"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 5:47-50",
    "hint": "Ele disse a suas esposas Ada e Zila: 'Ouvi a minha voz... pois matei um homem para minha ferida e um moço para meu dano'.",
    "explanation": "Lameque perpetuou os juramentos de iniquidade e assassinato de Caim entre os homens corruptos de sua época."
  },
  {
    "id": "pgv_080",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Moisés 6:5-8, o que foi mantido zelosamente entre os filhos de Deus desde o princípio no idioma adâmico puro e imaculado?",
    "options": [
      "Um mapa dos caminhos percorridos pelos patriarcas",
      "Um livro de recordações, escrito no idioma de Adão pelo espírito de inspiração",
      "Um catálogo das armas produzidas pelos descendentes de Caim",
      "Um registro dos tributos pagos pelas primeiras cidades"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 6:5-8",
    "hint": "No qual se registrava a genealogia dos filhos de Deus e os ensinamentos transmitidos aos filhos com fidelidade.",
    "explanation": "O Livro de Memórias preservou a história sagrada e a pureza doutrinária patriarcal através das gerações antediluvianas."
  },
  {
    "id": "pgv_081",
    "category": "pgv",
    "difficulty": 4,
    "question": "Quantos anos duraram os dias de Sião nos dias de Enoque, segundo Moisés 7:68?",
    "options": [
      "120 anos",
      "500 anos",
      "365 anos",
      "430 anos"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 7:68",
    "hint": "'E todos os dias de Sião, nos dias de Enoque, foram trezentos e sessenta e cinco anos'.",
    "explanation": "Moisés 7:68 atribui 365 anos aos dias de Sião nos dias de Enoque."
  },
  {
    "id": "pgv_082",
    "category": "pgv",
    "difficulty": 4,
    "question": "Quem perguntou a Enoque quem ele era e de onde vinha, em Moisés 6:40?",
    "options": [
      "Maalalel",
      "Lameque",
      "Maíja",
      "Matusalém"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 6:40",
    "hint": "O texto nomeia o homem que se aproximou do profeta para interrogá-lo.",
    "explanation": "Moisés 6:40 identifica esse homem como Maíja; não o descreve lutando com Enoque."
  },
  {
    "id": "pgv_083",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Abraão 2:14-15, com que idade Abraão partiu de Harã em direção a Canaã com sua esposa Sarai e seu sobrinho Ló?",
    "options": [
      "75 anos de idade",
      "80 anos de idade",
      "100 anos de idade",
      "62 anos de idade"
    ],
    "correct": 3,
    "scriptureRef": "Abraão 2:14",
    "hint": "Use a idade indicada no Livro de Abraão, distinguindo-a do relato de Gênesis.",
    "explanation": "Abraão 2:14 informa que Abraão tinha 62 anos quando partiu de Harã."
  },
  {
    "id": "pgv_084",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Abraão 2:22-25, por que o Senhor instruiu Sarai a dizer no Egito que era irmã de Abraão em vez de sua esposa?",
    "options": [
      "Para conseguir uma audiência com os sacerdotes de Faraó",
      "Para obter o direito de herdar propriedades no Egito",
      "Para dispensar a família de tributos durante a fome",
      "Evitar que os egípcios matassem Abraão para tomar sua esposa por causa de sua beleza"
    ],
    "correct": 3,
    "scriptureRef": "Abraão 2:22-25",
    "hint": "Deus mesmo revelou esta cautela a Abraão perante o perigo moral da corte de Faraó.",
    "explanation": "O Senhor protegeu a integridade de Abraão e de Sarai, abençoando o patriarca e preservando a linhagem do convênio."
  },
  {
    "id": "pgv_085",
    "category": "pgv",
    "difficulty": 4,
    "question": "No Livro de Abraão 3:15, qual foi o mandamento que o Senhor deu a Abraão concernente aos conhecimentos de astronomia que acabara de contemplar?",
    "options": [
      "Guardar os conhecimentos até depois de voltar a Canaã",
      "Declarar no Egito as palavras e os conhecimentos que o Senhor lhe havia mostrado",
      "Transmitir os ensinamentos apenas aos sacerdotes caldeus",
      "Ensinar aquelas palavras somente aos descendentes diretos"
    ],
    "correct": 1,
    "scriptureRef": "Abraão 3:15",
    "hint": "Abraão deveria usar esses conhecimentos sublimes para ensinar a realeza egípcia sobre o verdadeiro Criador.",
    "explanation": "A astronomia revelada a Abraão serviu de ponte missionária para demonstrar a soberania do Deus vivo aos idólatras do Nilo."
  },
  {
    "id": "pgv_086",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual é a ordem correta dos três Fac-símiles na Pérola de Grande Valor?",
    "options": [
      "Altar; trono de Faraó; hipocéfalo",
      "Trono de Faraó; altar; hipocéfalo",
      "Altar; hipocéfalo; trono de Faraó",
      "Hipocéfalo; trono de Faraó; altar"
    ],
    "correct": 2,
    "scriptureRef": "Pérola de Grande Valor: Fac-símiles 1, 2 e 3",
    "hint": "Da libertação do sacrifício em Ur à glória astronômica de Cólobe e ao ensino perante a corte de Faraó.",
    "explanation": "Os fac-símiles retratam a progressão da jornada de fé, revelação cósmica e ministério diplomático e espiritual de Abraão."
  },
  {
    "id": "pgv_087",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em quem a Primeira Regra de Fé declara a crença?",
    "options": [
      "No Pai Eterno, em Abraão e nos mensageiros celestiais",
      "Em Jesus Cristo, em Moisés e em Elias, o profeta",
      "No Pai Eterno, no arcanjo Miguel e no Espírito Santo",
      "No Pai Eterno, em Jesus Cristo e no Espírito Santo"
    ],
    "correct": 3,
    "scriptureRef": "Regra de Fé 1; D&C 130:22",
    "hint": "Confirmando a verdade bíblica e a visão sublime do Bosque Sagrado de 1820.",
    "explanation": "A Regra de Fé 1 sintetiza a doutrina da Deidade restaurada com clareza incomparável."
  },
  {
    "id": "pgv_088",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual é a cidade que a Décima Regra de Fé profetiza que será construída no continente americano e chamada de Sião?",
    "options": [
      "A cidade de Atenas",
      "A Babilônia restaurada",
      "A Nova Jerusalém",
      "A Grande Roma"
    ],
    "correct": 2,
    "scriptureRef": "Regra de Fé 10; Éter 13:3-10",
    "hint": "Em harmonia com as profecias do Livro de Mórmon em Éter e 3 Néfi.",
    "explanation": "A Nova Jerusalém será a capital sagrada e o santuário dos santos congregados nas Américas antes da volta do Senhor."
  },
  {
    "id": "pgv_089",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Joseph Smith - História 1:56, qual foi a ocupação em que Joseph Smith trabalhou em outubro de 1825 para o senhor Josiah Stowell no Condado de Susquehanna?",
    "options": [
      "Construir um moinho para o processamento de trigo",
      "Trabalhar nas escavações para encontrar uma antiga mina espanhola de prata",
      "Transportar madeira para a construção de uma capela",
      "Preparar a tipografia para a impressão de um jornal"
    ],
    "correct": 1,
    "scriptureRef": "JS-H 1:56",
    "hint": "Após um mês de escavações sem sucesso, Joseph convenceu o idoso senhor a desistir da empreitada.",
    "explanation": "Durante essa estadia de trabalho em Harmony, Joseph hospedou-se na casa do senhor Isaac Hale e conheceu Emma Hale, sua futura esposa."
  },
  {
    "id": "pgv_090",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em que dia, mês e ano Joseph Smith e Emma Hale se casaram na cidade de South Bainbridge, Nova York?",
    "options": [
      "6 de abril de 1830",
      "22 de setembro de 1823",
      "18 de janeiro de 1827",
      "27 de junho de 1844"
    ],
    "correct": 2,
    "scriptureRef": "JS-H 1:57",
    "hint": "Casaram-se na residência do juiz de paz Zachariah Tarble.",
    "explanation": "O casamento com Emma foi uma bênção vital de companheirismo e fortaleza moral meses antes de receber as placas sagradas."
  },
  {
    "id": "pgv_091",
    "category": "pgv",
    "difficulty": 4,
    "question": "Quem era o irmão mais velho de Joseph Smith que faleceu em 19 de novembro de 1823 e cuja memória era reverenciada com profunda saudade por toda a família Smith?",
    "options": [
      "Alvin Smith",
      "Hyrum Smith",
      "Don Carlos Smith",
      "Samuel H. Smith"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:4; D&C 137:5",
    "hint": "Sua morte precoce devido a uma dose errada de calomelano comoveu a todos e inspirou as revelações sobre a salvação dos mortos.",
    "explanation": "Alvin era o esteio financeiro da família e incentivou Joseph até seus últimos suspiros a cumprir o desígnio de Deus."
  },
  {
    "id": "pgv_092",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual instrumento divino de duas pedras transparentes presas em aros de prata, semelhante a óculos e atado a um peitoral, acompanhava as placas de ouro para fins de tradução?",
    "options": [
      "A esfera chamada Liahona",
      "A espada que pertencera a Labão",
      "Os intérpretes, conhecidos como Urim e Tumim",
      "A vara usada por Moisés no deserto"
    ],
    "correct": 2,
    "scriptureRef": "JS-H 1:35",
    "hint": "Morôni explicou que Deus havia preparado esses instrumentos para a tradução do livro antigo nos tempos modernos.",
    "explanation": "O Urim e Tumim capacitou o jovem profeta a traduzir os caracteres egípcios reformados pelo dom e poder de Deus."
  },
  {
    "id": "pgv_093",
    "category": "pgv",
    "difficulty": 3,
    "question": "O que o Anjo Morôni trajava quando apareceu no quarto de Joseph Smith em 1823, conforme descrito vívida e minuciosamente em JS-H 1:31?",
    "options": [
      "Uma túnica de linho com um cinto de ouro e sandálias",
      "Uma túnica solta de brancura extraordinária, com mãos e pés descobertos",
      "Um manto de lã com bordados semelhantes aos sacerdotais",
      "Uma veste branca com peitoral e pedras nas ombreiras"
    ],
    "correct": 1,
    "scriptureRef": "JS-H 1:31-32",
    "hint": "Não somente a sua túnica era alva em extremo, mas toda a sua pessoa era indescritivelmente gloriosa.",
    "explanation": "A descrição de Joseph Smith reflete a pureza celestial e resplandecente dos seres ressuscitados imortais."
  },
  {
    "id": "pgv_094",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Joseph Smith - Mateus 1:37, qual é a chave indispensável dada pelo Senhor para não ser enganado nos últimos dias pelas artimanhas dos falsos mestres?",
    "options": [
      "Aguardar que os sinais sejam interpretados pelos governantes",
      "Procurar segurança somente nas tradições dos antepassados",
      "Aceitar qualquer mestre que realize sinais extraordinários",
      "Entesourar Sua palavra, preservando-a como proteção contra o engano dos últimos dias"
    ],
    "correct": 3,
    "scriptureRef": "JS-M 1:37",
    "hint": "Entesourar a palavra significa estudá-la, amá-la, guardá-la na memória e praticá-la no dia a dia.",
    "explanation": "O estudo diligente e a vivência diária das sagradas escrituras formam a bússola infalível de discernimento contra as ilusões do mundo."
  },
  {
    "id": "pgv_095",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual cidade celestial se reunirá com a Sião terrestre na profecia de Moisés 7:62–63?",
    "options": [
      "A cidade de Jerusalém dos dias de Salomão",
      "A cidade de Abraão na terra dos caldeus",
      "A cidade de Zaraenla dos dias de Benjamim",
      "A cidade de Sião de Enoque"
    ],
    "correct": 3,
    "scriptureRef": "Moisés 7:62-64; 10ª Regra de Fé",
    "hint": "Unindo-se com a Sião terrestre estabelecida pelos santos no continente americano.",
    "explanation": "Esta grandiosa convergência celestial e terrestre coroará o triunfo final da obra de Sião na Terra."
  },
  {
    "id": "pgv_096",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual profeta presidiu a Conferência Geral de 10 de outubro de 1880 em que a Pérola de Grande Valor foi unanimemente canonizada como a quarta Obra-Padrão da Igreja?",
    "options": [
      "Presidente Brigham Young",
      "Presidente Wilford Woodruff",
      "Presidente Joseph F. Smith",
      "Presidente John Taylor"
    ],
    "correct": 3,
    "scriptureRef": "História da Igreja, vol. 7",
    "hint": "Com Orson Pratt apresentando a moção ao corpo dos santos reunidos no Tabernáculo de Salt Lake.",
    "explanation": "A canonização oficial de 1880 selou o valor sagrado perpétuo da Pérola de Grande Valor para toda a Igreja."
  },
  {
    "id": "pgv_097",
    "category": "pgv",
    "difficulty": 3,
    "question": "Em Moisés 1:1, onde Moisés foi arrebatado para contemplar as visões face a face com o Criador?",
    "options": [
      "No monte das Oliveiras, diante da cidade de Jerusalém",
      "No monte Nebo, enquanto contemplava a terra prometida",
      "Num monte muito alto, sem nome indicado",
      "No monte Sinai, identificado expressamente no relato"
    ],
    "correct": 2,
    "scriptureRef": "Moisés 1:1, 42",
    "hint": "O Senhor ordenou-lhe que não mostrasse estas palavras ao mundo, até que um profeta como ele fosse levantado nos últimos dias.",
    "explanation": "As palavras de Moisés 1 foram retiradas por homens iníquos e restauradas a Joseph Smith em junho de 1830 por revelação direta."
  },
  {
    "id": "pgv_098",
    "category": "pgv",
    "difficulty": 4,
    "question": "Qual era o nome do rio do Jardim do Éden mencionado em Moisés 3:11-14 que rodeava a terra de Havilá, onde havia ouro bom, bdélio e pedra de ônix?",
    "options": [
      "O rio Eufrates",
      "O rio Tigre (Hídequel)",
      "O rio Giom",
      "O rio Pisom"
    ],
    "correct": 3,
    "scriptureRef": "Moisés 3:11-12",
    "hint": "O primeiro dos quatro rios que saíam para regar o jardim da criação.",
    "explanation": "Moisés 3 fornece a geografia edênica primordial antes das transformações geológicas da Terra."
  },
  {
    "id": "pgv_099",
    "category": "pgv",
    "difficulty": 4,
    "question": "Em Moisés 6:22, quem é o primeiro elo genealógico supremo a partir de quem todos os patriarcas são chamados de 'filhos de Deus'?",
    "options": [
      "Enoque",
      "Adão",
      "Noé",
      "Abraão"
    ],
    "correct": 1,
    "scriptureRef": "Moisés 6:22",
    "hint": "'E esta é a genealogia dos filhos de Adão, que era o filho de Deus...'.",
    "explanation": "Esta gloriosa declaração reafirma a filiação divina literal e nobre da humanidade como gerada à imagem do Pai."
  },
  {
    "id": "pgv_100",
    "category": "pgv",
    "difficulty": 4,
    "question": "Como Joseph Smith reafirma seu testemunho da Primeira Visão em Joseph Smith—História 1:25?",
    "options": [
      "Sabia que havia visto uma visão, sabia que Deus o sabia e não ousava negá-la",
      "Deixaria de contar a visão caso as perseguições continuassem",
      "Guardaria silêncio até receber a aprovação das autoridades",
      "Ainda esperava a confirmação dos ministros de sua região"
    ],
    "correct": 0,
    "scriptureRef": "JS-H 1:24-25",
    "hint": "A sua inabalável confissão de fé e fidelidade perante toda a humanidade e perante os céus.",
    "explanation": "Joseph Smith permaneceu leal e inquebrantável ao seu testemunho da Primeira Visão até selar suas palavras com a própria vida em Carthage."
  }
]

def build():
    target = Path(__file__).resolve().with_name("data_pgv.js")
    content = "/** Banco revisado: 100 perguntas; alternativas e gabaritos sincronizados. */\nvar QUESTIONS_PGV = "
    content += json.dumps(questions, ensure_ascii=False, indent=2) + ";\n"
    target.write_text(content, encoding="utf-8")
    print(f"Sucesso: {target.name} gerado com {len(questions)} perguntas.")

if __name__ == "__main__":
    build()
