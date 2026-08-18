# Transcrição da Aula: aula-11.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:06]** Olá, pessoas, boas-vindas. É mais uma aula do nosso curso de fastidia IPI. Eu sou do Nossauro. Boa noite para quem está aqui na live. Bom dia ou boa tarde para quem estiver vendo isso depois, porque na internet não tem horário. E eu estou falando assim, tudo rapidinho, né? Vocês me darem um feedback, né? Eu preciso saber se vocês estão me ouvindo, se vocês estão me vendo, às vezes eu fico falando sozinho, por longos minutos, antes da gente começar a aula. Bom, eu vou dar aqui um...

**[00:00:31]** uma palhinha do que a gente vai ver hoje, mas eu conto com a resposta de vocês aqui pra gente saber se vai dar tudo certo, se vocês estão me ouvindo, me vendo e tal. Bom, hoje, basicamente, a gente vai fazer uma parte importante da nossa aplicação, que é criar um container da aplicação, né? Opa, imagem audio OK. Muito obrigado. Então é isso. Então hoje a gente vai criar um container da nossa aplicação.

**[00:00:59]** Eu coloquei aqui como Docker, porque a gente vai usar o Docker como ferramenta para a criação de containers, mas existem outras ferramentas e tudo mais. E, por fim, a gente vai introduzir o Postgrease, né? Eu acho que a gente vai fazer na ordem ao contrário, né? Primeiro vem o Postgrease, depois o meu Docker, o Docker a gente vai usar para subir o Postgrease, vai dar uma confusãozinha, mas vamos lá. E a ideia é essa, o Postgrease é um banco de dados...

**[00:01:25]** Como eu posso dizer, um banco de dados parrudo para a gente botar em produção e é isso que a gente vai fazer hoje. Então, a gente vai entender como é que a gente cria uma imagem docker da nossa própria aplicação, ou seja, como é que a gente cria um pedacinho do nosso, esse código que a gente tem, a gente cria uma forma em que ele seja compartilhável para a gente poder subir na plataforma e rodar em produção.

**[00:01:49]** A gente vai aprender a rodar a aplicação com isso, introduzi o Docker Compose, que é uma forma de...

**[00:01:56]** agrupar vários containers e fazer com que eles subam todos de uma vez ou sejam derrubados. Então a gente vai criar nosso Dockerfile e entender um pouquinho desses benefícios e tudo, mas a gente vai mexer com um pouco de testes hoje. A aula de hoje tem pouquíssimo código assim, a gente vai mexer em um lugar muito pontual do código hoje, mas basicamente toda a nossa preocupação é com essa parte de infraestrutura. Então eu vou fazer uma pergunta para vocês assim.

**[00:02:22]** Vocês já estão habituados com essa coisa de trabalhar com containers? Se nunca trabalhando com containers, me respondam aí. E a ideia é que a gente converse hoje sobre esse assunto. Tem um aula um pouco mais pontual de entender as dúvidas de vocês, tentar explicar isso da forma mais...

**[00:02:41]** concreta possível de uma forma um pouco mais palpável, porque a ideia padrão é que a gente não mexe com código hoje, só arrumar uma coisinha ou outra para poder rodar dentro do container. Então, sintam-se à vontade para conversar comigo, vamos trocando ideia porque o objetivo dessa aula é hoje. O objetivo dessa aula hoje é essa parte de implantação, né? Então, vamos lá! Eu quero...

**[00:03:07]** Habituado é muita coisa, eu uso na marra, todo mundo usa isso aqui no ódio às vezes, grande parte das pessoas. Então, vamos lá, a gente vai conversar primeiro, esse primeiro ponto sobre o Docker e sobre o Postgres. Então, legal, o Docker é uma ferramenta para criar containers. E aí você pode estar se perguntando, porra, beleza, o que é um container? Porque um container pode ser muitas coisas.

**[00:03:33]** Um container pode ser aquela coisa que a gente transporta no navio, saca, que você bota no navio e traz, sei lá, faz sua cumprinha na China, compra no Aliexpress e eles botam dentro do container, esse container vem no navio, a ideia do container.

**[00:03:52]** É essa. Tipo assim, isso te chama container, a gente faz esse tipo de abstração pra explicar isso aqui. Mas basicamente a ideia é você ter uma caixa, uma capa que protege tudo que você tem na sua aplicação de forma isolada. Sabe quando a gente lida com...

**[00:04:14]** com o VNV do Python. Já que tem várias pessoas que nunca trabalharam, eu vou me permitir explicar um pouquinho mais sobre isso aqui. Então, vamos pôr. A gente não trabalha de uma forma mais ou menos assim, a gente tem o sistema operacional, né? Deixa eu colocar uma corzinha mais bonitinha aqui, vai. A gente tem o sistema operacional, né? E se tiver pequeno, vocês me avisam. Eu posso ir aumentando aqui.

**[00:04:44]** Então a gente tem essa parte que é o nosso próprio sistema operacional, aí dentro do nosso sistema operacional a gente tem as nossas aplicações, né? E aqui dentro dessa camadinha de aplicações, né? Aqui estão rodando as coisas que a gente costuma rodar normalmente, né? Sei lá. O editor de texto, pera aí que eu queria botar espaço. Então a gente tem o nosso editor de texto, fui trollado aqui, vai. Editor, a gente tem o Python instalado, a gente tem várias outras coisinhas, né? Dentro dessa nossa aplicação.

**[00:05:22]** dentro do nosso computador, dentro dessa coisa instalada aqui nessa camada de aplicação. Você tem o seu navegador que você está me assistindo agora e vários outros tipos de coisa. Quando a gente está criando uma aplicação, tipo assim, uma aplicação Python normal que a gente usa, eu vou chamar ela de app aqui, quando a gente cria um aplicativo Python, geralmente o que a gente está fazendo, a gente está usando o Python que a gente já tem aqui embaixo, o nosso app.

**[00:05:53]** Não é assim, a gente usa o Python que tem instalado na máquina, geralmente a gente faz isso. Aí a gente tem uma outra camada aqui dentro desse pedacinho, onde estão as aplicações e tudo mais, que são as bibliotecas do sistema, que elas podem ou não estar no mesmo nível, mas é só para a gente ter uma abstração aqui para poder olhar isso. Então a gente tem as bibliotecas.

**[00:06:21]** do sistema e todas essas outras coisas que a gente instala, certo? Geralmente, quando a gente está fazendo uma aplicação Python, a gente evita, não é? Usar as bibliotecas do sistema, não é? Lembra que a gente evita fazer aquelas instalações globais, muito malucas? Que a gente geralmente faz? Então, a gente cria um vmv, não é? O vmv é uma forma de isolar as bibliotecas Python, não é? Então, a gente cria umas próprias bibliotequinhas aqui.

**[00:06:50]** que a gente chama daqui depende delas, né? Aí a gente chama isso aqui de vmv, né? Que é um lugar certinho pra gente poder usar essas coisas. E aí quando a gente usa, a gente modifica o Python pra poder usar essas coisas. A gente não usa as bibliotecas do sistema, certo? Tá fazendo sentido isso aqui que eu tô falando com vocês? E aqui é o nosso app.py, né? App.py, só pra ficar claro, né, do que a gente tá falando.

**[00:07:19]** Então, por exemplo, a gente usa o Poetry aqui dentro do nosso curso para instalar as bibliotecas, a gente isola isso no ambiente virtual, às vezes a gente usa o próprio instalador do Poetry, que separa isso aqui também num ambiente virtual, a gente coloca isso dentro da aplicação, ele não depende exatamente desse Python, a gente usa esse aqui.

**[00:07:46]** E aí, basicamente, a gente faz uma coisa meio isolada, mas a gente roda em cima de toda essa camada do sistema operacional, das bibliotecas e tudo mais. Basicamente, a ideia de um container, quando a gente fala de docker e tudo mais, é que a gente consiga isolar tudo isso aqui. Eu vou criar até contracinhos aqui. A gente isole tudo isso aqui, nessa coisa que a gente vai chamar de container.

**[00:08:18]** Ou seja, a gente ainda tem os recursos do sistema operacional, mas a gente coloca tudo dentro de uma caixinha. Então, por exemplo, a gente instala o Python, a gente instala outras bibliotecas, a gente instala, sabe tudo o que a gente precisar num lugar isolado. E é isso aqui, depois no fim, fica como se fosse uma caixinha assim. E aí eu posso entregar isso aqui para a infraestrutura ou para a parte do...

**[00:08:45]** do DevOps ou as gente mesmo sobe isso aqui e aí dentro dessa caixinha estão todas as coisas, todas as nossas bibliotecas, todas as nossas aplicações, o nosso aplicativo, o nosso virtual envy, tudo está aqui e tudo é compartilhado de uma forma simples. E qual que é a ideia por trás disso aqui? A ideia por trás disso desses containers é que eu possa criar esse pacote

**[00:09:14]** E aí, por exemplo, vamos supor que a Julia é o servidor aqui, né? Então, a gente pega esse pacotinho que a gente tem aqui, sobe lá para o servidor da Julia, e aí ele fica rodando em produção.

**[00:09:27]** Saca? Então, porque como é que a gente vai rodar? Eu não quero que isso rode dentro de casa, dentro do meu PC, porque eu preciso garantir que o meu PC vai ficar ligado 24 horas por dia, que eu tenho um gerador de energia, que eu tenho um link sinistro com a internet, o IP fixo e vários outros tipos de coisas. Obviamente, tem soluções para rodar em casa, mas a ideia do docker de uma forma geral ou de qualquer estrutura de container é que a gente consiga fazer isso aqui e compartilhar.

**[00:09:53]** Todas as nossas dependências, as aplicações das quais a nossa aplicação depende, o nosso Python, o nosso ambiente virtual, o nosso código, tudo isso, e mandar para a produção. Ou compartilhar com outras pessoas, isso facilita também o desenvolvimento. Então, por exemplo, eu estou desenvolvendo junto com o Ruzin aqui, né? E aí a gente fica trocando essa ideia, e aí a gente tem um arquivo de container único.

**[00:10:17]** e a gente pode simular a mesma coisa, ou seja, eu estou rodando isso aqui no Linux, o Husny está rodando no Windows, o Luis está rodando no Mac, a Julia no FreeBSD e a gente compartilha esse mesmo contenda e ele se comporta da mesma forma em todos os sistemas operacionais.

**[00:10:38]** faz sentido isso então a gente tira essa diferença de estar pensando pô estou desenvolvendo na minha máquina e na minha máquina funciona e aí quando vai é exatamente isso aí que eu tenho falou ele falou junto comigo na minha máquina está funcionando mas quando vai para o servidor não funciona porque lá às vezes não tem as mesmas aplicações não tem as mesmas bibliotecas não tem a mesma versão do python saca esse tipo de coisa o container evita e faz com que a gente

**[00:11:07]** compartilhe isso. Aí o germano falou, chegou a hora de papo de empresa grande. Não! Isso aqui pode simplificar o ambiente de desenvolvimento, né? A gente vai ver aqui como vai ficar mais simples. Então, basicamente, essa é a ideia do container, né? Ele isola as dependências, mas não são as dependências das bibliotecas do Python, né? São as dependências gerais do sistema. Então, a gente compartilha o sistema operacional embaixo, né? Essa camadinha aqui, né?

**[00:11:38]** do sistema operacional ou kernel do sistema, mas a gente roda outras aplicações, outras bibliotecas de forma isolada, para que a gente consiga reproduzir o mesmo comportamento em qualquer lugar que a gente esteja. Então, essa é a ideia. Aí, a gente está aqui usando Docker, e eu particularmente, na minha máquina, nas minhas coisas, eu não uso Docker. Eu costumo usar outras ferramentas de containers, e elas existem, né? Tem o container de...

**[00:12:07]** que lida com a interface do Nerd CTL. A gente tem o Podman, que é uma outra arquitetura que também é Open Source. A gente tem o LXC, que são containers nativos do Linux e tudo mais. Aí a Paloma fez uma pergunta. Pergunta, o container está isolado do SEO da máquina, mas o container roda em qualquer outro SEO. Então, geralmente...

**[00:12:35]** A gente instala uma uma camada de compatibilidade, né? E na grande maioria dos casos, os containers que a gente cria tipo com Docker, com Podmer, eles são baseados em Linux. E aí o Windows tem um subsistema para lidar com coisas do Linux.

**[00:12:53]** E no Mac também existe esse tipo de coisa. Então essa camada de compatibilidade que a gente instala faz com que todo mundo rode no mesmo negócio, que é o que a gente chama de demon, né? Tem algumas coisas que são demon, les e tal, mas por exemplo, em todo lugar que a gente instala o docker, porque o docker que a gente está usando, o contêiner vai se comportar da mesma forma.

**[00:13:13]** As vezes tem alguns problemas de arquitetura, por exemplo, você tem um Mac com um processador silicon, né? M1, M2, M3, e às vezes você não tem suporte a 64 bits, tem alguns problemas de incompatibilidade, mas no grande, assim, no grosso das ocasiões, tipo assim, 90% das coisas vão ser solucionadas instalando essa camadinha de compatibilidade, que é a própria aplicação, o próprio docker, né?

**[00:13:38]** aí bom eu não vou instalar o docker aqui porque a gente precisaria estar com todos os sistemas operacionais aqui funcionando e tudo mais aí caso você não tem o docker instalado na sua máquina eu separei os principais aqui aí você pode clicar nesse aqui eu tenho pra windows aí tem o link aí você pode usar ele com um wsl não sei se seu windows tem wsl ou ser hyper v ai no linux

**[00:14:08]** Depende da distribuição, tem no app ou não. E no Mac também tem um link aqui. Aí você tem que escolher se é Intel ou se é Silicon. Então tem muitas variáveis de instalação aqui. Então você vem aqui, dá uma clicada, instala aí no seu sistema. E é tipo assim, tirando essa parte de ter que instalar.

**[00:14:33]** E tudo mais, se não for no Linux vai ser Next, Next, Next, Next. E no Linux tem tutoriais completos para fazer isso, então quem usa Linux se dá bem com essas coisas de terminal e tal. Aí o Feito falou que eu gosto de desenvolver dentro do container. Eu já não gosto muito de desenvolver dentro do container, mas é uma coisa. Então, é basicamente esse esquema aqui. Então a gente isola as dependências. Paloma, fez sentido isso?

**[00:15:01]** Não sei se fez sentido essa coisa que a gente conversou aqui, que a gente vai ter uma camadinha que é a instalação dessa coisa, dessa ferramenta, do Docker, do Podman, do ContainerD, do LXC, e aí a partir dali a gente consegue reproduzir todo mundo no mesmo container. Aí, como a gente não vai se aprofundar nisso, eu dei uma explicação bem superficial aqui por cima, eu deixei aqui, linkado, uma playlist da Linux Tips, o Jeff.

**[00:15:31]** A pessoa super, a gente fina. Ele tem um curso inteiro, assim, uma... uma playlist muito grande aqui, gigantesca, sobre Docker e tudo mais. Então, quem tiver mais interesse em se aprofundar aqui, é que a gente só vai usar hoje o Docker. Então, tem essa playlist de graça, pode ir lá conhecer, já é versão de gente boa pra caramba. Ele faz um conteúdo muito parecido com a gente aqui, de... de graça e tudo mais. Então, é isso. Massa? Então, essa é a ideia do Docker.

**[00:16:04]** E aí beleza, a gente vai também introduzir dentro dessa aula o Postgres SQL. E o Postgres é um banco de dados, a gente tá usando o SQLite pra fazer tudo que a gente fez até agora. O SQLite não é ruim, ele é ótimo, mas quando a gente precisa escalar, e aqui eu tô falando de escalas grandes, a nossa aplicação tá rolando e tem, sei lá, 100 pessoas conectadas, 200 pessoas conectadas ao mesmo tempo, saca?

**[00:16:35]** E aí o SQLite, porque ele é um arquivo, ele não é feito para lidar com essa larga escala. Em um uso normal, a gente vai conseguir trabalhar com ele de boa, tanto que eu coloquei até aqui no próximo slide. Para os objetivos da nossa aplicação, que é uma coisa simples para a gente entender como funciona, a gente está desenvolvendo, colocando o banco, aprendendo o framework,

**[00:16:59]** Sei lá, a nossa aplicação vai ter 5 pessoas usando, sabe? Tipo assim, o SQ Lite vai dar conta disso. Mas o problema, obrigado Regis, ó, um beijo pra você. O problema é quando as coisas precisam escalar e ser concorrentes, sabe? De uma forma bem grande, assim, saca? Então vai ter 200 pessoas ao mesmo tempo. E aí eu preciso que rode dois bancos de dados ao mesmo tempo, sabe-se lá por quê? Então...

**[00:17:28]** A ideia é essa. Para funcionalidades mais avançadas, sabe coisas, malucas, o posto está aqui. Aí o Paulo falou, eu diria que o SQLite serve para teste, mas não para produção. Paulo, o SQLite serve sim para produção, ele tem vários usos muito interessantes em produção, mas quando você precisa escalar, ele não é a ferramenta certa. Massa?

**[00:17:51]** Então, dito isso, para o nosso contexto, Postgres faz tudo, o SQLite serviria, mas a gente vai usar o Postgres, porque eu quero levar vocês para o caso...

**[00:18:01]** maior, de produção, um caso real. No caso de ObserveSky Lite seria um arquivo e o Postgres seria uma aplicação com memória, é tudo isso. O Postgres é uma aplicação mesmo, assim, é um banco de dados bem robusto, ele é de código aberto, ou seja, ele é tão sinistro dos melhores do mundo, assim, e ele é open source, ele é de graça, ele funciona super bem, assim. Então, é muito massa.

**[00:18:33]** Aí o... O que ele me mandou aqui é o seguinte, se eu não me engano, costumo usar a SQ Lite no Android. Sim, não só no Android, sempre que você tem que armazenar dados do lado do cliente, que você precisa fazer essa sincronização, sabe? Pô, eu preciso de coisas aqui, tem um cache local para a gente poder trazer os dados, ou a gente precisa persistir dados para um momento para depois sincronizar com o servidor, o SQ Lite mata isso e ele é muito bom assim. Ele funciona muito bem.

**[00:19:02]** Só que ele não é feito para larga escala. Então, é por isso que a gente vai mudar para o Postgres de novo. Nossa aplicação suportaria rodar com SQLite. A gente vai subir o Postgres mais para uma perfumaria. Quero mostrar para vocês esse tipo de coisa. Então, legal. E aí, como é que a gente roda uma coisa aqui? Tipo assim, eu vou...

**[00:19:25]** É offline and first. Isso é muito importante. O sistema sempre pode ficar fora do ar. Principalmente se ele rodar do lado do cliente. Foi uma aplicação desktop, mobile, esse tipo de coisa. O SQLite funciona bem até em aplicações do web assembly. Saca, que você roda dentro do browser. Ele é lindo, mano, ele é lindo. Então, como é que a gente sobe uma imagem aqui? Basicamente, a gente vai dar um docker run. Simplone, simplone assim. Docker run. E aí você passa.

**[00:19:57]** o nome do container que a gente quer usar. Para a gente não ter que ficar com aquele negócio, tipo assim, pô, vamos instalar o Postgres na minha máquina, porque eu preciso fazer, e aí vai, volta, configura e sabe todo esse negócio, a gente vai usar o Docker, porque o Docker já está pronto. Lembra, a gente traz essa caixinha para a nossa máquina. E aí o que a gente precisa fazer? Dockerrem Postgres. Só isso.

**[00:20:24]** E aí ele vai começar a rodar o Postgres na nossa máquina. Tem algumas outras coisas que a gente vai passar, mas só pra explicar isso aqui. Docker, Bram, Postgres.

**[00:20:37]** Vocês estão demais hoje, mas isso me ajuda muito, valeu demais pelos Superchats. Então, simplesmente, Docker, RAM, Postgres. Aí você está falando, beleza, Postgres é o nome da aplicação que a gente quer, mas de onde que isso vem, né? Então, existe uma plataforma por trás do Docker, que é o Docker Hub. E aí, qualquer uma dessas coisas que você precisar de aplicações externas que já vem pronta, a gente precisa rodar dentro...

**[00:21:05]** do nosso ambiente, a gente pode vir aqui e tem um monte de imagens, assim, um monte. Ó, por exemplo, o Nginx, por exemplo, que é um servidor web, a gente tem o próprio Python que a gente vai usar aqui, a gente tem um pôso, assim, tem um Reds, que é um broker, um banco de dados de cache no SQL, a gente tem um Node, o Apache, o MySQL, o Mongo, Raptmq, que é um sistema de mensageria, a gente tem do Go, MariaDB, né, que é o...

**[00:21:38]** sqlite, saca, WordPress, Ruby, outras linguagens, pô, tem um monte de coisas aqui. Então, você pode acessar aqui, vir aqui no Docker Hub, e procurar aqui a imagem que você quer. Por exemplo, eu quero rodar o Postgres. Então, Postgres. E aí, a gente tá aqui, ó, de preferência sobre as imagens oficiais. Aí, se você quiser clicar aqui em Oficial, aí você tem aqui. Às vezes, você quer verifier também, causa de alguma outra coisa, que não tenha uma imagem oficial.

**[00:22:13]** Massa, aí clicou aqui, a gente está aqui, ele vai falar quais são as versões que têm, quais são as coisas, tudo que está rolando aqui. Massa, então, o pôstro já está na versão 18 beta, né? A gente vai usar a versão 17 dentro dessa coisa aqui. Aí me corrigiram aqui que o MariaDB é o MySQL sem Oracle. Obrigado pela correção. Massa, faz sentido isso aqui? E aqui a gente pode pegar qualquer imagem que a gente tem aqui dentro.

**[00:22:58]** Legal, vamos usar o postgres. Fez sentido o que a gente falou? Vocês entenderam isso aqui? Da onde vem a imagem, o que a gente vai baixar e tudo mais? Só para a gente saber, continuar a aula aqui certinho, porque eu sei que às vezes você não tem, às vezes falta isso aqui.

**[00:23:26]** Então, enquanto isso, enquanto vocês me respondem, se está tudo certo, se a gente pode continuar aqui, eu vou responder essa pergunta da Paloma aqui. Opa, perdi aqui. A Paloma fez o seguinte, qual é a diferença entre container e imagem? Porque na minha cabeça, imagem é um script e o container é algo como um todo. O que que é isso? Então, vamos pensar o seguinte. Sabe quando a gente cria uma classe em Python? Deixa eu fazer isso aqui. Talvez fique claro. Sabe quando a gente cria uma classe? Class C.

**[00:24:00]** Isso aqui é a imagem, é a coisa, é a forma do bolo que a gente vai seguir. E a instância da classe quando a gente cria essa referência é o container. Faz sentido essa analogia? Então aqui a gente tem a forma como montar essa coisa, a imagem, tudo mais, e a instância. Tipo assim, quando o container está sendo executado, quando ele está em runtime, é o container.

**[00:24:35]** fora disso ele é a imagem, parado ele é a imagem rodando ele ao container. Faz sentido? Tipo assim, tem uma explicação muito mais técnica do que essa, mas eu estou tipo assim tentando me manter no simples, senão a gente se perde aqui. Então legal, então vamos lá. Docker, run, run é de rodar, né? Então roda a imagem e a gente quer a imagem do Postgres, né? Então Postgres. Aí a gente vê aqui que existem várias imagens do Postgres, mas aqui em cima está especificado.

**[00:25:06]** Postgres. Legal? O Postgres, se a gente ver aqui na documentação, você vai ver que ele tem algumas variáveis que a gente precisa passar para ele. Então, por exemplo, se eu for logar no banco de dados, eu preciso da senha do banco. Eu preciso de várias coisas, então eu preciso da senha do banco.

**[00:25:26]** do username do banco, o nome do banco de dados e tudo isso aqui. Então para cada uma dessas variáveis a gente tem que passar o parâmetro "-e", na hora de montar aqui. Aí de novo eu vou tirar aqui e eu vou quebrar aqui só para ficar simples de ler, mas não precisa, pode rodar tudo numa linha só.

**[00:25:44]** Então, aí a gente vai dar aqui o "-e", e aí o "-e", é de environment, né? É uma variável de ambiente. As mesmas que a gente coloca, tipo assim, no vmv, no .mv da nossa aplicação, a gente está passando esses para o .mv do container. Massa? Então, a gente tem todas essas variáveis aqui. Uma delas aqui que a gente quer é o user, né?

**[00:26:10]** Aí eu vou colocar um nome bem genérico aqui, só pra ficar simplão de ler. Então a gente tem aqui, o nome do usuário do nosso Postgres vai ser app-user. O nome do nosso DB vai ser app-db. Por quê? Porque eu tô com muita criatividade. A hora que eu fiz os slides eu tava muito criativo. E a gente vai passar a senha que vai ser app-password aqui. Legal, então a gente passou as variáveis que preencha o .env desse container quando ele estiver rodando.

**[00:26:43]** Aqui tem mais algumas coisas, tipo esse name. E aí o name aqui é o nome que a gente vai dar para esse container aqui. Ou seja, a gente está usando a imagem do Postgres, mas o container, quando ele estiver rodando, ele vai se chamar de AppDataBase. Ou seja, é o banco de dados da nossa aplicação. Então a gente vai subir ele aqui também. E aqui, por último, tem esse P. E aí, o que que é o P? O P é de porta.

**[00:27:15]** Lembra quando a gente sobe o nosso servidor, o UVCorn da nossa aplicação? Ele abre sempre a porta 8000 da nossa máquina. Então, significa que o nosso serviço, a nossa aplicação, roda na porta 8000. O Postgres, por padrão, roda nessa porta que a gente chama de 5, 4, 3, 2. É a porta padrão do Postgres. E aí, o que acontece que a gente tem essas duas coisas? 5, 4, 3, 2, 2.5, 4, 3, 2.

**[00:27:45]** A gente está dizendo que a porta que a aplicação abre lá dentro do container dessa coisa isolada vai estar no bind ou vai fazer um bind, ela vai corresponder à porta 5, 4, 3, 2 da minha máquina do localhost. Então, quando eu acessar a porta 5, 4, 3, 2 da minha máquina, eu vou estar acessando a porta 5, 4, 3, 2 do container.

**[00:28:15]** Fez sentido isso? Aí, por fim, a gente coloca o nome da imagem. A imagem é sempre a última coisa. Então, Postgres. Pronto. Subiu nossa aplicação aqui. Ele tá rodando um Postgres aqui. Aí, os arquivos. Quem é o dono dos arquivos é o Postgres, tal. Ele tá explicando aqui que ele leu as coisas. Subiu. A aplicação tá de pé. Tá rodando aqui. Super simples de levantar, né?

**[00:28:53]** Não tem nada de complicado. Aí ele tá falando, ele tá ouvindo na porta 5A32000, lembra? Do localhost, mas esse localhost lado contêiner. Aí a gente coloca as duas portas aqui pra combinarem aqui dentro. Simplão, juro, a gente rodou isso aqui, tá de pé o pôsigos na máquina, a gente não tem que instalar nada, não precisou rolar nada aqui dentro. Por exemplo, se a gente quisesse fazer isso aqui, ó, agora eu vou dar um Docker PS, né?

**[00:29:22]** que ele mostra o que está rodando. Não tem nada rodando. Massa, ou seja, como é que sai do contender, né? Contra o C, você consegue sair dele. Você pode dar ele no modo Detached, né? Que é com menos D. Aí ele não polui, né? A coisa aqui, mas depois a gente conversa sobre isso aqui. Então, o que vai rolar aqui? Se a gente pra pra desencargo de consciência, eu vou eu vou dar um rum na imagem do Python aqui.

**[00:29:53]** Só para vocês sacarem o que acontece. Então ele está baixando a imagem do Python, legal. Aí ele vai começar a executar o Python lá dentro dessa imagem, tudo certinho, tudo bonitinho. Você está dizendo que dentro do projeto você instalou um banco de dados Postgres? Não, eu estalei o banco de dados Postgres no ambiente. Tipo assim, lá dentro do container está rodando. Saca tem essa instância, esse container rodando e ele está dentro da minha máquina, mas ele não está dentro do meu projeto.

**[00:30:33]** Eu só rodei no terminal aqui pra executar. Aí você tá vendo, ele rodou a imagem do Python, não aconteceu nada. Por quê? Porque o Python não é uma coisa rodando e tudo mais, mas eu poderia fazer isso aqui, ó. Eu poderia falar que eu quero rodar o Python, sei lá, de qualquer forma aqui. A gente vai ver mais pra frente o que consegue. Nessa imagem do Python, precisa especificar a versão. Aqui, quando você não coloca a versão, ele pega sempre a última. Por exemplo, eu quero o Python, sei lá, três...

**[00:31:04]** .13, aí você bota esse dois pontos aqui, aí ele vai rodar a imagem 3.13 do Python. Massa? É isso aqui que acontece. Então é legal, aí quando a gente roda isso aqui, a gente criou um container aqui e tudo mais, e ele roda, ele tá falando, ó, eu não consigo rodar esse comando de novo, porque a gente já rodou esse comando e já existe esse update a base. Então se a gente der que um docker a container

**[00:31:38]** LS, ou seja, liste os containers, não existe nenhum container. Se a gente vier aqui e dá um image, LS, ele mostra aqui, ó, todos os containers que eu tenho instalado aqui na minha máquina. Então, eu tenho a última versão do Postgres, a versão 16 do Postgres, o Python na última versão, porque eu não coloquei tag, o Python 3.13, o Python 3.13 Slim e tá todo mundo aqui. Massa!

**[00:32:09]** Então, esses são as imagens que eu tenho. Se eu quisesse ver os containers que eu tenho, containerls de list. Eu não tenho nenhum container rodando aqui. Mas, ó, eu já criei alguns containers aqui, ó. Tipo, esse app database aqui, algum tempo atrás, ele só não tá rodando, mas ele foi criado. Então, existe esse app database. A gente tem o eager beaver, ele vai dando nomes para as coisas que a gente foi rodando aqui dentro do sistema. Massa?

**[00:32:44]** Aí o André perguntou... Alguém perguntou se tinha um cliente SQL modo texto. Eu tenho Harley Quinn, a gente viu ele nas aulas passadas, mano. Harley Quinn, ele é um cliente de banco de dados modo texto, que se você precisar, não é uma ideia de modo texto. Legal? Então é isso, eu vou mudar o nome do container, para ele criar o outro, para a gente ver o que acontece aqui, e vou deixar ele rodando, vai? Então eu vou colocar database 2, só para ele rodar aqui. Massa!

**[00:33:23]** Subiu aqui, tá rodando, ele criou um novo container, aquele que a gente tinha. Tá lá, ele criou dois, se você vier aqui no Shell de novo e dá um, sei lá, Docker PS, agora você vai ver que ele tá rodando aqui, ó. Ele é o app Database 2, ele faz o bind da 5.4.3.2, é a imagem do Postgres, esse é o ID do container. Massa? Então ele tá rodando aqui. Se você der um Docker...

**[00:33:45]** Images, a gente tem aqui do lado, a gente tem o Docker, container, ls, lista, os containers rodando aqui e a gente está com esse aqui. Então ele tem um ID aqui que é o identificador dele. Aqui para ver o ID, imagem, comando que ele rodou, quando ele foi criado, quanto tempo ele está rodando, quais as portas, qual o nome dele e tudo mais. Então a gente tem todas essas coisinhas aqui. Massa, aí agora!

**[00:34:14]** Eu quero fazer uma coisa com vocês. Eu quero fazer a nossa aplicação usar esse Postgres, que a gente acabou de subir, na 5A32. Aí, para isso, a gente precisa instalar a biblioteca do Postgres no Python. A biblioteca do Postgres é essa aqui, é o PissarIncoOPG. Então, é o Postgres malucão. PissarIncoOPG.

**[00:34:43]** E aí, ele tem essa opção aqui de instalar o binary. Ou seja, se a gente não coloca esse binary, ele vai trazer algumas outras informações aqui pra gente que talvez a gente não queira. Ele vai tentar escompilar o pacote, dependendo da plataforma, então a gente vai instalar o Psy-COPG binary aqui. Massa? Então, eu vou vir aqui, só pra um lugar onde eu tenha aplicação rodando aqui, dentro do meu editor, ou qualquer shell que seja, eu vou dar um poetry, edge.

**[00:35:14]** É. Psycopg binary. Já tive muito problema com esse Psycopg e o binary, né? Então é legal. Psycopg binary. Aí ele instalou aqui a versão do Psycopg, a versão 3.2, que é a versão que a gente está usando agora, e ele instalou o binário também aqui. Mas se vocês forem seguir outro tutorial, alguém vai falar, estalo Psycopg2, não faça isso, estale o Psycopg. Sem Psycopg2, não.

**[00:35:47]** O binary é a versão compilada, assim. Legal? Então a gente trouxe aqui. Para a gente poder usar esse banco de dados na nossa aplicação, simplesmente o que a gente vai fazer é popular o nosso ponto envy. Porque lembra, a gente foi criando estruturas para a gente poder fazer as coisas mais simples, né? Então a gente vai aqui no nosso ponto envy e vai colocar isso aqui. Eu estou deixando aqui embaixo. Olha, eu vou deletar a linha do...

**[00:36:11]** do SQLite, e aí o RL do banco de dados vai ser essa aqui agora. Eu estou colocando aqui embaixo, porque eu quero discutir com vocês algumas coisas que estão rolando aqui. Mas, a gente está falando o seguinte, que a gente vai usar o Postgres SQL na nossa aplicação. O driver que a gente vai usar, ou seja, a biblioteca que a gente vai usar para se comunicar com o banco, é o Psycopg. Então, por isso a gente está usando Postgres SQL mais Psycopg.

**[00:36:50]** Aí beleza, dois pontos, barra a barra, a gente vai colocar o nome do user, do banco de dados, e a senha, então é usuário dois pontos senha, que foi basicamente o que a gente passou aqui, a hora que a gente subiu o container, lembra aqui ó, app user, app password, então, usuário senha. Aí a gente está falando, o arroba é de app, né, aonde ele está rodando, então ele está rodando na minha própria máquina.

**[00:37:19]** Na porta 2.5432, ou seja, tá rodando na porta 5.432 porque a gente deu aquele bind de porta, lembra? A hora que a gente deu o DockerRAM e aqui é o nome do nosso banco de dados. Então, barra appDB, que é o nome que a gente tinha passado aqui no PostgresDB. E aí é assim que essa URL toda aqui do banco tá consistida, né? Então a gente tá falando. É Postgres, qual é o driver, usuário, senha, aonde tá, qual é a porta e qual é o banco de dados.

**[00:37:49]** Essa é toda a explicação aqui. Aí você bota tudo numa linha só, né? Eu só quebrei pra gente poder ir discutindo aqui. Massa? Então a gente bota isso aqui, pode botar lá no começo, igual tava, no mesmo formato, não precisa fazer nada muito diferente disso. Legal? Rodou aqui? Agora vocês vão ver a magia do SQL que minhas são. Eu vou dar um poetry ram, vai, poetry ram, task ram. Legal.

**[00:38:27]** Estamos conectados no banco. Sério. Agora, para quem não tinha entendido ainda, o grande valor do SQL Alchemy acabou de sacar, né? Porque eu não precisei mudar nada no código. Eu só mudei a URL que sobe nos settings aqui, né? Então, eu só mudei essa URL e o banco de dados está de pé. Porque eu posto, Gris.

**[00:39:12]** funciona da mesma forma, tá ligado? Tipo assim, simplão. E as tabelas já foram criadas, então é o que a gente vai ver agora. Então, vamos lá. Agora eu vou lá no localhost, 8000, barra docs, né? Pra gente ver o que que rola aqui. Eu vou só tentar criar um user aqui. Vou dar um try it out. Vou rodar aqui. Execute. Pimba. Deu erro interno. Interno serve erro. Deu 500. O que que aconteceu? Olha, deu erro aqui, ó.

**[00:39:45]** Pissai com o PG Errors. Undefined Table. Relation User does not exist. Quando ele foi fazer um From Users, para poder inserir a coisa no banco de dados, não existe a tabela. A tabela Users não existe. Por que ela não existe? Porque a gente precisa aplicar a migração aqui. Então... Só que isso poderia ser muito difícil, muito custoso.

**[00:40:18]** Mas a gente tem uma limbic, né? Para resolver esse problema. Como a limbic também usa a configuração dos settings que a gente já definiu lá no .mv, se eu rodar ele aqui, a limbic upgrade head, beleza, não tem, porque eu não estou no ambiente virtual, eu vou habilitar o ambiente virtual. Pô, etrichel, vai para ficar mais fácil.

**[00:40:44]** Ele aplicou todas aquelas modificações que a gente criou de esquema no banco, foi alterando as tabelas, foi criando isso aqui. Aqui, olha o que ele fez. Você pode vir aqui no Shell, aqui. Aqui ele tem aquele erro que a gente tinha dado pra gente, do statement de não existir, mas ele deu que a migração tá rodando, que funcionou e tudo mais. Vamos rodar a aplicação agora? Vamos voltar lá no nosso pay bala, vou mandar o request de novo.

**[00:41:24]** Execute, rodou. Aqui ó, ID1. Massa, né? Tá funcionando. A gente tem o mesmo comportamento que a gente tinha antes. Tudo isso pela maravilha do S-K-L-Q-M. E do Alembic. Então, se precisasse, aí alguém perguntou tipo assim, ah, e se eu precisasse mudar pro... Se fosse usar o...

**[00:41:57]** Mas SQL, serviria. Se eu fosse usar o MariaDB, serviria. Isso serve para qualquer banco de dados que o SQL é algo que me suporta. Então, aqui ó. Cadê, cadê, cadê? Não é aqui, né? Cadê, cadê, cadê? Engine Configuration. Pô, eu preciso achar aqui. Vamos lá. Aqui na documentação. Current Documentation. Vamos fazer uma busca aqui. Postgres. Postgres SQL. Ah tá, eu escrevi errado.

**[00:42:49]** Postgres. Cadê, cadê, cadê? Aqui tem vários dialetos de banco de dados que ele consegue falar e eu quero a página de cima dessa aqui. Se alguém achar o link que quiser me mandar vai ser mais rápido, né? Connection Pulling, Connection Engines, Dialects aqui. Achei a página. Então ele suporta o...

**[00:43:26]** Microsoft SQL Server, ele suporta o MySQL e o MariaDB, Oracle, PostgreSQL e o SQLite. Isso por padrão, ele suporta essas bibliotecas. E aí, se você tiver algumas coisas a mais, ele tem plugins. Aí tem egress, que é a base do PostgreSQL.

**[00:43:50]** Tem Amazon Athena, Amazon Redshift, Apache Drill, Apache Druid, Hive, Presto, Solar, Clickhouse, CockroachDB, CreateDB, DataEnd, Databricks, Firebird, Big Query do Google, Google Sheets, Google Sheets, Planilhas do Google e um monte de coisas aqui, né? Então suporta um montão de bancos de dados, então acho que...

**[00:44:17]** Essa é uma das grandes vantagens do SQL Alchemy, de ter ele na nossa aplicação, que ele faz esse tipo de coisa. E aí, já tá rodando, já tá funcionando, a aplicação tá linda, maravilhosa. Foi num cinha. Agora, eu quero explicar uma coisa que pode ter passado agora, porque você não tá reproduzindo junto comigo, mas vai te pegar no futuro. Tem alguém aqui usando Windows? E aí, quando eu digo Windows, eu tô falando Windows mesmo.

**[00:44:49]** Tipo assim, você não tá rodando no AVM, você não tá rodando no Hyper-V, você não tá rodando no WSL, tá rodando no C-M-D-Zão da vida, no PowerShell, a aplicação? Se você precisar rodar isso no Windows por padrão, a pólice do PSY-COPG não costuma funcionar muito bem com a CINCAIO no Windows. Então, aqui tem uma explicação para quem quiser depois. Aqui, ó.

**[00:45:26]** Aí tá aqui, onWindows precisa ir com o pg, e não é compatível, né? Com o ProActorEventLoop, padrão, né? Então a gente tem que trocar o EventLoop pra rodar no Windows, né? Então, basicamente o que precisa ser feito é isso aqui que eu coloquei no slide. A gente vai falar, a gente vai ver, tipo assim, ah, qual que é a plataforma? Se for Win32, a gente vai setar o EventLoop, a polícia do EventLoop, pra ser

**[00:45:56]** pro Windows selecionar qual ele vai querer. Depois vocês podem pegar isso, tá nos slides, tá lá. Mas eu vou colocar aqui dentro do meu código também pra gente entender onde vai colocar isso aqui. Eu vou colocar isso no app. Bem no app mesmo. Então antes a gente definiu assim que aí o app do FastAPI, aí a gente importa aqui, né? Importa 6 e importa assim que aí, ó. Massa.

**[00:46:26]** Você vai ver que mesmo aqui no Linux, se eu rodar, ele vai continuar rodando e tudo mais, então não tem nenhum problema. Ele vai olhar esse if e vai falar, ah, é Windows? Não. Então, tá tudo bem. Então, pra quem tiver, pode ser que esse problema aconteça aqui. Basicamente, a gente só vai trocar a polícia do Event Loop pra falar Windows. Selecione aí o Event Loop certo. Porque isso varia de versão do Windows, tá? Tem uma confusão aqui que roda por trás.

**[00:46:57]** Tem uma explicação lá no link que eu deixei. Aí, se vocês estiverem fazendo agora junto comigo e quiserem isso aqui, tem uma... Cadê? Cadê? Cadê? Cadê? Antes de estar no próximo comando, pera aí. Windows. Aqui, ó. Nesse ponto aqui, tem o comando exato que eu preciso colocar aqui, né? Para ele colocar a polícia e tal. Eu quebrei aqui só para ficar bonitinho, né? Mas isso aqui vai ficar numa linha só, assim. Massa? Então, é basicamente isso que eu preciso.

**[00:47:37]** Aí o Reds perguntou, mas se isso for no Docker, não faz diferença? Sim, não faz diferença. Mas se você tentar rodar o código na tua máquina usando o lupi-saic-opg-acíncrono, que é o que a gente está fazendo, ele não vai funcionar. Então, não custa nada, é um if no código, sabe? Tá tudo bem. Então, para quem tiver esse problema, é assim que resolve.

**[00:48:02]** Se você estiver fazendo o código síncrono, sem assim caiu, ele vai funcionar normal. O problema é só as corrotinas à síncronas. Massa, então, segue o jogo aqui. Beleza. A gente está com tudo funcionando, está tudo rodando, tudo bala aqui. Só que, se eu rodar os nossos testes aqui, então task test, deixa eu só dar um format aqui, para ele ficar bonitinho aqui.

**[00:48:39]** O teste continua passando, tá tudo rodando lindamente bem, mas pera aí. Por que o teste continua rodando se a gente mudou de banco de dados? Então, a gente migrou de banco, mas a gente não fez a migração certinha aqui. O Rafa perguntou se a configuração pode botar no lifespan. Pode, é que eu não ensinei o lifespan, então por isso eu não tô colocando lá. Assim que resolve? Assim? É assim que resolve mesmo, mano.

**[00:49:14]** Então, a lembra que a gente tá usando aqui, né? Na nossa própria criação, aqui no nosso próprio monstreio, que é nossa fixture de session, a gente cria, né, a engine do banco de dados pra interagir diretamente com o esquelite, né?

**[00:49:31]** E a gente não quer mais isso, né? Porque se a gente for testar, a gente quer testar com o banco de verdade, com o banco que a gente está usando em produção, né? Eu não quero que isso aqui esteja dessa forma. Então, lembra que a gente conectou isso aqui, static pull, a gente foi criando várias configurações e tudo mais. O que a gente precisa aqui agora é usar o banco de dados de produção, mano. Só bora! Então, a gente não vai mais usar isso aqui. A gente vai usar...

**[00:50:01]** Os settings deitabase. Deitabase URL. O mesmo banco que a gente está usando em produção. Legal. Os settings já estão importados? Settings já. Aqui. Então, a gente vai usar ele aqui. Settings deitabase e tal. Se a gente for rodar agora, olha que interessante. Eu vou rodar o teste aqui. Ah, beleza. Task Format. O que é bonitinho? Task Test. Legal. Funcionou.

**[00:50:47]** Tudo continua rodando, tudo ficou maravilhoso aqui, porém, se eu parar o banco de dados aqui, vou parar o banco. A nossa aplicação para de funcionar, porque ele não consegue se comunicar com o banco de dados. E aí agora, a gente acabou de criar um problemão, né? E qual que é o problema?

**[00:51:22]** O banco de dados precisa estar online, precisa estar o container de pé pra gente poder rodar os testes da aplicação. E aí você fala assim, pô, e aí se eu rodar isso aqui junto com o banco, aí ele vai deletar todas as coisas do banco direto, né? Fica complicado, né? Fica difícil, né? Não tem como resolver isso aqui, né? Porque eu não quero que ele apague os dados lá, mas aí eu também preciso que o container esteja de pé. E agora?

**[00:51:53]** O que a gente faz? E aí que eu vou colocar mais uma dependência aqui no nosso projeto, que é o test containers. Test containers é uma biblioteca Python, que o que ela faz? Ela levanta os containers durante o teste, só que ela cria os próprios containers para o teste. Ela não vai falar tipo assim, ah, preciso.

**[00:52:24]** Sabe que o contêiner esteja rodando? Não, ela vai lá, se o contêiner não tiver na tua máquina, se você não tiver a imagem, ele vai lá, baixa a imagem, traz para o seu PC, roda tudo o que precisa, levanta isso dentro do escopo do teste. Então você pode ter dependências externas de contêiner externos, pode ser até contêiner de outra aplicação, microserviços, sei lá, que o outro time mexe, tudo mais. O teste de contêiner vai dar conta desse tipo de coisa.

**[00:52:54]** Então, aí agora, vamos instalar ele aqui, então vou colocar no grupo de desenvolvimento aqui, Normal, TestContainers. E eu acho que eu não vou levar vocês pra lá, então vou fazer isso aqui antes. Pra vocês sacarem que isso aqui ajuda muito assim. Eu quero ver todas as imagens aqui, isso que eu quero mostrar pra vocês. Módulos, aqui.

**[00:53:36]** Então, qualquer dependência que você tiver, que você precisar subir um container externo, o teste container basicamente tem. Ah, preciso de uma AWS Lâmbida, de um, sei lá, um container de um serviço externo. Ah, precisa ser um Pulsegres, um Enginex, que é um servidor web. Ah, olha o Pulsegres aqui. Ah, precisa ser um Oracle DB. Saca? Ranges. Raptmq.

**[00:54:02]** Qualquer coisa que você tiver como dependência, e essa dependência precisa rodar um teste que depende dos sistemas de mensageria, que depende de uma quantidade, que depende de qualquer coisa, que existe um container para essa coisa, você pode usar o test containers para chamar sua coisa e resolver o que você precisa aqui dentro. Massa?

**[00:54:24]** E aí ele vai simplesmente dentro do escopo do teste, dentro da fixture, ele vai levantar esse container, a gente interage, faz tudo o que precisa fazer com ele e depois ele derruba o container de novo. Lindão, bonito. Como a gente vai usar o Postgres, né? Então a gente vai lá no testcontainers.postgres import PostgresContainer, que é o container do Postgres. Então eu vou colocar ele aqui.

**[00:54:54]** Então, a gente vai chamar esse PostgresContainer aqui. E aí dentro do nosso código aqui, eu vou copiar e a gente vai explicando aqui para ficar mais simples aqui. Dentro do nosso fixture de session aqui, eu vou falar o seguinte, olha, cria a Engine para mim.

**[00:55:15]** do banco de dados. Cri e faz a conexão com o banco de dados. Aí você vai falar o seguinte, olha, eu quero que você conecte no Postgres, aí é aquela mesma coisa. Ah, dois pontos a versão, né? A gente baixou a 17, né? Que a gente baixou a última. Quando eu escrevi esse material, a última era 16, né? Então eu posso colocar o 17 aqui. O driver que a gente vai usar é o Psy-COPG. E aí agora, a gente simplesmente vai chamar ele aqui, né? Então ele vai criar a Engine com...

**[00:55:53]** Essa coisa que a gente tem aqui que é esse Postgres, tal, tal, tal. Massa, então ele vai criar uma URL de conexão, uma look aqui dele, que ele vai gerenciar tudo isso sozinho. A única coisa que tem que lembrar aqui é o seguinte, todo esse bloco, toda a coisa da fixture tem que ficar dentro do if do container, senão não vai dar certo. Massa, vamos rodar os testes agora e ver o que acontece? Então ele vai baixar a imagem do Postgres e tudo mais.

**[00:56:29]** Ó, uma outra coisa que eu queria mostrar pra vocês aqui é o seguinte, eu não sei se eu vou conseguir aqui, ó. Nota uma coisa aqui. Os testes rodaram com o banco de dados em 3 segundos. Guarda essa informação. Agora eu vou rodar com o Task Containers. Task Format, Task Test. Legal. Aí ele tá pegando aqui, ó, ele tá falando. Pulling Image, Task Container, tal, tal, tal. Ele precisa da imagem base do Task Container. Aí ele tá pegando o Postgres 17.

**[00:57:00]** que a gente já tinha, por isso foi mais rápido. Mas olha o tanto que demora para passar os testes agora. Dá para tomar um café. E não de vocês que tem mais testes que os meus, por causa do exercício, vai levar muito mais tempo. E mais funciona. E aí, vocês acharam uma boa ideia isso aqui? O que vocês acharam disso aqui? Resolve o problema. Mas não gostei da solução que a gente criou aqui.

**[00:58:01]** É, toda vez ele criou o container, exatamente. A todo teste, ele vai fazer isso aqui. Todo o teste que depende do client, da fixture de client, ele vai... Todo o que precisa de session e o client precisa de session, né? Então ele vai fazer isso aqui todas as vezes. Ó, a gente tinha um teste que levou 3 segundos, né? Agora a gente tem os testes que demoram 77 segundos. Legal, tudo bem?

**[00:58:30]** Aí agora você tem que lembrar o seguinte, imagina que eu não tenho a imagem do Postgres aqui. Vamos ver o que que rola? Vamos ver quanto tempo a mais vai demorar. Então beleza, Docker, Image, LS. Eu tenho a imagem do Postgres 17 aqui, certo? Então eu vou remover essa imagem aqui. Docker, RMI de imagem, remove image.

**[00:58:55]** Beleza, eu vou dar um prune, vai? Vai ser mais rápido aqui. Docker, System, prune, menos A, menos F, deleta tudo e tá tudo bem. Legal? Removeu tudo. Vamos ver agora num caso real que eu rodaria isso aqui a primeira vez, né? Enquanto está rodando, ó, ele vai baixar a imagem do pôso e agora vai demorar muito mais, tá ligado? Ó, agora sim está demorado.

**[00:59:35]** Então, legal. Então, agora eu quero conversar com vocês sobre alguma outra coisa, né? Tipo assim, pra gente melhorar isso aqui. Lembra que a gente tava brincando até agora? A gente falou sobre essas coisas, né? Que são fixtures, né? Do Python. Fixtures do Python Test. E aí, o que que acontece? Uma fixture, né? Queremos um cafezinho. Eu também, se alguém passar, me oferece. Toda vez que a gente roda o Python Test, né? Eu tenho o Python Test Runner.

**[01:00:05]** A gente tem uma fixture, né? Aí o que vai acontecer? Ele vai executar a fixture até o wield. Aí depois ele executa um teste. E aí ele executa a fixture depois do wield. Toda vez isso acontece, né? Ou seja, isso aqui é o que está rolando. Então ele vai precisar conectar, ele vai precisar da sessão. Aí o que ele faz? Ele cria...

**[01:00:32]** o container do banco de dados, ou seja, ele vê se o container baixou ou não, aí depois ele levanta o container, aí ele dá a sessão pra gente, a gente vai se resolver com essa sessão, a gente vai conversando, vai fazendo o que tem pra fazer, aí depois que acaba o teste, ele volta pra cá pra executar o resto da fixture, aí ele drop o database, desmonta o banco de dados, o container do banco de dados, e ele vai pro próximo teste, e ele fica fazendo isso todas as vezes, né?

**[01:01:00]** A grande sacada aqui é que o PiTest tem vários escopos de fixture, ou seja, por padrão, ele executa o escopo de function, ou seja, antes de cada função de teste, ele cria fixture de novo e executa mais uma vez, ou seja,

**[01:01:21]** A cada teste ele cria tudo até o yield e depois ele roda o fim. Aí depois de uma próxima função de teste ele vai fazendo isso aqui. Porque que a gente está fazendo aqui, né? Deixa eu pegar o teste users aqui. Toda nossa coisa são funções de teste, né? A gente tem essa def, essa outra def, essa outra def, essa outra def, essa outra def, ou seja, o escopo padrão vai fazer isso várias vezes, né?

**[01:01:51]** E aí, o PiTest tem alguns outros escopos, não é? Ou seja, se a gente tivesse uma classe de teste, ele rodaria uma vez por classe, a gente poderia pedir para ele rodar uma vez por módulo, a gente poderia pedir para ele rodar uma vez por pacote de teste, mas o que é interessante para a gente aqui é o Session. Ou seja, ele vai executar uma vez antes de executar todos os testes,

**[01:02:18]** Ou seja, ele vai começar, vai rodar essa fixture antes dos testes, e depois ele vai dar o banco de dados pra gente, a gente trabalha em todos os testes, e depois ele termina o serviço, né? Ou seja, ele levanta o banco antes e depois. Só que a gente não pode colocar essa fixture aqui pra falar nessa aqui, eu poderia falar o seguinte, Scope, e falar o seguinte, olha, isso aqui é Session. Eu não posso fazer isso aqui. Por que se eu fizer isso aqui?

**[01:02:51]** Eu vou rodar os testes aqui com vocês, vamos ver o que que rola, vai ser mais rápido. Só que os testes vão começar a quebrar. Massa? Então, o que que eu vou pensar aqui com vocês? A gente vai criar uma nova fixe, se liga, se liga. Que cria, porque tipo assim, eu não posso garantir que o teste vai funcionar? Porque o teste, ele tem que subir o banco de dados, mas antes de cada teste, ele tem que criar, limpar os metadeitas, né?

**[01:03:38]** Então a gente vai criar uma nova fixture. Então vamos lá. Arroba, pie-test, ponto fixture. E aí eu vou criar uma fixture que a gente vai chamar de Engine. Que ela só faz isso aqui. E aí a gente passa aqui, essa fixture de Engine pra cá. Aí a gente pode dar, sei lá, um... Peraí que eu rodei um Konami Code aqui no teclado. A gente vai fazer o seguinte, yield.

**[01:04:16]** E aí a gente fala que essa fixture, que é a fixture que sobe o container e cria a conexão, tem o scope de Session. Olha que interessante. Então, ele vai subir o banco de dados, criar a conexão uma vez só. Ou seja, antes de todos os testes, ele vai gerar esse objeto aqui. Depois que todos os testes rodarem,

**[01:04:52]** Ele vai desmontar o container, ou seja, a gente ainda vai ter um gargalo, porque a gente vai ter que esperar o container subir, mas ele vai subir uma vez, rodar 50 tests, e depois a gente baixa o container. Fez sentido que essa fixture faz o que, qual que é o esquema do scope aqui? Ele não roda toda vez. Vamos testar aqui, enquanto eu rodo, vocês me falam aí o que vocês acham. Ah, ah, pera aí que ficou assim que algum lugar aqui. Ah, tá, beleza. Tá com a identação zoada aqui. Task test.

**[01:05:37]** rodei, ó, agora ele vai subir, ó, ele esperou o pôsogris subir, subiu, levantou o pôsogris, rodou todos os tés e acabou de novo. Ou seja, a gente ainda tem um tempinho a mais porque tem que esperar a imagem subir, mas tipo assim, é uma vez só. De três segundos, agora leva cinco, ok, tudo bem. Demora dois segundos a mais, só que isso aqui não escala nem em relação, tipo assim, ah, tipo assim, se eu tiver...

**[01:06:06]** 5 testes ele vai levar esses 2 segundos a mais. Se eu tiver 800 testes ele vai levar esses 2 segundos a mais, não escala isso aqui. Legal. Então basicamente essa é a ideia do testes containers e a gente junta ele com essa ideia de fixtures aqui. A gente poderia colocar outro tipo aqui, por exemplo, em vez de session a gente vai rodar por módulo.

**[01:06:30]** Massa, só pra ver, ele subindo várias vezes aqui. Então ele vai rodar, ele vai subir uma vez no teste do user, uma vez no teste to do, uma vez no teste do banco, só pra vocês sacarem o que acontece aqui. Nessa questão dos escopos aqui, ó. Ó, subiu o container, aí ele rodou o teste do app, aí agora ele rodou o teste do alpha, aí subiu o contêiner de novo, rodou do security. Subiu o contêiner de novo, rodou os to dos. Subiu o contêiner de novo.

**[01:07:01]** Agora rodou-os do user e massa. Então essa é a diferença do escopo da session. Massa? Então existem vários escopos. Pode ser por módulo, pode ser por pacote, por classe, por função, é o padrão. E a gente usou o session que roda uma vez só. Massa? Então era isso que eu queria mostrar pra vocês aqui agora. É basicamente como fica a outra fiction, né? Quando a gente impede a Engine aqui. Massa?

**[01:07:30]** Alguém tem alguma pergunta sobre isso aqui? Sobre essa parte do assunto? Eu sei que é um pouco... Foram muitas coisas, é docker, é banco de dados, é teste containers, é fixture, é uma montão de informação. Então, se vocês tiverem perguntas, me mandem aí. Então, agora, o que a gente vai fazer? A gente vai criar o container, a gente usou, né? O container do pôsso e tudo mais. Agora, a gente vai fazer o container do nosso próprio projeto. Massa?

**[01:08:07]** E aí, como é que isso funciona? Para a gente criar um container, como a gente está usando Docker, o nome do arquivo tem que ser Dockerfile. E eu vou colocar ele aqui na raiz do nosso projeto, só para vocês... Aqui, é na raiz do projeto. Aonde está o PyProject, por exemplo. Eu vou chamar isso aqui de... Ah, pera aí. Dockerfile.

**[01:08:38]** Nossa, então chegamos aqui. Aí o que que eu vou falar? O seguinte, quando eu vou criar a minha imagem, eu posso criar a imagem do zero. Só que eu não quero, né? Por que? A gente precisa que o Python esteja instalado, vamos simplificar a vida. Então a gente faz o seguinte, From. E a gente fala, olha, lá da imagem do Docker Hub que a gente vai pegar aqui, então vamos lá, Docker Hub, a gente seleciona aqui o Python, se a gente fosse procurar isso na mão, Python.

**[01:09:08]** Então a gente vai pegar a imagem do Python, qual a versão que a gente está rodando? É a 313, que é a última versão do Python. Então a gente vai falar o seguinte, Python 2.3.13. Então a gente vai pegar a imagem já pronta lá do Python 3.13 e a partir daquela imagem que já tem o Python instalado, tem algumas coisas para rodar tudo do Python, a gente vai fazer nossa aplicação. O Python tem várias versões, aqui eu não vou me estender muito nisso.

**[01:09:39]** Tem várias. Tem o Alpine, o Slim, o Bullsev, o Bookworm. Tem várias imagens aqui. Eu vou pegar a menor imagem que é o Slim. É pequenininho, só vem o que precisa para rodar o Python. A gente não precisa de muito mais do que isso. Perdão. Se você estiver rodando algumas outras coisas e tal, você pode pegar mais recursos aqui. Aí você olha exatamente o que tem em cada imagem.

**[01:10:16]** para a gente o sling vai ser o suficiente. E aí aqui, como a gente já está rodando dentro do ambiente que é controlado, eu vou passar essa variável de ambiente para o pointer aqui, que é o seguinte, envy de variável de ambiente é a mesma coisa que a gente faz no ponto envy aqui. Eu vou falar para o pointer o seguinte, olha, não cria um ambiente virtual. Ah, ele pode criar um ambiente virtual? Pode. Não precisa, não? Assim, isso vai tomar mais tempo de builds se a gente fizer isso, então eu não quero.

**[01:10:48]** Aí, agora a gente tem uma outra chamada, que é tipo uma linguagemzinha de marcação, não é, você viu? Da imagem do Python com a figura e essa variável de ambiente. E aqui é o workdir, ou seja, a gente fala em qual pastinha a gente vai trabalhar dentro dessa maquininha, dentro do contêiner, né? Onde a gente vai colocar nossos arquivos. Então, eu vou colocar, ele vai criar essa pastinha app dentro do contêiner e a gente vai copiar as coisas para lá. Massa? Então, o que eu preciso fazer? Eu vou copiar o meu projeto para dentro do contêiner.

**[01:11:18]** Aí eu coloquei aqui copy ponto ponto.

**[01:11:21]** Ou seja, copia a pasta inteira que a gente tem pra dentro do container. Alguém vai... Aí, aqui existem vários casos de otimização aqui, eu não vou me estender muito nesse assunto. A gente vai criar imagem mais simples possível. Eu poderia copiar só o Pi Project e depois instalar, sabe? A ordem é que importa no tempo de build, mas eu não quero me aprofundar muito nisso aqui nesse exato momento. Então a gente vai copiar toda essa nossa pastinha.

**[01:11:49]** para dentro do container aqui. Aí a gente tem esse rum, que é essa coisinha chamada rum, ou seja, roda alguma coisa no terminal, lá de dentro do container. E aí eu vou pedir para ele instalar o polleter aqui para mim. Massa, vou rodar isso aqui para a gente ver o que acontece. Vamos rodar.

**[01:12:10]** A gente tem esse comando que se chama Docker Build, aí a gente vai criar a imagem da nossa aplicação aqui. Docker Build, aí eu vou chamar essa aplicação de FastAPI0, que eu lembro que a gente está usando, e o ponto é o lugar onde a gente está, ou seja, o lugar é onde tem o arquivo Docker File aqui dentro. Mas aí o T, eu estou passando tipo o nomezinho, a tag da nossa imagem aqui. Legal? Ponto. Olha o que que vai acontecer.

**[01:12:41]** Ele pegou, ele foi lá, baixou a imagem do Python. Nesse caso, eu não poderia instalar o Pipex. Poderia, né? É que aqui é mais rápido, né? Então, ó, ele copiou, né? Ele foi lá, pegou a imagem do Python 3.3 Slim, baixou pra dentro da nossa máquina. Beleza, fez tudo que tinha pra fazer. São várias camadinhas que essa imagem tem. Definiu a pasta de trabalho aqui como app. Copiou nossos arquivos aqui pra dentro.

**[01:13:17]** Aí a gente rodou o pipinstal poetry, ele instalou o poetry, nomeou essa imagem, porém, nada acontece, né? Porque a gente não pediu pra ele rodar nada, né? A gente pediu, roda o pipinstal, aí ele rodou o pipinstal, mas não pedimos pra ele rodar a aplicação, então, obviamente, nada acontece aqui até esse momento. Paloma, muito obrigado pelo super chat, isso me ajuda demais, mano. Coaquinha de sucesso, valeu.

**[01:13:44]** Então, vamos continuar construindo nossa imagem aqui. Então, legal, o que a gente precisa aqui? A gente precisa instalar as bibliotecas do Python aqui dentro. Então, o que a gente costuma fazer na nossa máquina quando a gente precisa fazer isso é o pipin-poetry install, que instala todas as bibliotecas que a gente precisa. Só isso aqui já seria o suficiente.

**[01:14:06]** Só que, às vezes, o poetre aparece um negocinho, tipo assim, pô, já tem esse pacote, você quer instalar de novo? Às vezes, ele tem essa interação aqui. Então, a gente tá tirando as interações. Se ele perguntar qualquer coisa, a gente tá falando. Não pergunte nada. Aí, a gente tem essa tag aqui, que é noance, né? Porque, tipo assim, ah! Vai ter algumas interações e tal. Às vezes, uma coisinha vai ficar colorida, um negocinho, pipipipipopopó. Não quero isso.

**[01:14:39]** E aí, por último, a gente tem isso aqui que é o without deve, né? Ou seja, não instala as dependências de desenvolvimento. Por que que eu não quero que instala as dependências de desenvolvimento? Porque quando eu for rodar isso aqui em produção, eu não vou rodar o pie test, eu não vou rodar o rough, sabe? Qualquer outras dessas coisas. Então, ele vai eliminar na hora de instalar todos esses pacotes que a gente tem aqui embaixo que estão como...

**[01:15:07]** Dependente, ou seja, se eu só quero executar a aplicação, eu não quero que estale o rough, o pytest, o pytestcov e o taskpy, o pytest assim caiu, factoryboy, frizzygun, testcontainers, não faz sentido. Saca, não faz sentido. Então, eu só quero que ele instale as coisas que tem aqui dentro. Legal? É isso aqui. E aí agora, né, eu tenho um comando que eu deixei aqui que é o seguinte, ah...

**[01:15:44]** Dependendo da máquina, às vezes você tem um problema que a máquina não é muito boa para poder rodar um negócio, tipo assim, mirabolante, às vezes o poetre tem 200 bibliotecas para instalar e aí ele cria tipo assim 200 threads e tenta instalar tudo ao mesmo tempo.

**[01:16:00]** Não é o nosso caso, né? A gente tem poucas bibliotecas dentro do nosso projeto, uma, duas, três, quatro, cinco, seis, sete, oito e nove, e essas nove têm suas próprias subdependências e tudo mais, mas às vezes você vai rodar isso no ambiente, que sei lá, é um servidor da empresa que faz o build e lá tem, sei lá, um giga de memória. Então... Saca, não... Sabe, não estoura a memória da máquina, não faz tudo ser mais confuso, sabe?

**[01:16:30]** Fica no limite aqui, então, quando você for instalar, usa 10 workers no máximo aqui, pra gente não ter problemas de memória e tudo mais. De novo, precisaria disso aqui? Não necessariamente. Saca? Não necessariamente, mas eu tô fazendo isso pra imagem ficar mais levinha de build-up e tudo mais, evitando problemas no servidor onde isso for rodar depois. Tiago, muito obrigado, mano. Valeu demais.

**[01:17:04]** Aí perguntaram se nesse caso seria interessante o Stal ou o Sink para atualizar o Lock. Não, é só install, mano. Não atualizo o Lock aqui dentro. Porque se você atualizar o Lock, você perde o fio da ameada das coisas. Não está rodando a mesma coisa que está rodando a tua máquina. Então é install mesmo. Aí a Paloma perguntou, Without ajuda a subir o ambiente mais rápido ou no tamanho do pacote? As duas coisas. Saca, as duas coisas aqui.

**[01:17:37]** ele não vai instalar os pacotes de desenvolvimento, o que vai fazer a imagem ficar menor, e ele também não vai gastar mais tempo fazendo downloads desnecessários, né? Tipo assim, ele não vai baixar essas bibliotecas a mais e as dependências dessas bibliotecas aqui dentro. Mas é por isso que a gente coloca o without aqui, né? Se tivesse outros grupos, você poderia passar o without deve, dock...

**[01:18:07]** e, sei lá, spam. Saca, então você pode pedir só para instalar as dependências do próprio pacote aqui. Massa? Aí, por padrão aqui, eu vou falar o seguinte, que isso aqui expõe, dentro dessa imagem, a gente expõe a porta 8000. Ou seja, a porta 8000 desse container vai estar aberta para a gente poder dar binding na nossa máquina.

**[01:18:35]** E aí, por último, a gente vai rodar o CMD, que é o comando da imagem. Aqui a gente pede para ele rodar alguma coisa, e aqui no CMD a gente está falando. Esse é o comando do container, ou seja, Poetry Run, UVCorn, e tem isso aqui, né? A gente falou sobre isso aqui, mas em algum outro momento, mas eu vou relembrar vocês aqui. Massa, então a gente vai rodar o UVCorn direto, para não precisar chamar o FACE API de desenvolvimento e tal.

**[01:19:10]** O host aqui é importante, lembra que lá na aula que a gente falou sobre o vicorn, a introdução ao web, a gente falou ao 0.2, a gente falou quando a gente usa o menos-menos-host 0.0.0, a gente abre a porta na rede, não fica só dentro da nossa máquina, então por isso a gente falando, todo mundo que quiser acessar, que se conectar na porta 0.8.0, a gente vai responder, não só o loopback.

**[01:19:38]** E aí, por último, a gente tem o Fast API 0, que é o nosso projeto, o nome do nosso arquivo que é o app e os dois pontos que é o nome do nosso objeto app aqui dentro. A gente faz isso toda hora, né? A gente configurou assim no comando do taskpy, né? Legal? E aí, com isso aqui, se a gente buildar esse container, agora ele vai executar todos os passos que a gente precisa. Vamos lá!

**[01:20:04]** demorou menos tempo baixando Python, ele compilou, o Workday copiou as coisas e agora ele está instalando todas as dependências, ele está instalando o Poetry primeiro, ele configurou os Workers, ele está instalando as bibliotecas sem as de Dev, é mais rápido. Massa, e agora se a gente quiser, a gente pode rodar isso aqui. A gente deu esse nome de FastAPI0 aqui, a gente vai colocar aqui, FastAPI0. A gente tem aqui, Docker Run.

**[01:20:48]** O nome da nossa aplicação, a porta que a gente quer, a porta 8000 e o nome do nosso container e a versão aqui que é o latest, não preciso do latest, porque a gente só tem uma versão, a gente tem duas, mas tudo bem, é isso aqui. Massa, vamos ver o que que rola aqui. Subiu. Aqui, agora a aplicação está rodando na porta 8000 aqui dentro. Copiar isso aqui, eu não sei se não está rodando em lugar nenhum mais.

**[01:21:26]** Vamos rodar e ver o que pega aqui, ó. Beleza, a nossa API tá funcionando aqui. Se a gente for tentar rodar, lembre, né? Não vai funcionar. Porque o banco de dados não tá de pé, né? Se a porta já tá exposta, precisa informar na hora de rodar o comando? Sim, porque você precisa fazer o bind pra alguma porta da tua máquina, né? Você precisa falar qual porta da tua máquina vai ouvir a porta que o container tá expondo. Faz sentido? Beleza, deu erro.

**[01:22:11]** E aí, o erro está aqui. ConnexionFailage não conseguiu se comunicar com o SQL Alchemy porque o Postgres não está ouvindo lá na porta 5A32. A gente não subiu Postgres. E como é que a gente vai fazer isso aqui agora? A gente vai ter que levantar o container do Postgres. Então, vamos lá. Vamos voltar aqui. Legal, legal, legal, legal. Kd como roda o container do Postgres. Aqui atrás.

**[01:22:42]** Então, a gente vai pegar, eu vou duplicar dois shells aqui, ó. Nesse aqui, eu vou rodar o... Eu vou tirar o name aqui, só pra não dar confusão. Eu vou rodar o Postgres aqui no run, legal. Aí ele baixou a imagem do Postgres, tá rodando. Aí agora eu vou subir a minha aplicação aqui agora. É por causa do name. Eu não vou colocar o name aqui primeiro, beleza. Só pra facilitar, vai? Vamos rodar. Beleza, aí agora tá rodando na porta 8.0.

**[01:23:18]** Ou seja, se eu acessar agora, você viu que eu tive que subir os dois containers na mão, né? Nem todo mundo tem esse carinho com dois shells na máquina aqui, né? Mas se a gente falar no local host, e se a gente der um barra dox, a gente vai conseguir criar o nosso user aqui, né? User post, try it out, execute. Internal serve nem erro. Não consigo rodar. Olha aqui, que gangrena. Eu não consigo conectar a porta 5, 4, 3, 2.

**[01:23:52]** Mas, isso está rodando na porta 5, 4, 3, 2. A gente botou para rodar na porta 5, 4, 3, 2. E aí aqui, a gente botou para rodar na porta 8000. Por que que essas coisas não estão se comunicando? Por que que essas coisas não estão se comunicando? Porque a gente precisa de uma rede para fazer isso se comunicar. Eu não vou me aprofundar muito em redes de Docker, né? Mas, você precisaria configurar a rede aqui, ó. Deixa eu achar aonde é executando as migrações aqui embaixo. Tenho um comando.

**[01:24:26]** para rodar a rede. Então você precisa fazer com que as coisas se conectem.

**[01:24:32]** umas com as outras aqui. Então você vai falar que o network é o host, o outro também é o host, aí a gente vai criar um monte de coisas juntos e tal para tudo funcionar na mesma rede e tudo mais. Bom, beleza, está ficando complicado, né? Tipo assim, eu não sei, para mim já ficou complicado o suficiente. Eu tenho que subir um container, eu tenho que buildar esse container dessa forma determinada, aí eu tenho que subir o outro container, aí eu tenho que abrir dois shells e aí eu mexo de um, mexo para cá, edito no código, eu tenho que descer... Tá chato, né?

**[01:25:05]** Tá ficando complicado, né? Eu, pelo menos, pra mim, já começou a complicar. Não gosto muito disso. Então, a gente vai... Vou apresentar pra vocês uma outra ferramenta do Docker, que se chama Docker Compose. E a ideia do Docker Compose, como o Jordani disse aqui, né? Já estou sedento por um arquivo yam meu. A ideia do Docker Compose é facilitar com que a gente suba

**[01:25:43]** todos os containers, de uma vez só, com um único container, com um único comando, uma coisinha mais simples de fazer. Então a ideia é essa, tipo assim, eu vou descrever como os containers da minha aplicação vão ser, vão se parecer e a partir disso a gente vai rodar um Docker Compose Up e aí ele levanta todos os containers da nossa aplicação.

**[01:26:08]** Então, a ideia é essa, ele gerencia vários containers dentro de um único arquivo lindo, maravilhoso e tudo mais. O Docker Compose também tem que ser instalado à parte e aí lá na documentação do Docker que vocês acessaram para instalar tem como instalar o Docker Compose. Legal? Então, vamos lá. Como é que a gente queria? Eu vou criar na home, na raiz de novo, no mesmo lugar onde está o Dockerfile, onde está o PyProject. Eu vou criar um arquivo chamado compose.yaml.

**[01:26:37]** E aí a gente pode chamar ele com um ponto YAML ou com um ponto YAML. Aí é contigo. Massa. E aí o que que acontece? Dentro desse arquivo a gente vai criar uma coisa chamada Service. Massa. Simplão assim. Service. Agora vem a hora. Agora vem a hora. Agora vem a hora da verdade aqui que eu preciso falar uma coisa pra vocês. Vocês acham que Python é chato com identação? Vocês não mexeram com YAML ainda.

**[01:27:13]** Agora precisa prestar atenção, mano. Eu vou falar dois espaços, quatro espaços. Se não for, a quantidade de espaços, certo, vai dar errado. Massa? Então, um, dois espaços. Aí você vai colocar o serviço que a gente quer aqui. Aí, por exemplo, eu vou subir o FastZero deitabase aqui. Massa?

**[01:27:38]** Legal, então a gente vai começar a descrever o nosso banco de dados. A gente poderia fazer também o nosso app aqui. Vocês entenderem que isso aqui está no mesmo nível de... Então, tudo está dentro de service. A identação conta aqui. Então, aqui eu vou configurar as coisas do dois espaços de nome. Ou seja, são quatro espaços. 1, 2, 3, 4. Massa. Aqui eu vou configurar as coisas do database. E aqui eu vou configurar as coisas da aplicação aqui dentro. Então, legal.

**[01:28:10]** Qual que é a imagem que a gente vai baixar pra gente chamar o Postgres? Então, a imagem dele é o Postgres. Massa, então, Image, Postgres. Legal? Quais são as variáveis de ambiente que a gente vai passar aqui? Então, a gente também descreve aqui tudo bonitinho. Ó, essas são as variáveis de ambiente. São as mesmas que a gente tinha passado com o "-z", lembra?

**[01:28:39]** appuser, appdb, apppassword, tá tudo aqui. São as variáveis de ambiente que a gente vai passar pra essa imagem. A gente tá construindo aquele comando que a gente tinha de forma declarativa aqui dentro. Então, legal. E qual é a porta que a gente vai expor aqui? A gente vai expor a porta 5, 4, 3, 2. A mesma coisa que a gente tinha lá. Porta 5, 4, 3, 2. Legal? Então, você viu que a gente escreveu basicamente o que a gente tinha escrito naquele comando, só que em um arquivo.

**[01:29:13]** Eu já vou explicar esse volume aqui, pera aí, então vamos começar a construir a aplicação aqui. Então legal, a aplicação, ela é um pouco diferente, porque a imagem que ela vai usar aqui, é essa imagem que a gente vai chamar de FastZero app, que é o mesmo nome daqui de cima. E aí ela tem um negócio de build aqui. E aí esse build descreve que essa imagem, ela não vem...

**[01:29:41]** Lá do Docker Hub, por exemplo, ela vem, ela vai ser buildada aqui na nossa aplicação. O ponto é porque ela está exatamente no mesmo nível, ou seja, o Dockerfile está aqui. O Dockerfile está aqui dentro da nossa estrutura. Ah, como é que está isso aqui? Está aqui dentro. Então, está aqui. O Dockerfile está no mesmo lugar que o Compose está. Então, é isso. Massa, então, build aqui, porta oito mil.

**[01:30:15]** A gente vai chamar uma outra coisinha aqui, odeio a identação de Emel, bem-vindo ao Clube. As pessoas não gostam de Python, por causa da identação, mas o Emel é sensacional, porque ele é muito pior. E a gente vai falar o seguinte, olha, depende de FastZero Database, ou seja, ele vai esperar esse container estar pronto, e aí depois que ele está pronto aqui, a gente vai chamar essa outra coisa aqui, ou seja...

**[01:30:45]** Depois que ele subir, a gente sobe esse aqui. Massa, isso não garante que o pôster já vai estar, como diz, né? Positivo e operante. Tem algumas coisas que precisam ser feitas aqui e lá no texto tem algumas explicações. Para o nosso uso, isso aqui vai funcionar. Mas se você precisar fazer isso aqui rodar de uma forma mais bolada aqui, aqui ó.

**[01:31:15]** A boa prática aqui dentro tem um negócio que chama aqui, boas práticas de inicialização do banco de dados. Aí ele vai falar como sobe, uma checagem e tudo mais, o Harano que está aqui na aula que escreveu essa parte aqui para a gente. Então está aqui, massa. E isso aqui é o suficiente para a gente poder subir os dois containers ao mesmo tempo. Eu peguei esse endereço do environment aqui, só para mostrar para vocês que a gente consegue setar as mesmas variáveis que a gente coloca no .env aqui.

**[01:31:49]** Massa, então eu poderia falar, olha, eu estou sobreescrevendo, por quê? Porque agora não vai ser mais localhost, não é o nome da máquina aqui, não? Vamos lembrar aqui. Lembra aqui? Então o user, tal, tal, tal, e aí ele vai se comunicar uma máquina que se chama FastZero Database. E aí, FastZero Database é o nome dessa máquina aqui. Massa, desse container aqui.

**[01:32:18]** faz sentido essa configuração por isso a gente está sobrescrevendo aqui então tudo que a gente passar aqui sobrescreve o ponto em viu arquivo porque ele bota numa variável de ambiente legal vamos rodar aqui e ver o que acontece agora eu vou simplesmente rodar esse comando docker compose op docker compose op adicional property services não é não até lá oi tá vendo começou

**[01:32:53]** Em algum lugar é Services, tá vendo? Tem que saber de cabeça todas as coisas. Beleza. Locker Compose Up. Aí agora, ó. Começou a fazer o build e tal, vai instalar o Poetry legal. Ele tá construindo a nossa imagem. E a outra ele vai baixar da internet. Legal, ó. Aí aqui tá um log das duas aplicações, né? Do FastZero Database.

**[01:33:29]** e do nosso FastZero app, que é o nosso aplicativo. Então agora se a gente for acessar aqui, local roche 8000, tá rodando a aplicação. E a aplicação tá conectada com o banco de dados. Só que não tá funcionando o banco ainda, né? Rodei, internal server error, porque a gente não fez migração nesse banco aqui, né? Legal, a gente vai resolver isso aqui. Mas sacaram o que que acontece aqui? Esse arquivo faz com que todas as coisas se conectem.

**[01:34:04]** Ah, se eu tiver 10 containers, a gente vai juntar todos aqui, fazer eles funcionarem juntos e levantar tudo de uma vez, um espera o outro, roda as coisas que precisa. E se você tiver mais serviços, um servidor HTTP, um cache, alguma coisa pra rodar em background, tarefas, um celery, um broker, saca, às vezes você roda um milhão de coisas aqui e aí você precisa desse tipo de comunicação aqui.

**[01:34:36]** 0000? 8000? É, localhost 8000. Tanto faz que você preferir aí. É o loopback. Fez sentido isso aqui, esse arquivo? Pra que a gente faz ele? Me respondeu aí. E aí, por último, eu quero mostrar essa coisa pra vocês aqui, que é o Volumis. Que eu vou colocar aqui embaixo. Ele precisa estar no mesmo nível de services aqui em cima. Massa Services tá aqui. O volume tá aqui embaixo. E qual que é a ideia do volume?

**[01:35:15]** A ideia do volume é que a gente crie uma pasta, um diretório, para quem for mais exigente. A ideia é que a gente crie uma pastinha que seja compartilhada entre a nossa máquina, entre o host, e a máquina, as coisinhas do contêiner ali dentro. Chama de máquina para ficar mais fácil.

**[01:35:41]** Então a ideia é que a gente compartilhe arquivos de lá pra cá, de cá pra lá e a gente possa trocar essa ideia aqui dentro. E aí o que acontece? O que a gente vai pegar? A gente vai pegar esse volume específico aqui, eu vou copiar e a gente vai conversando aqui, que eu vou chamar de PGData, ou seja, PGD Postgres Data aqui. Então ele vai salvar as coisas que tem dentro do container.

**[01:36:13]** que estão nessa pasta aqui, barravar, barralib, barrapostgres, sql, barradeita, que é onde o postgres salva os dados. Então, seja, lá dentro do container está aqui, tudo certinho, e o pgdata interage aqui. Aí ele os perguntou, o Compose não precisa configurar a rede? Não, ele faz isso sozinho. A não ser que você queira um modo diferente de rede, mas...

**[01:36:36]** Basicão aqui, você pode usar, ele já cria comunicação entre os dois containers. Você pode criar um modo de rede se você precisar, mas não é o caso aqui. Mas só fez sentido esse volume? Aí agora, eu vou parar tudo aqui e ele vai criar as duas coisinhas aqui. Se eu der um LS aqui na minha pasta, você vai ver que quando a gente inserir dados lá dentro,

**[01:37:08]** Ele vai conectar, ele vai trazer essas coisas pra dentro desse volume, né? Pra dentro dessa pastinha no nosso PC aqui. Pra dentro do pgdata. Mas como não tem data, então não vai trazer nada aqui. Massa? Legal. A gente rodou, a gente viu que não funciona porque a gente não executou as migrações. A Paloma fez uma pergunta aqui, essa pasta de volumes pode ser editada fora? Ou é uma pasta read? Você pode...

**[01:37:39]** executar ela de fora também não tem problema você pode escrever colocar arquivos geralmente a galera quando está desenvolvendo costuma colocar o volume a pasta que está o projeto e ele já vai atualizando dentro do container você pode fazer essa interação aqui dentro massa funciona não funciona migrações mas antes da gente discutir a migração fizeram uma pergunta muito interessante alguns minutos atrás né tipo assim ah qual que é a diferença do

**[01:38:14]** O Breno fez uma pergunta, qual é a diferença do compouso para o Kubernetes? Ou Kubernetes mesmo, como a gente fala no Brasil? Então, qualquer ideia. O Docker Compose, ele é uma ferramenta para a gente usar em ambiente de desenvolvimento para essa tensão. Em ambiente de desenvolvimento. Ou em ambiente de produção muito pituxos, assim.

**[01:38:38]** A ideia dele é simplificar esse ambiente, a gente precisa subir as coisas, roda tudo, sobe, vai, e pega e naip, sabe? Tipo assim, nesse sentido, vai subindo as coisas e funciona. O Kubernetes, ou Docker Swarm, ou qualquer outra ferramenta desse nível, eles são ferramentas de orquestração. Ou seja, se eu preciso atualizar o código aqui no Docker Compose, eu tenho que tirar a aplicação do ar e subir de novo. E aí o que que acontece?

**[01:39:11]** Eu vou ficar, dar um sign, vou ficar com a aplicação parada. As ferramentas de... de orquestração, a gente vai pegar as ferramentas de orquestração...

**[01:39:25]** E, por exemplo, faz um novo deploy, aí ele cria um novo container com a versão nova, e aí ele sabe, tipo assim, são muitas coisas que vão ser feitas ali nesse momento. Ah, a aplicação está recebendo muitas requisições, o container não está dando conta, aí ele sobe dois containers da mesma coisa. Saca?

**[01:39:51]** Então, você vai rodando isso aqui e a ideia do Kubernetes ou do Docker Swarm é fazer orquestração de containers. O Docker Compose, a ideia dele é só rodar os containers em ambiente de desenvolvimento. Por isso que não é recomendado usar em produção. Obviamente, se você for fazer uma coisa pequena, é uma aplicação simples, suave, usa o Compose, tá tudo bem. Não tem nenhuma que estigma contra isso. Não, porque é corretude, não sei o quê. Não, mas tipo assim, saca.

**[01:40:22]** Tem que tomar um certo tipo de cuidado com essas coisas. Massa? Legal. Aí o Rogério perguntou, é obrigatório eu criar o container da aplicação? Se eu quisesse usar a aplicação na minha máquina e o pôsico de um container, era para criar o Compose só com pôsico? Sim. Sem problema nenhum. Vou derrubar ele aqui contra o C. Vou comentar todo o código da aplicação aqui. Subi aqui. Compose up. Pronto. Subiu só o banco de idade. Massa?

**[01:40:56]** Pode ser. Mas a ideia da imagem é porque é essa imagem docker que a gente vai fazer deploy dela. Massa. Então é essa imagem. O container aqui tá pela o pôsso dos aqui pelo momento né pra gente saber e fazer a configuração roda tudo direitinho. Mas a ideia é que a gente rode em produção a gente vai subir esse container para a plataforma que é o Fly.io que a gente vai usar a gente vai subir o container buildado para lá. Massa.

**[01:41:29]** Então, vamos resolver o problema das migrações aqui. E aí, o problema das migrações aqui, eu vou criar um arquivo aqui que eu vou chamar de entrypoint.sh. Então, é o ponto de entrada aqui. Ah, eu dá pra subir o compouso falando só o nome do container, não precisa comentar. Sim, também, mas aí, tipo assim, mano, se eu for explicar o compouso inteiro, a gente não vai embora hoje.

**[01:42:03]** Legal, aí o que que acontece aqui? Eu vou trocar, eu vou criar esse arquivo chamado entrypoint aqui, que a gente criou agora, entrypoint.sh, e ele é um shell script aqui, né? E aí, qual que é a parada? Aqui dentro do Dockerfile, você tá vendo que a gente tem um cmd aqui, que é tipo assim, roda esse comando e esse comando vai ficar rodando pra sempre.

**[01:42:29]** eu não quero esse comando rodando aqui é legal isso aqui funciona quando eu tiver que rodar mas dentro do compose eu preciso garantir que a migração sempre seja executada independente de quando estiver acontecendo então a gente vai criar esse arquivo entre ponte que substitui essa chamada do cmd aqui dentro massa então em vez de chamar o cmd ele vai chamar isso aqui aí ele vai rodar as migrações

**[01:42:59]** Poy to Run Alimbic Upgrade Red e depois ele vai rodar a aplicação. E é que é Fast API Zero, né? Quero que a gente tenha feito. Então, sempre quando a gente for rodar aqui, a gente pode chamar só o que precisa aqui, né? Então, ah, beleza. Eu preciso rodar mais uma outra coisa aqui antes de subir o container. Mais uma outra coisa. Aí você pode colocar tudo aqui. Isso aqui para o ambiente de desenvolvimento que a gente está montando. Para a produção, a gente não vai rodar a migração toda vez que sobe o container, não faz sentido.

**[01:43:31]** Massa, e aí a gente vai colocar esse entry point pra rodar aqui dentro do compose. Mas você pode colocar em qualquer lugar aqui, vou colocar embaixo do build. Aí agora, quando a gente subiu o compose aqui, em vez de rodar aquele cmd, ele vai rodar isso aqui, né? Unable to find entry point. Será que eu escrevi errado? Talvez. Pera aí, onde que eu tava aqui?

**[01:44:33]** Beleza, ele deu certo, mas deu errado, pera aí. Ah, eu preciso fazer o build, né? Eu preciso buildar, né? O contendo, ele tá tentando rodar uma coisa que não tem, então vamos lá. Docker, compose, aí eu posso fazer o build aqui, pra ele buildar a imagem, fazer o build. Vamos ver se agora vai. Fizemos o build, a gente pode dar o up. Se você quiser, você poderia rodar o build direto, também se você quiser esse aqui.

**[01:45:16]** Aí beleza, ele deu erro aqui, tipo assim. A OCI Runtime Created, Runtsecreated, Failure, Neighbor to Start Container Process, ErrorDuringContainer, Init, Exec, etc. Permission Denied. Então eu vou dar essa permissão aqui de execução, chmod mais x pro entry point. E vamos rodar de novo aqui de novo, vou fazer o build, não precisa, mas tudo bem. Pronto. Refaz o build, rodou aqui, olha que interessante.

**[01:45:56]** Olha o que ele fez aqui, no primeiro começo ele já está dando aqui, que ele rodou a migração e subiu o serviço aqui. Se a gente for lá agora na aplicação, em teoria tudo tem que estar funcionando. Execute, beleza, temos o ID aqui. Legal, se a gente der um get executar, não estamos autenticado, precisa logar aqui, pronto, está aqui o nosso user. Está funcionando tudo que a gente já feita dentro da aplicação até agora e o banco de dados está de pé.

**[01:46:46]** Legal? E aí, se a gente quiser parar o container, a gente pode dar Docker Compose Down. Daaam... Assim. Aí ele desfaz a rede, tudo mais, descreia os containers e tudo mais. Aí você fala, eu queria rodar isso aqui e ficar rodando sem ocupar o meu shell. E aí você pode dar um Docker Compose, por exemplo, menos D, que é ele desagarra, detete do shell. Beleza, tá rodando aqui.

**[01:47:17]** Aí você pode mexer com o que você quiser aqui, dó, quer compose. Aí você fala, eu quero baixar, né? Que foi o que o Elial tinha falado aqui. E eu quero baixar a aplicação, eu quero ficar só com o contêndulo rodando. Aí você pode falar down, fast api, app. Como é que é o nome do serviço? Já não lembro mais. É fast zero app. Legal. Aí você fala, eu quero derrubar esse aqui. Aí ele parou de rodar só um. O banco de dados ainda vai ficar rodando.

**[01:47:49]** E aí, da mesma forma, você poderia dar o up para cada um também. Saca, ah, eu quero dar o, sei lá, down em todo mundo, mas eu quero rodar só o FastZeroDB. É deitabase, né? FastZero deitabase. Legal. Aí, ele subiu só o banco. E aí, a aplicação se roda na tua máquina. E aí, você vai fazendo essa coisa se você quiser. Aí, você dá o up, ele sobe tudo, down, deleta tudo.

**[01:48:26]** e o "-d", olha, se você precisar rebuildar a aplicação, sei lá, você mudou algumas coisas, você pode dar um up, "-build", ele refaz o build e sobe de novo, e aí é contigo. Mas ele só vai rodar se tiver alguma diferença aqui dentro. Massa! Então, aí agora você tem um ambiente que é compartilhável entre todas as pessoas, a gente pode rodar ele da mesma forma em todas as aplicações. E o backup do volume do banco.

**[01:49:01]** Eu não vou falar sobre isso porque a gente não vai rodar o banco em produção, mano. A gente vai rodar o banco em outro lugar, né? Isso aqui é só o ambiente de desenvolvimento. Então eu não quero fazer backup do banco de desenvolvimento. Saca? Faz sentido? Porque isso aqui é só o ambiente de desenvolvimento. Em produção a gente vai usar o postgres do FlyAiota, entendeu? Aí lyrs, gerencinho, backup, lyrs fazem tudo. Isso aqui é só o ambiente de desenvolvimento.

**[01:49:36]** A gente pode falar sobre isso em outro momento, mas não é aqui o ponto. Antes de a gente finalizar aqui, eu queria falar passar um recado. Lembra que a gente não está usando mais o IOSkenlight, né? Então a gente pode remover ele do projeto. Então, uma coisa menos para estalar. Se a gente der o build agora, ele vai rebuildar porque mudou os arquivos. Mas aí enquanto ele roda aqui, eu vou comentar isso aqui para a gente

**[01:50:25]** Subi, aí quem precisar do código fonte está todo aqui. Vou parar tudo aqui. Down. Vou subir. Dá um push. E aí, beleza. Vocês têm algumas perguntas para fazer aqui? Mas sim, é muito bom, mas sim. Vocês têm alguma pergunta para fazer? Tem alguma coisa que vocês querem saber?

**[01:50:52]** Enquanto eu vou finalizando aqui, vocês mandam umas dúvidas e tudo mais. E desculpa por ser tão corrido assim, mas é que é muita coisa. Pensa que a gente queria só usar o docker, eu passei um tempo explicando algumas coisas que fogem um pouco do caminho aqui, mas espero que tenham feito sentido as coisas. Bom, na próxima aula, a gente vai conversar um pouco sobre a integração contínua. A integração contínua é o processo de rodar os testes lá no GitHub, por exemplo.

**[01:51:24]** com GitHub Actions, por exemplo. Não só no GitHub funciona com qualquer outro sistema, né? A ideia é que toda vez que a gente coloca o código no repositório, toda vez que a gente dá um push, ele executa os testes, faz algumas validações, vê tudo o que precisa acontecer e aí ele fala se aquele código pode ser integrado ou não lá dentro. Massa? E bom, aí suplementar para a próxima aula, para quem quiser.

**[01:51:55]** Dá uma olhada nisso antes. Tem uma live aqui com Will, que é essa aqui, a 170, que ele explica pra gente um pouco sobre o GitHub Actions, e a gente vai configurá-lo no nosso projeto. Então, quem quiser já chegar na IC. Bom, lembrando, tem o Quiz. Sempre tem o Quiz. Então tem várias questões nessa aula, respondam o Quiz. E essa aula não tem exercícios.

**[01:52:28]** Mas essa aula não tem exercício de propósito, porque o exercício vai ser fazer tudo isso funcionar na tua máquina, porque vai dar um trabalhão, né? Então...

**[01:52:44]** Espero que vocês dêem uma olhada com carinho, tentem subir, tentem rodar os containers aí. Esse é o exercício, vai dar muito trabalho. Tipo assim, vai ter que ficar revendo a aula. Onde muda? O que que muda? Qual o parâmetro? Aí o yam meu quebra e tudo mais. E no feriado vai ter aula, vai ter aula assim. E aí uma coisa aqui que eu tenho que falar é o seguinte. É o seguinte. Antes da gente ir embora.

**[01:53:16]** Tenho que responder as perguntas, né? Então, vamos lá. Quinta vai ter aula? Vai ter aula. Ah, obrigado. Muito brabo. Valeu, estamos junto. Estou com um problema para fazer tudo desfuncionar. Então, é agora que entra o grupo e tudo mais. Legal. Alguém tinha feito uma pergunta aqui para mim que eu não consigo mais achar? Que o Lúcio fez uma pergunta assim o seguinte. Você comentou que não usa o Dock, e usa o que e por quê?

**[01:53:49]** Feriado é só para ser ele teis, exatamente. Eu não gosto de usar o Docker. Eu já usei muito Docker no passado, mas o Docker tem alguns problemas com licenciamento mais recentemente, principalmente para quem usa plataformas Microsoft, tudo mais. Não é o meu caso, mas eu me incomodo com as licenças do Docker. Aí, agora, eu tenho usado Podman, que é um outro projeto para rodar containers e tudo mais. Ele é aberto e...

**[01:54:24]** tem um pouco menos de problemas e tal, com esse negócio de licenciamento e tal, ele faz as mesmas coisas, funciona muito bem e tal, e é o que eu tenho usado, é o Podman. Em alguns outros casos, eu tenho usado ContainerDi com NerdCTL, que também é uma outra forma de fazer isso ser aberto e tudo mais. Nas minhas máquinas virtuais, eu tenho usado o NerdCTL com ContainerDi.

**[01:55:01]** na minha máquina que eu tenho usado o podman tanto que e uma coisa e uma coisa eu não uso podman desktop eu uso podman mesmo e aí tudo isso que a gente fez aqui está vendo que a gente subiu docker compose e tudo mais é tudo compatível com podman eu poderia fazer o seguinte podman compose up legal tá rodando aqui que eu preciso dar o build né menos menos build aí ele vai pegar aqui minhas imagens e tudo mais tipo assim da mesma forma mudei um

**[01:55:38]** Eu mudei o comando, tá ligado? E continua tudo funcionando, é tudo retrocompatível e tudo mais. Então funciona super bem assim. Então no dia a dia eu tenho usado o Podman na minha máquina durante o meu ambiente de desenvolvimento e em produção das minhas VMs eu tenho usado o Nerd CTL. Aqui funcionou tudo, top. Top demais. Beleza, massa? Alguém tem mais alguma pergunta? Pra gente liberar o pessoal?

**[01:56:15]** para a galera dormir, descansar, o que é escorrido nada, muito melhor que o que lhe, sensacional. Pô, tamo junto, valeu demais. O resto fala que na Red Hat tem um curso de pod, mano, gratuito. Eu não tenho certeza, eu tenho dificuldade em entrar no canal específico do curso no Telegram. Me manda mensagem, mano, entra no grupo da live de Python, eu não sei se você tá lá, e aí qualquer coisa eu te adiciono lá. Massa? Então eu vou ficar por aqui, vou liberar vocês, ó, beijinho.

**[01:56:56]** A gente se vê na quinta-feira, pra falar sobre integração contínua, botar isso tudo pra rodar, bonitinho no répo. Beijinho pra vocês, ó! Tchau!

