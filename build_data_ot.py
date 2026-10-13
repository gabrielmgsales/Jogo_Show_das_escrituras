# -*- coding: utf-8 -*-
"""Gerador do banco OT; mantém textos revisados e gabaritos distribuídos."""
import json
from pathlib import Path

questions = [
  {
    "id": "ot_001",
    "category": "ot",
    "difficulty": 1,
    "question": "Em qual montanha a arca de Noé repousou após as águas do grande dilúvio começarem a minguar?",
    "options": [
      "Os montes de Ararate",
      "As montanhas de Efraim",
      "Os montes da região do Sinai",
      "As montanhas de Gileade"
    ],
    "correct": 0,
    "scriptureRef": "Gênesis 8:4",
    "hint": "Localizado na cordilheira da atual Turquia/Armênia.",
    "explanation": "Gênesis 8:4 afirma que a arca repousou no sétimo mês, no dia dezessete do mês, sobre os montes de Ararate."
  },
  {
    "id": "ot_002",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual ave Noé soltou pela primeira vez da arca para verificar se as águas haviam secado da face da Terra?",
    "options": [
      "Um corvo, que ia e voltava",
      "Uma pomba",
      "Uma águia",
      "Uma andorinha"
    ],
    "correct": 0,
    "scriptureRef": "Gênesis 8:7",
    "hint": "Esta ave voava indo e voltando até que as águas se secaram; depois soltou a pomba.",
    "explanation": "Noé soltou primeiro um corvo e, posteriormente, uma pomba que retornou na segunda vez com uma folha verde de oliveira no bico."
  },
  {
    "id": "ot_003",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual era o nome original de Sara e Abraão antes de o Senhor mudar seus nomes ao estabelecer Seu convênio eterno?",
    "options": [
      "Sefora e Terá",
      "Sarai e Abrão",
      "Milca e Naor",
      "Quetura e Harã"
    ],
    "correct": 1,
    "scriptureRef": "Gênesis 17:5, 15",
    "hint": "O Senhor disse: 'Não mais te chamarás Abrão, mas Abraão será o teu nome, porque por pai de muitas nações te constituí'.",
    "explanation": "A mudança de nomes simbolizou o novo nascimento espiritual e o convênio eterno da semente de Abraão."
  },
  {
    "id": "ot_004",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual cidade perversa foi destruída por fogo e enxofre caídos do céu, da qual a mulher de Ló olhou para trás e virou uma estátua de sal?",
    "options": [
      "Sodoma e Gomorra",
      "Nínive e Babilônia",
      "Jericó e Ai",
      "Tiro e Sidom"
    ],
    "correct": 0,
    "scriptureRef": "Gênesis 19:24-26",
    "hint": "Situada na planície do vale de Sidim, perto do Mar Morto.",
    "explanation": "A mulher de Ló desobedeceu à advertência angélica de não olhar para trás e foi transformada em uma coluna de sal."
  },
  {
    "id": "ot_005",
    "category": "ot",
    "difficulty": 3,
    "question": "Em qual monte Abraão foi provado por Deus ao levar seu filho amado Isaque para oferecê-lo em sacrifício antes do anjo detê-lo?",
    "options": [
      "Monte Sinai",
      "Monte Moriá",
      "Monte Horebe",
      "Monte Sião"
    ],
    "correct": 1,
    "scriptureRef": "Gênesis 22:2",
    "hint": "O mesmo monte em Jerusalém onde Salomão construiu mais tarde o Templo sagrado.",
    "explanation": "No monte Moriá, o sacrifício de Isaque tipificou de maneira perfeita a futura entrega voluntária do Filho Unigênito pelo Pai."
  },
  {
    "id": "ot_006",
    "category": "ot",
    "difficulty": 1,
    "question": "Por que prato de comida o caçador Esaú vendeu levianamente seu direito de primogenitura sagrada a seu irmão gêmeo Jacó?",
    "options": [
      "Um bolo de cevada servido com mel",
      "Um prato de trigo cozido com azeite",
      "Um cordeiro assado com ervas amargas",
      "Um guisado de lentilhas com pão"
    ],
    "correct": 3,
    "scriptureRef": "Gênesis 25:29-34",
    "hint": "Esaú voltava cansado do campo e disse: 'Eis que estou a ponto de morrer; e para que me serve a primogenitura?'.",
    "explanation": "Esaú desprezou a sua sagrada herança e convênio patriarcal por um momento efêmero de satisfação física."
  },
  {
    "id": "ot_007",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual nome Jacó deu ao lugar onde teve a visão celestial de uma escada que tocava o céu com anjos subindo e descendo?",
    "options": [
      "Betel",
      "Peniel",
      "Hebrom",
      "Maanaim"
    ],
    "correct": 0,
    "scriptureRef": "Gênesis 28:12-19",
    "hint": "Ele usou uma pedra como travesseiro e depois a ungiu com azeite como monumento sagrado.",
    "explanation": "Jacó declarou: 'Quão terrível é este lugar! Este não é outro lugar senão a casa de Deus, e esta é a porta dos céus'."
  },
  {
    "id": "ot_008",
    "category": "ot",
    "difficulty": 3,
    "question": "Após lutar com um mensageiro celeste até o romper da alva junto ao ribeiro de Jaboque, qual novo nome Jacó recebeu?",
    "options": [
      "Melquisedeque",
      "Efraim",
      "Judá",
      "Israel"
    ],
    "correct": 3,
    "scriptureRef": "Gênesis 32:28",
    "hint": "O Senhor declarou: 'Não se chamará mais o teu nome Jacó, mas Israel; pois como príncipe lutaste com Deus e com os homens, e prevaleceste'.",
    "explanation": "O nome Israel tornou-se o título de todo o povo do convênio do Senhor."
  },
  {
    "id": "ot_009",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual filho de Jacó teve a ideia de vender José aos mercadores ismaelitas (midianitas) por vinte moedas de prata em vez de matá-lo?",
    "options": [
      "Simeão",
      "Rúben",
      "Levi",
      "Judá"
    ],
    "correct": 3,
    "scriptureRef": "Gênesis 37:26-28",
    "hint": "Rúben pretendia livrá-lo mais tarde da cova, mas este irmão propôs vendê-lo aos mercadores que iam para o Egito.",
    "explanation": "Judá sugeriu a venda de José, da cuja linhagem séculos mais tarde nasceria o Messias."
  },
  {
    "id": "ot_010",
    "category": "ot",
    "difficulty": 2,
    "question": "O que significavam as sete vacas gordas e as sete vacas magras que Faraó contemplou em seu sonho perturbador interpretado por José?",
    "options": [
      "Sete anos de fartura seguidos de sete de fome",
      "Sete anos de guerra seguidos de sete de paz",
      "Sete reis prósperos seguidos de sete governantes pobres",
      "Sete colheitas perdidas seguidas de sete abundantes"
    ],
    "correct": 0,
    "scriptureRef": "Gênesis 41:25-32",
    "hint": "José aconselhou Faraó a estocar mantimentos nas cidades durante os anos de fartura.",
    "explanation": "A revelação divina permitiu a José armazenar trigo suficiente para salvar não apenas o Egito, mas toda a família de Israel."
  },
  {
    "id": "ot_011",
    "category": "ot",
    "difficulty": 1,
    "question": "Como Deus Se manifestou a Moisés pela primeira vez no monte Horebe quando este cuidava das ovelhas de seu sogro Jetro?",
    "options": [
      "Numa nuvem que cobria toda a entrada de uma caverna",
      "Numa sarça que ardia sem se consumir",
      "Num fogo que consumia as pedras ao redor do rebanho",
      "Num vento forte que despedaçava as rochas do monte"
    ],
    "correct": 1,
    "scriptureRef": "Êxodo 3:1-4",
    "hint": "O Senhor ordenou-lhe: 'Tira os sapatos de teus pés, porque o lugar em que tu estás é terra santa'.",
    "explanation": "Na sarça ardente, o Deus de Abraão, Isaque e Jacó comissionou Moisés para libertar Israel do Egito."
  },
  {
    "id": "ot_012",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual foi a décima e última terrível praga que convenceu Faraó a deixar o povo de Israel sair do Egito?",
    "options": [
      "A transformação das águas do Nilo em sangue",
      "As trevas que cobriram o Egito durante três dias",
      "A morte dos primogênitos",
      "A destruição das plantações pelos gafanhotos"
    ],
    "correct": 2,
    "scriptureRef": "Êxodo 12:29-31",
    "hint": "Os israelitas marcaram os umbrais de suas portas com o sangue do cordeiro pascoal para serem poupados.",
    "explanation": "A Páscoa judaica foi instituída em memória perpétua dessa miraculosa libertação e da redenção do anjo destruidor."
  },
  {
    "id": "ot_013",
    "category": "ot",
    "difficulty": 2,
    "question": "O que o Senhor fez chover dos céus todas as manhãs no deserto para alimentar os filhos de Israel durante os quarenta anos?",
    "options": [
      "Cevada, recolhida antes do aparecimento do sol",
      "Trigo, já separado da palha e pronto para moer",
      "Maná, semelhante à semente de coentro",
      "Pão de farinha, preparado com azeite e fermento"
    ],
    "correct": 2,
    "scriptureRef": "Êxodo 16:14-31",
    "hint": "Quando viram, perguntaram: 'Man-hu?' (Que é isto?), dando origem ao seu nome.",
    "explanation": "O maná diário ensinou a Israel a confiar na providência de Deus, colhendo o dobro apenas na véspera do sábado."
  },
  {
    "id": "ot_014",
    "category": "ot",
    "difficulty": 3,
    "question": "Quem sustentou os braços cansados de Moisés erguidos no alto da colina até o pôr do sol para que Israel vencesse a batalha contra Amaleque?",
    "options": [
      "Arão e Hur",
      "Josué e Calebe",
      "Fineias e Nadabe",
      "Jitro e Eleazar"
    ],
    "correct": 0,
    "scriptureRef": "Êxodo 17:10-12",
    "hint": "Um de cada lado colocou uma pedra para Moisés sentar e seguraram suas mãos firmes.",
    "explanation": "Quando as mãos de Moisés permaneciam erguidas, Israel prevalecia, demonstrando o poder de apoiar os líderes do Senhor."
  },
  {
    "id": "ot_015",
    "category": "ot",
    "difficulty": 3,
    "question": "O que ficava guardado dentro da sagrada Arca da Aliança coberta de ouro puro no Santo dos Santos do Tabernáculo?",
    "options": [
      "O livro da lei, o azeite da unção e as pedras do Jordão",
      "A vara de Moisés, as trombetas de prata e o incensário",
      "As tábuas da lei, o peitoral sacerdotal e a espada de Josué",
      "As tábuas da lei, um vaso com maná e a vara de Arão"
    ],
    "correct": 3,
    "scriptureRef": "Hebreus 9:4; Êxodo 25:16; Números 17:10",
    "hint": "Três testemunhos tangíveis da lei, da provisão e da autoridade legítima do sacerdócio.",
    "explanation": "A Arca continha os memoriais sagrados do convênio sob o propiciatório guardado pelas asas dos querubins."
  },
  {
    "id": "ot_016",
    "category": "ot",
    "difficulty": 3,
    "question": "Quais foram os dois únicos espias israelitas dentre os doze enviados que deram relatório de fé e coragem para conquistar Canaã?",
    "options": [
      "Arão e Moisés",
      "Gideão e Baraque",
      "Josué e Calebe",
      "Nadabe e Abiú"
    ],
    "correct": 2,
    "scriptureRef": "Números 14:6-9",
    "hint": "Eles rasgaram suas vestes e disseram: 'A terra pela qual passamos a espiar é terra muitíssimo boa... o Senhor é conosco, não os temais'.",
    "explanation": "Por causa de sua fidelidade inabalável, somente Josué e Calebe de toda aquela geração adulta viveram para entrar na terra prometida."
  },
  {
    "id": "ot_017",
    "category": "ot",
    "difficulty": 2,
    "question": "O que Moisés ergueu sobre uma haste no deserto para que todo aquele que fosse picado por serpentes abrasadoras olhasse e vivesse?",
    "options": [
      "Uma serpente de bronze",
      "A vara de amendoeira",
      "Uma bandeira branca",
      "Uma tocha acesa"
    ],
    "correct": 0,
    "scriptureRef": "Números 21:8-9; Alma 33:19",
    "hint": "Símbolo profético de Jesus Cristo sendo levantado na cruz para conceder cura e vida eterna aos que olharem com fé.",
    "explanation": "Cristo mesmo citou esse episódio a Nicodemos em João 3:14: 'Assim como Moisés levantou a serpente no deserto, assim importa que o Filho do Homem seja levantado'."
  },
  {
    "id": "ot_018",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual animal falou com voz humana repreendendo o falso profeta Balaão por espancá-lo três vezes quando um anjo do Senhor com uma espada desembainhada bloqueava o caminho?",
    "options": [
      "Seu camelo",
      "Um cordeiro",
      "Uma águia",
      "Sua jumenta"
    ],
    "correct": 3,
    "scriptureRef": "Números 22:28-30",
    "hint": "O Senhor abriu a boca da jumenta, que perguntou: 'Que te fiz eu, para que me espancasses estas três vezes?'.",
    "explanation": "A visão da jumenta salvou Balaão de ser morto pela espada do anjo do Senhor."
  },
  {
    "id": "ot_019",
    "category": "ot",
    "difficulty": 3,
    "question": "De qual monte o profeta Moisés contemplou toda a formosa Terra Prometida antes de falecer aos 120 anos de idade?",
    "options": [
      "O monte Sinai",
      "O monte Hermom",
      "O monte Carmelo",
      "O monte Nebo"
    ],
    "correct": 3,
    "scriptureRef": "Deuteronômio 34:1-4",
    "hint": "Situado nas planícies de Moabe em frente a Jericó.",
    "explanation": "Moisés subiu ao monte Nebo, contemplou a herança de Israel e foi recolhido pelo Senhor sem que ninguém soubesse o seu sepulcro."
  },
  {
    "id": "ot_020",
    "category": "ot",
    "difficulty": 4,
    "question": "Em Deuteronômio 6:4-5, qual é a solene confissão monoteísta fundamental de Israel recitada diariamente pelos judeus?",
    "options": [
      "A oração de Salomão no templo",
      "O Shemá: Ouve, ó Israel",
      "O cântico de Moisés junto ao mar",
      "A bênção sacerdotal de Arão"
    ],
    "correct": 1,
    "scriptureRef": "Deuteronômio 6:4-5",
    "hint": "A pedra angular da fé e adoração israelita através de todas as gerações.",
    "explanation": "O Shemá proclama a unidade de Deus e o mandamento de amá-Lo com todo o coração, alma e forças."
  },
  {
    "id": "ot_021",
    "category": "ot",
    "difficulty": 1,
    "question": "Como os impenetráveis muros da cidade fortificada de Jericó caíram diante do exército de Josué?",
    "options": [
      "Após os soldados escavarem as bases das muralhas",
      "Após as voltas, as trombetas e o brado do povo",
      "Após um cerco que esgotou as provisões dos moradores",
      "Após um ataque noturno enquanto os sacerdotes oravam"
    ],
    "correct": 1,
    "scriptureRef": "Josué 6:15-20",
    "hint": "No sétimo dia deram sete voltas, soaram as trombetas de chifre de carneiro e as muralhas ruíram.",
    "explanation": "A queda de Jericó deu-se pelo poder divino em resposta à estrita obediência e fé do povo de Israel."
  },
  {
    "id": "ot_022",
    "category": "ot",
    "difficulty": 2,
    "question": "Quem era a mulher em Jericó que escondeu os dois espias israelitas no terraço de sua casa sob os talos de linho e foi poupada?",
    "options": [
      "Débora",
      "Rute",
      "Jael",
      "Raabe"
    ],
    "correct": 3,
    "scriptureRef": "Josué 2:1-6; 6:25",
    "hint": "Ela atou um cordão de fio de escarlata à sua janela como sinal de proteção para toda a sua família.",
    "explanation": "Raabe foi acolhida em Israel por sua fé corajosa, tornando-se antepassada de Davi e de Jesus Cristo."
  },
  {
    "id": "ot_023",
    "category": "ot",
    "difficulty": 3,
    "question": "Em qual batalha miraculosa Josué orou e o sol parou sobre Gibeão e a lua no vale de Aijalom durante quase um dia inteiro?",
    "options": [
      "Contra os habitantes da cidade de Ai",
      "Na batalha contra os cinco reis amorreus, na região de Bete-Horom",
      "Contra os defensores da cidade de Jericó",
      "Contra os exércitos reunidos junto ao Jordão"
    ],
    "correct": 1,
    "scriptureRef": "Josué 10:12-14",
    "hint": "O Senhor também lançou grandes pedras de granizo do céu sobre os inimigos em fuga.",
    "explanation": "Josué 10:14 relata que nunca houve dia semelhante a este, nem antes nem depois, em que o Senhor atendeu à voz de um homem."
  },
  {
    "id": "ot_024",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual profetisa e juíza de Israel julgava o povo debaixo de uma palmeira em Efraim e liderou a vitória com Baraque contra Sísera?",
    "options": [
      "Miriã",
      "Hulda",
      "Ana",
      "Débora"
    ],
    "correct": 3,
    "scriptureRef": "Juízes 4:4-9",
    "hint": "Ela cantou um célebre hino de vitória celebrando a libertação de Israel.",
    "explanation": "Débora foi uma líder extraordinária e mãe em Israel cuja fé derrotou os 900 carros de ferro do general Sísera."
  },
  {
    "id": "ot_025",
    "category": "ot",
    "difficulty": 2,
    "question": "Com quantos soldados seletos que lamberam água com a língua levando a mão à boca Gideão derrotou o imenso exército midianita?",
    "options": [
      "Doze mil homens",
      "Dez mil homens",
      "Trinta e dois mil homens",
      "Trezentos soldados"
    ],
    "correct": 3,
    "scriptureRef": "Juízes 7:5-7",
    "hint": "Eles levaram trombetas, cântaros vazios e tochas acesas dentro dos cântaros gritando: 'Pelo Senhor e por Gideão!'.",
    "explanation": "O Senhor reduziu o exército a trezentos homens para demonstrar que a vitória procedia do poder divino e não da força humana."
  },
  {
    "id": "ot_026",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual era a fonte do poder físico sobre-humano do juiz Sansão conforme o seu voto perpétuo de nazireu com Deus?",
    "options": [
      "A bênção transmitida pelo pai por direito de primogenitura",
      "O uso de armas separadas para o serviço do tabernáculo",
      "O vínculo com Deus simbolizado pelo cabelo não cortado",
      "A unção recebida dos sacerdotes antes de cada batalha"
    ],
    "correct": 2,
    "scriptureRef": "Juízes 16:17",
    "hint": "Ele revelou seu segredo à pérfida Dalila, que o traiu aos príncipes dos filisteus.",
    "explanation": "O voto de nazireado proibia cortar o cabelo e beber vinho; a quebra do voto retirou a presença protetora do Espírito do Senhor."
  },
  {
    "id": "ot_027",
    "category": "ot",
    "difficulty": 1,
    "question": "Qual nobre mulher moabita recusou-se a abandonar sua sogra viúva Noemi dizendo: 'Aonde quer que fores, irei eu... o teu povo é o meu povo, o teu Deus é o meu Deus'?",
    "options": [
      "Orfa",
      "Mical",
      "Rute",
      "Vasti"
    ],
    "correct": 2,
    "scriptureRef": "Rute 1:16-17",
    "hint": "Ela recolheu espigas no campo de Boaz em Belém e casou-se com ele.",
    "explanation": "A lealdade e devoção de Rute a tornaram bisavó do Rei Davi e antecessora na linhagem terrena de Cristo."
  },
  {
    "id": "ot_028",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual mãe piedosa orou no tabernáculo em Siló derramando sua alma perante o Senhor em lágrimas e prometeu consagrar seu filho primogênito a Deus?",
    "options": [
      "Joquebede, mãe de Moisés",
      "Rebeca, mãe de Jacó",
      "Ana, que se tornou mãe de Samuel",
      "Raquel, mãe de José"
    ],
    "correct": 2,
    "scriptureRef": "1 Samuel 1:10-15",
    "hint": "O sacerdote Eli pensou que ela estivesse embriagada, mas ela respondeu: 'Sou uma mulher atribulada de espírito'.",
    "explanation": "Deus atendeu à oração de Ana, dando-lhe o menino Samuel, a quem ela entregou para servir no santuário conforme prometera."
  },
  {
    "id": "ot_029",
    "category": "ot",
    "difficulty": 2,
    "question": "Após receber a orientação de Eli, como Samuel respondeu quando o Senhor voltou a chamá-lo?",
    "options": [
      "Envia teu servo à casa de meu pai",
      "Aqui estou; por que me chamaste novamente?",
      "Fala, porque o teu servo está ouvindo tua voz",
      "Mostra-me um sinal para que eu reconheça tua voz"
    ],
    "correct": 2,
    "scriptureRef": "1 Samuel 3:9–10",
    "hint": "Seguindo a sábia instrução do velho sacerdote Eli.",
    "explanation": "Samuel tornou-se um dos maiores profetas de Israel, de cujas palavras nenhuma caiu por terra desatendida."
  },
  {
    "id": "ot_030",
    "category": "ot",
    "difficulty": 1,
    "question": "Quantas pedras lisas do ribeiro o jovem pastor Davi escolheu e colocou em seu alforje antes de enfrentar o gigante Golias?",
    "options": [
      "Três pedras lisas",
      "Sete pedras lisas",
      "Doze pedras lisas",
      "Cinco pedras lisas"
    ],
    "correct": 3,
    "scriptureRef": "1 Samuel 17:40",
    "hint": "Ele pegou seu cajado, sua funda e cinco pedras redondas no leito das águas.",
    "explanation": "Davi usou apenas a primeira pedra de sua funda para encravar na testa do campeão filisteu e derrotá-lo em nome do Senhor."
  },
  {
    "id": "ot_031",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual filho do Rei Saul amava a Davi como à sua própria alma e fez com ele uma célebre aliança de amizade leal, entregando-lhe seu manto e espada?",
    "options": [
      "Abner",
      "Isbosete",
      "Absalão",
      "Jônatas"
    ],
    "correct": 3,
    "scriptureRef": "1 Samuel 18:1-4",
    "hint": "Ele alertou Davi com flechas disparadas no campo quando seu pai Saul tentava matá-lo.",
    "explanation": "A nobreza de Jônatas ao apoiar Davi, sabendo que este seria o rei escolhido por Deus em seu lugar, é um modelo sublime de amor fraternal."
  },
  {
    "id": "ot_032",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual profeta repreendeu o Rei Davi por seu terrível pecado com Bate-Seba e a morte de Urias contando a parábola da ovelhinha do pobre?",
    "options": [
      "Gade",
      "Samuel",
      "Natã",
      "Ezequiel"
    ],
    "correct": 2,
    "scriptureRef": "2 Samuel 12:1-7",
    "hint": "Após Davi se enfurecer contra o homem rico da parábola, o profeta apontou-lhe o dedo e disse: 'Tu és este homem!'.",
    "explanation": "A advertência de Natã levou Davi a compor o comovente Salmo 51 de profundo quebrantamento e confissão."
  },
  {
    "id": "ot_033",
    "category": "ot",
    "difficulty": 1,
    "question": "O que o jovem Rei Salomão pediu ao Senhor em sonho em Gibeom quando Deus lhe disse: 'Pede o que queres que eu te dê'?",
    "options": [
      "Longa vida para conduzir Israel durante muitas gerações",
      "Um coração entendido para julgar o povo e distinguir o bem do mal",
      "Riquezas para engrandecer o reino diante das nações",
      "Vitória sobre os inimigos que ameaçavam suas fronteiras"
    ],
    "correct": 1,
    "scriptureRef": "1 Reis 3:5-12",
    "hint": "Deus alegrou-Se porque ele não pediu riquezas nem glória pessoal e concedeu-lhe a maior sabedoria da antiguidade.",
    "explanation": "A sábia escolha de Salomão atraiu bênçãos inigualáveis e a admiração dos monarcas de todo o mundo conhecido."
  },
  {
    "id": "ot_034",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual rainha rica viajou de terras distantes com camelos carregados de especiarias e ouro para provar a sabedoria de Salomão com enigmas difíceis?",
    "options": [
      "A Rainha Ester",
      "A Rainha Jezabel",
      "A Rainha Atalia",
      "A Rainha de Sabá"
    ],
    "correct": 3,
    "scriptureRef": "1 Reis 10:1-9",
    "hint": "Ela declarou deslumbrada: 'Foi verdade a palavra que ouvi... mas não me contaram a metade da tua sabedoria'.",
    "explanation": "A visita da Rainha de Sabá atestou a glória internacional da corte salomônica e o esplendor do Templo de Jerusalém."
  },
  {
    "id": "ot_035",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual profeta desafiou os 450 profetas de Baal e os 400 profetas de Aserate no Monte Carmelo para provar quem era o verdadeiro Deus por fogo?",
    "options": [
      "Micaías, filho de Inlá",
      "Isaías, filho de Amoz",
      "Elias, o tisbita",
      "Eliseu, filho de Safate"
    ],
    "correct": 2,
    "scriptureRef": "1 Reis 18:19-39",
    "hint": "Ele mandou derramar quatro cântaros de água três vezes sobre o altar de lenha antes de orar.",
    "explanation": "O fogo do Senhor desceu, lambeu o holocausto, a lenha, as pedras e a água, e o povo caiu com o rosto em terra clamando: 'O Senhor é Deus!'."
  },
  {
    "id": "ot_036",
    "category": "ot",
    "difficulty": 3,
    "question": "Como o profeta Elias subiu aos céus quando caminhava com seu sucessor Eliseu junto ao rio Jordão?",
    "options": [
      "Foi levado por uma nuvem que cobriu o rio Jordão",
      "Foi conduzido por anjos até o alto de um monte",
      "Foi levado ao céu num redemoinho, após a aparição de um carro de fogo",
      "Desapareceu entre as chamas do altar junto ao rio"
    ],
    "correct": 2,
    "scriptureRef": "2 Reis 2:11-12",
    "hint": "Eliseu clamou: 'Meu pai, meu pai, carros de Israel e seus cavaleiros!' e apanhou o manto de Elias que caíra.",
    "explanation": "Elias foi transladado sem experimentar a morte para cumprir missões futuras na dispensação dos tempos."
  },
  {
    "id": "ot_037",
    "category": "ot",
    "difficulty": 2,
    "question": "O que Eliseu pediu a Elias antes de seu mestre ser arrebatado aos céus?",
    "options": [
      "Pediu que uma porção dobrada do espírito de Elias estivesse sobre ele",
      "O direito de servir como sacerdote em Jerusalém",
      "A bênção de jamais enfrentar os inimigos de Israel",
      "A autoridade para governar as tribos do norte"
    ],
    "correct": 0,
    "scriptureRef": "2 Reis 2:9",
    "hint": "Elias respondeu: 'Coisa difícil pediste; se me vires quando for tomado de ti, assim se te fará'.",
    "explanation": "Eliseu recebeu a porção dobrada e operou o dobro de milagres registrados durante seu ministério profético."
  },
  {
    "id": "ot_038",
    "category": "ot",
    "difficulty": 3,
    "question": "O que flutuou na superfície das águas do rio Jordão quando o profeta Eliseu cortou um pau e o lançou no local onde os filhos dos profetas trabalhavam?",
    "options": [
      "A ponta de uma lança perdida pelos profetas",
      "O recipiente de bronze usado para buscar água",
      "A corrente usada para puxar os troncos do rio",
      "A peça de ferro do machado que um dos homens havia tomado emprestado"
    ],
    "correct": 3,
    "scriptureRef": "2 Reis 6:5-7",
    "hint": "O discípulo gritara em desespero: 'Ai, meu senhor! porque era emprestado!'.",
    "explanation": "O ferro nadou sobrenaturalmente até a superfície para que o trabalhador pudesse devolvê-lo intacto."
  },
  {
    "id": "ot_039",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual rei de Judá adoeceu de morte e teve quinze anos acrescentados à sua vida após orar em lágrimas com o rosto voltado para a parede?",
    "options": [
      "Josias",
      "Asa",
      "Ezequias",
      "Usias"
    ],
    "correct": 2,
    "scriptureRef": "2 Reis 20:1-6; Isaías 38",
    "hint": "Como sinal divino, o profeta Isaías fez a sombra do relógio de sol de Acaz retroceder dez graus.",
    "explanation": "Deus ouviu as súplicas piedosas do rei Ezequias e libertou Jerusalém das mãos do terrível exército assírio de Senaqueribe."
  },
  {
    "id": "ot_040",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual jovem rei piedoso de Judá, coroado aos oito anos de idade, chorou e rasgou suas vestes quando o sumo sacerdote Hilquias encontrou o Livro da Lei no Templo abandonado?",
    "options": [
      "Manassés",
      "Joás",
      "Ezequias",
      "Josias"
    ],
    "correct": 3,
    "scriptureRef": "2 Reis 22:8-13; 23:1-3",
    "hint": "Ele removeu todos os ídolos pagãos e restaurou a celebração da Páscoa como não se via desde os tempos dos juízes.",
    "explanation": "Josias promoveu uma das mais profundas reformas espirituais de volta às escrituras de toda a história de Judá."
  },
  {
    "id": "ot_041",
    "category": "ot",
    "difficulty": 4,
    "question": "Segundo Josué 3:16, perto de que cidade as águas do Jordão que vinham de cima ficaram represadas?",
    "options": [
      "Perto de Adão e Zaretã",
      "Perto de Hebrom e Debir",
      "Perto de Gilgal e Jericó",
      "Perto de Betel e Ai"
    ],
    "correct": 0,
    "scriptureRef": "Josué 3:15-17",
    "hint": "As águas que desciam de cima pararam e levantaram-se num montão muito longe, junto a esta localidade.",
    "explanation": "As águas que vinham de cima se acumularam perto de Adão, ao lado de Zaretã; o povo atravessou em frente a Jericó."
  },
  {
    "id": "ot_042",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual profeta foi engolido por um peixe e, após se arrepender, pregou em Nínive, ficando irado porque o Senhor teve compaixão e não destruiu a cidade convertida?",
    "options": [
      "Habacuque",
      "Jonas",
      "Naum",
      "Miqueias"
    ],
    "correct": 1,
    "scriptureRef": "Jonas 3:10; 4:1-4",
    "hint": "Ele sentou-se fora da cidade sob uma aboboreira (quiqueiom) e reclamou com Deus.",
    "explanation": "Deus ensinou a Jonas a lição sublime de que Sua misericórdia alcança todas as nações que se arrependem com jejum e cilício."
  },
  {
    "id": "ot_043",
    "category": "ot",
    "difficulty": 1,
    "question": "Qual homem justo da terra de Uz perdeu todos os seus rebanhos, servos, dez filhos e a própria saúde física, mas permaneceu fiel dizendo: 'O Senhor deu, e o Senhor tirou; bendito seja o nome do Senhor'?",
    "options": [
      "Noé",
      "Abraão",
      "Enoque",
      "Jó"
    ],
    "correct": 3,
    "scriptureRef": "Jó 1:20-22",
    "hint": "Ele suportou as zombarias dos amigos no monturo de cinzas sem jamais amaldiçoar a Deus.",
    "explanation": "A paciência inquebrantável de Jó culminou na restauração em dobro de todas as suas bênçãos terrenas e espirituais."
  },
  {
    "id": "ot_044",
    "category": "ot",
    "difficulty": 2,
    "question": "Em Jó 19:25-26, qual é o sublime testemunho de esperança na ressurreição que ecoa através de todos os séculos?",
    "options": [
      "Seu Redentor vivia, e ele esperava ver a Deus em sua própria carne",
      "O Senhor me restaurará os filhos antes do fim de meus dias",
      "Minha justiça me livrará de descer à morada dos mortos",
      "Meu sofrimento cessará quando meus amigos reconhecerem o erro"
    ],
    "correct": 0,
    "scriptureRef": "Jó 19:25-26",
    "hint": "Imortalizado no oratório de Handel e nos hinos sagrados de todo o cristianismo.",
    "explanation": "Em meio a chagas e miséria indescritíveis, a alma de Jó vislumbrou a vitória eterna do Redentor sobre a morte."
  },
  {
    "id": "ot_045",
    "category": "ot",
    "difficulty": 1,
    "question": "Como começa o célebre e consolador Salmo 23 escrito pelo Rei Davi?",
    "options": [
      "'O Senhor é o meu pastor; nada me faltará'",
      "'Os céus declaram a glória de Deus'",
      "'Deus é o nosso refúgio e fortaleza'",
      "'Bendize, ó minha alma, ao Senhor'"
    ],
    "correct": 0,
    "scriptureRef": "Salmos 23:1",
    "hint": "Continua: 'Deitar-me faz em verdes pastos, guia-me mansamente a águas tranquilas'.",
    "explanation": "O Salmo 23 é o mais amado poema de confiança na terna provisão e proteção do Bom Pastor."
  },
  {
    "id": "ot_046",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual é o capítulo mais longo de toda a Bíblia Sagrada, composto por 176 versículos estruturados em 22 seções segundo o alfabeto hebraico dedicadas à glória da Palavra de Deus?",
    "options": [
      "Salmo 150",
      "Salmo 119",
      "Isaías 53",
      "Gênesis 1"
    ],
    "correct": 1,
    "scriptureRef": "Salmos 119",
    "hint": "Nele encontramos o versículo: 'Lâmpada para os meus pés é a tua palavra, e luz para o meu caminho'.",
    "explanation": "O Salmo 119 é um monumento acróstico hebraico de louvor contínuo aos preceitos e testemunhos da lei do Senhor."
  },
  {
    "id": "ot_047",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual é a célebre exortação de Provérbios 3:5-6 sobre como devemos nos conduzir diante do Senhor em todos os nossos caminhos?",
    "options": [
      "Seguir o conselho dos poderosos para assegurar caminhos de paz",
      "Buscar primeiro a aprovação dos sábios antes de orar ao Senhor",
      "Confiar no Senhor de todo o coração, reconhecendo-o em todos os caminhos",
      "Confiar nas próprias decisões depois de estudar os antigos reis"
    ],
    "correct": 2,
    "scriptureRef": "Provérbios 3:5-6",
    "hint": "Um dos princípios fundamentais para o jovem e o missionário discernirem a vontade divina.",
    "explanation": "Salomão ensina que a verdadeira paz provém de submeter a sabedoria humana finita à direção infinita de Deus."
  },
  {
    "id": "ot_048",
    "category": "ot",
    "difficulty": 2,
    "question": "Em Isaías 7:14, qual é a extraordinária profecia messiânica sobre o nascimento virginal de Cristo dada como sinal à casa de Davi?",
    "options": [
      "Um profeta semelhante a Moisés será levantado entre o povo",
      "Uma virgem conceberia um filho e lhe daria o nome de Emanuel",
      "Um descendente de Davi restaurará o trono de Jerusalém",
      "Um governante nascerá em Belém e apascentará Israel"
    ],
    "correct": 1,
    "scriptureRef": "Isaías 7:14; Mateus 1:22-23",
    "hint": "Emanuel significa: 'Deus conosco'.",
    "explanation": "Mateus cita diretamente essa passagem profética de Isaías para confirmar o nascimento de Jesus por Maria em Belém."
  },
  {
    "id": "ot_049",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual capítulo sublime de Isaías profetizou em detalhes comoventes os sofrimentos vicários do Messias como o 'Servo Sofredor' centenas de anos antes da cruz?",
    "options": [
      "Isaías, capítulo 60",
      "Isaías, capítulo 40",
      "Isaías, capítulo 53",
      "Isaías, capítulo 66"
    ],
    "correct": 2,
    "scriptureRef": "Isaías 53:3-5",
    "hint": "Abinádi citou este capítulo inteiro perante o Rei Noé no Livro de Mórmon em Mosias 14.",
    "explanation": "Isaías 53 retrata o Salvador como o cordeiro levado ao matadouro ferido pelas nossas transgressões."
  },
  {
    "id": "ot_050",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual profeta foi lançado numa cisterna escura e atolou-se no lodo por profetizar a queda de Jerusalém perante os babilônios, sendo resgatado com cordas por Ebede-Meleque?",
    "options": [
      "Daniel",
      "Ezequiel",
      "Jeremias",
      "Isaías"
    ],
    "correct": 2,
    "scriptureRef": "Jeremias 38:6-13",
    "hint": "Conhecido como o 'profeta que chorava' por sua compaixão pela destruição de Sião.",
    "explanation": "Jeremias sofreu severas perseguições das autoridades corruptas de Jerusalém nos dias do Rei Zedequias."
  },
  {
    "id": "ot_051",
    "category": "ot",
    "difficulty": 3,
    "question": "Na grandiosa visão de Ezequiel 37, o que o profeta viu no meio de um vale que se uniu osso ao seu osso, cobriu-se de carne e reviveu pelo sopro do Espírito?",
    "options": [
      "Pedras dispersas que formaram novamente os muros da cidade",
      "Árvores secas que voltaram a produzir folhas e frutos",
      "Ossos secos se uniram, receberam carne e vida e formaram um grande exército",
      "Cinzas que se transformaram em pessoas diante do profeta"
    ],
    "correct": 2,
    "scriptureRef": "Ezequiel 37:1-10",
    "hint": "Profecia sobre a ressurreição física e a restauração da esperança da casa de Israel.",
    "explanation": "A visão dos ossos secos testemunha a fidelidade de Deus em reviver e congregar o Seu povo nos últimos dias."
  },
  {
    "id": "ot_052",
    "category": "ot",
    "difficulty": 4,
    "question": "Na interpretação da Igreja restaurada, quais registros são associados às varas de Judá e de José em Ezequiel 37?",
    "options": [
      "As tábuas dos mandamentos e os rolos do templo",
      "Os registros dos reis de Judá e as cartas dos sacerdotes",
      "A lei de Moisés e os escritos dos profetas",
      "A Bíblia, associada a Judá, e o Livro de Mórmon, associado a José"
    ],
    "correct": 3,
    "scriptureRef": "Ezequiel 37:16-19; 1 Néfi 13:40-41",
    "hint": "Profecia central da Restauração unindo os dois testamentos sagrados de Jesus Cristo.",
    "explanation": "Ezequiel profetizou a convergência providencial da Bíblia Sagrada e do Livro de Mórmon como testemunhas unificadas de Cristo."
  },
  {
    "id": "ot_053",
    "category": "ot",
    "difficulty": 2,
    "question": "O que Daniel e seus três companheiros hebreus pediram para comer durante dez dias na corte da Babilônia em vez dos manjares e vinho da mesa do rei?",
    "options": [
      "Legumes e água pura",
      "Frutas e leite de cabra",
      "Pão e azeite",
      "Peixe assado"
    ],
    "correct": 0,
    "scriptureRef": "Daniel 1:11-15",
    "hint": "Ao final dos dez dias, seus semblantes pareciam mais robustos e sábios do que todos os jovens da corte.",
    "explanation": "A fidelidade de Daniel à lei de saúde divina deu-lhe sabedoria dez vezes superior aos sábios babilônicos."
  },
  {
    "id": "ot_054",
    "category": "ot",
    "difficulty": 3,
    "question": "Na interpretação de Daniel sobre o sonho da grande estátua de Nabucodonosor, o que representa a pedra cortada do monte sem mãos que esmiuçou a estátua e encheu a Terra?",
    "options": [
      "A cidade de Jerusalém reconstruída depois do exílio",
      "O Império Romano que substituiria os reinos anteriores",
      "A aliança dos reis que derrotariam o reino da Babilônia",
      "O reino que Deus estabeleceria e que jamais seria destruído por outro povo"
    ],
    "correct": 3,
    "scriptureRef": "Daniel 2:34-35, 44-45",
    "hint": "Profecia messiânica sublime que os santos dos últimos dias identificam com a Restauração da Igreja de Jesus Cristo.",
    "explanation": "A pedra que enche toda a Terra simboliza a Igreja restaurada rolando até os confins do globo terrestre."
  },
  {
    "id": "ot_055",
    "category": "ot",
    "difficulty": 3,
    "question": "Quem apareceu caminhando ileso no meio da fornalha ardente aquecida sete vezes mais ao lado de Sadraque, Mesaque e Abednego?",
    "options": [
      "Um soldado enviado pelo rei para retirar os três jovens",
      "Um profeta que viera advertir o rei sobre o julgamento",
      "Uma quarta figura semelhante ao Filho de Deus",
      "Um sacerdote de Jerusalém carregando o incensário"
    ],
    "correct": 2,
    "scriptureRef": "Daniel 3:24-25",
    "hint": "Nabucodonosor exclamou atônito: 'Não lançamos nós três homens atados dentro do fogo? Eis que vejo quatro homens soltos...'.",
    "explanation": "O próprio Senhor Jesus Cristo manifestou Sua presença salvadora para proteger Seus santos servos fiéis."
  },
  {
    "id": "ot_056",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual misteriosa inscrição em aramaico uma mão invisível escreveu na parede do palácio de Belsazar durante um banquete idólatra com os vasos sagrados do templo?",
    "options": [
      "'Aleph, Beth, Gimel, Daleth'",
      "'Mene, Mene, Tequel, Ufarsim'",
      "'Kokaubeam, Oliblis, Shineha'",
      "'Sanctus, Sanctus, Dominus'"
    ],
    "correct": 1,
    "scriptureRef": "Daniel 5:5, 25-28",
    "hint": "Daniel interpretou: 'Contou Deus o teu reino... pesado foste na balança e achado em falta... dividido foi o teu reino'.",
    "explanation": "Naquela mesma noite o rei Belsazar foi morto e Dario, o medo, apoderou-se do império babilônico."
  },
  {
    "id": "ot_057",
    "category": "ot",
    "difficulty": 2,
    "question": "Em Malaquias 3:10, qual promessa extraordinária o Senhor faz àqueles que trazem todos os dízimos à casa do tesouro?",
    "options": [
      "Dispensar os fiéis das demais ofertas exigidas pela lei",
      "Abrir as janelas do céu e derramar uma bênção abundante",
      "Conceder a cada família uma herança adicional em Canaã",
      "Reunir todos os tributos das nações no tesouro de Israel"
    ],
    "correct": 1,
    "scriptureRef": "Malaquias 3:10",
    "hint": "'Provai-me nisto, diz o Senhor dos Exércitos, se eu não vos abrir as janelas do céu... e repreenderei o devorador'.",
    "explanation": "O princípio da lei do dízimo é associado a bênçãos espirituais e temporais abundantes concedidas pelo Senhor."
  },
  {
    "id": "ot_058",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual é a última profecia solene de todo o Velho Testamento em Malaquias 4:5-6 sobre o retorno do profeta Elias?",
    "options": [
      "Elias viria antes do dia do Senhor, voltando os corações dos pais e dos filhos",
      "Elias conduzirá as tribos através do mar até a terra prometida",
      "Elias ungirá um novo rei antes da reconstrução de Jerusalém",
      "Elias reunirá os levitas para restaurar os sacrifícios antigos"
    ],
    "correct": 0,
    "scriptureRef": "Malaquias 4:5-6",
    "hint": "Esta chave do sacerdócio foi restaurada por Elias em pessoa a Joseph Smith no Templo de Kirtland em 1836 (D&C 110).",
    "explanation": "O retorno de Elias confere o poder de selamento que une as gerações familiares para a eternidade nos templos sagrados."
  },
  {
    "id": "ot_059",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual profeta menor profetizou que nos últimos dias os fiéis de Israel subiriam ao monte Sião como 'salvadores' para julgar a terra?",
    "options": [
      "Obadias",
      "Zacarias",
      "Habacuque",
      "Malaquias"
    ],
    "correct": 0,
    "scriptureRef": "Obadias 1:21",
    "hint": "Joseph Smith ensinou que nos tornamos 'salvadores no monte Sião' quando realizamos as ordenanças vicárias pelos nossos antepassados no templo.",
    "explanation": "Obadias profetizou a obra de salvação e redenção genealógica operada pelos santos no monte do Senhor."
  },
  {
    "id": "ot_060",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual foi o rei persa inspirado por Deus que promulgou o célebre decreto permitindo aos judeus exilados na Babilônia retornarem a Jerusalém e reconstruírem o Templo?",
    "options": [
      "Artaxerxes, rei da Pérsia",
      "Ciro, rei da Pérsia",
      "Dario, rei da Pérsia",
      "Xerxes, rei da Pérsia"
    ],
    "correct": 1,
    "scriptureRef": "Esdras 1:1-3; Isaías 44:28",
    "hint": "Isaías o chamou profeticamente pelo nome mais de cem anos antes de seu nascimento.",
    "explanation": "O decreto de Ciro pôs fim aos 70 anos de cativeiro babilônico e possibilitou o retorno liderado por Zorobabel."
  },
  {
    "id": "ot_061",
    "category": "ot",
    "difficulty": 3,
    "question": "Quem era o copeiro do rei persa que liderou com coragem heroica a reconstrução dos muros em ruínas de Jerusalém em apenas 52 dias contra inimigos conspiradores?",
    "options": [
      "Zorobabel",
      "Mordecai",
      "Neemias",
      "Esdras"
    ],
    "correct": 2,
    "scriptureRef": "Neemias 1:11; 6:15",
    "hint": "Ele ordenou que os construtores trabalhassem com uma mão na colher de pedreiro e a outra na arma de defesa.",
    "explanation": "A abnegação e determinação de Neemias restauraram a segurança e a dignidade civil da cidade santa de Sião."
  },
  {
    "id": "ot_062",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual sacerdote e escriba da linhagem de Arão leu solenemente o Livro da Lei de Moisés desde a manhã até o meio-dia perante todo o povo reunido na Porta das Águas em Jerusalém?",
    "options": [
      "Neemias",
      "Esdras",
      "Zorobabel",
      "Jesua"
    ],
    "correct": 1,
    "scriptureRef": "Neemias 8:1-8",
    "hint": "Ele subiu a um púlpito de madeira e explicava com clareza o sentido das escrituras ao povo em pranto.",
    "explanation": "Esdras liderou o grande renascimento espiritual e bíblico pós-exílico em Israel."
  },
  {
    "id": "ot_063",
    "category": "ot",
    "difficulty": 3,
    "question": "Em Provérbios 31, qual poema acróstico famoso elogia a mulher sábia, virtuosa e trabalhadora cujo valor excede o de finas joias?",
    "options": [
      "O cântico de Miriã junto ao mar",
      "A oração de gratidão de Ana",
      "O cântico de vitória de Débora",
      "O poema de elogio à mulher virtuosa e trabalhadora"
    ],
    "correct": 3,
    "scriptureRef": "Provérbios 31:10-31",
    "hint": "'Enganosa é a graça, e vã é a formosura, mas a mulher que teme ao Senhor, essa será louvada.'",
    "explanation": "Provérbios 31 celebra a nobreza moral, a liderança compassiva e a dignidade santa da mulher que honra a Deus."
  },
  {
    "id": "ot_064",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual profeta do Velho Testamento profetizou que nos últimos dias o Senhor derramaria o Seu Espírito sobre toda a carne, com filhos e filhas profetizando e velhos tendo sonhos?",
    "options": [
      "Joel",
      "Amós",
      "Oséias",
      "Sofonias"
    ],
    "correct": 0,
    "scriptureRef": "Joel 2:28-29; Atos 2:16-18",
    "hint": "O apóstolo Pedro citou textualmente esta passagem no dia de Pentecostes.",
    "explanation": "O anjo Morôni também citou essa profecia a Joseph Smith em 1823, afirmando que ela estava para se cumprir em plenitude."
  },
  {
    "id": "ot_065",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual profeta advertiu a Israel sobre uma futura fome espiritual terrível sobre a terra: 'Não de pão, nem sede de água, mas de ouvir as palavras do Senhor'?",
    "options": [
      "Amós",
      "Zacarias",
      "Malaquias",
      "Habacuque"
    ],
    "correct": 0,
    "scriptureRef": "Amós 8:11-12",
    "hint": "'E irão errantes de um mar a outro... buscando a palavra do Senhor, e não a acharão.'",
    "explanation": "Amós profetizou com clareza a Grande Apostasia e a privação da palavra viva de revelação que precedeu a Restauração."
  },
  {
    "id": "ot_066",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual profeta messiânico profetizou com precisão geográfica que o Rei de Israel entraria em Jerusalém 'humilde e montado sobre um jumento, sobre um jumentinho, filho de jumenta'?",
    "options": [
      "Jeremias",
      "Zacarias",
      "Malaquias",
      "Isaías"
    ],
    "correct": 1,
    "scriptureRef": "Zacarias 9:9; Mateus 21:4-5",
    "hint": "Cumprido literalmente por Jesus Cristo na Sua triunfal Entrada em Jerusalém no Domingo de Ramos.",
    "explanation": "Zacarias antecipou com séculos de antecedência a humilde e gloriosa entrada do Príncipe da Paz."
  },
  {
    "id": "ot_067",
    "category": "ot",
    "difficulty": 4,
    "question": "Em Zacarias 11:12-13, qual foi o preço profético exato estipulado pelo salário do Bom Pastor, lançado para o oleiro na casa do Senhor?",
    "options": [
      "Duzentas moedas de prata",
      "Sessenta moedas de prata",
      "Trinta moedas de prata",
      "Cinquenta moedas de prata"
    ],
    "correct": 2,
    "scriptureRef": "Zacarias 11:12-13; Mateus 26:15",
    "hint": "O mesmo valor que os sacerdotes pagaram a Judas Iscariotes pela traição de Cristo.",
    "explanation": "Uma das profecias mais minuciosas do Velho Testamento que se cumpriu ao pé da letra no Novo Testamento."
  },
  {
    "id": "ot_068",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual pergunta sobre feridas aparece em Zacarias 13:6?",
    "options": [
      "Por que estão vermelhas as tuas vestes?",
      "Quem é este que vem de Edom?",
      "Onde está o rei dos judeus que nasceu?",
      "Que feridas são estas nas tuas mãos?"
    ],
    "correct": 3,
    "scriptureRef": "Zacarias 13:6; D&C 45:51-52",
    "hint": "D&C 45 confirma que naquele momento glorioso eles olharão para Ele e chorarão ao reconhecerem o Redentor.",
    "explanation": "Esta sublime passagem descreve o reconhecimento final de Jesus Cristo como o Messias prometido por Seu povo."
  },
  {
    "id": "ot_069",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual é a cidade onde Deus confundiu a linguagem de toda a Terra quando os homens soberbos tentaram construir uma torre cujo topo tocasse o céu?",
    "options": [
      "Nínive",
      "Babel",
      "Tiro",
      "Ur dos Caldeus"
    ],
    "correct": 1,
    "scriptureRef": "Gênesis 11:1-9",
    "hint": "O nome Babel deriva do hebraico que significa 'confusão'.",
    "explanation": "A dispersão de Babel espalhou as famílias humanas pela Terra e deu origem à jornada dos jareditas no Livro de Mórmon."
  },
  {
    "id": "ot_070",
    "category": "ot",
    "difficulty": 3,
    "question": "Quem era o sogro madianita de Moisés, sacerdote de Midiã, que lhe deu conselhos de liderança organizando Israel em chefes de mil, de cem, de cinquenta e de dez?",
    "options": [
      "Jetro",
      "Labão",
      "Potifar",
      "Balaão"
    ],
    "correct": 0,
    "scriptureRef": "Êxodo 18:13-26",
    "hint": "Pai de Zípora, esposa de Moisés.",
    "explanation": "O conselho de Jetro estabeleceu a sábia delegação de responsabilidades que preservou as forças de Moisés perante o povo."
  },
  {
    "id": "ot_071",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual filho de Jônatas ficou com deficiência nos dois pés quando criança e depois foi acolhido à mesa do rei Davi?",
    "options": [
      "Mefibosete",
      "Armoni",
      "Isbosete",
      "Quiliabe"
    ],
    "correct": 0,
    "scriptureRef": "2 Samuel 9:3-13",
    "hint": "Davi restituiu-lhe todas as terras de seu avô Saul e fez com que comesse continuamente como filho de rei à sua mesa.",
    "explanation": "O terno cuidado de Davi para com Mefibosete é um exemplo imortal de fidelidade aos convênios de amizade."
  },
  {
    "id": "ot_072",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual rei de Judá foi ferido com lepra na testa no próprio Templo de Jerusalém por tentar queimar incenso no altar, função exclusiva dos sacerdotes levitas?",
    "options": [
      "Uzias",
      "Acaz",
      "Roboão",
      "Manassés"
    ],
    "correct": 0,
    "scriptureRef": "2 Crônicas 26:16-21",
    "hint": "Oitenta bravos sacerdotes o confrontaram, e ao encolerizar-se, a lepra brotou imediatamente em sua fronte.",
    "explanation": "Uzias permaneceu leproso e isolado até o dia de sua morte por usurpar a sagrada autoridade do sacerdócio."
  },
  {
    "id": "ot_073",
    "category": "ot",
    "difficulty": 4,
    "question": "Em qual cidade filisteia a estátua do ídolo pagão Dagom caiu por terra com o rosto em pó diante da Arca da Aliança capturada, tendo sua cabeça e mãos quebradas?",
    "options": [
      "Gaza",
      "Asdode",
      "Gate",
      "Ascalom"
    ],
    "correct": 1,
    "scriptureRef": "1 Samuel 5:1-5",
    "hint": "Os sacerdotes filisteus apavoraram-se e enviaram a Arca de cidade em cidade até a devolverem com ofertas a Israel.",
    "explanation": "A humilhação do ídolo Dagom demonstrou a soberania absoluta do Deus de Israel sobre os falsos deuses das nações."
  },
  {
    "id": "ot_074",
    "category": "ot",
    "difficulty": 3,
    "question": "O que o profeta Isaías respondeu quando teve sua visão no templo e o Senhor perguntou: 'A quem enviarei, e quem há de ir por nós?'?",
    "options": [
      "'Eis-me aqui, envia-me a mim'",
      "'Rogo-te que escolhas outro mais forte'",
      "'Não sou homem eloquente'",
      "'Dá-me tempo para preparar-me'"
    ],
    "correct": 0,
    "scriptureRef": "Isaías 6:8",
    "hint": "Um serafim havia acabado de purificar seus lábios com uma brasa viva tirada do altar celeste.",
    "explanation": "A pronta submissão de Isaías é o lema eterno da prontidão de todos os servos e missionários chamados por Deus."
  },
  {
    "id": "ot_075",
    "category": "ot",
    "difficulty": 3,
    "question": "Em Êxodo 34:29-35, por que Moisés teve que colocar um véu sobre o seu rosto quando descia do monte Sinai para falar com o povo de Israel?",
    "options": [
      "O véu fazia parte das vestes exigidas a todos os profetas",
      "A pele de seu rosto resplandecia após falar com Deus, e o povo temia aproximar-se",
      "Seu rosto estava marcado pelas cinzas dos sacrifícios",
      "O povo havia sido proibido de ver o rosto do legislador"
    ],
    "correct": 1,
    "scriptureRef": "Êxodo 34:29-35",
    "hint": "A glória da presença de Deus refletia-se de maneira física e visível na face do profeta.",
    "explanation": "Moisés colocava o véu perante o povo e o retirava quando entrava na presença do Senhor para conversar com Ele."
  },
  {
    "id": "ot_076",
    "category": "ot",
    "difficulty": 2,
    "question": "Quantos dias e noites choveu ininterruptamente sobre a Terra durante o dilúvio na época de Noé?",
    "options": [
      "Cem dias e noites",
      "Setenta dias e noites",
      "Cento e cinquenta dias e noites",
      "Quarenta dias e noites"
    ],
    "correct": 3,
    "scriptureRef": "Gênesis 7:12",
    "hint": "O número 40 na Bíblia é tradicionalmente associado a períodos de provação, purificação e espera.",
    "explanation": "A chuva torrencial e as fontes do grande abismo romperam-se cobrindo todos os altos montes sob os céus."
  },
  {
    "id": "ot_077",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual foi o sinal do convênio que Deus pôs no céu entre Si e toda criatura vivente prometendo que as águas nunca mais se tornariam em dilúvio para destruir a carne?",
    "options": [
      "Uma coluna de fogo sobre as águas",
      "Uma nuvem permanente sobre a terra",
      "O arco-íris colocado nas nuvens como sinal do convênio",
      "Uma estrela sobre os montes de Ararate"
    ],
    "correct": 2,
    "scriptureRef": "Gênesis 9:12-17",
    "hint": "'O meu arco tenho posto nas nuvens; este será por sinal da aliança entre mim e a terra.'",
    "explanation": "O arco celeste é o memorial eterno da fidelidade e misericórdia do Criador para com toda a criação."
  },
  {
    "id": "ot_078",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual filho de Abraão nasceu de sua serva egípcia Hagar e tornou-se pai de doze príncipes conforme a promessa do Senhor?",
    "options": [
      "Isaque",
      "Zinrã",
      "Ismael",
      "Midiã"
    ],
    "correct": 2,
    "scriptureRef": "Gênesis 16:15; 25:12-16",
    "hint": "O anjo do Senhor disse a Hagar no deserto: 'E chamarás o seu nome Ismael, porquanto o Senhor ouviu a tua aflição'.",
    "explanation": "Deus abençoou Ismael e multiplicou sua semente em cumprimento à promessa feita a Abraão."
  },
  {
    "id": "ot_079",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual foi a esposa que Jacó amava profundamente e por quem trabalhou quatorze anos como pastor para seu tio Labão em Padã-Arã?",
    "options": [
      "Zilpa",
      "Bila",
      "Raquel",
      "Lia"
    ],
    "correct": 2,
    "scriptureRef": "Gênesis 29:18-30",
    "hint": "Mãe de José e Benjamim, que faleceu no caminho de Belém.",
    "explanation": "Jacó serviu sete anos por Raquel que lhe pareceram poucos dias pelo muito que a amava, e mais sete após o engano de Labão com Lia."
  },
  {
    "id": "ot_080",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual filho de Davi rebelou-se contra o próprio pai, proclamou-se rei em Hebrom e teve seus longos cabelos presos nos ramos de um grande carvalho ao fugir em sua mula?",
    "options": [
      "Absalão",
      "Adonias",
      "Amnon",
      "Salomão"
    ],
    "correct": 0,
    "scriptureRef": "2 Samuel 18:9-15",
    "hint": "Davi chorou amargamente sua morte clamando: 'Meu filho Absalão, meu filho, meu filho Absalão! Quem me dera que eu morrera por ti!'.",
    "explanation": "A tragédia de Absalão ilustra a dor paternal de Davi e as consequências trágicas da sedição e do orgulho."
  },
  {
    "id": "ot_081",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual era o nome do general do exército de Davi que liderou suas tropas com bravura incontestável durante a maior parte de seu reinado?",
    "options": [
      "Benaia",
      "Abner",
      "Amasa",
      "Joabe"
    ],
    "correct": 3,
    "scriptureRef": "2 Samuel 8:16",
    "hint": "Filho de Zeruia, sobrinho de Davi.",
    "explanation": "Joabe foi um comandante militar feroz e eficaz que conquistou a fortaleza de Sião dos jebuseus."
  },
  {
    "id": "ot_082",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual valente soldado de elite de Davi pulou numa cova num dia de neve e matou um leão feroz com as próprias mãos?",
    "options": [
      "Eleazar, filho de Dodô",
      "Samá, filho de Agé",
      "Abisai, filho de Zeruia",
      "Benaia, filho de Joiada"
    ],
    "correct": 3,
    "scriptureRef": "2 Samuel 23:20",
    "hint": "Ele também matou dois heróis valorosos de Moabe e um gigante egípcio arrancando a lança de sua mão.",
    "explanation": "Benaia tornou-se o chefe da guarda real pessoal de Davi e de Salomão por sua bravura incomparável."
  },
  {
    "id": "ot_083",
    "category": "ot",
    "difficulty": 3,
    "question": "Quem Joabe enviou a Davi com uma história para convencê-lo a trazer Absalão de volta do exílio?",
    "options": [
      "Mical, filha do rei Saul",
      "Hulda, mulher que exercia o dom de profecia",
      "Uma mulher de Tecoa sem nome registrado",
      "Abigail, antiga esposa de Nabal"
    ],
    "correct": 2,
    "scriptureRef": "2 Samuel 14:1-14",
    "hint": "Ela declarou com eloqüência profunda: 'Porque certamente morreremos, e seremos como águas derramadas na terra... mas Deus não tira a vida, senão que cogita meios para que não fique banido dele o seu desterrado'.",
    "explanation": "Sua comovente oratória tocou o coração de Davi e permitiu a restauração de seu filho banido."
  },
  {
    "id": "ot_084",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual conselheiro sábio de Davi passou para o lado rebelde de Absalão, e ao ver que seu conselho não fora seguido, foi para sua casa e se enforcou?",
    "options": [
      "Husai",
      "Aitofel",
      "Zadoque",
      "Abiatar"
    ],
    "correct": 1,
    "scriptureRef": "2 Samuel 17:23",
    "hint": "O conselho deste homem naqueles dias era tido como se alguém consultasse a palavra de Deus.",
    "explanation": "A traição de Aitofel foi frustrada pelas orações de Davi e pela lealdade de Husai, o arquita."
  },
  {
    "id": "ot_085",
    "category": "ot",
    "difficulty": 2,
    "question": "Qual mulher formosa e prudente evitou uma carnificina levando apressadamente pães, odres de vinho, ovelhas preparadas e passas a Davi após a grosseria de seu tolo marido Nabal?",
    "options": [
      "Abigail",
      "Bate-Seba",
      "Mical",
      "Ainoã"
    ],
    "correct": 0,
    "scriptureRef": "1 Samuel 25:18-35",
    "hint": "Após a morte súbita de Nabal pelo Senhor, Davi enviou mensageiros e tomou esta virtuosa mulher por esposa.",
    "explanation": "A prudência e humildade de Abigail pacificaram a ira de Davi e preservaram suas mãos imaculadas de sangue inocente."
  },
  {
    "id": "ot_086",
    "category": "ot",
    "difficulty": 3,
    "question": "Onde o Rei Saul foi consultar ilegalmente uma mulher médium espírita na véspera de sua trágica morte no Monte Gilboa contra os filisteus?",
    "options": [
      "Em Siló",
      "Em En-Dor",
      "Em Bete-El",
      "Em Gibeá"
    ],
    "correct": 1,
    "scriptureRef": "1 Samuel 28:7-14",
    "hint": "Ele pediu que fizesse subir o espírito do falecido profeta Samuel.",
    "explanation": "A consulta de Saul à feiticeira de En-Dor selou seu abandono espiritual total antes de perecer no combate."
  },
  {
    "id": "ot_087",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual era o nome dos dois filhos de Arão que ofereceram 'fogo estranho' perante o Senhor no santuário e foram consumidos pelo fogo que saiu da presença de Deus?",
    "options": [
      "Eleazar e Itamar",
      "Coré e Datã",
      "Hofni e Fineias",
      "Nadabe e Abiú"
    ],
    "correct": 3,
    "scriptureRef": "Levítico 10:1-2",
    "hint": "Arão guardou silêncio perante a santidade terrível do juízo do Senhor.",
    "explanation": "O trágico fim de Nadabe e Abiú ensinou a Israel a estrita santidade e reverência exigidas nas ordenanças divinas."
  },
  {
    "id": "ot_088",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual levita liderou uma rebelião de 250 príncipes da congregação contra Moisés e Arão no deserto e foi tragado vivo pelas entranhas da terra que se abriu sob seus pés?",
    "options": [
      "Coré",
      "Balaão",
      "Acã",
      "Zinri"
    ],
    "correct": 0,
    "scriptureRef": "Números 16:1-33",
    "hint": "Eles acusaram Moisés dizendo: 'Basta-vos, pois que toda a congregação é santa... por que pois vos elevais sobre a congregação do Senhor?'.",
    "explanation": "A terra abriu sua boca e tragou Coré e suas tendas por sua insolente rebelião contra a autoridade ordenada por Deus."
  },
  {
    "id": "ot_089",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual homem israelita da tribo de Judá escondeu secretamente em sua tenda uma capa babilônica de valor, duzentos siclos de prata e uma cunha de ouro do anátema de Jericó, causando a derrota em Ai?",
    "options": [
      "Acã, filho de Carmi",
      "Fineias, filho de Eleazar",
      "Calebe, filho de Jefoné",
      "Zabdi, descendente de Zera"
    ],
    "correct": 0,
    "scriptureRef": "Josué 7:19-26",
    "hint": "Ele confessou: 'Com efeito pequei contra o Senhor Deus de Israel... vi e cobicei-os e tomei-os'.",
    "explanation": "O vale onde Acã foi apedrejado e sepultado foi chamado de Vale de Acor (vale da tribulação)."
  },
  {
    "id": "ot_090",
    "category": "ot",
    "difficulty": 3,
    "question": "Qual rio abençoado o profeta Ezequiel viu brotando de debaixo do limiar do Templo em direção ao oriente, tornando doces as águas amargas do Mar Morto?",
    "options": [
      "As águas curadoras que brotavam de debaixo do limiar do templo",
      "As águas do Querite onde Elias se havia refugiado",
      "As águas do Jordão depois de atravessarem Jericó",
      "As águas do Quisom vindas do monte Carmelo"
    ],
    "correct": 0,
    "scriptureRef": "Ezequiel 47:1-12",
    "hint": "O rio tornava-se cada vez mais profundo: pelas águas aos artelhos, aos joelhos, aos lombos e águas que se deviam passar a nado.",
    "explanation": "O rio de Ezequiel simboliza a influência vivificante e curadora do evangelho e das ordenanças do templo divino."
  },
  {
    "id": "ot_091",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual rei de Judá escondeu-se no quarto das camas do Templo quando bebê, protegido por sua tia Joseba da ira assassina de sua avó usurpadora Atalia?",
    "options": [
      "Ezequias",
      "Josafat",
      "Joás",
      "Uzias"
    ],
    "correct": 2,
    "scriptureRef": "2 Reis 11:1-3",
    "hint": "Aos sete anos de idade, o fiel sumo sacerdote Joiada o coroou rei e a rainha ímpia foi executada.",
    "explanation": "Joás foi preservado para manter a promessa divina de uma lâmpada contínua para a linhagem de Davi."
  },
  {
    "id": "ot_092",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual jovem nobre judia tornou-se rainha da Pérsia no lugar de Vasti e desbaratou o plano maligno de Hamã de exterminar todos os judeus do império?",
    "options": [
      "Sarai, depois chamada Sara",
      "Abigail, antiga esposa de Nabal",
      "Noemi, que pediu ser chamada Mara",
      "Ester, também chamada Hadassa"
    ],
    "correct": 3,
    "scriptureRef": "Ester 2:7; 7:1-10",
    "hint": "Mardoqueu lembrou-lhe: 'E quem sabe se para tal tempo como este chegaste a este reino?'.",
    "explanation": "O jejum de três dias de Ester e sua coragem heroica salvaram a semente de Israel do genocídio na Pérsia."
  },
  {
    "id": "ot_093",
    "category": "ot",
    "difficulty": 3,
    "question": "O que aconteceu com o ímpio conspirador Hamã que havia construído uma forca de cinquenta côvados de altura para enforcar o fiel Mardoqueu?",
    "options": [
      "Foi preso na fortaleza enquanto o rei julgava seus filhos",
      "Foi desterrado após perder seus bens e sua autoridade",
      "Foi executado no mesmo campo onde reunira seus soldados",
      "Foi morto na forca que preparara para Mardoqueu"
    ],
    "correct": 3,
    "scriptureRef": "Ester 7:9-10",
    "hint": "A festa judaica de Purim celebra até hoje essa dramática libertação divina.",
    "explanation": "A justiça divina fez com que a forca preparada com ódio para o justo servisse de instrumento para o próprio carrasco."
  },
  {
    "id": "ot_094",
    "category": "ot",
    "difficulty": 3,
    "question": "Em Salmos 127:3, como os filhos são chamados pelo sábio salmista inspirado?",
    "options": [
      "Escudo dos justos e sinal da aliança",
      "Herança do Senhor, sendo o fruto do ventre o seu galardão",
      "Coroa de sabedoria e fonte de entendimento",
      "Raízes da casa e fundamento da cidade"
    ],
    "correct": 1,
    "scriptureRef": "Salmos 127:3",
    "hint": "O versículo continua: 'Como flechas na mão do guerreiro, assim são os filhos da mocidade'.",
    "explanation": "As escrituras ensinam a sagrada santidade e dignidade divina da família e da posteridade eterna."
  },
  {
    "id": "ot_095",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual profeta menor casou-se com uma mulher infiel chamada Gômer por ordem de Deus para ilustrar a dor e a misericórdia inabalável do Senhor para com Israel adúltero?",
    "options": [
      "Joel",
      "Oséias",
      "Miqueias",
      "Amós"
    ],
    "correct": 1,
    "scriptureRef": "Oséias 1:2-3; 3:1-3",
    "hint": "Ele comprou sua própria esposa de volta do mercado da escravidão por quinze peças de prata e uma medida de cevada.",
    "explanation": "A vida de Oséias é uma das mais profundas e pungentes parábolas vivas do amor restaurador incondicional de Deus por Seu povo."
  },
  {
    "id": "ot_096",
    "category": "ot",
    "difficulty": 4,
    "question": "Em Miqueias 6:8, qual é o resumo definitivo que o Senhor exige de todo homem para andar retamente perante Ele?",
    "options": [
      "Oferecer sacrifícios, ampliar o templo e guardar suas portas",
      "Praticar a justiça, amar a benevolência e andar com Deus",
      "Jejuar regularmente, vestir-se de saco e viver no deserto",
      "Reunir riquezas, resgatar terras e fortalecer as muralhas"
    ],
    "correct": 1,
    "scriptureRef": "Miqueias 6:8",
    "hint": "'Ele te declarou, ó homem, o que é bom; e que é o que o Senhor pede de ti senão...'",
    "explanation": "A essência da verdadeira adoração a Deus reside na retidão moral, na misericórdia amorosa e na humildade genuína."
  },
  {
    "id": "ot_097",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual profeta menor orou no capítulo 3 dizendo que mesmo se a figueira não florescer, nem houver fruto na vide, e o gado for arrebatado do curral, ainda assim se alegrará no Senhor?",
    "options": [
      "Zacarias",
      "Sofonias",
      "Habacuque",
      "Ageu"
    ],
    "correct": 2,
    "scriptureRef": "Habacuque 3:17-18",
    "hint": "'Todavia eu me alegrarei no Senhor; exultarei no Deus da minha salvação.'",
    "explanation": "Habacuque expressou a mais sublime e pura fé incondicional que confia em Deus independentemente das circunstâncias materiais."
  },
  {
    "id": "ot_098",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual sacerdote e líder zeloso atravessou com uma lança um príncipe de Israel e uma mulher midianita pecadores em pleno acampamento, cessando a praga mortífera em Sitim?",
    "options": [
      "Nadabe, filho de Arão",
      "Fineias, filho de Eleazar",
      "Hofni, filho de Eli",
      "Zadoque, filho de Aitube"
    ],
    "correct": 1,
    "scriptureRef": "Números 25:6-13",
    "hint": "O Senhor fez com ele uma 'aliança de paz e sacerdócio perpétuo' por seu zelo santo pela honra de Deus.",
    "explanation": "O ato de Fineias aplacou a ira divina sobre Israel e preservou a santidade do povo no deserto."
  },
  {
    "id": "ot_099",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual rei de Judá construiu um túnel subterrâneo escavado na rocha sólida com 533 metros de comprimento para canalizar as águas da fonte de Giom para dentro das muralhas de Jerusalém durante o cerco assírio?",
    "options": [
      "Salomão",
      "Davi",
      "Ezequias",
      "Josias"
    ],
    "correct": 2,
    "scriptureRef": "2 Reis 20:20; 2 Crônicas 32:30",
    "hint": "A célebre inscrição de Siloé, encontrada no interior do túnel, documenta os operários cavando de ambos os lados até se encontrarem no meio.",
    "explanation": "A monumental obra de engenharia de Ezequias garantiu água fresca para a cidade e secou as fontes externas contra os assírios."
  },
  {
    "id": "ot_100",
    "category": "ot",
    "difficulty": 4,
    "question": "Qual foi a última praga que destruiu o exército assírio de Senaqueribe acampado ao redor de Jerusalém numa só noite após as orações de Ezequias e Isaías?",
    "options": [
      "Uma enchente arrastou as tropas reunidas junto às muralhas",
      "O anjo do Senhor saiu e feriu 185 mil homens no acampamento dos assírios",
      "Uma batalha noturna destruiu os acampamentos assírios",
      "Uma doença obrigou Senaqueribe a abandonar todo o cerco"
    ],
    "correct": 1,
    "scriptureRef": "2 Reis 19:35; Isaías 37:36",
    "hint": "Pela manhã, o rei Senaqueribe levantou-se e viu apenas os cadáveres de seu imenso exército dizimado.",
    "explanation": "A miraculosa libertação de Jerusalém confirmou a palavra infalível do profeta Isaías de que o rei da Assíria não atiraria nenhuma flecha contra a cidade santa."
  }
]

def build():
    target = Path(__file__).resolve().with_name("data_ot.js")
    content = "/** Banco revisado: 100 perguntas; alternativas e gabaritos sincronizados. */\nvar QUESTIONS_OT = "
    content += json.dumps(questions, ensure_ascii=False, indent=2) + ";\n"
    target.write_text(content, encoding="utf-8")
    print(f"Sucesso: {target.name} gerado com {len(questions)} perguntas.")

if __name__ == "__main__":
    build()
