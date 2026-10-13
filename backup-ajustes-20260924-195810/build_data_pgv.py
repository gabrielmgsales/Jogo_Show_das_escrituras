# -*- coding: utf-8 -*-
"""
Gerador de data_pgv.js com 100 perguntas desafiadoras da Pérola de Grande Valor
"""
import json

questions = [
  # 1-35: Livro de Moisés
  {
    "id": "pgv_001", "category": "pgv", "difficulty": 1,
    "question": "Em Moisés 1:39, qual é a célebre declaração que define a obra e o propósito supremo de Deus?",
    "options": ["'Pois eis que esta é minha obra e minha glória: levar a efeito a imortalidade e vida eterna do homem'", "'Construir templos de mármore em todos os mundos'", "'Destruir os ímpios com fogo e enxofre'", "'Criar estrelas sem número para Sua vaidade'"], "correct": 0,
    "scriptureRef": "Moisés 1:39",
    "hint": "O Senhor revelou este propósito após mostrar a Moisés todas as criações da Terra e dos céus.",
    "explanation": "Moisés 1:39 é a pedra angular da teologia da salvação, revelando que a glória de Deus é exaltar e salvar Seus filhos."
  },
  {
    "id": "pgv_002", "category": "pgv", "difficulty": 2,
    "question": "O que Moisés sentiu fisicamente após a presença da glória de Deus se afastar dele em Moisés 1:9-10?",
    "options": ["Caiu por terra e por muitas horas não pôde recobrar suas forças naturais, dizendo: 'Agora sei que o homem nada é'", "Sentiu-se mais forte que um leão", "Voou pelos ares até o Egito", "Ficou com o corpo transparente como vidro"], "correct": 0,
    "scriptureRef": "Moisés 1:9-10",
    "hint": "Ele percebeu a absoluta pequenez do homem mortal perante a magnificência infinita do Criador.",
    "explanation": "Moisés esteve transfigurado na presença de Deus; ao cessar a glória, sua fraqueza mortal evidenciou a infinita distância entre o homem e a Divindade."
  },
  {
    "id": "pgv_003", "category": "pgv", "difficulty": 3,
    "question": "O que Moisés ordenou a Satanás quando este apareceu clamando com raiva: 'Moisés, filho do homem, adora-me'?",
    "options": ["'Retira-te, Satanás, não me enganes; pois Deus disse-me: Tu és à semelhança de meu Unigênito... Onde está a tua glória, para que te adore?'", "'Dá-me metade de teu reino terreno'", "'Ensina-me a sabedoria do Egito'", "'Mostra-me os segredos da terra'"], "correct": 0,
    "scriptureRef": "Moisés 1:12-16",
    "hint": "Moisés comparou a escuridão vazia de Satanás com a luz resplandecente da glória de Deus.",
    "explanation": "Moisés repeliu o adversário pelo nome de Jesus Cristo, fazendo Satanás chorar, bramir e tremer antes de fugir."
  },
  {
    "id": "pgv_004", "category": "pgv", "difficulty": 3,
    "question": "Em Moisés 4:1-4, o que Lúcifer exigiu de Deus no conselho pré-mortal em troca de sua proposta de redimir toda a humanidade destruindo o livre-arbítrio?",
    "options": ["'Dá-me, pois, a tua honra' (a própria glória e poder soberano de Deus)", "A posse das doze estrelas celestes", "Um reino isolado no norte", "Todas as pedras preciosas da criação"], "correct": 0,
    "scriptureRef": "Moisés 4:1-4",
    "hint": "Em contraste com o Salvador, que disse: 'Pai, faça-se a tua vontade e seja tua a glória para sempre'.",
    "explanation": "A rebelião de Lúcifer nasceu de seu orgulho desmedido em buscar destronar o próprio Deus e aniquilar o arbítrio moral do homem."
  },
  {
    "id": "pgv_005", "category": "pgv", "difficulty": 2,
    "question": "O que o anjo do Senhor explicou a Adão em Moisés 5:6-7 quando lhe perguntou por que oferecia sacrifícios de animais ao Senhor?",
    "options": ["'Isto é à semelhança do sacrifício do Unigênito do Pai, que é cheio de graça e verdade'", "'Porque a carne assada alimenta os anjos'", "'Para pagar o tributo do jardim'", "'Porque a terra precisa de sangue de ovelhas'"], "correct": 0,
    "scriptureRef": "Moisés 5:6-7",
    "hint": "Adão respondeu com pura fé: 'Não sei, a não ser que o Senhor me mandou'.",
    "explanation": "O anjo ensinou que os sacrifícios da lei mosaica apontavam simbolicamente para a futura redenção operada na cruz por Jesus Cristo."
  },
  {
    "id": "pgv_006", "category": "pgv", "difficulty": 3,
    "question": "Qual título diabólico Caim tomou sobre si em Moisés 5:31 ao fazer um pacto secreto com Satanás para matar seu irmão Abel e obter seu rebanho?",
    "options": ["'Mestre Maã' (o senhor deste grande segredo)", "O príncipe das trevas", "O leão do abismo", "O senhor do pó"], "correct": 0,
    "scriptureRef": "Moisés 5:31",
    "hint": "Ele se gloriou cinicamente dizendo: 'Estou livre; com certeza os rebanhos de meu irmão caem em minhas mãos'.",
    "explanation": "Caim inaugurou as combinações secretas e juramentos abomináveis da história humana motivado pela cobiça e homicídio."
  },
  {
    "id": "pgv_007", "category": "pgv", "difficulty": 2,
    "question": "Como o jovem profeta Enoque descreveu sua própria fraqueza humana quando o Senhor o chamou para pregar arrependimento ao povo em Moisés 6:31?",
    "options": ["'Sou apenas um moço e todo o povo me odeia, por ser eu lento no falar'", "'Não tenho ouro para viajar'", "'Meus pais não pertencem à linhagem'", "'Tenho medo dos animais ferozes'"], "correct": 0,
    "scriptureRef": "Moisés 6:31",
    "hint": "O Senhor respondeu: 'Abre a tua boca e ela encher-se-á, e eu te darei o que falar'.",
    "explanation": "Enoque sentia-se inadequado, mas a graça de Deus o transformou num dos maiores profetas da história universal."
  },
  {
    "id": "pgv_008", "category": "pgv", "difficulty": 3,
    "question": "O que o Senhor mandou Enoque fazer com barro e água em Moisés 6:35 para que seus olhos espirituais fossem abertos?",
    "options": ["Untar os olhos com barro e lavá-los na fonte de Siloé", "Beber água de uma taça de prata", "Olhar através de um cristal no monte", "Ungir a cabeça com azeite de oliva"], "correct": 0,
    "scriptureRef": "Moisés 6:35",
    "hint": "Ao lavar os olhos, ele contemplou os espíritos que Deus havia criado e coisas que não eram visíveis a olho nu.",
    "explanation": "Desde aquele momento, Enoque passou a ser chamado de 'vidente' pelo povo de Deus."
  },
  {
    "id": "pgv_009", "category": "pgv", "difficulty": 1,
    "question": "Em Moisés 7:18, quais são as três características sublimes que definiam o povo da Cidade de Sião liderado por Enoque?",
    "options": ["Eram de um só coração e um só pensamento; viviam em retidão; e não havia pobres entre eles", "Eles tinham os maiores palácios de pedra", "Eles falavam todas as línguas da Terra", "Eles eram guerreiros invencíveis com armaduras"], "correct": 0,
    "scriptureRef": "Moisés 7:18",
    "hint": "O padrão supremo do que o Senhor espera de Sua Igreja em todas as dispensações.",
    "explanation": "A pureza e unidade perfeita do povo de Enoque alcançou tal glória que o Senhor chamou seu povo de Sião e o transladou aos céus."
  },
  {
    "id": "pgv_010", "category": "pgv", "difficulty": 3,
    "question": "O que o profeta Enoque viu o Deus do Céu fazer em Moisés 7:28 que o deixou profundamente atônito e comovido?",
    "options": ["Viu o Deus do Céu chorar sobre a iniquidade e sofrimento das obras de Suas mãos", "Viu Deus lançar raios sobre a Terra", "Viu anjos construindo uma torre de fogo", "Viu o sol apagar-se no firmamento"], "correct": 0,
    "scriptureRef": "Moisés 7:28-33",
    "hint": "Enoque perguntou assombrado: 'Como é que os céus choram e suas lágrimas caem como a chuva sobre as montanhas?'.",
    "explanation": "Este capítulo revela o coração compassivo de Deus, que não é um ser impassível, mas um Pai amoroso que chora pelas dores de Seus filhos."
  },
  {
    "id": "pgv_011", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 7:62-64, qual glorioso encontro de dois povos é profetizado para ocorrer na Segunda Vinda de Jesus Cristo?",
    "options": ["A Sião celestial de Enoque descerá dos céus e se abraçará com a Sião terrestre restaurada na Terra", "Os romanos se encontrarão com os gregos", "As tribos do norte conquistarão o Egito", "Os reis da Pérsia visitarão Jerusalém"], "correct": 0,
    "scriptureRef": "Moisés 7:63-64",
    "hint": "'E nos lançaremos ao seu pescoço e eles ao nosso, e nos beijaremos mutuamente... e ali será a minha morada'.",
    "explanation": "Uma das mais sublimes visões escatológicas de toda a revelação, antecipando a gloriosa união dos santos de todas as eras."
  },

  # 12-45: Livro de Abraão
  {
    "id": "pgv_012", "category": "pgv", "difficulty": 1,
    "question": "Onde o patriarca Abraão habitava no início de seu registro, antes de fugir por causa da idolatria dos sacerdotes pagãos de Faraó?",
    "options": ["Em Ur dos Caldeus", "Em Mênfis no Egito", "Em Hebrom", "Em Damasco"], "correct": 0,
    "scriptureRef": "Abraão 1:1; 2:1",
    "hint": "Terra governada por governantes babilônicos/caldeus.",
    "explanation": "Abraão buscou a retidão e as bênçãos dos pais, recusando os deuses pagãos de seus progenitores em Ur."
  },
  {
    "id": "pgv_013", "category": "pgv", "difficulty": 3,
    "question": "Quais eram os nomes dos quatro deuses pagãos falsos cujos vasos e sacerdotes tentaram oferecer o jovem Abraão sobre o altar da colina de Potifar?",
    "options": ["Elquená, Libna, Mamacra e Coras", "Baal, Aserá, Dagom e Moloque", "Osíris, Ísis, Hórus e Anúbis", "Júpiter, Marte, Vênus e Apolo"], "correct": 0,
    "scriptureRef": "Abraão 1:9, 13-17; Fac-símile 1",
    "hint": "Representados nas figuras sob a cama de sacrifício no Fac-símile nº 1 do Livro de Abraão.",
    "explanation": "O Senhor enviou Seu anjo, quebrou os altares daqueles deuses estranhos e libertou Abraão com vida."
  },
  {
    "id": "pgv_014", "category": "pgv", "difficulty": 4,
    "question": "Segundo Abraão 1:21-27, por que o primeiro Faraó do Egito, embora sendo um homem reto e justo que abençoou seu povo, não tinha o direito de possuir o sacerdócio?",
    "options": ["Porque descendia da linhagem de Cam e Canaã, linhagem sobre a qual fora posta uma maldição quanto ao sacerdócio", "Porque os sacerdotes de Ur o proibiram", "Porque não sabia ler hebraico", "Porque nasceu em terra estrangeira"], "correct": 0,
    "scriptureRef": "Abraão 1:21-27",
    "hint": "Faraó procurou diligentemente imitar a ordem de sacerdócio patriarcal de Adão, mas não possuía a chave legítima de sucessão.",
    "explanation": "Abraão 1 esclarece a genealogia dos primeiros governantes do Egito preservada através da esposa de Cam, Egyptus."
  },
  {
    "id": "pgv_015", "category": "pgv", "difficulty": 2,
    "question": "Em Abraão 2:9-11, qual é a promessa universal e eterna concedida no grandioso 'Convênio Abraâmico'?",
    "options": ["Em sua semente todas as famílias da Terra serão abençoadas com as bênçãos do Evangelho, da salvação e da vida eterna", "Sua semente conquistaria o Egito pelas armas", "Eles construiriam as pirâmides de Gizé", "Teriam navios que dominariam o oceano"], "correct": 0,
    "scriptureRef": "Abraão 2:9-11",
    "hint": "Todo aquele que recebe o Evangelho é contado como semente de Abraão.",
    "explanation": "O Convênio Abraâmico é o alicerce pelo qual todo membro da Igreja torna-se participante do sacerdócio e da salvação de Cristo."
  },
  {
    "id": "pgv_016", "category": "pgv", "difficulty": 2,
    "question": "Qual é o nome da estrela que o Senhor mostrou a Abraão pelo Urim e Tumim, descrita como a maior e a mais próxima do trono de Deus?",
    "options": ["Cólobe", "Oliblis", "Kokaubeam", "Shineha"], "correct": 0,
    "scriptureRef": "Abraão 3:2-3",
    "hint": "Um dia em Cólobe equivale a mil anos na Terra, segundo o cômputo dos tempos do Senhor.",
    "explanation": "Cólobe governa todas as estrelas criadas e simboliza a preeminência suprema de Jesus Cristo sobre toda a criação."
  },
  {
    "id": "pgv_017", "category": "pgv", "difficulty": 3,
    "question": "No vocabulário astronômico revelado a Abraão no capítulo 3, o que significam as palavras 'Shineha' e 'Kokob'?",
    "options": ["Shineha é o Sol, e Kokob é uma Estrela", "Shineha é a Lua, e Kokob é a Terra", "Shineha é o Céu, e Kokob é o Mar", "Shineha é o Dia, e Kokob é a Noite"], "correct": 0,
    "scriptureRef": "Abraão 3:13",
    "hint": "E disse-me ele: Isto é Shineha, que é o sol; e disse-me: Kokob, que é estrela.",
    "explanation": "O Livro de Abraão preserva raízes semíticas e egípcias autênticas em suas designações celestes."
  },
  {
    "id": "pgv_018", "category": "pgv", "difficulty": 3,
    "question": "Em Abraão 3:22-23, o que o Senhor mostrou a Abraão antes que o mundo fosse organizado?",
    "options": ["As nobres e grandes inteligências espirituais que foram organizadas antes de o mundo existir, dizendo: 'Abraão, tu és um deles; foste escolhido antes de nasceres'", "A destruição da Babilônia", "As montanhas de ouro da América", "A queda dos impérios de Roma"], "correct": 0,
    "scriptureRef": "Abraão 3:22-23",
    "hint": "O mais claro texto das Obras-Padrão sobre a pré-ordenação e existência pré-mortal da alma humana.",
    "explanation": "Esta passagem revela que os profetas e santos foram preparados e escolhidos na presença de Deus antes de nascerem na mortalidade."
  },
  {
    "id": "pgv_019", "category": "pgv", "difficulty": 2,
    "question": "Em Abraão 3:25, qual é a definição divina do propósito da criação da Terra como um teste probatório para os filhos de Deus?",
    "options": ["'E com isso os provaremos para ver se farão todas as coisas que o Senhor seu Deus lhes ordenar'", "'Para que tenham ouro e glória carnal'", "'Para que vivam para sempre no corpo carnal'", "'Para que construam cidades sem morrer'"], "correct": 0,
    "scriptureRef": "Abraão 3:25",
    "hint": "Aquele que guardar seu primeiro estado (a vida pré-mortal) receberá um corpo; e quem guardar o segundo estado (a vida mortal) terá glória eterna.",
    "explanation": "A vida mortal é um período probatório deliberado de crescimento, provação e exercício do arbítrio moral."
  },
  {
    "id": "pgv_020", "category": "pgv", "difficulty": 3,
    "question": "Quem foram os dois que responderam no conselho dos céus quando o Senhor perguntou: 'A quem enviarei?'?",
    "options": ["O Primogênito (Jesus Cristo) respondeu: 'Eis-me aqui, envia-me a mim'; e o segundo (Lúcifer) disse com soberba: 'Eis-me aqui, envia-me a mim'", "Moisés e Elias", "Adão e Noé", "Pedro e Paulo"], "correct": 0,
    "scriptureRef": "Abraão 3:27-28",
    "hint": "E o Senhor disse: 'Enviarei o primeiro', provocando a fúria e rebelião de Lúcifer, que arrastou consigo a terça parte das hostes do céu.",
    "explanation": "A escolha voluntária de Cristo como o Redentor do mundo preservou a liberdade de escolha de todos os homens."
  },
  {
    "id": "pgv_021", "category": "pgv", "difficulty": 3,
    "question": "Em Abraão capítulos 4 e 5, como os criadores do céu e da terra são designados de maneira reverente e plural?",
    "options": ["'Os Deuses' ('E os Deuses disseram: Haja luz... E os Deuses organizaram os céus e a terra')", "'Os anjos de pedra'", "'Os espíritos da natureza'", "'O universo cego'"], "correct": 0,
    "scriptureRef": "Abraão 4:1-3; 5:1",
    "hint": "Refletindo o conselho conjunto dos Deuses sob a liderança do Pai Celestial e de Jesus Cristo.",
    "explanation": "O relato de Abraão usa o termo plural hebraico Elohim ('Os Deuses'), enfatizando a ordem executiva divina da Criação."
  },
  {
    "id": "pgv_022", "category": "pgv", "difficulty": 4,
    "question": "No Fac-símile nº 1 do Livro de Abraão, o que a Figura 1 retrata na ilustração egípcia?",
    "options": ["Abraão atado sobre o altar de sacrifício com o sacerdote idólatra de Elquená erguendo a faca sobre ele", "O enterro de Faraó numa pirâmide", "A criação dos planetas", "O casamento de Isaque"], "correct": 0,
    "scriptureRef": "Abraão Fac-símile 1, Fig. 1",
    "hint": "Com o anjo do Senhor (o pássaro) voando para protegê-lo.",
    "explanation": "A cena retrata a tentativa de martírio de Abraão e o milagroso socorro angélico que o resgatou."
  },
  {
    "id": "pgv_023", "category": "pgv", "difficulty": 4,
    "question": "No Fac-símile nº 2 de Abraão, qual figura representa a estrela Cólobe no centro do disco hipocéfalo recebendo poder de autoridade?",
    "options": ["A Figura 1 (no centro)", "A Figura 5", "A Figura 7", "A Figura 12"], "correct": 0,
    "scriptureRef": "Abraão Fac-símile 2, Fig. 1",
    "hint": "Primeira na criação, mais próxima do centro celestial.",
    "explanation": "A Figura 1 central representa Cólobe como o primeiro e maior corpo criado governando as outras ordens."
  },
  {
    "id": "pgv_024", "category": "pgv", "difficulty": 4,
    "question": "No Fac-símile nº 3 do Livro de Abraão, o que Abraão é retratado fazendo na corte real do Egito?",
    "options": ["Sentado no trono de Faraó usando uma coroa na cabeça e ensinando astronomia aos nobres egípcios", "Cozinhando trigo para os servos", "Navegando pelo rio Nilo", "Sendo coroado imperador"], "correct": 0,
    "scriptureRef": "Abraão Fac-símile 3, Fig. 1",
    "hint": "Com o príncipe de Faraó e a rainha em pé ao seu lado ouvindo suas instruções de sabedoria celeste.",
    "explanation": "A cena cumpre o encargo divino de Abraão de ensinar a ciência celestial e os caminhos de Deus na corte egípcia."
  },

  # 46-75: Joseph Smith - História e Mateus
  {
    "id": "pgv_025", "category": "pgv", "difficulty": 1,
    "question": "Em que cidade e estado dos Estados Unidos o profeta Joseph Smith nasceu em 23 de dezembro de 1805?",
    "options": ["Sharon, Condado de Windsor, estado de Vermont", "Palmyra, Nova York", "Boston, Massachusetts", "Salt Lake City, Utah"], "correct": 0,
    "scriptureRef": "JS-H 1:3",
    "hint": "A família Smith mudou-se para Palmyra quando Joseph tinha cerca de dez anos de idade.",
    "explanation": "Joseph Smith nasceu em Sharon, Vermont, filho de Joseph Smith Sr. e Lucy Mack Smith."
  },
  {
    "id": "pgv_026", "category": "pgv", "difficulty": 1,
    "question": "Quantos irmãos e irmãs Joseph Smith tinha em sua família conforme enumerados em Joseph Smith - História 1:4?",
    "options": ["Dez irmãos (totalizando onze filhos na família)", "Sete irmãos", "Três irmãos", "Doze irmãos"], "correct": 0,
    "scriptureRef": "JS-H 1:4",
    "hint": "Alvin, Hyrum, Joseph, Samuel Harrison, Ephraim, William, Don Carlos, Sophronia, Catherine e Lucy.",
    "explanation": "A família Smith era numerosa, unida, honrada e temente a Deus em suas devoções domésticas."
  },
  {
    "id": "pgv_027", "category": "pgv", "difficulty": 2,
    "question": "Qual passagem da Bíblia o jovem Joseph Smith leu em sua Bíblia em Manchester que o levou comovido a orar a Deus no Bosque Sagrado?",
    "options": ["Tiago 1:5 ('E se algum de vós tem falta de sabedoria, peça-a a Deus...')", "Mateus 7:7 ('Pedi e dar-se-vos-á')", "João 3:16 ('Porque Deus amou o mundo')", "Provérbios 3:5 ('Confia no Senhor')"], "correct": 0,
    "scriptureRef": "JS-H 1:11-12; Tiago 1:5",
    "hint": "Ele declarou que nenhum trecho de escritura jamais penetrou com mais força no coração de um homem.",
    "explanation": "Tiago 1:5 foi a fagulha inspirada pelo Espírito que inaugurou a abertura da dispensação da plenitude dos tempos."
  },
  {
    "id": "pgv_028", "category": "pgv", "difficulty": 2,
    "question": "O que aconteceu com Joseph Smith imediatamente após ele se ajoelhar e começar a orar vocalmente na floresta na primavera de 1820?",
    "options": ["Foi dominado por um poder invisível e espantoso das trevas que lhe atou a língua para que não falasse", "Ouviu cânticos de anjos imediatamente", "Caiu em sono profundo sem orar", "Um raio partiu a árvore diante dele"], "correct": 0,
    "scriptureRef": "JS-H 1:15-16",
    "hint": "Ele reuniu todas as suas forças para clamar a Deus por libertação desse inimigo real do abismo.",
    "explanation": "O adversário tentou destruir o jovem profeta na iminência da abertura dos céus, sendo derrotado pela luz celestial."
  },
  {
    "id": "pgv_029", "category": "pgv", "difficulty": 1,
    "question": "O que o Pai Celestial disse a Joseph Smith na Primeira Visão ao apontar para o segundo Personagem glorioso ao Seu lado?",
    "options": ["'ESTE É O MEU FILHO AMADO. OUVE-O!'", "'Tu serás o rei de Sião'", "'Constrói uma grande arca na floresta'", "'Escreve um livro sobre os anjos'"], "correct": 0,
    "scriptureRef": "JS-H 1:17",
    "hint": "Ele o chamou primeiro pelo seu próprio nome: 'Joseph!'.",
    "explanation": "O Pai introduziu o Salvador Jesus Cristo, que pessoalmente instruiu o jovem Joseph Smith sobre o estado do mundo."
  },
  {
    "id": "pgv_030", "category": "pgv", "difficulty": 2,
    "question": "Qual foi a resposta do Salvador quando Joseph perguntou qual de todas as seções religiosas estava certa para que ele se juntasse a ela?",
    "options": ["Que não se filiasse a nenhuma delas, pois estavam todas erradas; seus credos eram uma abominação à Sua vista e ensinavam mandamentos de homens tendo aparência de piedade", "Que escolhesse a igreja presbiteriana", "Que fundasse uma igreja batista em Manchester", "Que todas as igrejas possuíam a plenitude da verdade"], "correct": 0,
    "scriptureRef": "JS-H 1:19",
    "hint": "Eles se aproximam de mim com a boca e com os lábios me honram, mas o seu coração está longe de mim.",
    "explanation": "A resposta divina atestou a realidade da Grande Apostasia e a indispensável necessidade de restaurar o evangelho puro de Cristo."
  },
  {
    "id": "pgv_031", "category": "pgv", "difficulty": 2,
    "question": "Qual anjo apareceu no quarto de Joseph Smith na noite de 21 de setembro de 1823, anunciando a existência das placas de ouro e das pedras do Urim e Tumim?",
    "options": ["O Anjo Morôni", "O Arcanjo Miguel", "O Anjo Gabriel", "O Apóstolo Pedro"], "correct": 0,
    "scriptureRef": "JS-H 1:30-34",
    "hint": "Ele apareceu três vezes durante aquela mesma noite repetindo as mesmíssimas instruções e profecias sagradas.",
    "explanation": "Morôni declarou que Deus tinha uma obra para Joseph realizar e que seu nome seria conhecido para o bem e para o mal em todas as nações."
  },
  {
    "id": "pgv_032", "category": "pgv", "difficulty": 3,
    "question": "Quantos anos consecutivos Joseph Smith teve que comparecer anualmente no dia 22 de setembro no Monte Cumora para receber instruções do anjo antes de poder levar as placas para casa?",
    "options": ["Quatro anos consecutivos (de 1823 a 1827)", "Sete anos", "Dois anos", "Dez anos"], "correct": 0,
    "scriptureRef": "JS-H 1:53-54",
    "hint": "Ele finalmente recebeu as placas de ouro, o Urim e Tumim e o peitoral em 22 de setembro de 1827.",
    "explanation": "Durante quatro anos de tutoria angélica no monte Cumora, Joseph amadureceu espiritualmente para guardar os anais sagrados com integridade absoluta."
  },
  {
    "id": "pgv_033", "category": "pgv", "difficulty": 3,
    "question": "Qual professor erudito da Universidade de Columbia em Nova York rasgou seu próprio certificado de autenticidade dos caracteres quando Martin Harris disse que um anjo havia revelado as placas de ouro?",
    "options": ["Professor Charles Anthon", "Dr. Samuel L. Mitchill", "Dr. John Clark", "Professor George Bush"], "correct": 0,
    "scriptureRef": "JS-H 1:64-65",
    "hint": "Ele disse com arrogância: 'Não posso ler um livro selado', cumprindo textualmente a profecia de Isaías 29:11-12.",
    "explanation": "O incidente com o Professor Anthon fortaleceu imensamente o testemunho de Martin Harris e comprovou a presciência das profecias bíblicas."
  },
  {
    "id": "pgv_034", "category": "pgv", "difficulty": 2,
    "question": "Quem serviu como escriba principal e incansável de Joseph Smith durante a maior parte da tradução do Livro de Mórmon em Harmonia, de abril a junho de 1829?",
    "options": ["Oliver Cowdery", "Martin Harris", "Emma Smith", "David Whitmer"], "correct": 0,
    "scriptureRef": "JS-H 1:67-68",
    "hint": "Um jovem professor primário que fora inspirado por Deus a viajar até a casa de Joseph em Harmonia.",
    "explanation": "Oliver escreveu o texto sagrado que saía da boca do profeta dia após dia sem interrupção."
  },
  {
    "id": "pgv_035", "category": "pgv", "difficulty": 2,
    "question": "Em Joseph Smith - Mateus 1:22, o que o Salvador profetiza sobre os falsos cristos e falsos profetas dos últimos dias?",
    "options": ["'Farão tão grandes sinais e prodígios que, se fora possível, enganariam até os próprios eleitos, que são os eleitos de acordo com o convênio'", "'Eles serão fracos e ninguém os ouvirá'", "'Eles pregarão apenas em hebraico'", "'Serão destruídos em três dias'"], "correct": 0,
    "scriptureRef": "JS-M 1:22",
    "hint": "Uma advertência solene para que os santos tesourem a palavra de Deus a fim de não serem enganados pelas astúcias do mundo.",
    "explanation": "Apenas aqueles que guardam seus convênios e dão ouvidos ao Espírito Santo discernem os ardis enganadores do adversário."
  },

  # 76-100: As Regras de Fé (Artigos de Fé 1 a 13)
  {
    "id": "pgv_036", "category": "pgv", "difficulty": 1,
    "question": "A qual proeminente jornalista de Chicago Joseph Smith enviou a célebre carta de 1842 contendo a história da Igreja e as treze Regras de Fé?",
    "options": ["John Wentworth", "Horace Greeley", "James Gordon Bennett", "Thomas Sharp"], "correct": 0,
    "scriptureRef": "A Carta Wentworth (1842)",
    "hint": "Ele era editor do jornal Chicago Democrat e pedira um resumo conciso das origens e crenças dos santos dos últimos dias.",
    "explanation": "A Carta Wentworth gerou o documento imorredouro das 13 Regras de Fé e o célebre Estandarte da Verdade."
  },
  {
    "id": "pgv_037", "category": "pgv", "difficulty": 1,
    "question": "O que estabelece textualmente a Segunda Regra de Fé a respeito da responsabilidade moral de cada indivíduo perante a justiça eterna de Deus?",
    "options": ["'Cremos que os homens serão punidos por seus próprios pecados e não pela transgressão de Adão'", "'Cremos que todos herdam a culpa original de Adão'", "'Cremos que não há pecado no mundo'", "'Cremos que o pecado é punido apenas na vida mortal'"], "correct": 0,
    "scriptureRef": "Regra de Fé 2",
    "hint": "Rejeita de forma categórica o dogma tradicional do 'pecado original herdado' que condena criancinhas inocentes.",
    "explanation": "A Segunda Regra de Fé proclama a responsabilidade pessoal individual de cada filho de Deus por suas próprias escolhas morais."
  },
  {
    "id": "pgv_038", "category": "pgv", "difficulty": 1,
    "question": "Qual é a declaração sublime da Terceira Regra de Fé sobre o alcance salvador de Jesus Cristo?",
    "options": ["'Cremos que, por meio da Expiação de Cristo, toda a humanidade pode ser salva, pela obediência às leis e ordenanças do Evangelho'", "'Cremos que apenas os descendentes literais de Jacó serão salvos'", "'Cremos que a salvação não exige ordenanças'", "'Cremos que Cristo salva os homens em seus pecados'"], "correct": 0,
    "scriptureRef": "Regra de Fé 3",
    "hint": "Une a graça universal e infinita da Expiação com a exigência divina de fé ativa e obediência aos mandamentos.",
    "explanation": "A Expiação estende redenção incondicional da morte física a todos e exaltação condicional aos obedientes."
  },
  {
    "id": "pgv_039", "category": "pgv", "difficulty": 1,
    "question": "Quais são os quatro primeiros princípios e ordenanças do Evangelho enumerados com precisão na Quarta Regra de Fé?",
    "options": ["Primeiro, Fé no Senhor Jesus Cristo; segundo, Arrependimento; terceiro, Batismo por imersão para a remissão de pecados; quarto, Imposição de mãos para o dom do Espírito Santo", "Amor, Caridade, Jejum e Oração", "Dízimo, Templo, Sacerdócio e Hinos", "Leitura da Bíblia, Silêncio, Vigília e Esmola"], "correct": 0,
    "scriptureRef": "Regra de Fé 4",
    "hint": "O caminho estreito e apertado de entrada no reino de Deus delineado por Pedro no Pentecostes e por Néfi em 2 Néfi 31.",
    "explanation": "A Quarta Regra de Fé sintetiza a doutrina elementar e salvadora da porta de entrada no convênio cristão."
  },
  {
    "id": "pgv_040", "category": "pgv", "difficulty": 2,
    "question": "Segundo a Quinta Regra de Fé, como um homem deve ser chamado por Deus para pregar o Evangelho e administrar suas santas ordenanças?",
    "options": ["Por profecia e pela imposição de mãos por quem possua autoridade", "Por voto secreto da assembleia de fiéis", "Por ter concluído um curso em seminário teológico secular", "Por desejo pessoal de enriquecer a comunidade"], "correct": 0,
    "scriptureRef": "Regra de Fé 5",
    "hint": "Seguindo o padrão eterno de Hebreus 5:4: 'E ninguém toma para si esta honra, senão o que é chamado por Deus, como Arão'.",
    "explanation": "A autoridade do sacerdócio provém de revelação divina transmitida por sucessão legítima sob a imposição física de mãos."
  },
  {
    "id": "pgv_041", "category": "pgv", "difficulty": 2,
    "question": "Qual é a organização eclesiástica que a Sexta Regra de Fé declara existir na Igreja restaurada, igual àquela que existia na Igreja Primitiva do Novo Testamento?",
    "options": ["Apóstolos, profetas, pastores, mestres, evangelistas, etc.", "Cardeais, bispos e freiras", "Apenas pastores locais independentes", "Conselho de anciãos sem profetas"], "correct": 0,
    "scriptureRef": "Regra de Fé 6; Efésios 4:11",
    "hint": "Citando a mesma estrutura ministerial revelada por Paulo em Efésios 4:11 para o aperfeiçoamento dos santos.",
    "explanation": "A Igreja restaurada de Jesus Cristo possui os mesmíssimos ofícios e ministérios instituídos pelo Salvador no meridiano dos tempos."
  },
  {
    "id": "pgv_042", "category": "pgv", "difficulty": 2,
    "question": "Quais dons espirituais do Espírito Santo são afirmados na Sétima Regra de Fé?",
    "options": ["O dom de línguas, profecia, revelação, visões, cura, interpretação de línguas, etc.", "O dom de prever o futuro em cartas", "O dom de voar sobre as águas", "O dom de transformar pedras em prata"], "correct": 0,
    "scriptureRef": "Regra de Fé 7",
    "hint": "Os mesmos dons operantes nos dias dos apóstolos em 1 Coríntios 12 e em Morôni 10.",
    "explanation": "A Sétima Regra de Fé testifica que os dons sobrenaturais e espirituais acompanham os crentes em todos os séculos."
  },
  {
    "id": "pgv_043", "category": "pgv", "difficulty": 2,
    "question": "Como a Oitava Regra de Fé se expressa a respeito da Bíblia Sagrada e do Livro de Mórmon como palavras de Deus?",
    "options": ["'Cremos ser a Bíblia a palavra de Deus, desde que esteja correta a sua tradução; cremos também ser o Livro de Mórmon a palavra de Deus'", "'Cremos apenas na Bíblia'", "'Cremos que o Livro de Mórmon substitui a Bíblia'", "'Cremos que nenhum livro contém a palavra de Deus'"], "correct": 0,
    "scriptureRef": "Regra de Fé 8",
    "hint": "Reconhece o valor inestimável da Bíblia e as falhas históricas de tradução e cópias humanas ao longo dos milênios.",
    "explanation": "A Igreja apoia e reverencia a Bíblia Sagrada, ao mesmo tempo em que reconhece no Livro de Mórmon a pureza virginal de sua tradução pelo dom de Deus."
  },
  {
    "id": "pgv_044", "category": "pgv", "difficulty": 2,
    "question": "Qual princípio fundamental de teologia dinâmica e aberta é proclamado na Nona Regra de Fé?",
    "options": ["'Cremos em tudo o que Deus revelou, em tudo o que Ele revela agora e cremos que Ele ainda revelará muitas grandes e importantes coisas pertencentes ao Reino de Deus'", "'Cremos que o cânon das escrituras está eternamente fechado'", "'Cremos que Deus não fala aos homens nos tempos modernos'", "'Cremos apenas nos credos de Nicéia'"], "correct": 0,
    "scriptureRef": "Regra de Fé 9",
    "hint": "O princípio inabalável da revelação contínua que guia a Igreja por meio de profetas vivos.",
    "explanation": "Deus continua falando à humanidade, adaptando Suas instruções aos desafios e necessidades de cada geração."
  },
  {
    "id": "pgv_045", "category": "pgv", "difficulty": 3,
    "question": "Quais três grandes profecias escatológicas são proclamadas na Décima Regra de Fé?",
    "options": ["A coligação literal de Israel e a restauração das Dez Tribos; que Sião (a Nova Jerusalém) será construída no continente americano; e que Cristo reinará pessoalmente sobre a Terra renovada", "Que o mundo será destruído por cometas", "Que todos os homens viverão na Europa", "Que não haverá mais templos na Terra"], "correct": 0,
    "scriptureRef": "Regra de Fé 10",
    "hint": "A Terra receberá sua glória paradisíaca no glorioso milênio.",
    "explanation": "A Décima Regra de Fé delineia o destino milenar triunfal da Terra sob o governo pessoal de Jesus Cristo."
  },
  {
    "id": "pgv_046", "category": "pgv", "difficulty": 2,
    "question": "Em que termos nobres a Décima Primeira Regra de Fé estabelece a santidade irrestrita da liberdade religiosa e de consciência para todos os seres humanos?",
    "options": ["'Reclamamos o privilégio de adorar a Deus Todo-Poderoso de acordo com os ditames de nossa própria consciência; e concedemos a todos os homens o mesmo privilégio, permitindo-lhes adorar como, onde ou o que quiserem'", "'Apenas os santos dos últimos dias devem ter templos'", "'Todas as nações devem ser forçadas a crer na Bíblia'", "'O Estado deve ditar as orações de cada cidadão'"], "correct": 0,
    "scriptureRef": "Regra de Fé 11",
    "hint": "Um dos mais nobres manifestos de tolerância, respeito mútuo e dignidade humana já redigidos.",
    "explanation": "A Décima Primeira Regra de Fé consagra a liberdade de consciência como um direito inalienável outorgado pelo Criador."
  },
  {
    "id": "pgv_047", "category": "pgv", "difficulty": 2,
    "question": "Qual é o posicionamento de cidadania e lealdade cívica declarado na Décima Segunda Regra de Fé?",
    "options": ["'Cremos na submissão a reis, presidentes, governantes e magistrados; na obediência, honra e manutenção da lei'", "'Cremos na anarquia pacífica'", "'Cremos que as leis dos homens não devem ser obedecidas'", "'Cremos no isolamento das cidades civis'"], "correct": 0,
    "scriptureRef": "Regra de Fé 12",
    "hint": "Os membros da Igreja são incentivados a serem cidadãos exemplares, patriotas e guardiões da lei em todos os países onde vivem.",
    "explanation": "A Décima Segunda Regra de Fé estabelece a cidadania responsável, o respeito à ordem pública e a preservação do Estado de Direito."
  },
  {
    "id": "pgv_048", "category": "pgv", "difficulty": 1,
    "question": "Como se inicia o nobre padrão de vida moral e ético cristão da Décima Terceira Regra de Fé?",
    "options": ["'Cremos em ser honestos, verdadeiros, castos, benevolentes, virtuosos e em fazer o bem a todos os homens...'", "'Cremos em acumular tesouros de ouro'", "'Cremos em competir com nossos vizinhos'", "'Cremos em evitar estrangeiros'"], "correct": 0,
    "scriptureRef": "Regra de Fé 13",
    "hint": "Citando o apóstolo Paulo aos Filipenses: 'Se houver qualquer coisa virtuosa, amável, de boa fama ou louvável, nós a buscaremos'.",
    "explanation": "A Décima Terceira Regra de Fé coroa as declarações de crença dos santos com a busca incansável por tudo o que é nobre, belo e divino."
  },
  {
    "id": "pgv_049", "category": "pgv", "difficulty": 4,
    "question": "Qual célebre declaração profética, conhecida como 'O Estandarte da Verdade', foi inserida por Joseph Smith na mesma Carta Wentworth de 1842 que continha as Regras de Fé?",
    "options": ["'O Estandarte da Verdade foi erguido; nenhuma mão ímpia pode deter o progresso da obra; as perseguições podem rugir... a verdade de Deus avançará com ousadia, nobreza e independência, até penetrar em cada continente... e ecoar em cada ouvido'", "'O mundo será conquistado em dez anos'", "'A Igreja permanecerá restrita à América'", "'Os profetas descansarão sem pregar'"], "correct": 0,
    "scriptureRef": "A Carta Wentworth (1842)",
    "hint": "Até que os propósitos de Deus sejam cumpridos e o Grande Jeová diga que a obra está concluída.",
    "explanation": "O Estandarte da Verdade é uma das mais inspiradoras e audaciosas declarações de triunfo profético da história universal."
  },
  {
    "id": "pgv_050", "category": "pgv", "difficulty": 4,
    "question": "Em que ano a Pérola de Grande Valor foi compilada e publicada pela primeira vez em Liverpool, Inglaterra, pelo Élder Franklin D. Richards para os santos britânicos?",
    "options": ["1851", "1830", "1844", "1880"], "correct": 0,
    "scriptureRef": "Introdução da Pérola de Grande Valor",
    "hint": "Mais tarde, na Conferência Geral de 10 de outubro de 1880, o livro foi formalmente aceito como uma das quatro Obras-Padrão da Igreja.",
    "explanation": "Franklin D. Richards compilou os preciosos escritos de Joseph Smith para fortalecer os santos na Inglaterra, tornando-se canônico em 1880."
  },

  # 51-100: Aprofundamento Teológico e Histórico da PGV
  {
    "id": "pgv_051", "category": "pgv", "difficulty": 3,
    "question": "Em Moisés 1:4-6, o que Deus revela a Moisés sobre o Seu nome e sobre as Suas infinitas obras?",
    "options": ["'Eis que sou o Senhor Deus Todo-Poderoso e Infinito é meu nome; pois não tenho princípio de dias nem fim de anos... Mostro-te a obra de minhas mãos, mas não todas'", "'Meu nome é segredo até o fim dos tempos'", "'Eu criei apenas esta Terra e nada mais'", "'Meus anos são contados como os dos homens'"], "correct": 0,
    "scriptureRef": "Moisés 1:3-4",
    "hint": "Deus revela Sua natureza infinita e eterna a Moisés antes de mostrar-lhe as visões cósmicas.",
    "explanation": "Esta sublime passagem amplia a perspectiva humana finita para contemplar a eternidade insondável de Deus."
  },
  {
    "id": "pgv_052", "category": "pgv", "difficulty": 3,
    "question": "O que Moisés viu em Moisés 1:27-28 quando a glória do Senhor descansou sobre ele pela segunda vez após a fuga de Satanás?",
    "options": ["Viu a Terra e todos os seus habitantes, não havendo uma única alma que ele não visse pelo Espírito de Deus", "Viu apenas a terra do Egito", "Viu o templo de Salomão", "Viu as pirâmides de Gizé sendo construídas"], "correct": 0,
    "scriptureRef": "Moisés 1:27-28",
    "hint": "E ele contemplou também muitas terras; e cada terra chamava-se terra, e havia habitantes sobre sua face.",
    "explanation": "O Espírito de Deus transfigurou Moisés de modo que sua mente finita pôde contemplar a totalidade dos filhos da Terra."
  },
  {
    "id": "pgv_053", "category": "pgv", "difficulty": 4,
    "question": "O que o Senhor explicou a Moisés em Moisés 1:35 sobre os muitos outros mundos que foram criados e que já passaram?",
    "options": ["'Mas para mim todas as coisas são presentes, pois conheço a todas elas... Muitos mundos passaram pela palavra de meu poder. E muitos há que agora permanecem, e são inumeráveis para o homem'", "'Os outros mundos foram destruídos e esquecidos'", "'Apenas os anjos habitam nos outros mundos'", "'Não há vida fora do jardim do Éden'"], "correct": 0,
    "scriptureRef": "Moisés 1:35",
    "hint": "Assim como uma terra passa e seus céus, assim também outra vem.",
    "explanation": "Esta gloriosa revelação desvenda a imensidão do cosmos e a presença constante do amor e governo de Deus sobre mundos sem número."
  },
  {
    "id": "pgv_054", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 3:5, que doutrina essencial e consoladora da Criação é revelada com clareza cristalina?",
    "options": ["A Criação Espiritual: que o Senhor Deus criou todas as coisas espiritualmente antes que existissem naturalmente sobre a face da Terra", "Que todas as coisas surgiram por acaso", "Que a matéria foi criada do nada absoluto", "Que os animais não possuem espíritos"], "correct": 0,
    "scriptureRef": "Moisés 3:5",
    "hint": "'Pois eu, o Senhor Deus, criei espiritualmente todas as coisas de que falei, antes que existissem naturalmente...'.",
    "explanation": "A revelação ensina que toda planta, animal e ser humano teve uma prévia existência e organização espiritual antes de sua incorporação física."
  },
  {
    "id": "pgv_055", "category": "pgv", "difficulty": 3,
    "question": "Em Moisés 5:10-11, o que Adão e Eva exclamaram e cantaram com alegria espiritual após a Queda e ao receberem as instruções do anjo?",
    "options": ["Adão bendisse a Deus e disse: 'Por causa de minha transgressão meus olhos estão abertos e nesta vida terei alegria'; e Eva alegrou-se dizendo: 'Se não fosse por nossa transgressão, jamais teríamos tido semente, nem jamais teríamos conhecido o bem e o mal, e a alegria de nossa redenção'", "'Maldito seja o fruto que comemos'", "'Quem dera tivéssemos ficado para sempre no jardim'", "'Perdemos para sempre a presença do Pai'"], "correct": 0,
    "scriptureRef": "Moisés 5:10-11",
    "hint": "Um dos cânticos de louvor mais profundos da teologia da Restauração, demonstrando que a Queda foi um passo progressivo glorioso.",
    "explanation": "Adão e Eva compreenderam com sabedoria sublime que sem a Queda não haveria família, nem redenção, nem a vida eterna em Cristo."
  },
  {
    "id": "pgv_056", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 6:51-68, qual é o relato impressionante do primeiro batismo de Adão nas águas?",
    "options": ["Adão foi arrebatado pelo Espírito do Senhor e levado para dentro da água, foi imerso na água e tirado de dentro da água, e o Espírito Santo desceu sobre ele", "Um anjo despejou água sobre sua fronte", "Ele se lavou sozinho nas fontes de Siloé", "Moisés o batizou no Jordão"], "correct": 0,
    "scriptureRef": "Moisés 6:64-66",
    "hint": "E ouviu uma voz vinda do céu dizendo: 'Tu és batizado com fogo e com o Espírito Santo... Eis que és um em mim, um filho de Deus'.",
    "explanation": "O relato de Moisés comprova que o evangelho com todas as suas ordenanças salvadoras por imersão foi revelado desde os dias de Adão."
  },
  {
    "id": "pgv_057", "category": "pgv", "difficulty": 4,
    "question": "Qual montanha tremeu e dividiu-se diante do profeta Enoque quando este ergueu a voz e falou a palavra do Senhor em Moisés 7:13?",
    "options": ["O Monte Simeão", "O Monte Sinai", "O Monte Horebe", "O Monte Hermom"], "correct": 0,
    "scriptureRef": "Moisés 7:13",
    "hint": "E os rios desviaram-se do seu curso e o rugido dos leões ouviu-se no deserto, e todas as nações temeram grandemente.",
    "explanation": "A fé de Enoque era de tal grandeza que a própria natureza e os elementos obedeciam instantaneamente ao comando de sua voz."
  },
  {
    "id": "pgv_058", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 7:48, quem clamou em pranto dizendo: 'Ai de mim, mãe dos homens; estou aflita, estou cansada por causa da iniquidade de meus filhos! Quando descansarei e serei limpa da imundície que saiu de mim?'?",
    "options": ["A própria Terra", "A mãe Eva", "A esposa de Noé", "A cidade de Sião"], "correct": 0,
    "scriptureRef": "Moisés 7:48",
    "hint": "Enoque ouviu a própria mãe Terra gemer pelas transgressões dos homens sobre a sua face.",
    "explanation": "A Terra é uma criação viva que aspira ao seu batismo de água e fogo e ao seu descanso milenar na presença de seu Criador."
  },
  {
    "id": "pgv_059", "category": "pgv", "difficulty": 4,
    "question": "Qual patriarca antediluviano em Moisés 8:1-3 profetizou que de seus lombos brotariam todas as nações da Terra através de seu neto Noé após o dilúvio?",
    "options": ["Matusalém", "Lameque", "Jarede", "Mahalaleel"], "correct": 0,
    "scriptureRef": "Moisés 8:2-3",
    "hint": "O homem de maior longevidade física registrado nas sagradas escrituras.",
    "explanation": "O Senhor fez convênio com Matusalém de que sua posteridade seria preservada nas águas do grande dilúvio através da arca de Noé."
  },
  {
    "id": "pgv_060", "category": "pgv", "difficulty": 4,
    "question": "Em Abraão 1:18, qual promessa o Senhor faz pessoalmente a Abraão enquanto quebrava os altares pagãos da colina de Potifar?",
    "options": ["'Eis que te conduzirei pela minha mão e tomar-te-ei para pôr sobre ti o meu nome, sim, o sacerdócio de teu pai'", "'Dar-te-ei todas as coroas dos faraós'", "'Não precisarás mais viajar pelo deserto'", "'Viverás quinhentos anos na Pérsia'"], "correct": 0,
    "scriptureRef": "Abraão 1:18",
    "hint": "E meu poder estará sobre ti; como foi com Noé, assim será contigo.",
    "explanation": "O Senhor confirmou o direito de primogenitura sacerdotal sobre Abraão, tornando-o o grande patriarca dos convênios de Deus."
  },
  {
    "id": "pgv_061", "category": "pgv", "difficulty": 4,
    "question": "Qual era a palavra egípcia arcaica para o firmamento celeste que os egípcios chamavam de 'Enish-go-on-dosh', mencionada em Abraão Fac-símile nº 2?",
    "options": ["O firmamento dos céus que governa as rotações dos planetas", "O sol poente", "O Nilo transbordante", "A lua cheia"], "correct": 0,
    "scriptureRef": "Abraão Fac-símile 2, Fig. 5",
    "hint": "Diz-se também ser o sol e receber sua luz de Cólobe através do meio de Kae-e-vanrash.",
    "explanation": "A explicação do Fac-símile 2 desvenda a astronomia sagrada e os canais cósmicos de energia transmitidos pelas estrelas governantes."
  },
  {
    "id": "pgv_062", "category": "pgv", "difficulty": 4,
    "question": "Em Abraão Fac-símile nº 2, Fig. 6, o que as quatro figuras representam na astronomia do Livro de Abraão?",
    "options": ["Os quatro cantos da Terra (ou as quatro partes da Terra)", "Os quatro filhos de Noé", "Os quatro rios do Éden", "As quatro estações do ano"], "correct": 0,
    "scriptureRef": "Abraão Fac-símile 2, Fig. 6",
    "hint": "Representadas frequentemente na egiptologia pelos quatro filhos de Hórus.",
    "explanation": "Joseph Smith interpretou corretamente essas quatro figuras como simbolizando os quatro quadrantes ou cantos geográficos da Terra."
  },
  {
    "id": "pgv_063", "category": "pgv", "difficulty": 4,
    "question": "Qual é a estrela ou planeta que 'governa todas aquelas que pertencem à mesma ordem daquela em que te encontras' segundo Abraão 3:9?",
    "options": ["Cólobe", "Shineha", "Oliblis", "Kokaubeam"], "correct": 0,
    "scriptureRef": "Abraão 3:9",
    "hint": "O Senhor explicou que ela é a maior de todas as Kokaubeam que ele vira.",
    "explanation": "Cólobe é a representação física suprema do poder, majestade e luz do Salvador Jesus Cristo sobre o universo."
  },
  {
    "id": "pgv_064", "category": "pgv", "difficulty": 4,
    "question": "Em Abraão 3:18-19, como o Senhor usa a astronomia e as grandezas das estrelas como metáfora para explicar a preeminência de Deus sobre os espíritos humanos?",
    "options": ["Assim como uma estrela existe acima de outra e há estrelas mais luminosas que outras, assim também há espíritos mais inteligentes que outros; e Deus é mais inteligente que todos eles", "As estrelas são moradas dos reis", "Os homens viram estrelas na morte", "As estrelas não têm relação com as almas"], "correct": 0,
    "scriptureRef": "Abraão 3:18-19",
    "hint": "'Eu sou o Senhor teu Deus, sou mais inteligente do que todos eles'.",
    "explanation": "Esta sublime analogia cósmica demonstra a transcendência infinita da mente, luz e santidade de Deus sobre todas as criaturas."
  },
  {
    "id": "pgv_065", "category": "pgv", "difficulty": 3,
    "question": "O que o Livro de Abraão revela sobre a natureza do Espírito que desceu sobre a face das águas na Criação em Abraão 4:2?",
    "options": ["'E o Espírito dos Deuses movia-se sobre a face das águas'", "'Um vendaval violento soprava sobre a terra'", "'Uma nuvem escura tapou o sol'", "'O mar ferveu com fogo'"], "correct": 0,
    "scriptureRef": "Abraão 4:2",
    "hint": "Em perfeito alinhamento com a obra conjunta e harmoniosa dos Deuses na organização do cosmos.",
    "explanation": "A criação no Livro de Abraão retrata a obra coordenada e deliberada dos Deuses ao introduzirem a luz e a vida nos mundos."
  },
  {
    "id": "pgv_066", "category": "pgv", "difficulty": 4,
    "question": "Em Abraão 5:13, qual era a medida de tempo computada para o homem antes de sua Queda no Jardim do Éden?",
    "options": ["O tempo do Senhor, que era segundo o tempo de Cólobe; pois até então os Deuses não haviam assinalado ao homem o seu cômputo", "O cômputo da lua de 28 dias", "O calendário solar dos egípcios", "Cem anos para cada hora"], "correct": 0,
    "scriptureRef": "Abraão 5:13",
    "hint": "Explicando por que Adão viveu quase mil anos terrenos após comer do fruto antes de morrer espiritualmente e fisicamente no mesmo 'dia' do Senhor.",
    "explanation": "Esta revelação esclarece a harmonia temporal entre Gênesis e a longevidade milenar dos primeiros patriarcas."
  },
  {
    "id": "pgv_067", "category": "pgv", "difficulty": 3,
    "question": "Em Joseph Smith - História 1:28, que esclarecimento humilde e cândido o Profeta faz sobre suas imperfeições humanas na juventude entre 1820 e 1823?",
    "options": ["Confessou que caía em tolices e fraquezas da mocidade, mas que jamais cometeu qualquer pecado grave ou malicioso contra seus semelhantes", "Declarou ter sido sempre perfeito em tudo", "Afirmou que nunca cometeu nenhum erro sequer", "Disse que se isolou completamente de todas as pessoas"], "correct": 0,
    "scriptureRef": "JS-H 1:28",
    "hint": "Ele admitiu sua disposição alegre e convivência jovial, lamentando ter sido levado por vezes a leviandades.",
    "explanation": "A sincera honestidade de Joseph Smith atesta sua humanidade autêntica, desprovida de qualquer pretensão hipócrita de infalibilidade pessoal."
  },
  {
    "id": "pgv_068", "category": "pgv", "difficulty": 4,
    "question": "Qual profecia do Velho Testamento o Anjo Morôni citou a Joseph Smith em 1823 com pequenas variações significativas, afirmando que ela estava prestes a se cumprir?",
    "options": ["Malaquias capítulo 3 e capítulo 4 (sobre o retorno de Elias)", "Gênesis capítulo 1", "Provérbios capítulo 10", "Eclesiastes capítulo 12"], "correct": 0,
    "scriptureRef": "JS-H 1:36-39",
    "hint": "Ele disse: 'Eis que eu vos revelarei o Sacerdócio, pela mão de Elias, o profeta, antes que venha o grande e terrível dia do Senhor'.",
    "explanation": "A citação modificada de Malaquias ressaltou a natureza de convênio patriarcal e promessas familiares inerentes ao selamento."
  },
  {
    "id": "pgv_069", "category": "pgv", "difficulty": 4,
    "question": "Qual passagem do livro de Joel o Anjo Morôni também citou a Joseph Smith na madrugada de 21 de setembro de 1823?",
    "options": ["Joel 2:28-32 (sobre o derramamento do Espírito, sonhos dos velhos e visões dos jovens)", "Joel 1:1-5", "Joel 3:10", "Joel 1:15"], "correct": 0,
    "scriptureRef": "JS-H 1:41",
    "hint": "Morôni disse que essa profecia ainda não estava cumprida, mas que se cumpriria em breve.",
    "explanation": "A profecia de Joel sinalizava a restauração do poder profético e a abundância de revelação espiritual nos últimos dias."
  },
  {
    "id": "pgv_070", "category": "pgv", "difficulty": 3,
    "question": "O que aconteceu com Joseph Smith no dia seguinte à visita tríplice de Morôni quando tentava trabalhar na colheita com seu pai?",
    "options": ["Sentiu as forças totalmente esgotadas e caiu desfalecido por terra ao tentar pular a cerca do campo", "Trabalhou o dia todo sem cansaço", "Perdeu as ferramentas de ferro", "Fugiu para a floresta"], "correct": 0,
    "scriptureRef": "JS-H 1:48",
    "hint": "Seu pai percebeu sua palidez e mandou que fosse para casa descansar.",
    "explanation": "Enquanto jazia desfalecido junto à cerca, o Anjo Morôni apareceu pela quarta vez ordenando que contasse tudo ao seu pai."
  },
  {
    "id": "pgv_071", "category": "pgv", "difficulty": 3,
    "question": "O que o pai de Joseph Smith (Joseph Smith Sr.) disse ao filho após ouvir o relato minucioso das visões angélicas de Morôni?",
    "options": ["Disse-lhe que aquilo era de Deus e que fosse e fizesse como o mensageiro havia ordenado", "Disse que ele estava sonhando e que voltasse ao trabalho", "Proibiu-o de ir ao Monte Cumora", "Chamou os ministros locais para interrogá-lo"], "correct": 0,
    "scriptureRef": "JS-H 1:50",
    "hint": "Um testemunho comovente de fé paternal imediata na vocação profética de seu filho.",
    "explanation": "Joseph Smith Sr. reconheceu a mão divina nas visões do filho e apoiou com fidelidade incondicional a sua missão sagrada."
  },
  {
    "id": "pgv_072", "category": "pgv", "difficulty": 4,
    "question": "Onde exatamente as placas de ouro, o peitoral e as pedras do Urim e Tumim estavam guardadas no Monte Cumora quando Joseph as viu pela primeira vez?",
    "options": ["Numa caixa de pedra bem fechada sob uma grande pedra arredondada no topo da colina, apoiada sobre quatro pedras menores", "Enterradas em um baú de ferro a três metros de profundidade", "Dentro de uma caverna aberta na encosta leste", "Escondidas nos ramos ocos de um carvalho"], "correct": 0,
    "scriptureRef": "JS-H 1:51-52",
    "hint": "Joseph usou uma alavanca para erguer a pedra da tampa e contemplou os artefatos sagrados exatamente como o anjo descrevera.",
    "explanation": "A caixa de pedra havia sido preparada com cimento e pedras por Morôni séculos antes para preservar os anais até o tempo devido."
  },
  {
    "id": "pgv_073", "category": "pgv", "difficulty": 4,
    "question": "O que o Anjo Morôni advertiu solenemente a Joseph Smith que aconteceria se ele fosse descuidado ou negligente na guarda das placas após recebê-las em 1827?",
    "options": ["Que seria cortado do reino de Deus; mas que se empregasse todo o seu empenho para preservá-las até que ele viesse buscá-las, seriam protegidas", "Que teria que pagar o valor do ouro aos juízes", "Que as placas virariam pedra comum", "Que perderia sua família"], "correct": 0,
    "scriptureRef": "JS-H 1:59",
    "hint": "O anjo cumpriu sua promessa e quando a tradução foi concluída, o mensageiro recolheu as placas sob sua guarda.",
    "explanation": "Apesar de inúmeras tentativas de roubo armadas por vizinhos gananciosos, as placas foram preservadas pela providência divina."
  },
  {
    "id": "pgv_074", "category": "pgv", "difficulty": 3,
    "question": "Qual foi a primeira coisa extraordinária que aconteceu com Joseph Smith e Oliver Cowdery logo após serem batizados um pelo outro nas águas do Susquehanna em 1829?",
    "options": ["O Espírito Santo desceu grandemente sobre eles, profetizaram muitas coisas relativas à ascensão da Igreja e compreenderam as escrituras com clareza celestial", "Suas vestes secaram instantaneamente", "Uma coluna de fogo desceu sobre o rio", "Apareceu ouro nas margens"], "correct": 0,
    "scriptureRef": "JS-H 1:73-74",
    "hint": "Nossas mentes foram iluminadas e começamos a compreender as escrituras como nunca antes.",
    "explanation": "O batismo legítimo abriu imediatamente os canais de revelação profética e iluminação espiritual aos dois élderes da Restauração."
  },
  {
    "id": "pgv_075", "category": "pgv", "difficulty": 4,
    "question": "Qual das seguintes frases NÃO faz parte da Décima Terceira Regra de Fé?",
    "options": ["'Cremos que todas as igrejas serão unificadas pelos reis da terra'", "'Cremos em ser honestos, verdadeiros, castos, benevolentes, virtuosos'", "'Se houver qualquer coisa virtuosa, amável, de boa fama ou louvável, nós a buscaremos'", "'Temos suportado muitas coisas e confiamos na capacidade de tudo suportar'"], "correct": 0,
    "scriptureRef": "Regra de Fé 13",
    "hint": "A Décima Terceira Regra de Fé segue de perto o conselho de Paulo em Filipenses 4:8.",
    "explanation": "A Regra de Fé 13 é um hino à integridade pessoal, bondade universal e busca pelo que é virtuoso e nobre."
  },
  {
    "id": "pgv_076", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 2:26-27, quem Deus consulta na criação do homem dizendo: 'Façamos o homem à nossa imagem, segundo nossa semelhança'?",
    "options": ["Seu Filho Unigênito (Jesus Cristo), que esteve com Ele desde o princípio", "Os anjos ministradores", "Os espíritos dos patriarcas", "Os querubins do altar"], "correct": 0,
    "scriptureRef": "Moisés 2:26-27",
    "hint": "'E eu, Deus, disse a meu Unigênito, que esteve comigo desde o princípio...'.",
    "explanation": "Moisés 2 revela a conversa íntima e cooperativa entre o Pai Celestial e Seu Filho Amado na criação do homem."
  },
  {
    "id": "pgv_077", "category": "pgv", "difficulty": 3,
    "question": "O que Eva disse a Adão em Moisés 4:12 ao tomar do fruto da árvore do conhecimento do bem e do mal?",
    "options": ["Deu também a seu marido, e ele comeu com ela", "Escondeu o fruto sob o manto", "Levou o fruto para o rio", "Recusou-se a comer sem os anjos"], "correct": 0,
    "scriptureRef": "Moisés 4:12",
    "hint": "Eva agiu com discernimento para permitir a continuação da família humana e o progresso eterno.",
    "explanation": "O ato de Eva e a subsequente escolha de Adão de permanecer ao lado de sua esposa abriram as portas para a mortalidade e o plano de salvação."
  },
  {
    "id": "pgv_078", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 5:4, quanto tempo Adão e Eva invocaram o nome do Senhor antes de ouvirem Sua voz falando-lhes do caminho que levava ao Jardim do Éden?",
    "options": ["Por muitos dias e anos após terem sido expulsos e começado a lavrar a terra e a ter filhos", "Apenas meia hora", "Três dias", "Sete semanas"], "correct": 0,
    "scriptureRef": "Moisés 5:1-4",
    "hint": "Eles continuaram perseverando em oração e trabalho com o suor de seu rosto na terra mortal.",
    "explanation": "A perseverança de Adão e Eva na oração preparou seus corações para receberem a mensagem do anjo e a plenitude do Evangelho."
  },
  {
    "id": "pgv_079", "category": "pgv", "difficulty": 4,
    "question": "Qual bisneto de Caim em Moisés 5:43-50 fez juramento com Satanás à semelhança de Caim e assassinou dois homens por causa do segredo?",
    "options": ["Lameque", "Tubalcaim", "Irad", "Meujael"], "correct": 0,
    "scriptureRef": "Moisés 5:47-50",
    "hint": "Ele disse a suas esposas Ada e Zila: 'Ouvi a minha voz... pois matei um homem para minha ferida e um moço para meu dano'.",
    "explanation": "Lameque perpetuou os juramentos de iniquidade e assassinato de Caim entre os homens corruptos de sua época."
  },
  {
    "id": "pgv_080", "category": "pgv", "difficulty": 3,
    "question": "Em Moisés 6:5-8, o que foi mantido zelosamente entre os filhos de Deus desde o princípio no idioma adâmico puro e imaculado?",
    "options": ["Um livro de memórias, escrito sob o espírito de inspiração", "Um mapa das estrelas", "Um escudo de metal", "Um baú de ouro"], "correct": 0,
    "scriptureRef": "Moisés 6:5-8",
    "hint": "No qual se registrava a genealogia dos filhos de Deus e os ensinamentos transmitidos aos filhos com fidelidade.",
    "explanation": "O Livro de Memórias preservou a história sagrada e a pureza doutrinária patriarcal através das gerações antediluvianas."
  },
  {
    "id": "pgv_081", "category": "pgv", "difficulty": 4,
    "question": "Quantos anos Enoque viveu na Terra conduzindo o povo de Sião em retidão antes que toda a cidade fosse transladada aos céus?",
    "options": ["Trezentos e sessenta e cinco anos", "Cento e vinte anos", "Novecentos anos", "Quinhentos anos"], "correct": 0,
    "scriptureRef": "Moisés 7:68",
    "hint": "'E todos os dias de Sião, nos dias de Enoque, foram trezentos e sessenta e cinco anos'.",
    "explanation": "Durante mais de três séculos Enoque edificou a sociedade celestial de Sião até que ela foi recolhida ao seio de Deus."
  },
  {
    "id": "pgv_082", "category": "pgv", "difficulty": 4,
    "question": "Qual gigante na Terra nos dias de Enoque tentou lutar contra ele e ficou aterrorizado com o poder da voz do profeta?",
    "options": ["Mahijah (ou Maquias)", "Golias", "Og", "Anak"], "correct": 0,
    "scriptureRef": "Moisés 6:40; 7:2",
    "hint": "Ele perguntou a Enoque: 'Dize-nos abertamente quem és e de onde vens?'.",
    "explanation": "Moisés 6 relata o confronto entre os homens rebeldes da antiguidade e a autoridade celestial de Enoque."
  },
  {
    "id": "pgv_083", "category": "pgv", "difficulty": 4,
    "question": "Em Abraão 2:14-15, com que idade Abraão partiu de Harã em direção a Canaã com sua esposa Sarai e seu sobrinho Ló?",
    "options": ["Setenta e cinco anos de idade", "Cem anos", "Cinquenta anos", "Quarenta anos"], "correct": 0,
    "scriptureRef": "Abraão 2:14",
    "hint": "Ele levou consigo todas as almas que haviam conquistado em Harã.",
    "explanation": "Mesmo em idade avançada, Abraão demonstrou pronta obediência ao chamado de Deus para deixar tudo e peregrinar na terra da promissão."
  },
  {
    "id": "pgv_084", "category": "pgv", "difficulty": 4,
    "question": "Em Abraão 2:22-25, por que o Senhor instruiu Sarai a dizer no Egito que era irmã de Abraão em vez de sua esposa?",
    "options": ["Para que os egípcios não matassem Abraão por causa da beleza de sua mulher e para que sua vida fosse poupada", "Para evitar pagar tributos de casamento", "Porque era costume caldeu", "Para enganar os sacerdotes de Faraó sem razão"], "correct": 0,
    "scriptureRef": "Abraão 2:22-25",
    "hint": "Deus mesmo revelou esta cautela a Abraão perante o perigo moral da corte de Faraó.",
    "explanation": "O Senhor protegeu a integridade de Abraão e de Sarai, abençoando o patriarca e preservando a linhagem do convênio."
  },
  {
    "id": "pgv_085", "category": "pgv", "difficulty": 4,
    "question": "No Livro de Abraão 3:15, qual foi o mandamento que o Senhor deu a Abraão concernente aos conhecimentos de astronomia que acabara de contemplar?",
    "options": ["'Declara todas estas palavras no Egito, como te ordenei'", "'Esconde estes registros na caverna de Macpela'", "'Ensina apenas aos teus filhos'", "'Não escrevas em rolos de papiro'"], "correct": 0,
    "scriptureRef": "Abraão 3:15",
    "hint": "Abraão deveria usar esses conhecimentos sublimes para ensinar a realeza egípcia sobre o verdadeiro Criador.",
    "explanation": "A astronomia revelada a Abraão serviu de ponte missionária para demonstrar a soberania do Deus vivo aos idólatras do Nilo."
  },
  {
    "id": "pgv_086", "category": "pgv", "difficulty": 4,
    "question": "Qual é a ordem correta dos três Fac-símiles na Pérola de Grande Valor?",
    "options": ["Fac-símile 1: Abraão no altar; Fac-símile 2: Disco astronômico hipocéfalo de Cólobe; Fac-símile 3: Abraão no trono de Faraó ensinando astronomia", "Fac-símile 1: No trono; Fac-símile 2: No altar; Fac-símile 3: Disco hipocéfalo", "Fac-símile 1: Disco hipocéfalo; Fac-símile 2: No trono; Fac-símile 3: No altar", "Fac-símile 1: A arca de Noé; Fac-símile 2: A criação; Fac-símile 3: O templo"], "correct": 0,
    "scriptureRef": "Pérola de Grande Valor: Fac-símiles 1, 2 e 3",
    "hint": "Da libertação do sacrifício em Ur à glória astronômica de Cólobe e ao ensino perante a corte de Faraó.",
    "explanation": "Os fac-símiles retratam a progressão da jornada de fé, revelação cósmica e ministério diplomático e espiritual de Abraão."
  },
  {
    "id": "pgv_087", "category": "pgv", "difficulty": 3,
    "question": "O que Joseph Smith ensinou sobre a Primeira Regra de Fé concernente à Trindade?",
    "options": ["Que cremos em Deus o Pai Eterno, em Seu Filho Jesus Cristo e no Espírito Santo como três personagens distintos e perfeitamente unidos em amor e propósito", "Que eles são uma essência sem corpo", "Que Jesus é apenas uma ideia moral", "Que o Espírito Santo é uma força cósmica sem personalidade"], "correct": 0,
    "scriptureRef": "Regra de Fé 1; D&C 130:22",
    "hint": "Confirmando a verdade bíblica e a visão sublime do Bosque Sagrado de 1820.",
    "explanation": "A Regra de Fé 1 sintetiza a doutrina da Deidade restaurada com clareza incomparável."
  },
  {
    "id": "pgv_088", "category": "pgv", "difficulty": 4,
    "question": "Qual é a cidade que a Décima Regra de Fé profetiza que será construída no continente americano e chamada de Sião?",
    "options": ["A Nova Jerusalém", "A Grande Roma", "A Babilônia restaurada", "A cidade de Atenas"], "correct": 0,
    "scriptureRef": "Regra de Fé 10; Éter 13:3-10",
    "hint": "Em harmonia com as profecias do Livro de Mórmon em Éter e 3 Néfi.",
    "explanation": "A Nova Jerusalém será a capital sagrada e o santuário dos santos congregados nas Américas antes da volta do Senhor."
  },
  {
    "id": "pgv_089", "category": "pgv", "difficulty": 4,
    "question": "Em Joseph Smith - História 1:56, qual foi a ocupação em que Joseph Smith trabalhou em outubro de 1825 para o senhor Josiah Stowell no Condado de Susquehanna?",
    "options": ["Contratado para cavar à procura de uma antiga mina de prata espanhola perdida em Harmony", "Construindo moinhos de trigo", "Fabricando ferraduras de cavalos", "Trabalhando em tipografia"], "correct": 0,
    "scriptureRef": "JS-H 1:56",
    "hint": "Após um mês de escavações sem sucesso, Joseph convenceu o idoso senhor a desistir da empreitada.",
    "explanation": "Durante essa estadia de trabalho em Harmony, Joseph hospedou-se na casa do senhor Isaac Hale e conheceu Emma Hale, sua futura esposa."
  },
  {
    "id": "pgv_090", "category": "pgv", "difficulty": 3,
    "question": "Em que dia, mês e ano Joseph Smith e Emma Hale se casaram na cidade de South Bainbridge, Nova York?",
    "options": ["18 de janeiro de 1827", "6 de abril de 1830", "22 de setembro de 1823", "27 de junho de 1844"], "correct": 0,
    "scriptureRef": "JS-H 1:57",
    "hint": "Casaram-se na residência do juiz de paz Zachariah Tarble.",
    "explanation": "O casamento com Emma foi uma bênção vital de companheirismo e fortaleza moral meses antes de receber as placas sagradas."
  },
  {
    "id": "pgv_091", "category": "pgv", "difficulty": 4,
    "question": "Quem era o irmão mais velho de Joseph Smith que faleceu em 19 de novembro de 1823 e cuja memória era reverenciada com profunda saudade por toda a família Smith?",
    "options": ["Alvin Smith", "Hyrum Smith", "Don Carlos Smith", "Samuel H. Smith"], "correct": 0,
    "scriptureRef": "JS-H 1:4; D&C 137:5",
    "hint": "Sua morte precoce devido a uma dose errada de calomelano comoveu a todos e inspirou as revelações sobre a salvação dos mortos.",
    "explanation": "Alvin era o esteio financeiro da família e incentivou Joseph até seus últimos suspiros a cumprir o desígnio de Deus."
  },
  {
    "id": "pgv_092", "category": "pgv", "difficulty": 4,
    "question": "Qual instrumento divino de duas pedras transparentes presas em aros de prata, semelhante a óculos e atado a um peitoral, acompanhava as placas de ouro para fins de tradução?",
    "options": ["Os Intérpretes (o Urim e Tumim)", "A Liahona", "A espada de Labão", "O bastão de Moisés"], "correct": 0,
    "scriptureRef": "JS-H 1:35",
    "hint": "Morôni explicou que Deus havia preparado esses instrumentos para a tradução do livro antigo nos tempos modernos.",
    "explanation": "O Urim e Tumim capacitou o jovem profeta a traduzir os caracteres egípcios reformados pelo dom e poder de Deus."
  },
  {
    "id": "pgv_093", "category": "pgv", "difficulty": 3,
    "question": "O que o Anjo Morôni trajava quando apareceu no quarto de Joseph Smith em 1823, conforme descrito vívida e minuciosamente em JS-H 1:31?",
    "options": ["Uma túnica solta da mais extraordinária brancura, que excedia qualquer coisa terrena que ele já tivesse visto; suas mãos, braços e pés estavam nus e sua face era como um relâmpago", "Uma túnica preta com cinto de couro", "Uma armadura romana de ouro", "Um manto bordado com pedras preciosas"], "correct": 0,
    "scriptureRef": "JS-H 1:31-32",
    "hint": "Não somente a sua túnica era alva em extremo, mas toda a sua pessoa era indescritivelmente gloriosa.",
    "explanation": "A descrição de Joseph Smith reflete a pureza celestial e resplandecente dos seres ressuscitados imortais."
  },
  {
    "id": "pgv_094", "category": "pgv", "difficulty": 4,
    "question": "Em Joseph Smith - Mateus 1:37, qual é a chave indispensável dada pelo Senhor para não ser enganado nos últimos dias pelas artimanhas dos falsos mestres?",
    "options": ["'E quem entesourar a minha palavra não será enganado'", "'Quem tiver mais dinheiro'", "'Quem viver nas montanhas'", "'Quem não conversar com estrangeiros'"], "correct": 0,
    "scriptureRef": "JS-M 1:37",
    "hint": "Entesourar a palavra significa estudá-la, amá-la, guardá-la na memória e praticá-la no dia a dia.",
    "explanation": "O estudo diligente e a vivência diária das sagradas escrituras formam a bússola infalível de discernimento contra as ilusões do mundo."
  },
  {
    "id": "pgv_095", "category": "pgv", "difficulty": 4,
    "question": "Qual é a cidade do Novo Mundo que o profeta Joseph Smith viu descer do céu no milênio, em cumprimento às profecias de Enoque em Moisés 7?",
    "options": ["A Cidade de Sião de Enoque", "A antiga Babilônia", "A cidade de Atenas", "A cidade de Alexandria"], "correct": 0,
    "scriptureRef": "Moisés 7:62-64; 10ª Regra de Fé",
    "hint": "Unindo-se com a Sião terrestre estabelecida pelos santos no continente americano.",
    "explanation": "Esta grandiosa convergência celestial e terrestre coroará o triunfo final da obra de Sião na Terra."
  },
  {
    "id": "pgv_096", "category": "pgv", "difficulty": 4,
    "question": "Qual profeta presidiu a Conferência Geral de 10 de outubro de 1880 em que a Pérola de Grande Valor foi unanimemente canonizada como a quarta Obra-Padrão da Igreja?",
    "options": ["Presidente John Taylor", "Presidente Brigham Young", "Presidente Wilford Woodruff", "Presidente Joseph F. Smith"], "correct": 0,
    "scriptureRef": "História da Igreja, vol. 7",
    "hint": "Com Orson Pratt apresentando a moção ao corpo dos santos reunidos no Tabernáculo de Salt Lake.",
    "explanation": "A canonização oficial de 1880 selou o valor sagrado perpétuo da Pérola de Grande Valor para toda a Igreja."
  },
  {
    "id": "pgv_097", "category": "pgv", "difficulty": 3,
    "question": "Em Moisés 1:1, onde Moisés foi arrebatado para contemplar as visões face a face com o Criador?",
    "options": ["A um monte excessivamente alto cujo nome não é mencionado", "Ao topo do monte Sinai", "Ao cume do monte das Oliveiras", "Às margens do rio Nilo"], "correct": 0,
    "scriptureRef": "Moisés 1:1, 42",
    "hint": "O Senhor ordenou-lhe que não mostrasse estas palavras ao mundo, até que um profeta como ele fosse levantado nos últimos dias.",
    "explanation": "As palavras de Moisés 1 foram retiradas por homens iníquos e restauradas a Joseph Smith em junho de 1830 por revelação direta."
  },
  {
    "id": "pgv_098", "category": "pgv", "difficulty": 4,
    "question": "Qual era o nome do rio do Jardim do Éden mencionado em Moisés 3:11-14 que rodeava a terra de Havilá, onde havia ouro bom, bdélio e pedra de ônix?",
    "options": ["O rio Pisom", "O rio Giom", "O rio Tigre (Hídequel)", "O rio Eufrates"], "correct": 0,
    "scriptureRef": "Moisés 3:11-12",
    "hint": "O primeiro dos quatro rios que saíam para regar o jardim da criação.",
    "explanation": "Moisés 3 fornece a geografia edênica primordial antes das transformações geológicas da Terra."
  },
  {
    "id": "pgv_099", "category": "pgv", "difficulty": 4,
    "question": "Em Moisés 6:22, quem é o primeiro elo genealógico supremo a partir de quem todos os patriarcas são chamados de 'filhos de Deus'?",
    "options": ["Adão, que era o filho de Deus, com quem o próprio Deus conversou", "Noé", "Abraão", "Enoque"], "correct": 0,
    "scriptureRef": "Moisés 6:22",
    "hint": "'E esta é a genealogia dos filhos de Adão, que era o filho de Deus...'.",
    "explanation": "Esta gloriosa declaração reafirma a filiação divina literal e nobre da humanidade como gerada à imagem do Pai."
  },
  {
    "id": "pgv_100", "category": "pgv", "difficulty": 4,
    "question": "Qual é a declaração final do Profeta Joseph Smith no último parágrafo de Joseph Smith - História sobre a veracidade de seu testemunho?",
    "options": ["Que a despeito de todas as perseguições, ele sabia que tinha visto uma visão, sabia que Deus o sabia e não podia negar nem ousaria fazê-lo, sob pena de ofender a Deus e ficar sob condenação", "Que esperava ser perdoado pelos pastores", "Que suas memórias foram escritas sem certeza", "Que a Igreja pertencia apenas a seus amigos"], "correct": 0,
    "scriptureRef": "JS-H 1:24-25",
    "hint": "A sua inabalável confissão de fé e fidelidade perante toda a humanidade e perante os céus.",
    "explanation": "Joseph Smith permaneceu leal e inquebrantável ao seu testemunho da Primeira Visão até selar suas palavras com a própria vida em Carthage."
  }
]

# Salvar em data_pgv.js
with open("c:\\Jogo novo\\data_pgv.js", "w", encoding="utf-8") as f:
    f.write("/**\n * 100 Perguntas de Alto Nível - Pérola de Grande Valor\n */\n")
    f.write("const QUESTIONS_PGV = ")
    f.write(json.dumps(questions, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"Sucesso: data_pgv.js gerado com {len(questions)} perguntas da Pérola de Grande Valor!")
