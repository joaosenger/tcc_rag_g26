# Transcrição da Aula: aula-06.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:03]** Olá, pessoas! Boa noite! Eu sou o Dono Sauro, ou bom dia, boa tarde, né? Se você estiver vendo isso depois. Olá, boas-vindas a mais uma aula do nosso Curso de Fecha API. Eu conto com vocês, né? Para vocês me darem aquele feedback que vocês estão me ouvindo, vocês estão me vendo, só para saber se eu não estou falando sozinho, né? Tipo, assim, aquele papo de maluco. Às vezes eu fico cinco minutos falando sozinho e quando eu vi, não dá transmitindo nada, né?

**[00:00:29]** Então, bom, pra gente conversar um pouco hoje, a gente vai falar nessa aula, né, sobre autenticação e autorização. Aí eu já quero perguntar pra vocês logo de cara se pra vocês esses termos significam alguma coisa, né, tipo assim, por autenticação, autorização, ovo bem, achei sensacional.

**[00:00:50]** Então, legal, dá tudo certo. E perguntar para vocês se a autenticação e autorização dizem alguma coisa para você, tipo assim, se vocês estão acostumados, ele dá com esse termo e tudo mais. Bom, para quem quiser o link dessa aula em texto, sempre é bom dizer, ele está aqui, aí, se quiser acompanhar por texto ou ir fazendo, copiando códigos, exemplos, eles estão todos lá. Então, legal, na aula de hoje a gente vai falar...

**[00:01:18]** De forma geral, assim, sobre coisas de segurança, eu vou dizer assim, mas entre aspas. A gente vai conversar, conversando sobre armazenamento seguro de senhas, que é uma coisa que a gente ainda não fez. Toda senha que a gente persiste, a gente salva no banco, ela de forma limpa, né?

**[00:01:35]** O que é um problema? A gente vai falar sobre autenticação e autenticação é basicamente quando você precisa conversar com alguém e você sabe, você vai num prédio e esse tem que dar seu documento, falar assim, essa pessoa sou eu, né? Então é aquilo que avalia suas credenciais, né? Então quando a gente tá falando de autenticação, a gente tá falando sobre isso. Como dizer que eu sou eu mesmo, né? Sei lá, às vezes a gente pensa em biometria, digital...

**[00:02:02]** fácil ir e sabe esse tipo de conhecenha tokens e tudo mais. Então é sobre isso que a gente fala sobre quando desautenticação e autorização é sobre a partir de quem a gente é na aplicação se a gente pode fazer alguma coisa ou não questão de controle de acesso. Eu não posso.

**[00:02:23]** deletar a senha do coleguinha, sei lá, o cacaroto está aqui, que foi a última pessoa que comentou, eu não posso alterar a senha do cacaroto, não faz sentido em meio dele, sabe? Não, sabe? Então, é sobre isso. E para essas coisas acontecerem, a gente vai ter que mexer bastante com testes e bastante com fixtures, colocar algumas coisas, umas regrinhas aqui, outras ali, para a gente poder ir vai passando esse tipo de coisa. Então, é sobre isso que a gente vai falar nessa primeira aula.

**[00:02:51]** Bom, o primeiro tópico, que é o armazenamento de senhas seguras, a gente tem alguns problemas que são relacionados a isso na aplicação de uma forma geral. Por exemplo, quando a gente pensa em...

**[00:03:09]** armazenar senhas, né? A gente tem que ter algumas coisas em mente, né? A gente pode armazenar a senha pura dentro do banco, mas pensa que isso aqui é um é um problema de segurança e quando eu digo isso nesse primeiro momento eu não tô dizendo externo, mas interno. Imagina que quem tem acesso ao nosso banco, a gente mesmo ou o time que tá desenvolvendo essa aplicação

**[00:03:34]** a gente pode ver a senha, né? O que é um problema, né? Então imagina que você tá mexendo lá e aí você olha o banco de dados, vê a senha de todo mundo, isso é muito complicado, né? Tem o segundo ponto, que é o ponto de erros eventuais, né? Imagina que sem querer você bota lá no esquema que vai sair a senha, sabe? Sem querer você bota password lá no esquema do pai idêntico, e aí a senha da pessoa tá exposta.

**[00:03:56]** por algum motivo. Isso é um problema. A gente tem esses erros eventuais e as nossas próprias seguranças, como pessoas que estão desenvolvendo a aplicação de não ver a senha dos outros, o que é bem esperado. É óbvio que a gente não deveria ter acesso a isso, principalmente porque as pessoas costumam usar a mesma senha em vários lugares, o que é um problemão.

**[00:04:19]** A minha senha é batatinhas 1, 2, 3. É a senha no Facebook, no Instagram, no Twitter, no Google. Essas coisas acontecem normalmente. Então é esse ponto aqui que é um problema.

**[00:04:33]** E o segundo é um problema externo, né? Que eu gostaria de dizer, né? Caso alguém consiga acesso ao nosso banco de dados, sei lá, um Shell Reverso, alguma coisa, sei lá, que alguém consiga invadir a nossa aplicação, porque tem que pensar sempre nisso, né? Nem tudo é seguro. Então, as pessoas podem associar, né? Alguns dados nós, tipo, vazamento de dados, né? Isso sempre acontece. Então, eu posso pegar alguns dados meus, tipo assim, sei lá.

**[00:04:59]** Meu e-mail e minha senha. Se eu usar senha em vários lugares, caso a minha base de dados base, isso vai ter um problema muito crítico. E aproveitando que a gente está falando sobre isso, eu não sei se todo mundo conhece, né? O Have I Been Pwned, né? Tipo, que é um site muito legal, que mostra se você pode o seu endereço de e-mail e ele mostra em que bases de dados seu e-mail já vazou, né? Por exemplo, lá Eduardo, ArrobaGmail...

**[00:05:26]** esse não é meu e-mail, mas é só pra gente ter uma coisa pra olhar aqui, né? Então, vai olhar que já vazou 138 vezes aqui o Eduardo ArrobaGmail.com, né? Alan Starlogs aqui em fevereiro de 2025, Speedio, Fipaclip, sei lá, mais um monte de outras coisas, Hot Topic...

**[00:05:50]** French citizens, tá vendo? Então bota teu e-mail aí, né? Eu não vou colocar o meu porque se não vocês vão ver onde o meu, onde o meu e-mail vazou, né? Mas é nesse sentido, o trelo já teve vazamento, então isso é muito comum de acontecer vazamentos de base de dados, né? Então bota seu e-mail aí, dá uma olhada e aí tipo assim, geralmente nunca vaz a senha, né? Porque a gente tem pelo menos um mínimo de segurança a partir dessa senha. Então beleza, pode vazar meus dados, mas tipo assim, a minha senha para a pessoa entrar em outros sistemas

**[00:06:21]** Então, por isso que é interessante a gente armazenar a senha dessa forma. Legal. Para a gente armazenar as senhas de uma forma um pouco mais segura, eu vou usar uma biblioteca do Python que se chama PWD Lib. PWD é de password, de senha. Lib é a biblioteca das senhas, né? E aí a gente vai instalar junto com ele esse argontune. O argontune é um algoritmo de hash, ou seja, é uma criptografia de mão única que vai...

**[00:06:48]** pegar os dados que a gente tem, vai gerar a partir de um algoritmo que a gente chama de Mark Dengar, vai fazer várias contas e vai gerar um hash, um numerosão, uma stringzona gigantesca, que a gente não consegue fazer o caminho inverso. O hash é uma criptografia de mão única, então ele só vai. Então é impossível a gente...

**[00:07:12]** do hash, a partir do hash, voltar para a senha pura. Isso pode acontecer em ataques de força bruta, mas isso é muito mais raro e difícil de acontecer. Dependendo da tamanho da senha, dependendo do sistema, dependendo de qual algoritmo, então a gente vai usar o Argon 2. Poderia ser qualquer outro algoritmo, mas escolhi o Argon, porque...

**[00:07:33]** é o padrão da PWD Lib. Massa, então eu vou instalar aqui com vocês, eu já estou no diretório do projeto, dá um pouco outro ad e a gente vai instalar o PWD Lib com o algoritmo de Argon 2. Legal? Então é isso. Então já está aqui no nosso projeto. Massa, temos aqui. E aí, como é que a gente faz isso aqui? Para a gente começar a organizar a casa dentro dessa coisa,

**[00:08:02]** coisas de segurança de uma forma geral, eu vou criar um arquivo chamado security.py aqui. E eu tenho uma mania de escrever ao contrário disso aqui. Sirute, security, saca? Então tem várias formas aqui. Aí perguntaram se eu já usei Bcrypt, sim. Argon é um algoritmo mais moderno do que o Bcrypt em alguns casos, então...

**[00:08:30]** Você pode usar Bcrypt também com a PWDlib, funciona, se você quiser. Então, a gente vai criar esse arquivo novo aqui no nosso projeto, chamado secu-lit-de-segurança.py. Mas aí aqui dentro, a gente vai importar a PWDlib. Então, from-pwdlib, a gente vai importar esse password hash, que é o objeto que gera hashes de senha. E aí aqui dentro desse esquema, a gente vai fazer o seguinte.

**[00:09:02]** A gente vai criar um contexto de criptografia. É bem simples aqui. A gente vai falar password hash e vai ver o que ele recomenda na hora. Aí se ele vai botar salt, que é uma forma de botar mais segurança em cima da senha, a gente deixa a cargo da biblioteca. Eu não quero mexer na configuração padrão dela. Massa. E aí a gente vai criar duas funções. Uma função que vai ler.

**[00:09:31]** a senha limpa e vai gerar o hash dessa senha, que eu chamei aqui de getPasswordHash, ou seja, gera o hash da senha simplona. Eu vou até copiar pra gente não perder tanto tempo. Então a gente vai pegar esse PWD content, vai gerar esse hash de uma senha específica.

**[00:09:52]** E aí a outra é a função que valida, mas pensa que validar a gente não vai decryptografar a senha, a gente vai encryptar de novo e ver se é a mesma coisa. É basicamente esse o algoritmo que a gente usa aqui, que é esse que a gente tem no Verify Password aqui embaixo. Então aqui a gente pega esse contexto que ele definiu aqui, como hash recomendado. A partir disso aqui a gente vai gerar o hash, então...

**[00:10:22]** Isso aqui vai dar pra gente uma stringona maluca. E aí na hora de verificar o que ele vai fazer. Ele vai chamar esse contexto, chamar o verificador, aí a gente vai passar sem a limpa pra ele, ele vai encryptar a senha de novo, né, vai gerar o hash de novo e ver se o hash é igual o hash que tem no banco de dados. O hash que a gente armazenou. Então basicamente essa é a ideia aqui. A gente não vai trabalhar tipo assim, uma forma de...

**[00:10:48]** de criptografar ou deixar limpa senha nunca de forma alguma e é basicamente isso se a gente quiser testar essas funções a gente pode vir aqui e brincar com isso né lá eu vou dar um python menos e deixa eu habilitar meu mente virtual não o outro excel aqui é importante ou você pode dar poetry run python tanto faz

**[00:11:09]** Python-i, aí eu vou lá dentro do meu feste tal e vou chamar esse módulo chamado security aqui dentro. Então a gente abriu shell dentro desse módulo, só pra gente ver o que acontece aqui. Aí eu vou chamar essa função getPasswordHash e vou passar aqui 1, 2, 3, sei lá, batatinhas 1, 2, 3. Essa vai ser minha senha aqui dentro da aplicação. E aí ele gerou esse hash usando argom aqui pra gente.

**[00:11:35]** Então, basicamente, toda vez que a gente for persistir a senha, sei lá, se a senha fosse batatinhas um, dois, três, a gente persistiria a senha dessa forma. Então, ele gerou um hash usando esse algoritmo. Então, a gente pegou, transformou isso aqui, e isso aqui é o que a gente espera que seja persistido no banco de dados, para que a gente nunca vaze a senha limpa das pessoas. Fez sentido isso aqui? Deu para entender aqui o contexto do que está acontecendo?

**[00:12:04]** E aí é outra função que verifica, que a gente chamou de Verify Password. Se a gente chamar o Verify Password e passar sem a limpa, que é o primeiro argumento, e depois o hash, vamos ver o que acontece, então a gente vai chamar o batatinhas 1, 2, 3, e a gente vai passar esse hashzão, que é o que a gente vai colocar no banco de dados, em algum momento. Aí ele deu pra gente true, tá vendo? Ou seja...

**[00:12:37]** Essa senha aqui bate com o hash que tem lá no banco de dados. Se a gente trocar a senha aqui, vamos trocar aqui batatinhas, um, dois, três, quatro, por exemplo. Aí ele deu false, ou seja, essa senha não gera esse hash usando esse algoritmo, então essa é a ideia por trás aqui da coisa. Então, o que a gente vai ter que fazer aqui? Basicamente, a gente vai ter que ir lá no nosso endpoint, onde a gente cria o user, o post, aqui, vamos lá.

**[00:13:08]** onde a gente cria o user e a gente vai alterar de uma forma bem simples. Em vez de salvar a senha, a gente vai salvar a senha com o hash gerado. É isso. E aqui no update, quando a gente altera, se a gente alterar a senha, a gente tem que ter essa coisa de poder alterar a senha também usando o algoritmo de hash. É isso.

**[00:13:31]** Basicamente essa coisa, a gente vai chamar essas duas, essa função agora, getPasswordHash duas vezes, no post e no put. Massa fez sentido, tá todo mundo assim, quietinho, né? Então, não sei se tá todo mundo tendendo as vezes. Tô falando sozinho de novo, caiu a internet. Então, aí o que a gente vai fazer aqui? Eu vou importar lá do security aqui, dentro do app, né? Então, from fest0.

**[00:14:00]** FastAPI0.securet import, a gente vai importar o GetPasswordHash, essa função zona aqui que a gente tinha usado lá atrás. Aí agora a gente vem aqui e onde a gente persiste o usuário, tipo assim, dentro do post a gente pega, vê se tem, a gente vê se já não tem um e-mail, vê se já não tem algumas coisas cadastradas e a gente vem aqui no password e só chama aquela função GetPasswordHash.

**[00:14:34]** E aí toda vez que agora a gente for criar o novo user dentro da nossa aplicação, a gente vai persistir a senha dele em um hash. Aí o Takoni perguntou aqui, seria muita viagem salvar o e-mail em hash? Ah, não necessariamente, mas é que o e-mail não é um dado sensível, né? Tipo assim, meio que você pode até salvar, mas tipo, tem algum ganho de verdade nisso?

**[00:15:02]** Aí o Thiago perguntou, mas como é que você vai mandar os puncher, recuperação de centro? Tem esse ponto também, né? E aí aqui, primeiro a gente vai colocar aqui no post, né? E aí agora a gente vai vir aqui, vai colocar no put também, aqui, onde a gente passa o password, a gente vai chamar o GetPasswordHash. Em, em teoria...

**[00:15:24]** Essa única modificação bem simples que a gente fez aqui, ela não deve gerar nada, né? Tipo assim, porque a gente não expõe a senha em lugar nenhum. Logo, se a gente rodar os testes, tanto do post quanto do pute, isso não deveria falhar, né? Porque em nenhum lugar a gente valida a senha, né? Por uma questão, tipo assim, de segurança, legal, que a gente nunca expõe a senha e também não valide a senha, né?

**[00:15:53]** Então, vamos rodar o teste aqui e ver o que acontece agora, né? Então eu vou dar um task, teste. Beleza, ó. Tudo continua passando, todos os testes que a gente fez. Por quê? Lembrando de novo. Por que os testes passaram se a gente alterou o código? Porque nada valida a senha. E é bom que seja assim, né? O único lugar onde a gente verifica, né? Tipo assim, a gente garante que o campo da senha existe é no teste do database, né? Que a gente viu...

**[00:16:26]** Ali. Esses algoritmos todos são one-away? Sim. Algoritmos de hash em teoria são algoritmos de mão única, né? Eles só vão. Para descobrir o que gerou aquele algoritmo aí você vai precisar tipo de... De uma... De força bruta, por exemplo. Então não tem como a gente fazer isso. Augusto, muito obrigado, mano, pelo teu super chat. Valeu, mano. Isso me ajuda muito, velho. A manter esse projeto. Valeu demais, velho. Tamo junto.

**[00:16:58]** Vem aproveitando que eu parei aqui pra dar um beijo, tem mais gente vendo do que like, deixa o like aí mano, ajuda, deixa as outras pessoas conhecerem esse projeto também, não sejam mesquinhos. Então legal, a gente viu essa parte, colocou uma senha, tá tudo funcionando, não foi muito.

**[00:17:18]** bizarro, aí colocou o hashcat, assim, o hashcat é uma forma de fazer esse ataque de força bruta, uma ferramenta para fazer força bruta de identificação de hash. Bom, então, vamos lá para a autenticação agora. Então, o que que, né? Como é que a gente vai descrever a autenticação de uma forma mais, assim, legal?

**[00:17:39]** Eu vou enviar minhas credenciais, né? Autenticação é o login aqui, né? Só pra gente lembrar isso aqui, não. Então, eu vou ter que criar um endpoint pra gente conversar sobre isso, mas eu tenho que enviar as minhas credenciais pro servidor de alguma forma. A gente vai fazer isso via HTTP, porque assim, esse modelo cliente servidor que a gente tá trabalhando. Então, eu vou enviar, por exemplo, vou fazer o login com e-mail e senha. E a gente vai enviar isso aqui via um formulário. A gente já vai discutir um pouco sobre esse formulário.

**[00:18:09]** Calma. Mas você basicamente lembra aquele form que tem? Ah, formulário de login, e-mail senha. O username senha, aí depende de como você quer implementar. E aí o servidor vai validar essas credenciais e vai enviar pra gente um Tolkien. Um Tolkien é um númerozão, tipo esse aqui que a gente tava vendo, tipo assim. Uma coisa que parece um hash, uma coisa assim, muito mirabolante.

**[00:18:35]** E é isso que a gente envia as credenciais erradas, isso aqui retorna um erro, né? O Tolkien é o que diz para o cliente que ele está logado. A gente vai melhorando isso aqui com o passar do tempo. Mas basicamente, a parte interessante aqui é essa aqui no primeiro momento, né? A gente vai enviar as credenciais ao meu username 100 ou meu email 100, dentro da aplicação a gente vai usar email 100. A gente vai enviar isso via formulário.

**[00:19:01]** A aplicação vai abrir esse formulário, vai ver o e-mail senha, vai buscar no banco de dados e vai falar, olha, deu certo ou deu errado, e-mail senha certo, e-mail senha errado, dessa forma. Então a gente vai tentar fazer dessa forma que o que eu diga aos meus dados e o servidor fala, ó, tá certo, você é você mesmo. E aí pra fazer isso, a gente vai fazer por partes, porque eu acho mais simples, né, a gente entendendo tudo.

**[00:19:30]** Para que as pessoas possam enviar as credenciais ou fazer esse autenticação, que é o nome correto, mais bonito do login, a gente vai criar um endpoint, uma rota, um post que a gente vai chamar de token, barra token, que é onde a gente vai entregar o token para a pessoa. Então, tem várias coisas que a gente vai precisar fazer aqui. A gente vai precisar criar um esquema de credenciais, um esquema de token, validar se o e-mail existe,

**[00:20:01]** O que a gente vai ter que buscar na base, se o email existir, a gente vai ter que ver se ele bate com o hash, aquela função que a gente acabou de criar aqui, que é verifier password. Caso não batam, a gente vai retornar um erro. E aí, se tudo der certo, por último, a gente vai retornar um token.

**[00:20:23]** um Tolkien JWT que a gente vai falar daqui a pouco o que que é, como se manifesta e tudo mais, com um tempo de duração. Ou seja, você tem esse Tolkien para conversar com o servidor para fazer coisas que você precisa estar autorizado para fazer durante um determinado tempo. A gente vai começar com 30 minutos. Tá tudo bem, aí depois você quiser colocar mais tempo, menos tempo, aí fica a critério de cada pessoa. Então legal, a primeira coisa que a gente precisa

**[00:20:51]** é desse esquema de credenciais, ou seja, o esquema de credenciais é essa coisa do pai dente, que a gente está acostumado a fazer, né? Que a gente tem aqui os nossos esquemas, um esquema que represente essa coisa de user e password. Nome de usuário e senha, ou e-mail e senha, aí vai dentro de que cada um pretende fazer. Dentro do Fast API, a gente tem já um formulário pronto para fazer isso.

**[00:21:18]** que é o Password Request Form, ou seja, é o formulário que requisita o password, a senha.

**[00:21:26]** E aí ele segue um padrão chamado OAuth2, ou OAuth2. Isso aqui é uma coisa padrão para vários tipos de login e tudo mais, é um padrão da web. A gente não vai se aprofundar muito nisso, mas se vocês quiserem ver mais material sobre isso, tem bastante coisa na internet, é um padrão aberto para essa troca, especificação de login e tudo mais. Aí o FastJPi tem já isso implementado para a gente poder trocar essa ideia com o servidor.

**[00:21:56]** Então, a gente vai usar esse formulário pronto aqui. Aí, se der certo, a gente vai criar um esquema de Tolkien que retorna. Esse aqui é seu Tolkien e qual é o tipo do Tolkien. Aí, a gente vai validar se o imeneste está tudo certinho e, para isso, a gente vai fazer um Tolkien, tudo bonitinho, ver o tempo, falar, ó, daqui meia hora é que hora. Então, vamos lá, vamos por parte.

**[00:22:23]** Vamos lá, dentro do nosso app.py, a gente vai criar esse endpoint, essa rotinha nova chamada Tolkien. E aí o que a gente vai pedir é o formulário, né? O formulário de password, o formulário de autenticação. E lembrando como eu disse, ele já vinha do FastApeIner. Então a gente vai simplesmente pegar ele aqui. Eu vou criar ele aqui dentro do app. Eu sei que para vocês o app já deve estar ficando...

**[00:22:48]** uma loucura, né? Porque tá muito grande já, mas tudo bem, a gente vai resolver isso nas próximas aulas, já estamos indo pra mais de 100 linhas aqui, né? Então, a gente vai chamar o app.post e aí aqui, eu vou chamar esse indipente de token, foi o nome que a gente combinou ali no slide. Então, a gente vai ter que enviar uma requisição pra cá pra fazer a autenticação. Ah, eu gostaria que fosse login, tudo bem, pode ser, aí é contigo.

**[00:23:15]** Eu vou usar token, porque no sentido semântico, a gente vai gerar um token aqui dentro. Aí a gente vai criar esse endpoint, que eu vou chamar de Login for Access Token, bem original, né? E eu não vou implementar nada por enquanto. A gente vai ter que importar, né? Lá do security do FastAPI ou alf, né? Então, vamos lá. Então, from FastAPI ponto security import ou alf. Aí você vai ver que tem vários aqui.

**[00:23:44]** ou Alphbert Tolkien, From Street, a gente vai importar esse aqui, que é o Request Form, lembra? Formulário de Requisição de Senha. Massa, então é isso aqui que a gente vai pegar. Nesses momentos que a gente vai fazer uma coisa bem esquisita aqui, e aí, quem não estiver olhando na tela, é bom olhar agora, porque vai acontecer uma coisa com a Ingestão de Dependência aqui, que é meio maluca. A gente vai falar o seguinte, isso aqui é Depends.

**[00:24:14]** E eu dei o nome no slide form data, form data. Aqui é dois pontos, peraí. Isso. Olha como isso aqui é estranho. A gente está usando Depends. Lembra que a gente conversou na aula passada sobre a Injeção de Dependência? Aqui dentro do Fast API, a gente vai simplesmente só falar Depends.

**[00:24:39]** Mas vai falar, mas por que depende sem nada se a gente não está injetando nenhuma dependência e tudo mais? Isso aqui é um problema que eu vou dizer que eu considero um problema de design do Fast API. Para garantir que o formulário de requisição vai ser recebido, a gente usa o Depends aqui. Eu não gosto dessa abordagem, eu acho meio esquisito.

**[00:25:06]** Mas tudo bem, a gente vai sobreviver por enquanto. É estranho mesmo e tá tudo certo. Massa, é isso aqui. Aí o Michael perguntou coisas, tipo assim, porque o projeto é síncrono quando ele vai virar síncrono daqui a algumas aulas. Então legal, eu vou...

**[00:25:28]** Rodar a aplicação, porque eu quero mostrar pra vocês como é que esse formulário vai se comportar lá no Swagger. Então vamos lá. Poetry Brown Tasking Serve. É Tasking Brown, não? Legal. Subiu o servidor aqui, eu vou chamar ele lá. A local host 8000-docs. Injetou a anotação. Eu acho esquisito também, mas tudo bem. Faz parte. É assim que funciona, né? A coisa aqui.

**[00:26:01]** É como o FastAPI implementou isso aqui. Aí eu já não posso discutir com como isso vai funcionar. Mas basicamente, olha o que ele virou, esse barra token. Ele chama Login for Access Token, que é o nome que a gente deu para a função. Mas olha que doida, já vem tudo meio que pronto aqui. Ele é um tipo Form, ele não é um JSON, né? Aí ele está aqui ó. WWFORM, tal, porque o padrão do ALP é que as coisas sejam um formulário mesmo, não um JSON.

**[00:26:31]** É um form. Aí, se a gente der um try it out, a gente vai ver aqui que ele pede o seguinte. Ele pede o username e o password aqui. E aí, quando a gente enviar esses dados, esses dados vão virar um esquema dupla idêntica. Lá dentro. Olha que legal.

**[00:26:54]** Então, ele pede várias coisas. Grandtype, username, password, scope, client ID, client secrets. A gente vai trabalhar com o básico do login. Username e senha. E para username aqui, a gente vai usar o e-mail. Ah, mas por que a gente não vai usar o username? Sei lá, porque eu escolhi usar o e-mail. Poderia ser o do noSour, mas vai ser o do noSouraruber email.com. Aí também é uma questão de gosto, né? Cada um prefere, eu prefiro o login com o e-mail.

**[00:27:23]** Aí a gente manda os dados, ele executa, e olha que legal como é que ele manda isso aqui, né? Ele fala que aceita Jason, mas o que ele tá mandando, ó, é tudo via Queer. Queer string, não é? Tipo, tá vendo? GrandeType, password, username string, password string, scope, client, tal, tal, tal. Tá mandando alguns dados vazios pra lá. Então, é tudo na URL. Por isso que é o FarmData.

**[00:27:51]** Massa fez sentido isso aqui, ele não é JSON, ele não manda no corpo da requisição. Aí ele deu no, deu erro aqui porque a gente não implementou e tá tudo bem, tá tudo certo. A gente vai fazendo isso aqui com o passar do tempo. Mas eu queria que vocês dessem uma olhada nisso aqui porque é bem diferente a forma como isso aqui funciona, né? Tipo assim, a gente vai pedir esse tipo de formulário e falar que ele precisa ser executado no request, mas...

**[00:28:18]** Não necessariamente o que vai vir aqui. Por padrão, como a gente vai validar, se o username existe, se a senha existe, aqui a gente vai ter que pedir a session do banco de dados. E aí eu vou chamar aqui de session, e a gente vai falar que isso é uma session do banco de dados, eu estou usando esse esquema aqui. Session, aí eu dependes get session, igual a gente fez na aula passada. Então session, e a gente vai...

**[00:28:52]** Falar que isso aqui depende, então a gente vai injetar a função getSession que a gente tinha criado na aula passada. GetSession. Massa, basicamente essa é a implementação do que a gente precisa para iniciar aqui a nossa brincadeira aqui. E aí, o que a gente vai fazer com isso aqui? Bom, eu coloquei um slide aqui para mostrar como que estava no Swagger, mas eu fiz isso antes do slide.

**[00:29:23]** mas basicamente a implementação é bem simples, a gente vai perguntar, a gente vai pedir aqueles dados do formulário, vai ver se eles estão no banco de dados, se não tiver o user que a gente queria, a gente vai falar que deu não autorizado, ou seja, é um notorizer, não preciso explicar, tipo assim, o que aconteceu, só deu erro, tipo assim, você não está autorizado a receber um Tolkien.

**[00:29:48]** porque talvez o seu e-mail seja diferente ou porque talvez a senha não bata então eu não quero dar muitas explicações aqui de qualquer forma vai levantar essa exception não autorizado legal mas antes da gente ver o banco eu quero fazer uma coisa com vocês aqui eu vou botar o breakpoint aqui o do debugger e vou enviar lá o formulário para vocês verem o que que é esse ou a alfie aqui né vamos vamos ver aqui o que que rola

**[00:30:15]** Talvez isso fica até mais simples de entender o que vai acontecer no código aqui. Então eu vou dar um execute e a gente vai voltar aqui para o shell onde a gente executou. Vamos ver esse form data aqui, o que que ele é. Ele é um FastAPI Security12, tal, tal, tal, tal, tal, tal. Ele é um modelo do pai idêntico tradicional. Se a gente pedir aqui os dados que a gente enviou aqui, como username, username ele deu aqui, string, foi exatamente o que a gente passou. E se a gente pedir o formdata.

**[00:30:46]** Password, ele também deu o string porque foi o que a gente enviou ali. Então, basicamente, são esses campos que a gente quer. O username e o password para poder olhar dentro da sessão se isso aqui existe ou não. Eu vou pedir para ele sair aqui. Vou tirar esse debugger só para ele dar o refresh na aplicação aqui.

**[00:31:08]** E a gente vai pegar essa sessão Session. e a gente vai ter que fazer um Scalers, né? Scalers. É o escalar no plural, né? Porque a gente vai buscar um registro só. E aqui, bom, beleza, a gente vai selecionar lá na tabela de Users. A gente quer saber se... Então, onde, né? Where? O User.

**[00:31:33]** ponto aí aqui lembra aquele negócio assim aqui vale prestar atenção se você quiser usar o e-mail como base igual eu tô fazendo eu vou usar aqui ó user e-mail igual a formidata ponto username tá vendo que eu tô eu tô colocando uma cláusula muito específica aqui né eu tô falando ó que eu quero usar o e-mail como login só que o campo no formulário se chama username

**[00:32:02]** Ah, se eu quisesse usar username com username, você poderia fazer username igual username. Então eu vou usar o e-mail porque eu gosto de usar e-mail. É uma preferência minha aqui. Mas então a gente vai pedir esse dado aqui pra ele. Então a gente vai procurar qualquer usuário que tenha o e-mail igual que veio lá no formulário.

**[00:32:25]** Massa, aí o footquist tá perguntando uma coisa que é de outra aula, mano. Pergunta lá no grupo pra gente não perder o fio da amiada aqui na aula, mano. Pode ser. Então, basicamente, essa é a implementação que a gente quer. A gente quer fazer essa boost aqui. Eu tô usando o e-mail. Lembre-se disso. Isso aqui é motivo de dar bugs depois, né? E aí a gente vai fazer aquele ifon normal, ok? If, not, né?

**[00:32:52]** username, ah, pera aí que eu não pedi, né? Aqui o resultado da quern, né? Eu chamei de user aqui. User. If not user, a gente vai retornar a exceção aqui, né? O erro. E aí o segundo caso, tipo assim, se deu esse erro aqui, o que que a gente vai fazer com isso, né? Então, se deu erro, a gente vai dar o rise, mas tem outra condição, né? Que é tipo

**[00:33:20]** Se a senha não bater, né? Só que a gente não importou isso aqui ainda, né? Então, vamos lá em cima. A gente tem lá no security, né? A gente importou só o get password hash. Aí eu vou importar o verify password aqui também. Porque aqui é a hora que a gente vai validar a senha, né? Então, if... Verify password. E a gente quer ver se a senha não bate, né? Então, not. If not verify password, aí a gente vai pegar o user.

**[00:33:52]** Primeiro é o limpo, lembrando aqui a procedência da função. O primeiro é o pleno, que é o que veio do form, então a gente vai chamar o form data.password, a gente vai validar se é igual ao do user que veio no banco de dados, então user.password, ou seja, a gente vai verificar se o limpo que a gente recebeu aqui é igual ao hash que está no banco de dados.

**[00:34:24]** E aqui também é uma outra condição de erro. Aí aqui a gente vai dar o rise, né? Rise. HTTP exception. Aí a gente tem que dar um status code, status code. É o HTTP status.unauthorize, né? Não tem autorização para fazer isso aqui, né? E aí você pode dar o detail aqui, né? Que você quiser. Detail. E falar qualquer coisa que você queira aqui. Eu dei o aqui, o incorrect email or password aqui.

**[00:34:58]** Então eu vou manter a mesma coisa aqui, só para a gente ficar nesse esquema. Aí aqui, o seguinte, a gente pode fazer dessa forma duplicando, você pode criar uma variável para esse HTTP exception, aí é contigo que você achar mais legal para duplicar o código aqui. Então o post está expondo o password até chegar no servidor. É, é isso. Você manda, só que não está exposto, né?

**[00:35:30]** Porque a gente não vai trafegar via HTTP, né? A gente vai trafegar isso via HTTPS. Então, a requisição já é encryptada por padrão, né? A senha vai limpar dentro do pacote encryptado, né? É basicamente isso que está acontecendo. A gente vai trafegar via HTTPS. Ou seja, HTTP, seguro. Massa? Então, a gente chegou aqui, né?

**[00:35:59]** Validamos, em teoria, se não existir dentro do banco de dados, ele vai ter que dar esse exception pra gente. Vamos ver o que acontece lá na nossa API agora? Então eu vou chamar esse string string aqui e ele tem que dar esse erro de não autorizado. Executei, olha o que que ele deu aqui pra gente. Não autorizado. Não existe esse e-mail ou essa senha. Ah, se fosse um e-mail, sei lá, válido aqui. Ah, sei lá.

**[00:36:28]** Eduardo Arroba, mail.com. Também não tem na aplicação, né? Mas só pra gente ver, vai dar incorrect email ou password. Então, isso só vai passar quando o email existir e a senha bater, senão ele vai retornar esse erro aqui. Massa, fez sentido aqui? Essa parte? Podemos prosseguir aqui? Podemos...

**[00:36:58]** Então dentro dessa brincadeira aqui, a gente fez toda essa primeira parte, a gente definiu o esquema de credencial que a gente não criou, usou a Alphi Porme do FESJPI, a gente fez a validação se o imenho existe, se a senha bate com o hash. Aí agora a gente precisa criar um esquema para o Tolkien, essa coisa que a gente vai retornar.

**[00:37:20]** E a gente precisa retornar um Tolkien que tem uma duração de tempo, ou seja, a pessoa está logada na nossa aplicação durante um determinado tempo. Só que aí eu preciso explicar o que é esse Tolkien, o que é essa coisa para não ficar tão abstrato aqui. Então a gente vai usar um esquema de assinaturas. É importante lembrar que isso aqui é um esquema de assinaturas, a gente vai entender o que significa.

**[00:37:43]** de JWT. A gente chama de Tolkien JWT, é redundante chamar de Tolkien JWT, porque o T de JWT já é Tolkien, mas tudo bem, a gente começa de algum lugar aqui, né? Então, o JWT é um Tolkien que trafega via Jason e ele é da web. Isso significa JWT, né? E isso é uma forma de assinatura do servidor. E aí, o que eu quero dizer com assinatura?

**[00:38:14]** Quando eu vou logo na aplicação, então eu vou lá e dou meus dados para a aplicação. E fala, olha, toma aqui a aplicação. Aí a aplicação, ela vai pegar esses meus dados e vai assinar eles criptográficamente. Ele vai pegar, vai aplicar um algoritmo bem parecido com esse que a gente tinha, que era de hash, mas não é de hash, né? É uma assinatura mesmo. Então ele vai assinar um servidor falando, olha...

**[00:38:43]** Essa pessoa me mandou as credenciais, é basicamente isso que significa. Essa pessoa mandou os dados, me mandou as credenciais, eu assinei, ou seja, peguei um algoritmo de assinatura, assinei isso aqui e estou te dando de volta, falando, ó, essa pessoa se identificou no meu servidor. Mas é basicamente isso aqui que o Tolkien JWT quer dizer. E aí ele é dividido em algumas partes, né? Ele tem o header...

**[00:39:11]** Ou seja, o cabeçalho do Jason, que ele vai falar qual foi o algoritmo que criptou e qual é o tipo de Tolkien que está ali dentro. A gente vai ver certinho essas variações. Aí a gente tem o payload, que são os dados que a gente assinou.

**[00:39:29]** Aqui a gente chama isso aqui de claims, né? É algumas coisas que a gente fala que a gente assinou, ou seja, assinei o username, vale até que hora, ele tem acesso a XPTO, então aqui são os dados, né? Que a gente assinou. E por fim, a gente manda assinatura, que é a aplicação desse algoritmo que está especificado no header, mais uma chave secreta que a nossa aplicação vai criar aqui, a gente vai fazer isso direitinho. Massa.

**[00:39:57]** Só para a gente especificar o que é o payload, a gente vai fazer todos esses passos juntos, mas tenho que destrinchar em algum lugar isso aqui. Quando a gente vai criar esse esquema de payloads, aqui, basicamente, a gente, dentro do JSON, tem essa chave-valor aqui. A gente vai falar que a gente tem um sub, e aí o sub significa subject, que é o assunto, ou seja, de quem é aquela assinatura.

**[00:40:24]** E aí o mais comum é ter uma data de inspiração aqui, ou seja, quando é que esse Tolkien deixa de valer. Isso aqui é uma forma de tempo inteiro. Então existem vários tipos de payloads possíveis que a gente pode mandar aqui dentro, ou, desculpa, existem vários tipos de clãs que a gente pode mandar aqui nesse payload. Vários. Isso aqui é um campo, sei lá, que cabem quantas coisas você pensar que existem aqui dentro.

**[00:40:52]** Deixa eu pegar aqui pra vocês. JWT claims. Só pra vocês verem uma lista do tanto de coisa que tem aqui dentro. Tem uma lista oficial aqui, mas essa aqui do Alf Zero já é legal aqui, que tem bastante coisa. A gente vai usar só duas, né? Mas existem várias coisas. Essa página do Alf Zero é bem legal, a gente vai usar ela inclusive daqui a pouco. Runti, muito obrigado, mano, pelo teu super chat.

**[00:41:24]** Valeu pela ajuda, ajuda muito mesmo. Tamo junto, valeu. E aí aqui, ó, ele tá falando do seguinte, olha, a gente tem o subject, ou seja, quem é, que tá autenticado aqui dentro, qual é o nome dessa pessoa, se essa pessoa é administradora do sistema ou não, ó, aí a gente tem audio, né, que é audiência, ou seja, aonde que essa pessoa pode mexer a partir desse token que ela tem, ó, tem muitas coisas, muitas, muitas, muitas assim.

**[00:41:53]** Aqui, na página do IANA, tem todas as clãs possíveis aqui. E são muitas, assim. Muitas mesmo, assim, ó. Quem é que abriu, né? O Isher, quem é o Subject, a audiência, a inspiração...

**[00:42:08]** Não antes, né? É um token que passa a valer amanhã, a partir de amanhã vale x tempo, algumas coisas assim. Então possam muitas coisas, muitas, você pode mandar o e-mail, e-mail verifier, gender, brief dates, zoning info, locale, telefone, por... É um monte de dados que você pode assinar aqui. Eu vou trabalhar com dois dados, os mais simples possíveis, quem é o subject e qual é o tempo de inspiração. Mas existem muitos outros...

**[00:42:37]** dados aqui que podem ser explorados aqui dentro do payload, várias formas de identificar a pessoa ou várias formas de assinar os dados que você quer gerar para aquele token.

**[00:42:49]** Massa? Bom, pra gerar tokens com Python, tokens JWT, né? De novo, redundante, né? Pra gerar JWT com Python, a gente tem essa biblioteca chamada PyJWT. Existem uma infinidade de bibliotecas, mas essa é a mais tradicional de todas. Então, eu vou instalar ela aqui com vocês. Então, vamos lá. Põe entre edge PyJWT. Legal, não tem nenhuma dependência, tá instalado rodando bala.

**[00:43:18]** E aí, o que que acontece? Eu quero mostrar pra vocês uma coisa aqui. Como é que fica? Qual que é a cara desse Tolkien? Porque se parece que já passou uma coisa de outro planeta. Eu tô falando, é dividido por três. Tem o header, tem o payload, tem a assinatura, tem um monte de coisa. O que que isso significa? Pode parecer qualquer coisa aqui, não é? Então, vamos lá. Eu vou abrir aqui no Shell com vocês, a gente vai chamar o JWT juntos aqui. Lembrando que você tem que estar no ambiente virtual, ativado. Então, Python.

**[00:43:46]** Eu vou chamar, né? O import JWT aqui, vou aumentar a fonte um boquinho pra gente ir vendo junto. Aí o JWT tem uma função que se chama encode. E aí eu vou passar aqui um dado pra ele. Qual dado que eu quero assinar? Qualquer coisa vale aqui, né? Então eu vou falar que quem gerou esse token foi o salo sub e aí eu vou chamar aqui de dunossauro. Fui eu que gerei esse token. Massa, é um token pro dunossauro. Ele é o assunto do token.

**[00:44:16]** E aí eu tenho que passar uma senha aqui, qualquer senha. A gente vai ver uma forma de gerar uma senha segura, mas eu vou gerar aqui um, dois, três. Massa? E aí eu vou fechar isso aqui. E ele deu uma coisa aqui muito legal, que é essa mensagem aqui. Uma coisa interessante de notar aqui no JWT, é que ele tem três pontinhos. Ele tem dois pontos que separam a mensagem em três aqui, né? Olha que legal. Então tem alguma coisa aqui muito maluca, um ponto.

**[00:44:46]** Alguma coisa muito maluca e um ponto. E depois, uma coisa muito maluca. Isso aqui é o header, antes do primeiro ponto. Isso aqui é o payload, o que está entre os dois pontos. E o que está depois do segundo ponto, é a assinatura. Olha que massa! Muito, muito interessante. E a partir do ponto em que eu pegar isso aqui, esses dados, eu posso dar o JWT.decode. E a gente vai rodar esse token que a gente recebeu aqui.

**[00:45:17]** Aí eu preciso falar qual que é a senha, tem que ter a senha, senão ele não desfaz esse esquema. Então a gente vai passar os dados que a gente mandou aqui do encode e a senha que era 1, 2, 3. Era 1, 2, 3? Já nem lembro mais qual que era. É 1, 2, 3. É o Tolkien 1, 2, 3. Caramba, estou viajando aqui. Ele tem um erro legal aqui.

**[00:45:49]** que ele precisa falar qual que é o algoritmo que gerou esse Tolkien. Mas a gente não falou qual que foi o algoritmo que gerou. E qual que é o padrão aqui? Isso é interessante de saber. Em Code. Vamos dar um help disso aqui e ver o que acontece aqui. Ele está falando que o algoritmo, se não passar nada, é NAN. Ou seja, eu não sei qual é o algoritmo que ele usou para encriptar isso aqui. E aí, se a gente for chamar a função de decode,

**[00:46:18]** Ele tá falando aqui, ó. Na hora eu tenho que passar o algoritmo e eu tenho que saber qual foi o algoritmo que foi passado aqui. Eu não consigo saber quem é que foi que gerou isso aqui sem passar o algoritmo por padrão é NAN. Então eu poderia fazer o seguinte, eu poderia em vez do aqui chamar o Verify, né? Ainda dizem que um, dois, três não é segura. Então eu poderia chamar o Verify, eu poderia chamar várias coisas aqui. A gente vai conversar daqui a pouco sobre essa parte.

**[00:46:52]** Mas eu poderia chamar o Verify, tá vendo? Olha o tanto de coisas que tem aqui nessa biblioteca, tem muita coisa. Basicamente. Mas pra decoder eu preciso saber qual foi o algoritmo que gerou, mas como eu não passei o algoritmo nenhum, a gente tem esse problema. Porém, com tudo entretanto da via, o que eu quero aqui é o Tolkien, porque eu quero mostrar pra vocês que isso não é encryptado. Ele deu erro porque eu não sei qual é o decode, mas eu quero copiar isso aqui e a gente vai lá no jwt.io.

**[00:47:25]** Espera só colar isso aqui, eu já mando o JWT.io pra vocês aí. Pô, tem um site mais bonito, né? O do... O Debugger.io é mais bonitinho aqui. Eu queria abrir em outra aba, né? Sem sair dessa. Pera aí, pera aí, pera aí. Acho que só tá esquisito mesmo aqui, né? Ah, agora carregou direitinho. O JWT.io. Eu vou colar esse Tolkien aqui e vou mandar pra vocês aqui o site.

**[00:48:05]** no jwt.io a gente consegue ver aqui qual foi o algoritmo que gerou hs256 e qual é o tipo de token que gerou isso aqui que é o jwt ele fala qual que é o sub, qual que é o dono sauro e aí a gente só consegue validar isso aqui se a gente souber qual que é a senha tá vendo ele tá falando que a assinatura é inválida mas por que que é inválida? porque eu não sei a senha se a senha for um dois três

**[00:48:35]** Aqui ó, a assinatura está verificada. Ou seja, existe um conjunto de todos os dados aqui, né? O header, o payload e a assinatura. E a assinatura está usando esse algoritmo. Se a gente testar outro, ainda vale. Ué, que estranho. Mas está vendo que ele está mudando aqui, ó. Isso é uma coisa que você tem que tomar prestar atenção aqui. Enquanto você muda aqui, ele vai mudando ali. Então você nunca sabe qual é o token que ele está usando ali. Mas, basicamente,

**[00:49:10]** Esse Tolkien aqui com esses três pontinhos tem essa informação aqui. O header, o payload e a assinatura. E a gente pode ver se ela está verificada ou não. Fez sentido isso aqui? Que essa string contém todas essas informações? Preciso ir do feedback de vocês, hein? Talvez tenha ficado um pouco enrolado aqui. Moringa, muito obrigado, Ben. Pelo super chat. Tamo junto. Fez sentido? Tudo que está...

**[00:49:54]** sendo armazenado nessa informação aqui, é que a gente vai nesse bem em volta e vai e volta e abre site e vai, mas basicamente a gente tem que entender isso. Quando a gente pede para lincodar qualquer coisa, ele vai gerar essa assinatura. Mas você viu que pelo Tolkien, a gente consegue saber tudo que tem lá dentro, a gente só não consegue validar isso aqui. Saca. Então, tipo assim, isso aqui é uma assinatura, isso aqui não é criptografia.

**[00:50:29]** Saca, isso aqui não é criptografia. Weak secret, me respeito. Não, é importante dizer, isso aqui é somente uma assinatura, né? A gente tá falando, olha, quem gerou foi isso aqui e pra validar a assinatura você tem que saber qual é a senha. Aí perguntou, meu, é tão estranho que se alguém pegar o JWT consegue ver tudo que tem nele, consegue ver tudo que tem nele. É por isso que você tem que tomar alguns cuidados nas coisas que você trafega via JWT. Isso aqui é uma forma só de assinatura.

**[00:51:06]** Então você está dizendo que esse Tolkien é meu e quem assinou foi o servidor. Só que você, esse último campo aqui, ele carrega a senha, a coisa, o segredo do servidor. E para validar você tem que saber qual é o segredo do servidor, não tem como você sem saber isso aqui. E aí, tipo assim, é isso, é simples, parece muito mais complicado do que é...

**[00:51:39]** De fato, mas é bastante simples aqui. Como é que essa coisa funciona? E aí, se você quiser decodar, que foi uma pergunta que o Regis fez aqui...

**[00:51:49]** É uma forma de garantir que as informações vieram de uma origem válida. Exatamente isso. Não só que vieram de uma origem válida, mas é o seguinte, o user deu as credenciais. As credenciais vão voltar como se elas forem assinadas pelo aquele servidor. Ou seja, é uma relação entre as minhas credenciais e o servidor. Saca? Então existe uma triangulação aqui. Faz sentido isso? Massa?

**[00:52:17]** Aí, se você quiser fazer o decode aqui, jwt.decode, aí a gente vai ter que falar qual que é essa estringona que a gente tem aqui. Opa, peraí que eu esqueci as... peraí que ele tá com... É por isso que deu erro no decode aqui, você tá vendo que ele tá juntando essa barra aqui? Decode, aí eu preciso passar qualquer 100, é 1, 2, 3. Aí ele falou, qual que é o algoritmo que gerou isso aqui? Aí a gente chama. Algoritmes...

**[00:52:51]** Ele tem um problema pra escrever isso aqui. Algoritmes. É assim? Pode ser que seja. HS256, que é o algoritmo que fez isso aqui. Aí ele trouxe pra mim aqui, ele falou, olha. O subjeto é isso aqui, ó. Donossauro. Massa, se eu passasse outra Secret aqui, como 4, ele vai falar, ó, essa assinatura não é válida, porque não fui eu que gerei. Saca, a Secret é outra.

**[00:53:23]** Então, pra gente fazer isso aqui, igual a gente tinha lá, a gente passa o algoritmo e, por padrão, o algoritmo é sempre h256. Por padrão. Aí ele pede que a gente fale o que que criptou isso aqui. Quando você só encoda sem falar nada, o padrão é h256, que é um algoritmo de assinatura disso aqui. Aí, por padrão, ele me deu o sub, que a gente tinha aqui. Legal? Então, essa é a parte do encode decode. Só que aí você vai falar, como é que eu gera uma senha segura?

**[00:53:56]** uma chave segura pra que a gente possa manter isso aqui de uma forma um pouco estruturada ou pelo menos minimamente estruturada né aí o python por padrão isso aqui é uma biblioteca do próprio python importing secrets o python tem uma biblioteca chamada secrets nativa e aí você pode chamar que o token é que vocês tem várias formas de token aqui eu não vou me aprofundar muito nisso mas ele gera um token e aí você passa pra ele

**[00:54:24]** O tamanho do Tolkien, sei lá, 10, 20, 2, 5, meia. E... Aí você pede para o Python, o Python vai te gerar um segredo a partir de um Tolkien aqui. Massa? Então, aí se vocês precisarem gerar uma chave segura, vocês podem usar essa coisa do Python aqui. Eu vou usar o tamanho padrão aqui, né? E qual é o tamanho padrão? Se alguém estiver perguntando, você dá um help e vê. Aqui, ó. Anybytes? None.

**[00:55:08]** E aí, qual é o padrão? Quem é que sabe? Muito bom. Mas beleza, se vocês precisarem disso aqui, vocês podem dar um token X e pedir para o pai onde dá uma chave segura. Toda vez que você gerar isso aqui, ele vai te dar uma chave diferente. Então o que você vai ter que fazer? Você vai ter que pegar essa chave e armazenar...

**[00:55:34]** Em um que? Exatamente num arquivo isso aqui. Porque isso aqui não pode ser dinâmico. Porque se isso aqui mudar, toda vez que a aplicação subir de novo, a chave vai mudar. Então isso aqui em algum momento a gente vai colocar lá no Envy File. Massa.

**[00:55:51]** Aí estou perguntando se tem uma comunidade sim, tá? Tá na descrição, mano, aqui o link. Legal, então se vocês precisarem de um valor para gerar isso aqui, você pode fazer isso aqui. E se você quiser investigar qualquer Tolkien, você pode, você só não pode verificar a assinatura dele, porque para verificar a assinatura você tem que saber qual foi o segredo que gerou aquela assinatura. Massa!

**[00:56:15]** Então, legal. Uma coisa que a gente tem que ficar claro é que quando a gente usa aquele padrão que a gente chamou de OAuth, ele usa um tipo específico de Tolkien, que a gente chama de Bear Tolkien. E na hora de retornar o Tolkien para a pessoa, você fala, olha, geramos aqui seu Tolkien JWT. Tolkien JWT, de novo. Vocês já sacaram que tem um problema, né? Geremos seu JWT aqui.

**[00:56:43]** E aí você tem que falar para a pessoa como é que ela vai usar aquele token toda vez que a gente precisar disso. Então, por padrão, é sempre legal retornar o token type, o tipo do token. Por padrão, a gente vai usar bare token. E o bare token, ele é um token que é passado no header da requisição. É que a poxa vai fazer sentido, então a gente vai retornar esse token.

**[00:57:05]** E quando a pessoa for fazer alguma coisa, que aí deixa de ser a autenticação, mas a autorização, a pessoa tem que especificar o Tolkien no cabeçalho do HTTP que ela vai enviar para a gente. Então, vamos criar esse Tolkien aqui, lá nos esquemas aqui. Class Tolkien. Aí o Tolkien é um Base Model. E aí a gente tem o Tolkien Type, quase. Tolkien Type aqui, que é uma String.

**[00:57:36]** E aí, por padrão, ele vai ser bare token, mas eu não vou passar essa informação aqui, eu quero que a gente sempre deixe isso explícito na aplicação. E aí, a gente vai passar o access token, que é o token de fato, aquele token com dois pontinhos, aquela string maluca dividida em três partes. Então, o ideal é que a nossa aplicação retorne esse token que se tudo der certo aqui, ou seja, no barra token, o modelo de resposta, o response model,

**[00:58:12]** é o modelo de Tolkien. Você poderia dar o nome de J.W.T. Tolkien, aí fica até o critério. Então eu vou colocar ele aqui, né? No import, a gente vai importar ele aqui, o Tolkien.

**[00:58:27]** E aí, toda vez que a nossa aplicação descerpe, se não der nada errado, a gente vai retornar esse token ali na frente. Só que a gente viu tudo o que acontece ali, tudo mais, tudo bonitinho, só que a gente não tem uma função que gera esse token. E a gente vai gerar isso lá no Securities e vamos definir algumas variáveis novas, algumas coisas lá. Massa, legal. Então, aqui, eu vou criar uma nova função que a gente vai chamar de Create Access Token.

**[00:58:58]** A isso aqui, ele vai receber o data, o data é um dict qualquer aqui, e esse data pra gente são os dados que a gente quer assinar. Então aqui a gente vai enviar as clãs, as coisas, tudo que a gente quiser mandar pra assinar, a gente vai mandar nesse dicionário aqui dessa função, ou seja, a gente vai chamar essa função lá no app depois pra ela dar o Tolkien pra gente. Massa, legal.

**[00:59:24]** E aí, o que a gente vai chamar? A gente vai chamar esse data que a gente tem aqui. Eu coloquei esse nome aqui de two in code pra facilitar a nossa vida aqui. Então, o que a gente vai encodar? Qualquer coisa que a gente mandar aqui dentro. E aí tem umas regras muito malucas aqui que a gente vai definir agora juntos. Eu quero que esse Tolkien valha por 30 minutos.

**[00:59:50]** Você poderia fazer isso de uma outra forma, da forma que você achar mais legal e tudo mais... Saca, aí é contigo. Fala, eu quero que dure 5 dias, eu quero que dure 10 minutos, eu quero que dure 30 segundos. Beleza, tá tudo bem. A forma como tu vai escolher gerenciar esse tempo é contigo. E aí pra isso eu criei uma constante aqui no código. Eu criei algumas constantes, eu vou trazê-las pra cá e a gente vai conversando sobre elas. Aqui a gente vai definir a nossa Secret Key. Só que eu deixei aqui como provisório.

**[01:00:22]** A gente vai ajustar isso aqui. A gente vai trazer isso lá para o Envy em algum momento, mas por enquanto a gente vai se basear nessas aqui. Aqui a gente está dizendo qual que é o algoritmo que a gente vai encodar. É importante a gente saber, né? E é importante que a gente possa trocar isso aqui sem mexer no código. Então a gente vai ajustar todas essas partes aqui depois. Mas por enquanto a gente tem que fazer o algoritmo funcionar. Então a gente tem a nossa chave secreta.

**[01:00:47]** A gente tem um algoritmo e a gente tem um tempo de inspiração desse Tolkien. E aí é tudo isso aqui que a gente vai usar aqui dentro. Para a gente dizer que o Tolkien vale por 30 minutos, eu preciso calcular a hora de agora, a hora que eu estou nesse exato momento, e a partir desse tempo...

**[01:01:07]** 30 minutos pra frente, ou seja, sua chave, o Tolkien que você vai mandar pra gente pra interagir, ele vai durar por 30 minutos. Só que pra isso, tá vendo que a gente vai pegar aqui o Date Time? E tem uma coisa aqui que é uma informação de Time Zone. Time Zone é fuso horário, né, em português. Eu vou usar o fuso horário zero, o TC, é o padrão global. Ah, mas eu queria usar América São Paulo, tudo bem, aí você vai gerenciando da forma como você quiser aqui.

**[01:01:36]** A gente está usando o tc, porque o banco também está em utc, então a gente padroniza tudo em utc, mas você pode usar o fuzurário que você achar mais legal aqui, é só trocar por america, barra, são, underline, paulo e tá tudo certo. Então vamos lá, vamos importar o date time aqui, então from date time import date time. E aí a gente vai achar mais o date time que a gente tinha aqui, date time ponto now. E aí?

**[01:02:10]** Eu tenho que passar o timezone, né? A informação de fuso horário. Aí eu vou chamar esse TZ. Aqui a gente tem um problema, né? Que pode acontecer na máquina de algumas pessoas e na máquina de outras pessoas, não. Então, vamos olhar aqui. Eu vou importar essa biblioteca aqui, chamada Zone Info do Python. Então aqui, From, Zone Info, Import, Zone Info, maiúsculo. Um em minúsculo, outro aqui é meu case, né?

**[01:02:39]** Zone Info. Algumas pessoas podem ter problema pra importar isso aqui, ou você vai rodar o código, ele vai falar, não existe esse Zone Info, a gente já vai ver isso aqui. Se você quiser testar aí, se você tem o Zone Info ou não, é uma boa. Só pra ver, testa aí no seu sistema. Se você não tiver, é legal que você estale o TZData. Algumas instalações do Python, dependendo de onde você compilou o seu Python,

**[01:03:09]** ou seja, se você pegou do Python tradicional, se você instalou via Poetry, se você usou o Pyng, aqui tem algumas variações e algumas variações vem com tzdata, outras não. Então, por padrão, é legal instalar, pelo menos fica explícito o que está acontecendo. Provavelmente a gente não vai ter esse problema aqui na minha máquina, mas na sua pode ser que aconteça. Então, vamos padronizar aí o tzdata.

**[01:03:36]** E aí o que eu vou fazer? A partir desse momento aqui, que é o DateTimeNow, eu vou importar daqui do DateTime o Delta, TimeDelta. E aí o que eu vou fazer? Desse momento onde a gente está agora, eu vou somar um TimeDelta. Ou seja, a gente vai adicionar um tempo pra frente, né? Ou seja, pegamos aqui e agora é 94, então eu quero pegar 934. Então eu vou pegar esse TimeDelta e vou somar...

**[01:04:06]** os minutos aqui, ao tempo que a gente colocou nessa constante. Mas, então, Minutes vai receber o tempo que a gente está usando nessa constante aqui. Ah, por que não passa 30? Não passa 30. Use a constante, porque depois isso aqui vai virar uma variável de ambiente. Um pouco mais para frente. A gente vai tirar isso aqui e colocar no Envifile. E aí a gente vai pegar esse Token Expand Minutes, ou seja...

**[01:04:36]** do tempo em que essa função for chamada mais 30 minutos para frente, o token vai ser válido. Aí eu vou chamar isso aqui de tempo de expiração aqui dentro. Deixa eu copiar aqui direitinho, não perder tempo digitando tudo. Aí a gente vai chamar isso aqui de expiração. Expine.

**[01:04:59]** E aí, o que aconteceu? A gente já tinha os dados que a gente quer encodar dentro das claims, e aqui a gente vai colocar essa claim chamada XP, que é o tempo de expiração, quando o Tolkien vai parar de valer. Então, a gente está simplesmente adicionando no dicionário que a gente tinha aqui. Ou seja, tem o data que vai ter o nosso subject ou os outros dados que você quiser colocar, mas o tempo de expiração que vai caber aqui dentro.

**[01:05:25]** Aí, como a gente já tem todas as informações agora, a gente pode formar aquela função encode do JWT que a gente usou lá atrás e estava testando, que a gente brincou lá atrás, né? Aí a gente tem o algoritmo que a gente definiu aqui em cima, que é o H256, a nossa chave secreta, que por enquanto é esse yourSecretKey aqui, você pode gerar um secrets e colocar aqui, tá tudo bem? E a gente falta importar o encode, né, do JWT. Então, from JWT.

**[01:05:57]** import encode, massa, aí a partir disso aqui a gente tem o token encodado, basicamente eu vou dar um return nele aqui, então toda vez que alguém chamar essa função create access token ele vai enviar um dicionário pra gente com alguns dados né, por exemplo isso aqui poderia ser

**[01:06:21]** Como a gente estava fazendo ali, é assim, né? Então a gente vai enviar o subject e o e-mail de alguém aqui, ou sei lá, qualquer outra coisa que a gente queira aqui. Então esse é o data aqui, né? Que a gente vai receber. Só pra ficar claro aqui, se alguém precisar dar uma olhada nisso depois, a gente vai receber todas as clãs aqui. Poderia chamar isso de clã, né? Pra ficar mais específico, mas eu vou seguir data porque tá nos slides e tudo mais. A gente vai retornar isso aqui.

**[01:06:51]** Então, a partir de agora, a gente tem todo o mecanismo para gerar o Tolkien da nossa requisição. Só que a gente precisa testar isso. Será que essa coisa funciona mesmo? Será? Vamos começar o nosso primeiro teste de segurança? Então, a gente está lá no nosso repositório, eu vou criar aqui no testes o...

**[01:07:22]** Só para a gente garantir que isso aqui está funcionando da maneira como, sabe, a gente esperaria que funcione. Escreveu um código muito louco, várias coisas aqui, tipo, e vai tempo, e não sei o que, vamos ver se está funcionando da maneira como a gente quer isso aqui. Vamos lá, From, Fast API 0.securet, importe a função que a gente vai testar essa função aqui do jontwt. Então eu vou chamar de teste, é o nome do teste, eu preciso saber qual é o nome da função, essa aqui, ó.

**[01:07:51]** Create Access Token. Aí eu vou dar um DevTest, sempre tem que chamar teste, JWT. Um teste simplão aqui, sem nada demais aqui. Então o que que eu vou pensar aqui? Eu quero um dado, né? A claim ou qualquer coisa que a gente vai passar, né? Então eu vou chamar de claim, ou data. E aí o que que a gente quer encodar aqui? Eu vou mandar um teste, teste, vai? Teste, teste. Aí a gente vai chamar o Create Access Token, que só precisa desse dado, né, para funcionar. A gente vai passar o data.

**[01:08:30]** e a partir desse valor que a gente mandar aqui, a gente vai ter que conseguir decryptografar isso aqui, então ele vai gerar o token e a gente vai chamar o decode para ver se funciona. Então vamos lá, a token e a partir daqui a gente vai lá no JWT, chama a função de token, então a fron JWT import decode já formatando certinho, então a gente vai chamar o decode do token.

**[01:09:01]** com o segredo que a gente mandou lá. E qual é o segredo que a gente tinha colocado lá? O segredo a gente pode importar aqui também, né? O segredo, o algoritmo, tudo a gente pode importar aqui. Então vou colocar aqui, sei lá, secret key, que foi a chave que a gente gerou lá atrás. Então secret key a gente pode importar o algoritmo também. Tá tudo bem. Então para fazer o decode a gente vai passar o secret key e o algoritmo disso aqui é o algoritmo que a gente definiu lá também.

**[01:09:31]** só para garantir que o teste teste volta teste teste. Então, a gente vai pegar esse dado decodado, né? É o return ou qualquer coisa, decoded aqui. E a gente vai ver se o dado decodado, ou seja, que a gente tinha aqui, é igual a data, que é o valor que a gente mandou aqui em cima. Só que quem que a gente quer validar o próprio campo de

**[01:10:01]** Teste, né? Então a gente quer saber se o teste voltou, né? Aqui a gente tava lidando só as clins, né? Poderia ser qualquer coisa aqui, eu vou chamar de teste. Então a gente quer saber se o data teste é igual a data teste. Nossa, parece um teste bobo, mas isso aqui só valida que todas as nossas regras estão funcionando. Mas só pra saber se a gente tá encryptando com a chave que deveria, se a gente tá usando o algoritmo que deveria,

**[01:10:32]** Se a função faz o que tem que fazer e se volta, se o valor que ela encodou, a gente consegue decodar por ela aqui. Faz sentido esse teste? É só para a gente garantir que a gente está usando os mesmos dados aqui e lá. É uma forma de contenção, sabe? Tipo assim, puta, será que eu não coloquei nenhum dado errado? É esse o quesito aqui desse teste. Então, eu vou rodar com vocês lá no show, então vamos lá. Pasque teste.

**[01:11:02]** Aí ele deu alguns erros de formatação, eu vou dar o format aqui. Aí ele está reclamando daquele, isso é provisório que a gente deixou aqui, né? Que eu deixei só para avisar. Ele está reclamando que tem um espaço aqui. Espera aí. Format, legal, task test. Se tudo deu certo aqui, ó, o teste do JWT passou. O que significa que a gente está usando a mesma chave, o mesmo algoritmo nos dois lugares e...

**[01:11:29]** Não codamos nada errado. Uma coisa que a gente pode fazer aqui, para validar nesse test security, é saber se o tempo está sendo colocado aqui. Como eu não quero mexer com abstrações de tempo aqui, eu quero simplesmente saber se o XP foi colocado no decoded. Massa? Então, beleza, ó. Veio a cling que a gente mandou? Massa, a cling de inspiração de tempo foi adicionada dentro desse teste?

**[01:12:01]** que é o que a gente espera que aconteça aqui, tipo assim, o XP tem que ser encodado também, o tempo de inspiração. Eu não quero validar o dado específico aqui, mas só saber se ele está funcionando, se ele veio, se ele foi colocado aqui dentro. Vamos rodar de novo. Legal, então passou, significa que foi encodado com os valores certos e também foi adicionado a...

**[01:12:22]** o tempo de inspiração, a resposta do Tolkien aqui dentro. Tiago, deixa eu agradecer você enquanto vocês me falam se está tudo bem, se está todo mundo entendendo, se está tudo certo, está todo mundo quietinho, pode ser que eu esteja falando sozinho de novo. Tiago, obrigado, mano. Valeu aí pelo teu super chat. Tamo junto. Valeu demais.

**[01:12:45]** Aí você vê que, beleza, em teoria está tudo certo, aí tinha aquele negócio. Pô, se você for rodar o teste agora e viu que falhou, pode ser a falta do tzdata, então adicione ele aí, é importante para isso que funcionar. Isso aqui costuma acontecer mais no Windows, dependendo da instalação não tem todos os time zones e tal, então é importante isso aqui rolar. Beleza, agora eu vou voltar com vocês para o Endpoint do Tolkien.

**[01:13:19]** Porque a gente fez tudo, mas não gerou token ainda, né? A gente tava preparando todo esse terreno pra devolver o token. Então eu vou só copiar esse retorno aqui, só pra não ter que escrever tudo lá e a gente não perder tanto tempo. Eu vou vir aqui no app, lá no endpun de token que a gente tinha aqui, e o que que a gente tem que retornar é o token de acesso e o tipo do token, que é bare token. E pra isso, a gente precisa fazer aquela chamada maluca aqui, né?

**[01:13:51]** Então, a gente vai importar lá do security essa funçãozinha que a gente acabou de criar aqui. Então, deixa eu deixar tudo bonitinho aqui, só para não ficar pulando aqui. A gente vai ter que importar essa função chamada Create Access Token. E vamos colocar ela aqui, em porte do Fast API 0 aqui. Então, para encodar o que a gente quer encodar aqui no Create Access Token, essa função retorna o token de acesso.

**[01:14:27]** E aí a gente precisa passar o data. E o data que a gente vai passar, o sub que eu quero mandar aqui, é o e-mail. Então, user.e-mail, pra gente saber quem é que gerou isso aqui. Então, eu vou chamar isso aqui de sub. Massa? Então, em teoria agora, se a gente falar e passar os dados corretos de um user que existe na base, a gente vai ter que conseguir...

**[01:14:56]** gerar o token dele aqui dentro da nossa aplicação. Vamos ver o que que rola, né? Então, vamos lá. Eu vou criar um user novo aqui. Então, eu vou dar um post, criar alguém aqui. Então, eu vou criar um username, vai chamar essa lá. DonoSauro, o e-mail vai ser DonoSauro à Robexample e a senha vai ser DonoSauro. Não estou me importando muito com isso aqui. Legal. Executou.

**[01:15:25]** Ele falou, olha, username já existe, já tem um do no sauro aqui. Então eu vou criar o seguinte, eu vou criar um tacone, vai? Aí o e-mail vai ser tacone-arrobexample e o password vai ser tacone. Massa, eu acho que não criamos o tacone na base de dados. Legal, então a gente tem aqui o tacone é o ID4. Eu vou lá na página de Tolkien agora, vou dar um reset aqui.

**[01:15:53]** A gente vai ter que mandar. O username lembra que é o e-mail e a senha é tacone. Mas se tudo deu certo, a gente vai ter que enviar essa requisição e a gente vai receber o token e o tipo do token que a gente vai ter que mandar nas próximas requisições. Execute. Ah, legal, funcionou. Então ele mandou aqui pra gente o nosso token e ele fala que o token type é bare token. Vamos lá na página do JWT e vamos decodar isso aqui pra gente ver.

**[01:16:28]** Aí ele falou o seguinte, olha, o algoritmo é hs256, que foi o que a gente tinha mandado aqui, hs256, o tipo é JWT, aí o sub é o tacone, o tempo de inspiração é esse aqui.

**[01:16:48]** Então ele introduziu tempo de expiração e aqui a gente precisa dar senha para validar, para ver se a assinatura está válida e a assinatura que a gente tinha deixado é your secret key, por enquanto, a gente vai melhorar isso depois. Aí legal, a assinatura é válida. Ou seja, olha, maravilhoso, maravilhoso. Olha que massa. Funciona bem. Aí o Reds fez uma pergunta sobre Flask e eu não sei responder essa pergunta mesmo.

**[01:17:25]** Legal. Funciona. Temos um endpoint de Tolkien. O Tolkien dá o valor que precisava dar. Ó. Maravilhoso. É meio complicado. É um modo de coisa e vai e vem e pega e naip e tal, mas funciona. Olha que lindo. Então vamos testar esse endpoint aqui para a gente ver se ele funciona. Seria interessante a gente saber se está tudo certo. Se está tudo ok. Se deu tudo bom.

**[01:17:52]** E eu tenho em achar que agora as coisas vão começar a dar errado, né? Mas tudo bem. Agora as coisas começam a ficar complicadas. Eu vou criar um teste para isso aqui. Vamos lá. No final, eu estou no teste app, não é? Importante, só para deixar claro aqui. Então no teste app, eu vou criar esse teste aqui com vocês. Teste GetToken aqui.

**[01:18:19]** Aí o que que a gente precisa? A gente vai precisar que o user esteja criado na base de dados, fixer que a gente gerou e a gente precisa do cliente porque a gente vai fazer uma requiseção para a aplicação. Então vamos fazer o seguinte, eu vou pegar o response e o response vai ser igual a client.post que a gente vai mandar um post para lá. E aí o que que a gente vai mandar? A gente vai mandar para o barra token e a gente vai ter que mandar alguns dados e como é que a gente manda os dados de form, form data.

**[01:18:49]** Lembra que a gente sempre fala, tipo assim, ah, é o JSON, né? Todos os outros testes a gente fez isso aqui, né? Enviu o JSON. Como isso é form data, a gente só fala que é form aqui dentro, em vez de JSON. Então, form. E aí, quais são os dados que a gente vai passar? Então, a gente tem o username, username, que é o e-mail no nosso caso, né? User.e-mail.

**[01:19:20]** A Lucas falou que estava bem abstrato até agora pouco, mas faz sentido ver o Tolkien no edupor. Pô, massa. Então, legal. Tiverem dúvidas e vai mandando aí. E a gente precisa do password, que é a senha. Password. E aí, a senha é a senha do user. User.password. Massa? Legal. Então, em teoria, se a gente enviar essa requisição para lá, a gente vai ter que receber...

**[01:19:50]** Um 201 ou um 200? A gente vai ter que receber 200, né? Porque isso aqui não é rest, né? É token, então ele retorna 200 por padrão. Então, vamos fazer o seguinte, a search, a gente vai falar response, né? Response.status.code, vamos pelo status code, gente. Status underline code, é igual HTTP status.ok.

**[01:20:19]** É o que retorna aqui por padrão. Tá tudo bem. Não é created. Poderia ser created token. Não sei. Legal. E a gente quer ver se o token veio aqui, né? Basicamente a verificação que a gente quer é essa aqui. A gente quer saber se o token veio. Eu não tenho como saber qual é o token. Ah, eu até tenho. Mas aí eu vou ter que fazer 550 fixtures para descobrir qual é o token. Se o token gerado é o mesmo. Legal. A gente quer saber se veio o token.

**[01:20:49]** aqui dentro, né? Então, eu vou pegar o response JSON disso aqui, então response.json disso aqui e vou chamar de token. Se tiver dúvida vai mandando, então não responde, né? É, porque é dúvida sobre a aula, né, mano? Se você pergunta uma coisa que não tem nada a ver com nada, aí tipo assim, tem um monte de gente assistindo, tá ligado? E aí você acha que o seu tempo vale mais do que de todo mundo que tá acompanhando a aula, tá ligado? É por isso que eu não respondo. Então, a gente vai chamar esse token aqui,

**[01:21:31]** e vê se o Access Tolkien está aqui dentro. E aí, uma outra coisa que a gente tem que saber aqui é se o tipo do Tolkien, que foi o que a gente mandou aqui atrás, se é o Bear Tolkien. Então, a gente quer saber se isso aqui é verdade. Então, vamos voltar lá e ver o que é o seguinte. Então, a gente quer saber se o que veio aqui no Tolkien, a gente chama o responso de Jason aqui.

**[01:22:04]** Legal? Veio o retorno lá da API, que vai retornar isso aqui, né? O access token e tudo mais. Se a gente quer ver se deu 200 a resposta, se o tipo do token é bare token e se o access token está aqui, por enquanto a gente não vai validar em si a coisa que a gente quer aqui, né? Legal? Então vamos testar e ver o que vai acontecer. Eu acho que agora vamos começar a aparecer vários problemas aqui para a gente ir arrumando, mas tá tudo bem.

**[01:22:32]** Vai dar tudo certo. Legal. Primeiro erro. Vamos lá. Ó, eu coloquei aqui Form. Por que eu coloquei Form? Porque eu não sei. Era Deita, né? Vamos rodar de novo. Task Test. Legal. Agora deu outro erro. Olha o que ele falou aqui agora. Só o finzinho do erro já é importante aqui para a gente entender o que está rolando aqui.

**[01:23:05]** Pwd exception and no hash error. Ou seja, this hash cannot be identified. Make sure it's valid. Ou seja, o hash que foi gerado aqui, ele não é o que exatamente? Um token. O que que aconteceu aqui? Por que que ele não consegue validar se o token é de verdade a hora que ele manda aqui? Ele deu um erro aqui, quando a gente mandou o token.

**[01:23:38]** ele tentou chamar essa função aqui verify password e ele não conseguiu chamar essa função de verificação porque o dado que está salvo no banco ele não está incriptado ele não é um hash isso é por conta da nossa fixture a nossa fixture por padrão ela não cria o hash da senha lá no conf test então a gente vai ter que pedir para ele fazer a senha para a gente validar para ver se vai dar certo então isso é um problema na fixture

**[01:24:09]** Aqui na fixture de user, que a gente tem aqui embaixo, tá vendo que a gente adiciona tudo limpo aqui? User, tal, tal, tal. A gente, em nenhum momento, como a gente não passa pelo endpoint pra criar o user aqui dentro, a gente tá chamando esse teste, teste. Então, vamos lá. Então, a gente vai ter que chamar lá do security, né? Então, vamos lá. From FastAPI 0.securet import GetPasswordHash.

**[01:24:40]** E a partir desse momento, a gente vai chamar o GetPasswordHash. Aí agora a gente persiste no banco de dados o hash e não mais uma senha limpa. Resquícios da configuração passada aqui. Vamos rodar esse teste e ver o que que acontece agora? Falhou de novo. Ah, e por que que falhou agora? Agora ele retornou 401 Anautorized. Ou seja, uma coisa não bate com a outra.

**[01:25:18]** Ou seja, quando ele está fazendo essa verificação aqui para ver se o hash bate, ele não bate. E aí a gente tem um problema aqui, problema 2. Porque quando a gente está fazendo a chamada, quando a gente armazena esse user com a senha criptografada, a gente perde a senha limpa. Então, a gente precisa ter as duas senhas para fazer isso validar. A gente precisa ter no banco a senha encriptada.

**[01:25:50]** E na hora de fazer o teste, a gente tem que passar sem a limpa. Então a gente vai fazer uma coisa aqui, uma estratégia avançada aqui, não é? A avançada, eu estou dizendo gambiarra mesmo, não é? Uma coisa chamada monkey patch. E o monkey patch, ele se baseia em fazer alterações no objeto em tempo de execução. Então o que eu vou fazer aqui? Eu vou pegar isso aqui e vou chamar de password aqui. Olha que massa. Password.

**[01:26:18]** E a partir disso aqui, a gente vai encryptar essa variável chamada password. Massa. E aí aqui nesse usuário, quando a gente for retornar ele, antes de retornar, eu vou dar um user.e qual o nome que eu dei? CleanPassword. CleanPassword aqui. E aí eu vou passar o password para ele. Ou seja, a gente vai alterar esse objeto em tempo de execução. E aí aqui é interessante se vocês tiverem alguma dúvida sobre isso. A gente vai alterar o objeto user.

**[01:26:50]** em tempo de execução. Mas, durante o período de teste, a gente vai falar, olha, salva ele no banco com a senha encryptada, o hash da senha, mas, porém, com tudo entretanto, todavia, retorna para mim, o usuário também com a senha limpa. A gente só colocou esse dado em tempo de execução aqui. Ele não está no banco de dados, ele só está no objeto que a gente vai manipular aqui dentro do teste. Se a gente quiser dar uma olhada nisso, eu vou dar aqui um...

**[01:27:21]** Breakpoint aqui. Só pra gente rodar e ver o que acontece aqui nesse teste. Ele travou aqui, né? Só dá uma LL e a gente tá dentro desse teste do GetToken. Se a gente chamar o User aqui, você vai ver que o User tem todos os dados que a gente persistiu no banco. O ID, o username, o e-mail, o password do CreatedAt. E aí a gente tem esse CleanPassword, que é um objeto que a gente só colocou aqui, sabe?

**[01:27:52]** Só pegou isso aqui. Agora tem um nome chique para as gambiarras que eu faço. Sim, esse é um monkey patch, não? Legal. Então, a partir disso aqui, a gente tem as duas senhas aqui. Tanto a limpa quanto a suja. Então, a gente vai mandar limpa aqui, não? Então, a gente tem o clean password.

**[01:28:11]** e aí ele vai ter só durante esse scopo de teste esse valor maluco aqui ou seja durante o lifetime o tempo de vida que a fixtures tem ele não tá persistido no banco nem no banco de test isso aqui tá persistido massa então agora a gente consegue mandar as duas coisas a gente consegue ter o dado certo no banco e o dado certo pra enviar no teste fez sentido? Nice! ó lindinho tudo passando

**[01:28:54]** Agora a gente pode ir para o próximo ponto, que é autorização aqui dentro, né? Bom, a gente viu, né? A gente já tem um Tolkien agora, né? Então, agora na parte da autorização, a gente tem que dizer para as pessoas o que que está acontecendo aqui, né? Como é que a coisa está rolando e o que que está...

**[01:29:12]** Diferente, sei lá, eu quero alterar os dados do Takone, eu devo poder alterar os dados do Takone, não sei, eu sou admin, não, mas a gente não estava vendo a administração. Agora é a ideia de controlar os escopos dos users, quem pode fazer o que dentro da aplicação. Então, eu posso trocar a senha do Lucas? Não. O Lucas pode trocar o meu e-mail? Não. Eu posso alterar o...

**[01:29:35]** o username do Thiago? Não, então só cada pessoa tem o acesso ao seu próprio escopo aqui dentro, né? E basicamente o que a gente precisa disso aqui é no Putin o delete, né? Basicamente, uma pessoa não pode alterar a conta de outra e uma pessoa não pode deletar a conta de outra. A gente pode fazer isso na nossa própria conta, né? Esse é o objetivo da autorização aqui nesse primeiro momento.

**[01:30:01]** E aí o que acontece? Eu não quero que uma pessoa altere do outro e nem delete do outro, mas eu quero que quando a gente faça aquele get que a gente lista os usuários, a gente precisa estar logado para fazer isso. Essa é uma exigência que eu quero aqui. Então, para listar os users, precisa ter um Tolkien. Para deletar, o Tolkien precisa ser meu. E para alterar, também precisa ser meu. Então, essa é a ideia aqui da autorização.

**[01:30:29]** Permissões, controle de acesso para determinadas coisas dentro da nossa API, dentro do nosso escopo. Massa. E aí, para isso, agora, a gente vai chamar aquela coisinha do FastAPI de novo. Lembra que a gente tinha o OAuth2 Password Form? Agora, a gente não quer o form, agora a gente quer o bare. B-A-R-E-R. Se vocês forem escrever, a gente quer o bare-talking. Ou seja, a gente quer garantir

**[01:31:00]** que o Tolkien veio, ele foi enviado na mensagem para a gente. E aí a gente vai pegar, criar uma funçãozinha aqui chamada gaticurrent-user, ou seja, pega o usuário corrente. Uma coisa bem simples, só para a gente dizer o que é que veio, da onde está, sabe, o que está acontecendo. E isso aqui eu vou criar lá no Security. Também a gente pode criar isso dentro do Endpoint.

**[01:31:29]** Aí é contigo aonde você quer fazer isso aqui, né? Bom, beleza, vamos lá! Eu vou criar essa função chamada getCurrentUser lá no nosso security. E eu tô falando o que tanto faz porque depois a gente vai revaturar toda essa estrutura aqui, né? Mas tudo bem, vamos lá! Eu vou criar essa função chamada getCurrentUser. Aí essa função, getCurrentUser, ela vai depender...

**[01:31:58]** de algumas coisas que a gente quer aqui, então beleza, eu preciso da sessão do usuário, a gente precisa saber, a gente vai precisar checar o banco de dados para ver se essa pessoa existe ou não, o que está acontecendo ali dentro, então a gente vai importar as coisas do banco. E aí uma outra coisa que eu quero aqui é o seguinte, eu também quero saber se essa coisa veio com

**[01:32:30]** o esquema se veio com o bare token dentro da requisição, do header, do cabeçalho da requisição. Massa é basicamente isso, então a gente vai usar esse Depends aqui dentro. Legal, para fazer isso aqui a gente vai ter que fazer aqueles imports malucos do Fast API. Então eu vou importando aqui depois a gente vai arrumando, então vamos lá.

**[01:32:58]** Como a gente vai usar o GetSession, a gente precisa disso aqui. A gente vai importar o Depends, né? Então, from FastAPI import Depends. A gente precisa desse OALF schema que a gente vai definir aqui, né? Isso aqui. OALF token, a gente já vai falar um pouquinho sobre isso e a gente importa lá do Security esse modelito que a gente quer aqui, né? Massa. Então, o que acontece aqui? Esse OALF best...

**[01:33:34]** Bertoken é uma coisa que vai checar o cabeçalho da requisição que a gente mandar e vai ver se lá dentro tem um Bertoken, ou seja, se a gente está passando um campo no header. A gente vai ver direitinho como é que esse campo funciona aqui, mas, basicamente, se não tiver esse campo, ele vai direcionar isso aqui para essa URL, que é o barra Tolkien, que é o que a gente acabou de definir aqui. Ou seja, você está tentando fazer uma coisa deslogada?

**[01:34:02]** Eu te falo, ó, é aqui que você loga. Então, por isso que a gente passa aqui o token URL aqui dentro. Massa. Então, deixa eu importar aqui from sql alchemy ponto rm import session, só pra ficar bonitinho aqui. Nada sem cores. Vou jogar tudo isso aqui em cima de uma forma bem bagunçada mesmo aqui, hein? E a gente dá o format, tipo, ele se virar aqui. E aí, eu vou juntar esse offscheme.

**[01:34:37]** aqui em cima dessas variáveis que a gente estava fazendo aqui. E aqui não é fsd0, é fsd api0, no getSession. Legal, vou dar o format só para ele dar um jeito ali, então taskFormat, aí deixou tudo arrumadinho aqui, a ordem dos imports, e aí a gente está nessa função aqui, getCurrentUser, a gente quer validar quem é o usuário corrente dentro dessa aplicação.

**[01:35:09]** E a gente vai fazer isso via bare token, que é aquele token que a gente trouxe lá atrás. Legal? Só que pra gente chamar essa função, a gente precisa injetar ela de novo, né? A gente vai usar o sentido de injeção de dependência. A gente vai lá na função de get e vai falar, olha, pra você, pra eu saber se você pode fazer o get ou não, eu quero que você seja validado pela minha aplicação.

**[01:35:41]** E aí, essa função, quando a gente chamar o Get, ele vai usar a Injeção de Dependência e chamar essa função aqui de trás, o Get que o Indie usa. Massa, é basicamente isso aqui que vai acontecer. Eu só vou dar um Depends aqui no Get. Então, vamos lá no nosso app. E a gente tem aqui o Get, vamos lá. Get total, está um pouco mais bagunçado aqui, mas tudo bem. Eu vou chamar essa função aqui. Legal?

**[01:36:13]** precisa ter um usuário corrente para a gente poder executar esse get. Ou seja, para listar os usuários você precisa estar logado na aplicação. Aí a gente vai lá do security e importa, né? O get current user. Agora eu quero subir isso aqui, essa aplicação com vocês lá no swagger e quero mostrar o que que vai acontecer aqui. Vou minimizar tudo aqui e vou dar um f5. Olha que interessante. Para fazer

**[01:36:43]** O get pra gente listar tem um cadeado aqui. Então a gente precisa logar na aplicação, gerar um token. Olha que interessante. E é aquele token URL, tá aqui ó, o barra token. Olha que massa, então esse endpoint está protegido. Protegido por essa função aqui chamada get que a gente usa. A gente ainda não implementou ela.

**[01:37:12]** mas agora esse endpoint está protegido, ou seja, você precisa enviar o token, porque se não enviar o token, você não consegue mais passar pelo endpoint de get, isso aqui, porque ele tem essa dependência aqui dentro. Mas, só que para isso a gente vai ter que implementar o fluxo aqui. Eu só queria mostrar o cadeado aqui para vocês. Uma coisa que eu queria antes de a gente fazer a implementação,

**[01:37:47]** Olha, olha o que vai acontecer aqui dentro. Se eu rodar os testes agora, o teste do GAT vai parar de passar. Aqui, ó. Quando eu dou o client GAT, em vez de dar 200, ele dá anautorized. Olha que massa! Não funciona! E por que que não funciona isso aqui, né? Porque eu não tenho um Tolkien na hora de fazer o teste aqui, né? Então, aqui nesse teste do GAT, então teste... Qual que foi o teste que falhou? Vamos ver aqui de novo.

**[01:38:22]** teste read users. Esse teste ele não tem o token. Então eu preciso agora a partir de agora passar aqui o token. Então a gente vai ter que falar qual é o header aqui dentro. Só que para ter o token eu preciso gerar o token. Olha que massa. Então eu vou ter que fazer uma nova fixture que é quem vai me dar esse token.

**[01:38:54]** Então vamos lá, como é que a gente gera o Tolkien? Então eu vou precisar ir lá no ConfTest, eu vou criar uma Fiction nova, então a rouba PyTest.Fiction, e aí eu vou chamá-la de Tolkien. Massa? E aí para a gente gerar um Tolkien, o que a gente precisa? A gente precisa de um User, então User. E aí o que a gente tem que mandar? A gente vai ter que fazer, a gente precisa do Client, para fazer a requisição. Aí todas as coisas vão se conectando.

**[01:39:21]** que a gente fez até agora. Então eu vou chamar o response aqui, vai ser o client.post que a gente vai enviar uma requisição lá nessa coisa, então no barra Tolkien, e a gente vai precisar passar no data os dados que geram o Tolkien, então o username e o password, legal?

**[01:39:53]** E aí a gente tem o user.email, que é o que a gente está usando para validar aqui, user.email. E o password aqui é o user.cleampassword. Lembra disso, né? Porque a gente precisa mandar sempre o limpo para lá. Legal. Aí a partir desse responso, esse responso aqui, a gente já testou, né? SendPoint, a gente vai retornar ele, então return.

**[01:40:20]** o response, ponto jzone, e o que que a gente quer aqui? o token. Olha que massa, então a partir de agora, todo o teste que a gente precisar de o token, a gente pode passar ele porque ele foi gerado em uma fixture. A partir do username que a gente inseriu pela fixture. Massa? Então aqui é access token, deixei errado. Access token. Então a partir de agora, a gente tem o token.

**[01:41:00]** E aí, a gente passa aqui, né? O header, que é o cabeçalho da requisição que a gente precisa aqui no teste, vai mandar o token aqui dentro. Então, toda vez que a gente fizer um request para algum lugar que é protegido dentro da aplicação, a gente precisa mandar o header. E aí dentro do header tem um campo chamado authorization, ou seja, um campo de autorização. E a gente vai mandar o token que a gente recebeu. E qual é o tipo do token? O token é bad token.

**[01:41:34]** A partir disso, a requisição tem que conseguir acontecer, né? Pode ser que não dê certo o teste ainda, mas agora a gente tem todos os dados, todos os insumos pra levar isso pra frente. Vamos ver o que que rola aqui agora? Task Test. Legal. Ele falhou o teste Read Users. Ele falou que tinha que voltar algumas coisas aqui. Ele falou que tinha que voltar nada.

**[01:42:08]** mas voltou algum dado aqui. Interessante esse erro aqui. Ele falou, ia voltar nada, mas voltou um user. O que que aconteceu nesse video-users? Lembra que a gente tinha um teste aqui para validar que não tinha nenhum user na base? Esse teste já não faz mais sentido, porque para funcionar precisa ter um user na base, senão a gente não consegue gerar o Tolkien.

**[01:42:37]** olha que massa então esse teste já não faz mais sentido então a gente vai para o teste baixo aqui e copio o header que a gente tem aqui nunca em hipótese alguma vai conseguir fazer essa requisição e voltar nada porque sempre tem que existir um user ali dentro então esse teste não faz mais sentido mas esse caminho serviu para a gente entender tudo o que precisava acontecer aqui dentro olha que massa

**[01:43:12]** Então, a gente até validou que o nosso teste parou de fazer sentido. Muito legal, vamos rodar os testes agora de novo. Legal. Funcionou, a gente conseguiu entrar no get, mas a gente ainda não validou nada, né? Assim, beleza, o teste do get funciona, o read user vai trazer o user que a gente precisa, você poderia fazer ele dessa forma com users de user schema.

**[01:43:36]** Saca, então é isso. Melhor coisa que escrever teste é deletar teste, eu também acho, né? Porque a aplicação foi se modificando, né, nesse sentido. E aí a gente nem precisa chamar mais o read-users, o if-user, né? A gente pode chamar esse teste de read-users mesmo, porque não dá pra não ter um user na aplicação. Massa, passou. Lindo, olha! Maravilhoso, né?

**[01:44:00]** Beleza, funciona, mas a gente ainda não está validando o payload do token. A gente não está validando nada, a gente está enviando o dado, mas esse tipo assim, ah, beleza, está autorizado. Por que a gente não enviou nada, não retornou nada, a gente não valida nada naquela função? E aí chegou a hora da gente implementar a validação do JWT aqui. Então, o que a gente vai fazer aqui? Então, vamos voltar lá no security, aqui na função. A gente precisa decodar o token agora, né? A gente vai ter que chamar a função decode aqui.

**[01:44:35]** E aí, a gente vai ter que importar ela lá do JWT, de code. Mas, aí, a partir disso aqui, a gente vai pegar os dados que a gente tem aqui, então, eu vou chamar o token que a gente recebeu aqui, tá vendo? Que a gente depende dele, né? Então, a gente vai ver o token que a gente validou, a gente vai passar a secret key pra ele, e aí, se você quiser passar o algoritmo, você também pode passar, né? Porque a gente definiu uma variável aqui chamada algoritmo.

**[01:45:05]** E a gente vai tentar fazer o decode disso aqui. Try. Decode. Aí você vai falar, mas por que a gente vai tentar isso aqui? Não vai decodar. Porque pode ser que alguém envie uma coisa bomba para a gente. Uma coisa que a gente não sabe o que é. E isso vai dar erro. Se enviar um token que não é um token JWT, vai dar erro. Então a gente vai chamar o reception aqui. E a gente vai chamar esse decode error. Por que? Deu erro de decode. E da onde vem isso aqui? Lá da biblioteca do JWT. Decode error.

**[01:45:38]** Então, se alguma coisa acontecer aqui, a gente vai dar um rise também, rise. E aí a gente já escreve esse rise aqui. Então, a partir disso aqui, a gente vai ter o decode e a partir do decode a gente tem as cleans, que foram retornadas aqui, ou payload, que é onde estão as cleans. E aí dentro desse payload, a gente vai tentar achar o subject.

**[01:46:04]** que foi quem a gente mandou para cá o email ou subjet email que era quem tava lá no sub a gente vai ver pô isso aqui tem o sub porque se não tiver o sub vai ter que dar outro erro né porque como é que eu garanto que alguém é alguém pelo email se não veio o email que a gente enviou que foi assinado dentro do token sabe esse rolezão assim muito louco aqui dentro então eu vou fazer um seguinte se não vier a gente vai dar um rise também aqui e aí a gente vai pegar esse

**[01:46:34]** Credential Exceptions aqui. É esse Credential Exceptions, ele vai dar o mesmo erro e aí o que que é essas exceções aqui, né? São uma coisa que a gente vai definir aqui dentro mesmo. Aí lá do Fastchip a gente vai importar o HTTP exception e vai falar o seguinte, olha, qual é a exceção que a gente vai retornar aqui? Anautorize it, né? Não conseguimos alterar, não conseguimos autorizar. Eu vou copiar daqui, a gente vai conversando junto aqui.

**[01:47:13]** Eu não consegui autorizar, ou seja, porque você não mandou uma credencial válida. Então você tem que autenticar de um jeito que é... Humbert Tolkien. Massa? Então é esse o erro que ele tem que dar aqui. Ou seja, se o JWT não valer, ou seja, se for uma coisa que eu não consigo decodar, ou se não veio o e-mail, que é o que para mim que valida essa coisa, a gente vai estourar essa exception. E aí, vamos importar aqui, então, from HTTP.

**[01:47:44]** import HTTP status. Só pra gente ter isso aqui, aqui embaixo. Então, a gente vai levantar essa exceção, Anautorizer, se você vier com essas coisas. Então, beleza, aqui a gente viu todos os tipos de erros possíveis que podem acontecer, né? Mas a gente não fez, dá certo, né? Só que dá certo, é bastante simples, né? A gente vai verificar se quem veio, né? Lá no, no sub.

**[01:48:18]** era o e-mail que a gente queria, então a gente vai buscar por ele. Então aqui ó, a gente vai buscar lá na tabela de users, onde o e-mail é igual o e-mail que veio no sub, né? O e-mail que tava dentro do JWT. Se não tiver, né? Se esse user não for cadastrado, porque pode ser que alguém encrypte um Tolkien com o e-mail que não existe, ou que alguém já tenha deletado a conta, mas ainda tem um Tolkien válido, saca? Isso é uma coisa que pode acontecer.

**[01:48:47]** Então, a gente levanta essa exception também. Se não, a gente retorna o user. Olha que bonitinho. Fica bonitinho aqui, né? Então, eu vou importar as coisas que ficaram faltando aqui, né? Então, vamos lá. From SQL Alchemy Import Select. E aqui, de dentro da nossa aplicação, From FastAPI0.Models Import User. Eu acho que eu não esqueci nada aqui, né?

**[01:49:24]** Então, legal, se não conseguir decodar, erro. Se conseguir decodar, a gente busca. Se não tiver o user que a gente quer, rise. Se der certo, a gente retorna um user que a gente tinha aqui dentro. Basicamente, esse é o esquema. Se a gente rodar os testes, não funcionou porque tem várias coisas para formatar, task format. Deixa ele formatar, vamos dar um task test.

**[01:49:49]** Beleza, em teoria, tudo continua funcionando. Por que que isso continua funcionando? Porque aonde a gente aplicou o getCurrentUser, que era a função de get, ela não usa o currentUser pra nada. Tá tudo bem, porque a gente só precisa que alguém esteja logado e que esse login seja válido dentro da aplicação. Então, pra essa parte, continua tudo valendo. Porém, com tudo entretanto e toda a via, lembra que a gente queria

**[01:50:17]** que deletar e alterar, você só pudesse fazer isso se a conta fosse sua. E aí é aquela coisa linda, maravilhosa. Ou seja, como é que eu altero um usuário corrente? Eu preciso saber se ele é o current user. Ou seja, se eu quero alterar o ID, que é o ID do mesmo user que a gente acabou de validar no JWT, a gente deixa passar. Se não, dá erro.

**[01:50:50]** Olha que massa, então lembra que aqui dentro do put a gente tinha essa busca no banco de dados e tal, fazer umas coisas mais maiores aqui? Lembra que a gente faz essa coisa aqui? Busca no banco, aí depois a gente vai fazer tudo isso aqui? Então, a gente pode chamar o current user aqui, current user, que é do tipo user, né? A gente pode passar aqui e ele é depends da função get current user, get current user.

**[01:51:25]** A partir disso aqui, eu não preciso mais fazer essa busca, porque a gente já tem o user, a busca já foi feita lá no getCurrentUser. Então, eu não tenho mais esse código. Legal. Eu não preciso mais saber se ele foi criado ou não, tipo assim, se esse usuário existe ou não, porque isso aqui vai dar erro lá nas credenciais também. Então, o que que a gente precisa aqui? Alterar esse userDB para o CurrentUser?

**[01:52:06]** porque é ele que vai ser alterado aqui e a gente cai no try que a gente tinha e aí eu preciso só dar aquele erro de autorização aqui no código, ou seja, se o current user, ou seja, for diferente do ID que ele quer alterar, a gente vai dar erro de credencial. É basicamente isso aqui, ou seja, se

**[01:52:38]** O usuário atual, ou seja, quem está logado, quem enviou o Tolkien JWT, foi diferente do user que ele quer modificar, ele não tem permissões suficientes. E aí a gente retorna o Forbidden. Lembra que antes a gente estava retornando o Anauthorized, que era o Status 401. Você não pode fazer isso aqui porque você não tem autorização. Agora, a gente está...

**[01:53:11]** Dendo um Forbidden, falando, ó, isso que você quer? Hmm, você não pode fazer isso aí, hein? Legal, é isso. Vamos rodar os testes agora? O meu não vai quebrar. Deixa eu dar um format, deixa eu rodar o teste de novo. O meu não vai quebrar? Não? É claro que quebrou. E por que que quebrou, né? Porque agora a gente depende do current user. E para a gente ter o current user, precisa enviar...

**[01:53:46]** Quem é de verdade sabe quem é de mentira, adorei esse comentário. Ou seja, pra fazer o update, eu também agora dependo do Tolkien. E aí eu vou ter que mandar o Tolkien aqui, que é essa coisa bonitinha aqui, esse header aqui, que vai se repetir basicamente em todos os testes. Então, se eu mandar o header, eu vou conseguir fazer o update desse user, vamos ver. Hmm, deu erro.

**[01:54:20]** Ah, mas ele deu erro em outro lugar. Ele deu erro no teste de integridade, porque o teste de integridade também é um teste aqui do... quando a gente tenta alterar um usuário por um usuário que já existe, né? Só que pra fazer isso aqui, eu também preciso do Tolkien, né? Agora, fixture de Tolkien vai ficar em todo lugar. Então, o erro de integridade, pra eu fazer a alteração, eu preciso enviar o Tolkien, senão...

**[01:54:50]** vai dar não autorizado. Vamos rodar agora e ver o que acontece. Legal, todo mundo passou. Ó, maravilhoso. E aí agora a gente precisa alterar esse teste, alteramos, fizemos juntos aqui, agora tem o red, o teste de integridade também está passando porque a gente está mandando o cabeçalho da requisição e agora falta o delete. E o delete também é o mesmo esquema. Eu não posso deletar alguém na aplicação.

**[01:55:24]** que não seja a pessoa que gerou o Tolkien. Ou seja, não vou alterar a conta de ninguém. E para isso, simplesmente, a gente não vai precisar mais fazer a busca no banco. Não vai ter not found, porque o usuário tem que existir para ter um Tolkien. Então, a gente só vai precisar de novo do Current User. Você viu que a implementação do JwT tirou um monte de coisas dos códigos, um monte de coisas meio duplicadas que a gente tinha.

**[01:55:58]** Então, a gente vai chamar o current user, a gente vai deletar o current user daqui, né? E tem aquela validação, né? Que, por enquanto, está duplicada, que é o... Not enough permission. Ou seja, você vai deletar a conta do amiguinho, você não pode, né? Então, vai dar... Not enough permission. Legal! Vamos rodar o teste, vai falhar, né? Por que que vai falhar? Porque eu não passei o header no teste do delete. Então, vamos lá...

**[01:56:28]** No teste do delete, a gente vai precisar do Tolkien. E aí pra deletar, a gente vai ter que mandar o Tolkien aqui. Uma outra coisa que eu tinha feito na outra aula, que eu acho que é legal pra gente colocar aqui, é... Aqui a gente tá passando User 1, a gente poderia passar o ID do User mesmo aqui. User.id. Já fica dinâmico, fica certinho, né? E aí agora a gente vai precisar do Tolkien, né? Pra fazer o header aqui.

**[01:57:08]** Vamos rodar? De novo, teste. Yeeey! Tudo passou, tudo passou. Se não tivesse o user ID, podia até tirar esse if. Sim. É uma boa prática criar usuários ver a requisição de API? Sim, como é que a gente criaria? Tipo assim, como é que você criaria uma conta se você não usasse o esquema das APIs? Tipo assim, essa é a pergunta, assim. Tipo assim, ah, eu tô usando a aplicação. Eu preciso criar a minha conta. Como é que eu vou fazer isso?

**[01:57:42]** Beleza, depois dessa volta toda, fechamos, atualizamos o teste de delete, e aí eu deixei um teste aqui, que é para a gente testar aquele momento do Tolkien, que é um Tolkien inválido. Lembra que a gente tinha feito algumas coisas aqui no security, que a gente validou aqui? Pô, vamos ver se o payload tem sub, se tem algumas coisas ou não. Só para a gente garantir que isso aqui está acontecendo, eu criei esse Tolkien.

**[01:58:16]** A gente tá usando a rota de delete, mas poderia ser qualquer uma. Olha que interessante isso aqui, né? Então, testa o token inválido. A gente vai mandar qualquer endpoint poderia ser, qualquer user poderia ser, a gente vai mandar um header. Cumber token inválido. E aí, por tá inválido aqui, aqui o token, ele vai dar erro de decode. Tá vendo? Aí ele vai cair nessa exception aqui. Deixa eu rodar o...

**[01:58:52]** O HTML cove aqui, só para vocês entenderem aonde ele não está passando aqui, né? Deixa eu pegar aqui no security. Ó, tem dois casos aqui onde a gente não caiu. Tem mais, né? Mas é esse caso aqui, ó. Tem esse credential exceptions, ou seja, a gente não chamou um token bomba aqui para saber se ele vai cair aqui, né? Então é isso que esse teste testa. Se, quando a gente mandar o token bomba, ele vai cair lá.

**[01:59:20]** É basicamente isso, nem precisa explicar muito o teste aqui, né? Tipo assim, a gente foi lendo junto, então vou copiar e executá-la. Caramba! Copy. Então eu vou lá no test security, vamos colocar isso lá. Test security. E aqui não tem um HTTP status, então vamos lá. From HTTP import HTTP status. Massa. Aí tem que dar não autorizado, que é a coisa da segurança aqui, né? Unauthorized.

**[01:59:59]** Vamos ver. Task test. O teste passou, ou seja, o teste JWT em vale de Tolkien. Se a gente falar no Coverage, a gente vai ver que agora essa parte está aqui. A gente só não tem um Tolkien válido com um Subject que não funciona, mas vocês já sabem onde vão cair esses dois testes aqui, não? Não preciso nem contar onde vocês vão escrever esses testes aqui, não? Nos exercícios!

**[02:00:36]** Então, legal, aquele coverage lá que ficaram faltando duas coisas, eu quero que vocês dêem uma pensada, né? Então, a gente tem que cobrir onde o user não é encontrado e o caso onde o e-mail não é enviado dentro do subject, né? Então, essas duas coisas são testes que eu gostaria que vocês fizessem aqui. Suspeitei desde o princípio. E aí, o exercício 3, ele é um pouco mais cabeçudo de fazer aqui.

**[02:01:08]** que é o seguinte, eu quero que vocês revejam tudo, eu revejo tudo que vocês criaram até então, lembra que as coisas que a gente está fazendo, que eram os exercícios ali, a gente criou um...

**[02:01:22]** o get de um só, a gente criou alguns outros cenários de teste que eram exercícios e eu quero que vocês revejam eles pra ver se eles fazem sentido, né? São todos os testes que deram 409, né? Lembra que eu falei, ah, vai cobrindo isso aqui, vai cobrindo isso aqui no outro? Então, eu quero que vocês tenham uma olhada nisso aqui e ver se eles fazem sentido e tem aquele get, né? Que é o get de um user só. Eu quero que vocês garantam que ele tá funcionando, né? Então...

**[02:01:50]** É pra ir fazendo isso aqui, né? Apunha lá nos pelos clases, que é isso. E aí não esqueçam de responder o quiz da aula, né? De tudo o que a gente viu até agora. E como hoje, eu tomei um pouco mais de tempo de vocês, né? Desculpem por isso. Liberei 10 minutos mais cedo quase todos os dias, mas hoje me exediu um pouco no tempo. Então vou cometando aqui.

**[02:02:31]** aqui ó, protege os endpoints de getput delete com a autenticação, vou subir lá pro meu rap, então quem quiser pegar lá e dar uma olhada tá liberado o que a gente vai perguntas pra fazer, eu vou ficar aqui mais uns 5 minutos pra gente responder as perguntas e de novo, né, Vera? Eu não preciso explicar isso, né? Perguntas que tenham a ver com o foco da aula, né? Por favor, respeita o tempo das outras pessoas, né? Então é isso, mas quem tá de boa, tá liberado, pode descansar e tudo mais

**[02:03:01]** E aí eu fico aqui para responder essas perguntas. Se alguém te venha.

**[02:03:12]** Fez sentido né? Enquanto vocês escrevem perguntas, vou perguntar se fez sentido, se vocês têm alguma dúvida meio cabeluda, senso sobre isso. Eu sei que é muita coisa, é muito pontinho, sabe? Esse negócio tipo assim, pega um negocinho e aí esse negocinho encaixa no outro negocinho. Tipo assim, tudo o que a gente fez hoje meio que foi reencaixar os componentes que a gente já tinha, né? A gente introduziu os tokens, né? Mas...

**[02:03:36]** Mas ao mesmo tempo, tudo foi meio que encaixando, uma coisa ou não a outra, assim. A fixture daqui com a fixture de lá que pega um negócio daqui torce e faz uma outra coisa. Tem várias coisinhas, né? O Germano fez uma pergunta legal, ele falou. Esse Alph já poderia colocar em produção? Ainda não. Porque tem algumas coisas aqui que precisam acontecer nessa autenticação que ainda não foram feitas, né? E essa é uma pergunta interessante porque...

**[02:04:05]** Se eu olhar lá no material de texto, aula 8, aula 9, é isso aqui, tornando o sistema de autenticação robusto. Então, a gente vai mexer mais nessas coisas aqui. A gente ainda não fez tudo que era para fazer aqui.

**[02:04:32]** Então, agora era uma ideia só pra gente introduzir o Tolkien, e mostrando onde tem autorização e tudo mais, mas a gente ainda tem muita coisa pra fazer, tem que testar aqueles minutos malucos que a gente deixou, a gente foi deixando, né, passando por ali, né, mas tem algumas coisas ainda que a gente precisa rever, e a gente vai rever isso lá na aula 9, depois que a gente estruturar, deixar melhor o projeto, arrumar a casa, né, porque tá muito bagunçado, né.

**[02:04:58]** Tipo assim, é um arquivão com os dentas linhas e aí é tudo teste, tá tudo misturado. Vamos arrumar isso aqui pra gente ir mexendo pontinho por pontinho. Takone fez uma pergunta muito legal aqui. Nas clãs do JWT tem um campo em meio. Valeria usar ele no lugar do Sub já que estamos usando de meio? Poderia ser, sem nenhum problema, né? Mas nesse caso...

**[02:05:25]** É que assim, o subject, ele é usado pra gente saber de quem é o Tolkien, tá ligado? Tipo assim, é uma forma de identificar o autor daquela coisa que fez essa assinatura, né? E é por isso que a gente tá usando o e-mail no subject. No mundo ideal, no mundo ideal, a gente não deveria usar o e-mail no subject, né? Mas, saca, a gente vai ter que pensar no identificador, alguma coisa nesse sentido.

**[02:05:57]** O e-mail ficaria no e-mail, mas como o e-mail é a coisa que o identificador a gente usa no seu objetivo, por esse motivo. Hoje é praticamente uma convenção usar o token para todas as aplicações, certo? Tem situação que o token seria só a frescura. Não, o token é a coisa que garante a autorização das coisas, então não é a frescura, ele é uma forma de usar. Mas existem várias outras formas de fazer autenticação e autorização, que não dependem necessariamente do token.

**[02:06:27]** O token, trafegado via bare token, ele é uma das formas de resolver o problema. Você poderia usar isso como cache de banco de dados. Aqui a responsabilidade está sendo dada para o cliente. O cliente tem que salvar o token usando nas outras exições. Mas se a gente usasse um browser, por exemplo, fosse uma aplicação REST, que tem HTML, que a gente conversa com ela, você poderia usar cookies. Então...

**[02:06:54]** Tem cookies, tem Session, tem armazenamento de banco de dados de cash, tem o JWT. Então existem várias formas de fazer tanto o transporte do Tolkien quanto a utilização da autorização. Então tem várias formas de fazer isso.

**[02:07:15]** Então, o Tolkien é uma delas, né? Não acho que é uma questão de frescura. Tem várias formas. E aí pode ser que você não queira essa responsabilidade no server dela pro cliente. Então, a gente vai usar via Tolkien. Se a responsabilidade for do browser, a gente vai usar cookies. Se a responsabilidade for do servidor, a gente poderia usar, falar um cache, então, sessions, né? Então, meio que isso varia de aplicação pra aplicação, assim. Depende muito do que você quer, especificamente.

**[02:07:46]** Aí o André fez uma pergunta, qual o sentido em não permitir o acesso para usuários não autenticados se os usuários podem usar o endpoint para criar uma conta? Porque imagina o seguinte, você vai entrar numa aplicação, você tem que criar uma conta, né? É a sua área alogada e a partir daquele momento eu posso saber o que que aconteceu ali naquele caso. Então, por exemplo, imagina o seguinte, você pode ver o...

**[02:08:11]** O... sei lá, vamos pensar numa aplicação aqui. Você pode ver todas as coisas no Mastodon, porque elas são públicas. Mas se você quiser publicar no Mastodon, você precisa ter uma conta, certo? É porque nesse sentido, a gente está fazendo só o gerenciamento dos users aqui no primeiro momento. Mas depois da nossa aplicação vai ter outras coisas. E essas outras coisas você vai ter que estar logado, você vai mexer nas suas próprias tarefas, sabe? Nesse sentido.

**[02:08:38]** Mas a ideia é que qualquer pessoa possa criar uma conta em qualquer aplicação, né? Saca. Saca, então tipo assim, é uma aplicação pública. As pessoas podem criar contas e tudo mais. Aí o Pedro mandou, pra que serve o refresh do Tolkien? A gente vai ver isso na aula 9. A gente vai conversar sobre o refresh do Tolkien, então eu não vou...

**[02:09:07]** cortar a caminho aqui. Aí o chinodinho falou, eu utilizo o UID como sub. Quando usar o troca sem, o UID também muda. Logo, todos os tokens são invaliados. Olha que massa, é uma outra forma de ver isso aqui. Onde eu consigo ver os tópicos da aula? Na minha visão, na minha visão não parece como você mostrou. Como assim? Os tópicos da aula aqui, eles estão aqui em aulas. Então todas as aulas aqui. A gente fez a seis hoje.

**[02:09:46]** E aí a gente vai voltar nesse assunto lá na 9. Que a gente vai tornar esse sistema de autenticação um pouco mais robusto. Bom, então é isso. Vocês não tiverem mais perguntas, eu vou ficar por aqui. A gente se vê na quinta-feira. A gente vai dar uma tapeada, né? Modar um pouquinho mais as coisas e dar uma organizada na casa aqui. Massa? Bom.

**[02:10:23]** Uma coisa é Authentication, outra coisa é Authorization. A gente ficou conversando um pouco sobre isso na aula. Um beijo para vocês, valeu! Até quinta-feira e a gente se vê. Tchau!

