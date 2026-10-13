# -*- coding: utf-8 -*-
"""Gerador do banco NT; mantém textos revisados e gabaritos distribuídos."""
import json
from pathlib import Path

questions = [
  {
    "id": "nt_001",
    "category": "nt",
    "difficulty": 1,
    "question": "Qual imperador romano decretou o alistamento (recenseamento) que fez José e Maria viajarem de Nazaré para Belém?",
    "options": [
      "Nero Cláudio César",
      "César Augusto",
      "Tibério César",
      "Cláudio César"
    ],
    "correct": 1,
    "scriptureRef": "Lucas 2:1",
    "hint": "Ele foi o primeiro imperador do Império Romano, sob cujo governo nasceu Jesus.",
    "explanation": "Lucas 2:1 registra o decreto imperial de César Augusto para o recenseamento de todo o mundo habitado."
  },
  {
    "id": "nt_002",
    "category": "nt",
    "difficulty": 2,
    "question": "Quem era o profeta idoso e justo no templo de Jerusalém que tomou o menino Jesus nos braços e bendisse a Deus dizendo: 'Agora despedes em paz o teu servo'?",
    "options": [
      "Zacarias",
      "Nicodemos",
      "Simeão",
      "Gamaliel"
    ],
    "correct": 2,
    "scriptureRef": "Lucas 2:25-32",
    "hint": "O Espírito Santo lhe havia revelado que não morreria antes de ver o Cristo do Senhor.",
    "explanation": "Simeão esperava a consolação de Israel e profetizou a Maria sobre o ministério de seu Filho."
  },
  {
    "id": "nt_003",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual profetisa viúva de 84 anos, da tribo de Aser, não se afastava do templo servindo a Deus com jejuns e orações e deu graças ao ver o menino Jesus?",
    "options": [
      "Elisabete",
      "Ana",
      "Marta",
      "Salomé"
    ],
    "correct": 1,
    "scriptureRef": "Lucas 2:36-38",
    "hint": "Filha de Fanuel, da tribo de Aser.",
    "explanation": "A profetisa Ana reconheceu imediatamente a redenção de Jerusalém no infante Salvador."
  },
  {
    "id": "nt_004",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual dos evangelistas abre seu registro apresentando a genealogia de Jesus Cristo a partir de Abraão, dividida em três grupos de catorze gerações?",
    "options": [
      "Marcos",
      "Lucas",
      "João",
      "Mateus"
    ],
    "correct": 3,
    "scriptureRef": "Mateus 1:1-17",
    "hint": "Ele era um cobrador de impostos (publicano) chamado Levi antes de seguir Jesus.",
    "explanation": "Mateus estruturou a árvore genealógica de Cristo com foco real messiânico para o público judeu."
  },
  {
    "id": "nt_005",
    "category": "nt",
    "difficulty": 3,
    "question": "Em qual cidade Jesus foi rejeitado por Seus próprios conterrâneos na sinagoga após ler o pergaminho do profeta Isaías?",
    "options": [
      "Betânia",
      "Cafarnaum",
      "Nazaré",
      "Jericó"
    ],
    "correct": 2,
    "scriptureRef": "Lucas 4:16-30",
    "hint": "Eles tentaram empurrá-Lo do cume de um monte para precipitá-Lo no abismo.",
    "explanation": "Jesus declarou: 'Nenhum profeta é bem aceito na sua pátria' e passou ileso pelo meio da turba furiosa em Nazaré."
  },
  {
    "id": "nt_006",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual era o nome do poço onde Jesus Se sentou fatigado da viagem e conversou com a mulher samaritana sobre a 'água viva'?",
    "options": [
      "O poço de Berseba",
      "O tanque de Betesda",
      "O poço de Jacó",
      "O tanque de Siloé"
    ],
    "correct": 2,
    "scriptureRef": "João 4:5-14",
    "hint": "Ficava na cidade samaritana de Sicar, perto da herdade que Jacó dera a seu filho José.",
    "explanation": "Jesus revelou à mulher samaritana Sua identidade messiânica e a fonte de água que jorra para a vida eterna."
  },
  {
    "id": "nt_007",
    "category": "nt",
    "difficulty": 3,
    "question": "Quantos pórticos possuía o tanque de Betesda em Jerusalém, onde os enfermos aguardavam o movimento das águas?",
    "options": [
      "Sete pórticos",
      "Doze pórticos",
      "Três pórticos",
      "Cinco pórticos"
    ],
    "correct": 3,
    "scriptureRef": "João 5:2",
    "hint": "Escavações arqueológicas perto da Porta das Ovelhas confirmaram exatamente esta estrutura de cinco alpendres.",
    "explanation": "Em Betesda, Jesus curou no sábado um homem que jazia enfermo havia 38 anos."
  },
  {
    "id": "nt_008",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era o nome do sogro de Caifás, que fora sumo sacerdote deposto pelos romanos e perante quem Jesus foi levado primeiro para interrogatório na noite de Sua prisão?",
    "options": [
      "Nicodemos",
      "Alexandre",
      "Gamaliel",
      "Anás"
    ],
    "correct": 3,
    "scriptureRef": "João 18:13",
    "hint": "Embora Caifás fosse o sumo sacerdote oficial daquele ano, este homem ainda retinha grande autoridade sacerdotal de fato.",
    "explanation": "Anás presidiu o primeiro interrogatório noturno e enviou Jesus amarrado ao seu genro Caifás."
  },
  {
    "id": "nt_009",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era o nome hebraico do pavimento de pedras onde ficava a cadeira de julgamento de Pôncio Pilatos?",
    "options": [
      "Gábata",
      "Betânia",
      "Gólgota",
      "Betfagé"
    ],
    "correct": 0,
    "scriptureRef": "João 19:13",
    "hint": "Pilatos sentou-se no tribunal num lugar chamado Litóstrotos, e em hebraico por este nome.",
    "explanation": "João 19:13 especifica: 'e sentou-se no tribunal, no lugar chamado Pavimento, e em hebraico Gábata'."
  },
  {
    "id": "nt_010",
    "category": "nt",
    "difficulty": 3,
    "question": "Quem era o discípulo de Jesus que pertencia ao grupo político dos 'zelotes' (nacionalistas radicais contra Roma)?",
    "options": [
      "Judas, filho de Tiago",
      "Tiago, filho de Alfeu",
      "Simão, o Zelote",
      "Simão, chamado Pedro"
    ],
    "correct": 2,
    "scriptureRef": "Lucas 6:15; Mateus 10:4",
    "hint": "Seu apelido indicava seu zelo fervoroso pelas tradições patrióticas de Israel.",
    "explanation": "Cristo uniu em Seu apostolado tanto Mateus (cobrador de impostos para Roma) quanto Simão o Zelote (militante anti-Roma)."
  },
  {
    "id": "nt_011",
    "category": "nt",
    "difficulty": 1,
    "question": "Na Parábola do Filho Pródigo, o que o jovem desejava comer para saciar a fome enquanto cuidava de porcos numa terra distante?",
    "options": [
      "As alfarrobas que eram dadas aos porcos de que ele cuidava",
      "Espigas deixadas pelos ceifeiros",
      "Pedaços de pão da mesa do patrão",
      "Figos secos guardados para o inverno"
    ],
    "correct": 0,
    "scriptureRef": "Lucas 15:16",
    "hint": "E ninguém lhe dava nada, até que ele 'caiu em si' e decidiu voltar à casa de seu pai.",
    "explanation": "As alfarrobas ilustram a mais abjeta humilhação espiritual e física do filho arrependido antes de seu retorno."
  },
  {
    "id": "nt_012",
    "category": "nt",
    "difficulty": 1,
    "question": "Qual amigo íntimo de Jesus havia falecido há quatro dias e já cheirava mal quando Cristo o chamou para fora da sepultura em Betânia?",
    "options": [
      "Jairo",
      "Lázaro de Betânia",
      "Bartimeu",
      "Simão"
    ],
    "correct": 1,
    "scriptureRef": "João 11:39-44",
    "hint": "Irmão de Marta e Maria, que choravam copiosamente.",
    "explanation": "Jesus ordenou: 'Lázaro, vem para fora!', operando uma das mais poderosas manifestações de Seu domínio sobre a morte."
  },
  {
    "id": "nt_013",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual dos dez leprosos curados por Jesus no caminho voltou glorificando a Deus e lançando-se aos pés do Mestre em gratidão?",
    "options": [
      "Um samaritano",
      "Um fariseu da Galileia",
      "Um centurião romano",
      "Um pescador de Betsaida"
    ],
    "correct": 0,
    "scriptureRef": "Lucas 17:15-18",
    "hint": "Jesus perguntou: 'Não foram dez os limpos? E onde estão os nove? Não houve quem voltasse para dar glória a Deus senão este estrangeiro?'.",
    "explanation": "Apenas o samaritano, desprezado pelos judeus, demonstrou genuína gratidão e foi salvo por sua fé."
  },
  {
    "id": "nt_014",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual era o nome do cego que clamou por Jesus à beira do caminho de Jericó, segundo Marcos 10:46–52?",
    "options": [
      "Zaqueu",
      "Bartimeu",
      "Nicodemos",
      "Malco"
    ],
    "correct": 1,
    "scriptureRef": "Marcos 10:46-52",
    "hint": "Ele jogou fora sua capa, levantou-se e foi até Jesus.",
    "explanation": "Bartimeu recobrou imediatamente a visão e seguiu a Jesus pelo caminho glorificando a Deus."
  },
  {
    "id": "nt_015",
    "category": "nt",
    "difficulty": 3,
    "question": "Onde Jesus realizou o milagre de expulsar uma legião de demônios de um homem para uma manada de cerca de dois mil porcos que se precipitaram no mar?",
    "options": [
      "Na região de Samaria",
      "Na região dos gerasenos",
      "Na região de Cesareia de Filipe",
      "Na região de Caná da Galileia"
    ],
    "correct": 1,
    "scriptureRef": "Marcos 5:1-13; Lucas 8:26-33",
    "hint": "Região a leste do Mar da Galileia no território de Decápolis.",
    "explanation": "Os demônios suplicaram para entrar nos porcos, e a manada se atirou pelo despenhadeiro no lago de Genesaré."
  },
  {
    "id": "nt_016",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual apóstolo encontrou uma moeda (estáter) na boca do primeiro peixe que pescou com anzol para pagar o tributo do templo por si e por Jesus?",
    "options": [
      "Pedro",
      "João",
      "André",
      "Mateus"
    ],
    "correct": 0,
    "scriptureRef": "Mateus 17:24-27",
    "hint": "Jesus instruiu: 'Vai ao mar, lança o anzol, tira o primeiro peixe que subir...' para não escandalizar os cobradores.",
    "explanation": "O milagre do estáter na boca do peixe ilustra a soberania de Cristo sobre a criação e Seu respeito pelas leis civis."
  },
  {
    "id": "nt_017",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era a quantidade de cestos de pedaços que sobraram após a multiplicação de sete pães e alguns peixinhos para os quatro mil homens?",
    "options": [
      "Doze cestos de pedaços",
      "Cinco cestos de pedaços",
      "Sete cestos de pedaços",
      "Três cestos de pedaços"
    ],
    "correct": 2,
    "scriptureRef": "Mateus 15:37; Marcos 8:8",
    "hint": "Na primeira alimentação (5.000) sobraram 12 cestos pequenos (kophinoi); nesta segunda sobram sete cestas maiores.",
    "explanation": "A distinção entre as duas alimentações é enfatizada pelo próprio Jesus em Mateus 16:9-10."
  },
  {
    "id": "nt_018",
    "category": "nt",
    "difficulty": 3,
    "question": "Na Parábola do Bom Samaritano, quais foram os dois líderes religiosos judeus que viram o homem ferido à beira da estrada e passaram de largo pelo outro lado?",
    "options": [
      "Dois fariseus",
      "Um saduceu e um escriba",
      "Dois rabinos de Jerusalém",
      "Um sacerdote e um levita"
    ],
    "correct": 3,
    "scriptureRef": "Lucas 10:30-32",
    "hint": "Eles desciam pelo caminho íngreme de Jerusalém para Jericó.",
    "explanation": "O sacerdote e o levita negligenciaram o dever sagrado de socorro ao próximo, enquanto o samaritano prestou cura e amparo."
  },
  {
    "id": "nt_019",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era o valor monetário do nardo puro preciosíssimo contido no vaso de alabastro derramado sobre os pés de Jesus por Maria em Betânia?",
    "options": [
      "Pouco menos de cinquenta denários",
      "Cerca de quinhentos denários",
      "Mais de trezentos denários",
      "Aproximadamente cem denários"
    ],
    "correct": 2,
    "scriptureRef": "Marcos 14:5; João 12:5",
    "hint": "Judas Iscariotes criticou o ato dizendo que o perfume poderia ter sido vendido para dar aos pobres.",
    "explanation": "Jesus defendeu Maria declarando que ela havia ungido antecipadamente Seu corpo para a sepultura."
  },
  {
    "id": "nt_020",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era o nome do servo do sumo sacerdote cuja orelha direita foi decepada pela espada de Pedro no Getsêmani e curada instantaneamente por Jesus?",
    "options": [
      "Sóstene",
      "Malco",
      "Teófilo",
      "Barrabás"
    ],
    "correct": 1,
    "scriptureRef": "João 18:10; Lucas 22:50-51",
    "hint": "O evangelista médico Lucas é o único que relata o toque de cura de Jesus restaurando a orelha.",
    "explanation": "Jesus repreendeu Pedro dizendo: 'Mete a tua espada na bainha; não beberei eu o cálice que o Pai me deu?' e curou Malco."
  },
  {
    "id": "nt_021",
    "category": "nt",
    "difficulty": 1,
    "question": "Quem era o homem de Cirene forçado pelos soldados romanos a carregar a cruz de Jesus a caminho do Gólgota?",
    "options": [
      "José de Arimateia",
      "Nicodemos",
      "Barnabé",
      "Simão Cireneu"
    ],
    "correct": 3,
    "scriptureRef": "Mateus 27:32; Marcos 15:21",
    "hint": "Pai de Alexandre e de Rufo, vindo do campo.",
    "explanation": "Simão de Cirene foi constrangido pelos guardas romanos a prestar esse serviço histórico ao Salvador."
  },
  {
    "id": "nt_022",
    "category": "nt",
    "difficulty": 1,
    "question": "Qual membro nobre do Sinédrio, discípulo secreto de Jesus por medo dos judeus, pediu o corpo do Senhor a Pilatos e o colocou em seu próprio sepulcro novo?",
    "options": [
      "Nicodemos",
      "Gamaliel",
      "Teófilo",
      "José de Arimateia"
    ],
    "correct": 3,
    "scriptureRef": "Mateus 27:57-60; João 19:38",
    "hint": "Ele era um homem rico e virtuoso que não havia consentido na condenação de Cristo.",
    "explanation": "José de Arimateia comprou linho fino e sepultou o corpo de Jesus numa tumba esculpida na rocha."
  },
  {
    "id": "nt_023",
    "category": "nt",
    "difficulty": 2,
    "question": "O que Nicodemos trouxe consigo para embalsamar o corpo de Jesus juntamente com José de Arimateia?",
    "options": [
      "Uma mistura de azeite e incenso",
      "Uma mistura de nardo e especiarias",
      "Uma mistura de bálsamo e canela",
      "Uma mistura de mirra e aloés, levada em grande quantidade"
    ],
    "correct": 3,
    "scriptureRef": "João 19:39",
    "hint": "Uma quantidade real e faustosa, digna do sepultamento de um grande monarca.",
    "explanation": "Nicodemos, que fora a Jesus de noite, demonstrou publicamente sua lealdade trazendo cem libras de preciosas especiarias."
  },
  {
    "id": "nt_024",
    "category": "nt",
    "difficulty": 2,
    "question": "A quem Jesus ressuscitado apareceu em primeiro lugar na manhã do domingo da Ressurreição junto ao túmulo no jardim?",
    "options": [
      "A Pedro e João",
      "A Sua mãe Maria",
      "Aos dois discípulos no caminho de Emaús",
      "A Maria Madalena"
    ],
    "correct": 3,
    "scriptureRef": "João 20:11-18; Marcos 16:9",
    "hint": "Ela inicialmente pensou que Ele fosse o hortelão, até que Ele a chamou pelo nome: 'Maria!'.",
    "explanation": "Maria Madalena teve a glória sublime de ser a primeira testemunha ocular do Redentor ressuscitado dentre os mortos."
  },
  {
    "id": "nt_025",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual dos dois discípulos caminhando para a aldeia de Emaús no dia da Ressurreição teve seu nome registrado no Evangelho de Lucas?",
    "options": [
      "Nicodemos",
      "Bartolomeu",
      "Tadeu",
      "Cléopas"
    ],
    "correct": 3,
    "scriptureRef": "Lucas 24:18",
    "hint": "Eles disseram: 'Porventura não ardia em nós o nosso coração quando, pelo caminho, nos falava...?'.",
    "explanation": "Cléopas e seu companheiro reconheceram o Senhor ressuscitado no partir do pão na estalagem."
  },
  {
    "id": "nt_026",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual apóstolo duvidou da Ressurreição dizendo que não creria a menos que visse o sinal dos cravos e pusesse a mão no Seu lado ferido?",
    "options": [
      "Tomé, chamado Dídimo",
      "Natanael, natural de Caná",
      "Filipe, natural de Betsaida",
      "Judas, chamado Tadeu"
    ],
    "correct": 0,
    "scriptureRef": "João 20:24-29",
    "hint": "Oito dias depois, Jesus apareceu e disse: 'Põe aqui o teu dedo... não sejas incrédulo, mas crente'.",
    "explanation": "Tomé exclamou: 'Senhor meu, e Deus meu!', recebendo a repreensão: 'Bem-aventurados os que não viram e creram'."
  },
  {
    "id": "nt_027",
    "category": "nt",
    "difficulty": 3,
    "question": "Quantas vezes Jesus perguntou a Pedro nas praias de Tiberíades: 'Simão, filho de Jonas, amas-me mais do que estes?', confiando-lhe a ordem de apascentar Suas ovelhas?",
    "options": [
      "Três vezes",
      "Sete vezes",
      "Duas vezes",
      "Quarenta vezes"
    ],
    "correct": 0,
    "scriptureRef": "João 21:15-17",
    "hint": "O mesmo número de vezes que Pedro havia negado o Mestre na noite da condenação.",
    "explanation": "Essa tripla declaração de amor restaurou Pedro plenamente à sua sublime missão de liderança da Igreja."
  },
  {
    "id": "nt_028",
    "category": "nt",
    "difficulty": 4,
    "question": "Em João 21, qual foi o número exato de peixes grandes que os apóstolos puxaram na rede sem que ela se rompesse por ordem do Senhor ressuscitado?",
    "options": [
      "173 peixes grandes",
      "144 peixes grandes",
      "153 peixes grandes",
      "150 peixes grandes"
    ],
    "correct": 2,
    "scriptureRef": "João 21:11",
    "hint": "O número 153 tem sido objeto de reflexões teológicas sobre a plenitude de todas as nações da Terra.",
    "explanation": "Simão Pedro subiu e puxou para terra a rede cheia de 153 grandes peixes intactos."
  },
  {
    "id": "nt_029",
    "category": "nt",
    "difficulty": 1,
    "question": "Quem foi o discípulo escolhido por sorteio pelos apóstolos para ocupar o lugar de Judas Iscariotes no Quórum dos Doze?",
    "options": [
      "José Barsabás (Justo)",
      "Barnabé",
      "Matias",
      "Estêvão"
    ],
    "correct": 2,
    "scriptureRef": "Atos 1:23-26",
    "hint": "Eles oraram: 'Tu, Senhor, conhecedor dos corações de todos, mostra qual destes dois tens escolhido'.",
    "explanation": "A sorte caiu sobre Matias, que foi contado com os onze apóstolos como testemunha da Ressurreição."
  },
  {
    "id": "nt_030",
    "category": "nt",
    "difficulty": 1,
    "question": "O que desceu sobre os apóstolos e discípulos reunidos no cenáculo no dia de Pentecostes, capacitando-os a pregar em línguas de todas as nações?",
    "options": [
      "Uma nuvem luminosa e uma voz vinda do templo",
      "Uma luz sobre o altar e a abertura das portas do templo",
      "Óleo sobre suas cabeças e a aparição de um mensageiro",
      "Línguas como de fogo e o Espírito Santo"
    ],
    "correct": 3,
    "scriptureRef": "Atos 2:1-4",
    "hint": "Veio do céu um som como de um vento veemente e impetuoso que encheu toda a casa.",
    "explanation": "No Pentecostes, o poder do Espírito Santo inaugurou a expansão apostólica internacional do Evangelho."
  },
  {
    "id": "nt_031",
    "category": "nt",
    "difficulty": 2,
    "question": "O que Pedro disse ao homem coxo de nascença que pedia esmolas junto à porta Formosa do templo em Atos 3?",
    "options": [
      "Vai lavar-te no tanque e apresenta-te ao sacerdote",
      "Estende a mão e recebe a oferta trazida pelos irmãos",
      "Em nome de Jesus Cristo, levanta-te e anda",
      "Levanta-te e toma o teu leito antes de entrar no templo"
    ],
    "correct": 2,
    "scriptureRef": "Atos 3:6",
    "hint": "Tomando-o pela mão direita, levantou-o, e imediatamente seus pés e artelhos se firmaram.",
    "explanation": "O homem curado entrou no templo com Pedro e João, andando, saltando e louvando a Deus."
  },
  {
    "id": "nt_032",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual casal de cristãos morreu subitamente diante do Apóstolo Pedro por mentir ao Espírito Santo sobre o valor real do campo que haviam vendido?",
    "options": [
      "Áquila e Priscila",
      "Ananias e Safira",
      "Filemom e Áfia",
      "Zacarias e Isabel"
    ],
    "correct": 1,
    "scriptureRef": "Atos 5:1-11",
    "hint": "Pedro lhes disse: 'Não mentistes aos homens, mas a Deus'.",
    "explanation": "O severo julgamento divino sobre a hipocrisia de Ananias e Safira causou grande temor em toda a Igreja nascente."
  },
  {
    "id": "nt_033",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual célebre doutor da lei e fariseu aconselhou o Sinédrio a não matar os apóstolos, dizendo: 'Se este conselho ou esta obra é de homens, se desfará; mas se é de Deus, não podereis derrotá-la'?",
    "options": [
      "Nicodemos",
      "Caifás",
      "Tertulo",
      "Gamaliel"
    ],
    "correct": 3,
    "scriptureRef": "Atos 5:34-39",
    "hint": "Ele era mestre em cuja escola o jovem Paulo (Saulo de Tarso) fora instruído com rigor.",
    "explanation": "A prudência de Gamaliel poupou os apóstolos da pena de morte naquele momento crítico."
  },
  {
    "id": "nt_034",
    "category": "nt",
    "difficulty": 2,
    "question": "Quem era o evangelista guiado pelo Espírito ao deserto de Gaza para explicar a profecia de Isaías 53 a um eunuco etíope, oficial da rainha Candace?",
    "options": [
      "Estêvão",
      "Filipe",
      "Apolo",
      "Barnabé"
    ],
    "correct": 1,
    "scriptureRef": "Atos 8:26-39",
    "hint": "O etíope perguntou: 'Eis aqui água; que impede que eu seja batizado?' e Filipe o batizou.",
    "explanation": "Após o batismo, o Espírito do Senhor arrebatou Filipe, e o eunuco seguiu o seu caminho jubiloso."
  },
  {
    "id": "nt_035",
    "category": "nt",
    "difficulty": 3,
    "question": "Em qual cidade Pedro teve a visão celestial de um lençol descendo do céu com animais quadrúpedes e répteis, aprendendo que não devia chamar imundo ao que Deus purificou?",
    "options": [
      "Em Cesareia",
      "Em Damasco",
      "Em Antioquia",
      "Em Jope"
    ],
    "correct": 3,
    "scriptureRef": "Atos 10:9-16",
    "hint": "Ele estava orando no terraço perto da hora sexta quando teve o êxtase.",
    "explanation": "Essa revelação divina preparou Pedro para batizar o centurião romano Cornélio, abrindo a Igreja aos gentios."
  },
  {
    "id": "nt_036",
    "category": "nt",
    "difficulty": 2,
    "question": "Em qual cidade os discípulos de Jesus foram pela primeira vez chamados historicamente pelo nome de 'cristãos'?",
    "options": [
      "Jerusalém",
      "Éfeso",
      "Roma",
      "Antioquia"
    ],
    "correct": 3,
    "scriptureRef": "Atos 11:26",
    "hint": "Barnabé e Saulo trabalharam juntos nesta metrópole durante um ano inteiro ensinando grande multidão.",
    "explanation": "Antioquia da Síria foi o grande centro missionário que enviou Paulo e Barnabé ao mundo gentílico."
  },
  {
    "id": "nt_037",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual rei mandou matar à espada Tiago, irmão de João, e prendeu Pedro durante a festa dos pães ázimos?",
    "options": [
      "Herodes Agripa I",
      "Herodes Antipas",
      "Herodes Arquelau",
      "Herodes o Grande"
    ],
    "correct": 0,
    "scriptureRef": "Atos 12:1-3",
    "hint": "Mais tarde, esse mesmo rei foi ferido por um anjo e comido de vermes após ser aclamado como deus em Cesareia.",
    "explanation": "Tiago Maior foi o primeiro dos Doze Apóstolos originais a selar seu testemunho com o martírio."
  },
  {
    "id": "nt_038",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual jovem serva foi à porta quando Pedro bateu após ser libertado por um anjo da prisão, mas de tanta alegria não abriu a porta e correu para avisar os irmãos?",
    "options": [
      "Priscila",
      "Lídia",
      "Rode",
      "Febe"
    ],
    "correct": 2,
    "scriptureRef": "Atos 12:13-15",
    "hint": "Os discípulos que oravam em casa de Maria, mãe de Marcos, disseram-lhe: 'Estás louca; é o seu anjo'.",
    "explanation": "Rode insistia alegremente que Pedro estava em pé à porta, até que eles abriram e ficaram atônitos."
  },
  {
    "id": "nt_039",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual profeta cristão em Antioquia profetizou uma grande fome mundial ocorrida nos dias do imperador Cláudio e mais tarde atou a cinta de Paulo profetizando sua prisão em Jerusalém?",
    "options": [
      "Silas",
      "Ágabo",
      "Judas Barsabás",
      "Mnason"
    ],
    "correct": 1,
    "scriptureRef": "Atos 11:28; 21:10-11",
    "hint": "Ele pegou a cinta de Paulo e atou seus próprios pés e mãos como sinal profético.",
    "explanation": "Ágabo foi um fiel profeta da Igreja primitiva cujas predições se cumpriram com precisão histórica."
  },
  {
    "id": "nt_040",
    "category": "nt",
    "difficulty": 3,
    "question": "Quem apresentou a proposta sobre os gentios depois dos discursos de Pedro, Barnabé e Paulo em Atos 15:13–21?",
    "options": [
      "Tiago, irmão do Senhor",
      "Pedro, irmão de André",
      "João, filho de Zebedeu",
      "Paulo, natural de Tarso"
    ],
    "correct": 0,
    "scriptureRef": "Atos 15:13-21",
    "hint": "Ele concluiu: 'Por isso julgo que não se deve perturbar aqueles, dentre os gentios, que se convertem a Deus'.",
    "explanation": "Tiago liderava a congregação de Jerusalém e redigiu a carta pastoral enviada às congregações gentílicas."
  },
  {
    "id": "nt_041",
    "category": "nt",
    "difficulty": 3,
    "question": "O que Paulo e Silas estavam fazendo à meia-noite na prisão escura de Filipos, com os pés no cepo, antes do grande terremoto abrir as celas?",
    "options": [
      "Planejavam sua defesa com os outros prisioneiros",
      "Oravam e cantavam hinos, enquanto os outros prisioneiros os escutavam",
      "Pediam aos magistrados uma audiência pública",
      "Explicavam a lei romana ao carcereiro"
    ],
    "correct": 1,
    "scriptureRef": "Atos 16:25",
    "hint": "Seus louvores na adversidade converteram o carcereiro e toda a sua família naquela mesma noite.",
    "explanation": "O terremoto abalou os alicerces, as correntes caíram e o carcereiro perguntou: 'Que é necessário que eu faça para me salvar?'."
  },
  {
    "id": "nt_042",
    "category": "nt",
    "difficulty": 3,
    "question": "Onde Paulo fez seu célebre discurso filosófico aos sábios estóicos e epicureus sobre o altar 'Ao Deus Desconhecido'?",
    "options": [
      "No Coliseu em Roma",
      "No pretório de Cesareia",
      "No templo de Diana em Éfeso",
      "No Areópago em Atenas"
    ],
    "correct": 3,
    "scriptureRef": "Atos 17:19-34",
    "hint": "Na célebre colina de Marte, no coração cultural e acadêmico da Grécia.",
    "explanation": "Paulo declarou: 'Pois nEle vivemos, e nos movemos, e existimos... sendo nós geração de Deus, não devemos cuidar que a divindade seja semelhante a ouro ou prata'."
  },
  {
    "id": "nt_043",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual jovem caiu do terceiro andar adormecido durante um longo sermão de Paulo que se estendeu até a meia-noite em Trôade, sendo ressuscitado pelo apóstolo?",
    "options": [
      "Tíquico",
      "Êutico",
      "Erasto",
      "Trófimo"
    ],
    "correct": 1,
    "scriptureRef": "Atos 20:9-12",
    "hint": "Ele adormeceu na janela e foi levantado morto, mas Paulo o abraçou e disse: 'Não vos perturbeis, que a sua alma nele está'.",
    "explanation": "Paulo operou o milagre de restauração de Êutico e todos foram grandemente consolados."
  },
  {
    "id": "nt_044",
    "category": "nt",
    "difficulty": 4,
    "question": "Em qual ilha Paulo sofreu um naufrágio durante sua viagem marítima para Roma e foi picado por uma víbora venenosa sem sofrer nenhum mal?",
    "options": [
      "Na ilha de Patmos",
      "Na ilha de Malta",
      "Na ilha de Creta",
      "Na ilha de Chipre"
    ],
    "correct": 1,
    "scriptureRef": "Atos 28:1-6",
    "hint": "Os nativos da ilha pensaram que ele fosse um assassino, mas ao verem que não inchou nem caiu morto, disseram que era um deus.",
    "explanation": "O milagre em Malta cumpriu a promessa do Salvador de que pisariam em serpentes e não lhes causaria dano."
  },
  {
    "id": "nt_045",
    "category": "nt",
    "difficulty": 1,
    "question": "Em 1 Coríntios 13:13, quais são as três grandes virtudes cristãs que permanecem para sempre, sendo a caridade a maior delas?",
    "options": [
      "A mansidão, a diligência e a perseverança",
      "A fé, a esperança e o amor, também chamado caridade",
      "A sabedoria, a justiça e a prudência",
      "A paciência, a coragem e a temperança"
    ],
    "correct": 1,
    "scriptureRef": "1 Coríntios 13:13",
    "hint": "'Agora, pois, permanecem a fé, a esperança e o amor, estes três; mas o maior destes é o amor.'",
    "explanation": "O apóstolo Paulo conclui seu sublime hino ao amor coroando a caridade como o dom supremo."
  },
  {
    "id": "nt_046",
    "category": "nt",
    "difficulty": 2,
    "question": "Em 1 Coríntios 15:40-42, a que Paulo compara a glória dos diferentes corpos na Ressurreição?",
    "options": [
      "À glória do Sol, à glória da Lua e à glória das estrelas",
      "Ao fogo, à água e ao vento",
      "Ao ouro, à prata e às pedras preciosas",
      "Ao céu, à terra e às profundezas do mar"
    ],
    "correct": 0,
    "scriptureRef": "1 Coríntios 15:40-42",
    "hint": "Passagem fundamental que fundamenta a doutrina da Restauração dos três graus de glória em D&C 76.",
    "explanation": "Assim como uma estrela difere de outra em resplendor, assim também será a ressurreição dos mortos em diferentes esferas de glória."
  },
  {
    "id": "nt_047",
    "category": "nt",
    "difficulty": 2,
    "question": "Em Gálatas 5:22-23, qual é a lista que Paulo apresenta em oposição às obras da carne?",
    "options": [
      "As obras previstas na lei de Moisés",
      "Os dons de administração da Igreja",
      "Os deveres dos ministros do evangelho",
      "O fruto produzido pelo Espírito"
    ],
    "correct": 3,
    "scriptureRef": "Gálatas 5:22-23",
    "hint": "'Mas o fruto do Espírito é: amor, gozo, paz... contra estas coisas não há lei.'",
    "explanation": "O fruto do Espírito é a evidência real da presença transformadora de Deus na vida do discípulo."
  },
  {
    "id": "nt_048",
    "category": "nt",
    "difficulty": 2,
    "question": "Em Efésios 6:11-17, qual é a metáfora militar que Paulo usa para descrever a proteção espiritual do cristão contra as ciladas do diabo?",
    "options": [
      "A fortaleza edificada sobre a rocha",
      "A armadura de Deus, com escudo da fé e espada do Espírito",
      "O exército que marcha para a batalha",
      "A torre erguida para vigiar a vinha"
    ],
    "correct": 1,
    "scriptureRef": "Efésios 6:11-17",
    "hint": "Para que possais estar firmes contra as astutas ciladas do maligno.",
    "explanation": "A armadura espiritual representa as virtudes salvadoras que revestem o cristão contra os dardos inflamados do adversário."
  },
  {
    "id": "nt_049",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual epístola de Paulo foi escrita especificamente para pedir o perdão e acolhimento como irmão do escravo fugitivo Onésimo?",
    "options": [
      "Tito",
      "Filemom",
      "Gálatas",
      "Colossenses"
    ],
    "correct": 1,
    "scriptureRef": "Filemom 1:10-16",
    "hint": "Paulo pede ao proprietário: 'Recebe-o não já como servo, mas mais do que servo, como irmão amado'.",
    "explanation": "A carta a Filemom é uma comovente lição prática sobre como o Evangelho transforma escravos e senhores em irmãos espirituais."
  },
  {
    "id": "nt_050",
    "category": "nt",
    "difficulty": 3,
    "question": "Em Hebreus 5 e 7, a qual antiga e misteriosa ordem sacerdotal Jesus Cristo é comparado como Sumo Sacerdote Eterno, superior ao sacerdócio levítico?",
    "options": [
      "À ordem de Arão",
      "À ordem de Moisés",
      "À ordem de Melquisedeque",
      "À ordem de Elias"
    ],
    "correct": 2,
    "scriptureRef": "Hebreus 5:6-10; 7:1-17",
    "hint": "'Tu és sacerdote eternamente, segundo a ordem de Melquisedeque.'",
    "explanation": "O autor de Hebreus estabelece que o sacerdócio maior de Cristo antecede e suplanta a lei e ordenanças levíticas."
  },
  {
    "id": "nt_051",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual apóstolo escreveu em sua epístola a célebre frase: 'Assim também a fé, se não tiver as obras, é morta em si mesma'?",
    "options": [
      "Paulo",
      "Tiago",
      "Pedro",
      "João"
    ],
    "correct": 1,
    "scriptureRef": "Tiago 2:17",
    "hint": "Ele desafiou: 'Mostra-me a tua fé sem as tuas obras, e eu te mostrarei a minha fé pelas minhas obras'.",
    "explanation": "Tiago enfatiza a harmonia inseparável entre a crença viva no coração e as ações práticas de discipulado."
  },
  {
    "id": "nt_052",
    "category": "nt",
    "difficulty": 3,
    "question": "Em 1 Pedro 3:18-20 e 4:6, que doutrina consoladora sobre os mortos é explicada pelo apóstolo Pedro?",
    "options": [
      "Somente os vivos podem ouvir o evangelho de Cristo",
      "Os mortos precisam voltar à vida antes de ouvir a palavra",
      "A pregação aos mortos aguarda o julgamento final",
      "O evangelho foi pregado aos mortos, para que vivessem segundo Deus em espírito"
    ],
    "correct": 3,
    "scriptureRef": "1 Pedro 3:19; 4:6",
    "hint": "Esta passagem bíblica foi a chave inspiradora para a grande visão da redenção dos mortos de Joseph F. Smith em D&C 138.",
    "explanation": "Pedro testifica que o ministério salvador do Senhor alcançou os espíritos dos antepassados que faleceram sem conhecer o evangelho."
  },
  {
    "id": "nt_053",
    "category": "nt",
    "difficulty": 4,
    "question": "Na Epístola de Judas, versículo 9, qual arcanjo contendeu com o diabo pelo corpo do profeta Moisés sem proferir juízo infamatório, dizendo apenas: 'O Senhor te repreenda'?",
    "options": [
      "Miguel",
      "Gabriel",
      "Rafael",
      "Uriel"
    ],
    "correct": 0,
    "scriptureRef": "Judas 1:9",
    "hint": "O grande capitão das hostes celestes, identificado na Restauração como o patriarca Adão.",
    "explanation": "Judas cita este texto sobre o arcanjo Miguel como modelo de sobriedade e reverência divina diante do mal."
  },
  {
    "id": "nt_054",
    "category": "nt",
    "difficulty": 4,
    "question": "Quantas eram as igrejas da Ásia Menor às quais o apóstolo João enviou mensagens e advertências proféticas específicas nos capítulos 2 e 3 de Apocalipse?",
    "options": [
      "Doze igrejas",
      "Três igrejas",
      "Sete igrejas",
      "Dez igrejas"
    ],
    "correct": 2,
    "scriptureRef": "Apocalipse 1:11; 2-3",
    "hint": "O número bíblico de completude e perfeição espiritual.",
    "explanation": "As cartas às sete congregações contêm repreensões, elogios e grandiosas promessas para os que vencerem o mundo."
  },
  {
    "id": "nt_055",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual é a cidade celestial descrita no final de Apocalipse com doze portas de pérolas, muros de jaspe e rua de ouro puro transparente como vidro?",
    "options": [
      "A cidade da Nova Jerusalém",
      "A Jerusalém dos dias de Davi",
      "A cidade de Babilônia",
      "A cidade de Antioquia"
    ],
    "correct": 0,
    "scriptureRef": "Apocalipse 21:10-21",
    "hint": "A cidade quadrangular onde não há necessidade de sol nem de lua, pois a glória de Deus e do Cordeiro é a sua lâmpada.",
    "explanation": "A Nova Jerusalém celestial representa a eterna habitação dos santos exaltados na presença do Cordeiro."
  },
  {
    "id": "nt_056",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual apóstolo era irmão de Pedro e foi o primeiro a dizer-lhe: 'Achamos o Messias'?",
    "options": [
      "André",
      "Tiago",
      "Filipe",
      "João"
    ],
    "correct": 0,
    "scriptureRef": "João 1:40-42",
    "hint": "Ele era anteriormente discípulo de João Batista e conduziu seu irmão Pedro a Jesus.",
    "explanation": "André foi um dos primeiros seguidores de Cristo e imediatamente compartilhou a boa nova com Pedro."
  },
  {
    "id": "nt_057",
    "category": "nt",
    "difficulty": 2,
    "question": "O que Natanael disse com preconceito regional quando Filipe lhe anunciou que haviam encontrado o Messias em Jesus de Nazaré?",
    "options": [
      "'Pode vir alguma coisa boa de Nazaré?'",
      "'Nenhum profeta surge de Samaria'",
      "'Onde estão as suas tropas?'",
      "'Ele conhece os sacerdotes?'"
    ],
    "correct": 0,
    "scriptureRef": "João 1:46",
    "hint": "Filipe respondeu-lhe simplesmente com o convite: 'Vem e vê'.",
    "explanation": "Ao ver Natanael se aproximar, Jesus declarou: 'Eis aqui um verdadeiro israelita, em quem não há dolo'."
  },
  {
    "id": "nt_058",
    "category": "nt",
    "difficulty": 3,
    "question": "Onde Jesus estava e o que Ele disse ter visto Natanael fazendo antes que Filipe o chamasse?",
    "options": [
      "Debaixo da figueira",
      "Orando no templo",
      "Pescando no mar",
      "Lendo os profetas na tenda"
    ],
    "correct": 0,
    "scriptureRef": "João 1:48",
    "hint": "Essa onisciência divina levou Natanael a exclamar imediatamente: 'Rabi, Tu és o Filho de Deus!'.",
    "explanation": "A visão de Cristo sobre Natanael sob a figueira converteu instantaneamente o seu coração."
  },
  {
    "id": "nt_059",
    "category": "nt",
    "difficulty": 3,
    "question": "Na interpretação ensinada pela Igreja restaurada para Mateus 16:17–19, o que representa a rocha sobre a qual Cristo edifica Sua Igreja?",
    "options": [
      "A tradição transmitida pelos mestres da lei",
      "A revelação que o Pai concede, testificando que Jesus é o Cristo",
      "A autoridade política dos descendentes de Davi",
      "O templo de Jerusalém e seus sacrifícios"
    ],
    "correct": 1,
    "scriptureRef": "Mateus 16:17-18; Ensinamentos dos Profetas",
    "hint": "'Pois não foi carne e sangue quem to revelou, mas meu Pai que está nos Céus.'",
    "explanation": "O princípio da revelação contínua de Deus é a rocha imutável sobre a qual o reino de Cristo é edificado."
  },
  {
    "id": "nt_060",
    "category": "nt",
    "difficulty": 3,
    "question": "Quais três apóstolos acompanharam Jesus no Monte da Transfiguração e também no Jardim do Getsêmani?",
    "options": [
      "Pedro, André e Tomé",
      "João, Mateus e Judas",
      "Filipe, Bartolomeu e Tiago",
      "Pedro, Tiago e João"
    ],
    "correct": 3,
    "scriptureRef": "Mateus 17:1; 26:37",
    "hint": "Eles formavam a presidência de liderança íntima mais próxima do Mestre.",
    "explanation": "Pedro, Tiago e João testemunharam a glória divina no monte e a extrema agonia expiatória no Getsêmani."
  },
  {
    "id": "nt_061",
    "category": "nt",
    "difficulty": 3,
    "question": "Quem apareceu glorificado ao lado de Jesus no Monte da Transfiguração para conferir chaves sagradas?",
    "options": [
      "Abraão e Davi",
      "Moisés e Elias",
      "Isaías e Jeremias",
      "Adão e Enoque"
    ],
    "correct": 1,
    "scriptureRef": "Mateus 17:3",
    "hint": "Os antigos detentores das chaves da lei e do selamento de Israel.",
    "explanation": "Moisés e Elias ministraram aos apóstolos conferindo autoridade espiritual indispensável."
  },
  {
    "id": "nt_062",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual foi a resposta de Jesus aos saduceus que tentaram confundi-Lo com a história da mulher que se casou com sete irmãos na Terra?",
    "options": [
      "O último casamento anula todos os casamentos anteriores",
      "A decisão caberá ao primeiro marido na ressurreição",
      "Eles erravam por não conhecerem as Escrituras nem compreenderem o poder de Deus",
      "A lei de Moisés impede que os sete irmãos ressuscitem"
    ],
    "correct": 2,
    "scriptureRef": "Mateus 22:29-30",
    "hint": "Os saduceus não acreditavam em ressurreição nem em anjos ou espíritos.",
    "explanation": "Cristo esclareceu que ordenanças mortais sem autoridade do sacerdócio não possuem validade na ressurreição."
  },
  {
    "id": "nt_063",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual é o primeiro e grande mandamento segundo a resposta de Jesus ao perito da lei em Mateus 22:37-38?",
    "options": [
      "Honrar pai e mãe para prolongar os dias sobre a terra",
      "Amar a Deus de todo o coração, alma e pensamento",
      "Guardar o sábado e santificá-lo em todas as gerações",
      "Amar o próximo como a si mesmo em todas as circunstâncias"
    ],
    "correct": 1,
    "scriptureRef": "Mateus 22:37-38",
    "hint": "E o segundo é semelhante a este: 'Amarás o teu próximo como a ti mesmo'.",
    "explanation": "Destes dois mandamentos de puro amor dependem toda a lei e os profetas."
  },
  {
    "id": "nt_064",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era a inscrição multilíngue (em hebraico, grego e latim) que Pilatos mandou pregar acima da cabeça de Jesus na cruz?",
    "options": [
      "Jesus da Galileia, o Profeta de Israel",
      "Jesus Nazareno, o Rei dos Judeus",
      "Jesus de Nazaré, o Filho de José",
      "Jesus Nazareno, o Mestre dos Judeus"
    ],
    "correct": 1,
    "scriptureRef": "João 19:19-22",
    "hint": "Os principais sacerdotes pediram: 'Não escrevas: Rei dos judeus; mas que ele disse...', e Pilatos replicou: 'O que escrevi, escrevi'.",
    "explanation": "A inscrição proclamava nos três idiomas principais do império a realeza sagrada de Jesus Cristo."
  },
  {
    "id": "nt_065",
    "category": "nt",
    "difficulty": 4,
    "question": "O que aconteceu com o grande e pesado véu do Templo de Jerusalém no exato instante em que Jesus expirou na cruz?",
    "options": [
      "O véu se rasgou em duas partes, começando no alto e indo até embaixo",
      "Caiu inteiro diante da entrada do santuário",
      "Foi retirado pelos sacerdotes durante o terremoto",
      "Rasgou-se em dois, de baixo para cima"
    ],
    "correct": 0,
    "scriptureRef": "Mateus 27:51",
    "hint": "Simbolizando que o acesso ao Santo dos Santos da presença de Deus agora estava aberto a todos pela Expiação.",
    "explanation": "O rasgamento do véu atestou a conclusão da antiga ordem sacrificial e a abertura da graça divina."
  },
  {
    "id": "nt_066",
    "category": "nt",
    "difficulty": 3,
    "question": "O que o centurião romano e os soldados aos pés da cruz exclamaram aterrorizados após o terremoto na morte de Jesus?",
    "options": [
      "Este homem veio para restaurar o reino de Davi",
      "Este homem era o profeta anunciado por Moisés",
      "Verdadeiramente este homem era o Filho de Deus!",
      "Verdadeiramente este era o rei prometido a Israel"
    ],
    "correct": 2,
    "scriptureRef": "Mateus 27:54",
    "hint": "Mesmo os algozes pagãos foram tomados de reverência perante os sinais miraculosos da natureza.",
    "explanation": "O centurião romano prestou um testemunho espontâneo e imorredouro sobre a divindade de Cristo."
  },
  {
    "id": "nt_067",
    "category": "nt",
    "difficulty": 2,
    "question": "Em Mateus 28:19-20, qual é a solene ordem conhecida como 'A Grande Comissão' dada pelo Salvador ressuscitado aos Seus discípulos?",
    "options": [
      "Ir a todas as nações, fazer discípulos e batizar em nome do Pai, Filho e Espírito Santo",
      "Reunir as tribos e estabelecer o reino em Jerusalém",
      "Levar as ofertas dos gentios aos sacerdotes de Jerusalém",
      "Ensinar somente em Israel até a reconstrução do templo"
    ],
    "correct": 0,
    "scriptureRef": "Mateus 28:19-20",
    "hint": "E Ele acrescentou: 'E eis que eu estou convosco todos os dias, até a consumação dos séculos'.",
    "explanation": "O mandato divino de estender as bênçãos do Evangelho e do batismo a todas as etnias e povos da Terra."
  },
  {
    "id": "nt_068",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual diácono da Igreja foi preso perante o Sinédrio e viu os céus abertos e o Salvador em pé à destra de Deus antes de ser martirizado?",
    "options": [
      "Nicanor",
      "Prócoro",
      "Estêvão",
      "Filipe"
    ],
    "correct": 2,
    "scriptureRef": "Atos 7:55-56",
    "hint": "Seu rosto brilhava como o rosto de um anjo e suas últimas palavras foram de perdão a seus carrascos.",
    "explanation": "Estêvão foi o primeiro mártir cristão, e Saulo de Tarso consentia em sua morte guardando as vestes dos agressores."
  },
  {
    "id": "nt_069",
    "category": "nt",
    "difficulty": 2,
    "question": "Na estrada para qual cidade Saulo de Tarso foi envolvido por uma luz celestial mais resplandecente que o sol e ouviu a voz de Jesus?",
    "options": [
      "Roma",
      "Damasco",
      "Atenas",
      "Antioquia"
    ],
    "correct": 1,
    "scriptureRef": "Atos 9:1-6",
    "hint": "Ele caiu por terra e perguntou: 'Quem és, Senhor?'. E ouviu: 'Eu sou Jesus, a quem tu persegues'.",
    "explanation": "A monumental conversão de Saulo em Damasco transformou o mais feroz perseguidor no maior apóstolo aos gentios."
  },
  {
    "id": "nt_070",
    "category": "nt",
    "difficulty": 3,
    "question": "Quem era o discípulo em Damasco a quem o Senhor apareceu em visão ordenando que fosse à rua chamada Direita para impor as mãos sobre Saulo cego?",
    "options": [
      "Barnabé",
      "Ananias",
      "Silas",
      "Tíquico"
    ],
    "correct": 1,
    "scriptureRef": "Atos 9:10-18",
    "hint": "O Senhor garantiu-lhe: 'Vai, porque este é para mim um vaso escolhido para levar o meu nome perante os gentios...'.",
    "explanation": "Ananias obedeceu à revelação e restaurou a visão de Paulo, batizando-o imediatamente."
  },
  {
    "id": "nt_071",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual levita generoso da ilha de Chipre vendeu um campo que possuía e levou o dinheiro aos pés dos apóstolos, sendo chamado de 'filho da consolação'?",
    "options": [
      "Barnabé, também chamado José",
      "Simão, também chamado Níger",
      "João, também chamado Marcos",
      "Judas, também chamado Barsabás"
    ],
    "correct": 0,
    "scriptureRef": "Atos 4:36-37",
    "hint": "Ele acolheu Paulo quando os outros apóstolos ainda temiam recebê-lo em Jerusalém.",
    "explanation": "Barnabé foi um dos esteios mais generosos e misericordiosos do apostolado primitivo."
  },
  {
    "id": "nt_072",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual ourives em Éfeso incitou um tumulto violento contra Paulo porque suas pregações estavam arruinando o comércio dos nichos de prata da deusa Diana?",
    "options": [
      "Demétrio",
      "Simão",
      "Alexandre",
      "Elmas"
    ],
    "correct": 0,
    "scriptureRef": "Atos 19:24-29",
    "hint": "A multidão enfurecida arrastou os companheiros de Paulo ao teatro gritando por duas horas: 'Grande é a Diana dos efésios!'.",
    "explanation": "O tumulto de Demétrio em Éfeso reflete o conflito entre o evangelho de Cristo e a idolatria comercial pagã."
  },
  {
    "id": "nt_073",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual rei judeu herodiano disse a Paulo durante seu julgamento em Cesareia: 'Por pouco me persuades a me fazer cristão'?",
    "options": [
      "Pórcio Festo",
      "Herodes Agripa II",
      "Félix",
      "Tibério"
    ],
    "correct": 1,
    "scriptureRef": "Atos 26:28",
    "hint": "Irmão de Berenice, que ouviu o relato de Paulo com grande interesse junto com o governador Festo.",
    "explanation": "Paulo respondeu: 'Quem dera a Deus que... não somente tu, mas também todos os que hoje me ouvem, se tornassem tais qual eu sou, exceto estas algemas'."
  },
  {
    "id": "nt_074",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual governador romano no julgamento de Paulo em Cesareia esperava secretamente receber suborno (dinheiro) para libertá-lo, mantendo-o preso por dois anos?",
    "options": [
      "Festo",
      "Pilatos",
      "Gálio",
      "Félix"
    ],
    "correct": 3,
    "scriptureRef": "Atos 24:26-27",
    "hint": "Ele tremia quando Paulo pregava sobre a justiça, a temperança e o juízo vindouro, mas adiava a decisão.",
    "explanation": "Félix deixou Paulo na prisão para agradar aos líderes judeus antes de ser substituído por Festo."
  },
  {
    "id": "nt_075",
    "category": "nt",
    "difficulty": 3,
    "question": "Em Romanos 8:38-39, qual é a gloriosa declaração de Paulo sobre o amor de Deus?",
    "options": [
      "O amor de Deus se limita aos que nasceram sob a lei",
      "A vida mortal é a única ocasião de receber o amor divino",
      "Nem morte, vida ou qualquer outra criatura nos separará do amor de Deus em Cristo",
      "As tribulações mostram que o amor de Deus se retirou"
    ],
    "correct": 2,
    "scriptureRef": "Romanos 8:38-39",
    "hint": "'Porque estou certo de que, nem a morte, nem a vida, nem anjos... nem altura, nem profundidade...'",
    "explanation": "Uma das mais sublimes passagens de segurança espiritual e vitória da fé de toda a teologia paulina."
  },
  {
    "id": "nt_076",
    "category": "nt",
    "difficulty": 3,
    "question": "Em 1 Coríntios 15:29, qual prática cristã primitiva da Igreja original Paulo menciona para comprovar a realidade da ressurreição dos mortos?",
    "options": [
      "O batismo em favor dos mortos, mencionado ao defender a ressurreição",
      "A partilha do pão nas reuniões da Igreja",
      "A coleta de ofertas para os santos",
      "A imposição de mãos sobre enfermos"
    ],
    "correct": 0,
    "scriptureRef": "1 Coríntios 15:29",
    "hint": "Esta passagem bíblica corrobora diretamente a sagrada ordenança vicária restaurada no templo moderno.",
    "explanation": "Paulo usou a ordenança do batismo vicário como argumento irrefutável para demonstrar que os mortos de fato ressuscitam."
  },
  {
    "id": "nt_077",
    "category": "nt",
    "difficulty": 3,
    "question": "Em 2 Timóteo 4:7-8, como o Apóstolo Paulo resume sua vida ministerial ao antecipar seu próximo martírio em Roma?",
    "options": [
      "Recebi a coroa dos homens e entregarei meu lugar a outro",
      "Combati o bom combate, terminei a carreira, guardei a fé",
      "Percorri todas as nações e agora espero voltar a Jerusalém",
      "Edifiquei muitas igrejas, e ainda me resta completar a lei"
    ],
    "correct": 1,
    "scriptureRef": "2 Timóteo 4:7-8",
    "hint": "A mais serena e vitoriosa declaração de despedida de um apóstolo fiel do Senhor.",
    "explanation": "Paulo encerra seu ministério com a certeza inabalável da coroa de justiça reservada pelo Justo Juiz a todos os que amam a Sua vinda."
  },
  {
    "id": "nt_078",
    "category": "nt",
    "difficulty": 2,
    "question": "Em Tiago 1:5, qual promessa inspirou o jovem Joseph Smith a orar no Bosque Sagrado na primavera de 1820?",
    "options": [
      "Se falta sabedoria, deve-se pedi-la a Deus, que dá liberalmente sem censurar",
      "Quem deseja compreender deve pedir um sinal dos céus",
      "Quem precisa de conselho deve aguardar uma visão noturna",
      "Quem busca a verdade deve consultar primeiro os escribas"
    ],
    "correct": 0,
    "scriptureRef": "Tiago 1:5; JS-H 1:11-12",
    "hint": "Esta passagem penetrou com mais força no coração de Joseph do que qualquer outra escritura jamais fizera.",
    "explanation": "Tiago convida a todos os que buscam a verdade a exercerem fé inabalável diretamente diante do Pai celestial."
  },
  {
    "id": "nt_079",
    "category": "nt",
    "difficulty": 3,
    "question": "Em 1 João 4:8, qual é a definição teológica mais simples e profunda sobre a essência de Deus?",
    "options": [
      "Deus é espírito",
      "Deus é luz",
      "Deus é amor",
      "Deus é fogo consumidor"
    ],
    "correct": 2,
    "scriptureRef": "1 João 4:8",
    "hint": "'Aquele que não ama não conhece a Deus; porque Deus é amor.'",
    "explanation": "O Apóstolo Amado sintetiza a natureza do Pai e do Filho no mais puro amor sacrificial."
  },
  {
    "id": "nt_080",
    "category": "nt",
    "difficulty": 4,
    "question": "No livro de Apocalipse, qual é o título que Jesus Cristo atribui a Si mesmo no primeiro e no último capítulo indicando Sua eternidade?",
    "options": [
      "O pão que desceu do céu",
      "O caminho, a verdade e a vida",
      "A ressurreição e a vida",
      "O Alfa e o Ômega, o princípio e o fim"
    ],
    "correct": 3,
    "scriptureRef": "Apocalipse 1:8; 22:13",
    "hint": "Primeira e última letra do alfabeto grego, representando a plenitude da criação e da redenção.",
    "explanation": "Cristo é o início e a consumação de todo o plano de felicidade e salvação eterna."
  },
  {
    "id": "nt_081",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual dos evangelistas era médico de profissão e companheiro fiel de viagens do Apóstolo Paulo?",
    "options": [
      "Mateus",
      "João",
      "Marcos",
      "Lucas"
    ],
    "correct": 3,
    "scriptureRef": "Colossenses 4:14",
    "hint": "Ele escreveu tanto o Evangelho que leva seu nome quanto o livro de Atos dos Apóstolos.",
    "explanation": "Lucas dedicou sua erudição médica e estilo refinado para registrar detalhadamente o ministério de Cristo e dos apóstolos."
  },
  {
    "id": "nt_082",
    "category": "nt",
    "difficulty": 4,
    "question": "A qual personagem ilustre, cujo nome significa 'amigo de Deus', Lucas dedicou tanto o seu Evangelho quanto o livro de Atos dos Apóstolos?",
    "options": [
      "Cornélio",
      "Tito",
      "Teófilo",
      "Timóteo"
    ],
    "correct": 2,
    "scriptureRef": "Lucas 1:3; Atos 1:1",
    "hint": "Lucas o tratou respeitosamente como 'excelentíssimo Teófilo'.",
    "explanation": "Teófilo foi o ilustre patrono cristão que financiou ou recebeu os anais históricos compilados por Lucas."
  },
  {
    "id": "nt_083",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual mulher cristã em Filipos vendia tecidos de púrpura caríssimos e foi a primeira convertida de Paulo na Europa, hospedando os apóstolos em sua casa?",
    "options": [
      "Febe",
      "Priscila",
      "Lídia",
      "Evódia"
    ],
    "correct": 2,
    "scriptureRef": "Atos 16:14-15",
    "hint": "Natural da cidade de Tiatira, temente a Deus, cujo coração o Senhor abriu para atender às palavras de Paulo.",
    "explanation": "O batismo de Lídia e de sua casa estabeleceu o primeiro núcleo cristão no continente europeu."
  },
  {
    "id": "nt_084",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual homem erudito de Alexandria, eloquente e poderoso nas Escrituras, pregava fervorosamente em Éfeso conhecendo apenas o batismo de João, até ser instruído por Áquila e Priscila?",
    "options": [
      "Barnabé",
      "Tito",
      "Apolo",
      "Sétimo"
    ],
    "correct": 2,
    "scriptureRef": "Atos 18:24-26",
    "hint": "Áquila e Priscila o chamaram e lhe expuseram com mais exatidão o caminho de Deus.",
    "explanation": "Apolo tornou-se um brilhante missionário em Corinto, refutando publicamente os judeus e provando que Jesus era o Cristo."
  },
  {
    "id": "nt_085",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual discípulo Paulo chamou de 'meu verdadeiro filho na fé', circuncidando-o por causa dos judeus e ordenando-o líder na Igreja?",
    "options": [
      "Tito",
      "Lucas",
      "Marcos",
      "Timóteo"
    ],
    "correct": 3,
    "scriptureRef": "1 Timóteo 1:2; Atos 16:1-3",
    "hint": "Filho de pai grego e mãe judia crente chamada Eunice e avó Lóide.",
    "explanation": "Timóteo foi um dos colaboradores mais caros de Paulo, liderando a congregação de Éfeso com grande retidão."
  },
  {
    "id": "nt_086",
    "category": "nt",
    "difficulty": 3,
    "question": "Em 2 Tessalonicenses 2:3, que acontecimento histórico sombrio Paulo profetiza que haveria de ocorrer antes da Segunda Vinda de Jesus Cristo?",
    "options": [
      "A apostasia e a revelação do homem do pecado",
      "O retorno do sacerdócio levítico ao templo de Jerusalém",
      "A conversão dos governantes romanos antes das perseguições",
      "A restauração do reino político de Israel pelos apóstolos"
    ],
    "correct": 0,
    "scriptureRef": "2 Tessalonicenses 2:3",
    "hint": "'Ninguém de maneira alguma vos engane; porque isto não acontecerá sem que primeiro venha a apostasia...'",
    "explanation": "Paulo profetizou a perda da autoridade do sacerdócio e da doutrina pura dos apóstolos, antecipando a necessidade da Restauração."
  },
  {
    "id": "nt_087",
    "category": "nt",
    "difficulty": 3,
    "question": "Em 1 Coríntios 12, a que Paulo compara a Igreja com seus diferentes membros e dons espirituais?",
    "options": [
      "A um rebanho e seus diferentes pastores",
      "A uma plantação e seus diferentes frutos",
      "Ao corpo humano, com seus vários membros",
      "A uma construção e suas diferentes pedras"
    ],
    "correct": 2,
    "scriptureRef": "1 Coríntios 12:12-27",
    "hint": "Cada membro possui um papel vital, e os membros que parecem mais fracos são muito necessários.",
    "explanation": "A harmonia orgânica do corpo de Cristo ensina que todos os dons e membros são essenciais para a edificação de Sião."
  },
  {
    "id": "nt_088",
    "category": "nt",
    "difficulty": 2,
    "question": "No Sermão da Montanha, o que Jesus disse que Seus discípulos deveriam fazer com seus inimigos em Mateus 5:44?",
    "options": [
      "Perdoar os inimigos somente depois de uma reparação pública",
      "Tratar os inimigos segundo a medida do que fizeram antes",
      "Amar os amigos e evitar qualquer contato com os inimigos",
      "Amar os inimigos, fazer o bem a quem os odeia e orar por quem os persegue"
    ],
    "correct": 3,
    "scriptureRef": "Mateus 5:44",
    "hint": "O mais elevado e revolucionário padrão ético e espiritual de discipulado de todos os tempos.",
    "explanation": "Cristo estabelece que o amor verdadeiro estende misericórdia mesmo aos perseguidores, refletindo o caráter do Pai celestial."
  },
  {
    "id": "nt_089",
    "category": "nt",
    "difficulty": 2,
    "question": "Qual é a oração perfeita ensinada por Jesus a Seus discípulos quando eles pediram: 'Senhor, ensina-nos a orar'?",
    "options": [
      "O Pai Nosso, dirigido ao Pai que está nos céus",
      "A oração de Jonas no ventre do peixe",
      "A oração de Salomão no templo",
      "A oração de Davi no Salmo 51"
    ],
    "correct": 0,
    "scriptureRef": "Mateus 6:9-13; Lucas 11:1-4",
    "hint": "Modelo eterno de oração simples, sincera, reverente e que busca a vontade do Pai antes de tudo.",
    "explanation": "O Pai Nosso ensina a priorizar a glória de Deus, o perdão mútuo e a busca do sustento diário."
  },
  {
    "id": "nt_090",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual árvore frutífera Jesus secou com uma palavra por ter muitas folhas mas nenhum fruto quando Ele teve fome perto de Betânia?",
    "options": [
      "Uma oliveira",
      "Uma videira",
      "Uma figueira",
      "Uma romãzeira"
    ],
    "correct": 2,
    "scriptureRef": "Mateus 21:18-22; Marcos 11:12-14",
    "hint": "No dia seguinte os discípulos viram a árvore seca desde as raízes.",
    "explanation": "A figueira estéril serviu de lição indelével contra a hipocrisia religiosa de aparência sem frutos de retidão."
  },
  {
    "id": "nt_091",
    "category": "nt",
    "difficulty": 4,
    "question": "Quem era o pai de João Batista, sacerdote da ordem de Abias, que ficou mudo até a circuncisão de seu filho por duvidar do anjo Gabriel no templo?",
    "options": [
      "Simeão",
      "Caifás",
      "Zacarias",
      "Nicodemos"
    ],
    "correct": 2,
    "scriptureRef": "Lucas 1:5-20",
    "hint": "Ele escreveu numa tabuinha: 'O seu nome é João', e imediatamente sua língua se soltou para louvar a Deus.",
    "explanation": "Zacarias e Isabel eram justos diante de Deus, e seu filho João Batista preparou os caminhos do Messias."
  },
  {
    "id": "nt_092",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual era a profissão de Mateus quando Jesus o viu na coletoria de impostos em Cafarnaum e lhe disse: 'Segue-me'?",
    "options": [
      "Cobrador de impostos",
      "Comerciante de tecidos",
      "Pescador no mar da Galileia",
      "Administrador de sinagoga"
    ],
    "correct": 0,
    "scriptureRef": "Mateus 9:9",
    "hint": "Também chamado de Levi, filho de Alfeu, que deixou sua mesa de dinheiro e ofereceu um banquete a Jesus.",
    "explanation": "A vocação de Mateus provou que Jesus não veio chamar os justos, mas os pecadores ao arrependimento."
  },
  {
    "id": "nt_093",
    "category": "nt",
    "difficulty": 3,
    "question": "Como o relato de Marcos 5:25–34 identifica a mulher curada de uma hemorragia após tocar a roupa de Jesus?",
    "options": [
      "Era Maria, irmã de Marta",
      "Era Salomé, mãe dos filhos de Zebedeu",
      "Era Joana, mulher de Cuza",
      "Não informa o nome da mulher"
    ],
    "correct": 3,
    "scriptureRef": "Marcos 5:25-34",
    "hint": "Jesus sentiu que de Si havia saído poder (virtude) e perguntou: 'Quem tocou nas minhas vestes?'.",
    "explanation": "Ela gastara todos os seus bens com médicos sem obter melhora, mas foi curada num instante ao tocar na orla de Cristo."
  },
  {
    "id": "nt_094",
    "category": "nt",
    "difficulty": 3,
    "question": "Qual chefe da sinagoga em Cafarnaum suplicou a Jesus que fosse à sua casa curar sua filha de doze anos que estava à beira da morte?",
    "options": [
      "Bartimeu",
      "Nicodemos",
      "Zaqueu",
      "Jairo"
    ],
    "correct": 3,
    "scriptureRef": "Marcos 5:22-23, 41-42",
    "hint": "Jesus entrou no aposento, tomou a menina pela mão e disse: 'Talita cumi' (que traduzido é: Menina, a ti te digo, levanta-te).",
    "explanation": "A menina levantou-se e andou imediatamente, enchendo os pais e discípulos de assombro."
  },
  {
    "id": "nt_095",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual dos discípulos de Jesus em Betânia ungiu os pés do Salvador com óleo precioso e os enxugou com os seus próprios cabelos?",
    "options": [
      "Maria, irmã de Marta",
      "Maria, chamada Madalena",
      "Joana, mulher de Cuza",
      "Salomé, mãe de Tiago e João"
    ],
    "correct": 0,
    "scriptureRef": "João 12:1-3",
    "hint": "Enquanto sua irmã Marta se ocupava em servir, ela assentou-se aos pés de Jesus para ouvir Sua palavra.",
    "explanation": "Jesus declarou que Maria havia escolhido a boa parte, a qual não lhe seria tirada."
  },
  {
    "id": "nt_096",
    "category": "nt",
    "difficulty": 4,
    "question": "O que Pilatos fez publicamente com uma bacia de água diante da multidão para simbolizar que se declarava inocente da morte de Jesus?",
    "options": [
      "Lavou o rosto e ordenou aos soldados que soltassem Jesus",
      "Derramou a água e entregou sua autoridade ao conselho",
      "Lavou as mãos diante do povo e declarou-se inocente do sangue daquele justo",
      "Ofereceu a água aos sacerdotes e pediu outra audiência"
    ],
    "correct": 2,
    "scriptureRef": "Mateus 27:24",
    "hint": "A mais célebre e covarde tentativa política de se esquivar da responsabilidade moral por condenar o Inocente.",
    "explanation": "Mesmo sabendo que Jesus era justo e que os líderes judeus O entregavam por inveja, Pilatos cedeu à pressão popular."
  },
  {
    "id": "nt_097",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual notório criminoso, preso por sedição e assassinato em Jerusalém, a multidão escolheu para ser solto em lugar de Jesus no indulto da Páscoa?",
    "options": [
      "Dimas",
      "Barrabás",
      "Judas",
      "Gestas"
    ],
    "correct": 1,
    "scriptureRef": "Mateus 27:16-21; Marcos 15:7",
    "hint": "Os principais sacerdotes instigaram o povo para que pedissem a libertação deste assassino.",
    "explanation": "Barrabás foi liberto enquanto o Cordeiro Imaculado de Deus foi entregue para ser crucificado em seu lugar."
  },
  {
    "id": "nt_098",
    "category": "nt",
    "difficulty": 4,
    "question": "Segundo a interpretação de Apocalipse 5 em D&C 77:6–7, o que representa o conteúdo do livro selado?",
    "options": [
      "As ordenanças civis a serem observadas pelas sete igrejas",
      "Os nomes dos reis que governariam o Império Romano",
      "As regras do sacerdócio levítico para o serviço do templo",
      "A vontade e os propósitos de Deus para a Terra ao longo de sua história"
    ],
    "correct": 3,
    "scriptureRef": "Apocalipse 5; D&C 77:6–7",
    "hint": "D&C 77:6 revela que os sete selos contêm as coisas secretas da economia de Deus durante as sete dispensações temporais.",
    "explanation": "O Leão da tribo de Judá, o Cordeiro como havendo sido morto, venceu para abrir os sete selos e revelar o destino do mundo."
  },
  {
    "id": "nt_099",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual é o rio que flui do trono de Deus e do Cordeiro na Nova Jerusalém, ladeado pela árvore da vida cujas folhas servem para a saúde das nações?",
    "options": [
      "O rio que Israel atravessou com Josué",
      "O rio junto ao qual João pregava o batismo",
      "O rio da água da vida, claro como cristal, que sai do trono de Deus",
      "O rio que atravessa o jardim do Éden"
    ],
    "correct": 2,
    "scriptureRef": "Apocalipse 22:1-2",
    "hint": "A árvore produz doze frutos, dando seu fruto de mês em mês.",
    "explanation": "Apocalipse 22 culmina com a restauração do paraíso eterno, onde a morte, a dor e a maldição cessam para sempre."
  },
  {
    "id": "nt_100",
    "category": "nt",
    "difficulty": 4,
    "question": "Qual bênção encerra o livro de Apocalipse?",
    "options": [
      "A graça de nosso Senhor Jesus Cristo seja com todos vós",
      "O amor de Deus e a comunhão do Espírito sejam convosco",
      "Ao único Deus sábio seja dada glória para todo o sempre",
      "A paz seja com todos os que estão em Cristo Jesus"
    ],
    "correct": 0,
    "scriptureRef": "Apocalipse 22:21",
    "hint": "A bênção apostólica universal que sela a revelação sagrada do Salvador da humanidade.",
    "explanation": "A Bíblia se despede da humanidade invocando a graça soberana e santificadora de Jesus Cristo sobre todos os crentes."
  }
]

def build():
    target = Path(__file__).resolve().with_name("data_nt.js")
    content = "/** Banco revisado: 100 perguntas; alternativas e gabaritos sincronizados. */\nvar QUESTIONS_NT = "
    content += json.dumps(questions, ensure_ascii=False, indent=2) + ";\n"
    target.write_text(content, encoding="utf-8")
    print(f"Sucesso: {target.name} gerado com {len(questions)} perguntas.")

if __name__ == "__main__":
    build()
