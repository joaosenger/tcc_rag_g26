# Transcrição da Aula: aula-04.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:05]** Olá pessoas, boa noite, eu sou o Dono Sauru e boas-vindas a mais uma aula do nosso curso de Festa API. Antes de a gente começar, eu queria aquele feedback de vocês, vocês estão me ouvindo, vocês estão me vendo, se está tudo funcionando bem, se não está, para a gente poder ir tocando a aula aqui.

**[00:00:24]** Bom, enquanto vocês vão se acostumando, o streaming vai começando aí pra todo mundo, eu já vou dando as introduções aqui, mas se vocês falarem, pô, não tô ouvindo, não tá funcionando, aí a gente reveu o que precisa acontecer aqui. Bom, hoje a gente vai falar sobre a configuração do Banco de Dados e sobre o sistema de migrações, né? Então, são duas coisas que precisam andar juntas, né?

**[00:00:51]** a evolução da nossa aplicação. Bom, pra quem nunca ouviu falar essa palavra migrações, eu vou dizer que é uma forma de ter um banco de dados que a gente chama de evolutivo, né? A gente pega, tem uma versão do software com uma versão específica do banco de dados. Quando a gente versionar o software de novo, talvez o banco precise estar em outra versão, então ele vai evoluindo, né? E o banco de dados, bom, é onde a gente salva os dados, não tem muito pra onde correr.

**[00:01:20]** Bom, se todo mundo me deu boa noite, eu acredito que vocês estão me ouvindo e o vídeo está legal. Então, vamos seguir. Antes de tudo, como sempre, vale lembrar que esse material está em texto, todo em texto. Então, se alguém precisar, dá uma olhada no material, dá uma revisada, está tudo aqui. Então, tudo que eu estou falando está escrito. Eu preferi tocar aqui a ordem um pouco diferente da escrita, mas no final vai dar o mesmo resultado. Massa!

**[00:01:50]** Então vamos lá. Sobre o que a gente vai falar hoje? Então a gente vai introduzir duas ferramentas, o SQL Alchemy e o Alembic. O SQL Alchemy é um toolkit de banco de dados, ou seja, uma ferramenta para a interação de banco de dados de várias formas e o Alembic. A gente vai instalar essas ferramentas, a gente vai configurar e criar o nosso primeiro banco de dados, a gente vai entender como...

**[00:02:15]** Como funciona o esquema de criar tabelas no banco de dados, sabe? Aonde que essas tabelas ficam? Como é que essa coisa vai funcionando? Aí, por último, a gente vai ver os testes, a integração, né, de alguns eventos do SQL Alchemy e a gente vai falar sobre as migrações lá no fim. Então, é o nosso último tópico do dia hoje. Legal? Então, vamos partir daqui. O Osnil falou que tá tudo bem, que ele tá me ouvindo, então... Massa, obrigado.

**[00:02:46]** Bom, então vamos fazer uma introdução ao SQL Alchemy aqui, que é essa ferramenta que eu falei tanto e tudo mais. Vamos lá, o SQL Alchemy, eu coloquei aqui que ele é um ORM, mas eu não gosto muito dessa definição aqui. O SQL Alchemy é um ORM, porque ele contém um ORM. O ORM está contido dentro da biblioteca do SQL Alchemy. E a ideia dela é permitir com que a gente consiga

**[00:03:11]** trabalhar com banco de dados, ou seja, SQL ou SQL, para quem prefere falar como a Luciana de Menes, de uma forma mais natural em Python. Vamos dizer assim. Existem toolkits e ORMs para todas as linguagens de programação. Existem outros, fora o SQL Alchemy no Python. Eu escolhi esse porque eu gosto bastante. E a ideia é pensar em não escrever SQL puro, SQL na mão, sabe?

**[00:03:37]** Select, total, total, que são strings e tem algumas coisas ali, que às vezes são um pouco perigosas de spoil e tudo mais, e transformar isso num esquema de Python. Ou seja, a gente vai codificar Python de fato e essas interações que a gente vai fazer com o código Python são refletidas no estado ou nas condições do banco de dados. Massa? Então, é nesse sentido que a gente vai conversar aqui.

**[00:04:08]** O RM, é uma outra palavra que a gente tem que falar aqui nesse momento, o RM significa mapeamento objeto relacional.

**[00:04:19]** O de Object, R de Relational, M de Mapper. E o que a gente quer dizer quando a gente está falando sobre mapeamento de objeto relacional, tipo assim, pô, é muito esquisito, mas o nome diz exatamente o que está acontecendo. Quando a gente tem um banco de dados SKL, de uma maneira geral, a gente está falando sobre banco de dados relacionais. Banco de dados SQL, SKL, significam banco de dados que usam a linguagem relacional de uma forma geral.

**[00:04:48]** E quando a gente fala de objeto, a gente está falando de objetos Python, de uma maneira geral. Queria uma classe, faz um item, atributos, tem métodos e tudo mais. E a grande ideia de um ORM é fazer o mapeamento entre as relações do banco com os objetos do Python. Parece esquisito de falar dessa forma, sabe?

**[00:05:12]** Ah, é uma coisa muito abstrata. A gente vai ver, mas a ideia é basicamente essa. A gente vai criar classes em Python.

**[00:05:20]** que significam linhas ou colunas e tabelas. E tudo isso a gente vai fazendo a linguagem de programação. E aí essas coisas são mapeadas por essa ferramenta, que é o ORM do SQL Alchemy, para o banco de dados. Então todas as interações que a gente faz com o banco, elas são intermediadas por essa ferramenta, que é o SQL Alchemy. Massa? Então...

**[00:05:45]** Por que a gente precisa disso? Essa é uma pergunta bastante interessante, porque muitas vezes você vai falar, ah, mas são coisas simples, eu adoro fazer a Skel na mão e tudo mais. Tem alguns pontos que são interessantes de a gente usar um RM. Uma das coisas, sei lá, que a mais vendida de todas é que assim, a gente pode trocar de banco de dados.

**[00:06:07]** Eu não acho que essa é uma grande vantagem. Meu Deus, amanhã vou trocar o meu banco. A gente vai fazer isso durante o curso, né? Então, por isso eu coloquei isso aqui como um ponto positivo. A gente hoje vai trabalhar com um banco de dados que se chama SK Lite.

**[00:06:20]** Ou seja, SQL, Light de pequeno, ele é um arquivo e tudo mais, não é um servidor de banco de dados grande, que escala e tudo mais, é uma coisa feita para rodar no nosso próprio dispositivo ou para a baixa carga, que é uma coisa que a gente pretende. Mas quando a gente for rodar isso em produção, a gente não sabe o que esperar em produção, então a gente vai emigrar de banco de dados, a gente vai para o Postgres SQL. E aí o Postgres...

**[00:06:45]** É um outro banco mais robusto para a produção, para um monte de coisa. E o fato de a gente usar o ORM ou SQL Alchemy de fato, significa que como a gente está interagindo no nível de Python, as idiosincrasias de cada banco, as particularidades de cada banco, elas não importam muito para a gente, porque pelo simples fato de a gente abstrair essa camada com essa ferramenta, com esse toolkit de banco de dados.

**[00:07:13]** Um segundo ponto interessante aqui é esse fato de segurança. Segurança é mais de uma forma de segurança mesmo, assim. Quando a gente lida com strings, strings permitem algumas vulnerabilidades bem clássicas de SQL e tudo mais.

**[00:07:29]** que grande parte das bibliotecas de banco até previne esse tipo de comportamento, mas dentro de uma abstração como o SQL, que a gente está protegido de coisas como escape de consultas, tipo assim, a gente passa uma string que vai ser completada em algum lugar, sabe? Ou ingessão de SQL, que é quando alguém, você vai falar tipo assim, select, não sei quem veio no parâmetro do endpoint, por exemplo.

**[00:07:55]** a select users, onde o usuário é o ID que a gente trouxe, aí alguém pode concatenar nisso, fazer uma injeção de SQL para rodar uma outra coisa, deletar um recurso e tudo mais, então a ideia mais ou menos é essa, então tem algumas camadas de segurança que são resolvidas aqui dentro disso.

**[00:08:19]** E o terceiro ponto, que é o que eu acho que é o mais primordial de todos, embora a segurança seja muito importante, é a gente poder ter uma eficiência. Eu não diria que é mais eficiente, mas ter uma eficácia melhor na hora de lidar com conexões de banco e pensar em coisas como a gente integraria a aplicação e o banco de dados e todos esses tipos de coisas. Então, o R&M ajuda a gente a fazer isso.

**[00:08:49]** Aí eu tomo as perguntas se dá pra usar a LAMBIC sem uma RM. Não. Inclusive a LAMBIC ele é atrelado ao SQL Alchemy especificamente. Cada RM tem o seu sistema de migrações de uma maneira geral. Mas você pode fazer migrações sem um RM, mas não com uma LAMBIC. Massa? É pra sim. Dá pra usar sem um RM.

**[00:09:12]** Deixa eu reformular a minha resposta, que dá para usar sem ORM, porque o SQL Alchemy ensina um ORM somente, mas você precisa ter uma forma de fazer esse mapeamento do banco. Então, você poderia fazer isso com SQL Alchemy Core, por exemplo, sem usar o ORM. Então, em teoria funciona, mas você depende dessa coisa. Massa? O Thiago fez uma pergunta aqui muito interessante, ele falou, tem alguma diferença de performance ao usar um ORM ao invés de SQL? Bruto, tem.

**[00:09:42]** Como qualquer camada de abstração vai trazer uma diferença de performance. Então, por exemplo, em vez de trazer um monte de tupla do banco de dados, ele vai transformar isso em objetos Python e tudo mais. Então, essa transformação tem um custo. Aí, a pergunta aqui é tipo assim, o custo é muito elevado e a resposta é não. Ainda vale a pena usar o RM.

**[00:10:08]** em quase todas as ocasiões tem lugares muito específicos que isso seria custoso demais mas na grande maioria não tipo assim 99% dos casos vai funcionar tudo bem às vezes tem uma busca no sistema específico mas são coisas muito pontuais assim

**[00:10:28]** Então, legal, vamos adicionar o SQL Alchemy dentro do nosso projeto e vamos ver como é que se funciona, como é que ele se comporta e tudo mais. Aí a gente vai vendo, né? Porque eu entendo que para quem nunca trabalhou com uma coisa dessa pode estar muito abstrato. Eu falei que tinha aquela aula suplementar para dar uma olhada, mas às vezes você não teve tempo e está tudo bem, saca? Então, vamos lá, vamos adicionar o SQL Alchemy aqui. Então poetry, edge, SQL, alchemy.

**[00:10:57]** A Poetry S, que é L... Esqueci um... Alchemy. Esqueci um L. Legal. Aí ele instalou duas dependências aqui, o Greenledge, que é uma coisa muito especial para poder performar coisas acíncronas. A gente vai falar sobre isso lá na aula 8, mas ele vem com um SQL Alchemy aqui. Legal. Temos o que a gente precisa. Está instalado no nosso projeto.

**[00:11:21]** E aí, qual que é a cara do ORM de uma forma geral? Eu vou pensar naqueles dados que a gente colocou na aula passada, que era o username, o password e o e-mail. Antes da gente ver essa confusão aqui, eu vou levar vocês lá para o código e depois a gente vai definindo passinho por passinho aqui. Legal? Aqui, eu vou criar um arquivo novo dentro do nosso projeto que eu vou chamar de Models.

**[00:11:47]** Massa são modelos de banco de dados. Então, Ctrl C, Ctrl N aqui no meu editor, model.py. Legal, e qual que é a ideia, né? Lembra que a gente estava falando sobre... Lembra que a gente estava conversando sobre essa troca, né, de ter um objeto?

**[00:12:10]** que é modelado para ser compatível com o banco de dados. Então, a gente faz esse esquema aqui. Então, eu vou criar um class, e aí eu vou criar essa classe aqui, deixa eu aumentar um pouco a fonte. E nessa classe, a gente vai chamar ela de user, que é o modelo que a gente quer representar, que era o cadastro de usuários que a gente estava fazendo na aula passada. Então, eu vou chamar de user. Para cada um desses campos, a gente tem algumas relações super simples daqui. Então, por exemplo, a gente tem o username,

**[00:12:38]** que é uma string, basicamente aquele modelo que a gente fez no PiDentic. A gente tem o email, que também é uma string, a gente tem o password, que também é uma string. Basicamente, o que a gente precisa fazer aqui é pegar essas coisas que a gente tem aqui e juntar isso

**[00:13:03]** para que isso seja refletido no banco de dados. Então, para isso, existem algumas coisas aqui dentro do SQL Alchemy que vão simplificar isso aqui para a gente. Vamos lá. Quais delas, né? Então, eu vou vir aqui do SQL Alchemy. Então, fromsqlalchemy.orm import mapper. Maped. É isso aqui que eu quero. E aí, o que que acontece aqui? Lembra que...

**[00:13:30]** Quando a gente costuma usar o SKE Alchemy, assim, ou qualquer outro banco de dados, geralmente quando a gente tá conversando com um banco de dados ou alguma coisa nesse formato, a gente sabe que a representação do dado no banco, por serem árvores binárias e tudo mais, elas não seguem mais ou menos esse formato. Sei lá, no SKE Lite, por exemplo, isso aqui não é uma string, né? É um varchar.

**[00:13:58]** Então essa ideia do MAPED aqui, ela vai fazer aquele esquema do mapeamento relacional. Então ele vai transformar esse campo string no mapeamento de alguma coisa que seja compatível com o banco. Ou seja, é um varchar daqui pra lá. Então dentro do Python a gente vai tratar isso como uma string e estamos mapeando pra gente poder trocar essa ideia de um lado pro outro. Então essa é a ideia do mapeamento aqui.

**[00:14:29]** Então, map it, map it. Então, independente do que seja no banco de dados, como o banco de dados aqui, como o RML é agnóstico do banco de dados, a gente não precisa saber, né? Ah, é no Postgres e tal, ele vai dar conta de resolver essa relação aqui dentro. Massa? Então, esse é o principal ponto que a gente tem aqui.

**[00:14:57]** Uma coisa importante aqui dentro é que lembra a gente criou um ID, né? Toda a tabela tem que ter um identificador, né? Então a gente vai falar aqui um ID. E aí o ID também é mapeado e ele é um inteiro, né? Gente.

**[00:15:10]** Um outro campo que eu queria adicionar aqui, que é uma coisa interessante aqui dentro, quando a gente faz esse tipo de coisa, a gente costuma colocar um campo que eu acho legal. Vocês já usaram alguma aplicação que ela manda assim pra você, tipo assim, ah, legal, faz 10 anos que você está com a gente, um ano que você está cadastrado no nosso sistema, ou qualquer coisa do gênero, vocês já viram isso? Então, eu vou fazer esse campo.

**[00:15:37]** que é quando esse registro foi criado aqui na minha aplicação. E aí também é um MAPED, só que isso aqui é uma data, né? Então, ah, quando é que foi criado esse registro na nossa aplicação? Então eu preciso saber, usando a biblioteca-padrão do Python, a gente pode usar o datetime, né? Então fron, datetime, import, datetime. Tá vendo como é super simples essa relação que a gente cria aqui? Então isso aqui é como vai ser...

**[00:16:08]** uma tabela do Banco de Dados. A gente tem os campos que vão representar as colunas. Então um ID, o username, o email, o password, o created at, então você está vendo que a gente vai criando essa relação aqui dentro e isso não deixa de ser um objeto Python, mas ao mesmo tempo ele é um objeto Python que representa a tabela do Banco de Dados. Faz sentido isso aqui que eu estou falando para vocês? Eu estou falando grego? Conversem comigo.

**[00:16:39]** Vamos fazendo junto. Enquanto isso, eu agradeço a Ju. Ju, obrigado pelo Super Chat. Valeu, tamo junto. O Resny falou que também me mandou um pico. Obrigado. Ó, tamo junto. Valeu demais. Beijo pra vocês. A gente tem uma pergunta. Pra fazer o DQL em vários bancos de dados, eu preciso consultar cada um deles. Existe uma forma...

**[00:17:05]** de fazer a mesma consulta para todos. Existe uma forma de fazer, existe multi-ten, tem várias formas de resolver isso, mas foge de total do nosso escopo aqui da aula. User seria uma tabela, sim, é exatamente isso aqui, o que está acontecendo aqui. E aí uma coisa que a gente pode falar aqui é dar o nome dessa tabela, então eu vou colocar aqui como a table name, e aí eu vou falar que o nome dessa tabela é users, no plural, porque é uma tabela.

**[00:17:34]** que tem vários users, né? Então, cada uma dessa coisa representa uma linha do banco de dados, mas isso aqui representa todas as colunas ao mesmo tempo. Massa! Então, é esse o esquema aqui dentro. Ok, legal! Isso aqui é um Python puro, mais ou menos, né? Só que a gente precisa começar a adicionar coisas do banco de dados aqui dentro.

**[00:17:57]** Então, pra eu dizer, né, pro SQL Alchemy, que isso aqui é uma tabela, de fato, então eu preciso juntar essas coisas, né? Ó, o Germano falou que tem mais gente assistindo do que like, hein? Por favor, ajudem isso a chegar em mais gente. Então, a gente pode pegar isso aqui e chamar esse objeto do SQL Alchemy que se chama Registry, né? Registry significa que ele vai registrar

**[00:18:25]** as coisas que serão mapeadas entre a aplicação, entre as tabelas Python e as coisas no banco de dados. O nome é bastante intuitivo, né? Como a gente fala, quando a gente fala isso aqui, né? Pô, o que que é? É um registry. Então, ele é uma coisa que contém todos os registros juntos. Eu vou chamar isso aqui de table registry para ficar explícito, né? E aí, a gente vai registrar essa tabela.

**[00:18:58]** Como Maped as Data Class, ou seja, é uma classe de dados. Pô, é super simples, né? Tipo assim... Pô, parece uma magia, uma coisa, muito maluca, né? Tipo assim... Pô, como é que uma coisa vai interagir com a outra? E a sintaxe do SQL é algo que me ajuda muito a gente a fazer isso aqui, né? Basicamente, com isso, a gente registrou, né? Com um table registry, todas as coisas que a gente quer que sejam objetos, que na verdade são tabelas do banco de dados. Massa, fez sentido isso aqui? Massa?

**[00:19:38]** É uma pergunta sincera. E aí a gente tem todos os campos que a gente precisava aqui. Uma coisa completa a outra, exatamente. Você vai dando todas as coisinhas, todos os dados e vai dando tudo certo no ano final, né?

**[00:19:54]** parece muito complicado quando as pessoas falam nossa o rm e tal não tipo assim object relational mapper tipo é básico de você olhar o código você consegue entender né ele é bem explícito acho que ele é o que é lindo por conta disso bom uma coisa que a gente tem que considerar aqui dentro é o seguinte quando a gente está usando essas coisas o banco de dados ele tem algumas propriedades para que a gente precisa

**[00:20:21]** que a gente precisa dar para poder interagir com ele. Então, por exemplo, eu preciso falar que esse ID é uma chave primária, ou seja, uma coisa que o banco vai usar para gerenciar e encontrar cada uma dessas coisas. Então, vamos lá. Eu trouxe um outro slide aqui. A gente tem essa coisa que se chama Maped Column, ou seja, é o mapeamento específico dessa coluna. Tem coisas do banco de dados ou coisas que a gente...

**[00:20:51]** precisa dizer aqui que a gente vai só dar mais informações, né? Então, vamos preencher isso aqui. Então, a gente vai precisar desse Maped Column aqui. Então, vou importar aqui. Maped Column. E aí no Maped Column, eu vou falar o seguinte aqui. O campo ID, né?

**[00:21:12]** Aqui ele é a chave primária dessa tabela, né? Ele é um registro único que não se repete, que é auto gerado pelo banco de dados. Então a gente pode vir aqui e falar o seguinte, primary key, true. Ou seja, agora isso aqui é a chave da nossa tabela no banco de dados. Ou seja, toda vez que a gente insere um registro, esse registro vai para lá e ele vai ser auto incrementado e vai rolar toda a coisinha que precisa acontecer aqui dentro. Massa.

**[00:21:41]** E aí, uma outra coisa que eu quero dizer é o seguinte, eu não sei qual é o ID da tabela, né? Porque toda vez que eu precisar dar o dado daqui pra lá, eu precisaria passar isso pra essa tabela, né? Como um argumento na hora de montar esse objeto. E eu não quero, né? Então eu vou colocar aqui init false.

**[00:22:01]** Então, a partir desse momento, a gente sabe que, quando chamarmos o objeto e o user, a gente não vai precisar passar o ID, porque o ID é gerado, gerenciado pelo banco de dados, e essa é a chave primária da nossa aplicação. A gente pode usar isso em vários lugares, em todos os campos que a gente quiser. Então, por exemplo, aqui, eu vou... Eu vou dizer, no created edge, que eu não quero passar a hora que esse objeto foi criado, né? Então, ele também recebe esse init false. Olha que massa!

**[00:22:32]** E aí tem mais algumas coisas que eu quero dizer aqui, por exemplo, como eu não vou passar o momento em que o objeto foi criado, a gente pode dar pra ele simplesmente falar o seguinte, olha, default, então a gente pode ir falar que o server default, tem o default e tem o server default, é importante falar sobre isso, mas aqui vamos lá, server default, e aí o default aqui...

**[00:22:56]** Ou seja, default significa, na falta de alguma coisa, quando esse parâmetro não for passado, como ele é init false, ele nunca vai ser passado, a gente vai pedir para ele pegar a hora do banco de dados, não a hora da aplicação. Então aí a gente vai passar um funk aqui e a gente vai chamar de now. Funk now. Ele vai executar...

**[00:23:17]** essa função do banco de dados a hora que esse registro for criado, então funk now. Aí você vai falar, bom beleza, da onde vem esse funk? Esse funk vem do SQL Alchemy, então from SQL Alchemy import funk. Legal, então a gente tem agora esse mapeamento e a gente diz uma coisa...

**[00:23:37]** para a outra aqui dentro. Tem mais algumas coisas que eu gostaria, por exemplo, ah, eu não quero que os e-mails, por exemplo, sejam duplicados na aplicação, então eu vou falar map.column.unique.true. Ou seja, eu não quero que esse valor se repita, eu não quero que dois e-mails iguais sejam cadastrados, tenham registros diferentes. E a mesma coisa eu posso fazer para username. A senha pode ser igual, não tem problema. Até esse momento está tudo certo. Então...

**[00:24:10]** username e email, eu não quero que se repita. E aí olha que interessante, a gente acabou de criar, a gente tinha uma tabela do Python, a gente mapeou os tipos do Python aqui no Mappet, e aqui no Mappet Column, a gente está dando as propriedades que essas coisas vão ter no banco de dados. Massa, então, beleza, o campo ID é inteiro em Python e algum valor que ele vai ter lá no banco de dados a gente não precisa saber.

**[00:24:42]** Não vamos passar esse dado e isso aqui é a chave primária. Então a gente começa a criar conexão entre as coisas. De um lado a gente tá criando a classe e do outro a gente tá criando as restrições da nossa tabela no banco de dados. Fez sentido que tá rolando aqui? Pergunta sincera aqui. Só pra ver se vocês estão acompanhando junto comigo. Aí algumas pessoas estão fazendo perguntando coisas de...

**[00:25:14]** Outras versões do SQL Alchemy, comparação com outro RM, eu acho que isso foge um pouco do escopo, mas a gente pode discutir sobre isso lá no grupo do Telegram depois. Mas isso foge um pouco do contexto do que a gente está falando aqui na aula, e eu vi que o JS deu algumas respostas e tudo mais aqui. Legal? Aí alguém fez um meme que tipo assim, ah, mensagem dizendo, alguém já tem alguma coisa pra você, né?

**[00:25:45]** Tipo assim, alguém já fez Unique True, alguém já tem essa mesma senha que você não cadastre, né? Aí alguém perguntou a estratégia de gerar uma chave, eu não entendi muito bem o que se dizer aqui, mas tudo bem, se quiser me mandar mais coisa e mais informações, eu consigo responder se for pertinente aqui. Então essa ideia de fazer essa correlação aqui lendo

**[00:26:14]** faz muito sentido, né? Olha, a gente vai mapear os campos, criar as colunas, as relações das colunas, a gente vai registrar essas tabelas no banco de dados. Pô, é muito massa, é muito massa. É muito descritivo, né? O que está acontecendo aqui. E aí, legal, tudo bem, vamos criar um teste agora. Vamos criar um teste bonitinho. Vamos rodar isso aqui e ver o que acontece. Eu vou lá no meu... na minha passinha de testes agora.

**[00:26:49]** E como isso aqui não é o app, mas são os modelos e tudo mais, a gente pode chamar de teste db. Isso ok? Então, teste tudo sempre tem que começar com teste, lembra? db.py. E aí a gente começa a fazer essa interação aqui, até para vocês verem como essa coisa é usada dentro do código. Então vamos lá, fromFest0, FestIPi0, que é o nome do nosso módulo, pontoModels.

**[00:27:15]** importe, a gente vai importar a nossa tabela de user, que a gente criou lá, aquela classe de user. E aqui eu vou criar essa flank com o mesmo nome aqui, só pra não me perder depois e ficar diferente dos lights, que é esse test create user. Acho que deu uma caidinha, né? Eu não sei se voltou ainda. Eu acredito que sim. Beleza, voltou? Legal, ok, massa. Então vocês estão de volta, significa que tá tudo funcionando.

**[00:28:11]** E qual que é a ideia aqui, né? Como é que a gente usa isso aqui? A gente precisa passar os campos que não são init, false, né? Ou seja, os campos que a gente tem que passar, ou seja, por default, todos são true, menos os que a gente fala que não são, né? Então, eu vou falar o seguinte. Ah, username, como é que a gente já feito aqui? Eu vou chamar tudo de teste, vai? Teste, a gente tem o email, que também vou chamar de, sei lá.

**[00:28:40]** O que eu dei aqui? A teste, a roba teste. E a senha que eu vou passar aqui para ela como um teste também, pode ser Secret. Eu coloquei aqui, vai. Secret. E basicamente essa é a criação de um registro aqui, né? Nessa interação é assim que funciona. Simplão, né? Bonitão, né? Vocês já pensaram em colocar coisas no banco de dados dessa forma?

**[00:29:14]** é super intuitivo, super simples, não requer nada demais. Olha que bonitinho. E a gente pode saber, né? Vamos, a gente está testando, eu vou escrever. Então, a sorte, eu quero garantir que o nome de user, por exemplo, ponto username, é igual a teste. Pô, legal, bonitinho, funciona, limpinho, deve nada pra ninguém, né? Muito massa. Então, eu vou rodar os testes aqui da nossa aplicação pra gente ver o que que acontece, então...

**[00:29:50]** Você pode dar poetry shell, eu vou dar um poetry run, task test. E aí eu vou rodar os testes aqui, ele vai falar alguma coisa aqui ó, lá no seu bloco, lá dos imports, tem um erro lá no registry. Eu vou dar um format para ele arrumar aqui, é aqui que está errado a ordem dos imports, format, legal.

**[00:30:16]** colocou bonitinho a ordem que precisava vou rodar um teste aqui e vamos ver o que que acontece beleza ele falou que passou teste está funcionando só que isso aqui não testa nada na realidade né só tá aqui tá aí legal é isso se a gente quisesse debugar isso aqui a gente poderia colocar aquele breakpoint que a gente viu na outra aula breakpoint aqui

**[00:30:44]** Rodar, a gente consegue ver o que é esse user, como é que ele funciona, né? Então, user, aqui ó, ele tem um ID NAN, um created at NAN, e os dados que a gente passou pra ele. Aí, bom, por que que esses dados aqui são NANs? Porque isso não tá interagindo com banco de dados de forma nenhuma. Você viu que a gente não tá passando nenhuma informação sobre o banco? Onde o banco tá? Do que veio? Pra onde vai? Saca.

**[00:31:16]** Então, é esse o ponto. E agora, o que que a gente faz? Porque parece que está tudo funcionando, mas não tem nenhuma interação com o banco, né? Tanto que eu coloquei aqui no slide. Aqui temos uma bomba, né? Uma brincadeira, né? Então, o que que a gente vai fazer? O que que esse teste testa, né? Ele testa se uma classe do Python pode ser instanciada. Ele não testa nada, né? Ou seja, nada.

**[00:31:44]** Eu queria colocar isso aqui porque geralmente a gente tem esse impulso de fazer a coisa da forma como a gente queria, mas ele não efetivamente testa nada. Para que a gente possa fazer isso aqui, a gente precisa criar essa tabela no banco de dados.

**[00:32:08]** E, pra isso, a gente usa uma coisa do SQL Alchemy, chamada metadato, né? Ou metadata, metadata, cada um fala de um jeito, mas a gente precisa dos metadados. E aí, quando a gente pega os metadados, a gente pode fazer a criação dessa tabela, em algum lugar. E depois a gente vai conectar com uma session pra fazer essa busca. Aí eu sei, tipo, nossa, é metadata, é session, é user. O que eu tô falando aqui?

**[00:32:37]** Vamos lá. O SQL Alchemy, ele é composto basicamente de duas coisas importantes, tem mais, mas por enquanto para o nosso momento aqui, a gente precisa de duas coisas. A gente tem a engine do banco de dados, que é o motor do SQL Alchemy, que é a hora que a gente conecta o banco

**[00:32:57]** com o código, né? Então a gente faz essa conexão, né? Então eu tenho que ter essa coisa, essa engine que a gente vai dar os dados de onde tá o banco, ou seja, conecta com o banco de dados, qualquer URL do banco, qualquer endereço do banco, onde que ele tá, qualquer senha e tudo mais. E a partir disso, a gente cria essa conexão e a gente vai usar essa conexão pra se comunicar com o banco de dados. E o segundo ponto, que é a segunda coisa que a gente precisa aqui, é a Session.

**[00:33:27]** E aí a sessão é quem faz esse movimento de pega o dado daqui, coloca para lá, transfere esse dado do estado do código para dentro do banco de dados. Então a gente vai fazendo essa correlação entre as duas coisas. Então além das tabelas, a gente tem a Engine e a gente tem a Session. Basicamente, se a gente for pensar nisso aqui, eu tentei fazer uma imagem mais bonitinha, né? Então a gente tem o RM do SQL Alchem.

**[00:33:55]** ele fornece essa session, porque a gente pode interagir. E aí dentro dela acontecem eventos e tudo mais. E aí a session, ela depende de uma engine, ou de uma engine, quem gosta de falar assim também, ou de um motor, alguma coisa assim, que se conecta com o banco de dados. Ou seja, então eu preciso fornecer esses dados para uma sessão de banco de dados, ou seja, uma comunicação ativa entre o código e ele.

**[00:34:25]** E aí essa session interage com os modelos e esses modelos podem executar determinadas coisas, ou seja, aquele modelo que a gente criou, aquela classe, ela tem metadados e tudo mais, e eles são mapeados para tabelas no banco de dados. Eu sei, ainda está confuso, pode ser. A gente vai voltando nesse desenho conforme for necessário, né? Então eu vou...

**[00:34:48]** tentar fazer toda essa conexão em um lugar de teste para a gente conseguir entendendo o que está acontecendo aqui. Olha como isso parece muito complicado, né? Parece, mas não é. Eu vou lá no nosso arquivo ConfTest, lembra que é um lugar onde a gente escreve bloquinhos de código de teste que vão ser reutilizados no ConfTest aqui. E aqui eu vou criar uma nova fixture.

**[00:35:15]** Mas antes disso eu vou só dar uma def aqui. Eu vou chamar essa de Session. Mas aí o que a gente precisa aqui? A gente precisa de alguns componentes do SQL Alchemy para poder fazer esse tipo de coisa. Eu preciso de uma Engine, né? Alguma coisa que se conecta no banco de dados que a gente vai usar. Então eu vou fazer tudo aqui, depois eu arrumo os imports, tá? Para ficar certinho, pertinho uma coisa da outra. Então vamos lá. From SQL Alchemy Import Create Engine.

**[00:35:47]** Massa, então aqui, eu vou falar pra ele, olha, cria uma conexão com o banco de dados. Aí, qual o banco de dados a gente vai se comunicar, como isso vai acontecer, qual é o caminho do banco, aonde ele está, a gente vai passar aqui dentro. Massa, e como a gente está usando SQLite em mem... A gente vai usar SQLite, ele tem uma função de usar em memória, né? Então, eu poderia falar o seguinte, SQLite 1, 2, 3, 2 pontos memory.

**[00:36:18]** E aí ele cria um banco de dados virtual, assim, memória que a gente pode ir jogando dados, consultando, só pra gente entender o conceito aqui por trás, né? Então a gente tem essa engine aqui, que é a conexão. Então a gente vai usar esse banco, que é o SQ Lite 3, pra quem não conhece. Isso já vem inativo dentro do Python, você pode usar na versão 3, então é esse banco de dados aqui.

**[00:36:46]** e a gente vai se comunicar com ele em memória, ou seja, ele não vai persistir dados no disco em lugar nenhum, a gente só vai usar e conversar com ele aqui dentro. E aí, a partir disso aqui, a gente vai pegar aquela tabela de registros que a gente tinha, né? Então, vou importar lá. Então, vamos lá. From. Fastapi0.models import registry, ou table registry, que foi onde a gente registrou as tabelas. E aí, aqui...

**[00:37:16]** O table registry tem essa coisa que chama metadata. E o que a gente quer dizer com metadados? Metadados são dados sobre dados.

**[00:37:25]** E o que que, na verdade, são esses metadados que a gente quer ver? São esses dados do modelo. Ah, essa classe user, né? A gente vai fazer uma introspecção de código aqui. Essa classe user tem ID, tem username, tem e-mail, tal. Tem o nome de tabela, tem esse tipo de coisa. Então a gente vai falar o seguinte pra ele, olha. Pega esses metadados de todas as tabelas que estão registradas aqui e cria pra mim, create, ó.

**[00:37:53]** Aí, para ele funcionar, a gente tem que falar, olha, como é que eu sei que isso está funcionando? A gente passa a engine para ele. Ou seja, dentro dessa conexão virtual que a gente tem em memória, a gente vai pegar todos os metadados que a gente registrou lá no registro de tabelas e ele vai criar tudo para essa conexão aqui. Ou seja, ele vai efetivamente criar a tabela no banco de dados, em memória. Ou seja, isso aqui deixa desistir quando a aplicação deixar de...

**[00:38:24]** de estar rodando. Fez sentido isso aqui? Parece que são muitos componentes, muita coisa, mas não é tão complicado assim. Tudo bem, é um pouco, eu assumo. Mas com a gente falando e tal, meio que as coisas são descritivas assim. E aí a partir disso aqui, vou fazendo aqui e vocês vão me respondendo, aí está tudo bem, está todo mundo entendendo, se tem alguma questão sobre o que a gente está conversando aqui.

**[00:38:50]** Lá no SQL Alchemy, então, from SQL Alchemy, lá na coisa, na parte do Toolkit que tem o RM, que é aquela relação entre as coisas, eu vou importar a Session. E aí eu vou falar o seguinte. With Session da conexão que a gente quer, Session, por exemplo, poderia colocar em minúsculo aqui, ou SS, o nome que você quiser aqui, a gente vai...

**[00:39:24]** fazer um yield session. O que que aconteceu aqui? A gente criou uma conexão com o banco de dados. Dentro dessa conexão, a gente criou as tabelas que a gente precisa e agora a gente vai abrir uma sessão de troca entre o banco de dados e o código nessa coisa que a gente chamou de session. Então, o objetivo da sessão é fazer essa troca. Então, a partir daqui, na sessão eu vou falar, insere um registro, remove um registro, faz uma busca.

**[00:39:57]** Então, a sessão é essa comunicação efetiva entre o banco. Aqui a gente ligou a conexão com o banco, e aqui a gente está pedindo, olha, me dá uma coisa para a gente fazer essa interação. Eu e o banco, o banco e eu. Massa, faz sentido isso aqui? Que está acontecendo aqui? Não é tão bizarro quanto parece. E a gente vai colocar esse table register aqui no fim.

**[00:40:26]** para depois, quando a gente desfazer, depois que acabar a execução do código que a gente queria, a gente vai dar, em vez de um create all, a gente vai dar um drop all. Lembra que na aula passada a gente estava conversando sobre esse esquema, tipo assim, ah, mas aí eu preciso que o banco de dados sempre esteja limpo, que um teste não dependa do outro, então olha que interessante, antes da gente dar a conexão para usar,

**[00:40:54]** A gente cria todas as tabelas, e depois que a gente usar, a gente deleta todas as tabelas. Com isso, a gente deixa o banco de dados sempre limpo, a partir da execução de cada teste. Muito legal, não? E aí, o que eu vou fazer com isso aqui? Eu vou transformar isso aqui em uma fixture do PiTest. Então, a rouba. PiTest.fixture. O Germano fez uma pergunta aqui. Deixa eu ver aqui. Ele falou o seguinte. Sessão seria começar a trocar os dados com o banco de maneira segura.

**[00:41:30]** por causa do Will de que caso de um erro volta às operações do Banco de Dados não não na verdade não o Will de aqui ele só está dizendo o seguinte olha essa sessão vai começar e vai terminar depois que essa fixture rolar então o Will de aqui ele vai ceder a vez né ele vai falar olha tá aqui o que você me pediu e aí ele fica pausado aqui né pausado aqui

**[00:41:58]** E aí, ele dá a sessão para a gente usar no teste, que a gente vai pegar essa session aqui, vai trazer para cá, por exemplo. Opa, session. Ele vai dar essa sessão para a gente poder usar aqui. E a partir desse relacionamento com a sessão aqui, depois que essa função for executada, ele deleta o banco de dados. Não tem a ver com a relação de dar erro ou não.

**[00:42:21]** Ele só abriu a sessão, essa canal de comunicação para a gente comunicar com o banco, e depois que essa função acabar, porque é o conta da fixture, é o teardown. Lembra? Aqui a gente está fazendo o arrange do teste, aí é que a gente faz o act do teste, o assert do teste, e depois ele faz o teardown. Ele desfaz as operações que tinha feito durante o teste, para isso não ficar sujo. Só que essa é a ideia.

**[00:42:51]** Massa? Fez sentido aqui? Esse ponto em que a gente tá trocando ideia aqui? Aí o Igor tinha falado que como lidar com tipos exclusivos de um determinado banco, a gente vai mudar depois, a hora que a gente for evoluindo, a gente vai usar um banco de dados como Postgres, por exemplo. Mas, por enquanto, a gente tá aqui de boinha. Sem pressa. Vamos aproveitar aqui o momento. Então, eu vou só organizar esses imports lá em cima.

**[00:43:23]** Só para não ficar sujo aqui. Então a gente vai trazer o módulos para cá. A gente tem SQLModel, SQLModelORM. Eu vou rodar o teste só para ver o que acontece. Se não deu nada de errado na nossa comunicação aqui. Aí ele falou olha, está errado a ordem dos importos. Eu vou dar um format aqui. Vamos ver o que ele vai mudar aqui em cima. Arrumou certinho. Tudo o que a gente precisava aqui. Então eu vou dar um teste.

**[00:44:02]** Legal, rodou o teste, passou, mas assim, nada aconteceu, né? Porque a gente não tá usando a sessão no banco, a gente não tá persistindo esse dado aqui, saca? Qual a diferença entre registro e declarativa e base? Michael, assiste a live que eu dei de material suplementar, se você quiser entender a diferença dessas coisas, porque a gente não vai usar declarativa e base, é bem fora dos copos essa pergunta.

**[00:44:28]** que o Germano está falando, é o tal do Comet. Não, mas a gente não chegou no Comet ainda, calma aí. Então vocês estão muito na frente, vamos devagarzinho aqui. Então é legal, agora que a gente tem a session, a gente pode falar o seguinte para o banco de dados agora aqui dentro desse teste. Eu poderia falar o seguinte, olha, session.ed adiciona esse user na sessão, ou seja, nessa comunicação

**[00:44:58]** que a gente está fazendo aqui dentro. Ou seja, a sessão agora tem o user. Massa, olha que interessante. A gente está pegando agora e a gente adiciona esse user na sessão. E aí toda vez que a gente quiser confirmar que uma operação acontece, ou seja, transita aqui o dado a...

**[00:45:25]** Para o banco de dados, a gente faz um commit, né? Tipo, uma afirmação, bora lá! Então a gente pode fazer o seguinte, session.comit. Ou seja, todas as operações que foram feitas na sessão vão ser transmitidas para o banco de dados de verdade. Massa, vamos rodar o teste, provavelmente vai acontecer tudo do mesmo jeito. Ah, tá, beleza, ele tá reclamando aqui do malim branco que ficou aqui em cima e aqui embaixo.

**[00:45:58]** Vamos rodar agora. Beleza. Continua tudo funcionando da mesma forma. Massa. Vamos colocar aquele breakpoint aqui e ver o que acontece nessa interação aqui. Vamos ver o user de novo. User. Olha que massa. O que aconteceu aqui. Agora o user.

**[00:46:21]** Tem todos os dados que a gente precisava. Agora ele carregou o ID do user. Olha que massa, então é o primeiro user que a gente inseriu dentro do banco de dados. A gente tem o created at, que foi a hora que isso foi criado. Então 20 dia 20, do 5, 2025. Pô, massa. Então a gente tem esse ID, porque agora ele transpassou a sessão. Saca, então ele de fato está.

**[00:46:54]** no banco de dados. Então a gente consegue fazer essa interação de um lado para o outro. Então a sessão, toda vez que ela encontra com esse commit aqui, ela definitivamente pega todas as operações que foram feitas no nosso código e persiste essas operações no banco de dados. Isso aqui é conhecido no mundo dos padrões de projeto como...

**[00:47:18]** Unit of the work. A gente faz várias operações na sessão e fecha a sessão e confirma a operação e faz uma operação só. Então a gente pode fazer várias coisas, tipo assim, adiciona 1, adiciona 2, adiciona 3, adiciona 4 e a gente vai tratando isso aqui e depois a gente faz uma única operação com o banco de dados. Fica mais leve esse tipo de comunicação. Então o objetivo da sessão é ser esse lugar

**[00:47:47]** transitivo, né? Entre o que está acontecendo no meu código e o que vai acontecer no banco de dados quando eu pedir para ele performar essa operação de fato. Massa, fez sentido essa brincadeira aqui que a gente fez? Então, é assim que se adiciona um dado no banco de dados usando a sql-alchemy. Então, basicamente o que a gente tinha era isso. A gente criou a conexão, criamos as tabelas,

**[00:48:18]** ligamos essa área transitiva de comunicação entre código e banco de dados, e depois quando o teste acabar, isso vai ser deletado. Que é uma coisa interessante, porque quando a gente rodar de novo esse teste, você vai ver que o ID vai ser determinístico. User ainda tem o ID 1, ou seja, toda vez que esse teste rodar, o user vai ter o ID 1, porque o banco está sendo deletado todas as vezes. Fez sentido essa coisa aqui que a gente está fazendo? Essa brincadeira aqui?

**[00:48:55]** Pergunta sincera aqui pra vocês. Aí eu me adiantei, né? Eu fui explicando as coisas que eu tinha colocado nos slides. Agora, uma outra coisa que é interessante aqui, né? É a forma de fazer buscas, né? Dentro do SQL que me... Então, por exemplo, eu queria fazer uma busca, né? Em vez de acertar esse user que a gente já tem, eu vou pedir um user do banco de dados.

**[00:49:27]** Então eu vou pensar aqui um, sei lá, um response user. Como é que eu coloquei ele? Eu coloquei user, né? Só user, eu fiz assim, ó. Esse é um novo usuário que a gente vai cadastrar no banco, o new user. E a gente vai pegar um user novo aqui, não? Então adicionamos esse novo usuário e a gente vai buscar ele dentro do banco de dados para saber se as coisas estão lá dentro mesmo. E como é que a gente faz isso?

**[00:49:51]** A gente vai fazer o seguinte, Session, ponto. E aí, como é que a gente busca os dados? Eu quero performar uma coisa no SQL Alchemy e eu vou falar o seguinte, Scholars, aqui. Eu posso dar só Scalar. E o que que acontece aqui? Toda vez que eu uso esse método da Session, chamado Scalar, quer dizer que eu estou pedindo para o banco de dados o resultado da operação que vai acontecer aqui nesse...

**[00:50:21]** Nessa coisa, ele vai me retornar em escalar. Escalar é um conceito de álgebra. E quer dizer que ele vai transformar tudo que vier do banco em um objeto Python. Mas, então, ele vai fazer aquilo. Tudo que veio do banco converte esse modelo no objeto Python. É a volta do ARM, né? A gente foi, agora a gente tá voltando pra cá.

**[00:50:48]** Assim, o mais difícil é pensar como um testa para não cair na ingenuidade de fazer algo que você não vai achar que está tudo bem. Então, é isso que a gente está exercitando, essa cultura de testes aqui. Então, para a gente fazer isso aqui, eu preciso importar lá do SQL Alchemy o Select. Então, vamos lá. From SQL Alchemy Import Select. Aí eu vou fazer o seguinte, eu vou fazer uma busca, então selecione para mim.

**[00:51:13]** Olha como isso vai começar a ficar interessante. Selecione para mim lá na tabela de users. Olha que massa. Selecione para mim a tabela de usuários. Então select alguma coisa from... Então select asterisco from user. Mais ou menos essa abstração que a gente está fazendo aqui. Tiago, muito obrigado pelo teu super chat. Ó, estamos juntos. Valeu.

**[00:51:49]** Tem como colocar autocomite? Tem, eu não recomendo. Explicito é melhor do que implícito, uma regra básica do Python. Então, seleciona todos os users aqui para mim e aí eu quero fazer uma condição. Onde? Então, where? Onde esse usuário tem o username? Então, a gente quer saber sobre user.username for igual a teste. Vou colocar o breakpoint aqui.

**[00:52:25]** Para a gente ver o que que acontece aqui. Então vou dar um playtest. Ah, ah. Poetryram. Playtest. Aí olha o que aconteceu, a gente parou aqui e vamos ver o que que é esse user. É literalmente o user que a gente tinha, a gente inseriu ele no banco de dados. Olha que massa. Então eu pedi o resultado escalar dele, ou seja, o que vier dessa consulta no banco

**[00:52:56]** Converta em um valor escalar, ou seja, que é a tabela do banco de dados que a gente tinha aqui no modelo. Então ele trouxe o resultado como se fosse uma instância dessa classe aqui. Então essa é a ideia do select aqui dentro. Massa?

**[00:53:20]** Então é basicamente isso que está acontecendo. E aí a gente pode simplesmente fazer o asserte aqui, né? E falar, olha, o user name que veio é teste, obviamente sim, né? Mas pode ser que você tenha esquecido o commit aqui, por exemplo. Aí agora ele não vai dar, ó, na busca. Ó, pior que deu. Porque a gente está na mesma session. Mas pode ser que eu tenha esquecido o ad, por exemplo. Aí ele fala, ó, não tem teste no user, porque o user que veio aqui é none.

**[00:53:52]** Deixe-me dar um breakpoint aqui para vocês verem. Como ele não retornou nada, é none. Vamos ver? User. None. Interessante, como essa coisa vai se comunicando, as coisas vão criando relações aqui. Então, a gente acabou de fazer essa validação aqui para ver se o username era L, teste, qualquer coisa do gênero aqui. Agora, vocês conseguem ver que isso aqui é um código...

**[00:54:26]** que fez uma viagem agora, né? Então a gente criou a sessão, que seja, como conectamos no banco, criamos as tabelas, abrimos um canal de comunicação efetivo, a gente criou uma instância daquele nosso objeto, adicionamos ele nessa transição, fizemos ele fazer o que tinha nesse transitivo ser inserido no banco,

**[00:54:53]** Depois a gente pegou e foi lá buscar dentro do banco de dados. Ó, existe alguém na tabela de user onde o username é teste? A gente trouxe esse resultado e validou para ver se essas coisas batiam, se esses dados estavam corretos. Então essa é a coisa que acontece aqui dentro desse esquema aqui dentro. Sempre faço consultos usando execute, depois escala. Bom, é questão de gosto, né? Legal?

**[00:55:22]** Então, essa é a ideia do scholar aqui, de fazer essa busca. Agora a gente trouxe exatamente o que tinha lá. Fez sentido? Não, antes da gente partir aqui, fez sentido? Essa relação, essa comunicação que a gente teve aqui com o Banco de Dados, eu preciso de feedbacks, né?

**[00:55:41]** Então assim, beleza. Deu para entender. Eu sei que algumas coisas ficam meio subjetivas ainda. Tipo, a InJine pega no circuito a session e tal. Mas tipo assim, no modo geral deu para entender o que está acontecendo nessa comunicação, nessas chamadas, nesse código que a gente escreveu. Fez. Legal. Lindo demais, ok. Massa. Agora, eu quero falar para vocês o seguinte. Esse nosso teste, ele é muito massa.

**[00:56:20]** Ele validou aqui que username é teste ou Alice, igual eu tinha colocado aqui no slide, mas eu não validei isso de fato, né? Você concorda comigo? É tipo assim, é uma validação meio pífia, igual que a gente fez. Ela é muito melhor do que a gente tinha antes, mas ela ainda não valida, né? A gente validou que o username se chama teste, né? Ou se chama Alice, depende de se você usou o slide ou fez junto comigo aqui.

**[00:56:53]** Mas a gente não validou tudo. Saca, eu quero saber se o objeto que eu inseri aqui é exatamente o objeto que precisaria ter sido inserido aqui. Saca, a gente validou um pedaço, a gente quer validar tudo, a gente quer testar de verdade, né? Eu vou... Antes da gente entrar no próximo tópico, eu quero explicar para vocês mais ou menos o que a gente precisaria validar aqui, né? Lembra que nos outros testes, nos testes da API aqui?

**[00:57:22]** A gente começou a validar tudo, a gente sabia qual era o ID, qual era o username, qual que era o e-mail e tudo mais, então a gente precisa trazer essa validação pra cá, né? Então, eu vou fazer o seguinte, eu quero saber se username aqui é igual, então a gente vai validar tudo, se é igual a teste, se o e-mail é igual a teste, arroba teste e-mail,

**[00:57:53]** É teste, arroba teste, só que eu coloquei ele, né? Teste, arroba teste. Eu quero saber se o password que foi inserido aqui é igual a secret, né? Eu não sei porque que eu estou colocando igual, igual aqui. Estou viajando forte aqui, é só dois pontos. Se isso aqui é isso aqui e se isso aqui é secret. Mas aonde mora o problema aqui? Você sabe que, tipo assim, pelo fato do banco de dados estar sempre limpo, a gente sabe que o ID é 1, né?

**[00:58:26]** Maça, só que a gente não consegue dizer se o dado que a gente está inserindo aqui foi inserido na hora que ele deveria ter sido inserido. Saca, é esse momento aqui que é difícil. Aí, como a gente vai fazer essa validação full match, como isso aqui, a hora que a gente criou o modelo, a gente falou que isso era uma data class do Python, mapeia como uma data class.

**[00:58:57]** As data classes do Python, então vamos lá. FromDataClassesImportAsDict. Ela tem uma coisa que converte a data class em um dicionário. Então, vamos validar aqui pra gente ver o que acontece. Então, vou rodar o teste de novo agora com todos os campos, lembrando que a gente tem o CreateAll aqui, o createdAt. Vamos rodar. TaskTest. Deu um erro de linha em branco, deixa eu dar um format, vai.

**[00:59:31]** Não quero perder muito tempo aqui. Legal, ele deu um erro. Porque a gente está usando username aqui, não é? Deberia ser só user, porque a gente quer validar o user inteiro. Então, vamos rodar de novo. Aí ele falou o seguinte, olha, deu tudo certo na comparação. Só que no lado esquerdo da comparação, no sdict user, veio um campo chamado created at. E como a gente vai falar, que hora que esse objeto foi criado?

**[01:00:05]** Então faltou esse campo created at. E como é que eu vou preencher esse campo? Como é que eu sei que hora que isso aqui foi criado? Ah, eu posso colocar o date time now aqui. Será? Eu não sei qual o valor é esse aqui.

**[01:00:23]** E agora a gente começa com alguns problemas aqui, né? Então, Screated Edge, eu preciso saber que hora, que minuto, que segundo, isso aqui foi criado dentro do banco de dados, porque lembra que a gente tá usando aqui o server default, ou seja, ele registra a hora do banco de dados e não a hora em que eu inseri o registro de fato, foi a hora em que o comit foi feito no banco. Ah, legal, né? E aí como é que a gente vai garantir isso aqui, né?

**[01:00:55]** O SQL Alchemy, o R&M em específico do SQL Alchemy, tem uma forma de lidar com isso, que é o seguinte, a gente pode roubar nos testes, porque ele permite um hook. Ou seja, antes de fazer alguma operação, faça outra coisa. Antes de resolver um problema, faça uma outra coisa. Saca, então ele tem um jeito de falar, olha, antes de inserir, faz uma coisinha aqui pra mim?

**[01:01:28]** Antes de mudar, faz uma coisinha aqui pra mim. Então são os eventos do ERM. A gente chama isso de hooks dentro da documentação do SQL Alchemy. Então a ideia aqui, a minha ideia é que durante o teste a gente robe na hora. Simplificar as coisas, né? Tipo assim. Porque alguém tá falando, ah, é só, teria que fixar a hora. Como é que eu vou fixar? A current date. Saca. Então...

**[01:01:55]** Como é que a gente faz isso com estilo, de uma forma bonita, com uma boa prática? O que eu faço aqui? Então, a grande sacada aqui do SQL Alchemy é poder fazer isso aqui, olha, vou importar os eventos do SQL Alchemy e vou falar pra ele, ou seja, fica ouvindo aí. Aí toda vez que o user, antes de ser inserido alguma coisa no user, chama uma função pra mim, esse hook. Olha que massa!

**[01:02:29]** Então, eu posso fazer essa interação aqui. Eu posso interceptar a mensagem da sessão e mudar alguns dados. Sensacional, né? Vamos brincar com isso aqui. Beleza, agora eu tenho um códigozão muito maluco aqui, mas a gente vai fazer isso junto, né? Vamos lá, juntinho. Lá no Conf Test aqui, eu vou criar uma nova função aqui.

**[01:02:57]** que eu vou chamar de MockDB Time, ou seja, DEF. Eu vou colocar Underline, vocês vão entender daqui a pouco, porque? Beleza, MockDB Time. Ou seja, eu quero mentir a hora que o banco de dados vai persistir alguma coisa. E aí, para persistir isso aqui, para mentir, eu preciso falar para ele que ele vai criar um evento, não é? Então, vamos lá. Então, From SQL Alchemy Import Events.

**[01:03:25]** Aí aqui dentro, eu vou dar um event, vou falar pra ele, olha, dá uma escutada aí no user, né? Naquela tabela de usuários, então, a From Fast API 0.models import user. Então, lá no user, eu quero que você dê uma mentida pra mim, em algum momento, ou seja, antes de inserir. Então, before, antes, né, before, insert.

**[01:03:51]** Então, antes de inserir o dado, eu quero que você execute para mim alguma coisa, uma função aqui. Qual que foi o nome que eu dei para ela? O que? FakeTimeHook. Eu vou copiar tudo aqui. Vai me poupar e descrever um pouco. Então, eu vou criar essa função FakeTimeHook. Então, aqui é fakeTimeHook. Então, sempre executa essa função antes de inserir o dado.

**[01:04:21]** Olha que massa! E aí o que que acontece? É que a gente precisa do mapeamento, a conexão e o target. Ou seja, o target é qual o objeto, né? O alvo desse hook, quem fez a conexão, e o maper é o mapeamento do ORM, que a gente conversou até alguns momentos atrás. E aí o que que eu vou fazer aqui, né? Então ó, tá vendo que ele pegou esse target, que é o alvo que a gente quer?

**[01:04:48]** Vou fazer o seguinte, eu vou dar um print nesse target, e depois a gente vê o que acontece aqui dentro. Legal? Então, mock, é uma forma de mentir, então a gente vai mentir a hora do banco de dados aqui dentro, dentro dessa função. Por enquanto, é isso aqui que a gente tem. Lembra que depois a gente tem que desfazer as coisas, porque cada teste tem seu próprio consumo, tem seu próprio momento. Então, a gente vai desfazer isso aqui depois.

**[01:05:18]** Então, em vez de Event Liston, a gente vai usar o Event Event Remove, né? Remove essa escuta aí, né? Ele tá vendo se tem boi na linha, remove aí, remove. Remove isso aqui. E aí, o que a gente vai fazer aqui? A gente vai retornar um tempo aqui, do mesmo jeito que a gente tinha feito ali. Eodime. Massa é a única coisa que importa pra gente aqui dentro. Caio, muito obrigado, mano, pelo...

**[01:05:53]** pelo Super Chat, mano. Valeu demais. Então, basicamente, é isso aqui que a gente quer fazer. E aí, o que a gente vai fazer? A gente vai receber o modelo que a gente quer usar aqui, ou seja, model, que, por padrão, pode ser user, por exemplo. A gente só tem user até o momento, mas a gente vai receber isso diretamente aqui. E qual é o tempo que a gente quer que ele minta aqui? Time.

**[01:06:23]** E aí para o time a gente vai importar, sei lá, um date time e gerar uma data aleatória aqui. Então, from date time import date time. Mas você pode falar, eu queria uma data qualquer aqui, sei lá. 2025, vou falar que toda inserção vai ser hoje. Dia 20, 6, 5, 5, 20. Legal, vai ser sempre nesse horário aqui.

**[01:06:53]** E a gente sempre vai ter que passar esse model aqui, em vez de fazer, porque a gente poderia fazer para created ads distintos, né? Então vai ser model e não vai ser mais para o user. A gente vai passar essa coisa lá do outro lado. Ou seja, então toda vez que algum evento, toda vez que o banco for fazer alguma operação, a gente vai colocar isso aqui dentro. A gente vai dar uma brincada com isso aqui.

**[01:07:23]** Uma das características interessantes do Python é que a gente pode, pelo fato de a gente ter esse yield aqui, a gente pode criar isso aqui só num momento, ou seja, lembra do with, aquele bloco de gerenciamento de contexto? Então eu vou vir aqui e falar o seguinte, olha, from contextlib import contextmanager. E aí eu vou falar o seguinte, olha, isso aqui é um gerenciador de contexto. Agora eu poderia fazer o seguinte aqui.

**[01:07:54]** para usar isso aqui, eu poderia fazer with. Então, user, e aí tudo que acontecer aqui dentro vai estar com um tempo de mentira. Então a gente pode usar isso lá dentro do teste. Faz sentido? É uma forma de mentir aqui, a gente ainda não implementou a função de mentira, mas é esse o esquema do evento aqui dentro. Ou seja, a gente vai ouvir e vai alterar todas as vezes que a gente receber.

**[01:08:28]** alguma coisa em um determinado modelo. E a gente pode aplicar esse WIF lá dentro do teste. Só que como eu não quero ter que ficar importando e fazendo esse tipo de coisa, a gente pode transformar isso numa fixture. Ou seja, uma fixture bem simples que só retorna isso aqui. Então, pi test, ponta fixture, def mock db time. E ela só retorna isso aqui. Return esse mock db time que a gente criou aqui em cima. Massa.

**[01:09:01]** Então é basicamente essa coisa que a gente quer operar aqui dentro. Fez sentido aqui, isso aqui? De onde saiu esse time? Foi eu que coloquei aqui. É um time qualquer. Dei a data de hoje. Só porque eu quis. Aí eu vou dar uma formatada aqui, né? Então format. Só pra ele arrumar os imports. Aí a gente vai ter que jogar esses imports lá pra cima. E aí eu deixo ele se virar aqui, vai ganhar tempo.

**[01:09:44]** E aí, toda vez em que acontecer isso aqui, ou seja, a gente vai pegar essa fixture que a gente criou aqui e vai trazer ela pra cá, que é no teste DB. Então, em vez de importar só a Session, que foi aquela outra sessão que a gente criou, a gente vai chamar o MockDB Time. E aí, tudo o que a gente vai executar no banco vai ser com um horário de mentira. Aí eu posso fazer o seguinte, with MockDB Time, tudo isso aqui vai acontecer dentro de MockDB Time.

**[01:10:21]** Olha que massa. E aí eu falo pra ele, olha, o model que eu quero mudar, que eu quero colocar aquele root aqui, model, é user. Aí, como ele tem esse yield aqui que dá o tempo pra gente, ele retorna esse tempo pra mim, eu posso falar o seguinte, olha. S-time. Aí pega esse tempo aqui, e essa é a hora exata que foi inserida, porque a gente tá mentindo a data. Olha que lindo isso aqui.

**[01:11:06]** É bonito, né? Fala, é bonito, é bonito, é bonito. Agora, para a gente ver que isso aqui está acontecendo de fato, eu vou dar um breakpoint aqui dentro. Breakpoint. E a gente vai navegar até aqui e ver o que acontece. Vou dar o task test. A gente vai chegar aqui e olha onde a gente está. A gente está dentro da função fake time route. E olha o que a gente tem aqui. O mapper que é user. Ah, sensacional. A gente tem a connection.

**[01:11:47]** que é a conexão que a gente fez lá na engine. E a gente tem o target, que é o objeto que a gente manipulou. Só que lembra que aquele não tem ID e nem tem o created yet ainda. E por que que ele não tem um ID nem o created yet? Porque a gente tá no before insert, ou seja, ele ainda não foi enviado pra lá.

**[01:12:11]** E aí agora, agora que chega a grande coisa aqui, eu quero fazer o seguinte, eu quero ver se esse objeto tem o atributo created at. Então vamos lá. If has a TTR, ou seja, o objeto que veio no target tem o atributo created at. Se tiver o created at, faz o seguinte, target.created at, created at, recebe time.

**[01:12:44]** Ou seja, antes de inserir, eu dou o tempo. Ou seja, porque ele só executa essa operação quando não vem. E como eu estou dando, ele vai persistir com o tempo que eu passei para ele. Vamos rodar e ver se o teste funciona agora? Maravilhoso, maravilhoso. Isso é lindo, isso é lindo.

**[01:13:15]** Olha que massa, então, a gente conseguiu fazer esse esquema aqui, né? Tipo assim, olha, quando comitar a operação, vai fazer uma transição aqui, aí essa transição vai chamar o beforeInsert, quando esse beforeInsert acontecer, a gente executa a operação que a gente queria, e aí depois ele passa para o insert, e aí a gente chama e vai para lá. Olha que massa, é bonito, não é?

**[01:13:46]** E aí com isso, a gente pode manipular o tempo da forma como a gente quiser. Então, por exemplo, se eu quisesse falar que aí, dependendo da dinâmica de teste que você quiser passar, eu queria falar, olha, o meu time é outro time. Então, por exemplo, sei lá, é now. Por exemplo, sei lá, então, date time, date time, ponto now. É outro agorário. Legal. Ele se resolve com isso aqui. Ah, é outra classe. Sei lá.

**[01:14:20]** Outra tabela, Table. Se essa Table existisse, ele faria esse tipo de coisa. Então, é uma solução para a gente poder brincar com isso aqui, né? Então, a gente passa exatamente o que a gente precisa, quando a gente precisa, e o valor que a gente quer validar. Sem ter que fazer nenhuma coisa de monkey pet, nem nada. O SQL Academy tem uma coisa que permite que a gente faça esse tipo de rolêzinho. Uma coisa que eu gosto de colocar aqui...

**[01:14:46]** que eu coloquei lá no no texto foi isso aqui né um asterisco aqui pra exigir que você tenha que passar model aqui só pra fazer sentido a fixture a hora que você tiver ele não vai deixar o instância assim eu preciso passar o model igual massa isso tudo só no teste sim só no teste catapim mas eu já fiz tanta gambiarra pra resolver isso então mano tem tem coisas interessantes que a gente pode fazer e tem recursos que a gente pode usar pra isso

**[01:15:21]** Pô, muito legal, não é isso aqui? Muito massa. Funciona super bem e a partir disso aqui a gente explode a cabeça, né? Como o William mandou ali. Boom! É exatamente isso. Fez sentido que a gente fez aqui? A gente altera no teste pra gente poder validar todos os dados que a gente precisa. Aí eu fiz um monte de coisa pra chegar nesse resultado aqui, né? Eu tô me adiantando, né? Os slides estão todos aqui pra me ajudar, mas eu tô fritando a mente aqui, né?

**[01:16:05]** Toda vez o Dunno me surpreende, que é isso? Magia pura. Pô, é muito legal isso, que é muito massa. Eu gosto muito. E aí, isso faz com que a gente possa fazer a validação completa do objeto. Ou seja, a gente pode garantir qualquer tipo de parâmetro, sem ter que ficar fazendo... Porque a galera costuma fazer umas gambiarras meio malucas aqui pra fazer... Nossa, isso aqui... Eu jogo um objeto na memória que faço no seu quê? Faço no seu quê lá, pô? Tem um jeito fácil de fazer isso.

**[01:16:33]** E aí o legal é que pra todas as vezes que a gente precisar testar um created at, a gente tem isso aqui. Ah, mas e se fosse outro campo? É só aumentar esse if aqui. E aí você vai brincando. Um dos exercícios é implementar o updated at. E aí vocês vão ter que mexer aqui no meio desse vespero aqui. Vou abrir um monster pra te acompanhar, bora. Legal?

**[01:17:01]** A gente fez tudo o que precisava, a gente configurou esse ambiente pra poder testar tudo bonitinho, encaixadinho, com fixture, sabe? Isso aqui vai servir pra qualquer coisa de banco de dados que a gente for usar. Por isso que eu separei uma aula pra gente falar especificamente sobre banco de dados. Mas você tá vendo que a gente não tá usando banco de dados na aplicação, né? E...

**[01:17:27]** Spoiler, a gente não vai usar. Hoje não, na próxima aula a gente vai integrar essas duas coisas. Hoje é mais pra gente fazer essa reba em boca da parafuseta pra tá tudo pronto pra gente poder usar em produção, né? Mas a gente garante que tá tudo funcionando aqui. Uma coisa que é interessante aqui é que embora a gente ainda, a gente tá usando esse banco de dados fake aqui, a gente não colocou o banco pra gente poder usar na aplicação, né?

**[01:17:57]** E isso aqui é uma prática ruim, colocar coisas hardcoded. Aqui no teste está tudo bem, no teste tem que ser explícito. Mas na hora de fazer a minha aplicação eu não queria colocar esse endereço do banco em memória, né? Então aí a gente vai ter que instalar uma extensão do PiDentic, que é o PiDentic Settings. PiDentic Settings. PiDentic... Agora foi.

**[01:18:29]** E aí, qual que é a brincadeira aqui, né? Tipo assim, boa prática da gente começar a brincar é não colocar essas coisas, né? Tipo assim, o banco de dados importa dentro da aplicação. Imagina que eu coloco o endereço do banco de dados dentro da aplicação. E aí, tipo assim, se eu precisar botar um banco de dados de produção, um banco de dados de QA, um banco de dados de stage, sabe? Eu quero que as configurações da aplicação sejam independentes, né?

**[01:18:59]** do código, né? Então, essa é a brincadeira que o Paidantic Settings vai fazer pra gente aqui. Existe uma coisa que se chama Twelve Factor App, né? Pra quem quiser brincar. Tem as referências lá no material de texto, mas isso aqui são boas práticas pra gente colocar uma aplicação em produção e tudo mais, que é tirar códigos hardcoded, esse tipo de coisa aqui ó, codebase.

**[01:19:31]** dependes, config, a gente vai trabalhar nessa terceira dependência aqui para a gente poder conversar. Mas basicamente o que eu quero aqui é que a gente não ensira, né? Nem vai ter no banco, nem vai ter o endereço aqui dentro, quando a gente começar a fazer essa integração, que é no caso agora. Vamos lá?

**[01:19:51]** Eu vou criar um novo arquivo aqui. Interessante, aqui lá dentro da nossa passa do projeto, eu vou criar uma coisa chamada settings.py. Então, vamos lá. Fecha IPI0 aqui. Eu vou criar um settings.settings.py. E agora, a gente vai começar a brincar com esse pa-identic settings aqui. Vamos lá. Então, from pa-identic pa-identic settings import. A gente vai chamar esse base settings aqui dentro.

**[01:20:22]** Base Settings. E a gente vai criar uma clássica, eu vou chamar de Settings mesmo. Settings. Que vai herdar de Base Settings. E aqui dentro, eu quero trazer o endereço do nosso banco de dados. Então, Database, Database, URL. E é isso aqui, é uma string. Massa.

**[01:20:44]** E aí, de onde que eu quero trazer esses dados? Então, essa é a brincadeira. Então, a gente vai desacoplar, né? A coisa, a gente nem vai chegar a ter aqui a configuração do banco aqui. A gente quer tirar a configuração do banco e colocar ela num arquivo que a gente vai chamar de ponto envy, ou dot envy, cada um chama de um jeito. E esse dot envy são as configurações do ambiente, do environment, né? Então, vamos lá. Aqui a gente tem esse settings, config dict.

**[01:21:14]** E aí aqui eu vou fazer o load do nosso modelo. Então o modelo config recebe settings e eu vou falar o seguinte, olha, traz para mim o nosso arquivo que é o ponto env. Você pode fazer isso passando o nome do env file, o que eu recomendo, no env file. E para a gente se prevenir de alguns possíveis erros, coisa de sistema operacional e tudo mais, eu vou falar sobre o encode.

**[01:21:42]** desse arquivo, que é o Envifile encode. E aí vou falar que o arquivo é o TF8. Só porque caso você copie o meu código ou sobe no Git, desce no de outra pessoa, a gente tem que saber como foi encodado esse arquivo. Massa? E é a partir disso aqui, a gente vai trazer as configurações do nosso projeto, então beleza, database urn, a configuração do projeto vai vir do arquivo...

**[01:22:12]** .env, eu uso o meu editor de texto é o Guinui Max, Natalia. Massa? Legal. É basicamente isso, é bem simples, database URL e tal. E aí, dentro desse arquivo Env, a gente vai criar um database URL.

**[01:22:30]** Simplão, assim, simprão, simprão. Então, vamos lá, aqui na raiz do nosso projeto, na raiz do projeto, aonde tá o pyproject.toml, é interessante, aqui, .toml, cada um fala o jeito que gosta. Eu vou criar um novo arquivo chamado .env. Para essa atenção, vamos isso aqui. Para quem nunca criou isso aqui, é .env, com ponto mesmo no final. É o ponto no começo, então é .env. Massa.

**[01:22:58]** ponto envy, yes. Então vou criar esse arquivo e aí dentro desse arquivo eu vou criar aquela variável que a gente criou aqui dentro dos settings, que era o database URL. E aí é que eu vou passar o endereço. Não precisa de aspas, mas para evitar algumas coisas em alguns sistemas eu vou...

**[01:23:24]** colocar entre aspas, ok? Então, onde vai ficar o meu banco de dados? Lembrando que a gente está usando o SQLite, que é o banco de dados que é simples. Ele não tem um servidor, ele roda dentro...

**[01:23:35]** da nossa máquina em um arquivo. Então eu preciso falar para ele, aonde vai ficar o banco de dados? Então eu vou falar o seguinte, SQ Lite 1, 2, 3, é importante, tenha 3. 2 pontos, barra, barra, barra, 3 barras. E eu vou chamar isso de database.tb. É o arquivo aonde a gente vai persistir os nossos dados. Os dados da aplicação e não os dados do ambiente de teste. Massa.

**[01:24:04]** Como a gente está chamando isso aqui de database.db lembra que a gente criou na primeira aula um arquivo oculto também com ponto que chamava git ignore aqui dentro eu vou adicionar o nosso database.db porque eu não quero que suba né eu chamo isso aqui sempre de project stuff coisas do projeto eu não quero que suba isso aqui pro git né você não vai dar seus

**[01:24:33]** suas coisas, em outro lugar e tudo mais. Então, tipo assim, a gente armazena aqui e fala, não vai subir para o repositório o nosso database.db. O .env também não se sobe, mas o .env já está aqui no environment, está vendo? O .env já está aqui dentro do gitignore que a gente criou na primeira aula. Então, eu só vou adicionar o database aqui dentro. Legal? Temos isso aqui configurado, tudo rodando, tudo bonitinho.

**[01:25:01]** Agora a gente vai conversar sobre migrações. Então migrações, qual é a ideia da migração? É ter um banco de dados evolutivo que acompanha as alterações no código, reverte alteração no esquema, mas basicamente o que isso quer dizer? Vamos lá, vamos lá, vamos lá. Lembra que a gente pegou? Eu estou falando dos slides assim porque eu quero explicar isso de uma outra forma que talvez seja mais simples de entender. Lembra que a gente criou aquele modelo no código? A gente criou uma tabela

**[01:25:32]** que é uma classe Python, class user, que tem o nome de uma tabela, que tem todos os campos, que tem todas as restrições do campo, do que que é para a Amariki, o que que é Unique, o que que é InitFalse, todas aquelas associações. Então isso aqui vai ser uma string, isso aqui vai ser um inteiro, isso aqui vai ser um date time. Então a gente pegou todo aquele esquema que a gente tinha no código.

**[01:25:54]** E a gente criou uma classe, né? Uma classe de ORM, né? Ou seja, que vai ser mapeada pra dentro do banco de dados que a gente vai usar a aplicação. E não de teste mais aqui. E... Como a gente vai fazer essa transferência de um lado pro outro, é interessante que a gente escreva em um lugar específico do código como aplicar isso no banco de dados.

**[01:26:25]** Massa, então eu preciso falar o seguinte, olha, essas são todas as minhas tabelas, porque você pode dividir em N e arquivos e fazer da forma que você quiser, essas são todas as minhas tabelas referências a esse comit de código, ou seja, quando a gente subir no Git, a gente tem que falar, essas são as minhas tabelas e assim que você deve criar elas no banco de dados. Então, uma das partes da migração é essa. Então, a gente detalha

**[01:26:51]** Então, a gente vai criar um arquivo novo, né? O Alembic, essa ferramenta de migrações, vai criar esse arquivo. E aí, o que acontece? A gente vai pegar e ele vai olhar tudo que tem lá e vai criar um arquivo pra gente. Então, toda vez que a gente for alterando o código, a gente pode gerar novas revisões do banco de dados. Então, por isso que a gente chama de banco de dados evolutivo. Imagina o seguinte, hoje a gente criou essa tabelinha Users.

**[01:27:17]** E aí, a gente tá lá funcionando e tudo mais. Aí a gente tá rodando o código em produção e alguém descobre que tem um bug. Como é que a gente reverte o código? A gente volta no Git, né? A gente tem o versionamento. Então a gente volta no Git. Só que o banco de dados, ele precisa ter uma forma de transitar entre estados diversões na aplicação. Faz sentido isso que eu tô falando? Ou é muito abstrato? E aí a gente tem a opção de como...

**[01:27:47]** levar o banco de dados até a versão do código, ou como voltar até a versão do código. Então a gente faz dessa transferência, a gente chama isso de migração, ou seja, migra.

**[01:27:58]** os metadados do banco entre versões de código. Então, por isso que a gente tá falando aqui, né? Tipo assim, é um banco de dados evolutivo, porque ele evolui junto com a aplicação, é fora daquele stigma, tipo, ah, vamos sentar e decidir tudo do banco de dados? Não, ele vai evoluindo, né? É uma tática ágil de banco de dados. E o banco de dados vai acompanhando a aplicação comite a comite. Então, a gente pode reverter sempre que possível, ir pra frente sempre que necessário.

**[01:28:27]** Massa? Então, é esse o esquema das migrações aqui. Para a gente fazer migrações em Python, eu sei que está tudo muito abstrato ainda, a gente vai fazer mão na massa e vai fazendo junto, a gente precisa dessa ferramenta chamada alambic, ou alambic, alambic de cachaça mesmo. Então, é a ferramenta que faz isso em conjunto com o SQL Alchemy. Então, vamos lá. Poetry, Edge, Alambic. Beleza?

**[01:28:56]** Aí ele criou isso aqui, o Alembic, instalou o Alembic e o Maco, que é uma linguagem de templates do SQL Alchemy. Mas essa migração é na estrutura do banco ou da wholeback nos dados? As duas coisas, a gente vai entender mais ou menos quando a gente for criando aqui. Então, vamos lá. Para a gente usar o Alembic, a gente precisa disso aqui, então a gente precisa rodar o Alembic init migrations.

**[01:29:26]** Lembrando, se você tiver no Shell, então poetry Shell, você pode digitar a Lambic. Mas se você não tiver no Shell, você tiver fora do Shell, então você tem que dar poetry ram a Lambic, só para lembrar isso aqui. Então, o que a gente vai fazer? A gente vai começar com init. Ou seja, eu quero iniciar um sistema de migrações. E a gente vai iniciar esse esquema de migrações numa pasta que a gente vai chamar de migrations.

**[01:29:56]** Mas é um nome padrão que a gente costuma usar. Aí ele deu umas respostas aqui. Ele falou, olha, criei um diretório, né, Creating Director, então ele criou uma pastinha no nosso sistema chamado Migrations. E dentro desse diretório, ele criou um arquivo chamado Versions, um arquivo chamado Script.py, um Readme, um Envio, além de Keyin e várias dessas coisinhas aqui. Então...

**[01:30:22]** Nosso projeto ganhou uma pasta a mais aqui, deixei lá com vocês aqui, essa passinha chamada migrations. Aí aqui ele criou esse envy, um versions e tudo mais, um readme, a generic single database configuration. Lembra que lá atrás a gente tinha comentado, lá na primeira aula quando a gente começou isso aqui, a gente falou que ele ia ignorar algumas coisas, tipo...

**[01:30:47]** lá no rough eu não quero que cheque a pastinha migrations porque você viu o que que aconteceu agora a gente criou e falou a lembra que criam isso aí aí ele criou o código automático e a gente não quer que o rough ou a ferramenta de formatação fique lidando com arquivo gerado automaticamente não quero então foi por isso que a gente colocou isso lá atrás esse migrations poderia colocar agora se fosse necessário mas essa ideia então por isso que a gente adicionou essa pastinha

**[01:31:17]** Legal? Então, ele criou essa nova estrutura aqui. Ele criou um arquivo chamado Alembic INI, aqui na home do repositório. Aí ele está falando, olha, onde é que está o nosso inscrito de migração? Está na pasta migrations. E é onde que isso está? No ponto, né? No lugar exato de onde a gente saiu. Aí ele está falando de coisas de sistemas operacionais, o que vai acontecer depois, os logs que ele vai mostrar aqui, mas basicamente o que é importante é que é isso aqui. Onde está a pastinha? Migrations.

**[01:31:46]** Massa, e aí dentro dessa pastinha tem um arquivo chamado Envy, que é environment, é onde a gente vai configurar a migração. Aqui dentro dessa pastinha versions, é onde vão estar versionadas aquela coisa da evolução do banco de dados para a gente poder ir para frente ou para trás. E aqui tem um script que é basicamente um código de template que ele vai gerar automaticamente para a gente.

**[01:32:08]** não precisa se preocupar muito com essas coisinhas ali. Então, o arquivo para a gente aqui, importante, é esse env.py que está dentro da pasta de migrations, que é onde a gente vai configurar a criação do banco de dados, de fato. Legal? Então, a gente vai alterar esse arquivo env.py e o que a gente precisa aqui? A gente precisa falar para ele aonde está

**[01:32:35]** o nosso settings, a nossa configuração, lembra? Aonde está configurado o nome do arquivo que vai ser o nosso banco de dados, ou aonde ele está localizado, qual que é a conexão dele? Lembra que isso aqui está no arquivo.env, né? E aí o arquivo.env é carregado pelo nosso arquivo de settings, que está aqui. Então é ele que carrega. Então a gente precisa dar um jeito de falar aqui

**[01:33:05]** para o sistema de migrações, aonde está o nosso banco de dados e como é que a gente configura ele. Então esse é um ponto que a gente tem que fazer. E outra coisa é que a gente tem que falar para ele aonde estão os nossos table registers, ou seja, aonde estão os metadados que a gente tinha que configurar dentro desse arquivo.

**[01:33:23]** Saca? Então, basicamente, a gente tem que dar duas informações para a Lembric poder funcionar de fato. Aonde estão os nossos metadados? Lembra? Tem borragem dos pontos metadata. E aonde está a configuração do banco de dados que a gente vai usar para aplicar esse tipo de coisa? E a gente só vai fazer essa configuração dentro da Lembric. Não tem muito aqui, o slide está grandão, mas é super simples. Aqui...

**[01:33:50]** Lá dentro do arquivo, em fp.py, tem um lugar aqui que se chama config. Olha que massa. Aqui ó, config. A única coisa que a gente precisa dizer para ele é o seguinte, config. A gente vai falar para ele, set main options. E vai falar o seguinte, olha, aonde está a URL do banco? A conexão que a gente precisa, que é aquilo que vem lá do VNV. Então, SQL e Alchemy.

**[01:34:19]** Alchemy.url. Aonde está isso aqui? Então, isso foi carregado lá nos settings, né? Então, a gente vai ter que importar os settings para cá. Então, vamos lá. From, Fast API Zero, que é o nome do nosso projeto, ponto settings, e importe aquela classe de settings. E aí, eu vou falar para ele, olha, o que a gente quer é os settings. Então, a gente instancia a classe e a gente fala o database.url aqui dentro.

**[01:34:48]** simples, ou seja, quando a limbic for funcionar, ele vai conectar no banco usando o endereço que está aqui dentro do arquivo envi. Fez sentido essa associação, ela vai muito longe, né, mas... Então, é basicamente essa configuração que a gente precisa fazer aqui.

**[01:35:11]** E aí, aqui embaixo, você está vendo que ele tem aqui o target metadata? Qual que é o metadata do Alvo aqui, né? Então a gente importa aqui, então vamos lá. FromFestAPI0.models import table registry, que é quem tem os metadados que a gente precisa. Então aqui no target metadata, ele está falando, olha, tem que ser o base.metadata. Então a gente tem aqui o tableregister.metadata.

**[01:35:39]** E aí essa é a configuração que a gente tem que fazer aqui. Aí agora a gente linkou todo o sistema, né? Então ele vai usar para criar versões do banco de dados, tudo que estiver em modules, tudo que for registrado no banco de dados, e ele vai fazer isso no banco de dados que estiver configurado lá no .env.

**[01:36:01]** Então isso aqui é dinâmico, eu posso criar cinco bancos de dados, alterar o ponto env e ele vai executar todos os mesmos passos e ao mesmo tempo eu posso ir alterando coisas no modelo aqui e tudo que tiver registrado aqui vai ser refletido na configuração do Alembic. Essa relação que a gente vai fazer aqui. Massa, fez sentido? Essa união de conceitos aqui, então a aplicação e o banco vão desaguar na configuração

**[01:36:32]** das migrações. Tô tendo problemas com isso por causa dos settings do pai identity. Mas qual o problema Ricardo? Então feita essa configuração aqui que é super simples, né? É dois imports, coloca as coisinhas aqui, a gente vai pedir pra ele gerar uma versão, por isso aqui que a gente chama de revision, ou seja, crie uma revisão do banco no estado atual.

**[01:36:59]** Aí quando a gente passa essa flag aqui, auto-generate, ele vai buscar lá nos metadata o que tem e vai configurar. Então ele vai pegar essas configurações tudo o que tem lá no metadata e vai criar um arquivo especificando como fazer essa alteração. Esse é o esquema do auto-generate. E aí o "-m", aqui é só pra gente passar uma mensagem. Ah, criando...

**[01:37:26]** criando tabela de usuários. Eu vou usar essa mesma mensagem aqui. Então, aqui no chão onde a gente está, lembra, se você rodar e falar, ah, não tem Alembic, é porque você está fora do chão. Então, Poetry Run. Massa? Então, eu vou rodar isso aqui. Poetry Run, Alembic, Revision, ou seja, cria uma nova versão autogerada pelo que tem lá nos metadados e o nome dela vai ser Create User Table. Legal. Aí ele deu uma mensagem aqui e falou, olha.

**[01:37:57]** A gente entrou no contexto, a gente assume que a gente está num estado transacional, detectamos que foi criado dentro do projeto uma tabela chamada Users. E aí a gente gerou esse arquivo lá dentro de Migration Versions, um arquivo que tem um hash aqui e a mensagem Create Users Table. E dentro desse arquivo ele descreve como o banco de dados tem que ser criado para comportar essa tabela que a gente gerou no código.

**[01:38:27]** Vamos ver aqui, migrations, versions aqui dentro, ele criou esse arquivo aqui ó, que tem um hash no seu, pode ser qualquer outro valor aqui no começo, mas ele sempre vai terminar com a mensagem que você mandou pra ele. Então, vamos entrar aqui, e aí ele fez o seguinte, olha, essa é a nossa migração, esse é o ID dela, o ID é sempre random, a data em que isso foi criada,

**[01:38:54]** e aqui ele tem algumas coisas de tipo aqui tudo mais porque não importa muito mas ele criou basicamente aqui um upgrade e uma função de da upgrade ou seja como eu volto na versão antes dessa migração beleza não tinha a tabela users então ele dropa ele deleta a tabela users e aí como que ele faz para criar essa tabela então ele está falando aqui olha

**[01:39:21]** A gente vai executar uma operação de Create Table. O nome da tabela é Users. Aí a gente vai criar uma coluna chamada ID que o tipo é inteiro e é Nullable Fals. Aí ele falou aqui ó, a primary key é ID. Tá vendo? Tudo aquilo que a gente escreveu, ele tá escrevendo em uma linguagem de baixo nível do SQL Alchemy, que é a linguagem do SQL Alchemy Core. Então ele vai criar uma coluna ID, uma coluna username, uma coluna email, password, uma created edge.

**[01:39:55]** Aí ele está falando qual é a função que ele vai executar lá, é o current timestamp do banco de dados, quando esse registro for inserido. É tudo nulo ou false. Aí aqui, Unique e Mail é Unique, Username é Unique. Então ele mostra para a gente como o banco de dados faz para chegar nesse estado. É isso que quer dizer o upgrade. E o upgrade é como é que a gente sai desse estado em que a gente criou aqui.

**[01:40:25]** Uma coisa interessante aqui, é que se a gente for ver, ele criou aqui um arquivo do banco de dados aqui. Eu não sei se vocês viram, mas ele criou aqui o database.db. É um arquivo que a gente não consegue ler, um binário e tal. Mas a gente pode inspecionar ele com um Python. Então a gente poderia falar o seguinte, olha.

**[01:40:51]** Python-m para chamar o módulo do Python, o Python tem o módulo do SQLite3, então a gente pode Python-m SQLite3 e passa o database de .db, que é esse arquivo que a gente criou aqui. Olha que massa. Aí, o que que aconteceu? Ele criou uma tabela aqui dentro, uma tabela de banco de dados. Aí o SQLite tem uma tabela chamada SQLiteMaster, então a gente poderia fazer o seguinte, ó, select, escrevendo uma linguagem de banco mesmo, select,

**[01:41:22]** Name From SQ Light Master, se eu não me engano é isso aqui. Master. Aqui. Aí ele criou uma tabela pra gente no banco, chamada Alembic Version. Olha que interessante. Então ele já criou um versionamento do Alembic, mas provavelmente ele tá em versão nenhuma aqui, né? Então se a gente der um Select...

**[01:41:52]** Asterisco from alembro version está vendo que não tem nada. Ele criou a tabela, mas não tem nada aqui dentro. Basicamente é isso que ele está dizendo pra gente, porque a gente não aplicou a migração, né? É ponto quit. Legal. Então a gente saiu aqui, desse modinho aqui. Então a gente gerou essa migração, ele conectou essa coisa no banco e falou, ó, o banco vai ser autogerido por migração, mas ele não tem...

**[01:42:23]** Esse rolêzinho ainda. Se você quiser ver alguma coisa, tipo assim, ah, eu queria ver isso de uma forma mais legal, mais visual. Lembra que a gente instalou o Pipex? Você pode dar um Pipex Run. A gente tem uma coisa chamada Harley Quinn. Deixa eu pegar aqui. Harley Quinn. Então você pode dar um Pipex Run, Harley Quinn e passar o nome do banco aqui. Então, sei lá. Database.db. Ele vai gerar uma...

**[01:42:51]** uma visualização legal de terminal pra gente poder ver isso aqui. Eu vou mandar o comando aqui no chat pra quem quiser rodar aí depois também. Aí legal, ele criou uma coisa aqui que a gente tem do banco. Então a gente tem o database, aí ele tem o main aqui, aí ele criou essa tabelinha aqui, chamada alambic version, e aqui dentro tem o version number, mas não tem nada aqui. Assim, se a gente ver aqui, ele não tem nenhum tipo de dado inserido nessa tabela aqui, mas ele criou.

**[01:43:23]** A Harley Quinn é muito legal, por conta disso dá pra ver as coisas de uma forma gráfica. Eu acho mais simples do que ter que ficar entrando no database, ficar derritando, tudo mais. Então é uma alternativa, é uma opção se você quiser ver isso no Shell. Legal, então a gente gerou essa migração. Ele criou essa estrutura no banco de dados, mas a gente não tem o que precisa ainda. Então a gente precisa aplicar a migração. E aí essa...

**[01:43:54]** Essa migração aqui que a gente vai usar, então a gente vai dar um upgrade, ou seja, lembra? A gente tem aqui dentro do upgrade, então ele vai aplicar isso aqui. O Harley Quinn é no terminal, sim, é uma ferramenta de terminal. A gente vai falar que a gente vai para o head, ou seja, para a cabeça, ou seja, para a última versão que a gente tem, como a gente só tem uma, então ele vai aplicar essa coisa aqui, então a gente pode dar um... Peraí, deixa eu do si aqui.

**[01:44:29]** Então ele vai aplicar essa coisa no banco de dados, ou seja, essa migração aqui. Então ele vai criar essa tabela User com esses campos aqui. Vamos ver. Upgrade, Head. Não encontrado porque, lembra, eu não estou no show. Vamos ver Shell ou Poetry Shell ou Poetry Brand, aí é contigo. Além de que, Upgrade, Head. Aí ele falou o seguinte, olha, Running Upgrade. E ele atualizou para essa versão aqui. Que é aquele hash que ele tinha dado para a gente. Aqui ó, Create Users Table.

**[01:45:02]** Legal. Então, ele criou isso aqui no banco de dados. Se a gente quiser ver com o SQLite, a gente pode vir aqui e fazer aquele select, a name from SQLite Master. Tá aqui, ó. Ele criou a tabela Users. Se a gente quiser ver com o Harley Quinn, o que eu acho mais legal, porque é sempre mais divertido.

**[01:45:31]** A gente pode ver aqui que ele criou aqui um database, tem um main, aí ele criou uma tabela chamada Users, olha que legal. E essa tabela Users tem created at email id password username. E aqui na tabela do Alembic, ele tem as versões aqui dentro. Olha que massa, então se a gente quisesse fazer um select para ver o que está acontecendo aqui, você poderia fazer. Então sei lá, From Alembic Version, então Selecting.

**[01:46:03]** A gente roda com ele aqui, e ele fala olha, a versão tá aqui ó, 23, tal, tal, tal, tal, tal, tal. Aí se a gente usasse isso aqui pra iterar no users, você vai ver que não tem nada porque a gente não inseriu nenhum usuário aqui.

**[01:46:20]** Massa, então tá aqui ó, ID, username, email, password, create, etc. Mas não tem nada, porque a gente não criou absolutamente nada aqui, né? Porque a gente não inseriu nenhum registro. Mas o banco de dados está nesse estado aqui. E aí você fala, ah, beleza, tá nesse estado aqui, ok. Se a gente quisesse reverter essa coisa, a gente poderia fazer um downgrade. Downgrade. Aí a gente precisa ir para algum lugar, né? E aí, como é que a gente fala? Que a gente quer voltar uma, a gente dá um menos um.

**[01:46:53]** Aí ele voltou, relativo a Minuzum não produziu nada, tudo mais, mas se a gente abrir o banco de dados agora, você vai ver que ele não tem a tabela, tá vendo? Porque ele não tá em nenhum lugar.

**[01:47:09]** Ou seja, não tá em nenhuma versão. Então a gente pode, essa é a grande ideia aqui, a grande sacada da migração. Então a gente pode ir de um estado pra outro. Então a gente vai pro próximo volta, pro anterior. Então amanhã a gente cria outras tabelas, então a gente precisa transacionar de uma coisa pra outra, de um lado pra outro. Então a gente consegue versionar isso, baseado nesses arquivos aqui. É isso que o Alembic faz. Então ele cria uma...

**[01:47:36]** um esquema de visualização onde a gente pode ir pular, saltar entre versões dos modelos que a gente tem dentro da nossa aplicação. Então, a gente pode fazer essa transferência entre um lado e outro. Fez sentido a função do Alembe? Que que? Fez sentido que ele faz essa coisinha aqui? E aí que eu tinha colocado uma coisa aqui, né? Para a gente ver o Shell, o Alembe aqui embaixo, o New Users e tudo mais. Acabei mostrando o Harley Quinn, porque eu adoro o Harley Quinn, mas...

**[01:48:15]** Vocês podem usar da forma como quiserem aqui. Bom, antes da gente finalizar aqui, quem tiver dúvidas já pode ir mandando as perguntas. Dúvidas, por favor, não preciso dizer, dúvidas sobre a aula. Aí, por favor, deixem as dúvidas sobre a aula, sobre o conteúdo. Eu vou mostrar os exercícios aqui para vocês que deverão ser feitos dessa aula.

**[01:48:41]** Mas a gente vai comitar e já está liberado. Eu vou ficar mais um tempinho aqui para a gente responder as dúvidas. Massa? Então, legal. A primeira coisa que a gente precisa fazer aqui é o seguinte. Fazer uma alteração no modelo user. Aí eu quero que vocês adicione um campo chamado updated at nessa tabela aqui, nesse módulo. Massa? Então, eu quero que vocês adicione um novo campo chamado updated at.

**[01:49:11]** Aí o campo deve ser do tipo DateTime, ele tem que ser initFalse, o valor padrão deve ser funkNOW, e que é isso aqui, funkNOW. Aí lembrando que vai ter que fazer o teste, então a gente vai ter que alterar o evento de teste que a gente tem, o mockDbTime, para contemplar o campo updatedAt, também na validação. Então é esse esquema aqui.

**[01:49:44]** que a gente precisa usar. Aí depois, o terceiro exercício é criar uma nova migração autogerada com a Lambeck, e aí eu quero que vocês apliquem essa migração no banco. Ou seja, a gente vai mexer em praticamente tudo o que a gente fez. A gente vai ter que alterar o modelo, a gente vai ter que alterar o MochDB Time, aquela função, o evento que faz a coisa, a gente vai ter que gerar uma nova migração, e a gente vai ter que aplicar essa migração no banco. Ou seja, tudo o que a gente viu hoje está envolvido nesses...

**[01:50:13]** quatro exercícios que a gente tem aqui. Massa, esse é o exercício. Lembrem-se, não se esqueçam, a aula tem o quiz. Então, respondam o quiz. O quiz tem umas dez questões aqui para ir vendo o que está acontecendo e tudo mais. Massa, e aí eu vou subir isso aqui no git-add, git-commit e tudo mais. Então, git-add. Eu só quero o comit, não?

**[01:50:41]** Bom, a Git é de ponto, vou subir tudo. Git comit, então, adicionada a primeira versão do Alembro, criando a tabela de usuário e Git Pesh. Então, subi meu código aqui. E por hoje é só. Então, quem tá cansado, sabe? Tem coisa pra resolver, criança. Pistola do trabalho. Boa noite, eu vou responder as perguntas agora, então quem quiser ficar pras perguntas, mas quem quiser aí, tá liberado. 9 minutos mais cedo, hein?

**[01:51:12]** Estou liberando todo dia mais cedo. Beijo pra vocês, a gente se vê na quinta-feira, pra quem for agora, e eu vou responder as perguntas aqui agora, que me deixaram em relação ao fim da aula aqui. Ah, vamos lá. Pergunta, tem como reduzir o comando das migrações? Sim, você poderia criar um Task Migration. Tá tudo bem. É totalmente opcional. Como não é um comando que eu rodo toda hora, eu não fiz o Task Pie, mas você pode fazer.

**[01:51:46]** Estou resolvendo e me dei muita moda. Achei que ia precisar de Pytest e Envy, mas é mais simples. Obrigado. O que é isso? Tamo junto. Pergunta, tem como ter seeds no alembe? Essa é uma pergunta interessante que o Yago fez. Pra quem não sabe, eu sei que são seeds. Seeds.

**[01:52:01]** são dados iniciais, estruturais que você pode colocar na sua aplicação e na hora de gerar a migração. E sim, você pode gerar seeds, você pode gerar os seeds manualmente, se você quiser, aqui no... pera aí. Você pode vir aqui no arquivo de migrações e falar que essa migração específica, aqui, deixa eu achar aqui, migration, essa migração específica vai fazer algumas coisas aqui, então você tem essa operação aqui, você pode falar P, ponto, sei lá.

**[01:52:31]** Create de qualquer coisa ou qualquer outra coisa que você quiser. Ah, você tem esse users aqui, você pode importar ele aqui, né? Você tem essa tabela users, sei lá, From, SQL Alchemy Import, tal, tal, tal, você pode fazer isso aqui. A coisa da migration aqui que você pode fazer é o seguinte, quando você dá um migration aqui que você não quer auto-gerar pra ele não usar aqui, você pode falar, sei lá, inserindo seeds, por exemplo, só pra mostrar um esquema aqui. Então você poderia falar,

**[01:53:01]** Criando seeds. Massa não tem auto revision, tá vendo? Então ele gerou uma migração vazia aqui. E aí você escreve o que você quiser aqui. Aí você pode importar o modelo, a sessão, inserir seed, fazer o que você quiser aqui. Então é totalmente possível. Você pode fazer o rolezinho o que você quiser aqui. Massa, tem uma biblioteca...

**[01:53:32]** A Lambex... A Lambex Sidi, se eu não me engano. Python, a Lambex Sidi. S, que ele é álbum Sidi. Eu não lembro exatamente o nome da biblioteca agora. Me lembra isso lá no grupo? Eu mando depois o nome da biblioteca. Mas tem uma biblioteca que faz com que você possa escrever...

**[01:53:57]** Arquivos, tipo Yam, Tom L, tal, que podem gerar seeds. Será que é SQL Alchemy seed? Eu não me recordo. Aqui, SQL Alchemy seeder. É isso aqui. Não é essa biblioteca aqui. Tem outra, mano. Tem outra. SQL Alchemy seed. Eu lembro que a documentação é esse aqui, mano. É esse aqui, que pode ser várias coisinhas. É esse aqui mesmo.

**[01:54:31]** Aí, se você precisar, então você pode criar em JSON, YAML, tal, tal, tal, aí você monta o seu próprio seed, quais os modelos que você quer, e aí ele performe isso aqui dentro da limb, que se você quiser. Então, é uma forma de gerar isso aqui, se houver necessidade. Massa? Ah... Mas, passei a Ragnar e criei a migração, mudei a mic para vai git, pasta vazia, não subiu para o git, se não conseguir criar a migração do micro 2. Mano, tira as dúvidas lá no grupo, a gente vai acompanhando.

**[01:55:06]** Depois de um tempo vi que basta criar a versão na mão e deu tudo certo. Sim, você pode criar na mão. É uma parada. Beleza. Estou tendo um erro de validation settings no momento da revision. Settings, abre fecha parênteses, ponto database recide. Talvez esteja alguma coisa errada lá.

**[01:55:29]** ou não esteja acompanhando o esquema. Bom, todo mundo que está tendo a aula erro de código, manda lá no grupo, o link do grupo está aqui na descrição, a gente vai conversando e tentando resolver, porque aí vocês mandam um pedaço de código, a gente vai olhando, porque aqui no chat não fluiu muito bem aqui. Sabe esse tipo de coisa. Tem como limitar o Envy, por exemplo, rodar o comando, criar no banco local dentro... Cara, a gente não estava vivendo Docker, Docker era lá na aula...

**[01:55:55]** 10, mano, aí a gente conversa sobre isso. E o Dog Grid em Prod, como ficam os dados? Se você dropar a tabela, ele vai dropar os dados de produção.

**[01:56:03]** Aí, se você precisar fazer um upgrade, que adiciona um campo a mais, então, a gente viu a migração autogerada, né? Então, a ideia é que aquele campo lá, igual a gente viu sem uma autogerade, é que você trabalhe lá na migração, você coloca o que você precisa, você vai alterar a data, coloca as alterações que você precisa, se você precisa mudar no dullgrade, você vai colocar lá. Então, a ideia é que você vai mexendo na migração na mão, né? Tipo assim, beleza, ele gera o arquivo sozinho aqui, né? Mas...

**[01:56:30]** A ideia é que você também pode interagir com isso, né? Tanto que ele tá falando. Common Algerated by Alembic, please adjust. Ou seja, isso aqui é auto gerado, né? Gerado automaticamente. Por favor, ajuste. Então, beleza. Ah, em produção tem um campo que precisa ter um registro, tá? Não sei o quê. Então você vem aqui e aí você vai mexendo aqui e vai fazendo todas as alterações que você precisa. Massa?

**[01:56:56]** Então é isso. E aí como é que fica em produção e tal? Então dá pra gerar migrações offline e alguns outros tipos de coisa. No código da aula, aqui no esquema da aula, se vocês quiserem, pra quem quiser mais curiosidade, quiser ver umas coisas mais avançadas, a gente tem uma live de Python sobre migrations. Então vale a pena dar uma assistida.

**[01:57:26]** que aí eu falo especificamente sobre as coisas, como é que o que que muda, onde muda, como é que funciona o esquema, tipo que cria a migração na mão, faz uma migração offline, online, gênero SQL, algumas dúvidas vocês podem ter, tudo tá aqui, então meio que é isso. Depois a gente vai usar o outer column, porque cria a segunda deu errado, então, mano. Esse é o exercício, Rodrigo. Esse é o exercício, mano.

**[01:58:04]** Beleza, então beijo pra vocês, a gente se vê na quinta-feira e a gente começa a implementar essas coisas na aplicação. Agora a gente tem o banco de dados e tudo mais e a gente conversa sobre isso na semana que vem. Esse navegador é o Zen. Massa, então beijinho pra vocês, a gente se vê na...

**[01:58:31]** Na quinta, para começar a fazer aquele crude, misturar ele com coisas do banco de dados. Legal? Beijinho para vocês. Tirem as dúvidas, dúvidas com o código. Manda um pedaço de código, algumas coisas, a gente vê lá. Mas é necessário fazer um banco separado. Não, a gente... Bom, Thiago, a gente fez um banco separado na hora de fazer os testes, dá uma olhada. A gente fez isso na aula, menina. Beijo para vocês, ó. Até quinta-feira, vamos conversá-la no grupo.

**[01:59:03]** Beijinho e tchau!

