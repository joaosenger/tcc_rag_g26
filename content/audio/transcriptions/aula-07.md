# Transcrição da Aula: aula-07.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:07]** Olá pessoas, como vão vocês? Boa noite, eu sou o Dono Sauron e boas-vindas a mais uma aula do nosso curso de Fast API. Que a gente tá aqui trocando ideia. Hoje a gente vai trabalhar um pouco na refatoração dessa estrutura que a gente montou. Lembra na aula passada que eu tava falando? Não, você tem um monte de linha, um monte de coisa. A gente vai dar uma arrumada na casa. Mas antes, eu acho que tá tudo rolando, mas vocês me respondam, vocês estão me ouvindo, vocês estão me vendo. Se não, eu nunca sei como tá funcionando isso aqui.

**[00:00:36]** Aí vocês me dão feedback, a gente começa. Bom, enquanto vocês vão me dando feedback, eu vou dizendo aqui que, bom, toda essa aula também está aqui, né? Ela tem a versão em texto, aí caso você precise, tem todos os links, tem algumas referências a mais, coisa que a gente acaba não usando tanto na aula, né? Mas a gente vai por aqui, então, hoje. Massa? Bom, ah, valeu, todo mundo me respondeu que está tudo ok, então muito obrigado.

**[00:01:07]** Bom, essa aula sobre refatória estrutura do projeto, assim, vou conversar um pouquinho antes. A ideia dela é tornar o projeto mais fácil de manter do que a forma como ele está efetivamente estruturado aqui, não é hoje? Se a gente for parar para pensar, a gente vai ver que ele está, sei lá, tem uns arquivos muito malucos, tipo assim, ah, sem linhas, isso aí é um problema, não necessariamente poderia ser.

**[00:01:37]** Depende. Algumas pessoas também vão pensar que, sei lá, para um projeto ser legal e ser bem programado, ele teria que ter algumas implementações de patterns ou algumas outras coisas um pouco mais diferentes, sei lá, enterprise patterns ou domain driven design, sabe? Várias pessoas têm várias opiniões sobre o que a gente pode fazer ou deveria fazer aqui, né?

**[00:02:01]** Eu vou levar a gente para um caminho mais simples, né? Eu vou tentar pensar com vocês que a gente vai entender os recursos do Fast API, que possibilitam uma melhor escrita de código. Mas eu não quero ir para um lado, tipo assim, vamos em shared patterns, vamos criar 500 classes, ports e adapters, sei lá, service layers, use cases, não é esse o objetivo dessa aula hoje, então é interessante eu falar isso, né? Então, o que a gente vai ver aqui, né?

**[00:02:29]** a gente vai tentar colocar as coisas nos lugares onde elas deveriam estar simples assim vamos pegar todos aqueles arquivos monstros que a gente tem e a gente vai quebrar em partes menores e colocar em lugares certos e com isso a gente vai conhecer alguns recursos do pai dente que

**[00:02:48]** que são os queries via forms, a gente tem os routers, que são uma forma de separar o arquivo fastvpa em vários arquivos diferentes, e a gente tinha umas constantes que a gente falou, a gente vai remover isso daqui em algum momento, lembra? A gente falou sobre isso na aula passada, quando a gente estava colocando vários security, quando a gente criou security, a gente criou secret key.

**[00:03:13]** um monte de coisinhas lá. Então, basicamente, esse é o escopo. Não pense em coisas tipo de padrões de projeto, padrões arquiteturais, engenharia de software. A gente vai ir por um outro caminho, o caminho de arrumar as coisas com os recursos que o framework dá e prove para a gente. Massa, combinado? Então, vamos lá!

**[00:03:36]** Massa combinada, não espero ninguém respondendo, eles já vão, né? Mas qualquer coisa vocês me avisam aí. Então a primeira parte do que a gente quer falar hoje são sobre os routers. E o que são routers? Nós somos roteadores, né? A ideia deles, principal no Fast API, é que a gente consiga quebrar um arquivo do Fast API, tipo esse aqui que a gente tem aqui. Vamos lembrar do nosso app aqui. Então a gente tem várias coisas aqui. Tem aquele get que permite um domínio, a gente tem

**[00:04:07]** coisas de criação de usuário aqui, tá vendo? O post, o get, o put, o delete. E no de vocês tem mais, né? Porque vocês foram fazendo os exercícios, tem coisa de tokens, né? E você tá vendo que várias coisas que fazem parte disso aqui são coisas que, ah, elas não tem muito a ver, né? Por exemplo, ah, vou gerar um token, a nossa aplicação só tem esse negócio de users, por enquanto. Mas...

**[00:04:35]** Quando a aplicação crescer, como é que a gente lidaria com isso aqui? Então, o Tolkien tem a ver com o app, o Hello World que a gente tem aqui, o Alamundo tem a ver com a nossa aplicação, sabe? Então essas coisas elas são meio que separadas por natureza, né? A gente disse que isso aqui tem domínios, sabe? Então a gente pode separar, né? Em routers diferentes. Aí os routers, né? Além de permitir esse negócio de organizar e agrupar, né?

**[00:05:07]** Eles são subaplicativos de FastAPI. Então é como se a gente tivesse um arquivo de FastAPI novo para cada coisa que tenha a ver, que tenha o seu próprio domínio, que tenha a sua própria relação aqui dentro. Aí o Rodrigo fez uma pergunta muito legal aqui que eu adorei, que foi o seguinte. Tchau!

**[00:05:25]** Mas, se fosse pensar num padrão de projeto para estudar depois, qual seria o mais próximo aqui? Bom, como é que eu dividiria essa aplicação se a gente fosse pensar nesse caso? E, inclusive, é uma coisa que eu pretendo algum dia, né, ficando na minha cabeça, isso da gente escrever uma pente sobre isso. É fazer layering, né? Separar encamadas a aplicação seria uma forma de tentar minimizar o escopo disso.

**[00:05:51]** Aí, dependendo da literatura que você estiver usando como base, às vezes você tem o Domain Driven Design do Erky Events, você tem o Pattern of Enterprise Applications do... Caraca, esqueci o nome!

**[00:06:07]** Pô, me fugiu agora da cabeça. Mas aí você tem dois lados e aí de um lado a gente tem useCase e do outro a gente tem serviceLayers, né? A gente poderia tentar separar a aplicação. Entre a parte dos routers, né? Que é a camada de apresentação, uma camada intermediária no meio que eu vou chamar de serviços ou de useCases e a interação com o banco de dados a gente poderia usar um repository, uma coisa um pouco diferente, ou repository, cada pessoa chama de um jeito diferente.

**[00:06:35]** do Martin Fowler, obrigado. Me fugiu da cabeça aqui, o Rafael mandou aqui, né? O Patterns of Enterprise Applications é do Martin Fowler. Então, daria pra fazer por esse caminho. O que eu quero mostrar pra vocês hoje é uma coisa um pouco diferente, porque são os recursos do próprio framework, né? Afinal, a gente tá num curso de fast API, num curso de, sei lá, de engenharia de software.

**[00:06:58]** Mas a gente poderia conversar sobre isso em outro momento, caso vocês tenham interesse. Como é que a gente separaria essa aplicação em layers diferentes e tudo mais? É uma coisa possível de se fazer aqui. Então, a ideia principal agora é ver esses roteadores e entender como é que a gente separa no Feste API aqui. Bom, a primeira coisa que a gente vai fazer aqui é que eu criei uma passinha chamada routes.

**[00:07:25]** mas poderia ser routers, eu vou usar routers, porque eu acho que é mais interessante aqui. Então aqui dentro do nosso Fast API 0, ou Fast 0, dependendo do nome que você deu para o projeto aqui no meio, eu vou criar uma passinha que eu vou chamar de routers no plural aqui. Então a gente tem essa passinha chamada routers. Aí dentro dessa pasta...

**[00:07:51]** a gente vai começar a dividir as coisas que fazem sentido cada uma dentro do seu próprio contexto, né? Então, por exemplo, vamos lembrar que aqui a gente tem várias coisas de manipulação de user, né? Esse post, esse, o post, o get, o put e o delete e tem mais coisas no projeto de vocês, né? Que foram os outros endpoints que a gente foi criando. Então, a ideia que primária é remover tudo isso aqui do nosso app. Olha que legal!

**[00:08:21]** Tiramos tudo daqui, eu dei contra o x, eu dei cortar, porque eu vou colar nesse outro arquivo agora. E aí aqui, a gente vai criar um novo arquivo que eu vou chamar de users. Users.py. E aí aqui dentro do users, a gente vai ter todas as rotinhas, todas as coisas que o user precisa para funcionar. Obviamente nem tudo está aqui, porque a gente precisa dos imports e tudo mais, mas a coisa importante do FastAPI que a gente precisa aqui é esse API Router aqui.

**[00:08:55]** E a gente poderia fazer assim. Então, vamos supor que a gente queira fazer app igual a API Router. Então, a gente tem o nosso próprio roteador aqui, a partir disso. Saca? Então, a gente tirou tudo de um lugar.

**[00:09:10]** que estava tudo misturado, coisas que não tinham muito a ver, uma coisa com a outra, e separamos em um arquivo mais simples. Obviamente, a gente vai ter que chamar os imports todos aqui, né? Então, o que faltou aqui, né? O HTTP status, o LSP legal nessa hora, porque ele mostra as coisas que a gente precisa, né? Então, vamos lá. From HTTP, import HTTP status. Legal, trouxemos alguma coisa pra cá.

**[00:09:37]** A gente tem vários models, o user public, user schema e tudo mais. Eu vou copiar daqui para ser mais rápido, né? Então, a gente vai trazer daqui dentro da nossa aplicação, né? A gente não usa o Tolkien aqui, porque o Tolkien vai ficar lá no Tolkien. Mas o Kai falou, bora deixar o like. Bom, tem muito mais gente vendo do que likes, dados, então faça um favor aí. Ajude-se a chegar em mais pessoas.

**[00:10:05]** Então, a gente trouxe aqui, a gente está trazendo as coisas do SQL Alchemy, o Select, o erro de integridade, o Session. Então, vamos trazer para cá também. Aí, faltou do Fast API. O Depends, né? Depends. Aí, a gente vai vendo aqui, conforme vai passando. Falta o User. E aí, aqui no meu editor, ele vai ficando. Nessa TVLSP configurada, ele vai mostrando tudo que não está sendo usado aqui.

**[00:10:40]** Aí esse erro de integridade também não tá sendo usado, a gente precisa do Select e da Session aqui também. O Session já tinha trazido... Ah, o Select também. Então falta o GetSession e o User, né? Que eles estão aqui, um no... Ó, esses dois também não estão sendo usados, vou tirar daqui. Então a gente quer o GetSession e o User daqui também. Então...

**[00:11:11]** Pensei que tinha copiado, mas não copiei nada. Legal. Aí, faltou HTTP Exception do Fast API, HTTP Exception. Falta o GetCurrentUser, que vem lá do Securities também aqui. Eu acho que é onde ele está agora, né? Então vamos lá. Securities bem por último aqui. A gente tem o GetCurrentUser. Falta o GetPasswordHash.

**[00:11:55]** Acho que só isso aqui, pra gente poder trazer tudo pra cá. Gantt Password Hash. Aí uma coisa legal que a gente poderia fazer aqui é dar uma formatada pra garantir que está tudo funcionando aqui, então vamos lá. Task Formant, aí você pode dar o Poetry Shell ou Poetry Ram, aí é contigo. Aí ele deixou tudo bonitinho aqui. Legal. Agora tudo que tem a ver com user está aqui e não está mais...

**[00:12:28]** no app genérico aqui. Olha como isso é interessante. Então fica tudo que o user está no user. Caio, muito obrigado pelo seu super chat, mas isso me ajuda muito, valeu mesmo. Então essa é a organização, parecia, tipo assim, se vai pensar pô é muito mais complicado, mas na real é tudo bem de boa aqui.

**[00:12:53]** Uma coisa que isso aqui permite com que a gente faça é que a gente documente isso aqui de alguma forma, né? Então aqui a gente tem um negócio que a gente chama de tags. Aí as tags aqui, elas servem só para a documentação lá no swagger.

**[00:13:07]** Só que quando a gente for lá, a gente vai ter um lugar, olha, a gente vai ter tipo um menuzinho, né? De seleção e fala, olha, esses são os defaults, esses aqui são os endpoints relativos à user. Então você vai clicar lá e ele vai dar essa opção para a gente poder mexer. E uma outra coisa que tem aqui é o prefix. E aí o prefix é o nosso melhor amigo aqui, porque ele vai ajudar a gente a deixar tudo mais simples de funcionar aqui.

**[00:13:34]** Porque você está vendo que todos os endpoint são barra users. Barra users, barra, barra users, barra. Barra users, barra. Então a gente pode dar um prefixo aqui e falar que isso aqui é barra users. Está vendo? Aí eu falar que isso é barra users e aí tudo o que estiver dentro desse router aqui ele já vem, tirado isso da frente, ele já vem aqui. Então...

**[00:14:01]** esse endpoint de post agora ele é o barra users barra no método post então fica mais simples de escrever fica tudo menorzinho né então esse é o get barra esse é o users barra user id e aqui no delete a gente tem isso aqui né users também no barra fica mais simplão de escrever né fica mais bonitinho né

**[00:14:35]** Aí o nome que eu dei aqui, eu vou seguir o mesmo nome, só pra gente não se perder aqui, depois ficar diferente do texto, eu dei o nome de Halter aqui, né? E eu poderia deixar como Halter. Só que aí, você tá vendo que isso aqui não é mais app, né? Então a gente poderia substituir. App ponto, a gente vai trocando, né? Por Halter, app ponto, a gente troca por Halter, app ponto, a gente troca por Halter. Legal, tem mais algum app? Ninho.

**[00:15:04]** Então, essa é uma forma de reestruturar isso aqui de uma forma mais simplana. Simplana, bonitinho, fica legal, funciona, a gente tira responsabilidade de onde não tem. Onde não tem que ter essa responsabilidade, sei lá. A parte de usuários está isolada num domínio específico aonde a gente trata somente usuários. Aí eu fiz aqui uma forma de como isso aqui ficaria, barri-user, tal, tal. Só pra gente ter um exemplo de como isso ficaria no final. Mas lembra que é só os barras aqui, né?

**[00:15:38]** É só as coisas, as implementações dentro de Point, o importante é que a gente foi fazendo na mão. E aí, eu vou também criar um halter para Alf. Porque, por enquanto, nesse momento, aqui no app, a gente só tem uma coisa de autenticação aqui. Mas isso aqui poderia ser um lugar sozinho. Porque, no final, no futuro, a gente vai ter mais coisas, mais opções, mais negocinhos para colocar aqui. Então, aqui dentro da pastinha de halters, eu vou criar um Alf.

**[00:16:11]** ponto py. E aí agora as coisas de Alf estão no lugar de autenticação. De novo, os imports estão todos, eles vão precisar sair daqui, eu vou só copiar, trazer para cá de um jeito mais simples dessa vez, a gente vai apagando o que não precisa aqui. Então a gente não precisa do message, a gente não vai usar o FastAPI aqui, porque a gente vai usar o halter, igual a gente fez aqui. Então o API halter.

**[00:16:43]** E aí, eu também vou fazer uma coisa bem parecida com essa. Eu vou chamar de Halter aqui, sem nenhum problema, né? Então, a gente trouxe pra cá o Halter, só que aí a gente lembra, né? Tipo assim, qual que é o nome que a gente vai dar pra esse aqui? Como são coisas referentes à autenticação, eu vou chamar de... O prefixo vai ser Alf. E a tag também vai ser Alf, né? De autenticação. Essa é a ideia. Aí a gente tem que mudar, né? O app que ficou aqui pra Halter. No final...

**[00:17:17]** A nossa base da API ficou só com essa coisa aqui, que poderia ser um health check, uma coisa, sei lá, uma checagem, uma coisinha mais simples. Então, eu vou tirar todo mundo daqui. O Tolkien a gente não tá usando, a gente tá usando só o Message, Get Session, User. Olha tantos de coisas que a gente limpou daqui. Legal. HTTP Exception, o Depends, saiu tudo daqui. Fica muito mais simples, né? O Rodrigo deu aqui. O melhor é que assim fica mais tranquilo de trabalhar em equipe.

**[00:17:47]** E fica mesmo, né? Porque cada coisa está no seu lugar e quando a gente vai contribuindo, né? Isso é uma coisa interessante, eu vou falar. Quando a gente está mexendo num projeto um pouco maior, quando a gente tem uma equipe trabalhando, se a gente tem tudo no mesmo arquivo, você vai ter que fazer um review e aí comitou no Git a diferença, vem tudo no mesmo arquivo, fica uma bagunça e tudo mais, do jeito fica até mais simples, né? Pra poder trabalhar, pra ver tudo direitinho. Ó, deixa eu...

**[00:18:18]** e deixando mais lindinho aqui, mais bonitinho, aqui só ficou o Tolkien, então vai acabando ficando tudo mais simplão aqui, mesmo os importos aqui. Pronto, olha, legal. Vamos dar um format para ele dar uma arrumada em tudo. Ah, ele rodou tudo. Uma coisa que eu quero saber aqui, eu quero rodar o lint, né? Para ver se está tudo funcionando, está tudo bonitinho e não ficou nada perdido em lugar nenhum, né? Então, lint. Beleza. Tudo passou. Olha que legal.

**[00:18:57]** A Xanadinha falou, dá até um calafruim pensar como seria o Rebase, sim, porque são muitas coisas do mesmo arquivo e coisas que são descopos diferentes, então tudo mais, então fica mais lindinho, mais bonitinho de mexer. Mafa, muito obrigado, mano. Ó.

**[00:19:16]** Tamo junto, valeu demais, mas no Super Chat me ajuda demais, mas vocês não têm noção. Legal! E aí, meio que a gente organizou tudo. Olha que legal! Só que falta uma coisa aqui ainda, né? Que a gente precisa ver. Como é que a gente linka, né? O aplicativo, o FastIP, aí eu vou rodar ele aqui. Acho que vai ser mais interessante da gente ver. Eu vou dar o Tasker Brown para ele subir o servidor. E quero mostrar para vocês como é que ficou, né? Lá no Swagger, por exemplo. Então, local host.

**[00:19:47]** 8 mil, não subiu ainda. Vai, beleza. Então, barra dox. Olha como é que tá agora. Agora a gente só tem a nossa pay bala aqui, né? Mas só tem o default, tá vendo? E o único esquema que tem aqui é message.

**[00:20:05]** Porque embora a gente tenha separado, tenha usado aquele esquema do FastJPi e de criar halters diferentes em lugares diferentes, a gente não convergiu tudo em uma coisa sóna. E é o que tá faltando de acontecer aqui, né? Tenho preciso pegar todas as coisas e juntar elas. E é como é que a gente faz essa junção das coisas, né? Aqui, o próprio app do FastJPi tem um esquema que se chama Include Halter. Ou seja...

**[00:20:36]** Coloque, né? Inclua o router dentro dessa aplicação aqui, né? E aí a gente criou aqueles arquivos e a gente pode importar eles. Então vamos lá, vamos ver como a gente faria isso aqui. Bom, aqui a gente pegou o message, algumas coisas, então vamos lá. FromFestAPI0.houters. Como é que eu deixei o import aqui? Eu dei... Beleza. Então import na Alph e import users.

**[00:21:07]** E aí, junto com isso aqui, a gente pode simplesmente dar um app.include router e passar, né? Uma coisa que tem que tomar cuidado aqui pra entender, olha como é que eu fiz isso aqui. Então é um ponto router, só pra deixar certinho. Você tá vendo que a gente tá importando do módulo do nosso pacote? Dentro do routers a gente tá importando o arquivo alpha, né? Então a gente tá importando o módulo alpha.

**[00:21:31]** E aí, o que ele quer incluir é o router de Alphan. Então, a gente tem que colocar essa variável aqui. Esse é um erro que aconteceu bastante vezes com o pessoal na versão passada desse curso. Então, users. Users, routers. Pronto. Agora, em teoria, tudo tem que estar conectado. O servidor já deu reload aqui. Vamos lá no Swagger de novo. Opa. Drive 5. E massa. Tá tudo aqui. Olha que bonitinho. Ele criou uma...

**[00:22:00]** uma classificação para cada roteadora. A gente tem um alf, né? Isso aqui é por causa da tag. Então a tag deixou esse nome alf aqui. Aí ele adiciona aquele prefixo, alf barra token. Quero que a gente tinha aqui no alf, né? Então aqui ó, barra alf, barra alf barra token. Olha que bonitinho. Users.

**[00:22:23]** O default fica até mais fácil, para quem for consumir a documentação fica mais simplório de viver. Você sabe exatamente o que você quer, onde está. Se você for lá no Redock, ele separa também alf, users, e aí você pode ir olhando aqui um por um, fica mais bonitinho, mais organizado, tanto na documentação.

**[00:22:51]** O Vanderlei falou o seguinte, se existisse 300 routers, qual seria uma boa prática? Importar um a um ou asterisco? Nunca se usa asterisco em código que você precisa garantir uma integridade e tudo mais. Asterisco é uma prática legal para quando você está fazendo programação criativa, para quando você está no meio de uma brincadeira jogando todo mundo, quando você está dentro do terminal rodando coisas.

**[00:23:21]** Mas, em teoria, o código que você precisa rodar os linters, o teste, entender a cobertura, o interessante é não usar asterisco, nunca, nesse sentido. Mas, aí o Davidson mandou um super chat pra gente. Davidson, muito obrigado, mano, valeu. Mano, me ajuda muito, esses super chats. Valeu demais, mano. Dá pra colocar mais de uma tag por Halter? Dá sim, isso aqui é uma lista, né? Você poderia colocar, sei lá.

**[00:23:52]** pay só pra gente ver o que que acontece aqui aí quando a gente voltar lá no swagger aqui ó ele tem dentro dos dois lugares aqui ó o off e o pay aqui tá vendo não vou deixar o pay aqui mas é só pra mostrar que dá pra fazer esse tipo de coisa e aí ele fica certinho você pode usar em múltiplas tags múltiplas coisas aqui massa então acho que a gente passou por essa primeira parte de tentar organizar um pouco a casa mas

**[00:24:26]** Eu já me mostrei o Swagger também, vamos rodar os testes e ver se tudo continua funcionando agora. O que eu acho que não vai rodar, né? Vamos ver. Então, vamos lá. Ahn, legal, ó. Ele tá reclamando do offusers aqui, vamos dar um format. Só para ele arrumar as coisinhas e aí vamos dar um teste aqui.

**[00:24:56]** Algumas coisas passaram, outras coisas falharam. Lembra que o nosso teste está com "-x", quando a gente roda ele? Então na primeira falha, ele para de ser executado aqui. Deixa eu achar que pai teste aqui. Opa! Então ele roda com "-x". Esse "-x", ele falha o primeiro teste que ele encontrar o problema. E ele deu erro aqui no read users. Aí vamos ver o que aconteceu.

**[00:25:28]** Olha onde deu erro, ele deu erro no Tolkien, tá vendo? Porque pra enviar, pra ler os usuários, a gente precisava estar logado na aplicação. Só que o Tolkien aqui não é mais barra Tolkien, né? Como a gente colocou o prefixo no alf, agora ele é barra alf, barra Tolkien. Então a gente vai ter que mudar isso aqui, lá nos testes do alf. Vamos lá? Testes, a gente tem a conf-test, barra alf, barra Tolkien, aqui. E a gente vai colocar um barra alf, barra Tolkien.

**[00:25:59]** E aí, agora, toda vez que ele for gerar o token, ele vai pro endpoint certo dentro dos testes. Vamos rodar de novo e ver o que acontece agora. Quase tudo passou, o create, o read, o update, o delete, o integrity error, mas o teste do token falhou. Porque o teste do token falhou? A gente já sabe, né? Por que que ele falhou? É que o teste security, né? Não, é no teste app mesmo.

**[00:26:30]** Barra Tolkien, porque aqui também a gente tem esse mesmo problema, que teria que ser barra Alph, barra Tolkien. Vamos rodar de novo, espero que tudo passe agora. Legal, lindo, ó! Maravilhoso. Foi facinho de arrumar o teste, só aquela URL que estava errada. Pô, muito legal, funciona, né? A gente tem esse problema, trocamos isso aqui, né? Pro barra Alph, barra Tolkien. Só que a gente ainda tem um problema aqui, que é no Swagger.

**[00:27:02]** E embora os testes estejam passando, está tudo funcionando, se a gente for rodar lá no swagger, aqui eu vou dar um autorize, olha para onde ele está indo aqui, é o ARL do Tolkien. Tolkien, o ARL vai para a barra Tolkien. Isso acontece por conta daquele fome do próprio FastAPI, né? Que ele dá o, o Alf2 Password Bear, né? Então, isso aqui, ele está lá no security. Deixa eu achar aqui. Aqui, ó.

**[00:27:33]** ou alf skim ele fala que está no barra token e aí precisava ser barra alf barra token e aí agora se a gente rodar de novo então cinco aqui o autorize vai para o lugar certo oh massa está ficando bonitinho está ficando bonitinho mas ainda tem mais coisas para a gente arrumar não não estou contente só com isso aqui não então a gente arrumou o token

**[00:28:00]** Agora a gente falta reestruturar os testes, né? Porque, pô, é muito legal a forma que a gente fez aqui, né? Ó, criou um halter e foi distribuindo as coisas. Por que não fazer isso nos testes também? Por que não deixar os testes organizadinhos? Saca, é uma coisa que a gente poderia fazer. Separa por domínios os testes também. Vamos pensar, ó, a gente tem os testes do app, que tá todo mundo também, né? Ele roda o olamundo, tal, tal, tal, tal, tal. É isso que a gente quer.

**[00:28:29]** Lembra, não precisa ser fácil de descrever, precisa ser fácil de testar também, então vamos tirar todas essas coisas de user daqui, delete user, integrity error, e aí o teste do token fica aqui por enquanto. Aí o que a gente vai fazer aqui? Eu vou criar um teste users para as coisas do user, nada mais justo do que isso aqui, então vamos lá.

**[00:29:05]** Como a gente está usando fixtures aqui, fica tudo mais simples, né? Porque as fixtures já altos são importadas, né? Então o que vai faltar aqui é só o HTTP status, né? E esse public model que ficou aqui. Basicamente, esses dois imports. Aqui a gente não vai usar mais, então pode deletar e vamos trazer isso aqui para cá.

**[00:29:29]** Aí, uma coisa que eu gosto de fazer, conforme a gente vai mexendo, vai rodando os testes de novo, pra gente não ver tudo só lá no final. Então, vamos ver se tá tudo funcionando aqui. Task test. Legal. Olha, ele reconheceu todos os testes de user aqui, né? Aqui, ó, test user, tá todo mundo aqui. Uma coisa que alguém poderia estar se perguntando, é tipo assim, e se eu quisesse rodar só os testes do user, que agora a gente tem um arquivo separado, você poderia fazer o seguinte. Task...

**[00:29:58]** Deixa eu entrar no shell aqui para ficar menor o comando. A gente poderia fazer o seguinte, TaskTest, e aí você passa o diretório Testes, e aí você pode passar o Test Users. O comando TaskTest permite essa concatenação aqui. Caso você precise rodar só alguns, agora que você tem um lugar menor, mais organizado para poder ver isso, fica mais simples.

**[00:30:26]** E aí, agora a gente vai pros testes do Alf aqui, que são só esse aqui de Tolkien, né? Por enquanto. É interessante lembrar, por enquanto. Então agora eu vou criar um test Alf. Test underline Alf. Legal, trouxe pra cá, a gente precisa do HTTP status, né? Porque a gente tá usando ele como base aqui pra verificar. Legal. Roda tudo de novo, você pode rodar só o Alf, se você quiser.

**[00:31:04]** Beleza, passou. Aí você vai ver que a cobertura fica muito maluca, porque a cobertura é pra todo mundo, mas... O interessante que você queria ver é isso aqui, ó. Passou esse teste. Ah, beleza. Quero ver se passa tudo. Só por desencar o de consciência. Continua passando. Massa. Então, com isso, a gente organizou. Eu não sei o que vocês acham disso, porque vocês acham que ficou melhor de ver agora? Porque você tem aqui, nossa, os roteadores específicos têm as coisas específicas. Os testes...

**[00:31:33]** Testam cada coisinha em específico aqui também, né? O teste do app, o teste do app, o teste do off, o teste do off, o teste do user, o teste do user. Saca, aí é uma questão que eu queria conversar com vocês. Vocês acham que fica melhor de mexer no projeto assim? Agora você pode ir no lugar onde você quer, né? Você fica muito mais simples. A Ocha pergunta se pode enviar o pastel via pix, claro que pode, mano.

**[00:32:00]** aí o Thiago falou definitivamente então acho que ele achou que fica mais simples também concorda comigo aqui na hora de organizar isso que aí rodamos os testes e aí aqui tinha um problema que era tipo assim que eu deixei no slide mas eles não funcionam porque eu ia arrumar o Alf aqui mas eu eu eu me empolguei né eu me empolguei aqui e aí fui corrigindo tudo quando foi partindo os meus perdão por isso

**[00:32:27]** Aí o que eu ia deixar aqui é aquele de acertar, né? O off-talking. Eu tô empolgado, né? Aí fica difícil quando eu tá empolgado. Então legal, arrumamos os testes, arrumamos as coisas e agora a gente vai pra terceira parte desse infector maravilhoso aqui. Assim, muito melhor, cada coisa no seu lugar, mas que legal que vocês gostaram aqui. Aí!

**[00:32:50]** Agora a gente vem para a terceira parte aqui, que são algumas boas práticas do Fast API. Então, a primeira coisa, a gente aprendeu os routers do Fast API, depois a gente organizou os testes para ficarem de acordo com o domínio dos routers, e agora vou trazer dois conceitos para vocês aqui. O conceito de query strings do Fast API e o tipo annotated, que é do typing. Só que a gente vai fazer isso com a ajuda da análise estática. Lembra que a gente...

**[00:33:19]** colocou lá no arquivo no PyProject quando a gente estava configurando o projeto aqui a gente configurou o rough e aí a gente configurou várias regrinhas pra ele aqui aí todas as regrinhas que a gente tinha eram regras de boas práticas de código de uma maneira geral era o flake, os erros, os estilo a única coisa que a gente tinha de boas práticas de bibliotecas

**[00:33:51]** Era o PiTest, não é? Que é o PT. O Ruff, ele tem uma coisa chamada FEST, né? Então se a gente for lá no Ruff AstroFest, vamos ver se ele acha que logo de cara é pra mim. Não pegou, mas a gente pega aqui. Ruff, aqui é Rolds. Olha aqui, deixa eu procurar o FEST. Olha, ele tem umas regras de boas práticas do próprio FEST API aqui.

**[00:34:25]** Então, são só três, mas eu vou habilitar elas com vocês aqui para a gente ver o que que acontece, tudo mais, para a gente procurar por boas práticas do FESTE API aqui dentro. Então, a única coisa que a gente tem que fazer aqui é adicionar o FESTE no PyProject. E aí a gente vai ver se a gente está seguindo as regras que precisariam seguir. Nada muito... muito diferente, mas é simples, né? De colocar, então, por que não? Aí a gente vê.

**[00:34:57]** O que ele recomenda aqui, ou não? Se a gente rodar, a primeira coisa que ele vai falar é do annotated. E eu vou explicar isso para vocês, mas vamos ver o erro na nossa cara aqui. Pasquen lint. Ele deu vários lugares aqui, a gente está usando aquela sintaxe, né? O que é o seguinte, a session é do tipo session e depende de get session. O fast.mpi, na documentação, ele recomenda que a gente use

**[00:35:28]** a injeção de dependência usando um tipo chamado annotated. E aí, o tipo annotated, ele vai permitir com que a gente diga qual é o tipo que a gente quer aquela coisa e quem vai ser aquela coisa. Vamos lá. Então, tipo assim, session depende de get session, né? Essa é a forma que a gente tem aqui. E aí, o annotation permite que a gente faça isso aqui, né? O annotated, né? Anotated session depends get session.

**[00:36:00]** Olha como isso é legal. Você está vendo que a gente está definindo isso aqui dentro de uma variável. E aí isso faz o... A gente não tem que ficar definindo isso todas as vezes em todos os endpoints. Vamos lá para o nosso router de users aqui. Você está vendo que a gente faz isso aqui toda vez aqui? Session...

**[00:36:25]** O atributo session é do tipo session e o que ele depende é da função get session. Aí a função de annotator do Python, que ela vem do typing, então vamos lá. From typing import, import annotated. A função desse tipo aqui é fazer o seguinte, eu falo qual é o tipo que eu espero, então a gente quer o tipo session, por exemplo.

**[00:36:53]** E qual é, e a partir daqui, né, quais são os metadados que a gente quer adicionar a esse tipo? E aí eu posso falar que é o seguinte, olha, é o Depends Get Session. Aí a gente pode falar que isso aqui é Session, por exemplo, Session. Isso vai tornar tudo mais simples, porque em vez de ter que passar todo esse negócio do tipo aqui embaixo, tá vendo? Ah, Session depende de não sei o que, a gente pode só chamar.

**[00:37:26]** Session. Então, isso aqui é do tipo Session. Aí a gente criou uma variável, né? Para armazenar isso aqui, que fica mais bonitinho, mais simples. E aí para todo mundo, a gente pode tirar esse dependente tal, tal, tal, porque já fica subentendido via esse tipo annotated, que a gente vai dizer qual é o tipo e qual é o meta dado que é necessário aqui dentro. Você poderia passar isso aqui assim também, se você quisesse.

**[00:38:00]** Eu acho que não é a forma mais glamourosa de usar isso aqui, mas dá pra fazer também. Se você precisasse assim, a notante de Session Depends Get Session. É uma forma de usar também. Aí fica até o critério como você prefere fazer. Eu acho que criar variável é mais simplório, porque a gente só usa aqui. Type Session. Aí ele vai falar o seguinte, olha. Type Session é o tipo do RM Session que o uso Depends de Get Session.

**[00:38:34]** A gente pode ir refatorando todo mundo aqui e tirar os Depends daqui, né? Aqui ó Session... Session... Vamos rodar pra ver se tudo continua funcionando aqui agora? Com essa variável aqui? Task test, ele vai reclamar de algum lugar... Ah, porque ainda tem lugares, lá no Tolkien, ainda tem o... OALF, tal, tal, tal, tem o Get Current User em algum lugar que a gente tá passando também. Então vamos arrumar todos aqui, o Current User.

**[00:39:15]** Vou colocar aqui o coolHantUser, recebe o tipo annotated, ele vai usar user, que é o tipo que ele vai dar pra gente aqui, deixa eu achar aqui coolHantUser, e aí ele depende de getCurrentUser, então a gente poderia fazer o seguinte aqui, coolHantUser, e chamar ele aqui em cima.

**[00:39:58]** Pergunta, é possível com Depends fazer um annotation de uma função que depende, que também possui Depends? Sim, é totalmente possível, você pode fazer isso aí. Você pode colocar várias dependências injetando uma na outra, que o Festa API vai resolver essa sequência para você. Ele permite com que isso seja feito. Vamos ver se eu não deixei mais nenhum Depends aqui ó, ficou aqui também, né? Current User, ele é do tipo Current User. Em teoria,

**[00:40:29]** Esse arquivo foi resolvido, não é? Vamos dar um link? Aí a gente ficou aqui no user, parametro de default. Ah, tá, legal. Isso aqui é uma coisa que eu tenho que falar também. Tá vendo que aqui ele ficou com um outro corrente user? Peraí. Achei que eu tinha tirado todos. Essa parte refatorar é sempre legal e vendo o link interior e usando ele toda vez. Tá vendo que aqui a gente tem uns parâmetros que são default? Ou seja, que tem um valor padrão aqui?

**[00:41:04]** No Python, isso aqui só pode acontecer depois dos nomeados. Ou seja, você tem aqui os parâmetros posicionais e aqui você tem os parâmetros nomeados, que é o que tem um valor default. Ele sempre tem que ficar por último, senão o Python dá erro nessa coisa. Vamos rodar agora. Legal, agora a gente só ficou com um alf para resolver esses tipos daqui. Então a gente tem o session lá e esse o alf password request form.

**[00:41:35]** Então vamos mexer lá no Alps. Então a gente tem o tipo de sessão, então vamos lá. From typing import import annotated. E aí eu vou criar um session aqui pra gente. Session annotated de session. Depends get session. E eu não sei se eu dei um nome pro outro aqui, né? Tipo, eu chamei de o Alph farm aqui, só pra ficar.

**[00:42:12]** certinho. E aí a gente tem aquele negócio do próprio FastAPI, que é um Depends, que não depende de nada, tudo bem. A gente tolera esse tipo de coisa aqui. Aí o David tinha mandado aqui, teria problema fazer esse Shadow na variável do import ou para esse caso não teria grande impacto? Eu não sei se eu entendi o que é esse Shadow.

**[00:42:41]** Na variável do import, se você quiser me explicar, eu não sei se eu entendi essa pergunta. Legal, vamos rodar agora o link, ver se está tudo passando. Ó, tudo funcionando. Legal, ficou mais simples, ficou menor o código. Olha que bonitinho. E a gente não tem mais esse problema aqui, né? Então, vamos rodar os testes só para ver se está tudo funcionando. Nossas injeções funcionaram e conseguiram ser sobre escrita. Muito massa.

**[00:43:21]** Ah, vocês estão falando da gente redefinir a variável que é importada? Então, não tem muito problema aqui, né? Porque aí é uma questão dos próprios tipos do Python aqui, né? Session aqui é o tipo Session. No final das contas, esse tipo Session, ele é esse tipo, é o mesmo tipo. Algumas pessoas não gostam de fazer esse tipo de coisa, tipo assim, ah, eu não quero sobre escrever, né? Aí, lá na PEP 8, vamos lá, PEP...

**[00:43:51]** 8 Python. Legal que hoje todas as nossas perguntas têm a ver com a aula, eu estou muito feliz com isso. A gente tem aqui as variáveis de tipo, então type variable name. Aí uma grande coisa que eu ia introduzir aqui, quando a gente vai usar um tipo, é que a gente fale que é um tipo. A gente pode colocar esse prefixo t na frente.

**[00:44:17]** Algumas pessoas não gostam muito disso, mas você poderia fazer o seguinte, esse é o T-Session, e variáveis de tipo são definidas com letras maiúsculas, essa é uma coisa dessa PEP. Aí você fala, eu não quero sobre escrever, então você poderia usar o T-Session aqui, se fosse o caso, porque ele é o tipo Session.

**[00:44:38]** Aí vai do teu gosto, assim. Não tem nenhum problema sobre escrever isso aqui, você viu que nem o lin inter deu problema e tudo mais. Mas aí é contigo. A forma como você quiser fazer. Deixa eu pegar aqui, manda o link pra vocês aqui do type variable names. Decession, feion, eu também acho. Então, se você precisar aqui colocar um nome de um tipo, a gente costuma colocar isso aqui, sempre em letra maiúscula. Isso aqui é pra variáveis de tipo, mas...

**[00:45:10]** Dá pra entender o esquema, né? Está armazenando uma variável anoteita do tipo. Aí esse coi contra são de covariante contra variante e não entra no nosso ponto aqui. Mas se você for usar, a boa prática diz que o nome do tipo tem que ser com letra maiúscula, aí é contigo. Massa, está tudo funcionando aqui. Quando eu vejo ter alguma coisa, me remete a generics, né? É porque é o tipo session, né? Você poderia fazer...

**[00:45:44]** Session type, mas também ficaria muito esquisito também, né? Eu vou manter o session aqui. Massa, legal, simplificamos o off, rodamos os testes, tudo continua funcionando aqui, legalzinho. E aí eu quero mostrar pra vocês uma coisa que a gente pode fazer com as queries, né? A gente tinha aqui no user, né, na função de get aqui. Cadê? Cadê? Cadê o get? Get.

**[00:46:18]** A gente tem aquele Offset Limit aqui, né? A gente poderia, né? É uma coisa que... A partir de uma versão mais nova do Fast API, quando a gente deu esse curso no ano passado, isso aqui não existia ainda, né? Mas a grande sacada é que agora, para todos os Query Strings, né? Aquelas coisas que vêm na URL com um ponto de interrogação, a gente pode tirar daqui e criar um modelo do Piedantic para isso. Então, vamos pensar lá nos nossos esquemas.

**[00:46:50]** É um esquema de query string, né? A gente poderia criar um class, aí eu chamei de filter aqui, né? Filter page, né? Que filtra a quantidade de coisas. Então, filter page, por exemplo. É um base module. E aí você poderia passar aqui, né? O limit e o offset. Olha que interessante. Só que isso só pode acontecer graças ao campo annotated, né? Aqui. Porque aí você pode falar aqui, ó. Ah, então beleza. Vou importar ele aqui só pra não esquecer. Filter page.

**[00:47:29]** Cadê o nosso get? Aqui. Você poderia falar o seguinte, olha. Deixa eu só lembrar o nome que eu dei aqui. Eu dei filter users aqui, né? Filter users é do tipo que a gente vai chamar de filter page aqui. Aí você poderia chamar isso aqui, né? Filter users.limit, por exemplo. Filter users.offset. Essa é uma das coisas mais legais que eu vi aqui.

**[00:48:02]** Só que dessa forma, como a gente tá usando, eu vou subir aqui pra mostrar um problema pra vocês lá no Swagger, acho que vai ser legal de mostrar isso. Vou dar um get aqui. Quando a gente vier aqui no get do users aqui, você vai ver que ele requer como bari, né? E a gente quer que isso seja query, né? A gente quer passar esses campos na URL. Então, o Fast API tem um outro campo aqui que chama query. Aí você pode importar ele aqui, query.

**[00:48:33]** Aí você pode falar que esse filtro tem o metadado de query. Só que como é que a gente vai passar isso aqui? Não tem como a gente mover essas coisas. Então aí entra aquele tipo annotators que a gente tinha conversado lá atrás, que é o tipo filter page, ou seja, todos os parâmetros do filtro são queries. E aí a partir disso aqui, a gente tem esse aqui, como query strings.

**[00:49:08]** offset your limit. Aí a gente consegue fazer esse tipo de coisa. Aí o Jordane fez uma pergunta aqui o seguinte, ao refatorar usando routers e annotators pra gente gestão de dependências, qual seria o impacto prático de pôr todas as dependências em um único módulo? Você diz criar um novo arquivo onde só vai ter dependências? É isso que você quer dizer, Jordane, só pra eu entender aqui.

**[00:49:36]** Se offset limit forem negativos em filter users. Então, essa é uma coisa que a gente pode mexer aqui, né? Porque como a gente trouxe pra cá, a gente poderia usar um paedente que isso não tá na aula, mas eu adoraria adicionar isso na aula. Então, essa é uma boa pergunta aqui. Deixa eu fazer um pedido pra vocês. Quem tiver aqui que tiver mais intimidade lá com o repositório, abre o maixo.

**[00:50:06]** para eu colocar isso no material de texto, porque isso é super importante, eu não tinha pensado nisso. Aqui dentro do paedente, a gente tem um campo chamado Field. Field é campo, né? E aí você poderia falar o seguinte aqui, olha. Para garantir que o offset não seja negativo, você pode passar o Filter aqui, do Field, aí você pode falar que é o Greater Equal, né?

**[00:50:39]** Então é maior ou igual a zero. E aí você limita, né? E aí você pode passar o default aqui. Pera aí que ele... default zero. Olha que massa! E aí você poderia fazer isso para o de baixo também. Deixa eu mostrar para vocês como é que isso aqui ficou. Ó, minimum zero. Está vendo aqui? Ele muda. A gente poderia fazer para o de baixo também. Isso aqui. Aí você pode ir para lá, o default é 10. E aí se a gente rodar F5 de novo...

**[00:51:16]** Aí ele coloca aqui como o mínimo um zero. É uma coisa, isso não tava no curso, não sei por que eu não coloquei isso. Mas... Obrigado por levantar essa bola, Jordani. Alguém pode abrir a Ixu? Só me responde aí, eu vou abrir só pra eu saber. Se não, depois eu anoto aqui. E aí você pode fazer esse tipo de coisa aqui, dentro dos fields. Isso serve pra qualquer field, né, na real? Você poderia usar isso para identificar de maneira geral, em qualquer lugar que você quisesse. Massa?

**[00:51:51]** Abre lá já. Obrigado, Wanderlei. Valeu, mano. Demais. Brigadão. Demais. Aí a gente pode fazer isso aqui. E aí você tem agora esse filter page query aqui. Ah, e se eu quisesse fazer esse filter ficar lá em cima? Você poderia colocar ele lá em cima também. Aí é uma questão de gosto, né? Saca? As coisas vão funcionando da maneira como a gente quiser. Massa? Então, a gente junta, né? O modelo do Piedantic.

**[00:52:22]** E aí, o legal é que tipo assim, ah, num próximo filter, por exemplo, sei lá, todos os filters têm a limit offset. Aí você fala, ah, eu quero filtrar por name, né, filter name. Fala, name. Mas aí você pode herdar ele daqui depois, né. Então, é um filter page. Então, você pode filtrar por isso e isso, e name, que é uma string. Saca? Então, você consegue expandindo esse campo de quer strings.

**[00:52:52]** Isso aqui é lindo, essa é uma coisa que entrou depois da versão do curso do ano passado, mas é muito legal, é muito prático isso, muito útil. Então a gente viu aqui no Swagger como isso funciona. Legal, a quarta parte que a gente tem que fazer aqui é mover as constantes para variáveis de ambiente. A gente tinha aquela coisa que ficou lá no nosso security, deixa eu pegar aqui.

**[00:53:17]** lá no nosso security, ficaram algumas coisas aqui, como secret key, algoritmo e access token. Então, a gente vai tirar isso daqui e vai levar lá para o nosso settings, aquela classe zona que a gente tinha aqui, settings. Então, basicamente, o que a gente precisa fazer é trazer para cá. Então, vamos supor, isso aqui é uma string, secret key, é uma string.

**[00:53:54]** Pera aí que eu dei o autocomplete aqui sem querer. O algoritmo também é uma string, you get access token, access token experiments, é um inteiro. Aí você pode deixar esses valores de foo aqui, mas a ideia, eu preferia que a gente colocasse isso no arquivo .env. Então, aquele arquivo que a gente criou para colocar os dados do banco de dados, a gente pode vir aqui e colocar todas essas variáveis aqui. Então, vamos lá.

**[00:54:23]** Secret Key. Então, o algoritmo, eu vou deixar como HS256 mesmo, você não precisa de aspas aqui. Eu coloco, porque por uma questão de costume, algumas vezes dá problema de encode e tudo mais, aí a aspa ajuda isso aqui, né? Então, a inspiração em 30 minutos, aí fica legal, porque você pode trocar o tempo de inspiração sem ter que mudar o código da aplicação, isso ajuda muito, né?

**[00:54:52]** E aí é Secret Key. Vocês lembram como que já era Secret Key? Uma chave secreta aqui, pra gente não deixar esse Your Secret Key aqui, a gente poderia chamar o Python, né? Importar os secrets, né? Então importe Secrets. E aí dos Secrets, a gente chama o Token X, e a gente pode criar um token do tamanho que a gente quiser, sei lá. O padrão é 32, né?

**[00:55:21]** E vamos colocar esse Tolkien na nossa aplicação, e aí ele deixa de ser essa coisa aqui, né? Pronto. Sei que minha cara tá na frente, mas é isso aqui, então você pode gerar o seu Tolkien, a gente conversou sobre isso na aula passada aqui. E aí fica mais simplão, né? Aí eu não quero deixar nenhum valor de foco aqui, a gente sempre define tudo na variável de ambiente. Só que isso vai quebrar a nossa aplicação, né? Porque a gente não tá usando settings lá, né? Se a gente...

**[00:55:57]** Para a aplicação e tentar rodar ela de novo aqui, você vai ver que não vai funcionar, né? Então, falta que esse settings seja importado aqui e a gente comece a usar as variáveis de ambiente aqui. Trazemos tudo para cá, para essa classe maravilhosa. E aí, colocamos o arquivo Envy. Tudo que a gente precisa fazer lá no Security é importar, né? Os settings, né? Então, From, FastAPI0, import settings, import settings.

**[00:56:31]** A gente define a variável settings, eu vou passar ela aqui como uma constante aqui do código mesmo, settings, settings. E aí a gente vai chamando todo mundo que precisa aqui, né? Então a gente já tem os settings colocados, então settings.accessToken, settings.secretKey, settings.algoritmo. Aí ficou grande demais, beleza, a gente quebra pra ficar bonitinho.

**[00:57:01]** Aqui a gente tem o Secret Key de novo, então settings.secretkey, settings.algoritmo. Quebra aqui pra ficar bonitinho de novo. Eu acho que foi, né? Todos os lugares que precisava ter isso aqui estão aqui, né? Aí aqui ficou o Fast 0, né? Mas é Fast API 0. É o nome que a gente definiu. Aí esse erro sempre fica dando aqui, ah, falta essas... Tudo bem. O Linter não sabe lidar muito bem com o Python de settings. Então, se tudo deu certo aqui, né?

**[00:57:35]** Em teoria, esse shell aqui, do Fast API sempre quebra o meu buffer, eu não sei porquê. Então vamos lá, Tasking run, ou com polo entre ou com tal, legal. Leu aqui, significa que ele conseguiu carregar tudo, em teoria. Vamos ver o que está acontecendo aqui, vamos lá, mandar um post aqui, só para ver se ele cria, gera as coisas para a gente. Então vai ser esse aqui, sei lá.

**[00:58:13]** Teste, teste, teste. Legal. Aí o email é teste-arroba-example. Vamos tentar logar aqui para a gente ver o que acontece. Então teste-arroba-example, teste. Autorize, legal, logou, deu tudo certinho, o que significa que ele pegou as variáveis do lugar certo e está tudo massa. Vamos dar um get para ver todo mundo aqui. Try it out of set limit execute.

**[00:58:45]** Legal, tá todo mundo aqui. Significa que ele conseguiu pegar as variáveis de ambiente e ficou tudo maravilhoso. Legal, olha que lindo. Tudo funcionando direitinho. Aí a gente precisa executar os testes. Não sei se está tudo funcionando. Task test. Olha aqui. Mas ele está falando só que faltou uma linha em branco aqui. Por definição, sempre se pula duas linhas. Pronto. Task test.

**[00:59:24]** quebrou tudo. Ele quebrou na fixture. Quando ele tenta executar o test security, ele vai falar que vai tentar dar um import e tal, mas ele tenta importar lá do fast security o algoritmo e a secret key. Só que elas não existem no arquivo de teste. Porque a gente refatorou isso para seu setting. Então a gente vai ter que ir lá onde a gente faz isso aqui, que é no security.

**[00:59:55]** Então vamos lá, teste, teste security. Aí aqui ó, o algoritmo issecret key não existem mais, né? Então a gente importa lá do security. Então from, fash API 0.settings, importing settings.

**[01:00:17]** Aí você poderia chamar os settings aqui, você poderia definir uma fixture pra usar esses settings, você poderia importar os settings que já tá funcionando lá também, saca? É uma questão muito subjetiva aqui, a forma como você vai fazer isso. Por padrão, eu vou usar o mesmo settings que tá aqui lá, só pra ficar mais simples de fazer aqui. Mas uma coisa interessante que poderia acontecer aqui é a gente usar o...

**[01:00:49]** os settings, como uma fixture, que é uma coisa que a gente pode fazer depois para dar uma melhorada nisso aqui. Mas vamos rodar só para a gente ver se está funcionando, ver se está tudo certo. Legal, passou tudo. Lindo! Aí agora fica aquela pergunta para vocês aqui. O que vocês acham? Ficou mais interessante esse negócio? Ficou mais bonitinho, mais bem organizado? A gente poderia criar um conf-test aqui para os settings.

**[01:01:25]** Mas eu quero saber de vocês, vocês acharam dessa organização? Ficou mais organizado? Vocês gostaram mais? Então vamos lá, PyTest.fiction, a gente vai criar um, sei lá, settings. Aí os settings não precisa de nada, a gente só precisa importar, né? Então from FastAPI0.settings import settings. Aí a gente simplesmente retorna settings. Abre fast, aqui. Aí a gente bota isso aqui.

**[01:02:01]** Lá no topo, Fast API zero, Secure it, Settings. Vamos pegar aqui agora, lá no Test Secure it, a gente deixa de importar esses settings e passa ele como fixture agora. Settings. A gente não fica importando coisas declaradas de algum lugar. De novo, cometi o mesmo erro aqui, deixei ali em branco, lá embaixo. Faltou um Enter aqui. Pronto.

**[01:02:37]** Rodou, task test. Tá tudo funcionando. O que é uma coisa interessante que poderia ser feita aqui, né? Tipo assim, se você precisar manipular os settings de alguma forma, você pode trocar essa variável aqui no futuro. Mas aí fica a critério, né? Tipo assim, ah, tem uns settings que eu gostaria de mudar, né? Sei lá, eu quero testar que isso aqui seja de 5 minutos, em vez de 30. Aí você pode alterar esses settings aqui, né?

**[01:03:05]** Aí você pode falar, sei lá, duração dos settings, sei lá, espira em 10 e não em 30, sabe? Então isso permite uma certa flexibilidade aqui. Mas aí é contigo, né? A forma como você pensa, sabe? Por padrão, a gente só vai deixar aqui pra não importar de dentro do arquivo os settings que foi definido dentro de outro arquivo e tal, só pra ficar um pouquinho mais organizado. Mas em teoria, isso aqui.

**[01:03:34]** Essa é a nossa aplicaçãozinha. Ficou bem mais simplório, bem menorzinho as coisas cada uma no seu lugar e tudo mais. Não tem nenhum mistério. A gente rodou os testes, está tudo funcionando e tudo mais. A gente já acabou hoje. Mas a ideia é o seguinte, eu queria, essa aula é mais curtinha mesmo, porque a partir da próxima aula vai ser pancada.

**[01:04:03]** Então, eu queria tirar uns minutos pra gente conversar, pra tirar dúvidas, pra ver se vocês estão precisando de alguma coisa. Se vocês precisam de algo, essa aula é mais curtinha propositalmente pra isso. Porém, ainda tem alguns recados que eu preciso dar, mas eu quero dúvidas, eu quero entender de vocês, se tem alguma coisa que vocês gostariam de saber de dentro do contexto de tudo. Pode ser dúvidas de aulas passadas agora. Bom, uma coisa que a gente tem aqui é o quiz.

**[01:04:31]** Não esqueçam de responder o quiz, porque tem muitas coisas hoje, né? É annotator, é halter, é fixture, não sei o que, é form, é querestring, sabe? É um monte de coisa, então dá uma olhada nesse esquema. E essa aula aqui, ela só tem um exercício, né? Cadê? Aqui.

**[01:04:59]** que é para migrar os endpoints e testes criados nos exercícios anteriores para o local correto na estrutura da aplicação. Durante as coisas a gente foi criando a gente foi criando várias coisas então a gente criou vários outros endpoints vários outros testes a gente foi mexendo e futricando nas coisas ali atrás. Então quero que vocês migrem as coisas que foram criadas para esse novo formato.

**[01:05:34]** Vou dar o comit aqui, vamos lá. Só pra quem quiser pegar isso aqui do meu rap, pode pegar, porque tá um pouco diferente dos slides aqui, né? Porque a gente sempre vai incrementando coisas diferentes, né? Vou dar um get-punch. E aí, agora, eu tenho que fazer um pedido por obsequio aqui pra vocês. Da mesma forma que a gente tinha feito, lembra que eu falei, tipo assim, pô, pra assistir a próxima aula, lá na aula 3, eu falei, assistam a live sobre...

**[01:06:06]** sobre as que ele alqueme. Aqui eu gostaria que vocês parassem para assistir essa live, sei lá, no final de semana, porque o entendimento da coisa que tem aqui é muito importante. Que é essa aula aqui de Requestes Acíncronos, né? Na próxima aula, a gente vai transformar o projeto em assim. E...

**[01:06:37]** Eu sei que pra nem todo mundo, esse termo de acincronismo, né, concorrência, coisas rolando em background, é uma coisa muito comum, né? Muito padrão. E por conta disso, a gente tem isso aqui, né? Essa live. A gente tem uma série inteira no canal sobre isso, mas eu tive que escolher um material simples, né? Pra dar pra vocês aqui. Corroutinas. É uma playlist inteira sobre corroutinas. Deixa eu ver se eu acho aqui. Eu tô com o cabelo verde. Deve ser fácil de achar aqui.

**[01:07:10]** aqui então tem isso aqui que dá uma ideia sobre corrotinas mas são quatro lives é muito comprido se tiver um tempo pode assistir quanto mais melhor mas se der um tempo assiste essa live duzentos e trinta e quatro aqui

**[01:07:33]** Ela tipo vai dar o insumo do que acontece, de como é o event loop, a gente vai discutir mais, mas é legal que vocês já sigam, mas, sabe, mais preparados para pegar aqui a coisa e olhar e falar, nossa, que agora é o event loop, aqui é o request acíncrono. Só para dar uma olhada para isso aqui. Vai ser muito importante dar uma olhada nisso. O Lucas falou o seguinte, pelo que eu entendi, a refatoração organização é de acordo com o gosto mesmo. Pode deixar mega separado, tudo junto, sim, sim.

**[01:08:07]** É... É muito pessoal, né, a forma. Tanto que eu falei lá no começo da aula lá, mas e se eu quisesse fazer isso aqui usando, sei lá, use case do domain driven design ou, sei lá, usando camada de serviços lá do Fowler, a gente poderia juntar essas coisas aqui. Aí fica muito a critério de cada pessoa. Alguém poderia falar, mas eu gostaria de pegar um negócio e... Saca.

**[01:08:36]** criar uma classe que traz essas coisas aqui pra dentro, eu poderia fazer isso? Pode, né? São coisas muito abertas aqui, né? Porque, por exemplo, eu queria que isso aqui fosse uma camada de serviço, porque eu não gosto, já vieram falar isso aqui nessas aulas, tipo assim, ah, eu não gosto de código escrito dentro do Endpoint, porque isso aí fere e não sei o que lá. Saca.

**[01:09:04]** O fériu é esse do sólid, tal, tal, tal. Você poderia criar uma classe, injetar essa classe que, quando depende, saca, é uma questão muito de gosto aqui. Então, cada pessoa tem sua forma de ver. Aí a Paloma falou o seguinte aqui. Essa parte de assim que eu fui cobrada em um processo seletivo, e como eu não tenho experiência, tive muita dificuldade em explicar esse ambiente no mundo real. Bom, eu recomendo, Paloma, dar uma olhada na série.

**[01:09:35]** que eu mandei aqui tem bastante coisa interessante sobre esse assunto aqui a série dos geradores e uma introdução uma introdução a corrotinas aqui é um pouco mais antigo mas é tudo muito atual ainda dá pra entender bem os pormenores do que acontece por baixo dos planos aqui criar uma classe pra imports rola

**[01:10:01]** Você quer criar uma classe e isolar os importos dentro dessa classe? Não faz muito sentido isso. Se for isso, pode ser que eu tenha entendido errado. Mas aí, voltando aqui no esquema de decamada de serviço, se você quiser, você poderia criar uma classe e botar um GetUser, um CreateUser. Você bota todo esse código lá dentro, injeta a classe aqui e chama só o método. É uma forma de ver isso aqui. Eu devia achar muito bizarro.

**[01:10:33]** A galera montar uma classe para ter só um método execute. Então é o que acontece. Eu não queria ir por esse lado, então foi por isso que eu não fiz esse esquema. Mas para quem tem curiosidade sobre isso, vou deixar uma referência aqui. CosmicPython.com Existe um livro de Python especial para esse tipo de coisa, para quem quiser ver essas patterns arquiteturais e tudo mais.

**[01:11:00]** que é o Cosmic Python, ou esse livro aqui, Architectural Patterns with Python, ou Patterns, padrões de arquitetura com Python. Se você vier aqui, read it for free on the site, você pode ler de graça o livro inteiro, ele é aberto, está aqui no site. E aqui no começo, ele começa a falar nesse, como é que eu domino o modelo, como é que eu vou fazer isso aqui?

**[01:11:27]** para quebrar, se eu quisesse fazer esse tipo de arquitetura mais rebuscada e tudo mais, ele dá uma visão sobre tudo, sobre tudo aqui. Em algum lugar ele fala sobre layers aqui, aqui ó. Esse livro é com um flask, mas dá para entender tudo bonitinho aqui. Ele vai falar sobre como criar as camadas e tudo mais. Eu acho que é na introdução que ele coloca aqui o modelo, aqui ó, assim, a separação por camadas aqui, né, o layering.

**[01:11:57]** que é para quem segue esses patterns empresariais, tem tudo aqui, então como é que se divide? Aqui vai ficar só uma apresentação, aqui a gente vai criar uma camada de serviço para lidar com isso aqui, o repositório para lidar com o banco de dados, então se vocês quiserem dar uma olhada sobre isso aqui, como fazer uma refatoração baseada nesse mundo mais Morton Fowler, mais baseado em domínios, tem bastante coisa aqui.

**[01:12:21]** Inclusive, esse assunto, arquitetura encamada, o layering, poderia virar uma live de Python, e se alguém quiser falar sobre isso aqui, a gente pode marcar uma live sobre isso. Então, se alguém quiser abrir lá em um maixo, pode falar uma live sobre layering, a gente fala...

**[01:12:42]** sobre esse esquema. Mas, basicamente, ele explica muitas coisas do que a gente viu aqui, né? Por exemplo, ah, como é que funciona o Unit of Work Pattern, que o SQL Alchemy já implementa por padrão, mas ele cria uma abstração em cima e tudo mais. Então, para quem quiser ir para esse lado, mais Enterprise Patterns tem tudo nesse livro aqui. É com Flask, mas é muito parecido. As implementações são muito interessantes na forma como isso aqui funciona.

**[01:13:10]** Então, legal, fica isso aqui para a próxima aula, respondo um quiz e os exercícios e liberando muito mais cedo hoje, não é? Achei que... que eu tenha mais perguntas aqui sobre esses assuntos, mas quem tiver dúvidas pode mandar lá no grupo, eu estou pronto para responder, tem uma dúvida que eu tenho lá que eu não respondi ainda, e a gente se vê na semana que vem para essa coisa de Assimq. Então, lembra, fazer um combinado com vocês aqui.

**[01:13:42]** Estamos indo embora muito mais cedo, para dar tempo de assistir um pedaço da live de HTPX com assim, quem? Pega para dar uma olhada depois. Bom, eu vou ficando por aqui. Um beijo para vocês. Ó, a gente se vê na terça-feira agora, para a gente futricar um pouco mais fundo nesse projeto e quebrar a cabeça. Beijinho e até mais. Tchau.

