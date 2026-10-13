# -*- coding: utf-8 -*-
"""Gerador do banco DC; mantém textos revisados e gabaritos distribuídos."""
import json
from pathlib import Path

questions = [
  {
    "id": "dc_001",
    "category": "dc",
    "difficulty": 1,
    "question": "Onde o Senhor declarou ser a Sua 'única igreja verdadeira e viva sobre a face de toda a Terra, com a qual eu, o Senhor, me comprazo'?",
    "options": [
      "Em Doutrina e Convênios 20:1",
      "Em Doutrina e Convênios 76:50",
      "Em Doutrina e Convênios 88:1",
      "Em Doutrina e Convênios 1:30"
    ],
    "correct": 3,
    "scriptureRef": "D&C 1:30",
    "hint": "Revelação do prefácio oficial do livro dada em Hiram, Ohio, em novembro de 1831.",
    "explanation": "D&C 1:30 afirma que a Igreja restaurada possui a autoridade divina das chaves do sacerdócio para administrar a salvação."
  },
  {
    "id": "dc_002",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual é a promessa de Morôni a Joseph Smith registrada em D&C 2 sobre o plantio nos corações dos filhos das promessas feitas aos pais?",
    "options": [
      "O templo seria construído antes da organização da Igreja",
      "As dez tribos seriam reunidas antes da tradução do livro",
      "Revelar o sacerdócio pela mão de Elias antes do grande e terrível dia do Senhor",
      "As placas seriam entregues antes de sua próxima visita"
    ],
    "correct": 2,
    "scriptureRef": "D&C 2:1-3",
    "hint": "Se assim não fosse, toda a Terra seria totalmente devastada em Sua vinda.",
    "explanation": "D&C 2 contém as palavras exatas proferidas pelo Anjo Morôni a Joseph Smith na noite de 21 de setembro de 1823."
  },
  {
    "id": "dc_003",
    "category": "dc",
    "difficulty": 2,
    "question": "Quantas páginas do manuscrito da tradução inicial do Livro de Mórmon Martin Harris perdeu no verão de 1828 após levá-las para Palmyra?",
    "options": [
      "116 páginas",
      "100 páginas",
      "144 páginas",
      "50 páginas"
    ],
    "correct": 0,
    "scriptureRef": "D&C 3: Cabeçalho; D&C 10",
    "hint": "Correspondiam ao Livro de Leí, que o Senhor substituiu com sabedoria eterna pelas placas menores de Néfi.",
    "explanation": "A perda das 116 páginas levou à severa repreensão em D&C 3, ensinando que 'as obras e os desígnios e os propósitos de Deus não podem ser frustrados'."
  },
  {
    "id": "dc_004",
    "category": "dc",
    "difficulty": 1,
    "question": "Em D&C 4:2, com o que o Senhor exige que sirvamos a Ele nesta grandiosa obra para sermos considerados sem culpa no último dia?",
    "options": [
      "Com todo o coração, poder, mente e força",
      "Com todas as ofertas, posses, colheitas e habilidades",
      "Com toda a sabedoria, tradição, influência e eloquência",
      "Com todo o conhecimento, prestígio, tempo e patrimônio"
    ],
    "correct": 0,
    "scriptureRef": "D&C 4:2",
    "hint": "'Ó vós que embarcais no serviço de Deus, vede que o sirvais de todo o coração...'.",
    "explanation": "A seção 4 estabelece o modelo espiritual fundamental de discipulado missionário de consagração total a Deus."
  },
  {
    "id": "dc_005",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 8 e 9, como o Senhor descreve o 'espírito de revelação' dado a Oliver Cowdery para discernir a verdade?",
    "options": [
      "Por sinais exteriores, sem necessidade de estudar a questão",
      "Por meio do Espírito Santo, falando à mente e ao coração de quem busca revelação",
      "Somente por sonhos que repetem a mesma mensagem",
      "Por palavras audíveis, sem participação do entendimento"
    ],
    "correct": 1,
    "scriptureRef": "D&C 8:2; 9:8",
    "hint": "Ele ensinou que a revelação requer estudo diligente na mente antes de perguntar ao Senhor.",
    "explanation": "D&C 8 e 9 são as seções clássicas que ensinam como os sussurros mansas e tranquilos do Espírito Santo operam na mente e no coração."
  },
  {
    "id": "dc_006",
    "category": "dc",
    "difficulty": 2,
    "question": "Quais três testemunhas foram escolhidas por revelação divina em D&C 17 para contemplarem as placas de ouro, o peitoral, a espada de Labão e a Liahona?",
    "options": [
      "Sidney Rigdon, Parley P. Pratt e Hyrum Smith",
      "Joseph Smith Sr., John Whitmer e Peter Whitmer",
      "Brigham Young, Heber C. Kimball e John Taylor",
      "Oliver Cowdery, David Whitmer e Martin Harris"
    ],
    "correct": 3,
    "scriptureRef": "D&C 17:1",
    "hint": "Um anjo desceu dos céus na floresta de Fayette e lhes mostrou os registros sagrados com a voz de Deus confirmando a tradução.",
    "explanation": "As Três Testemunhas mantiveram seu solene testemunho inabalável até o fim de seus dias, mesmo quando passaram por crises pessoais."
  },
  {
    "id": "dc_007",
    "category": "dc",
    "difficulty": 1,
    "question": "Em D&C 18:10, qual é a sublime verdade declarada pelo Senhor sobre a dignidade de cada filho de Deus?",
    "options": [
      "O valor das almas se mede pela influência sobre o próximo",
      "O valor das almas aumenta conforme os cargos recebidos",
      "O valor de cada alma é grande aos olhos de Deus, segundo a declaração do Senhor",
      "O valor das almas depende do conhecimento já adquirido"
    ],
    "correct": 2,
    "scriptureRef": "D&C 18:10",
    "hint": "E o versículo seguinte explica: 'Porque eis que o Senhor vosso Redentor sofreu a morte na carne; portanto sofreu as dores de todos os homens'.",
    "explanation": "A seção 18 ensina que a Expiação infinita de Jesus Cristo é a medida real do valor infinito que cada alma tem para o Pai."
  },
  {
    "id": "dc_008",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 19:16-19, qual descrição íntima e comovente o próprio Salvador ressuscitado faz de Seu sofrimento no Getsêmani?",
    "options": [
      "Sofreu a ponto de tremer de dor, sangrar por todos os poros e desejar não beber o cálice",
      "Sentiu angústia, mas não sofreu dor física durante a expiação",
      "Recebeu auxílio que o dispensou de beber o amargo cálice",
      "Sofreu pelos justos, deixando aos demais toda a própria dor"
    ],
    "correct": 0,
    "scriptureRef": "D&C 19:18-19",
    "hint": "O único registro canônico em todas as escrituras onde o próprio Jesus descreve na primeira pessoa a agonia de Sua Expiação.",
    "explanation": "D&C 19 é um dos textos mais sagrados de toda a cristandade, revelando o sacrifício pessoal do Redentor para que não precisemos sofrer se nos arrependermos."
  },
  {
    "id": "dc_009",
    "category": "dc",
    "difficulty": 3,
    "question": "O que o Senhor ordenou expressamente a Martin Harris em D&C 19 para permitir a impressão das cinco mil cópias da primeira edição do Livro de Mórmon em Palmyra?",
    "options": [
      "Transferir a dívida aos escribas responsáveis pela tradução",
      "Aguardar as vendas do livro para assumir a dívida da impressão",
      "Obter dos futuros leitores o pagamento antecipado dos livros",
      "Oferecer seus bens liberalmente para a impressão e pagar a dívida com o impressor"
    ],
    "correct": 3,
    "scriptureRef": "D&C 19:26, 35",
    "hint": "Martin Harris hipotecou e vendeu 151 acres de sua preciosa fazenda para honrar o contrato de 3.000 dólares com Egbert B. Grandin.",
    "explanation": "A abnegação financeira e sacrifício de Martin Harris viabilizou a publicação e disseminação do Livro de Mórmon no mundo."
  },
  {
    "id": "dc_010",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual seção de Doutrina e Convênios é formalmente conhecida como os 'Artigos e Convênios da Igreja', servindo como a sua constituição eclesiástica inicial?",
    "options": [
      "Seção 42",
      "Seção 20",
      "Seção 1",
      "Seção 107"
    ],
    "correct": 1,
    "scriptureRef": "D&C 20",
    "hint": "Lida e aceita em conferência no início da Restauração, detalha deveres dos oficiais e as orações do sacramento.",
    "explanation": "D&C 20 estabeleceu a estrutura organizacional, crenças basilares e funções sacerdotais da Igreja restaurada."
  },
  {
    "id": "dc_011",
    "category": "dc",
    "difficulty": 1,
    "question": "Em D&C 25, qual honroso e carinhoso título o Senhor concedeu a Emma Smith, instruindo-a a compilar o primeiro livro de hinos sagrados da Igreja?",
    "options": [
      "'A matriarca da fé'",
      "'Uma mulher eleita'",
      "'A rainha de Sião'",
      "'A profetisa de Nova York'"
    ],
    "correct": 1,
    "scriptureRef": "D&C 25:3, 11",
    "hint": "'Pois minha alma se deleita com o canto do coração; sim, o cântico dos justos é uma prece a mim...'.",
    "explanation": "A seção 25 foi uma revelação pessoal de consolo e comissionamento divino à esposa do Profeta Joseph Smith."
  },
  {
    "id": "dc_012",
    "category": "dc",
    "difficulty": 2,
    "question": "O que o Senhor esclareceu em D&C 27 sobre o que deve ser usado na ordenança do Sacramento da Ceia do Senhor?",
    "options": [
      "O alimento deve seguir todas as prescrições da Páscoa judaica",
      "O alimento importa menos que a intenção de honrar Cristo",
      "A bebida deve ser produzida no lugar onde a Igreja se reúne",
      "O pão deve ser preparado apenas pelos membros do sacerdócio"
    ],
    "correct": 1,
    "scriptureRef": "D&C 27:2",
    "hint": "Esta revelação permitiu o uso da água limpa em vez do vinho para preservar a santidade da ordenança.",
    "explanation": "D&C 27 enfatiza que a intenção pura do coração e a lembrança do corpo e sangue de Cristo são a essência do sacramento."
  },
  {
    "id": "dc_013",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual membro de Fayette afirmava receber revelações para a Igreja por meio de uma pedra escura, sendo corrigido pelo Senhor em D&C 28?",
    "options": [
      "David Whitmer",
      "Martin Harris",
      "Hiram Page",
      "Oliver Cowdery"
    ],
    "correct": 2,
    "scriptureRef": "D&C 28:11-14",
    "hint": "O Senhor esclareceu que somente Joseph Smith fora designado para receber mandamentos e revelações para toda a Igreja.",
    "explanation": "Hiram Page reconheceu seu erro com humildade, e a seção 28 consolidou a ordem de sucessão e revelação no sacerdócio."
  },
  {
    "id": "dc_014",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual ministro congregacional e restauracionista eloquente de Ohio converteu-se ao ler o Livro de Mórmon e tornou-se escriba e conselheiro de Joseph Smith?",
    "options": [
      "Sidney Rigdon",
      "Edward Partridge",
      "Parley P. Pratt",
      "W. W. Phelps"
    ],
    "correct": 0,
    "scriptureRef": "D&C 35",
    "hint": "Parley P. Pratt e outros missionários aos lamanitas pregaram em sua congregação em Mentor e Kirtland.",
    "explanation": "Sidney Rigdon levou grande parte de seu rebanho batista/campbelita para a Igreja e contemplou a Visão de D&C 76 junto com Joseph."
  },
  {
    "id": "dc_015",
    "category": "dc",
    "difficulty": 3,
    "question": "Quem foi chamado em D&C 41 para ser o primeiro bispo da Igreja restaurada em Kirtland, Ohio?",
    "options": [
      "Newel K. Whitney",
      "Algernon Sidney Gilbert",
      "Titus Billings",
      "Edward Partridge"
    ],
    "correct": 3,
    "scriptureRef": "D&C 41:9",
    "hint": "Ele era um comerciante próspero e honesto, de quem o Senhor disse que seu coração era puro como o de Natanael.",
    "explanation": "Edward Partridge administrou a lei de consagração e os armazéns dos pobres no Missouri com integridade exemplar."
  },
  {
    "id": "dc_016",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual seção recebida em Kirtland em fevereiro de 1831 é formalmente designada como 'A Lei da Igreja' revelando os princípios da lei de consagração?",
    "options": [
      "Seção 20",
      "Seção 42",
      "Seção 88",
      "Seção 133"
    ],
    "correct": 1,
    "scriptureRef": "D&C 42:1-73",
    "hint": "Contém mandamentos morais, a lei de assistência aos pobres e as instruções para administrar a propriedade consagrada.",
    "explanation": "D&C 42 é uma das revelações fundamentais da Restauração, cumprindo a promessa de que a lei seria dada em Ohio."
  },
  {
    "id": "dc_017",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 57, qual localidade exata no Condado de Jackson, Missouri, o Senhor designou como o lugar central de Sião e o sítio para o futuro grande templo?",
    "options": [
      "Far West",
      "Independence",
      "Adam-ondi-Ahman",
      "Liberty"
    ],
    "correct": 1,
    "scriptureRef": "D&C 57:1-3",
    "hint": "'Eis que o lugar que é agora chamado Independence é o lugar central; e um sítio para o templo acha-se a oeste...'.",
    "explanation": "Em julho de 1831, Joseph Smith dedicou a terra de Independence e o terreno do templo em cumprimento a essa revelação."
  },
  {
    "id": "dc_018",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual princípio de livre-arbítrio e responsabilidade pessoal o Senhor ensina enfaticamente em D&C 58:26-28?",
    "options": [
      "Transferir aos líderes a responsabilidade por cada decisão",
      "Esperar uma ordem específica antes de iniciar qualquer obra",
      "Limitar o serviço às tarefas expressamente dadas por revelação",
      "Ocupar-se zelosamente numa boa causa, fazendo muito por livre e espontânea vontade"
    ],
    "correct": 3,
    "scriptureRef": "D&C 58:26-28",
    "hint": "Aquele que é compelido em tudo é um servo indolente e não sábio.",
    "explanation": "O Senhor ensina que Ele nos concede inteligência, arbítrio e poder para operarmos a retidão por iniciativa própria."
  },
  {
    "id": "dc_019",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 59:9-10, qual é o propósito sagrado do Dia do Senhor revelado aos santos?",
    "options": [
      "Interromper todo serviço, inclusive o cuidado dos necessitados",
      "Substituir a oração pessoal pela participação nos negócios da Igreja",
      "Ir à casa de oração, oferecer os sacramentos e manter-se limpo das manchas do mundo",
      "Reservar o culto para uma reunião anual de agradecimento"
    ],
    "correct": 2,
    "scriptureRef": "D&C 59:9-10",
    "hint": "Dia santificado para descansar dos trabalhos materiais e prestar devoção ao Altíssimo.",
    "explanation": "D&C 59 estabelece o Dia do Senhor como um deleite espiritual e uma renovação dos convênios batismais."
  },
  {
    "id": "dc_020",
    "category": "dc",
    "difficulty": 4,
    "question": "Quem tentou redigir um mandamento semelhante ao menor dos mandamentos do Senhor em uma conferência em Hiram em novembro de 1831 e fracassou, conforme o desafio de D&C 67?",
    "options": [
      "Oliver Cowdery",
      "David Whitmer",
      "William E. McLellin",
      "Sidney Rigdon"
    ],
    "correct": 2,
    "scriptureRef": "D&C 67:5-8",
    "hint": "O Senhor desafiou os élderes a indicarem o mais sábio entre eles para escrever uma revelação parecida.",
    "explanation": "McLellin tentou pela sua erudição secular compor uma revelação divina e não conseguiu, fortalecendo a fé de todos na inspiração de Joseph Smith."
  },
  {
    "id": "dc_021",
    "category": "dc",
    "difficulty": 1,
    "question": "Qual grandiosa seção de Doutrina e Convênios registra 'A Visão' dos Três Graus de Glória (Celestial, Terrestre e Teleste), contemplada por Joseph Smith e Sidney Rigdon em 1832?",
    "options": [
      "Seção 88",
      "Seção 110",
      "Seção 121",
      "Seção 76"
    ],
    "correct": 3,
    "scriptureRef": "D&C 76",
    "hint": "Eles contemplaram o Salvador à destra de Deus e exclamaram: 'E agora, depois dos muitos testemunhos que se prestaram dele, este é o testemunho... que ele vive!'.",
    "explanation": "D&C 76 expandiu de modo revolucionário a compreensão da salvação humana, dissipando o dogma tradicional do céu e inferno universais."
  },
  {
    "id": "dc_022",
    "category": "dc",
    "difficulty": 2,
    "question": "A quem se destina a mais sublime e excelsa glória do Reino Celestial segundo a revelação de D&C 76:50-70?",
    "options": [
      "Os honrados que não são valentes no testemunho de Jesus",
      "Os que recebem Cristo, guardam convênios e são selados",
      "Todos os que recebem um corpo, independentemente de sua vida",
      "Os que rejeitam o evangelho, mas o aceitam só após sofrer"
    ],
    "correct": 1,
    "scriptureRef": "D&C 76:51-53",
    "hint": "Eles são sacerdotes e reis do Altíssimo e habitarão na presença de Deus e de Seu Cristo para todo o sempre.",
    "explanation": "Os herdeiros do reino celestial vencem o mundo pela fé em Cristo e tornam-se deuses, co-herdeiros com o Salvador."
  },
  {
    "id": "dc_023",
    "category": "dc",
    "difficulty": 3,
    "question": "Quem herda o Reino Terrestre conforme descrito em D&C 76:71-79?",
    "options": [
      "Os que negam deliberadamente o poder de Deus que conheceram",
      "Os que rejeitam tanto o evangelho como o testemunho de Jesus",
      "Os fiéis selados pelo Santo Espírito da Promessa",
      "Os honrados que não são valentes no testemunho de Jesus"
    ],
    "correct": 3,
    "scriptureRef": "D&C 76:71-79",
    "hint": "Eles recebem da presença do Filho, mas não da plenitude do Pai.",
    "explanation": "A glória terrestre abriga as pessoas sinceras e justas que não demonstraram bravura ou valentia no evangelho de Cristo."
  },
  {
    "id": "dc_024",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 76, quem são os únicos indivíduos que se tornam 'Filhos de Perdição' para os quais não há perdão nem redenção?",
    "options": [
      "Os que conhecem o poder de Deus e o negam deliberadamente",
      "Os que cometem pecados antes de conhecer os convênios do evangelho",
      "Os que morrem sem nunca ter recebido uma oportunidade de crer",
      "Os que abandonam uma reunião por dúvidas sobre uma doutrina"
    ],
    "correct": 0,
    "scriptureRef": "D&C 76:31-37",
    "hint": "Eles pecam contra a luz do meio-dia tendo recebido um conhecimento seguro do Espírito Santo.",
    "explanation": "Os filhos de perdição rejeitam deliberadamente o Espírito Santo após conhecê-Lo plenamente, sofrendo a segunda morte espiritual."
  },
  {
    "id": "dc_025",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 84:33-39, qual é a grandiosa promessa do Senhor àqueles que obtêm e magnificam ambos os sacerdócios (Aarônico e de Melquisedeque)?",
    "options": [
      "Tudo o que o Pai possui será dado aos que receberem e magnificarem esse convênio",
      "Governar politicamente os povos que aceitarem o evangelho",
      "Receber uma herança material garantida durante a mortalidade",
      "Ficar livre de todas as provações após receber o sacerdócio"
    ],
    "correct": 0,
    "scriptureRef": "D&C 84:38",
    "hint": "'E aquele que me recebe a mim, recebe a meu Pai; e aquele que recebe a meu Pai, recebe o reino de meu Pai...'.",
    "explanation": "O juramento e convênio do sacerdócio promete a exaltação suprema e a plenitude da herança celestial de Deus."
  },
  {
    "id": "dc_026",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual seção profética recebida no Natal de 1832 profetizou com precisão que a Guerra Civil Americana começaria com a rebelião da Carolina do Sul?",
    "options": [
      "Seção 45",
      "Seção 133",
      "Seção 87",
      "Seção 135"
    ],
    "correct": 2,
    "scriptureRef": "D&C 87:1-3",
    "hint": "Recebida 28 anos antes do primeiro disparo dos canhões contra Fort Sumter na baía de Charleston.",
    "explanation": "D&C 87 profetizou a divisão entre os estados do sul e do norte por causa da escravidão e o subsequente derramamento de sangue."
  },
  {
    "id": "dc_027",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual seção maravilhosa foi chamada carinhosamente por Joseph Smith de 'A Folha de Oliveira colhida na árvore do Paraíso'?",
    "options": [
      "Seção 93",
      "Seção 76",
      "Seção 88",
      "Seção 110"
    ],
    "correct": 2,
    "scriptureRef": "D&C 88: Cabeçalho",
    "hint": "Mensagem de paz aos santos, ordenando a construção do Templo de Kirtland e a fundação da Escola dos Profetas.",
    "explanation": "D&C 88 ensina sobre a Luz de Cristo, leis eternas do universo, ressurreição e a busca do conhecimento secular e sagrado."
  },
  {
    "id": "dc_028",
    "category": "dc",
    "difficulty": 1,
    "question": "Em D&C 88:118, qual é o célebre mandamento educacional do Senhor para os santos dos últimos dias?",
    "options": [
      "Esperar que todo conhecimento seja concedido sem preparação",
      "Limitar o estudo aos livros escritos pelos primeiros apóstolos",
      "Buscar conhecimento apenas por meio de revelações pessoais",
      "Buscar sabedoria nos melhores livros e procurar conhecimento pelo estudo e pela fé"
    ],
    "correct": 3,
    "scriptureRef": "D&C 88:118",
    "hint": "O alicerce do compromisso milenar da Igreja com a instrução intelectual, acadêmica e espiritual.",
    "explanation": "O Senhor ordena que os santos busquem erudição de qualidade e refinamento intelectual sob a luz da fé cristã."
  },
  {
    "id": "dc_029",
    "category": "dc",
    "difficulty": 1,
    "question": "Qual é a lei de saúde recebida em Kirtland em 27 de fevereiro de 1833, que adverte contra bebidas fortes, tabaco e bebidas quentes?",
    "options": [
      "A Palavra de Sabedoria, revelada na seção 89",
      "O juramento e convênio do sacerdócio",
      "A lei da consagração dos bens",
      "A lei do dízimo e das ofertas"
    ],
    "correct": 0,
    "scriptureRef": "D&C 89",
    "hint": "Promete que aqueles que a guardarem correrão e não se cansarão, e o anjo destruidor passará por eles como nos dias de Israel.",
    "explanation": "D&C 89 protege a integridade do templo do corpo humano para que seja uma habitação digna do Espírito Santo."
  },
  {
    "id": "dc_030",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 93:29, qual doutrina sublime sobre a natureza eterna da inteligência e do espírito humano é revelada?",
    "options": [
      "A inteligência começa apenas quando se adquire consciência",
      "A inteligência é criada quando o espírito recebe um corpo",
      "A inteligência estava no princípio com Deus e não foi criada, nem pode ser feita",
      "A inteligência passa a existir quando o corpo é concebido"
    ],
    "correct": 2,
    "scriptureRef": "D&C 93:29",
    "hint": "Um dos conceitos mais grandiosos e originais da teologia restaurada de Joseph Smith.",
    "explanation": "D&C 93 estabelece a pré-mortalidade eterna do ser humano e a coeternidade de sua inteligência com o Pai Celestial."
  },
  {
    "id": "dc_031",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 107, por que o Sacerdócio Maior, antigamente chamado de Sacerdócio segundo a Ordem do Filho de Deus, teve seu nome alterado para Sacerdócio de Melquisedeque?",
    "options": [
      "Para marcar o fim de toda ordenação pela linhagem de Arão",
      "Para evitar repetir excessivamente o nome do Ser Supremo",
      "Para indicar que o sacerdócio passaria a pertencer somente a reis",
      "Para substituir o nome antigo, que não fora preservado nos registros"
    ],
    "correct": 1,
    "scriptureRef": "D&C 107:2-4",
    "hint": "Melquisedeque foi um homem de fé tão grandiosa e grande sumo sacerdote que a Igreja passou a chamá-lo por seu nome.",
    "explanation": "A Igreja utiliza o nome do rei de Salém para proteger a santidade do sagrado nome do Salvador."
  },
  {
    "id": "dc_032",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual vale sagrado no Missouri foi designado pelo Senhor em D&C 116 como o lugar onde o patriarca Adão visitará seu povo perante a Segunda Vinda?",
    "options": [
      "Adam-ondi-Ahman",
      "Vale de Zaraenla",
      "Vale da Decisão",
      "Planícies de Far West"
    ],
    "correct": 0,
    "scriptureRef": "D&C 116:1; 107:53-56",
    "hint": "Três anos antes de morrer, Adão reuniu seus descendentes justos neste vale e os abençoou profetizando tudo o que lhes sucederia.",
    "explanation": "Adam-ondi-Ahman será o cenário do grandioso conselho onde Adão devolverá as chaves de liderança ao Salvador Jesus Cristo."
  },
  {
    "id": "dc_033",
    "category": "dc",
    "difficulty": 2,
    "question": "Quais quatro mensageiros celestes apareceram no Templo de Kirtland em 3 de abril de 1836 (Páscoa) restaurando chaves supremas do sacerdócio registradas em D&C 110?",
    "options": [
      "Pedro, Tiago, João e João Batista",
      "Adão, Noé, Abraão e Melquisedeque",
      "Jesus Cristo, Moisés, Elias e Elias o Profeta",
      "Morôni, Néfi, Alma e Mórmon"
    ],
    "correct": 2,
    "scriptureRef": "D&C 110:1-16",
    "hint": "Cristo aceitou a casa dedicada e os profetas antigos entregaram as chaves do recolhimento de Israel e do selamento.",
    "explanation": "O dia 3 de abril de 1836 foi o clímax da Restauração das chaves do sacerdócio para a dispensação da plenitude dos tempos."
  },
  {
    "id": "dc_034",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual chave específica do sacerdócio o antigo profeta Moisés restaurou a Joseph Smith e Oliver Cowdery no púlpito do Templo de Kirtland?",
    "options": [
      "As chaves da dispensação do evangelho de Abraão",
      "Recolher Israel das quatro partes da Terra e conduzir as dez tribos do norte",
      "As chaves da ministração de anjos e do batismo",
      "As chaves do selamento das famílias para a eternidade"
    ],
    "correct": 1,
    "scriptureRef": "D&C 110:11",
    "hint": "Autoridade sob a qual toda a gigantesca obra missionária da Igreja é realizada no mundo inteiro.",
    "explanation": "Moisés entregou as chaves proféticas para reunir a semente de Israel dispersa nas nações."
  },
  {
    "id": "dc_035",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual é o nome oficial e solene da Igreja revelado diretamente pelo Salvador em Far West, Missouri, em 26 de abril de 1838 em D&C 115:4?",
    "options": [
      "A Igreja de Jesus Cristo e dos Santos da Nova Aliança",
      "A Igreja Restaurada de Jesus Cristo e dos Santos",
      "A Igreja dos Santos de Jesus Cristo nos Últimos Dias",
      "A Igreja de Jesus Cristo dos Santos dos Últimos Dias"
    ],
    "correct": 3,
    "scriptureRef": "D&C 115:4",
    "hint": "'Pois assim será a minha igreja chamada nos últimos dias, sim, A Igreja de Jesus Cristo dos Santos dos Últimos Dias.'",
    "explanation": "O Senhor estabeleceu o nome definitivo de Sua Igreja, que une o Seu sagrado nome com a designação dos membros no tempo do fim."
  },
  {
    "id": "dc_036",
    "category": "dc",
    "difficulty": 1,
    "question": "Em D&C 121:7-8, qual terna e inesquecível resposta o Senhor deu a Joseph Smith nas trevas gélidas da Cadeia de Liberty?",
    "options": [
      "Paz à alma; as aflições durariam um pequeno momento",
      "Vitória nos tribunais; todos os acusadores retirariam as denúncias",
      "Liberdade imediata; os guardas abririam a cadeia naquela noite",
      "Fim das perseguições; os santos retornariam de imediato ao Missouri"
    ],
    "correct": 0,
    "scriptureRef": "D&C 121:7-8",
    "hint": "O mais belo e consolador bálsamo celestial para os momentos de profunda angústia humana.",
    "explanation": "O Senhor assegurou a Seu profeta que a aflição mortal é passageira e serve para a nossa santificação e glória eterna."
  },
  {
    "id": "dc_037",
    "category": "dc",
    "difficulty": 2,
    "question": "Segundo D&C 121:34-42, como o poder e autoridade do sacerdócio devem ser exercidos, sob pena de os céus se afastarem e o homem ser deixado a escoicear contra os aguilhões?",
    "options": [
      "Por persuasão, longanimidade, mansidão, amor sincero, bondade e conhecimento puro",
      "Pela disciplina imposta sem necessidade de explicar as decisões",
      "Pela posição ocupada, mesmo sem o consentimento dos outros",
      "Pelo prestígio adquirido e pela obediência irrestrita aos dirigentes"
    ],
    "correct": 0,
    "scriptureRef": "D&C 121:41-42",
    "hint": "Nenhum poder ou influência pode ou deve ser mantido em virtude do sacerdócio a não ser com essas virtudes cristãs.",
    "explanation": "D&C 121 ensina que o sacerdócio de Deus é completamente incompatível com qualquer forma de compulsão, domínio injusto ou tirania."
  },
  {
    "id": "dc_038",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 122:7-8, após enumerar todas as mais atrozes tribulações possíveis, qual foi a solene pergunta retórica que o Senhor fez a Joseph Smith?",
    "options": [
      "Se teus amigos te abandonaram, em quem depositarás confiança?",
      "Se o povo deixou suas casas, quem reconstruirá as cidades de Sião?",
      "O Filho do Homem desceu abaixo de tudo; és maior que ele?",
      "Se recebeste tantas promessas, por que ainda buscas um sinal?"
    ],
    "correct": 2,
    "scriptureRef": "D&C 122:7-8",
    "hint": "Lembrando ao servo que o Salvador vivenciou o abismo mais profundo de toda dor e abandono.",
    "explanation": "Esta pergunta humilhou e fortaleceu o Profeta, lembrando que a graça redentora de Cristo compreende perfeitamente todas as nossas dores."
  },
  {
    "id": "dc_039",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 128:8, qual princípio divino fundamenta a validade cósmica das ordenanças do templo registradas fielmente na Terra?",
    "options": [
      "O registro celestial dispensa testemunhas e registros terrenos",
      "As ordenanças só passam a valer depois da ressurreição",
      "O que é ligado e devidamente registrado na Terra também é reconhecido nos céus",
      "Somente os registros feitos pelos primeiros apóstolos são aceitos"
    ],
    "correct": 2,
    "scriptureRef": "D&C 128:8",
    "hint": "Esta chave do sacerdócio une os registros fidedignos dos templos à eternidade do tribunal de Deus.",
    "explanation": "Joseph Smith explica que o poder selador do sacerdócio garante a autenticidade das ordenanças vicárias pelos mortos no céu."
  },
  {
    "id": "dc_040",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 130:22, qual verdade fundamental e física sobre os membros da Trindade é claramente revelada pelo Profeta Joseph Smith?",
    "options": [
      "Só o Pai possui corpo; o Filho e o Espírito Santo são espíritos",
      "Os três possuem corpos de carne e ossos separados e tangíveis",
      "Pai e Filho têm corpo; o Espírito Santo é personagem de espírito",
      "Pai e Espírito Santo têm corpo; o Filho é personagem de espírito"
    ],
    "correct": 2,
    "scriptureRef": "D&C 130:22",
    "hint": "Um dos pilares doutrinários restaurados que distingue claramente a fé dos santos dos credos tradicionais.",
    "explanation": "Esta revelação esclarece a individualidade física de Deus o Pai e de Jesus Cristo ressuscitado como seres tangíveis e exaltados."
  },
  {
    "id": "dc_041",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 131:1-4, o que uma pessoa deve fazer para alcançar o mais alto e glorioso grau de glória dentro do Reino Celestial?",
    "options": [
      "Receber a ordenação ao sacerdócio sem outros convênios",
      "Entrar no novo e eterno convênio do casamento, pela autoridade de selamento",
      "Ser chamado a presidir um quórum dos Doze Apóstolos",
      "Realizar todas as ordenanças apenas em favor dos mortos"
    ],
    "correct": 1,
    "scriptureRef": "D&C 131:1-4",
    "hint": "Sem este convênio, o homem pode entrar nos outros graus do reino celestial, mas não pode ter exaltação e continuação de semente para sempre.",
    "explanation": "O casamento celestial é a ordenança culminante do templo que permite ao marido e à mulher tornarem-se criadores e pais eternos com Deus."
  },
  {
    "id": "dc_042",
    "category": "dc",
    "difficulty": 1,
    "question": "Em que data histórica o Profeta Joseph Smith e seu irmão Hyrum selaram seus testemunhos com o próprio sangue na Cadeia de Carthage, Illinois?",
    "options": [
      "6 de abril de 1830",
      "24 de julho de 1847",
      "15 de maio de 1829",
      "27 de junho de 1844"
    ],
    "correct": 3,
    "scriptureRef": "D&C 135:1",
    "hint": "Eram cerca das cinco horas da tarde quando uma turba armada com rostos pintados de preto invadiu a prisão.",
    "explanation": "D&C 135 registra o comovente martírio dos dois irmãos, coroando a missão profética do vidente de Deus nesta dispensação."
  },
  {
    "id": "dc_043",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 135:3, qual grandioso tributo o élder John Taylor presta a Joseph Smith pelo imenso volume de obra realizada para a salvação da humanidade?",
    "options": [
      "Só Jesus fez mais pela salvação dos homens que Joseph",
      "Joseph realizou a mesma obra que cada profeta do passado",
      "Joseph seria lembrado principalmente por governar Nauvoo",
      "Sua principal contribuição foi conduzir os pioneiros até Utah"
    ],
    "correct": 0,
    "scriptureRef": "D&C 135:3",
    "hint": "Ele trouxe à luz o Livro de Mórmon, Doutrina e Convênios, a Pérola de Grande Valor, organizou a Igreja e enviou o evangelho aos quatro cantos da Terra.",
    "explanation": "O tributo de D&C 135 sintetiza a amplitude incomparável da Restauração da verdade operada pelo instrumento de Joseph Smith."
  },
  {
    "id": "dc_044",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual presidente da Igreja recebeu a revelação registrada em D&C 136 em Winter Quarters, organizando as companhias de pioneiros com capitães de cem, de cinquenta e de dez para a travessia das planícies?",
    "options": [
      "John Taylor",
      "Wilford Woodruff",
      "Brigham Young",
      "Lorenzo Snow"
    ],
    "correct": 2,
    "scriptureRef": "D&C 136:1-3",
    "hint": "'A Palavra e Vontade do Senhor concernente ao Acampamento de Israel em sua jornada para o Oeste.'",
    "explanation": "Brigham Young recebeu este modelo organizacional divinamente inspirado para conduzir com segurança mais de 70 mil santos pioneiros até o Vale do Lago Salgado."
  },
  {
    "id": "dc_045",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual irmão Joseph Smith viu no reino celestial na visão registrada em D&C 137?",
    "options": [
      "William Smith, seu irmão",
      "Samuel Smith, seu irmão",
      "Alvin Smith, seu irmão",
      "Don Carlos Smith, seu irmão"
    ],
    "correct": 2,
    "scriptureRef": "D&C 137:5-8",
    "hint": "Alvin Smith havia falecido tragicamente em 1823 antes da organização da Igreja e fora condenado por pastores locais por não ter sido batizado.",
    "explanation": "Esta sublime visão de 1836 abriu as portas da teologia da misericórdia de Deus e fundamentou a obra sagrada do batismo pelos mortos."
  },
  {
    "id": "dc_046",
    "category": "dc",
    "difficulty": 3,
    "question": "O que o Presidente Joseph F. Smith contemplou na gloriosa Visão da Redenção dos Mortos registrada em D&C 138 sobre o ministério de Cristo entre Sua morte e ressurreição?",
    "options": [
      "A pregação começou somente depois da ressurreição de todos os mortos",
      "Os justos aguardaram a ressurreição sem poder ensinar aos demais",
      "Cristo pregou pessoalmente a todos os espíritos dos desobedientes",
      "Cristo organizou mensageiros para ensinar os espíritos em prisão"
    ],
    "correct": 3,
    "scriptureRef": "D&C 138:29-37",
    "hint": "Recebida em outubro de 1918, desvendando o funcionamento perfeito da obra missionária no mundo espiritual dos mortos.",
    "explanation": "D&C 138 revela que os espíritos fiéis que partiram continuam seus labores ministeriais pregando aos que morreram em ignorância ou transgressão."
  },
  {
    "id": "dc_047",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual documento oficial anexado a Doutrina e Convênios foi promulgado pelo Presidente Wilford Woodruff em outubro de 1890 anunciando o fim da prática do casamento plural?",
    "options": [
      "A carta que contém as Regras de Fé",
      "A proclamação sobre a família",
      "A Declaração Oficial 2",
      "A Declaração Oficial 1"
    ],
    "correct": 3,
    "scriptureRef": "Declaração Oficial 1",
    "hint": "O Presidente declarou que o Senhor lhe mostrou em visão as consequências de destruição dos templos e confisco se a prática não cessasse perante as leis civis.",
    "explanation": "O Manifesto de 1890 pacificou as tensões legais com o governo dos Estados Unidos e permitiu a dedicação do Templo de Salt Lake e o reconhecimento de Utah como Estado."
  },
  {
    "id": "dc_048",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual revelação histórica recebida pelo Presidente Spencer W. Kimball em 1º de junho de 1978 estendeu todas as ordenanças do sacerdócio e do templo a todos os homens dignos de todas as raças?",
    "options": [
      "Declaração Oficial 1",
      "Doutrina e Convênios 139",
      "Carta de Wentworth",
      "Declaração Oficial 2"
    ],
    "correct": 3,
    "scriptureRef": "Declaração Oficial 2",
    "hint": "Recebida no Templo de Salt Lake após fervorosas súplicas conjuntas da Primeira Presidência e do Quórum dos Doze Apóstolos.",
    "explanation": "A Declaração Oficial 2 expandiu globalmente o sacerdócio divino e o trabalho do templo a todas as nações, tribos, línguas e povos."
  },
  {
    "id": "dc_049",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual é a lei financeira divina revelada na Seção 119 de Doutrina e Convênios em resposta à pergunta: 'Ó Senhor, mostra a teus servos quanto requeres dos bens de teu povo como dízimo'?",
    "options": [
      "A metade dos lucros obtidos no comércio",
      "Uma contribuição fixa igual para todas as famílias",
      "Entregar anualmente a décima parte de sua renda, conforme a lei do dízimo",
      "A quinta parte da renda anual"
    ],
    "correct": 2,
    "scriptureRef": "D&C 119:3-4",
    "hint": "Dada em Far West, Missouri, em 8 de julho de 1838, permanecendo como a lei permanente do dízimo até hoje.",
    "explanation": "D&C 119 estabelece o dízimo de 10% da renda como a lei sagrada de consagração e sustentação da obra de Deus."
  },
  {
    "id": "dc_050",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 130:20-21, qual é a lei cósmica e irrevogável que governa o recebimento de qualquer bênção de Deus?",
    "options": [
      "A posição ocupada dentro da organização da Igreja",
      "O número de pedidos feitos a respeito da mesma necessidade",
      "Recebemos bênçãos pela obediência à lei sobre a qual cada uma foi estabelecida",
      "O tempo decorrido desde a realização do primeiro convênio"
    ],
    "correct": 2,
    "scriptureRef": "D&C 130:20-21",
    "hint": "O princípio da causa e efeito espiritual na economia celestial.",
    "explanation": "Esta verdade fundamental ensina que o recebimento das dádivas do Senhor está perfeitamente atrelado à nossa obediência aos mandamentos."
  },
  {
    "id": "dc_051",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual apóstolo cantou o hino Um Pobre e Aflito Viajante na Cadeia de Carthage antes da morte de Joseph e Hyrum Smith?",
    "options": [
      "John Taylor",
      "Willard Richards",
      "Parley P. Pratt",
      "W. W. Phelps"
    ],
    "correct": 0,
    "scriptureRef": "D&C 135:2-3",
    "hint": "Hyrum Smith pediu que ele cantasse o hino uma segunda vez para trazer paz ao aposento.",
    "explanation": "John Taylor cantou este comovente hino de compaixão cristã minutos antes da invasão armada à prisão."
  },
  {
    "id": "dc_052",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual médico fiel e apóstolo acompanhou Joseph e Hyrum na Cadeia de Carthage e não sofreu nenhum ferimento sequer, cumprindo uma profecia anterior de Joseph de que 'as balas passariam ao seu redor como pássaros sem tocá-lo'?",
    "options": [
      "Cyrus Wheelock",
      "Willard Richards",
      "Dan Jones",
      "John Taylor"
    ],
    "correct": 1,
    "scriptureRef": "D&C 135:2",
    "hint": "Ele escapou milagrosamente sem nenhum orifício em sua túnica, exceto um pequeno arranhão na orelha.",
    "explanation": "Willard Richards sobreviveu ileso ao tiroteio e cuidou dos ferimentos graves de John Taylor, preservando os registros do martírio."
  },
  {
    "id": "dc_053",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 123:17, com que atitude o Senhor convida os santos a enfrentarem as perseguições e a cumprirem seu dever cristão na Terra?",
    "options": [
      "Fazer alegremente o possível e confiar na salvação de Deus",
      "Entregar aos tribunais toda a responsabilidade pelo futuro dos santos",
      "Esperar sem agir até que todos os adversários mudem de atitude",
      "Deixar de pregar enquanto não cessarem as perseguições civis"
    ],
    "correct": 0,
    "scriptureRef": "D&C 123:17",
    "hint": "Escrito das profundezas da prisão de Liberty como o encerramento da carta pastoral de Joseph Smith.",
    "explanation": "Este conselho imorredouro ensina a conjugar a diligência alegre no dever com a confiança serena e absoluta na redenção de Deus."
  },
  {
    "id": "dc_054",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual era a missão histórica da expedição chamada 'Acampamento de Sião' (Zion's Camp), organizada sob a direção de Joseph Smith em 1834 conforme D&C 103 e 105?",
    "options": [
      "Ir ao Missouri para socorrer os santos expulsos e ajudá-los a recuperar suas terras",
      "Conduzir as famílias pioneiras para o vale do Lago Salgado",
      "Reunir trabalhadores para a construção do templo de Nauvoo",
      "Levar os primeiros missionários para as cidades da Inglaterra"
    ],
    "correct": 0,
    "scriptureRef": "D&C 103:22-35; D&C 105:1-19",
    "hint": "Embora não tenham entrado em combate armado por instrução divina nas águas do Rio Pesca, a marcha de mais de mil milhas forjou a liderança futura de apóstolos como Brigham Young e Heber C. Kimball.",
    "explanation": "O Acampamento de Sião foi a grande forja espiritual de liderança onde os futuros líderes da Igreja demonstraram sua lealdade inabalável a Deus."
  },
  {
    "id": "dc_055",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 105:9-10, por que o Senhor ordenou que o Acampamento de Sião não redimisse Sião pelas armas naquela ocasião, dissolvendo a companhia?",
    "options": [
      "Os santos precisavam aprender a obedecer e os élderes receber poder do alto",
      "O governador já havia devolvido todas as propriedades aos santos",
      "Era preciso aguardar a chegada de mais armas e munições",
      "Os líderes receberam ordem de abandonar definitivamente Sião"
    ],
    "correct": 0,
    "scriptureRef": "D&C 105:9-11",
    "hint": "'Portanto, é necessário que espereis por um pouco de tempo a redenção de Sião...'.",
    "explanation": "O Senhor ensinou que Sião é edificada sobre princípios de retidão espiritual celestial e não por meio de conquista armada."
  },
  {
    "id": "dc_056",
    "category": "dc",
    "difficulty": 2,
    "question": "Qual membro foi advertido em D&C 5:1-3 de que 'não tem o dom de destruir' e que se continuasse fiel o Senhor lhe concederia uma vista das placas?",
    "options": [
      "David Whitmer",
      "Martin Harris",
      "Oliver Cowdery",
      "Joseph Knight Sr."
    ],
    "correct": 1,
    "scriptureRef": "D&C 5:1-4",
    "hint": "Ele viajou a Harmonia em março de 1829 pedindo um testemunho tangível das placas para tranquilizar sua esposa Lucy Harris.",
    "explanation": "O Senhor instruiu Martin Harris a buscar a fé verdadeira em vez de apenas evidências materiais externas."
  },
  {
    "id": "dc_057",
    "category": "dc",
    "difficulty": 3,
    "question": "Que dom, além do espírito de revelação, é mencionado para Oliver Cowdery em D&C 8:6–8?",
    "options": [
      "O dom de Arão, associado à revelação",
      "O dom de interpretar línguas sem tradução",
      "O dom de restaurar os registros perdidos do manuscrito",
      "O dom de presidir todas as congregações dos santos"
    ],
    "correct": 0,
    "scriptureRef": "D&C 8:6-8",
    "hint": "'Lembra-te de que este é o teu dom... não há outro poder, a não ser o poder de Deus, que possa fazer com que este dom funcione em ti'.",
    "explanation": "Oliver possuía grande sensibilidade espiritual e dons que o capacitavam a auxiliar o Profeta na grande obra da Restauração."
  },
  {
    "id": "dc_058",
    "category": "dc",
    "difficulty": 3,
    "question": "O que o Senhor prometeu em D&C 6:36 como o antídoto definitivo para vencer a dúvida e o medo espiritual?",
    "options": [
      "Confiar no próprio entendimento até receber uma visão completa",
      "Buscar o Senhor em cada pensamento e enfrentar as circunstâncias sem dúvida nem temor",
      "Aguardar um sinal visível antes de tomar qualquer decisão",
      "Recorrer somente aos que já passaram pela mesma experiência"
    ],
    "correct": 1,
    "scriptureRef": "D&C 6:36",
    "hint": "'Olhai para mim em todos os pensamentos... vede as feridas que me perfuraram o lado e as marcas dos cravos nas minhas mãos e pés'.",
    "explanation": "A contínua concentração mental e espiritual no Salvador dissipa a incerteza e a ansiedade da alma."
  },
  {
    "id": "dc_059",
    "category": "dc",
    "difficulty": 4,
    "question": "Quem era o irmão de Joseph Smith para quem o Senhor revelou a seção 11 em Harmonia, instruindo-o a esperar e estudar a palavra antes de tentar pregar?",
    "options": [
      "Don Carlos Smith",
      "Samuel H. Smith",
      "William Smith",
      "Hyrum Smith"
    ],
    "correct": 3,
    "scriptureRef": "D&C 11:21-22",
    "hint": "'Não procures pregar a minha palavra, mas primeiro procura obter a minha palavra; e depois tua língua será solta...'.",
    "explanation": "Hyrum Smith obedeceu com paciência exemplar, tornando-se o Patriarca da Igreja e o braço direito leal do Profeta."
  },
  {
    "id": "dc_060",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 12, qual amigo leal de Colesville, Nova York, foi aconselhado pelo Senhor após transportar suprimentos e papel para Joseph e Oliver enquanto traduziam?",
    "options": [
      "Newel Knight",
      "Joseph Knight Sr.",
      "Peter Whitmer",
      "Thomas B. Marsh"
    ],
    "correct": 1,
    "scriptureRef": "D&C 12",
    "hint": "Ele forneceu grãos, carne e papel de escrita essenciais durante os dias mais difíceis da tradução em Harmonia.",
    "explanation": "A família Knight foi uma das primeiras e mais firmes aliadas da Restauração do evangelho."
  },
  {
    "id": "dc_061",
    "category": "dc",
    "difficulty": 3,
    "question": "Onde João Batista apareceu em 15 de maio de 1829 para restaurar o Sacerdócio Aarônico a Joseph Smith e Oliver Cowdery?",
    "options": [
      "No bosque perto da casa dos Smith em Palmyra",
      "Às margens do rio Susquehanna, nas proximidades de Harmony, na Pensilvânia",
      "Na fazenda da família Whitmer em Fayette",
      "Na encosta do monte onde estavam as placas"
    ],
    "correct": 1,
    "scriptureRef": "D&C 13; JS-H 1:68-72",
    "hint": "Eles haviam ido à floresta para orar a respeito do batismo para a remissão dos pecados mencionado na tradução de 3 Néfi.",
    "explanation": "João Batista impôs as mãos sobre Joseph e Oliver, restaurando as chaves do ministério de anjos e do batismo por imersão."
  },
  {
    "id": "dc_062",
    "category": "dc",
    "difficulty": 2,
    "question": "Em D&C 18, quais três líderes foram incumbidos do chamado apostólico de buscar e escolher os futuros Doze Apóstolos da Igreja restaurada?",
    "options": [
      "Edward Partridge, Newel K. Whitney e W. W. Phelps",
      "Joseph Smith, Sidney Rigdon e Hyrum Smith",
      "Oliver Cowdery, David Whitmer e Martin Harris",
      "Brigham Young, Heber C. Kimball e John Taylor"
    ],
    "correct": 2,
    "scriptureRef": "D&C 18:26-37",
    "hint": "Eles deveriam procurar os Doze que tivessem o testemunho seguro e o desejo de tomar sobre si o nome de Jesus Cristo.",
    "explanation": "Em fevereiro de 1835, as Três Testemunhas ordenaram o primeiro Quórum dos Doze Apóstolos desta dispensação."
  },
  {
    "id": "dc_063",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual irmão mais novo de Joseph Smith foi ordenado o primeiro missionário oficial da Igreja recém-organizada em 1830 e vendeu exemplares do Livro de Mórmon que converteram a família de Brigham Young e Heber C. Kimball?",
    "options": [
      "Don Carlos Smith",
      "William Smith",
      "Samuel H. Smith",
      "Alvin Smith"
    ],
    "correct": 2,
    "scriptureRef": "História da Igreja, vol. 1",
    "hint": "Ele colocou livros em sua mochila e viajou a pé pelos condados vizinhos semeando a verdade com grande persistência.",
    "explanation": "A perseverança missionária solitária de Samuel H. Smith trouxe gigantes espirituais para as fileiras da Restauração."
  },
  {
    "id": "dc_064",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 21:4-6, dada no dia da organização da Igreja, qual é a promessa para aqueles que receberem as palavras do profeta como se saíssem da própria boca de Deus?",
    "options": [
      "Nenhuma oposição política voltará a atingir suas famílias",
      "Todas as dificuldades materiais desaparecerão de sua vida",
      "As portas do inferno não prevaleceriam, e o Senhor dispersaria os poderes das trevas",
      "Os tribunais reconhecerão imediatamente todos os seus direitos"
    ],
    "correct": 2,
    "scriptureRef": "D&C 21:4-6",
    "hint": "O mandamento exige paciência e fé para seguir o profeta vivo mesmo em tempos de prova.",
    "explanation": "A segurança espiritual dos santos está atrelada à obediência aos conselhos proféticos inspirados pelo Senhor."
  },
  {
    "id": "dc_065",
    "category": "dc",
    "difficulty": 4,
    "question": "Quem era o primeiro presidente do Quórum dos Doze Apóstolos na Restauração que mais tarde apostatou por uma disputa banal envolvendo leite desnatado de sua esposa e se afastou da Igreja?",
    "options": [
      "David W. Patten",
      "Luke S. Johnson",
      "William Smith",
      "Thomas B. Marsh"
    ],
    "correct": 3,
    "scriptureRef": "D&C 112; História da Igreja",
    "hint": "Mais tarde, na velhice em Salt Lake City, ele confessou seu erro e voltou humilde à Igreja pedindo perdão.",
    "explanation": "O caso de Thomas B. Marsh adverte sobre como pequenas mágoas e orgulho podem privar grandes líderes de seu galardão."
  },
  {
    "id": "dc_066",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual valoroso apóstolo foi o primeiro mártir do Quórum dos Doze, morto na Batalha do Rio Crooked no Missouri em 1838, cuja fé inabalável foi elogiada em D&C 124:19?",
    "options": [
      "Lyman Wight",
      "Parley P. Pratt",
      "David W. Patten",
      "Orson Hyde"
    ],
    "correct": 2,
    "scriptureRef": "D&C 124:19; D&C 114",
    "hint": "Suas últimas palavras aos companheiros foram: 'Não importa a morte; tudo está bem, tudo está bem!'.",
    "explanation": "David W. Patten selou seu apostolado com heroísmo defendendo seus irmãos contra turbas armadas no Missouri."
  },
  {
    "id": "dc_067",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual apóstolo viajou à Palestina e, em 24 de outubro de 1841, ajoelhou-se no Monte das Oliveiras e dedicou a Terra Santa para o retorno do povo judeu e reconstrução de Jerusalém?",
    "options": [
      "Orson Hyde",
      "Orson Pratt",
      "Wilford Woodruff",
      "John Taylor"
    ],
    "correct": 0,
    "scriptureRef": "História da Igreja, vol. 4",
    "hint": "Ele teve uma visão na qual o Senhor lhe mostrou que deveria viajar sozinho ao Oriente Médio para realizar esta dedicação profética.",
    "explanation": "A oração de dedicação de Orson Hyde no Monte das Oliveiras inaugurou o recolhimento moderno dos judeus à terra de seus pais."
  },
  {
    "id": "dc_068",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual astrônomo, matemático e apóstolo pioneiro escreveu e publicou panfletos proféticos e organizou as seções de D&C em versículos em 1876?",
    "options": [
      "George Q. Cannon",
      "Lorenzo Snow",
      "Orson Pratt",
      "Parley P. Pratt"
    ],
    "correct": 2,
    "scriptureRef": "D&C 1876; História da Igreja",
    "hint": "Irmão mais novo de Parley P. Pratt, foi o primeiro pioneiro a entrar no Vale do Lago Salgado em 21 de julho de 1847.",
    "explanation": "Orson Pratt foi um dos intelectuais mais brilhantes da Restauração, dedicando sua vida a defender o evangelho."
  },
  {
    "id": "dc_069",
    "category": "dc",
    "difficulty": 3,
    "question": "O que o Senhor ensina em D&C 130:18-19 sobre o conhecimento e a inteligência que adquirirmos nesta vida terrena?",
    "options": [
      "Somente as lembranças de ordenanças permanecerão após a morte",
      "Todos ressuscitarão com exatamente o mesmo grau de conhecimento",
      "O conhecimento adquirido será substituído por uma memória nova",
      "O conhecimento e a inteligência alcançados nesta vida acompanharão a ressurreição"
    ],
    "correct": 3,
    "scriptureRef": "D&C 130:18-19",
    "hint": "Aquele que adquire mais sabedoria e luz pela sua diligência e obediência terá tanto mais progresso na eternidade.",
    "explanation": "Esta doutrina confere valor eterno e transcendente a toda busca virtuosa de conhecimento e estudo acadêmico ou espiritual."
  },
  {
    "id": "dc_070",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 132:19-20, qual é a suprema promessa reservada àqueles casados pelo novo e eterno convênio com a devida autoridade de selamento se permanecerem fiéis?",
    "options": [
      "Ministração como anjos, sem continuação da posteridade",
      "Vida no reino terrestre com autoridade sobre outros reinos",
      "Governo sobre as nações limitado ao período do Milênio",
      "Serão deuses, com continuação da posteridade e das bênçãos do convênio para sempre"
    ],
    "correct": 3,
    "scriptureRef": "D&C 132:19-20",
    "hint": "O mais alto ápice da doutrina da exaltação (teose) revelada através do Profeta Joseph Smith.",
    "explanation": "O casamento celestial permite aos casais exaltados alcançarem a vida eterna e a geração infinita de vidas espirituais."
  },
  {
    "id": "dc_071",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 88:124, qual é o prático e sábio conselho de saúde e disciplina diária que o Senhor dá aos Seus servos?",
    "options": [
      "Cessar a ociosidade, deitar cedo e levantar cedo para revigorar o corpo e a mente",
      "Alternar dias inteiros de vigília com dias inteiros de repouso",
      "Reservar as noites para trabalhar e dormir durante todo o dia",
      "Reduzir continuamente o sono para aumentar o tempo de estudo"
    ],
    "correct": 0,
    "scriptureRef": "D&C 88:124",
    "hint": "'Cessai de dormir mais do que o necessário; recolhei-vos cedo à vossa cama, para que não vos canseis; levantai-vos cedo...'.",
    "explanation": "O equilíbrio físico e espiritual do descanso adequado e da disposição matinal promove saúde e vigor intelectual."
  },
  {
    "id": "dc_072",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual apóstolo de Kirtland teve uma visão em que contemplou anjos e escreveu o memorável relato da dedicação do Templo de Kirtland em 27 de março de 1836?",
    "options": [
      "Brigham Young",
      "Heber C. Kimball",
      "Parley P. Pratt",
      "John Taylor"
    ],
    "correct": 1,
    "scriptureRef": "D&C 109; História da Igreja",
    "hint": "Ele viu o profeta Pedro em vestes resplandecentes caminhando no púlpito daquele templo sagrado.",
    "explanation": "O dia da dedicação do Templo de Kirtland foi um novo Pentecostes de manifestações espirituais e línguas celestes."
  },
  {
    "id": "dc_073",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual seção de Doutrina e Convênios contém a comovente oração dedicatória proferida por Joseph Smith no Templo de Kirtland dada por revelação direta?",
    "options": [
      "Seção 109",
      "Seção 110",
      "Seção 88",
      "Seção 124"
    ],
    "correct": 0,
    "scriptureRef": "D&C 109:1-80",
    "hint": "Ela pede que a casa seja santificada e que a glória de Deus a cubra como uma nuvem de fogo resplandecente.",
    "explanation": "D&C 109 é a oração modelo de todas as dedicações dos templos sagrados da Igreja nos tempos modernos."
  },
  {
    "id": "dc_074",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual é a cidade do Missouri onde os santos construíram assentamentos prósperos até serem expulsos pela infame 'Ordem de Extermínio' do governador Lilburn W. Boggs em outubro de 1838?",
    "options": [
      "Far West",
      "Liberty",
      "Independence",
      "St. Louis"
    ],
    "correct": 0,
    "scriptureRef": "História da Igreja, vol. 3; D&C 115",
    "hint": "O governador decretou que os mórmons deviam ser tratados como inimigos e exterminados ou expulsos do estado.",
    "explanation": "A ordem militar inconstitucional de Boggs forçou milhares de santos a fugirem no inverno para o estado vizinho de Illinois."
  },
  {
    "id": "dc_075",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual cidade de Illinois, antigamente um pântano infestado de malária chamado Commerce, foi transformada pelos santos exilados numa metrópole de arquitetura deslumbrante chamada pelo nome hebraico de 'A Bela'?",
    "options": [
      "Carthage",
      "Quincy",
      "Nauvoo",
      "Springfield"
    ],
    "correct": 2,
    "scriptureRef": "D&C 124:25-30",
    "hint": "Nas margens do grande rio Mississippi, onde foi erguido o segundo grande templo da Restauração.",
    "explanation": "Nauvoo tornou-se uma das maiores e mais prósperas cidades do Meio-Oeste americano na década de 1840."
  },
  {
    "id": "dc_076",
    "category": "dc",
    "difficulty": 3,
    "question": "O que o Senhor mandou os santos construírem em Nauvoo em D&C 124 além do sagrado templo?",
    "options": [
      "Uma nova tipografia destinada exclusivamente aos hinos",
      "A Casa de Nauvoo, hospedaria destinada a receber viajantes que visitassem a cidade",
      "Uma escola de idiomas para os futuros tradutores das escrituras",
      "Um hospital para receber apenas os missionários que retornassem"
    ],
    "correct": 1,
    "scriptureRef": "D&C 124:22-24, 60",
    "hint": "'Uma casa para que o estranho que venha de longe possa repousar... e contemple a pedra angular de Sião'.",
    "explanation": "A Casa de Nauvoo foi projetada como um centro acolhedor de hospitalidade nobre e testemunho do evangelho aos povos do mundo."
  },
  {
    "id": "dc_077",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 134, qual é a declaração oficial da Igreja a respeito de governos humanos e leis civis em geral?",
    "options": [
      "Governos devem ser substituídos pelos tribunais da Igreja",
      "Governos foram instituídos por Deus para o bem humano, com responsabilidade por seus atos",
      "A lei civil se aplica somente aos que não professam religião",
      "Os deveres civis terminam quando alguém faz convênios religiosos"
    ],
    "correct": 1,
    "scriptureRef": "D&C 134:1",
    "hint": "Estabelece a santidade da liberdade religiosa, liberdade de imprensa, propriedade privada e a sujeição à lei.",
    "explanation": "D&C 134 é a declaração de crença dos santos sobre a responsabilidade moral dos cidadãos e dos magistrados civis perante Deus."
  },
  {
    "id": "dc_078",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual instrumento de consagração e ajuda mútua feminina foi organizado pelo Profeta Joseph Smith em 17 de março de 1842 na sala superior da loja de tijolos vermelhos em Nauvoo sob o padrão do sacerdócio?",
    "options": [
      "A organização das crianças da Primária",
      "A Associação das Jovens Moças",
      "O conselho das professoras da Escola Dominical",
      "A Sociedade de Socorro das Mulheres de Nauvoo"
    ],
    "correct": 3,
    "scriptureRef": "História da Igreja, vol. 4",
    "hint": "Joseph Smith declarou: 'A Igreja nunca esteve perfeitamente organizada até que as mulheres foram assim organizadas sob o sacerdócio'.",
    "explanation": "A Sociedade de Socorro é uma das mais antigas e maiores organizações humanitárias e espirituais femininas do mundo."
  },
  {
    "id": "dc_079",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual famoso lema foi adotado pela Sociedade de Socorro em Nauvoo, inspirado nas palavras de Paulo aos Coríntios e preservado até os dias atuais?",
    "options": [
      "'A Fé Remove Montanhas'",
      "'Unidas no Serviço'",
      "'A Caridade Nunca Falha'",
      "'Em Busca da Luz'"
    ],
    "correct": 2,
    "scriptureRef": "1 Coríntios 13:8; História da Sociedade de Socorro",
    "hint": "Emma Smith serviu como sua primeira presidente, auxiliada por Sarah M. Cleveland e Elizabeth Ann Whitney.",
    "explanation": "O lema reflete o espírito ministerial de socorrer os necessitados e edificar almas no amor de Jesus Cristo."
  },
  {
    "id": "dc_080",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 126, a qual apóstolo o Senhor dispensou de suas contínuas viagens para o exterior, ordenando que permanecesse em casa cuidando de sua família?",
    "options": [
      "Wilford Woodruff",
      "Orson Hyde",
      "Heber C. Kimball",
      "Brigham Young"
    ],
    "correct": 3,
    "scriptureRef": "D&C 126:1-3",
    "hint": "'Vi os teus trabalhos e tua labuta nas viagens pelo meu nome. Eis que não mais te é exigido que deixes a tua família... pois aceitei a tua oferta'.",
    "explanation": "Brigham Young havia viajado milhares de milhas em missões; o Senhor aceitou seus sacrifícios e preparou-o para liderar os santos em Nauvoo."
  },
  {
    "id": "dc_081",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual apóstolo escreveu as obras Voz de Advertência e Chave para a Ciência da Teologia?",
    "options": [
      "Orson Pratt",
      "Parley P. Pratt",
      "John Taylor",
      "George A. Smith"
    ],
    "correct": 1,
    "scriptureRef": "D&C 32; Autobiografia de Parley P. Pratt",
    "hint": "Ele viajou ao Chile e ao Pacífico como missionário destemido e compôs muitos hinos queridos.",
    "explanation": "Parley P. Pratt foi um dos primeiros e mais eloquentes teólogos e defensores públicos da Restauração."
  },
  {
    "id": "dc_082",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual poeta e líder dos santos escreveu o amado hino 'Hoje ao Profeta Louvemos' em homenagem ao martírio de Joseph Smith, bem como o hino 'O Espírito de Deus'?",
    "options": [
      "W. W. Phelps",
      "John Taylor",
      "Eliza R. Snow",
      "Parley P. Pratt"
    ],
    "correct": 0,
    "scriptureRef": "Hinos da Igreja, nº 14; D&C 55",
    "hint": "Ele havia se arrependido e retornado à Igreja após desavenças no Missouri, recebendo uma carta de Joseph dizendo: 'Vinde, caro irmão, pois a tempestade passou... amigos outra vez'.",
    "explanation": "W. W. Phelps dedicou seus talentos literários inigualáveis para imortalizar os hinos mais sagrados da Restauração."
  },
  {
    "id": "dc_083",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual poetisa de Sião e segunda presidente geral da Sociedade de Socorro compôs o sublime hino 'Ó Meu Pai', expressando a doutrina da Mãe Celestial?",
    "options": [
      "Emmeline B. Wells",
      "Eliza R. Snow",
      "Zina D. H. Young",
      "Emma Smith"
    ],
    "correct": 1,
    "scriptureRef": "Hinos, nº 177; Ensinamentos de Joseph Smith",
    "hint": "Ela escreveu: 'No céu há somente pais? Não, a razão diz-me que não. A verdade eterna clama: Tenho lá também Mãe sã'.",
    "explanation": "Eliza R. Snow foi uma líder extraordinária e voz inspiradora da poesia sagrada dos santos pioneiros."
  },
  {
    "id": "dc_084",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 45:32, onde o Senhor declara que os Seus discípulos permanecerão e não serão abalados durante os terrores que precederão a Sua Segunda Vinda?",
    "options": [
      "Em cidades cercadas por muralhas",
      "Em acampamentos nas montanhas do norte",
      "Em regiões distantes das grandes nações",
      "Em lugares santos, onde permaneceriam sem ser movidos"
    ],
    "correct": 3,
    "scriptureRef": "D&C 45:32",
    "hint": "Os 'lugares santos' incluem os lares retificados, as estacas de Sião e os sagrados templos do Senhor.",
    "explanation": "A firmeza espiritual dos discípulos fundamenta-se em habitar em retidão nos lugares consagrados ao Pai."
  },
  {
    "id": "dc_085",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual promessa consoladora o Senhor faz em D&C 98:1-3 àqueles que sofrem perseguições injustas por amor a Seu nome?",
    "options": [
      "Todas as aflições sofridas cooperariam para o bem dos santos e a glória do Senhor",
      "Todas as perdas materiais seriam restituídas no mesmo ano",
      "Nenhum fiel voltaria a enfrentar perseguição por sua crença",
      "Os adversários desapareceriam antes de novas provações"
    ],
    "correct": 0,
    "scriptureRef": "D&C 98:1-3",
    "hint": "O Senhor ensina a paciência incondicional e o perdão até setenta vezes sete antes de pleitear justiça.",
    "explanation": "D&C 98 estabelece o elevado padrão cristão da não retaliação e da fé na providência justa de Deus."
  },
  {
    "id": "dc_086",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 129, que chaves práticas de discernimento Joseph Smith ensina para distinguir entre o ministério de um anjo ressuscitado e um espírito justificado ou um demônio disfarçado de anjo de luz?",
    "options": [
      "Pedir ao mensageiro que explique sua origem e genealogia",
      "Pedir que o mensageiro apresente um sinal de autoridade visível",
      "Pedir que o mensageiro recite uma passagem das escrituras",
      "Oferecer a mão ao mensageiro e discernir pela resposta ao pedido de um aperto"
    ],
    "correct": 3,
    "scriptureRef": "D&C 129:1-8",
    "hint": "Três grandes chaves pelas quais podeis saber se qualquer ministração procede de Deus.",
    "explanation": "D&C 129 esclarece a natureza dos seres celestiais e desmascara os ardis do adversário."
  },
  {
    "id": "dc_087",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual é a definição inspirada da palavra 'Sião' dada pelo Senhor em D&C 97:21?",
    "options": [
      "Os habitantes do condado de Jackson",
      "Aqueles que são puros de coração",
      "Os que exercem o governo da Igreja",
      "Os descendentes literais de Efraim"
    ],
    "correct": 1,
    "scriptureRef": "D&C 97:21",
    "hint": "'Portanto, regozije-se Sião, enquanto todos os iníquos lamentam; pois isto é Sião...'.",
    "explanation": "Mais do que uma localidade geográfica, Sião é um estado espiritual de pureza, unidade e consagração com Deus."
  },
  {
    "id": "dc_088",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 101:16, qual é a doce palavra de alento dada aos santos expulsos de seus lares e terras no Missouri no inverno de 1833?",
    "options": [
      "Suspendei os convênios até que termine a oposição dos homens",
      "Acalmai-vos e sabei que eu sou Deus",
      "Reuni vossas armas e reconquistai imediatamente vossas terras",
      "Deixai o Missouri e nunca mais volteis a estabelecer Sião"
    ],
    "correct": 1,
    "scriptureRef": "D&C 101:16-17",
    "hint": "'Os que permanecerem e forem puros de coração retornarão e virão às suas herdades... com cânticos de alegria eterna'.",
    "explanation": "O Senhor reafirmou Sua promessa perpétua de que Sião triunfará e que a terra da promissão será herdada no devido tempo."
  },
  {
    "id": "dc_089",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual patriarca da Igreja e pai de Joseph Smith abençoou seus filhos no leito de enfermidade e serviu como o primeiro Patriarca Presidente da Igreja restaurada?",
    "options": [
      "Asael Smith",
      "John Smith",
      "Joseph Smith Sr.",
      "Hyrum Smith"
    ],
    "correct": 2,
    "scriptureRef": "D&C 107:39-40; 124:91",
    "hint": "Um dos oito homens que manusearam as placas de ouro e testemunharam sua veracidade.",
    "explanation": "Joseph Smith Sr. ministrou centenas de bênçãos patriarcais que consolaram e guiaram os pioneiros da Restauração."
  },
  {
    "id": "dc_090",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual apóstolo é associado ao tributo a Joseph e Hyrum Smith registrado em D&C 135?",
    "options": [
      "Willard Richards",
      "W. W. Phelps",
      "Wilford Woodruff",
      "John Taylor"
    ],
    "correct": 3,
    "scriptureRef": "D&C 135",
    "hint": "Ele estava com Joseph e Hyrum em Carthage e sobreviveu aos ferimentos.",
    "explanation": "John Taylor relatou o martírio e prestou o tributo registrado em D&C 135."
  },
  {
    "id": "dc_091",
    "category": "dc",
    "difficulty": 3,
    "question": "Qual era o nome do coronel da milícia de Illinois e governador que deu sua palavra solene de honra de proteger Joseph e Hyrum em Carthage, mas quebrou a promessa e deixou a cadeia desprotegida?",
    "options": [
      "Lilburn W. Boggs",
      "Thomas Carlin",
      "Thomas Ford",
      "Daniel Dunklin"
    ],
    "correct": 2,
    "scriptureRef": "D&C 135:1, 7",
    "hint": "D&C 135:7 registra que sua promessa de honra foi quebrada quando retirou a guarda de segurança e permitiu o ataque da turba.",
    "explanation": "A cumplicidade e negligência do governador Thomas Ford possibilitou o covarde assassinato dos mártires em Carthage."
  },
  {
    "id": "dc_092",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 64:9-11, qual é a contundente ordem do Senhor sobre o perdão mútuo entre os santos?",
    "options": [
      "O perdão depende de uma reparação estabelecida por um tribunal",
      "Devemos perdoar somente os que primeiro pedem desculpas",
      "Devemos perdoar apenas as faltas cometidas sem testemunhas",
      "O Senhor perdoa a quem deseja, mas de nós exige que perdoemos a todos os homens"
    ],
    "correct": 3,
    "scriptureRef": "D&C 64:9-10",
    "hint": "'Pois aquele que não perdoa a seu irmão está em condenação perante o Senhor; porque nele permanece o maior pecado.'",
    "explanation": "O mandamento do perdão universal é uma das leis divinas mais enfáticas de Doutrina e Convênios para a harmonia de Sião."
  },
  {
    "id": "dc_093",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 82:14, o que o Senhor ordena aos santos que façam a fim de que Sião prospere e aumente em beleza e santidade?",
    "options": [
      "Concentrar todos os santos numa única cidade murada",
      "Ampliar suas fronteiras, fortalecer suas estacas e aumentar sua beleza e santidade",
      "Interromper a expansão até reunir todo o dinheiro necessário",
      "Manter suas fronteiras e transferir suas estacas para Jerusalém"
    ],
    "correct": 1,
    "scriptureRef": "D&C 82:14",
    "hint": "A metáfora da tenda de Isaías cujas estacas devem ser cravadas mais firmemente na terra para estender as cortinas.",
    "explanation": "A criação de 'Estacas de Sião' em todo o mundo estabelece refúgios espirituais de santidade e defesa para os santos."
  },
  {
    "id": "dc_094",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual profeta presidiu a Igreja durante a dedicação do Templo de Salt Lake em 1893 e manteve detalhados diários históricos registrando quase toda a história da Restauração?",
    "options": [
      "Wilford Woodruff",
      "Joseph F. Smith",
      "John Taylor",
      "Lorenzo Snow"
    ],
    "correct": 0,
    "scriptureRef": "D&C 138; História da Igreja",
    "hint": "Como missionário na Inglaterra em 1840, converteu centenas de almas na fazenda de John Benbow em Herefordshire.",
    "explanation": "Wilford Woodruff foi um dos maiores missionários e mantenedores de registros históricos de toda a dispensação."
  },
  {
    "id": "dc_095",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 124:28, que ordenança essencial foi revelada como a razão fundamental pela qual o Senhor ordenou a construção do Templo de Nauvoo?",
    "options": [
      "A bênção das crianças recém-nascidas",
      "O batismo em favor dos mortos",
      "A confirmação dos conversos vivos",
      "A ordenação dos diáconos da Igreja"
    ],
    "correct": 1,
    "scriptureRef": "D&C 124:28-30",
    "hint": "O Senhor permitiu temporariamente os batismos no rio Mississippi até que a pia batismal sobre os doze bois de madeira fosse concluída no templo.",
    "explanation": "A ordenança do batismo vicário pelos mortos é uma ordenança de templo sagrado que exige casa dedicada ao Senhor."
  },
  {
    "id": "dc_096",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 50:23-24, qual é o padrão perfeito dado pelo Senhor para discernir se qualquer ensinamento ou espírito procede verdadeiramente de Deus?",
    "options": [
      "O que vem de Deus é luz; ao recebê-la e perseverar, a pessoa recebe ainda mais luz",
      "O que vem de Deus produz sempre um sinal visível",
      "O que vem de Deus dispensa qualquer discernimento pessoal",
      "O que vem de Deus se reconhece pela eloquência do mensageiro"
    ],
    "correct": 0,
    "scriptureRef": "D&C 50:24",
    "hint": "Tudo aquilo que não edifica não é de Deus e é trevas.",
    "explanation": "A luz divina edifica, traz clareza, inteligência e paz crescente à alma que busca a Deus."
  },
  {
    "id": "dc_097",
    "category": "dc",
    "difficulty": 3,
    "question": "Em D&C 88:63, qual é a amorosa promessa de proximidade que o Senhor faz àqueles que O buscam com sinceridade?",
    "options": [
      "Esperai que eu vos procure antes de me dirigirdes a palavra",
      "Se nos achegarmos ao Senhor e o buscarmos diligentemente, Ele se achegará a nós",
      "Buscai-me somente por intermédio dos dirigentes da Igreja",
      "Encontrar-me-eis apenas depois de conhecer todos os mandamentos"
    ],
    "correct": 1,
    "scriptureRef": "D&C 88:63",
    "hint": "O convite íntimo à oração fervorosa e comunhão diária com a Divindade.",
    "explanation": "O Salvador garante que a Sua presença responde prontamente ao menor movimento do coração humano em Sua direção."
  },
  {
    "id": "dc_098",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual foi a primeira seção revelada em que o termo 'Quórum dos Doze' é expressamente mencionado com o mandato de pregar o evangelho a todo o mundo?",
    "options": [
      "Doutrina e Convênios 18",
      "Doutrina e Convênios 20",
      "Doutrina e Convênios 84",
      "Doutrina e Convênios 107"
    ],
    "correct": 0,
    "scriptureRef": "D&C 18:27",
    "hint": "Revelada em junho de 1829 aos élderes Oliver Cowdery e David Whitmer em Fayette, meses antes da organização oficial da Igreja.",
    "explanation": "D&C 18 antecipou o apostolado moderno quase seis anos antes da ordenação física dos Doze em 1835."
  },
  {
    "id": "dc_099",
    "category": "dc",
    "difficulty": 4,
    "question": "Em D&C 133 (o Apêndice do Livro de Mandamentos), qual acontecimento extraordinário é profetizado sobre o retorno das tribos perdidas do norte nos últimos dias?",
    "options": [
      "As tribos permanecerão no norte até o término do julgamento final",
      "As tribos voltarão pelo mesmo deserto percorrido por Moisés",
      "As tribos chegarão primeiro ao Egito para renovar seus convênios",
      "As rochas seriam feridas, o gelo fluiria e uma estrada surgiria no grande abismo"
    ],
    "correct": 3,
    "scriptureRef": "D&C 133:26-34",
    "hint": "Receberão suas bênçãos das mãos dos servos do Senhor, sim, os filhos de Efraim em Sião.",
    "explanation": "D&C 133 é uma grandiosa revelação apocalíptica que detalha a vinda triunfal do Messias e o retorno miraculoso das tribos dispersas de Israel."
  },
  {
    "id": "dc_100",
    "category": "dc",
    "difficulty": 4,
    "question": "Qual é a última seção canônica numerada no livro padrão de Doutrina e Convênios antes das Declarações Oficiais?",
    "options": [
      "Seção 136",
      "Seção 137",
      "Seção 135",
      "Seção 138"
    ],
    "correct": 3,
    "scriptureRef": "D&C 138",
    "hint": "Recebida em Salt Lake City em 3 de outubro de 1918 e incorporada às Obras-Padrão em 1976.",
    "explanation": "A seção 138 coroa o cânon das escrituras modernas com a gloriosa luz sobre a vitória de Cristo e a libertação dos espíritos que aguardam a redenção no mundo espiritual."
  }
]

def build():
    target = Path(__file__).resolve().with_name("data_dc.js")
    content = "/** Banco revisado: 100 perguntas; alternativas e gabaritos sincronizados. */\nvar QUESTIONS_DC = "
    content += json.dumps(questions, ensure_ascii=False, indent=2) + ";\n"
    target.write_text(content, encoding="utf-8")
    print(f"Sucesso: {target.name} gerado com {len(questions)} perguntas.")

if __name__ == "__main__":
    build()
