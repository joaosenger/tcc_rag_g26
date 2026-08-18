# Transcrição da Aula: aula-09.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:05]** Olá, pessoas! Boas-vindas! A mais uma aula do nosso curso de Fashion API. Eu sou o Dono Saoro, pra quem tá aqui pela primeira vez. Olá! E aí, conto com o feedback de vocês aqui pra saber se estão me vendo, se estão me ouvindo, se tá dando tudo certo. Às vezes eu tô falando sozinho, pra nada, pra ninguém, aí fica difícil.

**[00:00:25]** Bom, enquanto vocês vão me falando, está tudo certo, hoje a gente vai conversar um pouco sobre o sistema de autenticação, não só autenticação, mas autenticação e autorização, que são coisas que a gente viu na aula passada. Algumas aulas atrás, antes do Async e antes do Refactor, a gente começou a trabalhar no sistema de autorização, mas ficaram algumas coisas em aberto.

**[00:00:52]** escutando, obrigado. Te ouvo, adoro oubo. Então, aí a gente fica nessa brincadeira, né? Tipo assim, pô, a gente fez o sistema, mas a gente não garantiu muitas coisas, né? A gente não sabe se o Tolkien inspira o que que acontece, a gente não passou na parte de autorização, né? A gente meio que não fez os testes, a gente foi deixando algumas coisas pra depois e nessa aula a gente vai voltar um pouco a falar sobre isso.

**[00:01:22]** Bom, para quem quiser o link da aula está aqui, eu estava revendo algumas coisas. A gente está na versão 4.0, sempre lembrar, sempre bom lembrar disso. E aí, para quem quiser o link da aula, quiser dar uma acompanhada, copiar os códigos, que você estiver fazendo junto comigo é sempre bom.

**[00:01:42]** Bom, então, o que exatamente a gente vai fazer hoje, né? A gente vai testar os casos de autenticação, né? De forma correta, né? É uma coisa, porque a gente não sabe se a autenticação exatamente está funcionando, como ela está funcionando, a gente tem alguns casos que a gente não testou. De autenticação, de autorização, a gente vai implementar o refresh do Tolkien, né? Que é uma das formas do JWT de lidar com alguns probleminhas que a gente tinha, né? Que é o exemplo de, ah, acabou o tempo, eu tenho que logar de novo.

**[00:02:13]** Então, antes de acabar o tempo, a gente pode dar um refresh no Tolkien, pegar o Tolkien de novo, e assim a gente evita de trafegar a senha. O usuário senha na aplicação várias vezes, né? A gente pode só dar um refresh no Tolkien. Um refresh no Tolkien. Obviamente, a gente trabalhou com isso num tempo de 30 minutos, aí tem que estar muito refresh, mas se lembra, é aquela questão de regra de negócios. Você quer um Tolkien que dure cinco dias, você quer um Tolkien que dure cinco minutos, aí depende muito.

**[00:02:40]** E aí, bom, nosso foco hoje!

**[00:02:44]** nos testes, porque a gente tem que testar bastante coisa embora a gente vai implementar o refresh, a gente vai conhecer duas bibliotecas que são muito massas assim, que eu gosto muito. Uma delas é o FreezyGum, existem outras bibliotecas para fazer isso, mas é uma biblioteca que manipula o tempo, ou seja, eu posso falar que, ah, o Tolkien vai ser gerado 30 minutos atrás, ou que o Tolkien vai ser gerado agora, mas a gente vai viajar no tempo,

**[00:03:12]** Dentro do teste é uma forma de driblar o teste, driblar os date times para falar que a gente está no futuro, que a gente está no passado, saca? Então a gente vai mentir o tempo aqui. E por último, e não menos importante, acho que é a primeira coisa que a gente vai ver, é como fazer a geração de modelos automáticos, com uma coisa que se chama Factor Boy. Factor é um modelo de...

**[00:03:38]** de padrão de projeto, né? Pra criar vários users, várias coisas, vários dados. Então, é o menino da fábrica. Então, consegui fazer umas coisas bem legais aqui. E, pra quem assistiu aquela aula suplementar, né? Era sobre randomização de testes, que era essa coisa. De volta pro futuro, dez. Exatamente. Back to the future, eu adoro esse filme. Então, vamos lá. A primeira coisa que eu quero falar com vocês aqui, hein?

**[00:04:05]** de volta para o futuro 10 é muito bom. Peraí que eu voto C. A primeira coisa que quero falar com vocês aqui é sobre o teste de autorização. Se a gente for olhar dentro dos nossos testes, tanto o Pute quanto o Delete, eles têm esse bloco aqui.

**[00:04:32]** que é o ifcurrentuser, diferente de user ID. Para a gente ver, se o usuário corrente, a pessoa que logo, a pessoa que enviou o token via Berna no header, é ela mesmo e tal, quem ela é. E se ela pode fazer uma operação que infringa o outro user. Ou seja, eu quero alterar o cadastro do Ruzni, por exemplo, do Regis.

**[00:04:58]** Eu não posso conseguir fazer isso, né? A ideia é que a gente consiga desviar desse caminho, né? Só que a gente não testou isso. E na edição do ano passado, nesse curso, a gente discutiu bastante sobre isso aqui, porque a gente chegou numa conclusão que esse teste poderia ser feito dessa forma. Então, eu vou ler o teste aqui com vocês, mais ou menos, a gente vai copiar, vai levar para lá.

**[00:05:24]** e vamos tentar discutir ele aqui. Mas basicamente ele é um teste que atualiza o user com o user errado. Olha que massa. E aí a solução que a gente chega aqui é essa. De que, beleza, se a gente quer testar com o user que é um outro ID, como a gente tem que passar o ID do usuário nesse endpoint que a gente quer modificar, a gente poderia fazer isso aqui, né? Somar mais um.

**[00:05:52]** E simples assim vai funcionar, a gente vai conseguir cobrir esse cenário. Então a gente vai tentar atualizar os dados, né, de quem seja o client aqui, com as credenciais do client, na verdade, com esse JSON, só que passando o ID de outra pessoa. Então, sabe, o ID do próximo user. Aí ele tem que dar forbida, né, que é o esperado aqui, né, ou seja, você não tem permissões o suficiente para resolver isso.

**[00:06:24]** essa coisa que você quer fazer, né? Essa brincadeira. Eu vou colocar ele aqui já no... Eu tô com o código aberto aqui, deixa eu lá nos testes. Esse é o teste do... Esse é o teste do users aqui embaixo. Eu vou colocar esse teste como último aqui. E aí eu vou rodar ele com aquela estratégia que a gente tinha pensado antes, né? Do minus k e tudo mais. Só pra gente ver o que que acontece aqui. Então eu vou dar um... Eu vou...

**[00:06:52]** ativar o shell né, para ficar mais simples, poetry shell, mas você pode dar um poetry run se você quiser. Então poderia fazer um poetry run, task test-k, esse aqui, só para a gente rodar esse único teste aqui, só para a gente ver o que acontece. Olha que interessante, esse teste, ele passa o teste update...

**[00:07:16]** user with wrong user, né? E se a gente for olhar o coverage aqui, então vamos lá no Zen, Browser, HTMLCovindex.html, se a gente for olhar lá no nosso users, a gente vai ver que aqui na parte do update, pera, tem alguma coisa errada com o meu...

**[00:07:44]** Ah, tá. Ele só vai testar aqui, né? A gente mandou rodar só esse aqui, então ele deveria cobrir só essa parte, né? Eu tô tipo, nossa, tá tudo descoberto, mas é porque a gente rodou só um teste. Olha que interessante. Ele passou por aqui e ele entrou nesse rise, né? Forbidem e tudo mais. O que significa que funciona, né? Você tá vendo que a gente consegue fazer essa simulação aqui. Só que essa simulação, ela tem N problemas, né? A gente tem muitos problemas aqui pra discutir dentro disso aqui, né?

**[00:08:16]** Porque, por exemplo, isso funciona, é uma técnica, tipo assim, ah, beleza. Eu consigo bypassar o teste e tá tudo bem, né? Falando, olha, eu vou modificar um ID que não é o meu ID. É exatamente isso que o teste testa, né? E é exatamente isso que é validado lá no nosso endpoint aqui no Users. Então, a gente tá no Put aqui.

**[00:08:44]** Só que vamos parar para pensar em como isso funcionaria num cenário de verdade. Em teoria, testa o que tem que testar. Mas vamos pensar o seguinte, esse mais um aqui que a gente adicionou, ele cumpre o requisito, mas a gente valida com um hack. Vocês concordam comigo que não existe mais um na base de dados? Tipo assim, a gente está validando, sei lá, o user 1, porque todo banco limpa.

**[00:09:13]** E a gente vai testar, a gente vai mandar o ID do User2. Mas não existe User2. E agora, o que que a gente faz, né? Rosinha, muito obrigado, mano, pelo teu super chat do cafezinho. Valeu demais, mano. Então, caso esse usuário existir, será que isso vai funcionar em produção? A gente não sabe, porque a gente não tem outro usuário na base, né? Toda vez que a gente roda o código,

**[00:09:48]** A gente drop o banco de dados, roda o código de teste, no caso, drop o banco de dados. A gente vai pro ID número 1 e, ok, massa. E como é que a gente representa um cenário mais próximo da realidade, onde a gente tem dois users? É isso que eu gostaria de pensar aqui.

**[00:10:11]** Que beleza, em teoria nada de errado existe aqui dentro desse teste, mas como é que a gente representa isso mais próximo da realidade? Existindo o outro ID de fato. Então, a gente precisa adicionar um novo user, né? Esse é o grande ponto. Só que beleza, a gente vai entrar no ponto aqui de que a gente vai adicionar um novo user e a gente tem aquela fixture aqui que a gente criou há uns dias atrás, que é o...

**[00:10:43]** user, assim que def user. Essa aqui. E essa feature tá aqui, ela funciona, tá tudo bem. A gente poderia duplicar isso aqui, né? Só que se você entende que duplicar isso aqui vai ter alguns problemas, né? Porque por exemplo, imagina que eu se eu precisar de três users. Como é que eu vou fazer? Se eu precisar de cinco users, sei lá, em algum cenário hipotético. E toda vez eu tenho que gerar esses nomes de forma diferente, né?

**[00:11:18]** Então beleza, o teste, o username teste, ele não pode ter teste no próximo username, porque os usernames são de unique no banco de dados, né? Lembra? A gente conversou sobre isso na aula 4, onde a gente estava fazendo esse tipo de incremento. Então eu preciso de uma forma de que toda vez que eu criar um user dentro do teste, ele seja um user diferente. Ele não pode ter as mesmas credenciais.

**[00:11:49]** Aí, o Resident falou, eu dupliquei em um teste que eu fiz, mas não tem problema, porque a gente não tinha chegado. Essa aula é exatamente para a gente conversar sobre isso aqui, né? Então, aí a gente entra numa biblioteca que eu gosto muito, que se chama Factor Boy, e a gente vai instalar ela.

**[00:12:05]** A Factor Boy vem de fábrica, o Factor é de fábrica, porque existe um padrão de projeto clássico do Game of Thrones, do livro clássico de padrão de projeto chamado Factor, que é uma forma de criar qualquer objeto. Então a gente precisa pegar isso aqui e gerar qualquer coisa, que a gente precisa com isso. Então a gente vai adicionar o Factor Boy aqui. Aí o Tenebu mandou uma coisa interessante.

**[00:12:36]** Usa o random. Então, o problema de usar o random, ou dados aleatórios de verdade, é que a gente não consegue validar, né? A gente não consegue fazer um teste determinístico. Ah, se eu criar um usuário, qual vai ser o e-mail dele? Eu não sei, porque a gente usou um valor random. Então, a ideia do Factory Boy é criar uma randomização, de alguma forma, mas uma randomização padronizada.

**[00:13:05]** loucura isso, né? Randomização padronizada. Tudo bem, vamos instalar o Factor Boy aqui e aí a gente vai conversando. Ó por padrão ele trouxe uma outra biblioteca junto com ele que é o Faker, que é uma biblioteca pra gerar dados falsos, né? Pra quem assistiu a aula suplementar, que eu comendei, já entendi o que é o Factor e o Factor Boy, mas o Faker, nesse curso em específico, a gente vai ver ele na próxima ou sem ser na próxima, na outra aula. Eu não sei exatamente se é na 10 ou na 11, não me recordo.

**[00:13:36]** A gente vai ver o Faker de novo, ele vai aparecer aqui. E a ideia do Factor Boy, né, é que a gente cria uma coisa parecida com esse, olha como isso é muito foda, se liga. Eu vou importar o Factor Boy aqui, então import Factor, eu vou fazer aqui em cima mesmo. Então a gente está aqui no PiTest, eu vou importar aqui, import Factor. E aí, a partir desse Factor, a gente vai criar uma nova classe aqui embaixo. Eu estou fazendo isso no ConfTest, poderia ser em outro lugar,

**[00:14:09]** cabe discussões aqui e a gente vai importar a gente vai herdar de factor ponto factor com f maiúsculo e aí aqui eu dei um nome de user factor porque é uma fábrica de usuários aqui dentro da nossa aplicação e aí o que que acontece o o factor boy eu acho que ele está reclamando por causa do porque eu estalei a biblioteca agora não

**[00:14:46]** A gente vai criar uma class aqui dentro que eu vou chamar de meta. Aí por que meta? Porque é onde eu estou passando definições sobre a coisa que ele vai criar. Mas aí a gente passa uma coisa que a gente chama de model. Então model vai ser o user. Então toda vez que a gente chama o user factor, ele vai criar um usuário novo. Uma classe dessa coisa chamada user.

**[00:15:16]** Aí alguém pode estar se perguntando, bom, mas o que que é user? É a nossa tabela do banco de dados, né? Então ele vai criar um novo objeto disso baseado em algumas regras que a gente vai passar para ele. Então, por exemplo, o que que eu quero daqui, né? O que que são os campos que a gente tem que passar, né? Que são os campos que não são init, né? Ó, é o createdat e o id ele gera sozinho, né? Então a gente precisa do username e do email, né? Então a gente vai trazer isso aqui para cá, né? Então eu vou falar username,

**[00:15:48]** email e password aqui dentro. E aí o que que vai rolar aqui? Dentro disso aqui eu vou chamar o FactorBoy e vou falar para ele o seguinte, olha, FactorBoy ponto sequence, tipo assim, que é esse esquema aqui, sequence. E aí o que que o sequence faz aqui para a gente? A gente tem que passar para ele alguns dados que a gente quer gerar em sequência e como a gente quer que essa sequência se comporte.

**[00:16:18]** Basicamente isso. Então, aqui eu uso uma função Lâmbida, para quem... Função Lâmbida é um termo padrão, porque todo mundo, se não, eu posso explicar ela. Não tem problema, não. Então, aí aqui, dessa biblioteca do Factor, a gente vai chamar o Factor Sequence. E aí, o que vai acontecer? Toda vez que a gente criar isso aqui, toda vez que a aplicação iniciar, ele vai criar uma sequência toda vez que eu pedir essa classe.

**[00:16:52]** Então, a primeira vez que eu gerar um factor, ele vai me trazer o username, vai se chamar teste com esse n, que é o valor que a gente está passando aqui, que a gente não passa, que a gente preencha ele, que é o valor da sequência. Ou seja, teste zero, teste um, teste dois, teste três, teste quatro, teste cinco e assim por diante. E aí, aqui a gente vai chamar o factor de novo. E aqui do factor, eu vou chamar o lazy attribute.

**[00:17:23]** Lazy attribute. E aí o que que quer dizer? Lazy attribute quer dizer que ele é preguiçoso. Isso o que significa lazy, né? Ele vai ser avaliado tardiamente. Ou seja, depois. Depois do que? Depois de tudo que não for lazy. Aí a gente tem a referência do objeto aqui, ó. Object.username. Aí com isso aqui, olha o que que vai rolar, né? Deixa eu colocar aqui bonitinho.

**[00:17:55]** ele vai pegar o nosso objeto que é o meta o user que a gente criou e vai dar pra ele ó o username aqui como parte dessa string ou seja o e-mail disso aqui vai depender da vez que ele foi gerado então vai ser a sequência então a primeira vez que for gerar vai ser teste zero aí o atributo aqui vai ser objeto que é o user username teste zero arroba teste.com

**[00:18:26]** Massa, e a mesma coisa a gente vai fazer para o password aqui embaixo. Peraí que eu deixei dois iguais aqui. A mesma coisa vai fazer essa sequência aqui. Então ele vai pegar o object.username, que é o número da sequência, e a partir disso aqui ele vai gerando novas, né? Então o password eu coloquei qualquer coisa aqui, como se fosse um e-mail, mas não precisa ser, você pode colocar o que você quiser aqui.

**[00:18:57]** Um número malandro aqui, qualquer coisa nesse formato. E aí toda vez que a gente gerar essa class meta, ele vai gerar um user com esses dados. São dados randomizados, mas são randomizados de uma forma como eu posso dizer. De uma forma bonitinha. Deixa eu ir com vocês lá nesse arquivo para a gente ver o que está rolando. Deixa eu dar um Python. E aí eu vou navegar até lá.

**[00:19:23]** que isso está no Testes, com o Fteste a gente vai abrir isso aqui com o "-z", que é o Python interativo. Aí eu vou chamar esse objeto aqui que é o UserFactor. UserFactory. Ah, esqueci o Y. UserFactory. Aí olha o que que aconteceu. Nessa primeira chamada, ele gerou alguém pra mim. Lembra que os init só ganham valores quando eles passam no banco de dados, né?

**[00:19:50]** Então, até que se diga o contrário de Sonane. Mas olha que louco, username test0, email test0, arroba teste, o password test0, arroba exemplo. Aí você poderia colocar qualquer outra coisa aqui, qualquer, sei lá, que é um caracté para ser uma senha, saca? E aí você consegue discernir entre quem é quem aqui. Então eu vou chamar de novo.

**[00:20:12]** aí ele gerou teste zero blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá blá

**[00:20:34]** randomizado, a gente costuma dizer, ele é sequencial aqui a partir dessa montagem aqui. Então, a fábrica é esse padrão. Eu dou alguns insumos e a partir disso ele vai criando coisas em cima. E aí isso funcionaria para qualquer objeto Python que você colocasse aqui no user e respeitando os atributos que ele tem aqui dentro. Mas isso precisaria da biblioteca, não dá para fazer isso com uma função simples, que é uma sequência numérica? Então, vamos lá!

**[00:21:07]** Aqui Lucas. Aí a gente tem algumas coisas tipo assim. Create Batch 10. Pronto. A gente tem 10 users. Saca, o ponto. E tem várias outras coisas que a gente pode fazer aqui, né? Eu posso falar o seguinte, que eu vou criar um user agora, que o username dele, ou sei lá, eu vou trocar o e-mail dele. Eu vou falar, o e-mail é FaustoArrobaMail.com. Só trazendo aqui pra cima.

**[00:21:45]** Agora ele criou o teste 16 com o falso modificado, mas os outros atributos lazy. Então você está vendo que eu tenho controle total de como a coisa vai ser criada e vai ser randomizada aqui? Saca, é muito mais complexo do que simplesmente adicionar uma sequência. É que no nosso caso

**[00:22:08]** Para esse exercício aqui que a gente está fazendo, a gente só precisa de um user, é super simples. Mas nas próximas interações que a gente for fazendo com isso, a gente vai criando coisas mais complicadas. Então, essa é a ideia do Factor Boy aqui no projeto. Legal? Fez sentido? Não entendi o lazy ainda. O lazy, ele vai fazer o seguinte, ó. Todos os atributos aqui embaixo são lazy, tá vendo? Deixa eu ver se ele carrega de novo o arquivo aqui, que ele está chatão com esse...

**[00:22:46]** vermelho aqui pronto só para ficar mais limpo aqui ele vai criar essa coisa que é o que precisa da sequência aí depois que ele definia a sequência ele vai para os lasers os lasers tem os o próprio objeto meta como referência e aí você pode passar o username é o username que foi gerado no outro campo tá vendo é por isso que ele é lazy ele é gerado depois dos outros campos fez sentido agora?

**[00:23:35]** Deixa eu dar um format aqui, velho. Ah, pera aí, deixa eu roubar isso aqui. Tás que format. Legal. Ficou tudo cabindo aqui. Entendi. Massa. Então, beleza. Então, a gente pode partir para o próximo aqui. Então, agora, o que a gente vai fazer? A gente vai começar a usar essas coisas que a gente definiu aqui. Eu não sei se vai dar. Ele deu... ficou maior aqui. Legal.

**[00:24:14]** Então, a gente tem esse objeto. Então, a ideia é que a gente pegue o factor boy e use ele para a gente gerar os nossos próprios modelinhos aqui quando a gente precisar. Então, agora em vez de chamar o user, construir a coisa, passar os dados que a gente queria aqui, a gente não vai fazer mais isso. A gente vai chamar o factor. Então, a gente vai chamar o user factor.

**[00:24:38]** e ele vai decidir tudo que a gente quer, só que o único dado que a gente vai passar para ele, de verdade, é esse aqui, eu do password. Aí você vai falar, mas por que a gente vai passar o password? Porque o password ele tem aquela regrinha, né? De ter que ser criptografado. Então a gente tem que ter essas duas coisas aqui, né? A gente tem que ter a criptografiazinha dele aqui, né?

**[00:25:04]** Tudo bem, eu poderia passar isso aqui, aqui dentro, no lazy attribute também, se eu quisesse. Eu poderia fazer isso aqui, né? Get password hash desse objeto aqui, e aí toda vez que a gente chamasse o lazy, vamos chamar de novo agora? Ah, tá. Eu esqueci o password aqui. Pronto. Toda vez que a gente chamar o lazy aqui, ele já vem criptografado. É uma outra opção. Olha que doido. A senha já vem certinha. Ó.

**[00:25:39]** A senha já está incriptada. A gente poderia fazer aqui, poderia fazer lá. Aí é uma questão de escolha aqui, né? Eu vou deixar lá porque eu gosto de que... Porque tem uma maracultaiazinha do password com o clean password e tudo mais, então eu vou deixar aqui. Mas vocês sacaram aqui o que que a gente trocou? Uma coisa bem simples, né? O que a gente fez. Aqui vai retornar o user agora e vai trazer para cá. Simplon. Jonas, obrigado.

**[00:26:12]** pelo... pelo teu super chat e ele falou pra que vocês não esqueçarem de deixar o like sempre importante não esqueçam pra isso chegar em mais pessoas então agora a gente tem o user aqui feito de uma maneira simples e agora eu posso gerar quantos users eu quiser na sequência que eu quiser como eu só preciso de dois por enquanto então eu vou criar uma outra fixture aqui que a gente vai chamar de order user, outro usuário order user

**[00:26:46]** E aí agora toda vez que a gente precisar de um outro usuário, a gente tem essa fixture aqui. Mas vocês lembram que se a gente precisar de 20, a gente cria em batch. Mas por enquanto, para simplificar os testes, eu vou criar esse outro ordered user aqui. A fixture é exatamente a mesma.

**[00:27:04]** Só que aqui ele vai gerar um user, com um ID e depois ele vai gerar com outro. Uma coisa maluca que vai acontecer aqui, que pode acontecer, é que os testes podem começar a falhar agora. Porque se a gente anotou ID 1 em algum lugar, nos exercícios, por exemplo, você colocou o ID fixo, como 1, o teste não vai passar mais. Porque a gente não sabe mais qual o ID. Agora ele está fazendo várias coisas e tudo mais. Vamos ver o que que acontece? Tasque teste, ver se roda.

**[00:27:32]** Em teoria está tudo funcionando, só que a gente ainda está com aquele teste problemático lá atrás, que era o UpdateUserRifWrongUser, com o usuário errado. E aí olha a solução aqui, a gente vai simplesmente criar um OrderUser, e desse OrderUser a gente vai passar aqui, OrderUserIg. Simplão. Então vamos lá no TestUser, em vez de fazer esse user aqui, a gente chama o OrderUser. O outro usuário.

**[00:28:10]** E aí a partir disso aqui a gente chama ele aqui, orderuser.id. E aí não preciso mais desse mais um. É uma garantia de que esse objeto sempre vai estar aqui, né? Ele sempre vai existir porque a gente criou dois. Aí você vai falar, bom, mas eu tô passando do order user, como é que ele funciona, né? Por que ele tá pegando do outro? Mas como é que isso aqui funciona? É por causa do Tolkien, né? O Tolkien, a fixture de Tolkien.

**[00:28:41]** Usa o user como base, né? Aqui, ó. Então ele sempre gera do user. Então toda vez que você precisar simular outro usuário, você usa a fixture de order do user. E aí ela funciona aqui de um jeito mais simplão. Massa! Deu pra entender o que a gente fez aqui? Fez sentido? Isso aqui? Agora a gente tem a cobertura daquele caso, né? Que a gente queria. Tás que... Tá loucura aqui, tá difícil de achar. Tás que teste, vai.

**[00:29:20]** Beleza, aí estão todos os testes passando, a gente tem a cobertura, que a gente precisava aqui no coverage agora, dessa parte, e a gente garantiu que está tudo sendo feito com dois usuários, existe o outro ID na base de dados. E aí tudo fica mais simples. E aí, vários outros testes que a gente tinha aqui, aí se vocês quiserem, vocês podem fazer depois. Lembra do teste DB, que a gente cria várias coisas aqui, a gente poderia usar a fixture para fazer isso.

**[00:29:56]** o factor, que é uma fiction. Então você poderia colocar ela aqui, você pode brincar com isso de várias formas, da forma que você se sentir mais tranquilo com isso. Mas se fez sentido? Ou estou falando sozinho? Então aí a gente responde àquela pergunta que a gente já fez aqui atrás. Como é que a gente representa o cenário mais próximo da realidade?

**[00:30:26]** adicionando novo user literalmente ao teste e aí a gente tá testando igual seria na vida real em produção massa e aí é mesmo o mesmo coisa vale pro delete né então tipo assim ai eu quero deletar alguém que não é eu mesmo saca então se eu não quero deletar se eu quero deletar alguém que não sou eu a gente só usa other user e aí o token a gente usa o token do usuário original basicamente esse teste não tem nada de mirabolante né a gente tá chamando o cliente

**[00:30:58]** Delete, aí a gente passa o ID do outro usuário, que não é o do Tolkien, e beleza, Forbidden, massa, sensacional, muito simplório isso aqui. Aí eu vou colocar aqui também, né? Beleza, a gente já sabe que vai funcionar, porque a gente já entendeu todo esse mecanismo, mas o importante é ver a cobertura nova aqui, né? Que a gente vai ganhar, que é o do Delete, que a gente não cobriu esse bloco aqui, né? Então vou rodar o task test.

**[00:31:33]** Dá um F5 aqui? E lindo! Beleza, cobrimos esse cenário. O other user é interessante? Para quem quiser refatorar a aplicação, tem esses pontos aqui ó. Como é que se simula o usuário que já existe dentro da base de dados? Saca!

**[00:31:53]** Então se adiciona o user, aí na hora de criar o factor, você cria com o mesmo user name do user passado. Então dá várias opções de refaturação aqui para quem tiver atrás disso, para quem quiser brincar com isso. Então tem várias formas de uso aqui. Não vai ser perdido. Massa? Aí agora eu queria conversar com vocês sobre a inspiração do Tolkien. Agora que a gente tem esse mecanismo para ficar brincando com users e tudo mais, eu vou para a segunda parte aqui para a gente discutir outra coisa.

**[00:32:26]** Bom, lembra que quando a gente gerou o Tolkien, a gente gera um Tolkien e ele tem uma validade, né? Geralmente o Tolkien tinha 30 minutos de duração e depois de 30 minutos, o Tolkien tem que expirar e quando o Tolkien expira, a gente vai ter que fazer o login de novo dentro da nossa aplicação. E aí ele sempre vem nesse tempo maluco aqui, que é alguma data em algum momento aqui da aplicação.

**[00:32:58]** Aí ele vem na clã de inspiração, né? Que é quando esse token para de ser válido. Só que a gente não criou nada pra isso, né? Esse é um ponto aqui, né? Como é que funciona o que a gente fez? A gente autentica pra criar o token, né? A gente faz o login. Não dá no off-token.

**[00:33:18]** Depois, a gente cria um token com um tempo de inspiração com a clã, a gente retorna isso aqui, aí o user pode fazer várias outras coisas. A gente manda o PUT, o POST, o DELETE, o GET, o POST não necessariamente, mas o GET, o DELETE, o UPDATE, que é feito via PUT, a gente manda a URL mais o token, a gente vai ali do token e retorna a forma como a gente está fazendo até agora.

**[00:33:49]** O grande problema aqui é que, em algum momento, esse Tolkien tem que parar de valer, né? Depois de 30 minutos, o Tolkien não pode valer mais. Ou seja, passou esses 30 minutos e aí lembra que o tempo aqui é uma variável de ambiente. A gente muda conforme a gente achar necessário, né? Pô, é 30, 50, 100, aí é contigo. Quantos minutos isso vai durar? Mas a gente ainda não implementou isso aqui. A gente nem sabe se funciona.

**[00:34:18]** Quando o Tolkien tá inspirado, acontece o quê? Então, agora a gente vai conhecer outro mecanismo de teste, né? A gente viu o Factor Boy, e agora a gente vai conhecer o Freezy Gun, que é, como alguém tinha dito, ali, o Back to the Future, né? A brincadeira de andar no tempo. E esse slide tá errado, né? Porque eu tenho que adicionar o Freezy Gun no teste, né? No grupo de desenvolvimento, né? A gente vai ter que adicionar ele aqui, no grupo de desenvolvimento. Então é o Freezy Gun.

**[00:34:50]** Freezy é de congelamento, né? De parar, né? E a Gun é de arma, né? A arma do tempo. Legal, aí ele instalou o Date-Ultre, que é uma outra biblioteca para manipular tempo, e o Six é para a compatibilidade entre Python 2 e Python 3, que é duas vezes três, seis. Ok. Ok, a gente vai superar isso aqui. Então a gente vai instalar o Freezy Gun. E qual que é a ideia do Freezy Gun aqui?

**[00:35:21]** O FreezyGam tem uma função que se chama FreezyTime, ou seja, congela o tempo. E aí a gente vai congelar o tempo em qualquer momento que a gente quiser que o tempo seja congelado. E aí a partir disso a gente vai conseguir validar se o nosso tempo está na frente, se o nosso tempo está atrás, para onde está o Tolkien aqui. Então a gente vai criar aqui, é uma simples chamada, né?

**[00:35:53]** para o post, então a gente vai fazer um post para o off-token e a gente vai mandar o username e o password limpo para ele fazer a validação lá. Igual a gente faz em todo post de login. Só que olha que doido, a gente vai parar o tempo com essa função chamada FreezyTime. Vamos levar isso para lá e vamos conversando sobre o que acontece. Agora a gente vai no testes do...

**[00:36:27]** Securit, que é onde a gente estava brincando com isso aqui. Não, é do teste do Alf, desculpa. Cadê, cadê, cadê Alf aqui? É a mesma coisa que a gente tinha feito aqui para ver se vinha o Bertoken e tudo mais. Vou colocar o Freeze Gun lá em cima e essa função FreezeTime faz exatamente o que se propõe a fazer. Ela para o tempo. E aí, beleza. Quando vocês querem parar o tempo? Alguém me fala uma data aí para a gente parar o tempo.

**[00:37:08]** Fala, fala, fala um aniversário aí, fala seu aniversário, quando é que você faz aniversário? Quando é quando nasceu, né? Pode ser aniversário, vai pra não expô muito. Então vai ser um aniversário de alguém aqui. Só precisa falar o dia e o mês. Não, pô, virar do dia no novo é muito padrão, né? Vamos colocar um dia quebrado aí, pra ser o dia de alguém aí. Vamos prestigiar alguém, né, pô? 31 do 12, beleza. Então a gente vai no... Rusni, por enquanto. Então a gente tá no 31, né?

**[00:37:48]** dia mês 12 31 a data no formato americano é o contrário né então é dia mês ano e aí vai ser ao meio dia isso aqui então quando a gente rodar essa função o tempo aqui dentro eu vou colocar um debugger aqui pra gente brincar break point e vou comentar essa última linha só pra ele não pro linter não reclamar ó o tempo aqui dentro

**[00:38:22]** É isso aqui, 31 do 12, meio dia. Então vou dar um task test aqui. Se a gente chamar o tempo agora, então sei lá, vamos ver que horas são agora. Então, from date time, date time, import date time, date time, date time, date time ponto now. Que horas são agora? Olha aí, eu nasci em 31 do 12.

**[00:39:12]** Tá vendo que loucura isso aqui? Olha que maluco. Vocês conseguiram entender o que aconteceu aqui? O tempo é outro momento, mano. Eu pedi a hora de agora. E ele falou que agora é dia 31 do 12 de 2025, meio dia. Doido, né? Doido, doido. A gente deu um print nisso aqui. Aqui, ó. Só que você viu que ele mudou o date time, né? Quando a gente pede o date time now, ele me deu um fake date time.

**[00:39:56]** Ou seja, porque ele mudou a parada. Deve dar pra enganar a inspiração do Office, é ótimo. Congelou o tempo, mas congelou o tempo só dentro desse bloco do gerenciador de contexto, WIF. Olha que interessante. Eu vou colocar um breakpoint dentro e um date time fora. Você poderia brincar com isso aqui.

**[00:40:23]** Então olha que massa, eu consigo simular qualquer hora que eu quiser, agora e travo. O Edu ficou preso no tempo, sim. Olha que interessante isso aqui. Essa biblioteca para fazer testes é sensacional. Então a gente parou o tempo aqui com o Freezedime. E aí, agora, eu vou fazer o seguinte, eu vou pegar esse Tolkien, olha que interessante, agora vamos voltar a entender o teste aqui. Então beleza, a gente pediu o Tolkien,

**[00:40:50]** Aí a gente viu, olha, status OK, então o nosso Tolkien, que foi criado agora, 31 do 12 de 2025, ao meio-dia, em teoria, esse Tolkien tem esse tempo, né? Esse tempo em específico. E aí o que a gente vai fazer? Se a gente quer testar se o Tolkien está inválido, a gente vai viajar 30 minutos para o futuro, que é essa coisa aqui.

**[00:41:25]** Pera aí, aqui. Eu vou copiar tudo aqui, depois a gente vai debatendo lá. Então aí aqui, eu vou pegar a mesma data que a gente tinha aqui e a gente vai para o meio dia e 31. Ou seja, se o Tolkien tem validade de 30 dias, agora a gente vai, 30 dias não, 30 minutos, a gente vai para 31 minutos no futuro e aí a gente vai tentar fazer um pute.

**[00:42:11]** E aí ele tem que dar... Anautorized. Por que ele tem que dar Anautorized? Porque a gente ultrapassou o tempo de validade do Tolkien. Aí você vai falar, ah, mas aí quanto tempo eu coloco aqui? O tempo que você precisar, né? Lembra que, como isso tá no nosso ponto envy aqui, né?

**[00:42:29]** Então lembra, você valia da regra de negócio. Pô, ele expira em 30 minutos. Então você pega esses 30 minutos e bota lá. Você pode colocar o próprio tempo do settings aqui, aí fica até o critério como você quer fazer isso, como você vai aplicar na regra de negócio depois do lugar onde você tiver trampango. Mas basicamente a gente vai tentar fazer um put normal igual todos os outros que a gente fez no teste. Só que 31 minutos depois. E 31 minutos depois tem que dar não autorizado.

**[00:42:59]** Validate credentials. Massa, né? Mario, muito obrigado, mano, pelo teu super chat, ó. Beijo pra ti, mano, isso me ajuda demais. Vamos ver o que vai acontecer agora? Agora chegou a hora de a gente rodar esse teste. Vamos rodar. Task test. Ih, quebrou. Olha o que ele deu aqui. Test talking, expired after time, né? Que é o nome do teste que a gente deu. Me empolguei aqui, né? Mas é o teste.

**[00:43:36]** que vê se o Tolkien foi expirado depois de um tempo, o teste falhou. E ele deu um erro muito maluco aqui. Olha o tamanho do erro aqui, é difícil até de ler. Aí ele viu todos os dados que a gente tinha aqui, beleza. Aí no final ele falou o seguinte, ó, quando a gente foi testar a expiração do Tolkien, ele falou, olha, deu erro, porque a assinatura está expirada. Isso aqui não pode acontecer, né? Deu um erro, mas a gente não queria esse erro, né?

**[00:44:10]** Isso é porque o nosso código não implementa essa verificação lá no security, não é? Vamos lá, vamos lá. Best API zero, security. Aqui, onde a gente valida, o current user, a gente prestou aqui, a gente viu só se dava erro de decode, mas a gente nunca viu se...

**[00:44:38]** se tinha explodido o tempo. E é exatamente aqui que ele vai cair, né? Deixa eu colocar um Except genérico aqui e colocar um Breakpoint. Só pra gente ver o que aconteceu aqui. Eu vou colocar Except Exception SE, porque pra gente poder validar essa exceção aqui dentro, né? Então eu vou colocar aqui E, só pra ele não ficar enchendo meu saco ali. Legal, aí ele vai cair lá nesse...

**[00:45:07]** Aqui, a gente está bem nesse teste, que é o teste token expanded after time. Então, eu vou dar um L e L, a gente viu que está aqui. E qual que é a exception que ele deu? A exception que ele deu? Olha, estourou essa exceção aqui. Expired Signature Error. Ou seja, a assinatura do token já está invalida. Passou o tempo de validar de dela. E como é que a gente vai resolver isso aqui? Para não explodir um 500 na nossa aplicação, a gente vai ter que tratar esse erro aqui, que foi um erro que a gente não tratou.

**[00:45:35]** que é colocando mais um exception para isso aqui, né? O Expoinered Signature Error. E vamos lá? Então a gente troca esse exception daqui, a gente vai tirar ele daqui, a gente colocou só para brincar, né? E aí de onde vem isso aqui, né? Ele está lá no JWT. Então vamos importar ele lá da bibliotequinha do pai JWT aqui. A gente tem aqui o Expoinered Signature Error.

**[00:46:09]** Ele vem daqui, do JWT, só pra ficar certinho pra que a gente vai a venda depois. Então, Xpire de Signature Error, e a partir disso aqui, a gente retorna o erro, de fato. E qual que é o erro que a gente precisa retornar? É o Rising dos Credentials, não? Então, aí, agora a gente tem um erro. Pra quando decode derrado, se jogue mandar um Tolkien que não tem nada a ver com nada, mas a gente tem um erro pra quando o Tolkien inspirar também.

**[00:46:41]** Você viu que a gente inverteu a lógica da implementação, né? Aqui, a gente geralmente escreve o código, nesse curso, a gente geralmente tá escrevendo o código, depois a gente testa. Aqui a gente foi caçar o bug no teste pra ver como ele se comportava na aplicação. Mas é uma forma diferente, né? De tentar entender isso aqui. É o que a gente chama de Test Driven Development, né? Que é escrever o teste, o teste quebra o código e a gente arruma o código depois. Caio, muito obrigado por tu super chat, mano.

**[00:47:10]** Pra Coquinha valeu, ó. Beijão. Obrigado demais. E é isso, eu fiz sentido essa implementação aqui que a gente fez. É meio maluca, vai e volta, para o tempo, depois anda o tempo pra frente. É back to the future mesmo, né? Agora vamos rodar o teste e ver se ele passa, né? Yay! Olha que massa. Aí agora a gente tem a cobertura desse caso também aqui, né? Que é o caso da assinatura aqui. Cadê, cadê, cadê, cadê? Aqui no security.

**[00:47:49]** Tá passando aqui, ó. Expand Signature Error. A gente conseguiu reproduzir o erro de quando a assinatura inspira. Pô, legal demais, legal. Pô, o Freezi Gun é sensacional. Vocês conheciam o Freezi Gun? É um maluquice total, né? Vai e volta no tempo, aí para o tempo, indo do tempo para frente. E é muito maluco, né? Mas é muito divertido. Legal, vocês gostaram? Já tinham usado o Freezi Gun? Me respondo aí.

**[00:48:23]** Enquanto eu vou começando o próximo tópico aqui. Bom, beleza. A gente resolveu esse problema aqui, né? Do Tolkien parar de valer. Mas se o Tolkien parar de valer, eu tenho que poder renovar o Tolkien, né? Se não, a coisa fica maluca, né? Ah, não, pera. Tem outras coisas que a gente não testou aqui, né? A gente vai pro refresh do Tolkien na parte 5. Desculpa, me confundi aqui. A gente vai ver problemas de autenticação, que são coisas que a gente ainda não resolveu. Conheci aqui o Freeze Gun. Pô, muito legal.

**[00:48:58]** Então, a gente ainda não tem testes que cobram os casos onde a senha está errada. A gente não fez esse teste, né? Tipo, a gente vai fazer o login, né? E o login, ele cai aqui no Verify Password e dá errado. A gente não fez esse teste, né? Que é lá no Alphi, né? Aqui, ó. Isso aqui, não está testado, né? Se a gente for olhar lá no Coverage...

**[00:49:38]** lá no Alf, a gente não tem essa validação, né? Se não tem password, se o password não bate. E a gente também não viu, né? Um login tentado usar um usuário que não existe, né? Outra coisa que a gente também não cobriu aqui, né? Então, a gente pode brincar com esses conceitos aqui, né? Então, sem correta e o e-mail que não existe. Pra gente cair naqueles pontos lá, né? É bom testar, né?

**[00:50:07]** Bom, testar a senha incorreta é super simples, né? Olha que legal, a gente vai fazer um login, a gente chama o user, só que na hora de passar a senha, a gente passa a senha errada. É o mesmo teste do certo, né? Do token, da validação do token, né? Que é o create token. Não tá no security, pera aí, ele tá no test off. Aqui é na obtenção do token, né? É o mesmo teste.

**[00:50:40]** Só que o que vai mudar, em vez de a gente fazer um post com os dados corretos, a gente vai mandar o formidenta, os dados errados. Simplão, aí a gente vai ver se dá errado. Se ele vai dar bad request, que é o que tem que retornar aqui, pera, aqui, o coverage. Que é o que vai ter que retornar aqui. Vai ter que ser anautorized, não a bad request que a gente mudou isso no decorrer do curso, mas é isso. Vamos copiar? Pô, é simplão, esse teste é bobo de fazer.

**[00:51:15]** ao invés de bad request, ele vai dar unauthorized aqui, ou seja, não tem permissão para fazer o login, por que? Porque a senha está errada. Pô, legal! Sim, pronto, vamos rodar. Passou também. Maço! Esse aqui foi mais fácil, né? Esse aqui não tem nenhuma loucura, não tem para o tempo, não gera um user maluco. A gente já tem o user na base e passa a senha errada.

**[00:51:54]** Se a gente olhar lá o covers, em teoria, essa parte aqui do Verify Password agora tem que estar coberta. Olha que lindo, maravilhoso, maravilhoso. E aí, agora a gente vai para o user. E o user, ele é mais simples ainda, né? Porque é só passar um user que não existe. Aí a gente nem precisa criar um user, né? Aí a gente só usa o cliente mesmo e tenta passar um username, no user no domain, aqui eu coloquei só de pirrassa, e...

**[00:52:26]** O password de teste teste. É o password até que a gente costuma usar na fixture, mas o user não existe. Simplom, o erro aqui não vai ser bad request, vai ser unauthorized. Unauthorized. Pô, legal! Simplom, vamos ver se a gente consegue cobrir aquele outro cenário ali? Yay! Pô, legal! Ó, cobrimos tudo isso aqui, né? A cobertura...

**[00:53:06]** Cobertura tá bala aqui nesse código, 95% de cobertura? Pô, muito legal. Aí alguém deve estar se perguntando sobre o database, né? A gente não fez nenhum teste que cobre o database, né? Aproveitando que eu tô falando de cobertura de teste, eu vou... falar sobre isso aqui. Você tá vendo que a gente nunca usa esse bloco de código? Só aproveitando que a gente tá aqui, nem tá no escopo da aula, mas eu vou falar sobre isso, porque algumas pessoas podem ter dúvidas sobre isso em algum momento.

**[00:53:47]** A gente nunca executa essa função, né? Porque sempre que a gente executa, sempre que a gente teria que executar o getSession, a gente tá trocando ele por esse session aqui, né? Aqui, ó. Esse aqui, né? A gente troca pelo session de test, né? Então aquele código nunca vai ter cobertura. E aí, como é que a gente faz, né? A cobertura tá melhor do que o sinal aqui, mano. Ah, vocês são bovos, né, mano?

**[00:54:26]** Aí tem uma coisinha aqui no Python, que a gente pode falar de que a gente não vai cobrir um determinado bloco de código, né? A explicação que a gente pode dar aqui nos Atabase, a gente pode colocar aqui um comentário que a gente vai chamar de pragma. E a gente vai falar, noCover. Ou seja, esse bloco de código não vai ser coberto. Eu não sei se tem esse traço aqui, eu acho que não. Eu acho que é só assim, noCover.

**[00:54:55]** Vamos rodar de novo agora e ver o que acontece, deixa eu tirar daqui, deixa eu rodar lá no grande. Ah, tá, beleza. Todo comentário tem que ter dois espaços. Ó, agora está aqui ó, 100%. Porque assim, esse código não é coberto porque a gente não usa ele no teste, né? Então, o que tem que colocar é esse aqui ó, espaço, espaço, espaço, espaço, pragma, dois pontos no cover, para falar que isso aqui não vai ser coberto. Massa?

**[00:55:36]** Não botem isso no código todo, a gente só vai botar aqui porque isso aqui impacta na nossa cobertura. Aí a gente tem o security, alguns blocos que eram exercícios e tem o users que também são blocos de exercícios. Então não é que eu dei uma roubada, é que a cobertura não se aplica aqui, por isso que a gente coloca no cover, porque a cobertura não se aplica a esse bloco de código.

**[00:56:01]** Tipo assim, esse bloco de código nunca vai ser coberto, porque ele essencialmente é substituído na hora de injetar a dependência. Já falou, não vão fazer gato no código para falar que a cobertura está alta, não é esse o objetivo, é para blocos onde não vai ser coberto nunca. Legal? Aí agora a gente vai resolver o esquema do Tolkien, eu devia ter invertido a ordem dessa aula que me confundia.

**[00:56:29]** O refresh do Tolkien, a ideia dele aqui, é que a gente tenha basicamente aquele fluxo, eu queria deixar o fluxo aqui mas não tem.

**[00:56:39]** um fluxo que a gente vai poder passar lá no alf onde a gente vai receber o token e a partir do token ou seja o token que é válido a gente vai gerar um novo token ou seja a deu 28 minutos que eu estou usando mas eu vou continuar usando então a partir do meu do meu JWT eu vou mandar uma requisição para aplicação e a aplicação vai me gerar um novo token que vale de novo por mais 30 minutos

**[00:57:07]** Ou seja, eu evito de ter que ficar trafegando o uso aresenha toda vez. Então eu uso o meu Tolkien. Isso é mais legal quando a gente pensa em tokens de longa duração, né? Tipo assim, ah, é um Tolkien que dura, sei lá, um mês, saca? Mas é interessante vocês entenderem como é que funciona essa lógica aqui. Também não tem nada de muito mirabolante, né? Se a gente for parar pra pensar...

**[00:57:33]** É um endpoint que vai ser barra-alf-refresh-token. A gente vai pegar o get corrente-user que a gente já definiu lá atrás, vai dar o responso de modo do token que a gente já fez no outro endpoint também, e a gente vai simplesmente chamar um novo token pro-user que a gente já tinha aqui, que já estava logado na aplicação. Pô, é simplão, né, o refresh. A gente vai adicionar ele lá no alf. Então aqui a gente tem o...

**[00:58:11]** Logging for access token, né? E agora a gente vai implementar esse aqui, que é o refresh. Uma coisa interessante aqui é que você tá vendo que esse aqui não tem o... o... o current user, né? A gente não importou ele aqui, porque aqui é onde a gente gera o current user, né? Então a gente nunca usou ele aqui, então vamos importar. Então, security... Vamos colocar bonitinho aqui. Get current user.

**[00:58:54]** E aí é bem simples. A gente pegou o user que já estava validado, que já tem um token que já existe e vai dar um novo token para ele, para ele poder chamar de novo. Sim prão. Nada demais aqui. Aí a gente precisa testar isso aqui, obviamente. E aí como é que a gente testa? Basicamente a gente tem um token que já é válido e a gente envia para lá e tenta dar o refresh desse token que a gente não tinha ainda. Vamos...

**[00:59:32]** mandar um post para esse endpoint refreshToken com alguém que tem um token válido. A gente já criou o user. Eu nem sei por que eu coloquei user aqui. A gente nem precisa do user aqui. A gente só precisa do token. A gente chama o token. Beleza. Passou aqui. Pegamos o data e vimos se a resposta dele veio 200. Se tem um accessToken.

**[01:00:02]** Se o token type é bare token, se veio a resposta e a gente vê se o tipo do token é bare token, que é o que a gente combina, que vai retornar aqui no esquema, né? É a mesma coisa do de cima. E a gente pode usar bem maiúsculo para padronizar, né? Para ficar igual, ficar mais simples. Pô, sim para um esse teste também, né? Você viu que depois que...

**[01:00:34]** Você viu que depois que as coisas vão encaixando, né? Tipo, depois que a gente constrói... Essa aula é mais sobre isso assim, né? Você viu que depois que a gente constrói um certo fundamento aqui, né? Dentro da aplicação, a aplicação vai fluindo, né? Tipo assim, a gente acabou de inserir um novo recurso na aplicação e esse recurso não precisou de muita coisa, né? Porque a gente já tinha a forma como pegar o usuário, a gente sabia. Depois...

**[01:01:05]** Se a gente fizer a coisa desamarrada, tipo assim, com injeção de dependência, cada coisinha no seu lugar, que a gente refatorou o sistema, pô, depois as coisas vão se encaixando de um jeito tão bonitinho, né? Tipo, não precisa de muito esforço, né? Ah, obrigado, MDR. Um beijo aí pra você, espero que esteja gostando. A gente não precisa de user aqui. Beleza, vamos rodar? Vê se funciona. Ah, olha o que que ele deu aqui.

**[01:01:37]** Fast 002, ou seja, se for injetar dependência, use annotated, né? Lembra? A gente aprendeu isso na aula do Refactor. Então, isso aqui é pra usar assim, né? Anotated. Ó, que massa! O linter funciona, mano! Passou! Legal! Ó, e aí aqui o ALF tá 100% coberto de novo. E ó, lindinho, né? Funciona bem!

**[01:02:14]** Aí uma pergunta que você pode estar se fazendo é a seguinte, e se eu tentar chamar o refresh depois do Tolkien tá inválido? Ou seja, depois de 30 minutos eu tento renovar o Tolkien. Isso não pode acontecer, né? Aí a gente tem que ter um ponto aqui, né? Uma coisa interessante aqui. Esse teste, em específico, ele não precisa ser feito. Mas aí a gente vai ter uma discussão aqui.

**[01:02:47]** A gente vai mandar um post para o token, gerar um token, depois a gente vai pedir um refresh token, aí você vai falar, beleza! Esse é um teste importante, né? Garante que a pessoa não vai conseguir dar o refresh do token depois. Só que lembra que a gente está usando a mesma função getCurrentUser aqui e a gente já validou se isso aqui funciona, o expiredSignatureError. A gente já tem isso validado.

**[01:03:18]** E por que que a gente vai fazer esse teste então? Se o teste testa a mesma coisa do teste de cima. Vou contar um segredo aqui. Hoje. Hoje. Hoje. Esse código usa o mesmo teste. Esse código usa o mesmo bloco do current user. Mas pode ser que amanhã ele não use mais. Saca.

**[01:03:47]** Pode ser que as coisas mudem, o código mude, pode ser que a gente tenha implementado errado sem o getCurrentUser. Saca? Então é interessante a gente validar esse fluxo. Porque as coisas mudam e a gente tem que garantir a integridade das coisas que a gente definiu. Mas em teoria, o teste vai passar pelo mesmo lugar, vai cair no mesmo lugar que o outro teste que a gente já tinha feito. Mas é importante a gente fazer isso. Ah, redundante. É. Mas... É hoje. Amanhã pode anunciar.

**[01:04:21]** Saca, faz sentido isso que eu estou falando? E eu vou usar até as mesmas datas que a gente usou naquele dia aqui. O dia 31 do 2 aqui. Muito bom o comentário. Mesmo que o teste pareça redundante, teste é teste. Tem que ser feito. Exatamente.

**[01:05:03]** Porque, tipo assim, hoje está funcionando, né? Amanhã, se a gente mudar um bloco aqui e falar, putz, não vamos mais ocorrer de user porque a gente pode fazer um negocinho aqui, a gente nunca mais sabe se está funcionando. Esse teste é exatamente o teste de anterior, né? Que cria o Tolkien e faz o... o push, o put, né? Para garantir que o Tolkien está inválido. Mas agora, a gente está usando o refresh do Tolkien para validar isso aqui. Se o refresh não pode acontecer depois de um tempo.

**[01:05:33]** Beleza, a gente sabe que vai passar, a gente já sabe que isso está testado, mas no dia de amanhã não saberemos se isso aqui vai estar funcionando, então é interessante garantir que a funcionalidade funcione da maneira que a gente quer. Mas aí você pode até se perguntar, mas eu não posso fazer um que para no tempo e valida o token dentro de cinco minutos? Posso, mas esse teste vai ser exatamente igual a esse aqui, né? Tipo assim, esse crio token

**[01:06:03]** E depois ele tenta dar um refresh com poucos milissegundos de diferença, mas é dentro do tempo hábio. Então, tá funcionando já. Massa? Acabou que eu tinha para falar hoje. Por que que acabou que eu tinha para falar hoje? Ah, interessante, fizeram uma pergunta aqui. Deixa eu finalizar aqui e aí eu respondo todas as perguntas. Massa? Ó, o Endpoint de PuT usa dois users criados na base de dados.

**[01:06:44]** Porém, até o momento ele cria um novo user no teste via request de API por falta de uma feature de order user. Atualize esse teste para a nova fixture. Tem um teste que ficou para trás. Lembra que a gente criou dois users lá atrás. Aqui precisa corrigir isso aqui. Legal? Tem o quiz dessa aula. Então...

**[01:07:24]** respondo o quiz, tá facilitando pra gente? Não, não tô facilitando. Eu tô sempre querendo abrir um espaço pra gente poder conversar aqui, né? Porque senão depois a gente fica nesse bagulho, pô, não dá pra tirar uma dúvida, porque a aula foi até o momento máximo do que dava, né? Aí eu vou fazer o comedy aqui, já vou copiar tudo de uma vez já, implementando o refresh do Tolkien, os testes de autorização, gitpush, tá lá no repositório.

**[01:07:58]** Agora, eu quero conversar com vocês e entender se vocês têm dúvidas sobre o que aconteceu aqui. Eu sei que na hora a gente vai tipo assim, pô, mas o FreeZTime já passou bolado, funciona. Agora é o momento de vamos trocar uma ideia sobre isso aqui.

**[01:08:18]** Ó, o Rafa mandou uma pergunta aqui, que é o seguinte, ele falou o seguinte, faz sentido criar um arquivo separado com dados pra teste, datas, tokens e senhas? Tipo assim, você quer criar um arquivo separado pra cada coisa dessas? Então, é que aí você tá pensando na estrutura, né? Tem não que é recorde pra fazer o PIX, mano, é PIX... PIX.DUNOSAURO, a rouba...

**[01:08:53]** gmail.com, entra aqui, está tudo aqui. Aí você clica no PIX, você chega lá, está aqui na frente, clica no PIX e vai aparecer a chave aqui. Então, faz sentido criar um arquivo separado para dados, testes e dados? Então, a questão é o seguinte, você está pensando na coisa como estrutura e testes, geralmente, não validam estrutura, eles validam comportamento.

**[01:09:33]** Ah, tipo um teste config, teste JSON, não mano, isso não faz sentido. Agora eu entendi o que você tá falando. Tipo, criar uma coisa de teste fora do teste, não mano, não faça isso, tá ligado? A ideia disso é fazer o seguinte, quando a gente escreve o teste, a gente tem que saber porque o teste quebra. Mas, então a ideia principal do teste

**[01:10:06]** é que testes tem que quebrar. O objetivo, toda vez que um teste quebra, é ótimo. Alguém fala, pô, teste quebrando é bom? Claro que é bom, porque significa que você não deixou o bug ir para a produção quando o teste pega o comportamento que tem aqui. Só que aí, o teste tem que ser fácil de ler.

**[01:10:30]** Você tem que bater o olho no código daquele teste. Essa é uma das premissas básicas ali. Você tem que bater o olho no teste de um arranjo acerte, saca, o acte. Eles têm que fazer sentido. Eles têm que estar ali na sua cara. Você olha aqui e fala, ah, é exatamente isso aqui. Porque se você esconde esses dados, os testes ficam mais difíceis de ver.

**[01:10:59]** Saca, e a ideia do teste é que um teste, eu posso até mostrar isso aqui, né? O teste seja um ciclo positivo de feedback. Peraí, eu tô digitando, mas eu tô abrindo aqui. Eu não sei se eu vou achar isso aqui. Eu acho que talvez no Google eu acho mais fácil. Peraí. Eu não sei se eu vou achar isso aqui.

**[01:11:35]** Mas a ideia é que sugere um ciclo positivo. Seja fácil, o teste dele tem que ser rápido de executar, ele tem que ser rápido de depurar, ele tem que ser rápido de escrever. A ideia é que a gente consiga ver isso de uma forma muito dinâmica assim. No livro do Kent Beck, que é o criador do TTD, o Kent Beck é Beck com E.

**[01:12:03]** Ele tem esse livro aqui que é o Test Driven Development by Exemple. É um livro muito legal, é o livro que traz as técnicas de TDD e tudo mais. E uma das dos padrões que ele vai falar sobre isso aqui é o ciclo de feedback. E aí a ideia do ciclo de feedback é que as coisas sejam rápidas de visualizar. Então o teste tem que rodar rápido, porque se o teste demora, você não roda toda hora. Saca, você viu aqui quantas vezes a gente rodou o teste? Deixa eu ver assim.

**[01:12:33]** Olha o tempo que roda o teste. Blum, acabou. Saca, se eu não tivesse estrimando, o teste rodaria mais rápido. Mas, pô, 17 testes passaram em 2 segundos. Sacan.

**[01:12:47]** Então, os testes têm que ser rápidos de executar, eles têm que ser rápidos de depurar, porque se o teste é difícil de entender, quanto mais difícil, imagina, sabe aquele bloco de código que ninguém mexe? Vocês já passaram por isso? Tem um bloquinho de código que fala, tipo assim, tem um comentário assim, não mexe aqui que dá ruim, tá ligado? É geralmente um bloco de código que não tem teste, geralmente é por aí. Mas tipo assim, quando o código, a gente começa a esconder coisa,

**[01:13:17]** Tipo assim, ah, isso aqui eu vou botar num arquivo. Aí amanhã o arquivo não está dentro do código de teste. Tipo assim, não é hard coded, não é o nome do username dentro do teste. Aí você vai lá e muda o arquivo. Aí você comita esse arquivo e de um dia para o outro o teste para de passar, mas não teve nenhuma alteração nem no código e nem no teste.

**[01:13:46]** Como é que você debura, depura isso, né? Como é que você vai debugar isso? Como é que você vai saber que essas coisas estão se transformando em determinados pontos? Então a ideia é que seja explícito o arrange, o act, o assert, eles estejam ali escancarados no teste. Saca. E aí se as coisas tiverem escancarados, elas são fáceis de resolver, em teoria elas têm que ser fáceis de ler, pra gente poder ir fazendo isso...

**[01:14:17]** de forma mais intuitiva. Então, toda vez que a gente roda, a gente tem um feedback. Feedback é sempre positivo. E quando ele quebra, é bom que quebre. A gente não quer enigmas. Saca, aquele meme... Ainda bem que eu sei ler hierógrafos, tá ligado? Você não quer isso quando você tá trabalhando com testes. E os testes aqui, uma outra coisa que vale a pena falar... A gente não teve muita oportunidade pra conversar sobre essas coisas dentro do curso, porque o curso é...

**[01:14:45]** Dali, dali, dali, né? Mas uma das coisas de escrever testes, né, é que os testes modelam a forma como o código é escrito. Então, tipo assim, ah, se o código é muito esquisito, o teste começa a se tornar muito esquisito.

**[01:14:59]** E quando é difícil de testar, é difícil da gente entender o que está acontecendo, saca? Então, um teste difícil significa um código difícil, e esse código difícil vai refletir em todo esse ciclo de feedback de novo. Pô, eu não vou mexer nesse código, porque pra eu mexer nesse código eu tenho que mexer no teste, aí o teste é meio esquisito, e aí tem um arquivo dentro do teste que importa, não sei o que, que leia uma outra coisa lá de fora, saca? Então, não faz muito sentido. Se você precisa trabalhar,

**[01:15:28]** com uma massa de dados e tudo mais, a ideia...

**[01:15:32]** é trabalhar com randomização, porque dentro da randomização você não consegue, a ideia é que você não consiga tirar as coisas de lá de dentro, né? Então, por exemplo, a gente, eu recomendei que assistisse a Live 281, que era a lição de casa da aula passada, né? Então, Live de Python 281, é, escrevi tudo, camelcase aqui, mas tudo bem. Live de Python 281, se eu não me engano é esse, esse é o número.

**[01:16:02]** Aqui ó, lives anteriores. 2.8.1. Ah, não é não. Ah, é 2.8.1 mesmo. Que é essa aqui, da randomização de dados. Então, se quiser dar uma olhada, é super interessante o funcionamento dessa coisa aqui que se chama randomização. Aí você fala, pô, eu preciso gerar um dado, aí como é que eu vou fazer, né? A gente tem várias bibliotecas para fazer isso. A gente viu o Factor Boy hoje, mas a gente tem coisas como o Faker. Eu uso exemplos do curso de Fast API aqui.

**[01:16:36]** Aqui está com My Meses. Eu gerei uns factors muito malucos aqui pra gente ver. Aí, por exemplo, ó, você tem dentro do Faker, você tem coisas desse sentido aqui, né? Ah, você precisa de um nome? Então eu vou gerar um nome pra você, um faker name.

**[01:16:56]** Ah, você precisa de um username? Beleza, vou gerar um username pra você. Você precisa de um e-mail? Eu vou gerar um e-mail pra você. Então, meio que a ideia é que você não esconda dados de preferência randomize isso aqui, né? Import, sei lá. From Faker, import Faker. A gente tem, sei lá, F, que vai ser o Faker. A gente pode chamar Faker.username. Aí você tem o Rebekah00, Christopher11.

**[01:17:27]** Semptors. Saca, eu preciso de um name. Legal. E aí dentro disso aqui, você tem uma tonelada de coisas aqui que você pode chamar disso aqui. Você pode pedir um ano, um zip code, que é um SAP. Você pode randomizar um monte de coisas, um monte de coisas. Ah, IPv4. Quero um IP randomico. Então, saca, a ideia é que o teste tenha esses dados.

**[01:18:04]** Aí você fala, pô, porque são dados difíceis de gerar. Então aí você tem o factor boy, né? Que ele vai montar uma estrutura bem mais complexa desse tipo de coisa aqui. E aí você pode randomizar as coisas também, né? Cadê aqui? Ok.

**[01:18:24]** o meta aqui, você vai falar um faker FirstName, LastName, DateObject, e aí você vai montando essas coisas e concatenando para criar um objeto grande, um objeto robusto, que tem esse tipo de coisa que você quer, né? Então, meio que a ideia do teste é nunca criar uns arquivos malucos daqui. Aí você tá vendo? Ele foi gerando uns faker muito maluco aqui pra gente, aí você pode gerar faker localizado, né? Tipo assim, de onde vem, pra onde vai, tudo mais.

**[01:18:54]** Então, a gente tem essas opções e isso tem que ser aproveitado, né? Mas assim, aí a gente vai pegando esses dados randomizados e vai gerando os testes a partir disso. A gente nunca esconde dados, a gente vai gerando novos dados a partir disso aqui. E aí com isso tem alguns testes que são tipo levados às últimas consequências aqui, né? Tipo assim, a gente tem o...

**[01:19:21]** é lives aqui a gente tem o outro live que eu fiz mais pra frente que é o hypothesis aqui né que é tipo assim o esquema de randomização levada ao extremo sabe tipo assim ah roda uns dados randômicos aí com umas primitivas aqui ó vai rodar esse teste quantas vezes eu quiser o inteiro aqui ó o inteiro vai ser menos sem o máximo vai ser

**[01:19:50]** 500 e tal, e aí você vai rodar esse test 50 vezes, variando os valores e tudo mais. Tem algumas coisas de Proper Basis para o Fast API também. A gente acabou não falando nessa live, mas é possível fazer isso também. Então, tipo assim, nunca fique nessa pira de esconder coisas, deixem as coisas no próprio código mesmo. Paz o que dá. É a melhor forma de resolver esse tipo de problema. Eu não sei se eu respondi à pergunta.

**[01:20:19]** Eu sei que eu não fui direto na resposta, mas é porque tinha uma coisa que a gente podia aprender aqui dentro desse esquema. Então, saca, sempre que possível, crie coisas assim, que você sabe onde está, você sabe como foi gerado, você pode vir aqui buscar o dado de volta, saca? Em vez de esconder arquivos e estruturas, saca? Nunca é uma boa ideia. Pô, valeu aí Impact.

**[01:21:01]** Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu... Pactu...

**[01:21:25]** A gente vai conversar sobre vários pontos de randomização aqui, porque a gente vai criar um studio list aqui que tem título, descrição, e aí são dados que são mais complicados de gerar no teste 1, teste 2, teste 3. A gente vai criar uns factors mais legais pra isso. Aqui são factors com um texto fake, um choice e várias outras coisas. Então na próxima aula a gente vai mexer com isso de novo.

**[01:22:10]** Massa, aí, antes de a gente fechar, queria saber, vocês têm mais alguma pergunta e tudo mais? E o WhatFallow que fez um, fez um pix aqui pra mim, obrigado, mano, ó, valeu aí. Vocês têm mais alguma pergunta, alguma coisa que vocês gostariam de trocar a ideia e tudo mais? Aproveita que eu já acabou bem mais cedo. Se não, a gente vai jantar, vai fazer as coisas. Que a manhã é quarta-feira, hein? Eu sei que tem um delay aqui, né?

**[01:22:51]** Mas então qualquer coisa vocês perguntem lá no grupo, a gente vai trocando mais ideia, conforme for sendo necessário e vamos descansar. Beijinho pra vocês e até quinta a gente vai falar sobre, a gente vai construir, né, o esqueminha de tudo list, tudo list, né, tarefas a fazer pra gente relacionar esses, as coisas e tudo mais. Então é isso, beijinho pra vocês, a gente se vê quinta-feira. Tchau, tchau.

