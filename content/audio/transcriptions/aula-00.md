# Transcrição da Aula: aula-00.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:09]** Olá, pessoas! Boa noite! Como vão vocês? Vocês estão bem? Eu sou o Dono Sauron, para quem não me conhece, para quem está aqui pela primeira vez. Boas-vindas ao nosso curso de Fast API, Fast API 2.0, numa nova edição de 2025, então espero que vocês...

**[00:00:28]** Se sintam em casa. E antes de eu começar, eu queria saber se o som tá legal, se o vídeo tá legal. Então vocês puderem me dar um feedback só pra gente saber se tá tudo funcionando e eu não começar a falar sozinho, mirabolância, sabe? Às vezes eu tô tipo falando e ninguém tá me ouvindo. Então... Vamos lá, boas-vindas. Olha, se tá todo mundo me dando boa noite. Obrigado, Clayton. Ó, sem o amor, mano.

**[00:00:58]** Valeu aí para que me dê o feedback de que está tudo funcionando. Então vamos lá, hoje a gente começa o nosso curso de Fast API do zero edição de 2025. Beleza, esse curso que a gente está vendo aqui em live, ele é um pedaço, ele é uma parte de um todo.

**[00:01:21]** Então, é interessante a gente dizer isso, né? Tipo assim, ele não é só um conjunto de lives aqui, mas ele tem um material inteiro de texto, então eu sei que tem gente que é mais de leitura e tudo mais, então pode acessar aqui, né? O Fester BI do 0.dunosauro.com e todo o material a gente vai conversando sincronamente, construindo esse projeto juntos, mas desde tudo aqui, né?

**[00:01:46]** Tudo já está aqui, pronto, você pode vir, se começa a fazer no teu tempo, na hora que você quiser. A ideia dessa nossa parte aqui ao vivo é porque eu sei que tem gente que precisa desse compromisso de fazer junto e tudo mais, mas o material todo existe em texto e você pode acessar a qualquer momento, pode pegar para tirar dúvidas, porque eu sei que às vezes é meio chato, né, de sair procurando... procurando coisas, né, tipo...

**[00:02:15]** no meio do nada, assim, tipo, sabe? Ah, onde ele falou isso no vídeo? Aí o vídeo não tá aminutado e aí precisa, sabe, de alguma coisa muito específica, sabe? Esse esquema todo. Então, esse é uma outra coisa, não é? Faz parte desse projetão todo. O BED falou que vocês darem like, é interessante, né? Porque aí ajuda esse conteúdo a chegar em mais pessoas, né?

**[00:02:42]** Então, se for possível, por favor, deixem o like aí. Então, legal! Então, hoje a gente... hoje é um encontro, né? A gente... para quem viu, né? Aquelas coisas, a gente vai se encontrar duas vezes por semana, no período de duas horas, live, para poder trocar a ideia, para fazer alguma coisa. Mas, hoje, a ideia é explicar tudo isso. Então, sobre o curso, sobre qual o valor do curso, é de graça mesmo?

**[00:03:10]** Como isso vai ser disponibilizado? Já falei que a gente vai fazer as lives, mas as lives já foram feitas no ano passado, tem o material em texto, tem slides, tem exercícios, tem um monte de coisa, a gente vai ver tudo no detalhezinho. O que precisa para acompanhar? Às vezes você pô, estou começando a aprender Python agora e aí tipo, será que isso aqui é para você? Então tem alguns pré-requisitinhos, algumas coisas. A programação do curso, quando vão ser todos os encontros e o que a gente vai ver neles.

**[00:03:38]** e vou explicar um pouco sobre o projeto final, sobre o que a gente vai ver lá no final. Legal, então sobre o curso. Basicamente a ideia aqui, tudo que eu tenho aqui tem links porque está escrito lá no material de texto também. Mas a ideia é que a gente...

**[00:03:55]** Comece a desenvolver um projeto na prática, assim, né? Eu sou uma pessoa muito de teoria e aí a gente fica explicando e sabe, nossa, o argumento da função e tal. Então, a ideia é que a gente faça um projeto prático. É um título list, né? Um esquema de tarefas, né? Para você manusear tarefas. E essa é a ideia dele.

**[00:04:18]** E a gente vai fazer tipo um crudizão, né? Pra quem já é mais de casa, né? A gente tá num crudizão bem feito, sabe? Então a ideia é essa. Então a gente vai ver como organizar um bom pacote Python, um bom projeto Python, como lidar com isso, como fazer testes, como colocar isso na integração contínua, a gente vai falar sobre deploy, a gente vai falar sobre programação concorrente, né? Sobre programação acíncrona. Então a ideia...

**[00:04:46]** Deste curso é que a gente saia do nada, então a gente tem as ferramentas, um editor de texto e um terminal, o que é o que precisa. Temos o editor de texto e um terminal e o Python instalado, porque não é um curso básico de Python, então eu presumo que você já tem o Python instalado aí, e a gente vai sair daqui e fazer o deploy de uma aplicação no ar, tudo isso de boaça, tranquilo. A ideia é que a gente vai evoluindo, vai trocando e saber.

**[00:05:16]** passinhos juntos. Por isso que eu gosto dessa coisa sincrona live, porque a gente vai fazendo, você olha para mim e fala, caraca, isso não faz nenhum sentido. Aí a gente senta e troca a ideia e vê o que está acontecendo e vai, sabe, construindo tudo ao mesmo tempo. Adorei o comentário do Rafa aqui, que ele falou tipo assim. O editor de texto, o terminal e um sonho, que é sair do outro lado com isso pronto.

**[00:05:48]** É exatamente essa brincadeira que eu quero para a gente, então a gente tem um terminal, o editor de texto, um sonho quando vê a gente estar lá do outro lado. Então esse é o mesmo curso sobre Festa API, essa é uma coisa que eu gostaria de deixar aqui frisada, sabe, de uma forma bem radical. A ideia desse material não é um curso sobre Festa API.

**[00:06:12]** Festa API é a desculpa que eu arrumei para a gente poder conversar sobre todas as coisas, né? Então, de novo, é aquilo, a gente tem um editor de texto, um terminal e um sonho. Então, sobre o que a gente vai falar aqui? Sobre fundamentos de desenvolvimento web, a gente vai falar sobre o framework Festa API, obviamente, porque a gente quer pegar isso.

**[00:06:37]** e entender como fazer uma aplicação web, então, a gente para nos fundamentos, dá uma olhada no Fast API, a gente vai falar muito sobre o PaiDentic, que é uma forma de validar inputs e outputs de dentro dessa API que a gente vai construir aqui. O Juvicon, que é o servidor da aplicação, que é aquela hora que a gente vai olhar e falar, meu Deus, tipo...

**[00:07:04]** O que a gente quer, sabe? Como é que a gente bota isso no ar? Então, isso é o servidor que a gente usa na aplicação. A gente vai falar sobre a Skelly Alchemy, que é um tool kit inteiro de banco de dados. Então, dá para a gente criar as tabelas e tudo mais. Ele é compatível com o sistema de migrações, que é o Alembic e tudo mais. A gente vai falar sobre JWT.

**[00:07:27]** que é uma forma de assinar as coisas, sabe? Pra ter um pouco mais de segurança, pra não vazar sem a, passar sem a no request, sabe? Esse tipo de coisa. Então aqui a gente vai fazer, vai trabalhar só com permissionamento, sabe? Eu não posso excluir a conta de ninguém, só a minha. Aí a gente trabalha com autenticação, né? Aquele negócio logo, fala, ó, você é você mesmo, cara crachá, então essa é a ideia aqui.

**[00:07:53]** e aí a gente também vai falar sobre assim que aí eu e o que tá todo mundo me perguntando o link do curso é o mesmo do anterior o curso é o mesmo do anterior então a gente pode vou parar para responder isso aqui né então vamos lá

**[00:08:10]** Isso não é muito interessante para quem está vendo esse curso pela primeira vez, mas a gente fez uma edição desse curso no ano passado e, bom, muitas coisas mudaram num ecossistema do Python inteiro em um ano. Então as coisas foram atualizadas, então a aula 0, a aula 1 do curso passado não funciona mais, porque o Poetry foi atualizado, porque o Fast API foi atualizado, a aula 4 agora tem mais coisas, agora tem assim que aí eu, então tipo...

**[00:08:38]** tudo vai mudar aqui. Aí o rei se perguntou, o curso anterior se tornou obsoleto? Não, o curso anterior ainda vale, tudo lá funciona. Tirando a primeira aula que a forma de atualizar as coisas, sabe? Então é a forma de atualizar as coisas ou de instalar as coisas mudou radicalmente aqui, né? Agora o Pou Aitri suporta features do paienvi, o...

**[00:09:08]** Tem a introdução a síncrona, a gente aprofundou mais no ORM, então tem várias mudanças. O projeto é o mesmo da primeira versão, só que com coisas novas. É um revisado, corrigido e ampliado. O projeto é o mesmo, não vai mudar muita coisa a respeito disso, mas tudo evoluiu aqui.

**[00:09:33]** Então, sabe? Tipo assim, se você faz o trampo duas vezes na primeira, não sai muito legal. Na segunda, a esperança é que a gente aprenda com os erros do passado. Então, essa é a minha forma de me redimir com isso. Massa? Então, essa é a ideia aqui. Então, a gente vai conversar sobre práticas de desenvolvimento de uma maneira geral, além das ferramentas que a gente vai falar, porque não é um curso só sobre fast API. A gente vai... Saca.

**[00:10:04]** conversar sobre mais coisas então a gente vai conversar sobre ferramentas e ambiente de desenvolvimento de uma maneira geral como é que a gente gerencia o

**[00:10:17]** um projeto Python. Então, a gente precisa de um project manager que gera o build, que faz as coisas, que gera exemplos reproduzíveis para a gente poder rodar isso em outros lugares e tudo mais. Então, essa é a ideia de a gente usar o PoEtre aqui. Aí a gente vai usar o TaskPy, que já falou, no outro eu aprendi o PoEtre e o TaskPy. Então, TaskPy é uma forma de automatizar tarefas e tudo mais. Pô, tem que lembrar 50 comandos, a gente bota lá um Task...

**[00:10:44]** faz o que eu quero, saca? Então tem isso aqui, rough, que é a ideia de boas práticas de como manter o CodeStyle, o estilo de código uniforme entre todo mundo que está fazendo o projeto, ou seja, a gente delimita algumas regras e...

**[00:11:03]** faz esse esquema, a gente vai falar sobre testes, então, pie test, fixtures, cobertura de testes, a gente vai falar sobre como manipular o tempo, testes envolvendo contêiner, né? Porque a gente vai falar sobre docker lá no final, lá na frente. Então, muitas coisas aqui vão ser vistas juntas com isso, né? E aí...

**[00:11:29]** Containers, que é uma coisa super importante nos dias de hoje, né? Como é que a gente cria um container docker? Ou pode ser qualquer outra coisa, né? Pode ser Podman, pode ser com Nerd, CTL, pode... Sabe, qualquer engine de container vai funcionar, porque a ideia é que a gente entenda o conceito e sai aplicando.

**[00:11:46]** Como funciona o esquema de integração contínua, né? Que é tipo assim, pô, pega, roda os testes, vê tudo, toda vez, a todo comete, a gente sobe no repositório, vê como é que funciona. Então a gente vai conversar sobre o deploy também, então a ideia é essa, né? É um projeto feito... A gente vai começar com o editor... Como é que é que vocês falaram? A gente vai começar com o editor de texto, um terminal e um sonho.

**[00:12:09]** E a ideia é que a gente saia com tudo isso lá depois, um projeto bem gerenciado, com boas práticas, testado em containers, com práticas de integração contínua, se há e a gente vai fazer o deploy. Então a ideia é que a gente, sabe, faça o projeto todo. Saca, então a ideia é essa. Então não pense para quem...

**[00:12:32]** Tá aqui pela primeira vez que a ideia aqui é fazer um curso de framework. A ideia é que a gente consiga chegar do outro lado. Saca, a gente vai pegar as coisas e vai, sabe, maturando junto tudo o que for preciso. Saca, então, essa é a ideia aqui. E aí, te vou agradecer o super chat aqui, Thiago. Obrigado. Eu espero que sim, espero cumprir as expectativas do conteúdo de primeira aí.

**[00:12:57]** O Jason mandou aqui do, como sempre, segue fazendo fora da curva e trazendo a apresentação riquíssima em conteúdo altamente relevante, que é isso! Muito bonito! Me senti até importante agora. Pergunta, vai ter algum CLI junto com o FastAPI no curso? Como assim, algum CLI? Não sei se eu entendi a pergunta. Vai ficar gravado? Sim, sempre fica. Inclusive, as do ano passado continuam gravadas, você pode assistir, se quiser.

**[00:13:29]** Achei que ia meter um V no lugar do poetre. Mano, esse curso é mais velho. Eu estou escrevendo esse material há mais tempo do que o V existe. Então, eu não refaria tudo só por causa de uma ferramenta, sabe? Então, é isso. Rodrigo, obrigado. Tamo junto. Espero que ajude. Então, a ideia é essa aqui.

**[00:13:57]** Seguiu? Aqui ó, no fim vou poder integrar com... Não mano, é o básico bem feito. Pensa assim, a gente vai fazer um projeto simples muito foda. Com tudo que tem de melhor no mundo. Mas é um projeto simples. Então, é isso, né? A gente já falei mil vezes, mas tá aqui no slide, né? Eu sou o pai da teoria, vocês me conhecem, sabe que eu fico macetando coisas? Tipo assim. Pô, eu tenho uma série de três lives de duas horas pra explicar como funciona uma função.

**[00:14:30]** Vocês sabem que eu sou desse jeito, macetando, então a ideia aqui é ser um pouco diferente. A gente vai começar do zero, vai explicando, enquanto vai fazendo e vai construindo o projeto juntos. Do zero, conteste isso, até o deploy. É isso. Massa. E aí, como é que vai ser o projeto? Eu já falei, já dei coisinhas, mas basicamente o que a gente vai fazer é um tudo list, né?

**[00:14:59]** Tudo liste para quem não sabe é aquele tipo de coisa, tipo assim, tarefas a fazer, tarefas feitas, tarefas a fazer, tarefas feitas, tarefas que eu estou fazendo agora, sabe? Um bordzinho daquele tipo de coisa. Não tem front nesse esquema que a gente vai fazer, né? Então é só API JSON mesmo que a gente vai trafegar aqui. Então é interessante que isso fique claro aqui, né?

**[00:15:25]** Então, é o básico, é o clichê, mas é com estilo. É bonito, com estilo. Então, uma coisa que eu quero vir aqui... Pera aí, deixa eu vir para a camera aqui, que eu quero agradecer as pessoas. River, obrigado. Espero que você acompanhe. Dylan, obrigado por se tornar membro, estamos junto. E Rafa, obrigado, mano. Estamos junto. A ideia é essa.

**[00:15:58]** E aí legal, eu estou vendo que tem um monte de gente falando de UV, de não sei o que, de não sei o que lá. Mano, eu vou ser bem sincero aqui, vou tentar ser aberto porque eu não quero desperdiçar o tempo das pessoas falando dessas coisas que não estão no curso. Você pode usar o que você quiser, pode fazer o curso junto comigo em Flask. A ideia é essa, porém, contudo, entretanto, todavia, pensa que a gente está fazendo junto a parada.

**[00:16:26]** Eu e você. Se você sair do roteiro, que eu estou seguindo junto com você, eu tive que escolher umas ferramentas, o que se adequada melhor. Ah, mas eu não gosto de X. Tudo bem, não usa. Mas a ideia do que eu vou dar suporte, do que eu vou acompanhar vocês, é no conteúdo programático. Sabe, se você quiser fazer um brand do conteúdo programático e viajar por aí, fazer com Django, tá tudo bem. Ah, eu não quero usar X. Não precisa.

**[00:16:54]** mas eu vou seguir junto com vocês no conteúdo programático massa ok combinado Diego obrigado mano pelo super chat valeu mano estamos junto então a ideia é essa e aí o que que acontece aqui então beleza alguns links antes da gente

**[00:17:20]** conversar aqui, né? Então, vamos lá. O projeto final, ele deve se parecer com uma coisa que tem aqui no git, né? Isso já tá tudo pronto, porque o texto inteiro já tá pronto. Então, aqui tem o código das aulas e aí você vê aqui no treze, que é a última versão, né? É a última aula, né? Então, cada aula tem seu próprio, sua própria pastinha aqui.

**[00:17:44]** Então a ideia é que o projeto no final se pareça com isso. A gente tem o docker que roda a nossa aplicação, a gente tem muitos testes, factors, confie testes, fixtures e todo esse esquema. A gente tem isso aqui, vai ter um sistema de migrações para a gente poder fazer as coisas todas, então...

**[00:18:10]** tem tudo isso aqui, a ideia é que a gente consiga construir esse projeto junto. Aí tem Docker Compose, tem Deploy no Fly Iow, saca? Tem código pra caramba aqui, então a ideia é essa, então a gente vai sair de lá e olhar, ver, desbravar esse horizonte aqui. Massa, então é um projeto...

**[00:18:36]** Simples, mas bem honestinho, bem organizado, com todas as coisas, padrões modernos do Python, PyProject e tal, tudo mais. Então a ideia é bem por essa, bem por isso aqui. Então a gente vai fazer um deploy disso aqui, o objetivo é esse. Se o meu deploy subir aqui, eu espero que não dê o melhor chudo da vida. Exatamente isso. E no final a gente vai ter essa API aqui que retorna um olá mundo.

**[00:19:06]** é que o Olamundo ficou aqui, mas a gente tem o Swagger aqui, barra Docs, por exemplo, e aí aqui tem todos os Endpoints, a ideia é que a gente construa isso aqui junto, então tem Endpoints para usuário, Post, Gat, Put, Delete, gerenciamento de Tolkien via JWT, tem os Tudus, aí tem esse Olamundo que a gente vai criar na primeira aula.

**[00:19:30]** tem todos os esquemas aqui, a gente consegue então testar isso aqui, criar alguém por aqui, sei lá, vou criar o usuário string. Ele falou, ó, o usuário string já tem o e-mail registrado, então meio que a ideia é a gente partir por aqui. Swagger e Redock, sim, o Redock também está aqui no nosso projeto final, o Redock. Então está aqui toda a nossa especificação, da nossa aplicação, como ela foi feita, os erros e tudo mais. Então...

**[00:19:59]** a ideia é essa então a gente além de tudo vai documentar tem essa coisa essa coisa de documentar falar tipo assim nossa vai ficar super mega documentado é porque o festival já faz isso sozinho saca então a gente vai ganhar isso de brinde rua obrigado mano pelo vintão da coxinha tamo junto velho valeu demais então a ideia é essa aqui legal

**[00:20:29]** Essa é a aplicação que a gente vai construir. Se vocês quiserem acessar aqui e brincar com ela, está aqui no meu FastZeroApp.fly, porque a gente vai fazer o deploy lá no Fly.io, então a ideia é essa. E aí a gente tem o ambiente de integração contínua mesmo, que roda os testes, que faz as paradas e tudo mais. Então esse meu FastZero aqui está com algumas coisas por causa da Brinch.

**[00:21:00]** foi o que a gente colocou aqui, mas ele roda os testes, eu não estou logado aqui, mas a gente tem todo um ambiente de CI aqui pronto nesse projeto aqui, tem o workflow e tal, esse é o projeto do ano passado, mas aqui tem o pipeline, então a gente vai fazer todo o pipeline de verificação depois,

**[00:21:25]** Checkout, Estalo Python, Estalo Poetry, faz as coisas, executa os testes, roda o linter e tudo mais, tem várias outras coisas que a gente pode ir incrementando aqui dentro desse projeto enquanto a gente vai fazendo e vai trocando ideia e tudo mais, então tá tudo disponível aqui, se vocês quiserem dar uma olhada lá no Apple, tá tudo lá. Mas se eu deixa eu pegar o repositório que eu tenho mantido aqui, nossa, que demora pra voltar aqui.

**[00:21:56]** Então legal, eu acho que eu vou pegar aqui e vai ser mais rápido. Então, aqui a gente tem uns workflows mais legais, né, do que esse da última vez que a gente rodou e tal. Mas a ideia é essa, ir fazendo tudo, pegar tudo certinho, aí a gente já tá com os testes com a 5IO e tudo mais, inclusive quebrou a última vez que eu rodei. Muito massa, muito legal.

**[00:22:23]** Então, a ideia é que a gente construa esse projeto aqui. Aí, se quiser criar, clicar em todos esses links, lá no... Aqui na página do curso, tem aqui, caso você prefira ver em vídeo, é exatamente o que a gente está fazendo aqui agora, Inception. E aí, você precisar dos slides, os slides estão aqui, com todos os links, todas as coisas, se quiser baixar e tudo mais. Gostei que quebrou aqui, né?

**[00:22:53]** no f5. Nada dá certo quando a gente tá em live, né? Então tá aqui, aí você quiser ver os slides. Essa animação é muito legal, né? Eu gostei bastante de ter feito ela com o Python ainda, com o Python ainda fizemos. Então tá aqui, pode acessar todos os links, eles estão todos no material de texto se precisar. E aí, como é que vai funcionar, né? São 14 aulas no total, né? Tirando essa, que é a abertura. Então...

**[00:23:26]** A gente vai começar a brincar. Se você quiser, toda aula tem um material de texto, então é interessante que você...

**[00:23:35]** Valada, elmalide e tal. A ideia é mais do ao vivo, a gente vai fazer tudo que tem no texto, mas a ideia é que a gente vai trocando a ideia. Eu vou fazendo, vocês vão perguntando, sabe? Pensa que o valor da gente estar aqui sincronamente é a gente trocar essa ideia, né? Poder bater papo, poder fazer perguntas, responder as coisas e tudo mais. Então é esse esquema. Legal? Então aqui tem, sei lá...

**[00:24:03]** O exemplo da aula, toda aula tem o texto, então você pode vir aqui, deixa eu pegar aqui. Deu not found, porque é esse endereço aqui, agora é no estável. Então beleza, você tem o texto todo da aula, no final da aula, todas as aulas têm exercícios e tem um quiz, pra gente resolver que foi o que eu deixei aqui. Então, eu espero, né, aí é aquele negócio que eu espero que vocês façam junto comigo. Saca?

**[00:24:35]** Então, aqui no final, toda aula tem um exercício, na primeira aula o exercício é bem simples e tal, e aí tem um quiz, né? Todos os exercícios também estão resolvidos, então se precisar, tiver dúvida, quiser estar aqui também. E a gente tem um quiz que é a coisa que eu acho mais legal de todas as aulas, né? Que é poder responder os quizzes, né? Todas as aulas têm tipo umas dez perguntas pra gente pegar, tentar entender, fixar o material mesmo, né?

**[00:25:05]** Tentei fazer a coisa mais completa que a gente podia. Então tem exercícios, tem as resoluções, tem o texto da aula, tem a aula aqui para a gente trocar uma ideia, conseguir conversar e tem os quizzes para responder as perguntas e tudo mais. Acho que é uma boa forma de poder ir testando o conhecimento e fazendo as coisas. Então toda aula vai ter uma live que a gente vai conversar, tem textos, tem exercícios e tem o quiz.

**[00:25:34]** Eu acho que assim, a gente pode pegar isso aqui e se eu puder dar uma dica assim, vai dar uma olhada depois que a gente termina a aula, tenta antes da aula que vem responder as questões do quiz, fazer o exercício ou pega para fazer tudo no final de semana porque essa parte é legal para a gente pegar e fixar o conteúdo mesmo, sabe? Pô, o que que tinha uma pergunta ali e o que que saber?

**[00:26:09]** Saca, esse ponto é muito interessante. Então vale a pena dar uma olhada boa, fazer os exercícios, fazer o squeeze e tudo mais. E aí eu tenho que falar uma coisa, né? Tipo assim, beleza! Vai ter tudo isso, a gente vai falar só que o que a gente não vai falar, né?

**[00:26:31]** Eu acho que isso aqui é mais importante até do que o que a gente vai falar, que é o seguinte, a gente não vai construir um cliente, a gente vai construir o back-end que retorna, um API JSON. Saca, é isso.

**[00:26:49]** A gente não vai fazer cliente, não vai ter HTML, não vai ter interface gráfica, não vai ter cliente mobile, sabe? E todas essas coisas. A gente já falou uma coisa que é super interessante aqui, né? Que é tipo, não só isso, né? Tipo, você já vem com as dúvidas prontas, né? Tipo, por ter tentado fazer as coisas e tudo mais. A gente não vai entrar no contexto de CD, né? Embora... ou CD, né? Continuous Deploy, a gente vai parar no CI, né? Que é o Continuous Integration.

**[00:27:18]** Não é uma coisa que eu estou muito afim da gente falar sobre CD.

**[00:27:25]** A gente não vai falar sobre deploy de modelo de AI, tipo de inteligência artificial, esse tipo de coisa. O FACIPI é muito usado para isso. O Gradle, algumas outras coisas são para isso, mas a gente vai se focar em fazer a API. Depois, se você quiser falar, eu vou usar o PiDentik AI para servir os modelos. Massa, você pode fazer, mas a gente não vai conversar sobre isso. Nosso foco é na aplicação web. Massa.

**[00:27:52]** A gente não vai fazer integrações, tipo assim, ah, mas eu preciso, sabe, que foi que perguntaram, ah, mas eu vou conseguir subir a minha aplicação para fazer, vender o produto, receber uma Stripe, não, não. A gente não vai trabalhar com integrações, embora a gente poderia trabalhar com integrações dentro do Python.

**[00:28:14]** Mas a gente vai só tratar com banco de dados. É a única coisa que a gente vai ter um serviço externo que não faz parte da nossa aplicação. Obviamente a gente vai fazer um embólocro dela, envolver ela no docker, fazer algumas outras coisas, mas a única coisa que a gente vai integrar o nosso serviço é com banco de dados. Não vai ter mais nada, senão o escopo fica infinito. Saca? E é isso.

**[00:28:39]** E a gente não vai falar sobre bots. Ah, mas meu bot para automatizar a resposta se não sei o que. Não, não. Aí falar é tipo assim, tá faltando, o blockchain tá faltando essa lista. Não tem blockchain, não tem web 3, não tem nada disso aqui. Embora a gente não vá falar sobre isso, com a base do que a gente aprender aqui, com o back end e tratando a API JSON aqui.

**[00:29:05]** é totalmente possível fazer todas essas coisas depois, mas se eu não fizer um escopo, a gente nunca termina, né? Então, é melhor ter 14 aulas bem feitas do que 250 aulas que cobrem assuntos variados, né? Tomás, obrigado, mano. Tamo junto. A primeira já foi um primor. Valeu demais por essa. Pô, tamo junto. Eu queria atualizar, eu tava com essa sensação de que o texto andou muito e os vídeos ficaram pra trás, né? Assim...

**[00:29:36]** Então, legal, aí vem a outra pergunta de sempre, né? Tipo assim, esse curso é de graça, porque eu vou dar as primeiras cinco aulas e aí depois que eu der essas primeiras cinco aulas, vocês vão ter que passar o cartão de crédito para ver as próximas. Não, o curso é de graça. Todas as aulas, todo o material, tudo isso aqui foi...

**[00:30:03]** feito a partir de uma campanha de financiamento colativo que a gente fez há um tempo atrás, então todo o material aqui é de graça. E não é só de graça como ele é livre. Ou seja, todos os vídeos estão em Creative Commons, todo o material em texto está em Creative Commons, todo, tudo é Creative Commons. Obviamente, tem algumas restrições de Creative Commons que a gente tem que respeitar, né? Se vocês quiserem ver aqui no texto...

**[00:30:34]** A gente tem aqui a licença desse material aqui, então... Não, não é open source. Que maneira é open source? Não é open source, é livre. É muito mais do que open source, é livre.

**[00:30:51]** Massa, então todo o conteúdo está aqui, então ele é cc, né? Creative Commons, by ncsa. O que significa que você pode copiar esse conteúdo, reproduzir esse conteúdo, compartilhar com todo mundo, fazer o que você quiser, você pode pegar esse material, modificar, criar outro curso, fazer tudo. Está tudo permitido. Obviamente você tem que dar os créditos.

**[00:31:14]** Você não pode usar isso aqui para fins comerciais e todo o material derivado desse também tem que ser livre. É o mínimo que eu espero, né? Então é isso. Basicamente, isso é o nosso esquema. Então o curso, ele não é só de graça, como ele é livre. Massa? Porém, contudo, entretanto, todavia...

**[00:31:40]** Você pode contribuir financeiramente com esse projeto, né? É importante, né? Porque isso é o que me mantém funcionando aqui, né? É essa parte do financiamento. Então, a gente tem a campanha de financiamento da Live de Python no APOIS. A gente tem o clube de membros do YouTube, os superchats, o GitHub Sponsor. Se você quiser me pagar um café, pode me pagar um Pix. Pode me mandar um... Pode me mandar cinco a um para eu comer um pastel amanhã.

**[00:32:09]** Então, a ideia é essa. O conteúdo é tudo aberto, é tudo de graça, tá tudo em Creative Commons. Se você quiser, ó, é importante que eu vou falar agora aqui, se você quiser e poder contribua, saca? Pode me mandar uma coca, tá tudo certo, saca? A ideia é democratizar isso aqui, porque todo mundo possa acessar, mas se você puder contribuir, por favor, ajuda nós. Legal?

**[00:32:43]** E aí, como é que esse curso vai ser disponibilizado, né? As lives do ano passado já estão todas de pé, então, se você quiser, você pode assistir a edição de 2024, embora essa esteja atualizada e revisada e com mais coisas. Ele tem o material de texto, que é o grande suprasumo, né? Na minha opinião, o material de texto, ele é incrível e, quando eu digo incrível, não estou dizendo que o trabalho que eu fiz é maravilhoso, lindo, sem defeitos, mas por quê?

**[00:33:11]** Tudo lá pode ser atualizado de forma simples, sem ter que fazer um grande festival no YouTube para a gente poder fazer esse tipo de coisa. Então, lá as coisas estão sempre mais atualizadas, elas vão andando mais rápido. Então, se você puder acompanhar por lá, as coisas vão andando mais rápido. Saca, daqui a três semanas pode mudar tudo o que eu falei e eu não consigo mudar no vídeo porque eu teria que fazer o vídeo inteiro de novo. Então, o texto é bom porque ele serve de consulta,

**[00:33:38]** Tem exercícios, tem todas as coisas e referências para outros lugares. Hiperlinks lindos. Que te levam a documentações, os lugares imagináveis. Então, tem o texto, se você for a pessoa que gosta de ler, leia. As aulas sincronas de 2024 estão todas aqui, tem uma playlist no YouTube. Você pode simplesmente falar, ó, eu tô com pressa, eu quero ver a edição do ano passado. Legal. Tá tudo aqui. Pode assistir. De novo, tudo livre.

**[00:34:11]** Mas se você quiser fazer isso junto comigo, ou seja, tirar dúvidas, trocar ideia, fazer parte do grupo, ter um compromisso de vir aqui, toda semana, então a ideia é essa. E uma coisa que eu gostaria de dizer aqui, que eu acho que é muito importante, que é o seguinte, existem alguns pré-requisitos para acompanhar esse material. Porque, beleza, eu não tenho o objetivo de ensinar Python aqui. Thiago, muito obrigado, mano, pela coquinha.

**[00:34:42]** Tamo junto. Valeu demais. Então, eu não tenho o objetivo de ensinar Python nesse curso. Obviamente, a gente vai ver várias coisas de Python aqui. Mas tem algumas coisas que seriam interessantes se vocês soubessem antes. Então, algumas coisas que eu considero de trivial importância aqui. Pagando pastel.

**[00:35:11]** Obrigado, Clayton. Paga no pastel. Alguém fala pra pegar o caldo de canais, mas vocês são muito comédia, mano. Eu adoro vocês, tá ligado? Então, tipo assim, como objetivo a gente conversar sobre o web e framework web e construir uma aplicação web, essa parte eu acho que eu consigo levar, a gente segura na mão do outro vai, mas eu acho que é importante trivial caso você, sabe, caiu de paraquedas do mundo aqui.

**[00:35:40]** Como funcionam funções? Eu acho importante saber, né? Então esses são os pré-requisitos que eu considero pra gente conseguir andar junto aqui, né? Saber como funcionam as funções, né? Tipo assim, não precisa ser, tipo assim, nossa, como funcionam as funções com os danders, callables, não sei o quê, é tipo assim, mano, sabe criar uma def? Sabe usar a def, chamar a def que você fez? Massa, é isso que precisa aqui. Aí, se quiser...

**[00:36:05]** Como diz, tudo está lá no material de texto. Tem uma referência aqui. Olha como eu estava cabeludo aqui. E aí tem uma referência de como funcionam as funções aqui e tudo mais. Todos esses links estão aqui no pré-requisito. Então, se alguém quiser aqui...

**[00:36:21]** Então, aqui, quem quiser dar uma olhada, então, basicamente, o que eu gostaria era que vocês subessem funções, o básico sobre funções, como funciona a estrutura de dados, listas, dicionários, esse tipo de coisa, sabe, aquele Python mais trivial, uma pitada sobre objetos, mas não precisa ser aquele negócio, tipo assim, nossa, classes abstratas, metaprogramação, é tipo assim, sabe o que é uma classe?

**[00:36:49]** O que é um método, o que é um atributo? Nice, é isso. Tem as referências aqui, se quiser, pode lá dar uma olhada. Uma outra coisa são classes de dados, deita classes, para quem entende essa parte das pitadas aqui, são classes só de atributos, classes só de dados. Então, mas tudo tem referência, tudo tem as coisas, você fala, pô!

**[00:37:09]** Eu queria dar uma olhada de novo nessa parte, sei lá, pode ser que eu não saiba exatamente, então tudo aqui tem referências para outras lives que a gente já fez no passado, então como funciona o Data Class, olha meu cabelão verde aqui, e programação orientada a objetos, e tem algumas coisas aqui, então tudo que vocês quiserem olhar, pode dar uma olhada por aqui, tem referências para tudo. Massa, deixa eu agradecer o super chat de novo aqui, do Celso, Celso, obrigado mano, pela força.

**[00:37:39]** material fantástico, vou aproveitar o máximo. Pô, tamo junto, a coxinha com suco. Valeu, mano, tamo junto. E o Paulo mandou aqui do tá chique demais. Obrigado, mano, obrigado. Tô feliz que cês gostam, tá ligado? Eu fiz isso com muito carinho e eu tô escrevendo isso há dois anos, tá ligado? Então, pô, feliz de saber que cês tão gostando.

**[00:37:59]** Então, legal, tem outras coisas que eu considero importantes, mas não essenciais porque a gente vai dando uma olhada assim, né? Então, se você já trabalhou com algum framework de desenvolvimento web, não precisa necessariamente ser em Python. Sabe a, já mexi com Laravel no PHP, com Rails. Ah, eu já usei Flask, então...

**[00:38:19]** Pô, se você souber um pouquinho de web, um pouquinho sobre APIs, REST, APIs, JSON, pô, tá massa, tá legal. Pô, se souber um pouquinho de banco de DAAS também tá massa, sabe?

**[00:38:31]** Pô, souber um pouquinho de Git legal, souber um pouquinho de Docker legal, essas coisas são não essenciais, a gente vai meio que passar por cima delas como um rolo-compressor, né? Mas essas coisas estão no curso, tem uma aula inteira pra gente falar sobre os fundamentos da web e tudo mais, mas vocês...

**[00:38:49]** Já conhecerem esses assuntos, se quiserem procurar um pouco sobre eles, eu acho que é um bom lugar, assim, e tem muita coisa interessante. A gente vai usar essas tecnologias, mas não necessariamente faz parte do foco total do curso, né? Poderia ser um curso inteiro só de docker, ou só de git, ou só de banco de dados. Sabe o que então? A gente vai fazendo isso junto, vou acompanhar vocês, estou aqui para tirar as dúvidas, para a gente conversar da maneira que for possível, mas lembra que não é o foco, então...

**[00:39:19]** só restringindo um pouco mais o nosso escopo aqui. A gente vai usar essas coisas, pode me perguntar sobre essas coisas, está tudo liberado, mas são coisas não essenciais aqui. Estão relacionadas com o que a gente vai fazer, mas não são exatamente o nosso escopo de tudo. Então legal, vamos lá. Como é que vai funcionar isso aqui para quem caiu de paraquedas? Então aqui estão todas as datas dessa apresentação aqui, deixa eu mandar o estável, que eu acho que vai ser melhor aqui.

**[00:39:50]** Então, todos os nossos encontros e qual aula do texto a gente vai se referir em cada data. Então, a gente está aqui na abertura e apresentação do curso. No dia 1, a gente vai conversar sobre a configuração do ambiente. E aí, é sobre essa aula aqui. No outro, a gente vai falar sobre introdução ao web. Então, está aqui também.

**[00:40:17]** cada aula dessas e cada encontro que a gente vai ter em todas as terças e quintas, né, entre hoje e dia 24 do 6. Então, todas aqui estão linkadas e a gente pode conversar sobre elas depois. Ah, Katia! Ah! Um beijo pra você. Vou muito legal que a Katia tá aqui. Fiquei feliz. Bom...

**[00:40:43]** Então cada uma dessas coisas linka com aquela coisa, eles falam, mas eu esqueço mano, eu não sou bom com datas, então aqui tem aqui embaixo um agenda, algum target de tempo, tá aqui também, né? A gente vai se encontrar durante duas horas entre as oito e as dez da noite todas terças e quintas, legal?

**[00:41:10]** E se você precisar, aqui embaixo tem o esquema de iCalendar, Google Agenda. Então você fala, eu sou aquela pessoa da organização, sabe? Eu não posso perder o compromisso. Então você clica aqui, importa a agenda do curso e usa. Sabe que então as agendas estão aqui. E aí, tipo, aqui tem as explicações do que a gente precisa para acompanhar o curso, basicamente o link com o internet para você ver as lives, um computador.

**[00:41:38]** Um sistema operacional que consiga executar o Docker, algumas versões do Windows têm algum problema com isso. O Windows Home, tem alguns problemas com esse esquema. Uma conta no GitHub, então se não tiver uma conta no GitHub, é legal se criar. E uma conta no Fly.io, que é onde a gente vai fazer o deploy. Então eu já mandei o link aí, vocês podem acessar, dá uma olhada.

**[00:42:00]** E é isso. E aqui está a playlist, como só tem esse vídeo que a gente está falando agora, mas ela vai ficar aqui linkada com todos os vídeos. Uma outra coisa que tem aqui é que a gente tem um grupo no Telegram. Então, se vocês quiserem entrar lá, é um grupo do curso de Fast API. Então, se vocês quiserem entrar lá para tirar dúvidas, para a gente conversar, saca?

**[00:42:30]** Se você falou que tá com Windows Home, então testa aí, vê se você consegue instalar o Docker e tudo mais. A gente vai usar o Docker lá na aula 10, acho. 10 ou 11. É lá pra frente. E vai rolar muita coisa antes disso. Saca? Então fica tranquilo. Então entrem lá no grupo do Telegram.

**[00:42:52]** Porque no grupo do Telegram a gente vai... Vocês podem tirar dúvidas em tempo real comigo, lá no grupo. Eu me disponho pra gente trocar uma ideia, então quem não tiver lá no grupo entra, quem não tiver uma conta no Telegram. Dá uma criada, a gente conversa sobre os assuntos lá e fica fácil de tirar dúvidas e tudo mais, sabe? Então, você pode me perguntar três horas da manhã no dia que não tem aula. E aí, quem sabe eu tô acordado e não respondo?

**[00:43:21]** saca? Então tá tudo lá. Então tem os encontros sincronos, tem as agendas, se vocês precisarem sincronizar agendas, é possível e bom, algumas recomendações pra gente acompanhar isso aqui, né? Cada pessoa estuda de um jeito diferente, eu sei disso, tem gente que precisa desse compromisso, tem gente que prefere ver o...

**[00:43:45]** O vídeo, tem gente que prefere ver o vídeo depois, a hora que quiser, a um demende, sabe? Há uma coisa que eu recomendo antes da gente vir pra cá, pra aula, tipo assim, não leve isso tipo assim, não, eu estou obrigando, sabe? Tem gente que tem família, tá ligado? E tem coisa pra fazer, trampa oito horas por dia e tem família. Mas se der um tempo, sabe, no final de semana, dá uma lida no material antes pra aproveitar melhor a coisa. Saca?

**[00:44:16]** é sabe pode ajudar e eu acho que é imprescindível sabe isso aqui é uma coisa que eu vou bater sempre a tecla façam respondam os quizzes e façam os exercícios saca isso aqui é muito importante sabe é a coisa de sabe pegar e olhar e falar meu amigo parecia que eu entendi tudo aí você vai fazer ativamente você fala nossa

**[00:44:44]** falou disso aqui na aula eu nem lembro então acho que o quiz são ótimos pra isso pra fixar as coisas e posta as dúvidas lá no grupo do telegram eu vi aqui eu tô acompanhando aqui ninguém entrou no grupo ahahahah entra aí agora que você tá fazendo

**[00:45:08]** O sonho de todo professor em universidade é que os alunos leiam o texto antes da aula. Então, se possível, leiam o texto, eu sei que nem todo mundo pode, mas é imprescindível, mano, fazer os exercícios. Vai ser muito proveitoso fazer os exercícios. Entrei, pô. Eu só tô penteleando só. E aí, ao final de todas as coisas?

**[00:45:41]** A gente tem um projeto. E aí é um projeto que eu não vou fazer com vocês. Obviamente, me disponho integralmente 100% pra ajudar, tirar dúvidas do projeto, fazer code review, dar uma pentelhada, falar sobre as coisas, eu tô sempre disponível. Mas a ideia é que no final vocês façam um projeto. E... aí, esse projeto é o Madder.

**[00:46:13]** Eu adoro a linguagem que eu dei pra ele, né? Você chegou ao final. Parabéns. Então, aí a gente vai fazer o nosso TCC aqui, né? O nosso trabalho de conclusão de curso. E aí eu bolei ele num esquema que é aquele esquema de teste técnico, sabe, de empresa. Então, Enterprise Business, pra quem fala Enterprise Business, é um teste técnico.

**[00:46:38]** Para quem é do mundo mais acadêmico, é o trabalho de conclusão de curso. Serve para os dois casos. Então, a ideia é que no final vocês consigam, porque a gente vai dar insumo para tudo isso durante esses encontros, construir a sua própria aplicação. É o Madder, o meu acervo digital de romances, é um sistema de biblioteca, é uma coisa diferente, um tudo de list, mas que contém todos os componentes e elementos que a gente aprendeu aqui.

**[00:47:06]** E aí você pode dar asas, né? Ah, mas eu vou mudar o nome, eu vou fazer no seu quê, sabe? Fazer do teu jeito. Não, porque eu prefiro uma arquitetura XPTO, então, sabe? Você faz do jeito que você quiser. Não, porque eu quero usar o V. Usa aqui. No curso, vamos seguir o conteúdo programático. Massa. Então, aqui tem toda uma explicação como se fosse um teste técnico de tudo o que cada endpoint precisa fazer e tudo mais.

**[00:47:34]** Como é que você vai lidar com os erros? Saca tá tudo aqui. Como que as entidades funcionam aqui? Em caso de emergência aqui, você precisa... Nossa, como é que funciona aquele relacionamento? Você poderia estar olhando aqui. E eu deixei todos os cenários de teste que eu consegui pensar aqui, né? Então, beleza. Como é que cria uma conta? Como é que altera uma conta? Como é que deleta uma conta? Então eu fui descrevendo aqui nessa linguagem chamada Gherkin.

**[00:48:06]** todos os cenários de teste que eu pensei, caso de erro, autenticação, criação de conta, o gerenciamento dos livros, como é que vai funcionar, então tá tudo aqui, tem exemplos, saca, tudo pra você conseguir fazer. E claro que tem o grupo, se precisar de ajuda, eu tô lá o tempo inteiro. Então a ideia é essa, né? E aí aqui tem algumas coisas, né, que eu gostaria, né? Então, tipo assim...

**[00:48:33]** Python atualizado, Fast API, as que é ali a Alchemy, que são as coisas que a gente vai ver. Aí eu falei aqui ó, alguma ferramenta que suporte PyProject. Aí você pode botar o V ou o PDM ou o hatch, o que você quiser. Vai ter que usar Postgres, porque o nosso curso inteiro é em cima do Postgres. Containers, aí pode diversificar, eu não quero Docker, eu quero fazer com Kubernetes ou com Podman ou com Nerd CTL. Fica à vontade. LXC do Linux.

**[00:48:58]** É contigo. E teste usando pai teste, porque é a coisa que a gente vai começar aqui. E aqui tem uma coisa com como entregar o projeto final. Tem várias pessoas que já entregaram o projeto nas edições passadas e tudo mais. Então, se vocês quiserem ver os TCCs das outras pessoas, eles também estão listados aqui. Então, é mais uma forma de aprender. E é que muda a coisa. Aí não está aprendendo comigo. Você está vendo? Pensei em tudo aqui.

**[00:49:28]** Tudo que me foi possível, eu pensei aqui. Então, dá pra aprender olhando o código das outras pessoas, dá pra aprender com o curso, lendo o texto. Pô, tem material, é o que não falta aqui, né? Então, aí tem o TCC aqui. Legal? Então, é interessante, é o projeto final. A Idex, vocês entrem lá, faça. Vai ser bem descretivo, tem todos os detalhes, eu já expliquei.

**[00:49:57]** Faça! Vai ser legal, vai ser proveitoso, espero que vocês se divirtam fazendo isso aqui, porque tem tudo, sabe? Tem todos os recursos necessários para fazer isso. E aí, a pergunta é de sempre, né? Tem duas perguntas que a gente recebeu, que eu vim pronto para responder hoje. Vai ter certificado? Aí o Hess já mandou aí, sabe? Tipo assim, vai ter certificado? Vai!

**[00:50:28]** Porém, né, tipo assim, tudo tem o porém aqui, né? Vai ter certificado, vai, porém, é um certificado simbólico. Porque eu não sou uma entidade certificadora, né? Eu não sou uma escola, eu não sou nada, então, o certificado que eu vou dar, é simbólico. Saca, é simbólico, mas vai ter o certificado. Então você fala, ah, como é que é o certificado? Deixa eu ver a cara desse certificado. Olha aqui! Ah, vai brincando, olha o certificado dele.

**[00:51:00]** esse é o certificado da versão passada eu eu confesso que eu não gostei muito do tamanho dessa fonte aqui tal talvez eu mude um pouquinho as coisas no certificado mas tá aí certificado precisar tal nice ó então tem aqui vai valer é simbólico já tô dizendo ah dá pra usar na faculdade horas complementares se você for lá e conseguir convencer a pessoa de que

**[00:51:33]** Você fez tudo aqui comigo, talvez você consiga validar o certificado, mas não é o certificado reconhecido. Igual o certificado de evento, é simbólico. Saca, é simbólico. Guilherme, muito obrigado, mano. Tamo junto aqui, assisti, recentemente conclui o projeto, muito obrigado. Vou acompanhar esse curso do Twinis. Pô, tamo junto, velho. A ideia é essa. Que a gente faça aqui. Então, legal.

**[00:52:00]** Eu conhecimento, transmitei de avaliamento, né? Todos os certificados da IUD e missão simbólico. Sim, certificado da IUD, minha simbólica, certificado, sabe? De evento, são todos simbólicos, né? Então, esse certificado é simbólico. Talvez ele valha em algum lugar que você precise dar horas complementares, talvez não. Mas, é isso. Então, para quem conclui o projeto, até novembro. Novembro, hein? O curso acaba em julho!

**[00:52:26]** E em junho ou em julho? É no final, é no começo de julho. Então, tem o tempo para fazer, para desgastar e faça. Então, está aqui. Para não falar depois... Sabe o que é que serve? Para postar no LinkedIn depois. Falar, olha, concluir o projeto do TCC do Nossauro. Aí você posta lá e ganha os likes. É para isso que serve. Lúcia, obrigado pelo...

**[00:52:54]** Pelo sábio aqui, tamo junto. Então a ideia é essa, a ideia é essa. Tenho o certificado. Massa? Certificado pelo Dunos Project, é, certificado pelo... Meknosauro. Então, ilegal. Aí eu queria falar uma coisa aqui. E se você vier aqui, ó, precienção, agora eu quero que você olhe pra mim. Você tá... Você tá... Por aí, perdido, olha pra tela agora.

**[00:53:27]** olha para mim porque agora vou falar uma coisa importante importantíssima talvez a mais importante que eu vou falar hoje que é o seguinte o material de texto gostaria de compartilhar mas esse passo importante na minha jornada exatamente a gente posta no link de em é e me marca se fosse postar em algum lugar me marca vou ficar vou ficar feliz de ver é o seguinte o texto

**[00:54:06]** Ele é avassalador. O tempo, sabe? Ele é cruel, com bibliotecas, com cursos, com vídeos. De maneira já... Ó, ganhou uma estrelinha na entrevista, porque citei você. Ó! Tamo junto, Vitória. Espero que ajude. A ideia é essa. Reconhecido pelo Maine, Ministério do Eduardo. Maine.

**[00:54:33]** Ah, vocês são muito bobs. Então é o seguinte, ó, vamos lá. O curso aqui, em texto, ele tem uma coisa aqui que é o versionamento. Versionamento, massa. Então vocês estão vendo aqui em cima que eu estou nesse rolezinho aqui, 4.0. Aqui em cima eu venho aqui e clico nessa paradinha aqui. Então tem a versão estável, tem a versão 4.0, tem a versão que a gente é apresentando lá atrás no ano passado que é 1.0.

**[00:55:03]** Então, o Curus, ele vai andando. Todo o texto que a gente citar durante toda essa apresentação, ou seja, durante todo o ciclo de vida, ele está na versão 4. Massa? A versão estável é sempre a que eu estou desenvolvendo no final das contas. Pô, tem alguma coisinha diferente ou outra agora, né? Porque eu estou mexendo.

**[00:55:30]** Mas se as coisas mudarem no futuro e você precisar voltar no texto para achar uma coisa que foi dita nessa sessão, nessas lives que a gente está discutindo, vem aqui e troca para 4.0. É a versão aqui do momento. Legal? Então, entre a estável e a 4.0 hoje tem só uns commits que eu fiz, mas depois vou atualizar a 4.0. Então a ideia é que a gente ande na 4.0.

**[00:55:58]** Alguma coisa. Hoje saiu a 4.0.1. Talvez eu vou atualizar os slides, vou mexendo nas coisas, a gente vai para o 4.0.2. Mas a ideia é que a gente mantenha sempre dentro dessa apresentação, dentro desses encontros que a gente está tendo, a gente está conversando sobre a versão 4.0 do texto. No futuro, pode ser que o texto atualize e vá para a versão 5. Mas as coisas estão fixadas nessa versão aqui.

**[00:56:27]** Essa animação foi feita com Python? Foi feita com Python, mas ela foi feita num software chamado Glaxon Image. Pra quem tem curiosidade sobre com que foram feitas as coisas aqui, aqui tem ferramentas de apoio e aqui tem a explicação de tudo o que eu fiz com tudo aqui. Então, pra essa página...

**[00:56:50]** Tudo é feito com Flosna, Free, Libre e Open Ser Software. Então, software livres e abertos. Então, tudo que eu usei para fazer as páginas, tudo que eu usei para fazer as coisas, os slides, tudo está aqui. Então, se quiser dar uma olhada, o que que eu uso para transmitir? Como é que eu faço as thumbnails? O que que a gente usa para o repositório? Onde foi feito o deploy? Ah, qual que é o meu sistema operacional? Todas essas coisas estão no material de texto aqui. Pode olhar lá depois. Massa.

**[00:57:20]** Então, está tudo aqui. A ideia é essa. Antes de a gente finalizar, várias pessoas me perguntaram uma coisa que eu deixei para responder no final, porque não tem muito a ver com a apresentação de uma forma geral. É tipo assim, que as pessoas me perguntaram, o que é que mudou da versão passada para essa versão do curso? Basicamente, uma tonelada de coisas. Se você vier aqui, no material de texto, tem um lugar que se chama Alterações, depois do projeto final.

**[00:57:51]** e as alterações têm absolutamente tudo que mudou, é o changelog do que mudou da última apresentação até hoje. Então beleza, adicionei mais links, a playlist, tem um legal ó, o que que saiu na 4.1, atualização da biblioteca, versionamento das páginas, o que que foi alterado, nota de docker?

**[00:58:14]** Quais bibliotecas foram autorizadas? Então tá tudo aqui. O que mudou internamente? Quais os slides que foram atualizados? Na versão 4.0. Na versão 3.0. Então você tá vendo que tá tudo aqui, você vem aqui, você olha e fala, ó, aqui que mudou de uma coisa pra outra. Mudou um monte de coisa. Todas as coisas estão descritas nessa página de alterações. Então você quer saber o que mudou? Ah, eu fiz a versão passada. O que mudou? Mudou uma caralhada de coisa.

**[00:58:43]** A resposta é essa. O projeto é o mesmo, mas foi revisado, corrigido e ampliado. Então, tá tudo aqui. Todo o material disponível pra vocês saber. Tá aqui. Ah, o que que mudou? Ah, correção no Windows. Coisas que estavam erradas na aula. Atualização do Poetry, porque não funciona mais na versão do ano passado. Ah, removemos um Tolkien Data aqui, que podia ser mais simples. Então, tudo foi melhorado, então tá aí.

**[00:59:13]** tudo detalhado, tem as descrições, das issues, ah, o que que mudou, o que que, sabe, o que que foi alterado, quando, quem fez o pull request, sabe, tá tudo aqui, então se precisar, tá tudo aqui explicadinho, massa, então acho que a gente fecha por aqui esse ciclo, e por hoje eu vou liberar vocês uma hora mais cedo, olha, olha como eu sou um professor legal,

**[00:59:46]** Tô liberando uma hora mais cedo hoje, mas é claro que eu vou ficar aqui pra responder perguntas se vocês tiverem perguntas. Então, quer aí ficar com a família, tomar banho, amanhã é dia de trampo, então fica à vontade se quiser sair agora, eu vou responder algumas perguntas de quem quiser, de quem precisar agora, quem tiver perguntas pra fazer sobre o conteúdo, né? Não vamos mandar tipo assim, ah, mas o que que você acha do...

**[01:00:16]** Sabe? Da filosofia do Bodeleta, ligado? Não. Nesse... Nesse contexto aqui. Massa? O Luiz falou que me mandou um píximo. Obrigado, ó. Beijo. Valeu demais. E aí, como eu disse, vou reiterar a pergunta é sobre o material. Tipo assim, não é sobre, tipo assim. Ah, o que que eu acho de outra biblioteca que eu não estou usando? Não acho nada, ligado. Não é o momento de a gente conversar sobre isso agora.

**[01:00:51]** esse era o único lugar que eu não queria ser liberado mais cedo amanhã, amanhã vai ficar, amanhã vai ficar as duas horas amanhã não, quinta-feira vai ficar as duas horas, não se preocupa talvez na próxima aula estrapolhe as duas horas vamos aproveitar essa hora, não, não hoje é dia de trampa que já é uma hora da manhã massa bom, já que ninguém tem nenhuma pergunta eu vou reiterar aqui

**[01:01:22]** O que eu tinha dito aqui, né? Então, tipo... Se não entrou no grupo do Telegram, tá aqui aulas, aulas sincronas. Tem aqui o link do grupo do Telegram pra tirar dúvidas. Então, entra lá. O link da agenda tá dando 404? Tá aqui a agenda. Tá funcionando, pô. Massa? Bom, aí você... Tipo assim...

**[01:02:21]** Ó, eu justinei, fiz uma pergunta aqui, tipo assim... Duno, começar agora no 4-0, se já fez a versão 1.0, seria interessante começar do 0? Justinei, o que você achar mais legal de fazer assim? Esse curso tem várias atualizações, tipo, em vários sentidos, se você quiser assistir de novo, vier aí comigo, a gente vai conversando, vai fazendo junto. Saca. Saca, então...

**[01:02:53]** Então, mãe, se quiser pegar umas aulas específicas para assistir, fica à vontade. A grande diferença aqui, eu vou tentar ser suscinto aqui. A grande diferença da versão 1 para essa agora é o seguinte, a primeira aula foi toda refeita, porque as coisas foram atualizadas. Na aula 4, a gente aprofundou mais com os seitos do SQL que ele é algo que me duquitinha na versão passada.

**[01:03:23]** Da aula oito pra frente, tudo é diferente. Então tipo assim, da aula oito, é uma aula nova sobre a 5IO, e dali pra frente, tudo muda. Ou seja, então se quiser pegar lá na frente, tipo assim, ah, sei lá, vou assistir da mudança do esquelhal que vim pra frente, da 4 pra frente. Ou da 8 pra frente, porque eu quero ver a 5. Tipo assim, pode assistir se quiser vir aqui também, pô, duas horinhas aqui, terça e quinta, a gente fica trocando ideia. Falando besteira, saca.

**[01:03:53]** Então... Tá tudo bem. João, obrigado, mano. Ó, valeu, mano. Espero que eu cumpre essas expectativas todas aí que tu tá, né, mano? Quando você passou pra Fittware, teve um monte de mudanças. Não seria legal, talvez, nessa versão em algo já deixar pronto... Não, eu não quero deixar nada pronto, mano. O curso é do zero, porque a gente faz junto, mano. Quando... Como eu...

**[01:04:25]** Como a gente vai fazer do zero, a gente vai fazer junto? Se eu trazer essa coisa pronta, a gente quebra a premissa 1, tá ligado? Que é tipo fazer do zero, tá ligado? Poetry não tem mais shell? Bom, não é que o Poetry não tem mais shell, ele tem, só virou um plug-in, que foi o que o Anderley mandou aí.

**[01:04:56]** O Rock falou que tem um erro de gramática lá na página, se quiser mandar o PR fica à vontade, mano. Tá tudo bem. A gente vê junto. Então, legal. Eu acho que... Ah, agora chegou uma pergunta aqui. Vi no projeto que você vai utilizar o Poetry Contendo. Você costuma usar os dois juntos desde o início ou começa o Poetry e depois faz a transição para o Docker? A gente vai ver o Docker na hora que a gente for começar a pensar na implantação. A gente não vai usar Docker desde a primeira aula até porque...

**[01:05:27]** só vai tornar tudo mais complicado. O Docker entra no momento do Docker. Lá na frente, na hora que a gente for começar a pensar em implantação, a gente vai ver o Docker. No começo, a gente vai é poetry, virtual, envy, até chegar no Docker. Sabe? Até a hora da implantação. Massa? Sei que vai acompanhar a primeira edição infestacional. Estamos juntos, mano. É nóis.

**[01:05:53]** Legal, então? Ó, eu vi que vocês fizeram várias perguntas, mas são perguntas que são fora do escopo da nossa apresentação aqui, né? Tipo, é coisa de Django, é coisa de SQL Model, saca? Então eu acho que pelo bem do tempo de todas as pessoas não faz sentido a gente ficar respondendo essas perguntas. Se vocês quiserem mandar elas lá no Telegram, mandem. Tá tudo massa.

**[01:06:24]** Legal? Bom, um beijinho pra vocês, eu vou ficar por aqui, vou liberar vocês mais cedo. Vamos, vamos, vamos curtir a vida, mano. Ter sol, jantou, vamos jantar, vamos passar um tempo com a família, ver o que está acontecendo aí. E é isso. Na quinta-feira a gente se encontra e aí a gente começa a macetação mental aqui, né? Tipo, vamos começar a fazer as coisas, configurar o ambiente e tudo mais na próxima aula.

**[01:06:55]** Massa? Então, a gente se vê lá. Vocês estão falando de pão entre, mano? Dá uma olhada na aula 1, tem a explicação sobre isso aí. Como fazer pro Shell funcionar no Python. Tá no material de texto. Sério. Eu juro que tá no material de texto. Então é isso, um beijo pra vocês. A gente se vê quinta-feira e ó, tchauzinho. Obrigado por acompanhar em essa missão. Espero que vocês se divertam.

**[01:07:26]** Cara, entra no link da agenda aqui, mano. Aqui, ó. Aqui. O link da agenda tá aqui, mano. Pegue ele aí. Legal? Então, eu vou finalizar aqui. E a gente se vê na quinta-feira. E se vocês tiverem dúvidas, tipo assim, ah, não tá funcionando. Eu preciso fazer no seu quê? Manda lá no grupo, mano. A gente vai resolvendo. Massa. Um beijo pra vocês. Brigado! Diogo pelo Super Chat. E tchauzinho a todo mundo.

