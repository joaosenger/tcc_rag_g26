# Transcrição da Aula: aula-05.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:08]** Olá, pessoas! Boas-vindas! Há mais uma aula, o nosso sexto encontro, né? Aula 5 do Curso de Fecha API. Eu sou do Nosauro. E... Boas-vindas! Sinta-se em casa! Antes de tudo, antes de a gente começar a saber aquele negócio. Vocês estão me ouvindo, vocês estão me vendo, tá tudo funcionando. Só fala assim, ok, tá tudo funcionando. Só pra eu saber que eu não tô falando sozinho aqui com as nuvens aqui, ó. Tipo assim, uuuh!

**[00:00:34]** viajando no espaço sideral sozinho aqui. Massa!

**[00:00:40]** Enquanto vocês me dão um feedback para eu saber se está tudo certo, eu queria falar com vocês que hoje a gente vai conversar sobre a integração no Banco de Dados Go State, assim, Hello World, tudo ok, foi muito bom. Hoje a gente vai fazer a integração do Banco de Dados com a nossa API e aí a gente vai usar o SQL Alchemy, que a gente começou a configurar aquela coisa que a gente fez na aula passada e vai trazer isso para integrar, fazer integração disso.

**[00:01:09]** com a nossa API. Então, a gente vai ver algumas coisinhas, né? Como fazer essa integração, a gente vai aprender um pouquinho sobre injeção de dependências, né? Que é um conceito bastante interessante, né? Dentro da engenharia de software, de maneira geral. A gente vai modificar, né? Todos aqueles indipontes, né? Que a gente fez, que tinha aquele banco fake. E a gente vai testar esses novos indipontes. E a gente vai ver novos desafios de fazer testes com os bancos de dados e tudo mais. Algumas coisas que a gente já deixou preparado na aula passada, mas...

**[00:01:40]** Vamos trilhar um caminho a mais aqui hoje. Bom, não custa nada dizer que essa aula está aqui de novo, está tudo aqui, tudo escrito, tudo bonitinho. Ó, maravilhoso, então tem uma acessada, se tiver algumas dúvidas, tem o grupo, vamos conversando. E o Harano falou, like, tem mais gente vendo que like, sempre. Por favor, me ajudem a disseminar conteúdo de qualidade gratuito na internet. Vamos lá.

**[00:02:10]** Então beleza, esses são os nossos objetivos hoje e é sobre isso que a gente vai conversar. Bom, lembra que na aula passada, para quem estava assistindo junto com a gente, a gente deixou uma coisa meio subjetiva, que era a Session, que era aquele meio do caminho que a gente conectava, fazia a Engine, e a sessão era quem trafegava os dados que a gente tinha na nossa aplicação no conteúdo Python.

**[00:02:35]** e fazia isso trafegar para o banco de dados, então acessam e ela faz meio que esse meio de campo. A gente conversou bem superficialmente, então queria tirar os nossos primeiros minutos hoje para conversar sobre a sessão do R&M e como é que ela funciona, qual é o escopo dela dentro da nossa aplicação aqui. Então, toda essa comunicação, eu falei na aula passada, mas eu acho bom reiterar. Toda vez que a gente for interagir com o banco de dados,

**[00:03:02]** A gente vai passar por essa sessão. A sessão é o importante aqui. E a sessão implementa vários padrões de projeto para quem vem acompanhando a série de padrões de projeto ou para quem já tem um pouco mais de experiência nessa área de engenharia de software. A sessão...

**[00:03:19]** Ela implementa várias coisinhas, que são muito importantes. E a gente falou, algumas vantagens de usar o RM na aula passada, mas aqui ficam claras algumas coisas e por que essas escolhas são interessantes aqui. Bom, a sessão implementa, sei lá, uns sete padrões de projeto desses de aplicação mesmo, de enterprise e patterns.

**[00:03:46]** padrões empresariais, um deles é o repositório. E o repositório é a ideia de fazer essa abstração da comunicação com o banco de dados, ou seja, eu nunca interajo com o banco de dados. Toda vez que eu preciso fazer uma persistência ou pedir um dado ou fazer esse esquema, a gente vai passar por uma camada de código Python.

**[00:04:09]** sem ter que fazer interação direta com o banco, né? Aí você lembra que isso aqui traz várias vantagens, aquele negócio de não ter SQL Injection, tem algumas camadas preparadas de segurança pra isso, e aí ele a gente consegue pegar e falar, olha, sessão, a gente vai trabalhar com esse, com essa tabela, essa coisa, e a partir disso a gente vai derivando o código dentro de um escopo controlado, né? É basicamente essa a função do repositório, se a gente for olhar de uma forma superficial, porque daria pra gente fazer uma aula inteira sobre ele, né?

**[00:04:39]** O segundo ponto a gente conversou na aula passada, que é a unidade de trabalho, ou unit of work, que a ideia da...

**[00:04:48]** da sessão aqui é atuar, como esse Gateway, esse repositório, essa coisa que a gente permeia sempre por ela e unidade de trabalho quer dizer que a gente vai executar várias ações, adiciona um usuário, adiciona outro, modifica um, a gente vai fazer várias operações e todas essas operações vão ser despachadas para o banco de dados com uma única.

**[00:05:12]** operação, ou seja, como uma unidade de trabalho. Então, a gente vai fazer várias coisas dentro da sessão, de maneira volátil, em memória, e aí, a hora que a gente der aquele comit, uma afirmação que a gente quer fazer a operação, ele vai ver todas as ações da sessão e vai fazer uma única chamada para o banco, garantindo uma certa... Como que eu posso dizer? Além da integridade, porque a gente...

**[00:05:40]** tem menos locks no banco, tem menos travas, a gente vai fazer esse esqueminha de, pô, vamos performar uma ação só? Massa, resolver o problema. E o terceiro padrão que a gente implementa é o mapeamento de identidade, o identity mapping em inglês, que é a hora de criar um cache.

**[00:06:02]** dentro da sessão, né? Uma forma simplória também de falar sobre isso, né? Também daria uma uma aula inteira sobre isso, mas é a ideia de a sessão carrega, né? Algumas coisas, né? A gente mapeia o que tá acontecendo dentro do código e beleza, a gente já inseriu, sei lá, o user Regis, que foi a última pessoa que comentou aqui no momento, então a gente adiciona o Regis. Se a gente adicionar o Regis de novo

**[00:06:29]** Ele sabe, tem esse cache, esse mapeamento das entidades que estão lá e quando a gente vai alterando coisas, da forma que a gente vai trabalhando com isso, a gente vai... Saca!

**[00:06:42]** trazendo esse ponto de comunicação. Ou seja, não vai persistir cinco users na mesma sessão. Então, vai ter um gerenciamento de memória um pouco melhor. Então, a gente faz esse tipo de coisa. O álbum não perguntou se a session não faz cache, né? O identity map é uma forma de cache, mas quando eu penso em cache, eu acho que você tá falando de uma coisa que persiste, né? Na aplicação e tal, durante um tempo maior. O SQL Alchemy.

**[00:07:10]** Tem uma forma de trabalhar com cache, é uma outra biblioteca assim como a Lembe, que é um puxadinho do SQL Alchemy, que é o DogPill. E aí o DogPill, deixa eu pegar aqui pra vocês, DogPill, pra quem quiser dar uma olhada, SQL Alchemy. Aqui, é um mecanismo de cache do SQL Alchemy. Saca?

**[00:07:52]** Então, se vocês precisarem disso de main cache, cache em memória e tal, o SQL Alchemy tem essa opção. Aí você pode trabalhar com o main cache mesmo, com a biblioteca, ou você pode trabalhar com o Redis, que é uma outra forma de ver isso aqui.

**[00:08:05]** Mas essa questão de ações de unidade de trabalho pode ser relativa à regra de negócio. Sim, aí você tem que trabalhar com transactions. E a gente tem uma aula do SQL Alchemy que a gente discutiu, que eu dei como referência, e lá a gente discute sobre transactions. Aqui a gente não vai falar sobre transactions ao mesmo tempo. Massa?

**[00:08:26]** Então, essa é a ideia da sessão, né? A sessão implementa três padrões de projeto clássicos que são importantes, né? Pra essa nossa comunicação e, além, né? Se a gente fosse olhar isso aqui de uma forma mais, saca, mão na massa pra não ficar muito abstrato, deixa eu agradecer o álbum aqui que...

**[00:08:45]** Pagou o cafezinho para nós? Obrigado, mano. Esses super chefs me ajudam muito, mano, muito. A manter a infraestrutura aqui das coisas. Então vamos supor que a gente tem esse... eu coloquei com um endpoint, mas poderia ser qualquer código Python. A sessão ela tem essa distribuição de executar coisas, de performar coisas. Então a gente tem o edge, o delete, né?

**[00:09:07]** Quando a gente pensa em Edge, as pessoas pensam em persistência no banco, mas a gente está adicionando um objeto, a sessão, a gente está removendo, deletando um objeto da sessão, a gente tem o refresh, que é uma forma de atualizar o objeto em sessão, ou seja...

**[00:09:24]** Vamos supor que a gente esteja trabalhando com um banco que está performando online, com várias ações. A gente precisa atualizar um registro que já está na session. Então, a gente usa refresh, a gente tem o holdback, que é uma forma de desfazer a unidade de trabalho, sei lá. Ah, eu adicionei umas coisas aqui, mas deu erro a hora que fui persistir. Então, a gente faz um holdback e volta, tem o commit, que é aquela coisa de executar as unidades de trabalho e tem as formas de buscar, os colors, que é para a gente...

**[00:09:53]** Trazer todos os resultados de forma escalar, ou seja, como objetos, e o Scalar para trazer um resultado único. Em código, isso se transfere mais ou menos dessa forma aqui. Então, a gente pega o SQL que me fala, olha, cria a Engine, a gente...

**[00:10:08]** Cria a sessão, né? A sessão pode ser dada com um block with, né? Que foi alguma coisa que a gente viu na aula passada. E aí a gente faz isso aqui, né? Adiciona, remove, atualiza. Scalers, commit, holdback. E isso aqui adiciona no banco e adiciona na sessão, né? Ele só vai adicionar no banco quando um commit for feito e vai deletar da sessão caso ocorra um holdback aqui, né?

**[00:10:32]** Então, mais ou menos essa é a cara, né? Da sessão do SQL Alchemy. É assim que a gente vai interagir com o banco. Então sempre a gente vai pegar essa sessão, vai trabalhar com ela e a partir dela a gente comita e insere as coisas no banco de dados. Então a gente vai sempre fazer esse intermédio e passar pela unidade de trabalho aqui.

**[00:10:51]** Massa, fez sentido isso aqui? A gente fez um código mais subjetivo na aula, mas aqui a gente tem essa gama de opções que a gente pode usar session, né? Que ela já implementa vários padrões e isso é muito legal. Quem quiser ver mais coisas sobre... sobre...

**[00:11:11]** Os padrões de projeto, o Mike Bayer, o criador do SQL Alchemy, tem um blog post falando sobre isso aqui, acho que pode ser interessante para quem quiser ver, o Data Map, Unit of Work, Data Map, Metadata Map, Query Object, Reposter, Lazy Load, são um montão de padrões. Esse aqui é o Mike Bayer, o criador do SQL Alchemy, esse é o blog pessoal dele.

**[00:11:34]** E aí tem essa postagem aqui, pode ser interessante, caso alguém esteja estudando essa parte mais de engenharia, mais pesada assim, para conseguir procurar mais recursos sobre isso. Bom, antes de a gente ir para a implementação, pô, Moringa, obrigado pelo Super Chat, um beijo. Valeu aí pelo Monsa, Johnny, um chá de baita. Obrigado aí para vocês, valeu demais, isso me ajuda muito, mano, valeu demais. Bom!

**[00:12:03]** Para a gente sair dessa parte mais subjetiva, dessa coisa que a gente está pensando e tudo mais, eu quero pensar com vocês ou repensar o endpoint que a gente já implementou, aquela rota, a URL de cadastro, o post. Eu quero começar com ele aqui, porque para a gente poder entender as coisas, como elas estão no banco, seria interessante a gente adicionar essa informação no banco primeiro.

**[00:12:26]** Então, vamos pensar um pouquinho naquele endpoint de cadastro que a gente tem aqui, né? Eu vou vir aqui no código, né? No FastAPI Zero, lá no app, a gente tem o CreateUser, né? Que é esse endpoint aqui que a gente tinha feito algumas aulas atrás, né? Então, a gente tentou simular um DB, a gente colocou isso em memória e tudo mais. Então, vamos repensar um pouquinho essa coisa e como ela tem que interagir com os dados, né? Que trafegam com a forma como a gente usa esse código, né?

**[00:12:55]** Bom, quando a gente vai cadastrar alguém na base, a primeira coisa que a gente tem que fazer é validar se aquilo está de acordo com o esquema, com os dados que a gente queria que viessem, que é o user public aqui. E essa validação a gente já ganha de graça. A gente só precisa configurar no pai dente que ia associar esse ao endpoint. Então, as outras preocupações que a gente precisa ter, lembra quando a gente criou nossa tabela? O e-mail era do tipo Unique. Deixa eu abrir o nosso modelo aqui.

**[00:13:24]** Então, o imenho ele é unique?

**[00:13:29]** O username também é unique, né? São duas coisas que são unique, ou seja, não podem ser repetidas dentro da nossa base. Então, a gente vai ter que pesquisar antes de inserir. Então, a gente vai ter que olhar e falar, pô, na base de dados, quando a gente for transacionar esses dados, já existe alguém que tem esse e-mail ou já existe alguém que cadastrou esse username aqui? Então, é interessante a gente saber disso diante, mano. Se existir, a gente vai ter que retornar um erro, né? O erro...

**[00:13:57]** Http para essa operação é o 409, que é o conflito, já existe na base de dados. E aí caso essa coisa não aconteça, a gente vai ter que inserir esse registro efetivamente dentro do banco de dados. É mais ou menos essa operação que a gente quer simular aqui, ou seja, a gente vai receber os dados no endpoint, vai ver o pai dente que já vai lidar se isso está na forma que a gente precisa, e a gente vai fazer uma coisa, perguntar, ó...

**[00:14:22]** Select e tal, e-mail e username e tal na tabela e ver se tem algumas coisas, né? O where, né? Onde o e-mail é igual ao e-mail que a gente recebeu, ou o username é igual ao username que a gente recebeu. Se sim, a gente vai retornar um erro. Vamos começar por aqui, né? Então, é basicamente essa operação que a gente quer performar aqui, né? E aí aqui eu deixei mais alguns detalhes, né? Tipo assim, os unique, né? Não pode ser reedicionados, né?

**[00:14:53]** Se existir, a gente usa aquele rise e a HTTPception que a gente colocou. E aí, para a gente conseguir fazer essas coisas, para adicionar na sessão, é o Edge. E para persistir a sessão no banco, a gente vai dar o Comet. E aqui, para checar, é o Scalers. Ou Scalers, dependendo de como você quiser ver isso aqui. Então, legal. Tem muito código aqui. Eu vou fazendo isso...

**[00:15:18]** devagarzinho com vocês, né? Daquela mesmo formato que a gente viu na aula passada, a gente pega a Engine, cria e faz todo o rolezinho que a gente tinha ali, né? Então, legal, pra gente inserir isso aqui, pra gente fazer essa comunicação aqui com o create user, a primeira coisa que a gente precisa é dar conexão com o banco de dados, né? A Engine, o Engine, o motor, do banco de dados. Então, a gente vai precisar fazer isso aqui, né? Engine.

**[00:15:44]** E aí para a gente chamar a Engine, a gente vai precisar daquela função do SQL Alchemy que cria a Engine. Eu vou fazer tudo aqui dentro do Endpoint e depois a gente vai distribuindo os imports da maneira que for necessário. Então beleza. From SQL Alchemy Import Create Engine. Então a coisa que a gente quer fazer aqui é criar uma Engine. Aí vocês lembram que a nossa conexão com o banco de dados, quem é que sabe?

**[00:16:10]** O endereço que a gente precisa se comunicar com o banco. A gente colocou isso lá naquele arquivo que a gente chamou de ponto envi. E esse arquivo ponto envi, ele está sendo lido pelo paydantic settings que está dentro do nosso arquivo de settings. Então, a gente precisa importar os settings.

**[00:16:32]** lá no app também aqui, né, pra passar pra Engine. Então, vamos lá, então, From Fast API Zero, né, que é o nome do nosso projeto, se você botou outro nome lembre-se que isso vai mudar, ponto settings import, né, então a gente vai importar a nossa classe de settings que a gente criou lá dentro. Então, a Engine que a gente quer aqui é basicamente os settings que é a classe que a gente queria e o valor que a gente quer é o database URL, né, que é exatamente o que a gente tinha aqui no nosso...

**[00:17:05]** Então, a partir disso, a gente já consegue se comunicar, né? A gente tem a conexão com o banco criada aqui. Eu sei, tipo assim, não tá um código bonito por enquanto, mas tudo bem. Essa é a ideia do que a gente tem aqui. A partir dessa engine, né? O que a gente precisa? Agora a gente precisa criar uma sessão, né? Assim, a gente já tem a conexão estabelecida, mas agora a gente precisa abrir o meio de campo, o túnel por onde a gente vai se comunicar com o banco de dados, né? Então...

**[00:17:33]** Essa é a grande hora aqui. Então, eu vou fazer from skelhalkim.orm import session, que é aquela sessão que a gente tinha na aula passada. Aqui, nesse exemplo, eu atribuí a session, a gente poderia fazer weave, tal. Eu não estou ligando muito para esse código da forma como ele está aqui, porque a gente vai melhorando ele conforme a gente for entendendo mais conceitos. Massa? Então, a gente vai criar essa session aqui.

**[00:18:05]** E aí a Session depende da Engine, da conexão com o banco de dados que a gente tinha. Legal, a partir disso, o que a gente precisa fazer aqui, né? A gente precisa pegar os dados que vieram de User e buscar por eles na Session. A gente viu, na aula passada, como é que fazia uma quernar quando a gente estava escrevendo o teste, né? Então, que era o Session.Scholar.

**[00:18:29]** poderia ser escala no singular para procurar um, escala no plural para procurar vários, para a gente estar tudo bem um só nesse momento. E a gente precisa dar a instrução de SELECT para fazer a busca. Então vou importar daqui o SELECT do SQL Alchemy. Então legal, a partir disso aqui a gente vai executar esse SELECT e para esse SELECT funcionar a gente precisa dizer em qual modelo a gente está trabalhando. É muito parecido com o que a gente fez na aula passada.

**[00:19:00]** Então, aqui a gente precisa do modelo, né? Então, From Fast API Zero, que é o nome do nosso módulo, ponto Models, Import User, que é quem a gente quer buscar aqui. Então, a gente vai fazer um Select em User. Aqui eu dei o nome de Debate User, eu vou manter o mesmo nome só para não esquecer depois. E aí, o que a gente vai fazer? A gente vai fazer uma busca na tabela de Users, né? E aí, o que a gente quer ver?

**[00:19:33]** A gente quer ver aquele ponto que a gente tinha colocado no slide. Se o email ou se o username estão acontecendo aqui. Então a gente vai procurar um where. E aí o que a gente quer? A gente quer saber se o user da classe que a gente tem aqui, ponto username, é igual ou igual a alguém. Isso aqui a gente vai trabalhar aqui melhor. Ou então, se o user ponto email

**[00:20:07]** user.email é igual a algum dado aqui. A forma de fazer o ou aqui é com esse operador de pipe. Então aqui a gente está fazendo selecione todos os usuários onde o username é xpto

**[00:20:34]** ou o e-mail é xpto. Para isso aqui ficar bem estruturado, para não ter confusão depois na hora de reproduzir no seu código, você pode botar uns parênteses aqui para ficar mais simples de ler aqui. Então, da onde vêm esses dados? Nesses dados vêm do endpoint, igual a gente estava usando aqui. Ah, veio do user, a gente pode pegar o user que tinha aqui, aí ele tinha os dados que a gente queria.

**[00:21:02]** Então, é esse user que a gente recebe no endpoint que vem do user-scheme, mano. Então, a gente vai chamar o user, minúsculo aqui, ponto username. E a gente quer saber se é esse meio ou, então, se, pera aí que eu tô na frente, ou então se é igual a e-mail. Massa, fez sentido esse comando aqui? Tá todo mundo ou...

**[00:21:36]** Ou todo mundo entendeu ou eu estou perdido aqui? Eu estou sozinho nessa. Quando não tem nenhuma pergunta é bizarro. Mas é legal, então a gente vai fazer uma busca para procurar se o username ou o seu e-mail já foi cadastrado dentro da nossa aplicação. Se isso aqui tiver uma resposta, né? Então aí entra o caso, né? Se DB User existir,

**[00:22:06]** Porque tem que lembrar de uma coisa aqui, né? Do Scalar. O Scalar, ele vai retornar ou um user, né? Ou none. É esse tipo de dado que ele vai dar pra gente aqui, né? Então, se for none, a validação vai dar certo, né? Então, a gente quer saber se não o user, né? If not user, ou seja, se voltou none,

**[00:22:41]** Significa que não inseriu ninguém. Se voltou true, significa que encontrou alguém, voltou o user. Então eu vou dar o if pro erro, né? Ah, você faz da forma que você acha mais legal aqui. Eu prefiro fazer o erro, né? Então aqui a gente vai retornar um erro. A gente vai retornar um erro aqui dentro. Massa. E aí se retornar um erro aqui dentro, a gente não vai. Vai pra onde aqui, né? Então...

**[00:23:13]** Se não der o erro, a gente vai voltar. A gente vai ter que tirar isso daqui e a gente persiste. Então se der o erro, se não der o erro, então aqui é se não der o erro. Massa? Então é isso aqui. Esmael, obrigado pelo... por fazer parte do clube de membros. Valeu demais, mano. Aí... o Adrel tá falando. Manipulando o banco direto da Vio. É, mano, é um curso inicial, né, mano?

**[00:23:44]** No seu projeto você pode fazer da forma como você quiser. Uma hora a gente vai refatorar isso aqui. Tem porte aqui dentro, tipo assim. Entender o conceito. Massa? Então é essa a ideia que a gente é. A gente vai checar se os valores únicos foram. E aí a gente fez os primeiros três passos aqui, né? O email existe ou o username se não retorna um erro. Beleza, a gente vai melhorar esse erro aqui, mas a gente tá indo aqui, né? Como é que a gente vai fazer isso aqui, né?

**[00:24:17]** Em algumas formas aqui, como a gente está fazendo isso de uma maneira didática? Eu vou retornar exatamente... Eu acho que caí aqui, né? Eu não sei se eu voltei. Voltou? Então massa. Valeu aí César, pelo aviso. Então legal. Num quesito de segurança, pode ser que você não queira fazer exatamente dessa forma. Eu...

**[00:25:09]** Eu vou fazer aqui porque a gente tá sendo didático aqui, mas não recomendo esse tipo de abordagem aqui em produção, mas é saber. Tá tudo bem. Então, o que a gente vai fazer aqui? Se tiver esse erro aqui, então a gente vai perguntar, if the Bay User ponto username foi igual ou igual a user ponto username?

**[00:25:42]** A gente vai fazer o quê? Vai retornar um erro de conflito falando que isso aqui já existe, né? Então, a gente vai dar um rise aqui, né? Então, rising. Httpception, né? A gente já viu isso aqui, não? Aqui. E aí, a gente vai ter que dar um detalhe aqui e falar qual que é o erro que a gente quer, né? Então, o erro, né? O status code que a gente quer é 419, que é o status code de conflito. E aí, a gente pode dar uma mensagem aqui. E a mensagem do erro fazer sentido ou não, né?

**[00:26:19]** Eu não sou o maior fã dessa abordagem aqui. E aí você pode fazer tipo assim, um ELSI, um ELIF, aí é contigo aqui. E aí, SI, né, é a mesma coisa, né, que a gente vai mandar aqui, né. SI, o DB e-mail já existe, você vai falar que é tipo assim, ah, e-mail already exists. Massa? É uma forma de resolver esse ponto aqui. Então, a gente valida, né, se existe um conflito.

**[00:26:50]** O que vai acontecer aqui? Massa, então depende muito da forma como você quer lidar com esse erro. Eu particularmente juntaria tudo em um só, mas aí é com cada um. Então legal, se a gente for cadastrar um user que já existe, esse user vai explodir. E aí, caso tudo der certo, caso não exista nesse user que a gente quer, aí a gente faz aquele processo. Cria o user, adiciona ele na base de dados.

**[00:27:24]** adicione ele na sessão, faz o commit e a gente vai usar esse refresh aqui né esse refresh ele é meio opcional aqui também eu gosto porque simplifica né mas aí é com cada um então a gente vai fazer o seguinte beleza não caímos nesse nesse ponto aqui né mas a gente vai criar né agora o user né então o user vamos pensar que não caiu eu vou chamar de debate user mesmo eu chamei de debate user então tá tudo bem debate user vai ser o user que a gente tinha

**[00:27:55]** E aí a gente pode fazer de uma forma simples, tipo assim, passando todo mundo, username é igual a user.username que veio lá do parâmetro. Ah, email é igual a email. E password é igual a password. Password é igual a passwords. Você poderia fazer assim, você poderia fazer daquela forma como a gente viu na outra aula, tipo assim, de fazer o unpacking.

**[00:28:27]** Também está permitido, igual a gente fez aqui embaixo. Ah, dá um model dump, desempaquota, passa todos os parâmetros, está tudo bem. É uma questão de gosto, de estilo, de código aqui. Massa, e aí, se não caiu nesse erro, a gente pode simplesmente fazer o seguinte. Ah, ad, tipo assim, session.ed, a gente vai adicionar esse DB user que a gente acabou de criar aqui. A gente vai dar um commit, session.commit.

**[00:29:00]** Inseriu isso aqui na base de dados. E aí a gente pode retornar Return the Bay User. Existe uma coisa aqui que acontece, quando a gente vai comitar isso aqui, lembra que a gente tem uns campos no modelo que vão ser definidos lá no banco de dados, que é o createdAt e o id. Ele só vai receber isso depois do commit quando for persistido. Então aí é por isso que a gente...

**[00:29:28]** pode usar o refresh aqui ponto refresh e a gente fala olha atualiza para mim na sessão em relação ao banco de dados o que está acontecendo aqui massa faz sentido isso aqui então a gente adiciona na sessão faz efetiva a transação e aí a transação faz esse essa atualização então traz o banco que está no traz o dado que está no banco de dados para dentro da sessão massa

**[00:30:03]** Posso entender que a sessão é uma conexão estabelecida? Não, a conexão estabelecida com o banco é a engine. A gente falou sobre isso na aula passada, então a engine é a conexão com o banco de dados. A session é a transação, o caminho, a abstração da comunicação entre os dois lados. Aqui que é implementado o repositório, o unit of work e mais algumas coisas. Se ainda não fez sentido, pode mandar a pergunta de novo.

**[00:30:32]** Bom, falaram o que faz. Então, basicamente é isso aqui, né? São muitas linhas, né, pra fazer... pra fazer sem inserção. E tá tudo bem, né? Por enquanto, a gente tá entendendo manualmente, conceito por conceito. Talvez não seja o código mais maravilhoso do mundo, mas... permeia por aqui.

**[00:30:57]** esse rolezinho. E aí, me falem isso. Tá tudo bem, vocês entenderam? Sacaram? Por que que a gente fez toda essa lambança de código aqui? Mas é simples, né? É esse, é esse rolezinho aqui que a gente precisa fazer. Vamos subir isso aqui e ver como é que isso dá lá no Swagger. Vou pegar aqui, vou subir nossa aplicação. Então, poetry run task test, ou se você der o poetry shell, só task test, não, task run.

**[00:31:27]** Beleza, vamos acessar o nosso local host aqui. É 8000 aqui, né? É 8000? O que eu deixei? É 8000. Legal, então a gente vai lá no docs, no swagger. Docs. E aqui a gente tem um post. Então, em teoria, se a gente adicionar esse username aqui, eu vou colocar um username válido, vai, pra gente... Vou colocar aqui.

**[00:32:04]** do no sauro e aí o e-mail vai ser do no sauro arrobaexemple.com. Massa, vamos inserir e ver o que acontece? Legal, ó. Ele deu 201. Retornou, né? Que ele tem um ID1, tal. Isso aqui está funcionando.

**[00:32:20]** Então se a gente for olhar no banco de dados, e aí fica a critério, conecto no SQLite pelo Python, pode ser. Python, menos M, SQLite 3, e a gente chama o nosso database, e a gente pode dar o SELECT aqui para entender o que estava acontecendo lá. O SELECT, asterisco from users, aí ele inseriu aqui, olha até aqui.

**[00:32:44]** um do nosauro, do nosauro ao back sample, o string e a data em que isso foi persistido. Pô, muito massa! Foi inserido, né? O registro no banco de dados. Aí você fala, ah, eu prefiro daquela outra forma estilosa que a gente tava fazendo, né? Com Harley Quinn, né? Rum, Harley Quinn. É, eu esqueci um Harley Quinn. Massa! E aí você pode ver aqui no Select from Users, tal. E aí você tem aqui, olha que bonitinho.

**[00:33:17]** Aí de um, do no sauro, tal, tal, tal. Pô, funciona muito bem. Aí o Reds falou que só não entendeu refresh, né? Algo se falou refresh é pra dar aplicação, é pra dar refresh, pra aplicação da refresh na nossa sessão. Sim, então, a ideia do refresh aqui, vamos lá no código aqui. Eu tô na outra tela aqui. A ideia do refresh aqui é o seguinte, imagina que a gente mandou isso aqui, né? A gente tá com esse user em memória aqui, né? Só que...

**[00:33:53]** esse user que a gente está mexendo aqui, ele não é...

**[00:34:00]** Especificamente, tipo assim, não tem os campos do banco de dados, né? Que são adicionados no banco, né? Como o ID, you created it, tá vendo que eles são init false? Então, aqui é o server default, então quem provê esses dados é o banco de dados. E aí, a hora que a gente dá o refresh, a gente pega esse user que já tá na sessão e atualiza os dados dele com as coisas que estão no banco de dados, ou seja, o ID, you created it, e pra quem fez o exercício, updated it também, né?

**[00:34:28]** Então é isso, e aí a gente traz isso aqui pra cá. Massa. Então é isso, a gente conseguiu inserir essas coisas aqui dentro do banco de dados. Legal. E o que que acontece se a gente for inserir isso de novo? Em teoria, vai ter que dar erro, né? Ou se a gente tentar adicionar o mesmo registro? Aqui é.

**[00:34:50]** Ele deu, ó, username alreadyexist. Ou seja, porque o username já tava aqui. Vou colocar o do no sauro 2. E aí o email continua mesmo. Se a gente rodar de novo. Aqui, ó, email alreadyexist. Massa! Muito simples, né? Tipo assim. O código é bem descritivo quando você entende o que cada coisa tá fazendo aqui dentro, né? Tudo bem, o código está ouripilante aqui dentro? Sim. Mas...

**[00:35:18]** Uma coisa de cada vez, a gente queria ver se o banco funcionava com todas aquelas coisas, todas aquelas idiosincrasias que a gente definiu na aula passada, Session, Engine, Vine, Cree, faz migração, bota no seu que, bota no seu aonde, traz a configuração. Pô, a gente viu, toda aquela config que a gente fez faz sentido aqui, né? Então, é muito massa. Então, tá aqui.

**[00:35:45]** Aí o Muringa falou, se não precisasse das infos como o ID, o created yet nem precisava dar o refresh. Sim. É exatamente isso, mas a gente não retorna, né? Eu acho que eu caí de novo, então me avisem aí se eu voltei. Eu acredito que sim. O internet parece que está pífia hoje, não? Mas tudo bem. Não sei se está funcionando, não sei se eu estou online ou se eu não estou. Voltou, massa, beleza.

**[00:36:42]** Então, a gente tá aqui... Mano, a minha internet tá meio... bichada hoje aqui, mas tudo bem, perdão por isso. Então, a gente tá nesse esquema aqui, que é uma coisa que a gente precisa pensar que é o dry, né? A gente falou sobre isso na aula passada, que é tipo assim, o não se repita, né? Tem um ponto aqui que é muito crítico, que eu deixei aqui, que é o não acople, né? Uma questão de acoplamento que é o que tá rolando aqui, que é o seguinte...

**[00:37:12]** A nossa sessão, ela não pode ser reutilizada, né? Tá vendo que a gente tá com um monte de coisa aqui? Mas se eu precisasse, por exemplo, usar a sessão no outro endpoint, eu teria que fazer isso aqui, né? Eu copio todo esse código... Puta, é modo aplicação de código, né? Tipo assim, aí eu trago pra cá, né? Pro endpoint do get. E a gente tem que fazer isso várias vezes, várias vezes, em todos os endpoints... Pô, não faz muito sentido, né? Isso aqui. Então, eu vou criar uma função...

**[00:37:45]** para a gente não ficar repetindo esse código toda hora. E aí eu vou criar um arquivo dentro do nosso projeto que vai se chamar database.py, database.py. Vamos lá? Então aqui, onde a gente está aqui na passa principal do projeto, eu vou criar um database.py aqui. Massa. E aqui eu vou trazer toda essa camada que a gente tem que ficar repetindo toda hora para cá. Ah, massa. Ó.

**[00:38:15]** Aí eu não preciso do user, eu não preciso do select, mas eu preciso da session aqui. E aí o que eu vou fazer aqui? Eu vou pegar e vou criar uma função chamada getSession. Simplona, simplona. Não precisa de mais aqui. Def getSession. Legal? Simplona. Aí a gente tem essa definição da session que a gente fez, pode fazer com width, width session as session.

**[00:38:51]** A gente dá um yield session. Ou seja, a gente vai entregar isso aqui, a gente pode formar essa função e trazer para cá. Jogá-la do outro lado. Aí fizeram uma pergunta, Caio fez uma pergunta, porque o yield, em vez de return? Porque o yield, ele faz uma condição de parada aqui, né? Então, aonde a gente receber a função get session?

**[00:39:17]** ele vai retornar a sessão e vai esperar. E aí, depois que a gente usar o que precisar usar, ele volta para fechar a sessão aqui. Se eu der um return, ele sai dessa função, né? Ele dá esse dado, mas sai da função. Quando a gente usa a wield, dentro do bloco with...

**[00:39:37]** Essa conexão vai ser mantida aqui, e aí lá onde a gente usar, depois que a gente terminar de usar, aí esse WIFI é executado e aí ele fecha a sessão. Pra gente não ter que ficar dando close na session toda hora. É por isso que a gente usa yield aqui, né? É uma corrotina. Massa? Aí a galera tá pedindo pra eu explicar o yield, mas eu vou fazer o seguinte. Tem uma live de Python inteira sobre yield. Então, se vocês quiserem dar uma olhada depois...

**[00:40:11]** Porque é uma coisa muito grande. Dentro desse sentido, fez sentido, por que que ele tá aqui? Mas se vocês quiserem entender o poder do Yield, eu recomendo que vocês dêem uma olhada, alguém, algum internauta pode me ajudar aí com a falar qual que é a live de Yield. Eu não sei exatamente qual é o número. Só pra gente não, só pra eu não parar tudo aqui, né? Então agora, olha que interessante.

**[00:40:42]** A gente pode trazer isso aqui pra cá e chamar simplesmente Get Session aqui. Olha que massa, então em vez de toda essa gangrenha aqui, a gente vai fazer o seguinte, olha, Session é Get Session. 151, obrigado, Vanderlei. Valeu demais. Essa é uma corrotina do tipo assim que é eu? Não, essa é uma corrotina clássica.

**[00:41:15]** com rotinas com assim que aí eu sou diferente. E aí então a gente importa aqui do database o get session, só que a gente precisa importar as coisas do SQL Alchemy que ficaram aqui. Falta o select aqui. Então vamos lá. From SQL Alchemy import select. Aí a gente tem aqui o select que a gente queria usar.

**[00:41:41]** Só que vai faltar o user, né? Que a gente vai ter que importar lá do nosso modelo. Então, fromFestAPI.models, que é o nome que a gente deu para o arquivo, trazer para cá, né? Então, vamos lá. FromFestAPI0.models import user. Massa! Aí agora, a gente tem o mesmo funcionamento que a gente tinha antes. Olha que bonitinho isso aqui, hein? Não há teus, obrigado por se tornar membro, menino.

**[00:42:13]** Ó, beijão pra você. Valeu demais. Aí agora, ficou mais simples, ficou bonitinho. Tem menos linhas, né? Só tem a linha do que interessa aqui, né? Ok, tá tudo bem. Melhor do que tava antes. Ok, massa. Vamos ver se isso funciona. Provavelmente vai funcionar, né? Vamos ver. Então, eu vou rodar aqui o do Nosaur 2. Internal Server Error. Ele deu um erro aqui, ó.

**[00:42:47]** Generator object has no attribute scholar. Interessante, vou fazer o seguinte aqui. Vamos para aquele caso do return aqui, que a Guine falou, ah, por que que não bota o return? Vamos dar um return e ver o que acontece. Return, vou executar de novo, agora funcionou. Mas beleza, com return funciona, mas com yield não funciona.

**[00:43:16]** Então eu botei esse yield aqui e, estratégicamente, pra gente fazer uma lambança aqui. Peraí. Peraí que a gente tá chegando lá. Porque a gente precisa que ele feche a sessão de novo, né? Mas a gente já vai resolver isso. Ah, obrigado Tiago, mano. Valeu demais pelo Super Chat, mano. Tamo junto. E agora, eu preciso explicar pra vocês uma coisa. Você tá vendo que essa função aqui...

**[00:43:46]** evitou a repetição de código? Ah, você vai falar, ficou mais bonito, tal, não sei o que, evita que a gente repita código. Só que isso encapsula um comportamento dentro do nosso código. Ou seja, como é que eu testo isso aqui? Tipo, como é que eu vou mentir o banco de dados que a gente tinha aqui? Lembra que a gente fez uma fixa, que tinha um banco de dados de teste e tal? Só que eu não posso mudar o comportamento de get session.

**[00:44:20]** Porque pra mudar o comportamento de GetSession, eu tinha que ser capaz de executar essa função de fora. Saca. Funciona, mas tipo assim, não tá muito legal. E aí, tem uma dependência, né? O Endpunty tem que reconhecer essa chamada, né? Aqui dentro e... Saca. Esse é um dos problemas clássicos que a gente tem na engenharia de software, que é tipo assim. A gente coloca um código dentro do outro de uma forma que a gente não consegue mexer nesse código que tá lá dentro.

**[00:44:51]** A gente colocou uma coisa aqui dentro e não vai dar pra tirar, não vai dar pra mexer, pra testar a gente vai ter que usar a sessão de produção e... meio complicado, né? Só que não. O Fast API tem um recurso maravilhoso que se chama Injeção de Dependência. E essa Injeção de Dependência vem num objeto do Fast API que se chama Depends.

**[00:45:20]** Legal, a gente vem aqui no FastAPI e fala o seguinte, olha, a gente está importando, importa para mim o Depends. Massa, a gente tem esse objeto maravilhoso Depends. E aí, qual que é a pira desse Depends? O Depends é uma forma de falar, olha, para executar o meu código, eu preciso que um outro código seja executado antes. E o resultado que esse código deu, eu quero que você me passe via parâmetro. Parece loucura, né?

**[00:45:53]** Parece loucura. Então o que a gente vai falar? A gente quer dizer para o nosso código aqui que a sessão não faz parte do código que a gente está usando aqui. A sessão é um requisito para a gente executar esse código. Ou seja, a gente precisa desse dado aqui. Ou seja, a nossa execução de código depende de outra coisa.

**[00:46:21]** E aí, para a gente não fazer esse acoplamento aqui, a gente injeta a dependência. Injetar a dependência quer dizer que a gente está falando para o framework e circuita esse código aí antes. Toda vez que você for executar essa função, você circuita esse código antes e me dá o resultado dele. E aí é para isso que serve essa função de injeção de dependência. Ou seja, a gente desacopla o código e passa só o resultado dele como parâmetro. Faz sentido isso que eu estou falando?

**[00:46:49]** Deve estar muito abstrato ainda, às vezes. Mas olha como é que usa isso aqui. Olha como isso é sensacional. É muito legal. Então, em vez de chamar essa sessão aqui, eu falo o seguinte aqui. Eu vou quebrar a linha por questão de praticidade aqui, mas eu vou falar, olha, Session. O meu objeto Session é um Depends disso aqui. Pronto.

**[00:47:39]** Agora, toda vez que eu executar esse código, ele vai me retornar a isso aqui. Ou seja, antes de entrar no escopo da função, ele vai lá no database, executa esse bloco de código, traz esse valor do yield que está aqui, executa toda a nossa função e, no final, ele fecha a sessão sozinho. Olha que lindo, mano, isso aqui. Aí, o Van der Ley perguntou, mas, por exemplo, não poderia ser passado só o session get session com um parâmetro igual o user? Ah, não.

**[00:48:13]** Tipo assim, a forma como funciona aqui, tipo assim, se você fizer só assim, get session, você tá acoplando. Porque isso aqui é estático no Python, né? Então, quando você executar a primeira vez, ele vai acoplar o resultado aqui. E não é isso que a gente quer. A gente quer que sempre seja reexecutado a sessão. Podemos depender de vários? Sim. Aí o Victor perguntou mais, como ele injeta? Não, a gente tá passando igual, depende. É só isso aqui.

**[00:48:46]** Sério, lindo, maravilhoso. Vamos rodar e ver o que acontece? Vou executar de novo. E aí, e-mail oradexis. Vou registrar o regis aqui. Regis, arroba, example, ponto com. Legal, funciona. Registrei o regis. Regis tem um ID 2. Executa de novo username oradexis. Massa, lindo. Ou seja, toda vez, antes de entrar nessa função, ele pegou...

**[00:49:15]** o resultado do getSession e passou para o session. Ó, maravilhoso. É lindinho. Não precisa de nada mais do que isso. É simplesmente, falou, getSession passa a coisa que você queria aqui. Ele pega o resultado ou o yield disso aqui, executa, depois ele volta e termina o contexto do que tinha ali. Ou seja, ele faz a operação, me dá o valor que eu preciso, eu faço tudo o que eu preciso, depois ele vai lá e termina a session.

**[00:49:48]** De forma graciosa, né Graceful. Close it. Ezra, obrigado por se tornar membro, ó. Beijo. Valeu. Demais. Legal. Fez sentido isso aqui? Ficou mais limpo ainda, né? Embora a gente tenha, tem muita quebrada de linha aqui, né? Que eu tô fazendo pro código ficar do tamanho que todo mundo consiga ler aqui. Mas é simplesmente isso. Não é muito complicado. A gente simplesmente falou. Me dá o resultado. É lindo.

**[00:50:19]** É lindo, maravilhoso. Simplão, né? Python é bonito. Essas magias, idiosincrasias do Python são maravilhosas. Então a gente pode fazer isso aqui. Só que agora... Não, agora? Para quem já estava falando, caraca, isso é demais. Se liga no que vai acontecer agora. Agora vai acontecer a coisa mágica. Lembra?

**[00:50:49]** que a gente, pra escrever os testes, tinha umas coisinhas lá, então eu vou começar a fechar as coisas que a gente abriu aqui. Vou deixar o app e vou voltar lá no nosso Conf test. Lembra que a gente tinha criado esse teste client aqui? Então, toda vez que eu uso Depends, eu posso falar pro Framework, na hora que ele tá criando o cliente de teste, fala, olha, sabe aquela função get session que você depende lá, que tá com os dados de produção amarrados?

**[00:51:21]** Então, na hora do teste, injeta outra coisa aí. Troca a função GetSession por outra coisa. É lindo, é lindo. Aí você pode falar, olha. Teste client. Pega a dependência que a gente tem lá e sobre escreve ela. Qual dependência que é? É GetSession. E bota o quê? O que eu quiser aí dentro.

**[00:51:45]** Ou seja, aquela sessão que a gente criou do banco de dados maluca em memória, a gente simplesmente faz esse shift aqui na hora de fazer o teste. E aí a gente pegou a dependência que a gente tinha troca por outra durante a execução do teste. Faz sentido isso? É muito maluco, né? Eu sei, eu sei que é muito doido. Vamos, vamos lá, vamos lá, vamos lá. Então em vez de retornar a isso aqui, a gente vai fazer o seguinte.

**[00:52:17]** Client, aí eu vou falar o seguinte, client.dependenceoverride, dependence, é dependence mesmo. E aqui eu dei o nome de client, beleza? Só para eu saber se eu estou com o nome certo aqui, app.dependenceoverride, é bruxaria isso aqui, né? Então eu vou falar, o que que eu quero trocar aqui? Eu quero trocar aquela função que a gente tem lá que é o...

**[00:52:49]** GetSession, massa, então vamos lá. FromFestAPI0.database import GetSession. E aí eu vou falar o seguinte, olha. Quando você for chamar GetSession, chama outra coisa para mim. Que outra coisa? A nossa session roubada que a gente tem aqui que testa em memória. Então eu vou fazer o seguinte aqui. Def, sei lá, como é que eu chamei aqui?

**[00:53:23]** GetSessionOverride, ou seja, sobrescreve o GetSession. E aí, a nossa fixture traz a outra fixture para dentro do contexto. Session. Return Session. E a gente vai passar isso aqui. Precisa ser uma função. GetSessionOverride. Aí, agora, eu posso fazer o seguinte. Yield. Porque lembra? Yield vai desfazer isso aqui sempre e depois, né?

**[00:53:58]** O wield aqui é um componente central aqui dentro dessa coisa. Então retorna o client e depois que acabar, ou seja, aqui eu... eu arrange, né, do teste. Aí ele retorna isso aqui pra gente poder operar. Depois que acabar o teste, desfaz essa gangrena que a gente fez aqui. Então app.dependenceoverrides.clear. Limpa as dependências. Aí agora...

**[00:54:29]** a nossa sessão quando a gente for fazer a requisição no banco de dados de produção a gente mentiu e a gente trocou essa session por essa session fez sentido eu sei que aqui a gente deu um salto muito grande de lógica aqui e aí se alguém tiver perguntas por favor mas é basicamente isso então

**[00:55:00]** A injeção de dependência permite com que a gente faça esse tipo de coisa aqui sobre escrevas dependências durante o teste. Então a gente força todos os testes que usam client a usarem a sessão do banco de dados de mentira que é resetado a cada teste. E aí a injeção também é resetada a cada teste. Pô, bonito, né? Bonito, bonito. Eu acho bonito, pelo menos.

**[00:55:33]** Então, vamos lá no nosso teste e ver o que acontece, né? O nosso teste de create user, porque foi o único endpoint que a gente implementou o banco de dados, né? Então, vamos lá no teste app. A gente tem esse create user, que é isso aqui, né? Ele vai retornar created no Alice, tal, tal, tal, tal, tal, tal. Vamos rodar isso aqui e ver o que que rola. A gente tem que rodar os testes, então vamos lá. Poetry RAM task test.

**[00:56:05]** Aí ele deu vários problemas de import, de linhas em branco, então eu vou dar um format, pra gente não se preocupar com isso agora, e eu vou dar o teste. Quebrou. Ele falou que deu um erro, um TraceBack, tal, tal, tal. E aí o erro que ele deu foi esse aqui, foi um erro do SQLite. Ele falou SQLite Objects Created in a Thread can only be used in the same thread. Ou seja...

**[00:56:37]** O objeto que é criado em uma thread só pode ser usado na mesma thread, ou seja, o conf-test aqui está rodando em uma thread. O fastchipi faz isso quando ele sobe o cliente. E aí o cliente de testes roda em outra thread, ou seja, é uma comunicação entre threads. E como a gente criou o banco de dados na thread de testes, quando a gente vai usar na thread de aplicativos, ele quebra. E é mais ou menos isso que o erro está dizendo aqui.

**[00:57:06]** Ou seja, foi criado numa thread, mas tá sendo usado em outra. Então, a gente tem um erro aqui e a gente vai fazer uma pequena engenharia aqui na Engine pra falar que a gente pode fazer isso aqui. Falar, ó, não tem problema. Nesse caso, tá tudo bem pra mim.

**[00:57:25]** A gente vai arrumar isso aqui. Então, com isso, não precisamos nunca de um banco de dev ou de kea. Não, claro que precisa. Testes de kea e testes de desenvolvimento são diferentes de testes unitários, que é o que a gente está fazendo aqui, né? Testes de unidades, né? A gente quer saber se o código funciona, mas em produção, sei lá, no stage, são outros testes, né? São outros níveis de teste.

**[00:57:47]** Então, o que eu tenho que fazer aqui? Eu tenho que falar só pro SQL Alchemy. A hora que ele for subir esse banco, não me interessa muito a thread, tá tudo bem? Massa, então ele tem esse connect args aqui, que ele fala, olha, checa se tá na mesma thread? Não, não faz isso, não precisa. A minha aplicação é resiliente a isso, porque a gente não tá rodando múltiplos processos e tudo mais. É só aqui. Massa, vamos rodar agora e ver o que acontece. Legal. Ele deu erro.

**[00:58:20]** Ele falou, no search table users, ou seja, não existe a tabela de usuários aqui aonde a gente tá criando. Mas você tá vendo que ele tá criando aqui, né? Então é esse ponto aqui, a gente precisa falar que o pull disso aqui é estático aqui dentro.

**[00:58:44]** É que ficou errado o slide, né? Mas tudo bem, isso aqui é um tab para trás, para quem for olhar o slide depois. Aí a gente só precisa falar para ele, olha, quando você for criar várias conexões e tal, porque ele está tentando pegar uma conexão com uma thread, outra conexão e outra, aí você fala, usa o mesmo pool, ou seja, usa a mesma conexão para as duas threads, porque agora ele não está checando se as threads são...

**[00:59:08]** diferentes de fato. Mas aí pra fazer isso aqui a gente tem que vir aqui e falar pro SQL Alchemy pra gente importar o static pull do SQL Alchemy pull. Então vamos lá. Então from sqlalchemy.pull import static pull. É só uma engenhariazinha aqui pra gente poder executar esse teste aqui. Ou seja, usa

**[00:59:33]** Um pul estático, não checa se está em três diferentes. A gente está usando em memória uma coisa super simples para rodar os testes. Vamos ver o que que rola agora? Funcionou! Olha que legal! Então o nosso primeiro teste passou. Test create users. Passed. Lindo! Ah! Fala aí, fala aí, fala aí. A gente deu uma volta, né?

**[01:00:01]** no universo inteiro pra chegar aqui. Mas você viu que a gente chegou. A gente deu uma volta grande aqui, né? Pra configurar um ambiente de teste, pra fazer as fixtures se encaixarem, sabe tudo fica certinho no lugar, mas funciona. E aí o nosso teste passou. E aí ele falhou no segundo teste. Ele falou, olha, a hora que eu tô dando o... o... read users, o read users falha.

**[01:00:30]** Lembra daquela conversa que a gente estava tendo há duas aulas atrás? Que a gente falou, ó, a forma como a gente está fazendo o teste é ruim, porque os testes não são isolados, né? Eles são interdependentes. Ou seja, para o read users funcionar, o create user tinha que inserir a parada e uma coisa estava dependendo da outra. Só que agora, como a gente está usando o banco de dados, a gente vai fazer isso aqui, né? A gente cria tudo, limpa tudo. Acho que voltou já, né?

**[01:01:09]** Tô caindo toda hora aqui. Mas esse teste em específico, ele tá falhando porque a gente não implementou o banco de dados nele ainda. Só me falem se eu tô online, né mano? Tipo assim, porra, a conexão hoje tá deixando ele já. Travou e voltou a massa, então beleza, então já estamos de volta. Então a gente precisa implementar o banco de dados no read-users, né? Então, vamos lá. Como é que a gente vai fazer isso aqui? Simplesmente, a gente vai usar o Depends...

**[01:01:41]** que a gente já tinha ali, o Depends que a gente colocou aqui, e vai trazer ele para dentro do Endpoint de Get. Então, agora a gente está no Get Users, Read Users, e a gente vai trazer aquelas coisas para cá. Ou seja, Depends, a gente vai trazer o Depends para cá. Então, a gente quer o Session, a gente precisa do Session para se comunicar com o Database, então a gente vai chamar o Depends de Get Session.

**[01:02:18]** Sim, prão. Algumas pessoas gostam de codar baseado em autocomplete. Saca. Tipo assim, ah, eu queria que esse session me mostrasse os argumentos que estão aqui, porque é só uma variável e tal. Existe uma anotação aqui dentro do Fast API que você pode fazer o seguinte. Isso aqui é do tipo Session. Massa. Então, se você importar lá do SQL que é o meu RM Session.

**[01:02:49]** Aí você ganha os autocompletes aqui, né? Você pode falar isso aqui. Então, se acha um ponto escala, por exemplo, tá vendo? Aí ele autocompleta se você tiver o LSP funcionando. Então, você pode usar essa definição aqui também. É uma outra forma de fazer isso. Não muda nada na prática, mas no desenvolvimento dá uma ajudada, né? Então, você pode usar assim. Você pode estar explicando qual é o tipo da coisa que veio via notação de tipo. Sabe? Na prática.

**[01:03:18]** Não vai mudar nada, mas na hora de codar fica mais simplão, né? Você pode falar session.refresh, sabe? Esse tipo de coisa. Você poderia fazer isso aqui se você quiser. Eu coloquei isso nesse código só para mostrar que daria para fazer isso aqui. Então o que a gente quer aqui? Se a gente quer retornar a todos os users do Database, basicamente o que a gente quer...

**[01:03:44]** É pedir todo mundo, né? Então a gente vai fazer um select de users, todos os users. Então Session.scholars no plural. A gente vai usar a função de selection, então busca todos os users na base de dados. Massa! Aí eu posso chamar isso aqui de users, por exemplo. Users. Simplom. Tá implementado o get. Olha que massa. Funciona bem. Ó o Pedro. Pra ajudar a pagar a internet. Obrigado, mano.

**[01:04:27]** eu vou ter que ligar lá e é uma das coisas que vocês sabem que é ótimo de fazer ligar na operadora então a partir de agora todos os nossos get em teoria que a gente fizer lá na pi eles têm que retornar os idis que a gente já inseriu simplão assim rapidão bala vamos dar o get aqui execute ó que massa olha id 1 regis id 2 então se a gente for inserindo mais pessoas aqui

**[01:04:58]** eu vou inserir aqui o xinodinho que é a última pessoa que comentou aqui xinodinho, massa, execute colocamos ele aqui, ele é o id3 execute pô, tá aqui massa, lindo, maravilhoso, simples, né? você tá vendo aqueles esquemas que a gente fez na aula passada? eles são muito massa porque eles já só que aqui tem uma outra coisa que eu queria falar com vocês que é o seguinte

**[01:05:42]** retornar todos os users nem sempre é uma boa ideia porque imagina o seguinte fala novamente beleza vamos lá a gente fez esse esquema a gente trouxe todos os users testamos eles vimos que eles são retornados a grande coisa que a gente precisa fazer agora é o seguinte é uma boa prática não retornar todos os users de uma vez porque imagina o seguinte

**[01:06:20]** Você vai fazer uma chamada aqui na aplicação e, sei lá, ela vai ter, sei lá, 200 mil registros. Tô dando uma solução hipotética aqui. E a gente não quer que isso aconteça. A gente quer paginar as coisas, né? Então, sei lá, a gente quer vir de 10 em 10, de 20 em 20, de 30 em 30, pra gente ter uma relação saudável com o banco de dados, né? Então, a gente pode fazer isso via Queer String, né?

**[01:06:47]** Lembra aquele ponto de interrogação que a gente viu lá na aula de HTTP? Então pra fazer isso aqui, a gente define o parâmetro aqui, eu vou falar que a gente quer um, sei lá, limit, a gente quer, sei lá, limitar em 10, por exemplo. E a gente vai fazer um offset de 10 também. Vou colocar assim, limit offset.

**[01:07:16]** Ou seja, eu quero passar, na hora que eu fui chamar esse endpoint, eu quero falar, olha, começa no zero e me traz do zero até o 10. E aí depois, na próxima, a gente passa o offset 1, o limite 10. Aí a gente paginou, né? Então a gente viu do zero, do 1 ao 10, depois do 11 ao 20, e assim a gente vai fazendo esse tipo de interação. E aí, só por a gente colocar esses parâmetros aqui, da forma como eles estão, como inteiros, você poderia falar, né? Isso aqui é um int.

**[01:07:48]** Isso aqui é um int, saca? Ficar explícito. Isso aqui vai ser refletido na documentação e também na hora da gente fazer a query string aqui. Deixa eu dar um f5 aqui. Deixa eu dar um get aqui no users. Olha o que que acontece. Então a gente pode fazer, eu quero limitar de um em um dentro da nossa API. A gente vai chamar, ele retornou todos, porque a gente não implementou isso na query ainda. Mas olha que interessante, agora ele implementa aqueles...

**[01:08:18]** ponto de interrogação que a gente estava vendo. Limita por um e off seta, né? Então anda de zero, sei lá, de zero até o limite que a gente queria. Então a gente vai trazendo, traçando essas combinações de parâmetros aqui, de query parâmetros. Massa? E aí, como é que a gente adiciona isso aqui? É simplesmente falar, ó, limit, limit, offset, offset.

**[01:08:50]** Tá legal, tô na frente, mas é isso aqui. Aí a gente fecha os parênteses aqui. É simplão assim mesmo. Então, seleciona user, limita a busca pelo número que vier de limite ali em cima e faz um offset. Ou seja, a paginação de tantos em tantos. Bom, sério, é um simplão assim. Bonito, né? Mas que ele é muito... Sabe? Ele diz tudo o que precisa ser dito, né? Isso é muito massa. Vamos executar de novo agora?

**[01:09:21]** Ó, ele trouxe o ID 1. Deixa eu limitar por 2, vai? Aí ele trouxe o Eduardo e o Regis. Na próxima, ele tem que trazer os próximos 2, mas só tem 1, então vai trazer o chinodinho aqui, ó. Offset. Ah não, ele trouxe, né? Offset vai trazer aqui, né? Então ele trouxe o Regis e o chinodinho. Então, ah, eu quero isso aí lá. Do 2 pra frente, me traz 2. Aí ele só tem esse aqui. Ah, do 3 pra frente.

**[01:09:51]** Aí não vai ter ninguém, né? Então ele vai dar users zero. Então a gente pode ir intercalando quantos a gente quer que mostre e a partir de qual posição a gente quer tratar isso aqui. Mas só fez sentido isso. Simplão também de resolver isso aqui. Deu para sacar? Dá todo mundo tão quietinho hoje. Às vezes eu acho que eu caí, não tenho certeza se eu voltei. Então legal. Vamos rodar os testes aqui agora para ver o que acontece. Vou rodar os testes.

**[01:10:36]** E aí, agora, como a gente está mexendo no Create User, no Read Users, o Read Users falhou, né? Porque não veio nada, né? Lembra que um teste não interfere no outro? Ou seja, então, como não tem ninguém inserido aqui? E como é que a gente vai rever isso aqui, né? Então, eu vou mudar esse teste que a gente tem aqui e vou fazer o seguinte. Eu vou fazer o nosso Read Users.

**[01:11:16]** Lendo nada. Porque, em teoria, a gente não tem nada nesse teste. O certo é que ele venha vazio, né? Read users, porque não tem nenhum user na nossa base de dados. Porque ele limpo o banco todas as vezes, né? Ele não depende um do outro. Vamos rodar agora e ver o que acontece? Legal. Ó, ele passou no teste Read users. A gente leu o user vazio.

**[01:11:52]** Massa! Funcionou! Por quê? Porque lembra? Ele dropa toda vez o banco de dados, ou seja, quando a gente está nesse lugar, ele não tem ninguém. Mas aí a gente precisa fazer um teste com alguém, né? É, o Rodrigo perguntou uma coisa interessante. Ele falou, paginação sempre tem que ser feita do lado da peina ou do lado do consumidor, certo? Sim, não, depende. Aí é regra de negócio.

**[01:12:17]** Aí é prática de negócio. Aí falou, tem alguma prática de trazer o total de registro que nem algumas APIs trazem? Então, essa é a aplicação de hate-oas, né, do que a galera fala, que é o API nível 3, tal? Tem algumas práticas a esse respeito. A gente não vai ver isso, mas dá pra fazer. Então, a gente implementou, testou aqui, né? A gente tem um get que não vem ninguém. Nossa, funciona, mas e se tiver alguém?

**[01:12:47]** O esquema está funcionando, as respostas funcionam da forma que precisam. Só que você está vendo que o get ele é um teste que precisa de alguém para a gente ver se tem alguém na base. Só que o put também depende de alguém estar na base, o delete também depende de alguém estar na base. Aquele get que vocês implementaram algumas aulas atrás que precisa de um, sabe, get by id, pega por id, também vai precisar de um user. Então a gente vai criar uma fixture nova. E nessa fixture nova

**[01:13:19]** A gente vai fazer o quê? Simples. Inserir um user. Ah, tá de brincadeira, sim. Pô, se vários testes precisam que o usuário esteja presente, por que não criar uma fixture pra ele? Arroba, pie-test, ponto-fixure, def-user. Lindo. Então a gente depende da session aqui também. Então a gente vai fazer o seguinte, session.ed user.

**[01:13:54]** Eu tinha deixado como user mesmo, tá, beleza. Só pra não confundir. Session.comit. Beleza. Return. User. Massa. Então eu só preciso definir um user aqui. Aí a gente vai ter que importar ele lá da onde a gente tinha, né? Lá do database, aqui do Models. A gente tem aquele modelo chamado User. Vou trazer ele pra cá. E eu vou inserir um user dummy aqui, né? Um user de teste. Ele tem o username. Ele tem um e-mail.

**[01:14:27]** e ele tem uma senha, password. E aí, eu vou seguir os mesmos dados que eu deixei aqui só para eu não diferenciar depois. Então, a gente vai inserir ele assim. Então, a gente tem um username que chama teste, um e-mail que chama teste, arrobatest.com, e um password teste teste. Massa, a gente pode dar um refresh aqui, para garantir que a gente vai ter o ID.

**[01:15:03]** Maça, se você quiser, daquele auto-complice, você também pode usar aqui no session. Mas você tem no session.edital. Legal. Lindo. Aí, a partir daqui, agora, a gente só usar a fixture que a gente tinha lá atrás, no teste que a gente tinha. Então, por exemplo, getUser. Se a gente passar a fixture user, a gente vai ver que o teste vai parar de passar. Porque agora a gente tem um user na base. Vamos ver o que acontece?

**[01:15:34]** Aí ó, legal. O teste do read user falhou, porque agora tem um registro aqui, né? Ah, massa! Então essa é uma forma de garantir que sempre vai ter um user aqui dentro. Só que eu quero testar se a resposta dá certo com e sem, né? Então eu vou criar um outro teste pra isso aqui. Um teste bem parecido com esse, que vai ser o read users with users. Mais simplão, né?

**[01:16:06]** Vai, read users with user. E a gente traz o user pra cá. Simplão. Aí o que a gente quer validar? Se o user que a gente inseriu vai voltar na resposta. Então a gente vale dos dois casos, né? O caso de não ter nada e o caso de ter alguém dentro da nossa API aqui. Mas só que aí tem uma coisa aqui que eu quero contar pra vocês que é uma parada interessante. Lembra que eu pra inserir esse user aqui...

**[01:16:35]** Eu preciso que ele seja para validar um esquema, né? Porque esse user aqui, ele é um user do Paidente, é um user do SQL Alchemy, né? Então eu não posso validar se esse user veio aqui.

**[01:16:51]** Eu preciso transformar isso aqui no modelo de resposta do pai idêntico, ou seja, é um JSON que tem só os campos específicos, né? E é o que a gente quer o user public, que é o que vai cair aqui, né? Então a gente pode importar ele lá em cima e falar o seguinte, eu vou importar aqui mesmo, só pra gente ir vendo. Então beleza, eu preciso falar do fromFestAPI0. Aí eu vou chamar quem? Os meus esquemas.

**[01:17:18]** importar o user public. E aí eu vou falar o seguinte, olha, pega esse user public que a gente tem aqui e valida o modelo dele. Olha que massa, então model validate de user. Ou seja, o que ele vai fazer? Ele vai transformar isso aqui no user, do pá idêntic, no user de esquema. O que veio do banco de dados vai virar um esquema aqui.

**[01:17:47]** Então, essa é a forma de fazer o inverso, né? Então, eu vou ter um usuário do SQL Alchemy e eu vou transformar esse usuário em um esquema, né, do PyDentic. É basicamente isso que a gente quer. E é que eu dei o nome de user-esquema. E aí, como a resposta que a gente quer é um JSON, né, um JSON, a gente pode dar o dump. Model dump. Aí, isso aqui vira um dict do Python, né? Então, aí a gente pode fazer a validação.

**[01:18:19]** Disso aqui. User schema. Ou seja, a gente converteu o user do banco de dados, que veio aqui da fixture, em um user public. Fez sentido isso, ok? Como que a gente fez essa transformação? Aí eu preciso importar ele aqui. Deixa eu dar um format aqui, vai. Então, sim, senhor. Vamos rodar então para ver? Task test. Ah, 40 RAM. Task test.

**[01:19:08]** Deu erro. Ah, maldição. Por que que deu erro, né? Ele falou o seguinte. Então, eu tenho que falar, para o modelo do Paedentic, como é que eu faço essa configuração? Olha que massa. Então, eu posso falar pra ele, olha, a configuração, como é que você vai pegar o int, o username,

**[01:19:39]** E a string do email vai ser via atributos, ou seja, ponto username, ponto email, ponto ID. É basicamente isso que eu falo pra ele, então a gente vai chegar lá no nosso modelo, então vamos lá. Nosso modelo no nosso esquema e aí a gente vai importar o config dict. E aí aqui no user public eu vou falar, olha, esse modelo é legal e tal, mas eu quero que você leia dos atributos.

**[01:20:14]** from attributes, true. E aí eu preciso falar, essa é uma chave padrão do... do... do identity que é o model config. Fig. Assim. E aí eu simplesmente falo pra ele aqui ó, model config, quando você receber os dados, eu quero que você pegue os dados via atributos, ou seja, username.id, username.email.

**[01:20:45]** dessa forma aqui. Aí agora ele consegue fazer a conversão. Porque não é um JSON que veio. É um objeto que a gente conhece. Legal, passou. Lindo, maravilhoso. Olha que incrível. Então ele leu 100 usuários e leu com o usuário. A gente conseguiu fazer essa conversão de um modelo e outro aqui. Ah, fala. É bonitinho, é bonitinho, né?

**[01:21:16]** As fixtures são muito poderosas, né mano? Você vai passando uma coisa para cá, uma coisa para lá e aí quando você vê... Aconteceu muita coisa aqui, né velho? É o banco que se limpa sozinho, que injeta o cliente, que troca dependência, que cria o user, que converte para o modelo do pai idêntico. Eu sei, é tipo... Fala, nossa, vou ter que assistir de novo muita informaçãozinha pequena, sim, mas é interessante de ver isso aqui. Mas é bonito, olha o teste, é muito pequeno, muito sucindo, sabe? Simples.

**[01:21:50]** de ler. Ele está usando DTO na veia nessa agenda. Aí agora falta o update. A gente não implementou o update ainda. E são essas coisas que a gente vai precisar.

**[01:22:14]** Favor, o que é DTO? É Data Transfer Object. É um objeto que passa de um lado para o outro. Tipo essa validação do pai dêndic. É um objeto, a gente encapsula ele numa outra coisa que faz essa área de transferência. É DTO, é um padrão de projeto. Architectural Patterns, Enterprise Architectural Patterns, esses nomes bizarros. Então vou voltar lá no app com vocês agora. Então lembra que a gente tem todo esse esquema aqui do...

**[01:22:44]** Update. Ó, eu fiz uma pergunta aqui que é o seguinte. Do config faz isso para todos os tipos de dados ou só para atributos primitivos? Para todos os tipos de dados que você precisar, ele vai fazer isso aqui. Você só precisa anotar certo dos dois lados. Mas ele funciona. Pô, legal, então a gente vai precisar do put, né? Eu vou começar com uma coisa aqui que é o erro, né? Então, eu vou fazer os dois juntos aqui agora, porque eu tô vida louca aqui.

**[01:23:13]** A gente já entendeu o que precisa fazer, é de novo, é aquela implementação, da implementação, é sempre a mesma coisa aqui, né? Então o que eu preciso saber aqui, né? Então para a gente alterar um usuário, o que a gente precisa fazer aqui, né? Então eu preciso ver se o user existe aqui dentro, né? Então a gente vai trazer a session para cá, né? Porque a gente está usando o banco de dados lindamente aqui, né? Não precisa de todos esses quebra-linhas aqui que eu costumo usar, mas é só para...

**[01:23:45]** Todo mundo conseguiu ver. Legal, então eu tenho uma sessão e eu preciso fazer o seguinte, eu preciso saber se existe o user DB aqui dentro. Então, legal, temos a Session, Session.scalar. Eu preciso saber se o user existe aqui, né? Então, eu quero o Scalar do Select, porque eu vou buscar pelo user. E quem é o user que eu vou buscar? Qual tabela eu vou buscar? Na tabela de User. Onde? O quê? Where? O?

**[01:24:22]** id que a gente quer aqui, que é o user id que a gente está passando via query string. Então eu preciso saber, se o user.id é igual a o quê? User id. Travei hard aqui agora. Legal, essa é a validação que a gente precisa fazer. Então, se não encontrar isso aqui, é aquele caso. Se voltar none, if not, user db,

**[01:24:56]** Então significa que o user não existe, né? Não tem esse valor que a gente quer aqui dentro, né? Então se ele não existe, a gente vai ter que dar um rise para quê? HTTP exception. E aí o status code que a gente vai ter que retornar é 404, né? Porque a gente está mandando, ele alterar um user ID que não existe. Então, not found. HTTP status.notfound Legal, né? Simplão.

**[01:25:31]** E aí o que eu coloquei aqui? Detail UserNotFound. Legal. Fui bem explícito aqui. Achei que eu tinha sido mais subjetivo aqui. Então a gente tem o UserNotFound. E a mesma coisa vale para o delete, né? Tipo assim, lembra? A gente tinha duplicado essa validação nos dois, né? Você pode fazer uma função para tirar isso daqui? Pode, mas... Eu...

**[01:25:56]** Eu ainda não quero refatorar o projeto. A gente pode refatorar ele em algum momento, mas a gente vai refatorar ele em algum momento, no normal lá pra frente, mas até então tá tudo bem pra gente. Então é isso que a gente precisa. Se não existir, ou seja, não tem esse registro, vai retornar 404. E aí tem o caso do registro existir, né? Então, se existir...

**[01:26:21]** a gente vai fazer aquela troca toda, então o username recebe username, lembra que no put a gente recebe todos os dados, o id tem que continuar sendo mesmo, então a gente vai fazer o seguinte, se não existir, dá esse exception, mas se existir, a gente vai fazer o seguinte, userDB ponto email vai receber user do que veio do esquema aqui, ponto email

**[01:26:54]** e a gente vai fazer isso para todos os campos username, username, porque é uma característica do pute, se fosse patch tem uma outra forma, a gente vai fazer em outro momento, mas por enquanto a gente está no pute e password, então a gente vai receber todos os valores aqui username, user, password, a gente faz o quê? a gente alterou os dados, então a gente adiciona isso aqui na session, então session.ed userDB a gente vai comitar isso aqui, comite

**[01:27:29]** A gente pode dar um refresh ou não, se você quiser. Então session.refresh.userDB. E aí a gente retorna um user, return user. Massa! Esse é o pute. Foi mais simples do que parecia, né? Lembrando, de novo, dá pra fazer aquele esquema de alterar tudo de uma vez com asterisco e modelDunk, mas pode ser mais simples, tá ligado?

**[01:28:02]** E aí beleza, é isso! Então se não tiver o user ele vai retornar a 404, se tiver ele vai alterar o user no banco de dados. Olha que massa!

**[01:28:15]** Aí o Lucas fez uma pergunta aqui. Alterou tudo para a mesma coisa? Não. A gente está pegando o usuário que veio do banco e está passando e-mail, tal, tal, tal. A gente está pegando tudo e esse user aqui é o que veio da requisição do user schema. Ou seja, a gente está pegando todos os dados que a gente tem e está trocando todos pelos que vieram no request de alteração. Ok, o userDB vai receber user.

**[01:28:44]** em todas as comparações. Fez sentido? É o userDB, que é o que está no banco, está recebendo as alterações do que veio no request. Não está alterando para a mesma coisa. Então, se eu mudar o e-mail na requisição, ele vai alterar o e-mail aqui. Se eu alterar o username, o password, e assim vai, por diante. Massa, fez sentido? E aí, vamos rodar o teste agora? Se... Beleza.

**[01:29:22]** Erros de import, tudo mais. Mas olha que interessante, ele deu um erro. Interessante aqui. Ele falou o seguinte, olha. Festa IPI0 e Esquimas e UserDB foi importado, mas nunca foi usado. Tá vendo isso aqui? É importante essa mensagem, por quê? Porque a gente criou o UserDB só pra gente simular o banco de dados, lembra?

**[01:29:50]** Então, ele não precisa existir mais. A gente pode ir lá nos esquemas e deletar ele. A gente criou ele só, só para a moda a gente brincar aqui naquela coisa passada. Do mesmo jeito, aqui a gente tem aquele database falso que a gente tinha criado aqui, que não precisa mais existir também, porque a gente não está usando mais o database falso.

**[01:30:14]** Legal, vamos rodar de novo agora? O teste, vê o que acontece? Olha, ele falou Session, Scalar, tal, tal, tal Undefined Name Session, na linha 81, é porque aqui embaixo eu comecei a alterar o delete, mas não implementei tudo, né? Então eu vou trazer o Session para cá, só para a gente ter as coisas aqui. Então legal, teste, tem que passar o update. Update, o user falhou.

**[01:30:53]** Por que que falhou? Porque ele está tentando alterar, lembra que a gente fez isso aqui no contexto onde um teste dependia do outro. Então ele está tentando alterar um user que não existe. Massa, como é que a gente faz um user existir no teste? Simples. User. Massa. Legal. Deu failad. Por que que deu failad? De novo. A hora que ele foi tentar fazer a coisa, vamos ver, seria lines e tal, tal, tal, deu um errão muito louco.

**[01:31:32]** Aí ele falou o seguinte, olha, Missing Lock Response ID. Não deu ID aqui. Hmm, que estranho. O que que está acontecendo? Ele está passando user, aí ele está passando Bob, tal, tal, tal, Secret. Mas na hora de responder a mensagem, Response ID, Field. Ou seja, a gente está passando o user-esquema com username Bob e mail-example e password Secret.

**[01:32:06]** O que que tá errado aqui? É no app, né? Mas a gente tá no teste certo? Só pra validar isso aqui. Tá. Tá no teste de update. Só pra ver se a gente não caiu no delete e tá lendo o erro do delete. Então ele deu erro aqui, porque a gente tá retornando o user. Tá vendo? Olha que cagadinha que eu fiz aqui. A gente precisava retornar o user DB.

**[01:32:29]** É o do banco de dados e não o user daqui. O Rodrigo comentou junto comigo aqui. Massa, vamos rodar de novo aqui e ver o que acontece? Legal. Passou o update. Ficou faltando o delete. Porque no delete a gente caiu nesse caso de tipo assim, a gente tá tentando deletar alguém, mas a gente ainda não implementou o código que deleta, né? A gente só fez o 404. Então...

**[01:32:56]** Vamos implementar o endpoint de delete. E para o endpoint de delete é simplão, né? Você pode falar, delete userDB. Simples, esse aqui é o mais lindo de todos, né? Beleza, passou daqui, o user existe. UserDB, então a gente vai chamar Session. Esse é o mais simplão de tudo, Session.delete. UserDB. Session.comit. Acabou. Deletou o user. A gente precisa dar o return aqui. E é o return que a gente retorna aqui.

**[01:33:30]** A gente está usando o user public aqui, para retornar. A gente pode usar o message, porque a gente não está retornando nada, não está retornando ninguém. Então, por que eu vou retornar o ID de alguém que não existe no banco? Eu vou retornar message. E qual que é a mensagem? User deleted. Simplão. Simplão. Ficou bonito. Se você quisesse usar o objeto aqui também funcionaria, você pode fazer isso aqui. Message.

**[01:34:04]** a mensagem é userdeleted você poderia fazer dessa forma também caso você prefira não queira fazer o json aqui aí é de cada uma aí é como você gosta de codar como seu coração mandar aqui eu vou mandar esse json aqui e aí vamos rodar agora e ver o que que acontece task test legal deu erro porque

**[01:34:33]** Ele está falando que deu not found, a gente está procurando um id que não existe, porque o delete não tem user, né? Então, user. Massa, vamos rodar de novo? Task test, legal. Rodou, funciona, só que aqui ele está validando uma outra coisa, né? Que é esse username, bobe, tal, tal, tal. Eu quero só falar que é tipo assim, user deleted, porque não me interessa.

**[01:34:58]** Que propriedades o usuário tem aqui? Eu só quero que ele tenha sido deletado. É uma forma de ver isso aqui. Então, se a gente rodar agora, a message com m e minuscola, não é? Message. Agora vai. E aí, lindo? Ó, que cremosinho. Fala aí pra mim. Funciona, mano. Olha que legal. Que bonitinho. Pronto, todos os testes que a gente tinha estavam passando. Só que agora passam com o banco de dados.

**[01:35:36]** Claro que teve toda uma coisa, que a gente teve que mandar aqui e tudo mais, mas... Massa! Funciona bonitinho. Toda hora cai, mano. Nossa, mano. Eu vou ter que ligar na operadora pra resolver isso aqui. Mas acho que voltou agora, né? Quando a gente retorna no content, a gente não retorna o JSON, mano. Saca, quando você faz isso aqui, no content, a gente tá falando que não tem conteúdo, só que a gente tá retornando conteúdo.

**[01:36:18]** Então deu certo. Massa, saca faz sentido essa parada? Só é no content quando não tem content. Nesse caso, é ok. Massa, então agora a gente tem esse esquema. A Lugas fez uma coisa, e se eu quiser ter um histórico de users mesmos deletados, eu teria que transferir o usuário pra outra tabela e colocar, você pode colocar um campo de ativação, tipo assim.

**[01:36:51]** Activated, sei lá, deactivated, deleted, true ou false, um boleano, você pode fazer isso da maneira que você quiser. Então, aí sobre esse caso 204, a 204 é no content só quando não tem content. Nesse caso tem, então é 200. Você poderia não retornar nada, aí você daria 204. Legal, tem um caso aqui que a gente não pensou, que é interessante aqui, que é o caso onde a gente tem o user no banco de dados,

**[01:37:23]** Lembra que os campos são unique, né? O username não pode ser duplicado? Então imagina, a gente está fazendo essa validação aqui no... no post, né? Só que a gente não faz essa validação no put. Então se eu quiser alterar para um nome de registro que já existe, então beleza, eu tenho username Fausto. Aí eu tenho username Regis. Aí o Regis quer trocar o username dele para Fausto. E aí o que que acontece?

**[01:37:54]** Então eu preciso fazer essa validação aqui. Eu preciso saber se isso vai dar certo ou não. Isso vai dar um erro de integridade no banco de dados. Então eu preciso garantir que aqui, a hora que eu for fazer esse pute, voltou. Aí eu vou dar um jeito da gente tentar simular isso aqui. Então eu vou copiar isso aqui e a gente vai discutindo junto aqui. Massa? Então...

**[01:38:43]** A gente vai debatendo tudo que está acontecendo aqui no teste, já no código. Então, olha o que a gente vai fazer. Eu vou testar o update, a integridade do update. Então, o que a gente vai fazer? Eu vou criar um user na base de dados, com a fixture de user. E aí, depois, a gente vai inserir outro user. Eu vou inserir o Fausto aqui, por exemplo. E aí, esse é o post rodou aqui. Está tudo massa.

**[01:39:17]** E aí o que eu quero fazer depois? Eu quero alterar o username, tá vendo? Do user que a gente já tinha lá com o ID certinho para o username do falso. Massa? Então beleza, a gente tem o falso na base que a gente tá inserindo aqui dentro do teste e a gente tem o user que ele já foi criado antes, é o da fixture, o teste.

**[01:39:50]** Lembra esse user aqui, o teste. E aí eu quero alterar o username dele de teste pra Fausto. Por isso que a gente tá passando o user ID dele aqui. E aí quando eu for fazer essa operação, tem que dar erro. Vamos ver o que que acontece? Eu vou tirar isso daqui, então a gente tá mandando no post, depois do post a gente manda o put pra tentar alterar um registro que já foi inserido. Vamos ver o que que rola aqui? Eu não sei se eu salvei. Vou rodar aqui, vamos ver o que que acontece.

**[01:40:24]** Olha, ele deu erro. Test Update Integrity Error. Falou o seguinte, olha, deu erro de integridade mesmo. Ele falou aqui, SQL Alchemy Exec Integrity Error. Erro de integridade. Unique Constraint Failed. User, username. Então, tipo assim, eu tô tentando passar uma restrição que já aconteceu, tá ligado? Tipo assim, eu tô tentando imputar um valor num campo que é unique.

**[01:40:51]** e ele já estava preenchido anteriormente. Isso não pode dar certo, isso tem que falhar. E está certo. Está certo o erro, né? Então, o teste testa a coisa certa. Está dando erro na aplicação, porque a aplicação não foi treinada ou tratada para resolver esse problema específico do Unique. Então, o que a gente vai fazer? Eu vou dar um try aqui. Simplão. Simprão de tudo aqui na nossa aplicação.

**[01:41:23]** Ok, test app. Ok. E eu vou fazer o seguinte, olha, na hora que você for fazer isso aqui, dá um try. E tudo o que vai acontecer dentro dessa operação, vou dar o return aqui também. A gente tenta, se não der, a gente vai levantar uma exception. E qual é o tipo da exception que ele levanta aqui? Essa é a exceção de Integrate Error aqui. Então a gente vai ter que importar lá do SQL Alchemy aqui em cima, então vamos lá. From SQL Alchemy.

**[01:41:58]** Exception import integrity error. E aí a gente vai trazer ela para cá e vai simplesmente fazer aqui ó. Se der erro de integridade, a gente vai levantar o erro de conflito, que é o mesmo erro que a gente já tinha criado antes, né? A gente já viu ele aqui, né? Que é esse aqui, né? Do conflito. E aí nesse caso aqui eu vou fazer diferente, né? Eu vou fazer username ou email, né?

**[01:42:38]** O diferente do que eu tinha feito lá em cima. E username ou email, a red existe. Ou seja, só para mostrar que dá para fazer das duas formas. Lá em cima a gente destrinchou o que estava igual e aqui a gente está mandando uma mensagem genérica para todo mundo. Ah, esse email ou esse username já existe. E aí aqui a gente vai cair no caso em que a resposta vai ser o conflito, o 419. Vamos rodar o teste agora para ver o que acontece?

**[01:43:12]** Ah, beleza. Isso aqui tem que ficar antes do ORM. Legal. Format. Vou dar de novo o task test. E o teste tem que passar. Mas ele passou de um jeito meio abusado. Tipo assim, ele funcionou. Porém, contudo, entretanto, todavia, esse teste não testa nada. Porque ele não tem acerte.

**[01:43:37]** Ou seja, a gente não está garantindo que o resultado é o que deveria vir, né? Então aqui a gente tem que falar que essa response que veio aqui do update, então eu vou ter que fazer o seguinte. Assert, response update, ela é, eu poderia usar só a response aqui, porque o de cima não tem nada, né? Então response.statusCode é igual ao que? HTTP é status.conflict, né?

**[01:44:13]** retornou o conflito. Agora sim, o teste testa se veio o conflito certo. E aí a gente tem que testar a mensagem que a gente queria, não é? Então a certe, a response.json é igual ou igual a message, não é message, é detail, não é? O detalhe do erro é que username ou email, username ou email.

**[01:44:42]** O que é? A RedExis, né? É isso aqui. Então, esse é o caso do erro de integridade, que a gente não tinha pensado quando a gente implementou o Endpoint. E aí, com isso, se a gente rodar os testes agora de novo... Nice! Tá tudo funcionando. Se a gente for olhar o Coverage agora, então vamos lá. A Zen Browser, de novo. Você pode clicar no arquivo, né? HTML Cov Index. Vamos ver o que aconteceu aqui. Ó.

**[01:45:16]** Dentro do app, eu tenho alguns caminhos não testados, né? Eu não tenho um teste para validar se isso aqui cai no conflito, o username ou o e-mail. Eu não tenho um teste de 404 do Put. Eu não tenho um teste do 404 do Delete.

**[01:45:36]** Massa, então isso aqui são aqueles testes que tinham ficado para o exercício. Lembra que um dos exercícios da aula 3 era um cobrir esses cenários? Então vocês já têm esses testes e vocês estão fazendo as coisas direitinho, certinho. E a ideia é que você, saca, reescreve esse teste ou atualize esses testes para contemplar esses cenários de 409, né?

**[01:46:08]** Então, tipo assim, vocês já têm o teste, não é porque o teste era do exercício passado, mas vai ter que dar uma olhada nele para atualizar ele para funcionar com essa fixa do banco de dados, esse é o exercício da aula de hoje. Uma outra coisa que a gente tem que olhar é que na aula 3 foram criados novos exercícios, lembra? Foi criado o endpoint que abriu a ID, que era um get por ID. Então vocês vão ter que...

**[01:46:34]** implementar a sessão do banco de dados lá dentro e atualizar o teste para o teste que está dentro desse esquema aqui, né? Então a gente vai ter que usar a fixture de user, vai ter que fazer aquele esqueminha todo. Massa! Essa é a ideia dos exercícios. Eu não sei se está todo mundo aí, está todo mundo quietinho. Mas essa é a ideia dos exercícios dessa aula. Legal lembrar vocês de que tem que fazer o quiz. É importante fazer o quiz e fazer os exercícios.

**[01:47:14]** que a gente tem aqui para fazer, então atualiza as coisas, testa o 409, implementa naquele endpoint que você tinha feito, como dever de casa e tudo mais, bora fazer o quiz, sim, bora fazer o quiz. E é isso, eu vou dar o commit aqui e vou subir isso aqui, então para quem já...

**[01:47:35]** Tá legal, já sabe o que é pra fazer. Tá cansado, precisa descansar. Família, emprego. Legal, a aula acabou aqui. Dá um beijo, aqui ó, beijinho. Tamo junto. E pra quem quiser ficar pra fazer as perguntas, tirar dúvidas, agora é a hora. Enquanto eu comito aqui, vou mandando perguntas se tiverem perguntas, claro. Nossa, então legal. Comitado está.

**[01:48:18]** Terei que rever a aula. Não, não, é muito detalizinho, né? Eu acho que essa aula e a aula passada, elas são meio brutais nessa parte de tipo, pô, é muito detalizinho, é fixture aqui, eu não sei o que, eu não sei o que lá, e aí vai e volta, dá um nó, uma fixture conecta na outra, eu sei que isso é complicado. Se vocês tiverem com dúvida sobre esse assunto, a gente tem a live das fixtures do PaiTest, né? Tá no material referenciado, quem quiser ver depois?

**[01:48:50]** Cadê aqui? Cadê, cadê, cadê aqui? Então, pra quem tiver um pouco de problema com isso, dá uma assistida nessa live aqui que eu dou uma explicada mais básica nessa brincadeira das fixtures, a gente entende direitinho o que que acontece dentro de cada uma e tal, porque esse assunto é trivial, assim, de ter o conhecimento nesse rolê aqui. A aula passada achei mais tranquilo.

**[01:49:34]** Mas essa foi muita coisa mesmo, então é... E é muito louco, porque se você não faz uma coisa, você não consegue encaixar a outra, né? Tipo assim... Pô, aí não entra a injeção de dependência, aí vai dando um mortal triplo-carpado, saca? É isso. Mas vamos com calma, vocês precisarem de mim, eu tô lá no grupo, sempre respondendo esse tipo de coisa, a gente vai conversando, vai vendo o que for possível...

**[01:49:59]** de tudo mais. A Rodrigo está mandando como ele fez o exercício. Menos, se você quiser comparar, tem a resolução dos exercícios. Lá no material de texto tem a resolução, caso traves e tudo mais. Então legal, como não tem perguntas, eu vou encerrar por aqui. E aí, se vocês tiverem dúvida, entrem lá no grupo, me chamem, a gente vai conversando. Massa?

**[01:50:37]** Então é isso, beijinho pra vocês, desculpem aí pela internet que tá caindo hardcoremente hoje. Eu vou ver se eu ligo na operadora pra gente resolver isso até semana que vem. Beijo pra vocês, ó, e até terça-feira. Façam os exercícios que agora eles estão ficando mais entranhados nas coisas, né? Beijinho, tchau!

