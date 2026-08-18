# Transcrição da Aula: aula-03.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:09]** Olá, pessoas. Boas-vindas a mais um dia aqui do nosso curso de Fecha API. Eu sou o Dono Sauron e boas-vindas aí todo mundo. Sintos em casa. Antes de começar, eu queria um feedback de vocês para saber se o som está legal, se o áudio está bom. Vocês estão me ouvindo? Barra me vendo, antes de tudo, para a gente poder começar bem. E é isso. Boa noite. Olá. Como vão vocês?

**[00:00:37]** Bom, pelo boa noite, presumo que a pessoa me ouviu e me viu, né? Então, eu vou começar aqui com vocês. Bom, hoje é nosso quarto encontro, nossa aula de número três, e a gente vai começar a estruturar o projeto, criar um pouco dessa coisa que a gente chama de Krud, que é Create, Read, Update, Delete, que tem a ver com aquele rolezinho que a gente falou na aula passada, que era o Put, Gat, Pat, Delete.

**[00:01:03]** Então, esse é o esquema. Bom, como sempre, não custa nada dizer. Entra lá no link da aula se precisar de alguma coisa, de algum reforço e tudo mais. Então, tá tudo aqui. Sempre bom lembrar que tem um material em texto e o material em texto é super importante da gente ver. Albano, deixa eu agradecer ao Super Chat aqui, se a gente começar. Obrigado, mano, isso me ajuda muito. Valeu aí demais. E bom, antes de de fato, né, tem mais.

**[00:01:34]** a gente assistindo o que likes galera vamos aí ajuda nós aí a chegar e mais gente com isso aqui é conteúdo de graça vamos fortalecer aí

**[00:01:44]** Bom, o que a gente vai conversar nessa aula em específico, né? Hoje a gente vai fazer a aplicação prática de tudo que a gente viu na aula 02. A gente vai conversar sobre HTTP, sobre os verbos, sobre os status codes, sobre os esquemas, tudo que a gente viu na aula passada, que a gente começou a trocar a ideia, a ver como é que estava funcionando e tudo mais. Agora a gente vai trazer isso por aspecto de código mesmo.

**[00:02:11]** Então, como é que a gente estrutura isso, né? E a gente vai ver essa relação entre crude e métodos HTTP, status codes e verbos. A gente vai aprofundar um pouco mais no paedentic, né? A gente criou um modelo de mensagem muito simples, então a gente vai fazer mais coisas, vai escrever testes para tudo hoje, hoje a gente vai cansar de escrever código, já vou logo dizer, códigos e testes, né? E a gente vai fazer um gerenciamento mínimo, né? Para cadastros, como cadastrar...

**[00:02:36]** Sabia, aquele tipo de coisa, cadastro, altero o cadastro, deleto o cadastro, listo os cadastros, esse tipo de coisa que a gente vai brincar aqui na aula de hoje.

**[00:02:44]** Então, bom, na aula passada, a gente tinha conversado um pouquinho sobre essa relação arquitetural da rede que envolve clientes e servidores, né? Então, a gente tem de um lado um cliente que basicamente a gente viu, a gente brincou com o HTTP, né? Mas foi só pra ver o cabeçalho, a gente viu o browser como cliente, né? Então, a gente faz essa requisição, envia isso pro servidor, né? Pra URL do servidor, onde tem alguém esperando, né? Um endpoint, que é aquele barra que a gente criou.

**[00:03:12]** ele vai processar essa requisição e vai retornar para a gente e a gente vai fazendo essa troca de mensagens via rede com esse servidor, essa aplicação que a gente está desenvolvendo aqui nesse curso de uma maneira geral.

**[00:03:27]** Então, a gente vai criar Endpoints, e a gente já vai entender o que é um Endpoint, para cadastro, recuperação, alteração e deleção, né? Muito bonito de falar, né? Cadastro, recuperação, recuperação é o get, alteração é o put, deleção, saber, esse tipo de coisa, né? E aí, para tudo isso, a gente vai se concentrar em uma coisa que a gente vai chamar de user.

**[00:03:51]** ou um usuário, um cliente, alguém que faça parte da nossa aplicação. Sabe, grande parte das aplicações tem essa coisa de fazer um cadastro, né? Então, a gente cadastra pessoas, cadastra tarefas. Sabe, vamos pensar no sentido mais simples de todos que a gente pode usar esse tipo de coisa. Então, uma pessoa quer se registrar na nossa aplicação para poder fazer um login, ela tem que poder mudar os dados. Imagina que ela troca de e-mail, sabe? Ah, um dia ela não quer mais fazer parte, então ela deleta essa parada, então...

**[00:04:21]** É basicamente esse tipo de coisa nesse contexto que a gente vai trabalhar aqui hoje. Esse recurso único chamado users e a gente vai trabalhar com eles em vários endpoints. Massa? Julio, obrigado por se tornar membro. Um beijo para você. Valeu demais. Então quando a gente fala nesse sentido de operações com dados e aqui a gente está envolvendo mais a parte de trás, não a parte da requisição web em si.

**[00:04:52]** A gente costuma usar essa sigla, ela é muito famosa na internet que é o crude. Tanto que está até no título da aula, está na thumbnail. E o que significa crude? crude é create, ou seja, a gente pode criar um recurso na nossa aplicação, falei muitas coisas com R. Na nossa aplicação, como adicionar novos registros, ou seja, para um sistema de...

**[00:05:18]** Pessoas, né? A gente tem que poder cadastrar pessoas na nossa base. Então, imagina que você tem uns clientes e precisa cadastrar esses clientes ou a sua aplicação registra qualquer outro tipo de recurso. Nesse caso, são users. Aí tem o region, que é ler. A gente costuma traduzir isso como recuperação de dados, né? Que é, seja, pegar os dados que estão em alguma base e trazer para frente.

**[00:05:42]** Tem o U de update, atualiza, modifica o registro, troca o e-mail, troca o nome, está lá e rei minha data de nascimento, vai lá e corrige. E o delete, o delete ele é meio auto-explicativo, para a gente poder deletar esse tipo de coisa. Para quem?

**[00:05:58]** Se perguntou um pouco na aula passada, né? Por que a gente viu tanto de HTTP e tudo mais? Acho que esse slide resume meio que essa relação em que a gente tem, né? De todas as coisas, né? Então a gente tem um recurso, que é qualquer coisa, né? Lembra do barra Recurso na URL? Então a gente tem um recurso único.

**[00:06:17]** E esse recurso é capaz de fazer todas essas operações da nossa API. Então, a gente tem que ser capaz de criar, ler, atualizar e deletar. E cada uma dessas operações está relacionada com mensagens, troca de mensagens via HTTP. Então, post getput delete.

**[00:06:35]** E aí, cada uma dessas coisas, a gente viu que tem seus status code, né? Pô, criou, deu certo, post, retorna, created, né? 201. Get deu certo, 200. Output deu certo, 200. Delete também, 200. Depende, às vezes é 204. Cada um tem seu lance aqui, mas basicamente essa é a relação, né? Entre o recurso, a coisa que a gente quer poder manipular dentro da nossa aplicação, sei lá, pode ser... Vamos pensar, tipo, num Instagram da vida. Então, tem que conseguir...

**[00:07:01]** Opa a minha foto, com a minha legenda, poder alterar a legenda, poder deletar a foto, poder ver as fotos que eu tenho, sabe? Então esse recurso poderia ser qualquer coisa dentro da nossa aplicação. Vai ser user porque user é uma coisa meio mais simples, né? Para a gente poder começar com isso, né? Fazer o cadastro e tudo mais. Então, basicamente isso. A gente envia 100 precis dados para poder trocar ideia conservadora via HTTP e o que a gente espera são essas operações que a gente vai chamar de crude.

**[00:07:30]** Massa legal faz sentido aqui, o que cada uma dessas coisas representa, vão conversando comigo. É interessante esse papo. Bom, quando a gente faz essa coisa, a gente precisa efetivamente trocar mensagens via HTTP com alguém, com algo, com um servidor, com uma aplicação, que a gente está servindo e tudo mais. Então essa relação, por exemplo, se eu quisesse

**[00:07:56]** trocar essa mensagem e a gente falou que ia trocar as mensagens via JSON ou JSON ou JSON. Chame como quiser isso aqui. Eu penso que a gente fazer uma troca de mensagens parecida com essa. Então vamos supor que eu queira transferir os dados para o servidor para fazer a criação.

**[00:08:15]** de um recurso. Esse recurso, no caso, é user. Então, eu quero criar um usuário na nossa aplicação, fazer o cadastro dele, né? Então, a gente vai mandar alguns dados que precisam para a gente poder cadastrar ele na nossa base. Poderia ser vários outros, né? Eu peguei alguns de exemplo que acho que fazem sentido, que acho que fazem sentidos para a gente poder saber.

**[00:08:37]** e interagindo. Então, por exemplo, eu tenho o username. É sempre bom a gente ter um nome de usuário, um alias, alguma coisa que represente o nome daquela pessoa na nossa aplicação. Por exemplo, em qualquer rede social você tem um handle, uma rouba. A rouba, seu nome. Aqui poderia ser a rouba do Nosauro, dentro da minha aplicação. É uma coisa que me identifica como usuário dentro do contexto da aplicação. Tem o e-mail, caso a gente precise enviar alguma informação, fazer uma confirmação, sabe?

**[00:09:06]** Cria aí sua conta, confirma aí que é você, clica nesse link. E uma senha, porque a gente vai logar dentro da aplicação em algum momento que não vai ser hoje. Então esses são os dados que a gente precisa enviar para um outro lado. A gente chama essa troca de mensagens, esse dado que vai partir do cliente e vai para o servidor de payload. São os dados que a gente vai enviar.

**[00:09:29]** quando a gente for fazer nossa requisição para o servidor. E o servidor pode responder algo nesse formato ou não, dependendo exatamente de como a nossa aplicação vai se comportar agora que a gente vai fazer ela. Eu penso num formato de dados de cadastro de usuário como isso aqui, né? Então, uma coisa simples, né? Enviou o seu nome de usuário, o render, o que você quer, o seu e-mail, sua senha. Aí para alugar depois, você pode usar o e-mail e a senha ou username e a senha e fica a critério de quem quiser depois no futuro.

**[00:09:59]** Para a gente traduzir isso aqui, esse payload, essa coisa, lembra que na aula passada a gente conversou um pouco sobre esquemas, sobre como a API tem que dizer para a aplicação.

**[00:10:12]** no sentido de tipo, ó, os dados que eu recebo estão nessa documentação. Lembra daquele caso de sepedante que alguém falou, né? Tipo assim, ah, a burocracia começou. Então, é exatamente isso. Então, a gente pode converter esse modelo de dados, né? Esse JSON que a gente vai trafegar na rede. Em uma classe ou um modelo ou um esquema, algumas pessoas chamam isso de DTO, né? Data Transfer Object. Cada literatura vai chamar de um nome.

**[00:10:38]** No Python, a gente costuma chamar isso de esquema mesmo. Algumas pessoas chamam de modelo. Então, é mais ou menos essa tradução que a gente vai ter que fazer aqui. Então, vamos pensar. Quando a pessoa mandar essa mensagem pra gente, a gente quer garantir que esses três dados estejam na mensagem e que esses três dados, como username, password e email, sejam ambos do tipo strings. E a gente pode criar esse documento lá onde a gente chamou naquele arquivo chamado esquemas.

**[00:11:07]** poderia ser um bom lugar para a gente começar. Então, vamos lá! Eu estou aqui no meu projetinho, o Fast API 0, que foi o que eu dei o nome para essa nossa aplicação, e a gente tinha aquele arquivo chamado esquimas, onde a gente definiu o message aqui. Então, vamos pensar o seguinte, se a gente vai tratar desse dado, um dado de user, que é o nome do nosso recurso, eu gosto de nomes explícitos.

**[00:11:36]** Então, acho que chamar de user-esquima, que é o esquema, o esquema, o contrato do user, daquele recurso que a gente quer gerenciar. Então, eu vou dar esse nome para ele aqui. Então, eu vou chamar, deixa eu aumentar um pouco a fonte aqui, eu vou dar um class de user, o esquema do user, que é o recurso e o esquema dele, user-esquima.

**[00:12:07]** E eu vou chamar isso de Base Model. Vou dar de Base Model aqui. Legal, temos essa coisa. Quais eram os campos? Username, e-mail, e... Oh, importei o e-mail, ele sem querer. E-mail e senha. Eu chamei senha em português ou inglês. Em inglês, né? Password. Password. Palavra chave.

**[00:12:33]** E aí, bom, basicamente segue aquele mesmo formato que a gente tinha visto antes, né? Alguma coisa, né? Alguma chave que a gente tem nesse contrato e cada coisa dessa chave é alinhada com um valor específico aqui, né?

**[00:12:47]** username é do tipo string, é um tipo de dado de texto. A gente também tem um email que é um tipo de texto e o password que também é um tipo de texto. Basicamente todas essas coisas que a gente quer gerenciar são textos. A gente vai receber um email, uma senha, uma string.

**[00:13:04]** Tudo é string, né? Não tem número aqui, não tem, sabe? A mesma sua senha foi um, dois, três, quatro, não sei o quê. Ainda pode ser uma string, né? A string é uma coisa mais genérica, né? Quando a gente costuma receber dados.

**[00:13:18]** Bom, o pai dente que tem algumas coisas muito legais, muito sensacionais que a gente pode juntar com isso, né? Que são tipos que não são tipos primitivos que a gente tem na linguagem, né? O pai dente que tem esse tipo chamado email string. Ou seja, além dele validar, né, quando a gente for colocar isso na documentação e falar, olha, tem que ser um texto, uma string. Você poderia falar, tem que ser um email. O email não deixa de ser uma string, né? Por si só, mas ele é um email. Então...

**[00:13:46]** ele segue aquele formato de ser um e-mail, não sei o que lá, a roba, não sei o que, ponto, sei lá, net, ponto com. Então você poderia trocar esse e-mail aqui por e-mail string. E aí você fica mais corretinho, né, do tipo de dado, da estrutura, que a gente vai conversar aqui com o cliente e a documentação, né.

**[00:14:13]** Bom, vamos implementar essa coisa de criar esse user, esse endpoint, essa coisa que a gente... Beleza, a gente já tem o esquema, a gente tem um contrato definido, mas como é que a gente coloca isso dentro do código? Bom, todo o ato de criação que a gente viu aqui atrás, ele está relacionado com um post, um método post, ou seja, post significa enviar algo para mim que eu vou criar esse recurso pelo create, é o C do crude.

**[00:14:43]** Então, a gente vai chamar lá do Fast API o appzinho que a gente tem e a gente vai chamar ele de post. É uma coisa que a gente não tinha feito até agora, a gente só tinha o get. Aqui eu vou fazer o seguinte, arrobaapp.post. E aí eu vou chamar esse endpoint, essa coisa, essa função de create user.

**[00:15:08]** Mas simplão assim, simplão. Aí eu preciso de um lugar na URL onde isso vai ser contemplado. Então eu poderia colocar a barra User. Aqui eu coloquei sempre no plural para simplificar as coisas um pouco. Barra Users. Olha, alguns lugares vão falar sobre semântica, se coloca essa barra no final ou não coloca essa barra no final. Por padrão eu vou deixar sempre com a barra no final. Mas existe uma discussão...

**[00:15:37]** feroz na internet do que seria isso aqui. Então a gente vai criar esse endpoint chamado create user. E aqui dentro a gente tem como é que a gente relaciona o dado que a gente vai receber de fora do cliente da aplicação. A gente usa essa coisa esse dois pontos e o objeto que a gente quer passar aqui. E aqui é o nome do parâmetro. Então isso aqui se chama.

**[00:16:04]** Function annotation é tipo assim uma anotação de função ou seja eu estou dando algumas informações um meta dado. Desse parâmetro aqui então existe user e eu estou falando olha user tem alguma coisa a ver com esse tal de user esquema que a gente definiu nesse caso específico é uma coisa que a gente chama de anotação de tipo.

**[00:16:27]** Ou seja, a gente está falando, olha, o user que a gente quer receber, ele é desse modelo aqui, que é o modelo User Schema. Vamos ver o que acontece, então vou importar lá do esquema aquele User Schema que a gente definiu lá no começo. Então vou colocar o seguinte aqui, ah, User, dois pontos e anoto, adiciona o meta dado de User Schema e eu vou simplesmente falar o seguinte, Return User.

**[00:16:52]** Só para a gente ter um ponto de partida, um lugar aqui para poder olhar para isso de uma forma mais simplória, né? Então, vamos ver o que acontece agora com isso? Pô, foi super simples aqui, né? A gente já tinha entendido todo esse contexto um pouquinho da aula passada. Vamos ver o que que rola quando a gente subiu a aplicação, né? Então, sei lá, Poetry Brown ou Poetry Shell, você decide. Contigo aí, Task.

**[00:17:15]** Então vamos levantar o servidor dessa aplicação e ver o que acontece lá na documentação quando a gente chega com esse user aqui. A gente acabou de criar um endpoint novo. Então endpoint é bom especificar isso aqui. Endpoint quer dizer que é um ponto final de algum lugar. Então na URL a gente vai dar aquela URL tipo assim.

**[00:17:40]** meu site.com-users, então a gente está se referindo a um ponto um pedaço na URL que representa a execução de alguma coisa, um bloco de código dentro da nossa API, dentro do nosso código. Massa, beleza, subimos servidor aqui, vamos olhar lá. Então localhost 8000-docs, para a gente ir lá para a página de documentação. Aqui ele já criou de outra corzinha aqui nessa coisa que chama post.

**[00:18:10]** E aqui embaixo a gente tem esse user schema que a gente criou aqui embaixo, olha que massa. Então ele tem o username, o email e o password. E olha que legal que ele coloca um label aqui, falando que essa string de email é do tipo email, ou deveria ser do tipo email. Então quando a gente for fazer essa comunicação a gente vai mandar uma mensagem daqui para que a gente sabe que aqui, bom, é uma string, mas tem que ser uma string de email. É porque poderia ser outro nome esse campo, poderia ser, sei lá.

**[00:18:40]** Qualquer coisa que você pensar pra fazer, são batatinhas fritas um, dois, três, mas eu quero que seja do tipo e meio. Ao mesmo tempo aqui, o presidente que adicionou mais dois modelos aqui na nossa documentação, que é esse validation error, que diz, né, ou seja, é a mensagem de erro que vai ser retornada quando a gente errar o request.

**[00:19:05]** Massa, e aí o HTTP Validation Error é a mesma coisa, só que contém vários itens de erro de validação aqui dentro. Então ele adicionou esses dois modelos, o Validation Error, porque quando dá erro, e o HTTP, que é quando dá erro de HTTP, que inclui esse erro aqui de baixo. Vamos trocar uma ideia aqui com o seguinte, eu vou mudar aqui na minha aplicação esse e-mail string, eu vou comentar aqui e vou colocar só string.

**[00:19:31]** Só para vocês darem uma olhada no que vai acontecer aqui. Eu vou dar um F5 aqui na minha API e bala. E a gente vai ver que agora o User Schema segue como string. Olha que massa! Então o tipo que a gente coloca aqui delimita como isso vai ser documentado lá. Agora se dar um F5 de novo, User Schema segue com um label e meio. Não deixa de ser uma string mais.

**[00:19:59]** Quer que isso seja um e-mail, né? Então, vou simplesmente mandar aqui, né? Então, eu vou dar um try-to-out e vou mandar nossos dados pra lá. Vamos ver o que acontece. Então, eu vou falar o seguinte, olha, o meu username é Dunosauro, o meu e-mail é, sei lá, dunosauroahobaxample.com e a minha senha é 123456p. Massa?

**[00:20:22]** Então, enviando isso aqui, execute, a gente mandou para o servidor, o servidor possivelmente colocou aqui, falando olha, recebemos um post em barri users via HTTP, 1.1 e a gente retornou 200, que é OK. Significa que deu bom, deu certo. E ele respondeu para a gente exatamente a mesma coisa que a gente tinha enviado para ele. O código de resposta é username, email e password. Porque eu disse para ele...

**[00:20:51]** que o que iria retornar é esse user. Uma coisa, uma característica interessante aqui é que esse user aqui ele não é um JSON ou um dicionário, né? Se a gente quiser ver o que está acontecendo aqui dentro, a gente pode chamar uma função do Python chamada Breakpoint. Breakpoint. E aí Breakpoint é uma parada de debugging, né?

**[00:21:14]** O que significa que quando eu enviar alguma coisa, que ele executar esse bloco de código, ele vai parar exatamente aqui, né? Então eu vou executar de novo aqui. Execute. Aí tá vendo que ele tá num load em eterno, rodando. Porque o servidor está parado aqui, né? Se você quiser ver tudo que tem aqui, você dá L. Aí ele listou. Ó, estamos aqui. Como se a gente estivesse rodando isso no shell interativo, né? Aí se a gente for olhar user...

**[00:21:40]** Olha o que é user. User é um objeto do tipo user-esquima. Ele não é um dicionário, ele não é um JSON. Ou seja, quando ele passou por aqui por user, ele foi convertido nesse objeto. Massa, faz sentido isso aqui? Ele converteu isso num objeto aqui, num base-model do opidentic, que a gente pode obter os valores aqui usando, sei lá, user.

**[00:22:09]** um dos atributos que tem aqui, por exemplo, ah, qual que é o username disso aqui? Então username é do no sauro, ah, qual que é o e-mail, tal. Aí para sair do debugger você digita que? De quit. Massa? Então vamos arrumar aqui, vamos tirar isso aqui, porque eu só queria mostrar para vocês o que era esse objeto. Ele não é um dicionário, ele não é um vezom, ele é literalmente esse objeto. Então o paydantic, quando recebeu essa coisa aqui,

**[00:22:40]** ele sincronizou uma coisa com a outra. Não entendia a parte do BaseModel. O que foi convertido para quê? Então, a gente envia para ele um JSON, essa estrutura de dados aqui, que é uma estrutura que trafega na rede, uma coisa que a gente chama de serializável. E quando o FES-API recebe isso aqui, recebe esse dado. Se a gente falar que o que a gente vai receber por lá tem um tipo,

**[00:23:15]** Ele faz essa conversão dessa coisa que a gente mandou em um objeto do paydentic que a gente colocou como anotado aqui. Então ele falou olha, o que vier no payload deve ser convertido em user schema. E aí ele veio e converteu nesse objeto aqui que a gente pode olhar e ver e manipular pegando ponto por ponto aqui ou se você quiser manipular da maneira que você quiser.

**[00:23:43]** Uma coisa interessante do pai Dante, que é que se a gente tirar esse password daqui e falar, não vou enviar a senha, você lembra que lá quando a gente documentou os esquemas aqui, a senha é obrigatória, ela tem esse asterístico, como diria a minha avó, vermelho, aí a gente executa, vamos ver o que que roda, então é só username e e-mail. Se a gente rodar, ele deu um erro.

**[00:24:10]** 422. 422, lembra, a gente tinha falado que é unprocessable entity. Ele faz a conversão automática, exatamente isso. Aí ele já deu erro pra gente com aquele detalhe que a gente tinha aqui embaixo, de validation error. Ele falou o seguinte, olha, essa mensagem que você me mandou, tá faltando o password. Aqui.

**[00:24:34]** No body, no corpo da requisição que você me mandou, não veio o campo password. E esse campo era required, lembra? Marcadinho com vermelhinho ali embaixo. E aí, então ele falou, você mandou username e email, mas você não mandou password. E password era necessário para isso. Então, o próprio identity já fez a validação para a gente antes disso entrar no nosso endpoint. Não foi executado nenhum bloco de código aqui.

**[00:25:03]** O próprio pai dente que já vale 2 já deu 422, o erro de unprocessable entity. Tem como editar? Tem. Não é o nosso foco agora, eu quero que vocês entendam aqui, toda dinâmica do que está acontecendo, mas dá pra mudar a mensagem, dá pra botar em português, dá pra fazer o que você quiser. Massa? Então, ele já dá um erro pra gente aqui mudando, né? Esses status code aqui pra gente. Só que, por enquanto, entretanto, todavia, lembra que...

**[00:25:32]** o status code correto para isso aqui, não é 200, né? Que é o que ele está retornando aqui, né? Ele está falando que se der sucesso, deixa eu dar um cancel aqui, se der sucesso, ele vai retornar 200. E quando a gente cria uma coisa no HTTP, a gente tem que mandar o 201, que é o created, né? Não é ok, é create. Então a gente teria que mudar essa resposta aqui.

**[00:26:01]** E como é que a gente muda a resposta? EstatosCode, que é a resposta que a gente vai dar pra ele, é o httpstatus.created. Você poderia colocar aqui 201 também, né? Sem ser tão preciosista, mas eu acho que é mais...

**[00:26:17]** Explicito aqui. Aí o Ivan perguntou o seguinte, essa conversão é uma característica do pai dêntic ou a função do Fast API? Então, quem faz essas validações é o pai dêntic. O Fast API torna as validações do pai dêntic automáticas, mas quem valida é o pai dêntic. O pai dêntic é quem tem essa função de fazer as validações. Massa? Então aí, a partir disso agora, se a gente for atualizar aqui...

**[00:26:44]** A gente vai ver que a resposta correta disso aqui é 201. Só que você está vendo que ao mesmo tempo ele ainda está errado na documentação, falando que isso aqui vai retornar uma string. A gente tem que retornar um objeto, mas tudo bem. A gente vai por partes aqui. Vamos entendendo uma coisinha de cada vez. Então, legal, recebemos esse dado nesse Endpoint Users aqui. Esse JSON, ele é validado

**[00:27:13]** Esse dado que a gente enviou, ele é validado e convertido no objeto que tiver aqui na frente. Se o que a gente enviar não fizer parte desse modelo aqui do User Schema, ele não chega a entrar na aplicação e o que é retornado é o 422, o Unprocessable Entity. É um erro de processamento aqui dentro. Massa, então eu tinha colocado o Docs aqui pra gente ver o que que acontece.

**[00:27:43]** Só que lembrando, a gente viu que aquela resposta estava meio esquisita, tipo assim, não é uma resposta muito legal, não é uma string, não é uma coisa legal. Então eu quero retornar alguma coisa para a pessoa. Saca, quero dar uma resposta coerente para a pessoa poder, dar uma olhada nisso. E como é que eu faço isso aqui? Lembra, a gente já tinha usado esse response model aqui, só que embora eu tenha esse user-scheme aqui, vou...

**[00:28:14]** Vou quebrar aqui pra ficar mais fácil da gente ver. Mas pode fazer tudo numa linha só. É só por motivos de estudo aqui. Então a gente vai chamar esse response model e eu posso falar, por exemplo, eu vou retornar o próprio user schema. Vamos rodar isso. Beleza, atualizou. Quando a gente for lá no Swagger agora, você vai ver que ele vai retornar aqui. Tá falando, olha. Quando der sucesso, ele vai retornar tudo isso aqui. Eu não gostaria.

**[00:28:42]** que a senha fosse retornada. Não faz sentido eu retornar a senha em plaintext. Tipo assim, já tem um problema acontecendo que eu recebei essa senha em plaintext. Pô, ainda vou exibir a senha? Não faz muito sentido pra mim esse tipo de resposta, né? Então, o que eu gostaria de fazer é que não enviasse a senha na saída. E pra isso, a gente pode usar o pai dêntico de novo pra fazer essa conversão, né?

**[00:29:06]** Então, eu vou criar um outro coisa aqui. O que eu tinha dado aqui no slide? Eu quero seguir o mesmo nome do slide. Eu tenho o nome de user public. Ou seja, o esquema público, né? Então, de user, do recurso user. Vamos lá, class user public. E aí também vai errar de base model. E aí ele só vai ter o username e o e-mail. Ele não exibe a senha mais do usuário. Eu quero mostrar isso porque tem uma característica importante do paydentic aqui por trás.

**[00:29:35]** Então eu vou importar ele aqui também, o user public. Vamos retornar isso aqui, que é a forma pública do recurso que a gente quer. Ele não é o recurso em si, mas é uma forma transformada do recurso. A gente não vai mudar nada, a gente está retornando user da mesma forma. Massa, vamos ver o que acontece lá no Swagger?

**[00:29:58]** Olha que massa, ele já deu aqui ó, que quando for retornado vai retornar username e e-mail. Só que você tá vendo que a nossa resposta aqui não filtra nada, não? Eu tô simplesmente retornando aqui. O que significa que o user esquema que ele tá tratando aqui dentro, que ele vai retornar, já tem esse campo password. Vamos ver o que que acontece quando eu chamar. Então, try to out. Vou mandar do jeito que tá aqui, string, user, example, string, execute.

**[00:30:24]** Olha o que aconteceu. Ele me retornou. É porque eu não mandei um dado bom, né? Vai, do Nosauro, do Nosauro, arroba exemplo aqui, vai. Vou dar um execute de novo. Ele retornou só o username do Nosauro e o e-mail, tal. Ele não trouxe a senha. Porque a senha não tá dentro desse esquema que a gente queria. Ou seja, o esquema aqui tá sem senha.

**[00:30:50]** Por mais interessante, que ele esteja aqui dentro, ele já está no objeto, o pai dente que vai fazer esse filtro na hora do retorno. Ele vai falar, ah, beleza, tem alguns campos que eu não posso enviar, massa, então ele tira o próprio pai dente que faz isso automaticamente.

**[00:31:10]** Mas, então, esse combo do FastIPiPyDentic, ele vai fazer tanto as validações da entrada quanto a limpeza e as validações da saída. Se eu mandasse qualquer outro tipo de dado aqui, batata, a gente viu isso na aula passada, mas ele vai dar um erro 500, né?

**[00:31:28]** Aqui, ó, 500 interna não serve erro, porque o servidor, sabe, não tá enviando uma coisa que corresponde a esse modelo de resposta. Então, o pudo é validado e feito dessa forma aqui dentro. Massa? Fez sentido aqui, tudo que eu contei aqui pra vocês, até esse momento? Me contem. Lucas, obrigado aí, mano. Tamo junto, valeu aí pelo copo de café, tamo.

**[00:31:57]** Tamo junto? O Reds mandou uma pergunta aqui. Ó, enquanto eu vou respondendo as perguntas, conversem comigo. Eu quero saber de vocês se vocês estão entendendo, se você está fazendo sentido as coisas. Reds mandou aqui. Apesar da conversão dos status codes, o FES-IPI sempre deixa livre para retornar o que quiser. Ou o FES-IPI tem uma... tem uma DOC, essa convenção. Eu estou perguntando isso porque eu poderia retornar qualquer coisa. Sim, você pode literalmente retornar qualquer coisa. Você segue as convenções, porque elas são convenções, mas não tem nenhum tipo de coisa.

**[00:32:26]** específica aqui rodando. A Wesley perguntou uma coisa sobre que não é da aula, manda lá no Telegram, manda a gente conversa. Mas tá legal, faz sentido, muito bom, é muito massa isso aqui, é muito simples, né? Tipo assim, é a junção de todos aqueles conselhos que a gente viu, mas de uma maneira muito simplória, né? Funciona muito bem, voltei pro user, legal, temos aqui o username, beleza, funcionando, ó, bala, lindo, maravilhoso.

**[00:32:57]** Então esse é o esquema, né? A gente tem esse problema, mas o pai dente que simplesmente ele é maravilhoso, ele faz o que precisa fazer. Aí aqui eu tinha colocado nessa junção do user-esquema com user-public e tudo junto, a gente acabou de ver. Só que bom, a gente veio aqui pra fazer um crude, né? E a primeira coisa que eu tenho que dizer pra vocês é que a gente vai fazer um crude de mentira. Ele é de mentira mesmo, sério. Real, não vale a pena, ele é falso.

**[00:33:31]** A gente vai usar um database aqui que vai ser uma lista em memória. Pra gente ir entendendo o que está acontecendo, né? Porque se eu colocar o banco de dados aqui, aí a gente vai ter que entender outros conceitos que fogem do crude, do HTTP e entram em conceitos de banco de dados. Então, nossa lista, nosso banco de dados, né, no caso, vai ser essa lista aqui, database. Massa? Chegamos em um lugar maravilhoso, lindo, simples, bonito, cheiroso.

**[00:33:59]** E em que o nosso database é essa coisa que estamos mentindo, está enganando o cliente? Sim, por enquanto sim. A ideia é que a gente consiga ir cadastrando vários users aqui e depois listar eles, alterar eles na medida do possível aqui dentro. Então o que a gente vai fazer aqui? Uma coisa que ajuda a gente a trabalhar num banco de dados, por mais falso que ele seja, é o esquema de ter um...

**[00:34:27]** um esquema, né? O esquema de ter um esquema, né? A gente precisa ter um identificador, algo que identifique que aquele usuário é aquele próprio usuário, né? Então a gente vai chamar isso de ID, né? ID de identificador. E pra isso eu vou criar um novo esquema que é chamado UserDB. Legal? Só pra gente ter mais esquemas, mais coisas.

**[00:34:50]** Tá enganando o cliente, literalmente, é... Gostei. Então, eu vou fazer o seguinte, ó, presta atenção que agora a gente vai fazer um conceito novo aqui no Piedantic. Eu vou fazer o seguinte, class, eu vou chamar esse de userDB, ou seja, o usuário, no database, o esquema dele dentro do database, e eu vou herdar, em vez de base model, eu vou herdar de user schema. Olha que bonitinho. E aí, eu vou colocar id int.

**[00:35:20]** Olha que massa, então a gente tem todos os campos que a gente tinha em user schema, ou seja, username e meio password, mais o campo ID, ou seja, tem tudo mais o ID. Se a gente quiser fazer uma coisa mais bonitona ainda, sei lá, vamos deixar isso aqui ultra pequeno, a gente poderia fazer o seguinte, olha, user public, aí a gente herda de user public.

**[00:35:49]** Aí, a diferença do user public para o user-esquima é que tem o password. Então, a gente foi criando uma cadeia de classes aqui, né? Então, userDB tem o user-esquima que tem o user-public que é um base-módulo. E assim a gente vai estendendo a aplicação da maneira que você achar melhor. É mais simples do que ter que ficar criando 500 coisas iguais, né? Tipo assim, tudo com o mesmo campo, tudo com a mesma coisa poderia ser mais simples. Eu vou deixar no meio termo aqui.

**[00:36:20]** Porque sim, porque eu gosto aqui. Massa, legal. O Thiago tá perguntando, quando você retornou mais Tringue, deu 500, mas tem como tornar essa mensagem mais amigável? Sim, mensagens de erros podem ser mais amigáveis. Eu não vou falar sobre isso agora porque eu quero entender o crude aqui com vocês primeiro, mas dá. Dá pra fazer sim. Mensagens de erros mais amigáveis. O 500 nunca vai ser amigável porque o 500 é uma coisa imprevisível, né? Mas tudo bem. Daria pra fazer tudo ser mais amigável, sim.

**[00:36:54]** Legal, e aí o que eu vou fazer aqui com esse userDB? Eu vou adicionar esse user com ID lá dentro do nosso database. Massa, vamos fazer uma mistureba aqui de coisas, né? Então eu vou fazer o seguinte, eu vou criar um user com ID, que é o user que a gente já tem aqui, né? Então eu vou fazer o seguinte, user with ID, que é o userDB, né? UserDB, em porteira aqui em cima.

**[00:37:26]** Talvez esteja ruim de ler, pera aí. Talvez a minha cabeçona esteja na frente. Então importei aqui, o user public e o user db. Legal? E aí eu vou fazer o seguinte, eu vou pegar o user db aqui e vou definir ele na mão. E aí o que acontece? Se eu precisar definir isso na mão, eu tenho que passar todos os valores que tem no user que a gente recebeu para lá. Então eu poderia falar, ó, username é igual a user.username.

**[00:37:57]** O e-mail é igual a user.e-mail. O password é igual a user.password. E aí o ID, a gente vai ter que definir aqui porque a gente não tem esse ID. Massa? Então é que eu vou dar para esse ID? Eu vou falar que o ID é o tamanho do database mais um. Ou seja, quando tiver zero, o ID vai ser um.

**[00:38:25]** Um com joinha ou um assim, né? Legal, a gente poderia fazer esse tipo de coisa aqui. Então eu vou fazer o seguinte, vou falar aqui, LAN do database mais um. Massa? Uma coisa simples aqui. E aí eu vou retornar esse user refiD. Esse mesmo objeto que a gente manipulou aqui, eu posso retornar user de user refiD, eu posso fazer o que eu quiser aqui. Lembra que o user refiD tem os campos ID e password que a gente...

**[00:38:54]** Quer mandar pra frente ou não? Uma coisa que eu queria colocar aqui no user public é que eu queria que o user public também tivesse o ID. Porque a pessoa pode saber qual é o identificador, esse não é o dado crítico da aplicação, né? A gente passa o ID, mas a gente não pega o... a senha. A única coisa que eu não quero expor é a senha da pessoa aqui dentro. Então, quando eu criar, ele vai adicionar nesse banco de dados em memória de mentira e vai fazer essa transformação do dado.

**[00:39:24]** e salva lá no database. E vai retornar agora porque o user public tem id, o id também. Vamos ver o que que rola aqui. Ah, pera, eu esqueci o essencial aqui. Eu não coloquei o user no database, né? Então vou fazer o seguinte, a database.append é uma append de lista de user with id. Massa, legal, simplão, simprão.

**[00:39:52]** Legal, vamos ver o que que rola aqui. Agora eu vou criar um dunossauro, tal, tal, tal, minha senha vai ser um, dois, três. Aí eu vou dar um execute. Aí ele foi para lá e me retornou. Olha, username, dunossauro, e-mail, dunossauro, wholeback sample, tem o ID 1. Que massa! Então significa que agora se eu criar mais um, como já tinha um ID na lista, então a gente vai para o 2, né? Vamos ver o que acontece?

**[00:40:18]** Ai de dois. Sensacional. Temos um banco de dados de mentira aqui. Ai de três. Ai de quatro. Ai de cinco. As coisas estão indo, né? Saca, olha que massa. Então funciona bem aqui. Dá pra ir levando as coisas e a gente acabou de criar vários recursos na nossa aplicação. Lindo, maravilhoso, não? Yay! Então esse é o nosso esquema aqui, né?

**[00:40:57]** Sacou, fez sentido, tudo que a gente fez aqui, rolou, deu pra entender. Esse userDB a gente tá usando só porque ele é de mentira aqui. E aí aqui eu deixei uma coisa mirabolante aqui pra simplificar a minha vida, que é o seguinte, em vez de ficar passando parâmetro por parâmetro, a gente pode usar o unpacking de dicionário. E falar o seguinte, olha, user.

**[00:41:22]** e aí ele vai pegar todos os campos de user e vai passar para esse novo modelo aqui e aí eu converto isso aqui em um dicionário de volta que é o model dump massa essa essa é uma coisinha de python model dump transforma o modelo em um dicionário de volta né e aí

**[00:41:46]** Quando a gente usa duplo star, ele cria chave-valor de todas as chaves do dicionário e todos os valores vão ser passados para os outros parâmetros. Mas ok, quem tiver dúvida sobre isso na live sobre cabeçalhos de funções tem a explicação mais elaborada do que acontece aqui, mas é só pra não ter que ficar passando todos os parâmetros todas as vezes. Se a gente for rodar lá de novo agora, beleza. Aí de 1...

**[00:42:17]** Aí de dois, ele começa sempre de novo porque é uma lista e toda vez que a aplicação sobe de novo, obviamente a gente vai perder os dados porque eles são voláteis. Massa, fez sentido aqui essa coisa? Essa bonitesa toda que a gente fez aqui? Dos esquemas? Então vamos escrever um teste pra isso aqui, porque tudo faz mais sentido, tudo fica mais bonito quando a gente faz testes, porque eu não quero ficar toda hora mandando esses dados pra lá, né?

**[00:42:49]** Por que não? Pô, você acha que isso aqui é alguém falou na aula passada? Ah não, a gente pode criar um postman ou insônia pra ficar mandando isso aqui toda hora. Pô, a gente pode escrever testes. Vai ser melhor, né? Do que ficar fazendo isso aqui toda hora na mão, o tempo todo e tudo mais. Não se esqueça a pergunta, pode ser que você não tenha colocado o FastAPI Dev no comando. E por isso que ele não tá... Ele tá travando a aplicação e não sobe de novo.

**[00:43:25]** Pode ser por isso. Então legal, vamos lá no Shell CDGit, FastAPI0, que é o nome do nosso pacotinho aqui. E aí agora eu vou rodar o nosso, sei lá, vou dar o Poetry Shell aqui, simplificar os comentários, poderia ser Poetry Brand no começo de todos eles. E eu vou fazer o seguinte, Task Link. Quero ver se tem algum erro no meu código aqui. Aí ele tá falando, olha, tem várias coisas aqui. Os imports não estão em ordem alfabética. Tem...

**[00:43:58]** linhas em branco no meio do nada aqui, tipo assim, em algum lugar, ó, tá vendo que tem, se não é uma linha em branco, tinha coisa ali, né? Então legal, tem algumas coisas pra corrigir, eu vou dar um task format pra ele dar uma arrumada na casa aqui, então ele já vai aqui, ó, ordenou os imports pela ordem que precisava, message, user db, user public, então tá tudo ordenado em ordem alfabética.

**[00:44:25]** Massa, legal, temos a nossa aplicaçãozinho aqui rodando. Então, vamos escrever um teste para esse endpoint aqui. A gente já tinha visto aqui, né? Como é que faz esse rolezinho, né? Então, a gente tinha um cliente. E qual que é o nome do teste que eu dei aqui só para eu não usar nomes diferentes? É o teste do create user. Vamos lá, então. Def, teste, create, user. Massa. E é o que que a gente precisa? A gente precisa do cliente de testes, né? É a mesma coisa do outro teste.

**[00:44:56]** Com um cliente de teste, a gente vai fazer o exercício do endpoint que a gente quer. Então client, ponto, agora não é get, né? Como a gente precisa chegar nesse aqui, precisa ser uma requisição do tipo post. Então post. E aí esse post vai para onde? Para a barra users. E aí fica com essas duas barras aqui. Como é que a gente envia aqueles dados que a gente tinha lá para cá, né? Então eu preciso enviar o JSON para cá, né?

**[00:45:26]** Então eu preciso que o cliente de teste envia o JSON para a aplicação. Então a gente fala o seguinte, JSON. E aí a gente coloca todos os parâmetros que a gente precisa, que são username, a gente tem password, a gente tem o e-mail. E aí com esses dados aqui a gente pode mandar qualquer coisa, qualquer username que você quiser. Eu coloquei aqui elici, porque nos padrões brincadeiras de criptografia a gente sempre usa elici e bob.

**[00:46:04]** Eu vou manter aqui, então o username é Alice. O e-mail da Alice vai ser Alice, a rouba example.com. E o password vai ser, sei lá, secret de segredo. É um segredo que a Alice está nos mandando aqui. E aí eu vou pegar isso aqui, armazenar uma variável que eu chamar de response. Massa. Então...

**[00:46:33]** Aqui o que que rola? A gente tá enviando aquela mesma requisição que a gente fez pro swagger de forma programática, dentro do código. Então a gente tá enviando um username, email e tal lá em users via método post. E aí o que responder aqui vai estar nessa variável response. Aí a gente pode checar pra ver se os resultados que vieram, que voltaram, são o que a gente esperava que fosse. Então, por exemplo, a search. Então eu poderia falar o seguinte, dentro do response...

**[00:47:02]** O status code que veio é created, ou seja, deu certo, é uma coisa que a gente pode fazer. Então, http status.created. A gente quer garantir que veio o criado. E aí, vamos rodar o teste aqui, não? Então, task test. Aí ele falou o seguinte, olha, passou o test create user.

**[00:47:24]** Passou, funcionou, retornou 201. E aí o que que a gente quer validar nesse teste? A gente quer saber se os dados que voltaram do endpoint são os dados que a gente queria que voltassem, que é o user ID, né? Então vamos testar isso aqui também. Então a certe response aponta o JSON, então é JSON aqui agora, que a gente quer a resposta do JSON. E eu vou fazer o seguinte, eu quero saber se isso é igual a... E aí o que que era esperado aqui, né?

**[00:47:49]** A gente espera que venha o id. E o id tem que ser um nesse caso. A gente já vai conversar sobre isso. O email vai voltar também. E vai voltar, o email é AliceExample, aqui. E ele vai retornar o id, o email e o username. Username, que é Alice. Massa!

**[00:48:18]** Então, a gente está validando se a resposta é o esquema que a gente se comprometeu a ver aqui, né? Que é o user public. Ah, o user public não. É o user public mesmo. É que isso aqui está desatualizado, né? Então, teria que voltar aqui. User name, email e id. User name, email e id. A ordem não importa aqui. Então, vamos rodar o teste e ver o que acontece. Task test. Aí, ele deu um import email, porque toda vez eu...

**[00:48:50]** Faço isso do enter e aí ele importa lá em cima pra mim. Legal. Agora vai dar certo. Vamos lá. Task test. E aí? Passou. Funciona. Lindo. Escreveu os nossos testes de post. Olha que bonito. Para. Não é legal? Escrever testes não é muito mais legal. Agora a gente sabe que se a gente errar lá dentro, lá em cima, o teste quebra. Falou ó, não vai retornar mais nada.

**[00:49:25]** Legal, aí o teste quebrou. É muito legal, é muito bonito. Ó, solta faíscas de amor aqui. Agora toda vez que a gente rodar, a gente sabe que está funcionando. Eu não preciso ir lá no postman, eu não preciso ir lá no swagger, não preciso criar um database de requisições, não sei aonde. Eu não preciso ficar indo lá na mão e vendo se está funcionando. O teste garante que toda vez que eu rode funciona.

**[00:50:00]** E é muito legal ver isso aqui verde, todas as vezes. É lindo. E roda rápido, funciona, saca? E faz várias coisas ao mesmo tempo e tudo mais. Bom, só que aqui ainda tem um problema que eu queria falar com vocês, que é o seguinte. Toda vez que a gente tá criando um teste, a gente tá fazendo esse esquema de client, teste, tal, tal, tal, tal, tal, tal. Esse aqui, ó. A primeira linha do teste, o arrange dos dois testes são o mesmo, tá vendo?

**[00:50:29]** Client app, client app, e aí toda vez que eu vou ficar chamando isso de novo, toda vez que eu for escrever um teste novo, eu vou ter que ficar fazendo isso aqui todas as vezes, de novo, de novo, e de novo. O Resident falou que o dele está retornando 4.2.2, é porque seu payload está errado, e aí toda vez que o payload está errado retorna 4.2.2 mesmo. Tem algum erro no seu JSON. Massa?

**[00:50:59]** Então, uma das regras boas de práticas do software é o dry. Não se repita, né? Don't repeat yourself. Não faça a mesma coisa de novo. E aí, na aula anterior, duas pra trás, eu tinha falado, pô, vamos dar uma olhada no negócio que se chama fixtures, né?

**[00:51:17]** que é uma forma de conseguir não repetir as coisas, eu dei uma referência, ela falei, olha, assiste essa aula, talvez seja uma boa e tudo mais. Então, vamos criar uma fixture. E o que é uma fixture? É um bloco de código de teste reutilizável, né? Ou seja, toda vez que eu precisar de uma coisa específica, por exemplo, esse cliente, eu posso vir aqui e só importar ele na função.

**[00:51:44]** Todas essas coisas a gente vai ver como importa isso na função. Mas é o seguinte, o principal. Toda vez que eu precisar de um cliente, eu chamo o cliente. Eu não peço ele aqui de novo e eu chamo ele via parâmetro porque é uma das características do PiTest a fazer isso. Eu poderia vir aqui, eu vou fazer nesse mesmo arquivo pra gente entender aqui. Então vamos lá, importe PiTest. PiTest.

**[00:52:12]** E aí eu vou criar uma função aqui que eu vou chamar de client. Def client. E aqui dentro desse client, eu vou colocar essa definiçãozinha que a gente tinha aqui. Do arrange. Então o arrange ele sempre vai vir daqui. Então return test client. E a gente usa esse decorador do pytest aqui ó. pytest.fix

**[00:52:42]** Para falar que isso aqui é um bloco de código de teste reutilizável. Ou seja, tem um nome chamado client e toda vez que eu quiser esse teste client e app tal, eu venho aqui e falo o seguinte, client. Eu passo como um parâmetro do teste. E aí o paeteste se encarrega de fazer essa mágica para mim. Client, client. Pronto, agora os testes ficam mais simples de escrever. Olha que legal. Você vai se rodar de novo.

**[00:53:09]** Ele deu erro por conta da ordem do import aqui, né? Ele tá falando que, olha, o PiTest não deveria estar importado aqui, deveria estar importado antes. Eu vou dar um TaskFormat e vou dar um TaskTest de novo. Legal, funciona.

**[00:53:22]** Ou seja, simplifica, né? Simplifica poder pegar a mesma coisa todas as vezes em muitos lugares. Só que se você está vendo isso aqui, vamos para que a gente crie outro arquivo de teste depois. Isso aqui está nesse arquivo, não sabe, não é muito legal. Para organizar isso, o PiTest tem um arquivo específico que fica dentro da pasta de testes que ele chama de ConfiTest. Ou seja, configurações de teste, né? .py aqui. Yes!

**[00:53:53]** E aí eu trago essas coisas, definições de fixture pra dentro desse arquivo com o teste. E aí eu preciso importar o pai teste aqui. Legal, aí eu preciso desse teste client e do app que estão aqui, então trago tudo isso aqui pra cá. Aí pra gente dar, tô com preguiça, dá um format aí, beleza, formatou. Olha como nosso arquivo de teste ficou muito mais limpo agora, eu vou tirar esse comentário daqui.

**[00:54:26]** que era só para a gente entender algumas coisas. Olha como ficou limpinho. Pô beleza, é o cliente de teste da nossa aplicação. Nice, só traz ele para mim. Vem para cá. E aí com isso agora a gente tem esse cliente que a gente pode mandar as requisições por aqui. E ele fica aqui paradinho no Conf Test. Vamos rodar de novo só para ter certeza?

**[00:54:55]** Funciona. A Rafael falou, poderia dar mais um exemplo de fixture? Sim, em outro momento. A gente vai criar, sei lá, umas 200 fixtures nesse projeto aqui, mas por enquanto é o básico. Vamos pensar que é tipo assim, eu feijão com arroz aqui hoje.

**[00:55:11]** Massa, legal? Então nesse arquivo com o teste, a gente sempre vai trazer essa coisa. Essa fixture garantir que o mesmo cliente vai ser usado em todos os testes? Sim, é exatamente isso que ela faz. Então em vez de ter que ficar fazendo definições e coisas, a gente usa uma coisinha pronta e não ficar repetindo isso no código todas as vezes. Essa é a ideia de uma fixture, né? Legal. A gente fez o post, a gente testou o post, a gente fez o que dava pra fazer e tudo mais. Agora faltou a coisa de...

**[00:55:40]** Dá o get, né? Me dá. Eu quero recuperar isso aqui. Ah, o Marcelo fez uma pergunta interessante. Não precisa importar o Conf-Test nos demais arquivos? O Pai-Test já entende isso? Sim, o Pai-Test é maravilhoso.

**[00:55:57]** Eu não sei do que eu gosto mais aqui. Se é o FastAPI usando o pai dente que para validar ou se é o pai teste fazendo essa magia dele aqui. É lindo, não precisa importar. É só usar aqui. O pai teste tem várias outras fixtures, você poderia vir aqui e fazer o seguinte. É pai teste menos menos fixtures. E aí você consegue ver que ele lista várias coisas aqui. Aí o nosso cliente está aqui. Fixtures definindo com o test. Ele tem várias outras. Várias, várias, várias, várias.

**[00:56:25]** Se você quiser ver as fixtures que ele disponibiliza, isso aqui. PiTest, menos ou menos um fixture. Massa? Não quero tomar muito tempo nisso, porque não é o momento agora. Legal, então a gente fez isso aqui. Vamos criar um endpoint que a gente pode pegar os users cadastrados. Eu não quero ler um, eu quero ler todos que tem na minha aplicação. Vamos pensar agora. Então legal, a gente tem um post desse recurso, ou seja, cria o recurso, agora eu quero ver todo mundo que está cadastrado.

**[00:56:54]** Então eu vou criar um app.get e eu vou sempre manter esse endpoint aqui pra gente aqui, user, o recurso vai ser sempre o mesmo. E bom, o que eu quero saber, toda vez que eu dou um get, que eu peço um recurso, peço alguma coisa pro servidor, se deu certo ele me retorna a 200, então statusCode, HTTP, status, deixa eu fazer maiúsculo aqui, HTTP status.ok.

**[00:57:22]** Por padrão já é ok, mas lembra, explícito é melhor do que implícito, não é aquela regrinha básica de sempre. E aqui eu acho que eu dei o nome de read users, ou seja, ler os usuários pra gente. O que que acontece aqui? A grande sacada aqui é que eu tenho que pegar os users que eu tenho e retornar eles...

**[00:57:44]** para fora da aplicação. Então eu vou fazer o seguinte, eu vou dar um return de database. Só para a gente ver o que está acontecendo, se ele retorna a todo mundo que a gente cadastrou aqui dentro da aplicação. Por enquanto eu vou fazer isso lá no swagger, porque a gente não vai escrever um teste nesse primeiro momento. F5, e agora a gente tem aqui o users. Vamos ver, aqui eu try it out, execute. Não tem ninguém na nossa aplicação, por isso que ele retornou uma lista vazia.

**[00:58:13]** Vamos criar, lembra que toda vez que muda o código ele reinicia zero banco. Vamos criar alguém aqui, try it out. Vou criar esse exemplo, então a gente tem o ID 1, vou criar de novo. ID 2, ID 3, ID 4. Mas cliquei várias vezes aqui.

**[00:58:31]** Agora vou dar um get aqui, vamos ver o que rola. Execute? Ó, agora ele trouxe pra mim uma lista com todos os users cadastrados na minha aplicação. Todo mundo que tá dentro do meu banco de dados voltou agora. No banco de dados, lembra? Banco de dados, ó, não é um banco de dados, né? Uma lista. Mas tá aqui, o username, um, dois, três e quatro. Todos eles foram retornados aqui.

**[00:58:57]** Só que você está vendo, beleza, embora seja simples, funcione, lindo, maravilhoso, vamos dar um cancel aqui e dá um F5. O que que retorna isso aqui? Uma string. Ou seja, não consigo dizer para a pessoa que a gente não tem um contrato firmado do que eu vou retornar aqui para ela. Então, uma boa coisa seria a gente ter um esquema de resposta. E como é que a gente monta esse esquema?

**[00:59:31]** Porque são vários users. Olha como o pai dente que é sensacional. Sim, eu tenho vários users e eu vou retornar uma lista, uma lista de quê? De todos os públicos, de todos os users públicos da minha aplicação. Simples, belo, lindo, maravilhoso, ó. Vamos ver como é que isso aqui se manifesta. Então, vamos criar um esquema aqui. Então, eu vou chamar esse Clash User List. Eu acho que foi esse mesmo nome que eu dei aqui, User List. E a gente vai herdar de Base Model.

**[01:00:07]** E eu vou falar, olha, quando isso aqui foi chamado, ele vai retornar vários users. Então, vou colocar no plural. E vai retornar uma lista de... O que a gente quer? User com ID? Não. A gente quer o user esquema, não porque tem acenho. Com ID também tem acenho. Então, a gente quer user public. Que são só os que a gente mostra para as pessoas. Nice! Vamos ver o que acontece aqui? Então, eu vou importar ele agora aqui.

**[01:00:36]** Agora eu vou precisar daquele parêntese aqui, não vai caber todo mundo aqui. E a gente vai ter que colocar o user list. Eu vou colocar ele já na posição certa aqui, user list. Massa! Então o dado que vai ser retornado aqui é o return model, user list. Vamos ver o que acontece? Vai dar erro, mas vai dar um erro legal de ver. Agora quando a gente voltar lá no swagger, a gente vai ver que isso aqui retorna, olha.

**[01:01:08]** uma lista de users, onde a gente tem um esquema mais ou menos assim. Oh, cara, o identity que é sensacional, né? Não, o identity é muito, é muito sinistro, né? Ele já resolveu a equação aqui, né? Então ele falou, olha, vai vir alguma coisa que tenha a chave users, dentro dessa chave users tem uma lista, e essa lista tem vários objetos JSON que tem username e mail id. Pronto, tá documentado. Aqui, se você ver aqui no user list, ele fala, vai ser vários users,

**[01:01:38]** E cada item dessa lista vai ter esses campos aqui. É sensacional. É sensacional. Só que quando eu pedir, ele vai dar erro. Vamos ver o que vai acontecer? Gatch, execute. Aí ele falou, internal server error. Deu erro no servidor da aplicação. E por que deu erro? Ele falou, input should be a valid dictionary or object.

**[01:02:04]** Ou seja, a gente está mandando uma lista vazia e precisava ser um dicionário ou um objeto que tivesse a chave, a chave Users, que é o que a nossa coisa não tem aqui. Então, eu vou retornar Users. Então, todo mundo que está no database, que é a lista do esquema que a gente queria, e essa era a chave que estava faltando, Users. Vamos rodar agora? Execute.

**[01:02:29]** Legal. Ó, voltou um users com uma lista vazia, que a gente restartou a aplicação. Vamos criar um 5 aqui agora, vai. Try it out. 1, 2, 3, 4, 5. Beleza? Última id 5. Vamos lá na listagem no get. Yay! Todo mundo aqui. Olha que bonito. Maravilhoso. Seguindo esquema. Pai dente que é lindo. Sou fã do pai dente, que desculpe. E esse é o nosso get.

**[01:03:02]** Agora a gente pode pegar todos os users que tem na nossa lista. Ele está enumerar todo mundo que está cadastrado na nossa aplicação. Legal, né? Está todo mundo tão quietinho que aí eu já não sei mais se eu estou em live ou se só eu que acho isso aqui extremamente impressionante desse jeito aqui, né? Então vamos escrever um teste para isso aqui, né?

**[01:03:32]** Então, basicamente, a gente vai chamar o barri users e vai esperar que algum user esteja lá dentro, esteja criado. Legal. Como é que a gente vai chamar esse teste de read users? Lê os usuários. Sim, prão, vai. Def read, é teste, sempre tem que começar com teste, read users. Massa? Olha que lindo isso aqui.

**[01:03:59]** Agora, eu não preciso mais me preocupar com aquilo, porque eu já fiz uma fixture que resolve esse problema. Tem um objeto de teste reutilizável? Ah! Delicioso, delicioso, né? O pai dente que é tão bom que estamos sem palavras. Maravilhoso, né? Então, legal, o que a gente vai fazer? Client, aonde a gente quer bater no endpoint get. Então, client.get, aí a gente tem... Isso aqui vai ser o response, não é disso aqui?

**[01:04:32]** E aí a gente quer dar um get em barra users, users. E é só isso, não precisa de muito show aqui. Só isso aqui. Então, o que ele tem que responder aqui? Então, a gente vai ter que fazer um asserte no response.statuscode, a primeira coisa que eu quero saber, status underline code, vai ter que voltar HTTP, HTTP status, ok, porque é um get.

**[01:05:05]** E o que que vai ter aqui dentro? Então vai ter que ter uma search, response.jzone, e ele vai ter que ter o quê? Ele vai ter que ter uma chave chamada users, e aqui dentro dessa chave a gente vai ter que ter uma lista que tenha esse resultado aqui da Alice aqui, né? Basicamente isso aqui. Eu vou rodar aqui e vamos ver o que acontece.

**[01:05:41]** Só pra ver se funciona. Talvez ele dê erro de formatação aqui. Beleza, deu alguns erros de linhas em branco, tal, tal, tal, tal, tal. Então task format. Legal, mantendo a integridade da API aqui. Então task test funcionou. Lindo, maravilhoso. Olha o teste que a gente escreveu aqui. Aqui tem um comportamento que é uma aberração no mundo dos testes. Sim, é um comportamento... Eu não queria dizer que é um comportamento...

**[01:06:14]** de merda porque eu queria poupar minhas palavras mas é um comportamento não esperado olha o que acontece aqui quando esses dois testes rodam o primeiro teste insere um user ta vendo? ele cria um usuário o segundo teste lê o usuário que foi inserido no primeiro teste olha o que aconteceu aqui

**[01:06:45]** Isso aqui é um comportamento que a gente chama de smell, cold smell, é um código ruim, porque os testes eles não são independentes, saca? Então os códigos eles dependem um dos outros, né? O primeiro teste só funciona, funciona a bala. Se eu comentar ele e rodar aqui só o segundo teste, ele falha. Olha que interessante!

**[01:07:13]** Falhou, porque users veio vazio, ou seja, toda vez que inicia a aplicação ele inicia sem nada, então ele tentou rodar, mas eu quero que vocês vejam um erro, porque o erro é bonito. Ele falou o seguinte, olha, o users que veio da requisição, o primeiro lado aqui que é o response.json, ele trouxe aqui o users vazio.

**[01:07:33]** Só que a gente estava esperando que viesse um users com uma lista e que dentro dessa lista tivesse um objeto que tem o e-mail, lc, id, username, lc. E não veio, porque os testes eles são dependentes um dos outros. Isso é muito ruim, né? Isso é muito ruim. Porém, com tudo entretanto, todavia, o nosso objetivo hoje é entender como escrever os testes mais básicos do crude e entender também

**[01:08:03]** As coisas do crud, o nosso banco de dados está em memória, é toda uma coisa, né? A gente vai resolver esse comportamento na aula 5, porque na próxima aula a gente vai introduzir o banco de dados aqui, né? Mas enquanto a gente não tiver o banco de dados aqui, vai ficar meio complicado de gerenciar isso. Os testes são interdependentes, isso é ruim, mas lembra, o nosso objetivo aqui é entender as coisas.

**[01:08:33]** Então, como faz um teste de get, como faz um teste de post, o que que vem, o que que volta, como faz o asserte, eu não estou muito preocupado com a melhor prática possível aqui. Porém, com tudo entretanto, isso aqui é uma gangrena, né? Na vida real, isso não pode acontecer. Massa, estamos entendidos? Eu vou seguir assim, mas a gente vai resolver isso aqui na aula 5. Depois, quando a gente vê um banco de dados, a gente vai poder zerar o banco de dados. Massa.

**[01:09:02]** Aí o André falou, o ideal é criar a fixture pra remover as dependências dos dados, então o ideal é que o cliente limpe os dados, mas a gente vai conversar isso no momento em que a gente tiver como limpar os dados, porque a gente não tem como limpar os dados ainda. Massa? Aí então vocês estão falando que tem mais gente vendo que like hein mano, deixa o like aí, não esquece, não esquece de deixar o like pra ver se isso chega em mais gente. Então legal, vamos lá, vamos lá, seguindo aqui.

**[01:09:37]** A gente criou dados, a gente viu os dados que a gente criou, né? Nice! Só que agora a gente precisa alterar os dados, né? Vamos supor que o meu e-mail seja outro e-mail, sei lá, não é dunossaurarroba-e-mail.com, é dunossaurarroba-e-mail.net, ponto AI, né, que é o modelo do, é o domínio do futuro agora, né?

**[01:10:02]** Então, vamos fazer isso, né? Então, vamos criar uma coisa para alterar. Existem dois métodos do HTTP para fazer a alteração, né? Um deles é o Put e o outro é o Patch. A gente vai usar o Put agora. Na próxima vez que a gente vai fazer um outro crude lá na frente com mais coisas, mais recursos e tudo mais, a gente usa o Patch. Por enquanto, vamos aprender o Put. Combinado? Patch, sei lá, na aula oito, por aí. A aula sete. Então, vamos lá. Arroba a app e ponto...

**[01:10:33]** PUT para alterar dados. Quem é o recurso? Users. Massa. O que que retorna o PUT? 200. Espera aí, que meu editor está aqui. Status Code retorna 200. Então é HTTP Status OK. O que que ele vai retornar quando a gente for...

**[01:11:00]** Dá o resultado de volta, é o user public, né? Então ele vai mostrar, ele tem que mostrar o mesmo ID só que com o campo que a gente alterou de forma diferente, né? Então ele vai retornar o response model dele. Response model dele é o user... user quem? User public. Até eu tô meio perdido aqui, é muito modelo, muito modelo. E a gente vai fazer o def... Como é que eu dei o nome aqui? Update user. Update.

**[01:11:31]** User. Aí o que ele tem que receber, né? Porque quando a gente tá alterando alguma coisa, a pessoa precisa dar o dado que precisa alterar. No PUT, nesse método específico do HTTP, a pessoa tem que mandar todos os dados. Ah, eu vou alterar a minha foto, mas você vai ter que mandar o RG, o CPF ou não sei o que, o nome do pai, o nome da mãe, é a característica do PUT. Mas então a gente vai receber user aqui.

**[01:11:58]** E aí esse user é do tipo user schema, porque ele tem que enviar todos os dados de novo, não é? Então user schema. Massa. Aí tem uma outra coisa que a gente precisa saber aqui, né? Que é aí que entra isso aqui, ó. As variáveis. Variável é o que? É o que varia, né? Aquilo que varia. Então eu vou colocar aqui o user ID. User ID.

**[01:12:28]** Antes de qualquer outra coisa, eu vou com vocês lá no Swagger pra gente ver o que que acontece aqui. Quando a gente dá essa variável User ID, e eu tenho que ter ela aqui no parâmetro também, User Underline ID. Tem que ser o mesmo nome. Aí eu vou falar, isso aqui é um inteiro. Massa? Então legal, quando eu preciso alterar o usuário, eu preciso falar pra API que usuário que eu tô alterando, né? Você vai ver que agora ele ganhou um laranjinho aqui, o Put.

**[01:12:58]** Olha que interessante. Toda vez que eu for falar que eu vou tentar um pute, eu tenho que falar qual é o ID de quem eu quero alterar. Porque não tenho como saber, né? Então a gente inseriu o ID, né? A gente sabe qual é o identificador daquele registro que a gente quer. E eu tenho que falar, eu quero alterar o ID 1, o ID 2, o ID 10. O ID, sei lá, 55.

**[01:13:20]** Se eu não tivesse essa variável aqui na URL, o user ID, eu não saberia quem eu tenho que alterar dentro da base de dados. Então a ideia disso aqui é que eu consiga saber quem eu altero. E se a gente der o breakpoint aqui, aquela coisa que a gente tinha feito antes para fazer o debug e breakpoint, quando a gente chama isso aqui, então eu vou passar 1 e, sei lá, username string total, execute. Aqui dentro, o user ID travou meu shell aqui.

**[01:13:52]** User Underline ID, ele é um. Meu shell travou geral aqui mesmo. Deixa eu matar ele aqui, vem. Que buffer, Vitamins. Legal, vamos rodar aqui de novo. Então, eu estou na parte de teste, é aqui. Então, quando eu enviar aquela requisição para cá, o ideal é que ele trave aqui e a gente consiga ver, né? Ainda não terminou de subir. Agora foi.

**[01:14:33]** Então, se a gente vier aqui e chamar o user ID, user ID, você vai ver que ele é um inteiro, que é exatamente o que tinha aqui, né? O user ID, um inteiro, e aí ele também tem o user, user, que é aquele outro esquema daqui. Dúvida, já vi código usando post para fazer consulta no banco, por quê?

**[01:14:54]** Essa é fora do escopo aqui, tipo assim. Tem outros tipos de coisas que não são esse formato RPC ou REST que a gente chama, que usam um post para fazer busca, tipo GraphQL e tal, mas é totalmente fora do nosso escopo aqui. Então olha que interessante, ele fez um link dessa coisa que tinha aqui, desse user ID, com o tipo que a gente passou aqui, que é o inteiro, então ele trouxe esse user ID para cá, isso virou um parâmetro da função. Então a gente sabe

**[01:15:25]** O que foi passado lá, o recurso, qual é o ID do recurso que a gente quer? Então a gente consegue pegar ele por aqui. Fez sentido isso aqui? Fez sentido esse uso aqui do ID, coloca assim mesmo, entre chaves, e a gente passa ele como um parâmetro aqui dentro. É basicamente esse o esquema dele aqui. Massa, fez sentido? Eu sei que tem um delay grande aí entre mim e vocês aí, mas tudo bem, a gente vai sobreviver.

**[01:16:02]** Vou deixar rodando aqui em background de novo. Então essa é a ideia desse PFEF aqui, desse parâmetro que a gente está passando para ele. A gente está dizendo que vamos receber um dado a mais. Fora a relação, esse aqui, como não tem na URL, esse user, quer dizer que a gente vai trazer ele do payload. E aqui é o que a gente está trazendo da URL.

**[01:16:29]** Então, quando a gente chama isso aqui, ao RL que a gente está chamando de verdade, é isso aqui, vamos lá. A gente está chamando esse caminho, né? Então, HTTP, S, dois pontos, barra, barra, HTTP, não é no caso, não é S. Localhost, dois pontos, oito mil, barra, users, barra, um, que é o registro que a gente quer checar aqui dentro. Então, é mais ou menos isso que a gente está chamando aqui, né? Então, se a gente chamar o HTTP.

**[01:16:59]** É o método PUT, disso aqui, no user1. Aí ele tá reclamando aqui que tá faltando algumas coisas e tal, deu 422. Mas a URL é essa aqui. Massa? Então tá aqui. O Lucas falou que não precisa, cara, precisa, depois vai dar outros erros bizarros quando você precisar relacionar esses parâmetros. Sempre coloca. Lembra do lembro do Python. Explicito é melhor do que implícito. Passe os parâmetros.

**[01:17:37]** Porque quando você faz assim, isso aqui é um parâmetro de URL. Quando você só coloca assim, isso é um path parâmetro. É um outro tipo de coisa. Tipo assim. Isso aqui vai ser coisa de formulário, sabe? É outro rolê, mano. Tipo assim. Precisa. Necessita ser assim. Depois, lá na frente, a gente vai ver uma coisa assim. Sem o parâmetro recebendo aqui, mas...

**[01:18:07]** Ainda não. Olha o que que rola aqui. Vamos voltar lá, vai? Pra essa dúvida. Aqui você tá vendo que isso aqui é um parâmetro, certo? Se eu tirar ele daqui, ele vira query. Eu deixei o debugger aqui. Put. Aqui, ó. Isso aqui é query, tá vendo o quê? Query. Se eu colocar isso aqui, tá subindo aqui, pera aí. Isso aqui é o path. Então, são coisas diferentes. Não confunda.

**[01:18:46]** Se precisa passar, tem que ser aqui na URL. Massa? Então, legal. E o que a gente vai fazer com esse dado aqui? Vamos lá. Para alterar o registro. Basicamente, eu vou fazer uma gambiarra naquele banco de dados que a gente tem aqui, né? A gente vai fazer o user ID, né? Que a gente tinha lá em cima. A mesma coisa que a gente tinha lá atrás.

**[01:19:16]** Eu copiei porque é a mesma linha que a gente digitou 10 minutos atrás, 20 no máximo. Então aqui...

**[01:19:29]** É a mesma língua que a gente tem aqui. Então, transformou o user que veio aqui, com isso aqui, usando o user ID que veio aqui em cima. Basicamente, é só um registro que a gente vai procurar. Aí, eu vou procurar ele lá no banco de dados. Olha que massa. Data Base, olha a nossa query de banco de dados aqui. Data Base vai ser user ID menos 1.

**[01:19:52]** menos um. Esse é o nosso select no banco de dados aqui, porque a gente não tem um banco de dados, né? Então, a gente vai pegar esse dado que está aqui na tabela, vai procurar a posição dele, ou seja, qual é o usuarial 3? Então, id 3, ele vai estar na posição menos um da lista, né? Porque a gente está adicionando mais um aqui em cima, porque o id não pode começar no zero, né? Então, a gente vai fazer isso aqui.

**[01:20:21]** e aí ele vai receber o usuário modificado simprão assim simprão simprão simprão demais gambiarra de qualidade gambiarra de verdade a gente tá aqui para entender o put post delete e getcher saca e eu vou dar um return isso aqui no user e find e a gente vai ver o que é um teste agora porque a gente tem vários recursos saca para a gente tratar aqui

**[01:20:46]** Legal, vamos ver. Poderia ser pelo menos um dicionário. Não, o legal da gambiarra é que quanto mais gambiarra a gente tiver, melhor. Resolução técnica diferenciada. Boa, gostei. Legal, então vamos ver o que acontece aqui. Eu vou criar alguém, olha. Agora, vamos entender o Put, de verdade, aqui. Eu vou criar alguém. Então, eu vou criar aqui um username chamado dunossauro. E aí aqui vai ser...

**[01:21:18]** do Nosauro Arroba Ex-Emple, massa. E a minha senha vai ser 1, 2, 3. Legal, ok? Então criamos isso aqui, retornou, a gente tem um ID 1 aqui no nosso banco de dados. Legal, agora vou dar um get in users para ver se ele existe mesmo, né? Para ver se... Pô, tá no banco de dados? Não existe banco de dados, mas tá em memória? Vou até parar para tu ser aqui.

**[01:21:53]** Tá no banco de dados? Tá no banco de dados, ó. Então tá lá. Existe um user com dunossauro, e-mail, tal, tal, tal, tal, tal, tal. Agora, eu vou pegar esse, isso aqui, e a gente vai trabalhar com ele lá em outro lugar, né? Vamos ver lá no pute agora. Eu quero alterar o registro 1, que é esse, dunossauro aqui. E aí o nome dele, agora vai ser Regis. Regis com o Regis Arroba Example aqui.

**[01:22:21]** Troquei! Não quero mais cedo no sauro, agora eu sou Regis. Massa? Executei. Pimba! Então ele voltou aqui, username Regis, tenho e-mail regisarrobexample.com, e o ID é um. Se a gente for listar, a gente vai ver aqui que o Regis está aqui. Nice! E se a gente criar outro registro aqui, vamos ver. Vamos criar alguém aqui, agora a gente vai criar a bug.

**[01:22:52]** buglcif, então aqui ó o e-mail da bug é bugarroba, eu vou colocar aqui ó bugarrobalcif ponto com a senha da bug também vai ser um dois três vai, então a gente tem aqui o user da bug

**[01:23:08]** E nada impede aqui, a gente lista e funciona. Temos três operações, a gente tem Create, Read e Update. Se a gente quisesse mudar agora qualquer outra pessoa aqui, tipo, e a gente vai nessa brincadeira. Então a função do PUT é essa de poder alterar os registros. Fez sentido pra que serve o PUT aqui? Tá no Manice? Só que tem alguns outros problemas que podem acontecer aqui, né?

**[01:23:38]** Senha padrão, um, dois, três. Descobriu minha senha? Senha, três primeiros dígitos do CPF. Legal. Não tão preocupado com segurança. Tão preocupado em entender o pute. Lembre-se disso. Fez sentido o pute? Pra que que ele serve? Então ele faz uma alteração do registro? É esse o ponto que eu quero chegar com vocês aqui. Legal? Só que tem um problema, né? E se eu pedir alguém que não existe?

**[01:24:05]** E se eu pedir um ID, se eu quiser alterar o ID de alguém que não usa o ID 3, por exemplo, vamos tentar, vamos testar, vamos ver aqui. Então eu quero alterar aqui no Put, o ID 3. O primeiro é o Regis, que era eu e viria o Regis, aí o segundo é a bug, só que eu vou alterar o 3 e o 3 também vai chamar Regis. Execute. Internal Server Error. Ou seja, deu erro interno no servidor.

**[01:24:31]** Aí ele falou o seguinte, olha, quando eu fui checar o database, lá ele deu indexerror. Lista assignment index out of range, ou seja, não existe o valor que a gente quer dentro da lista, ou seja, o ID 3-1-2 não está aqui, não existe. Ou seja, deu ruim, deu erro.

**[01:24:52]** Então, quando dá erro, vocês lembram qual que é o... Já tava dando a solução. Vocês lembram qual que é o erro da linha 400? Que representa o... Não tenham esse registro. Foi mal, patrão. Não tenham aí o que você quer. Qual que é esse código de erro? Maravilhoso? Fala aí para mim. Eu tô na confiança, que vocês vão me falar. E aí você vem aqui no FastAPI e você pode importar os erros aqui, né? Que é o... HTTP exception.

**[01:25:25]** Ó, o Caio já mandou a braba, que é o 404, not found, né? Não achei o que você queria. E aí, a coisa fica muito maluca, então a gente vai fazer isso aqui, mas a gente tem que checar, né? Tipo assim, pô, o registro, a gente vai ter que simular o banco de dados de verdade aqui, nessa parada. Então eu vou falar o seguinte, se o user ID for menor do que 1, ou seja, ele não pode ser...

**[01:25:52]** Se ele for menor do que 1, ele não pode ser menor do que 1. Então, se não for menor do que 1, a gente vai dar uma HTTP exception. Massa? Eu vou, eu vou, salva, salva isso aqui. E, ou, né, or, não tiver na lista, for maior do que o lane da lista, menos 1, aqui ó, eu tinha deixado aqui. Ou seja, porque a lista tem...

**[01:26:20]** 5 registros, tá ligado? Se for diferente, a gente não pode, tá ligado? Olha que sai de quests aqui, por não ter um banco de dados, mas tudo bem, porque o que eu quero mostrar é como dar um erro aqui. Então, o HD The Perception tem um campo aqui que se chama Detail, que você fala aqui o que que aconteceu. Deu ruim, não achei.

**[01:26:44]** Vocês estavam perguntando como é que fazia para ter uma mensagem bonita de erro? E a gente tem que passar qual que é o status code do erro, então o status code é not found, né? Então, HTTP status.notfound, que é 404. Massa, lindo, cremoso, né? E aí como é que a gente dá esse erro, né? A gente dá esse erro, a gente chama de explosão. A gente tem que jogar esse erro, levantar ele para cima. Então, é o Ryzy.

**[01:27:14]** Ryze HTTP exception, ou seja, explode essa exceção aí, quando for um valor maior do que eu tiver no banco de dados, ou for menor do que, do menor do que 1, né? Não vou pedir 1. Me dá o registro menos 57 aí, deixa eu fazer, não tenho registro menos 57, começa no 1, mano. Massa, vamos ver o que acontece agora? Então eu vou pedir para alterar, deixa eu falar um F5 aqui, eu vou pedir para alterar o registro menos 3. Vamos ver o que que rola?

**[01:27:44]** Ta-da! Not Found! Detail! Deu ruim, não achei! Muito bom, muito bom, muito bom! Aí ó, deu ruim! Deu erro! 404! Nice! Ó! Maravilhoso! Deu erro! Not Found! Qual que era o erro que eu tinha deixado aqui? User Not Found, né? Bem melhor, né? Vai! User Not Found, vai! Tudo bem, vamos deixar uma coisa...

**[01:28:17]** bonitinha, por que se depender de mim retorna pay? Por isso que eu escrevo slides, senão eu fico escrevendo gangrena, groselha depois. Legal, então se a gente pedir aqui, então o user not found, 3, e agora a gente não tem nenhum registro na base, né? Então se a gente pedir 1, né? Vamos ver, só ter certeza. Vamos listar todo mundo, a gente não tem ninguém. Ou seja, se a gente pedir o ID 1, tem que dar errado também. User not found. Mas se tivesse o user, então vamos criar ele com post.

**[01:28:49]** O crud inteiro hoje. Temos um. Então eu vou alterar um para esse registro aqui. Dei. Legal. Aí de um. Aí de dois. Not found. E aí. Beleza. Maravilhoso. Maravilhoso. Essa é a ideia de retornar erros no fastidio IPI. A gente dá esse Brazen, né? E a gente que a gente chama em português de levantar uma exceção. E que exceção é essa? É uma exceção de HTTP. Ou seja, é um erro.

**[01:29:21]** que a gente vai retornar, mas lembra, série 400 são erros do cliente, né? O cliente me pediu uma coisa e não tinha o que ele me pediu, então, 404. Massa, fez sentido isso aqui? Maravilhoso, não? Lindíssimo, né? Fala, vocês não gostaram? Tá todo mundo muito quietinho hoje. Então, vamos fazer o teste disso aqui, porque sim, porque a gente sabe fazer teste. Então, qual que é o nome do teste? Update User. Lindo, maravilhoso, vamos lá.

**[01:29:59]** def test update user A gente tem o client maravilhoso que a gente traz aqui client a nossa fixture linda cremosa maravilhosa que simplifica tudo e vamos fazer o seguinte client.put olha que coisa massa aqui eu posso alterar eu posso alterar isso aqui porque que eu posso executar o put pra fazer essa coisa lá atrás

**[01:30:29]** Porque lembra? O teste é uma grana. Ele tá olhando. Ele é interdependente. Tudo bem. Por enquanto, tudo bem. Eu vou morar um pute lá em users, né? Users. E qual que é o user que eu quero modificar? É o 1, né? Porque que é o 1? Porque eu inserir um user no teste aqui atrás e é tipo assim... O repealante. Mas tudo bem, funciona.

**[01:30:56]** para o nosso propósito de entender as coisas aqui. Então vamos lá, a gente quer um JSON aqui, né? E a gente vai alterar todos os campos que a gente precisa. Então eu preciso alterar o username, que em vez de Alice vai ser Bob. Eu quero alterar o e-mail. E-mail. E o e-mail agora vai ser Bob. Qual que era o e-mail da Alice? Example. Então Bob, eu rouba example.com. E...

**[01:31:27]** A nossa senha, o password, vai ser secret ainda. Segredos. Segredos. Massa? Quando meu chefe perguntar por que o teste é uma time gigante de 50 testes interdependentes com o Banco de Dazim, eu vou falar que eu aprendi com o Dú. Não, eu já falei que a gente vai corrigir isso depois, né mano? Não vem botar culpa em mim pra fazer carregada, não. Response? Legal, a gente quer a resposta disso aqui, a gente vai mandar.

**[01:32:06]** esse put no JSON, que vai ser exatamente isso aqui. Legal? Eu já falei, mano, eu falei, nós vamos corrigir isso lá na aula 5, mano. Não me coupe, não me coupe. E aí, o que a gente espera? Todo put, ele retorna a 200, né? Então return assert, response.statuscode, é igual a HTTP status. Ok, deu bom.

**[01:32:40]** Porque existe esse recurso que a gente quer lá. A gente tem um assert e a gente precisa de alguém para falar, olha, qual que é o JSON, voltou o JSON que a gente queria, e o JSON que a gente queria era exatamente esse aqui. Com o ID1 que a gente vai ter que adicionar, porque o ID vai vir, não vai vir a senha, aquele tipo de coisa toda. Então o response.json, aí o modelo que a gente tinha lá era esse aqui, só que não vem a senha.

**[01:33:09]** Ela não vem a 100, mas ainda vem o ID. E o ID é 1, porque é o ID que foi modificado aqui. 1. Mas não tem nada, não tem nada de muito especial nesse teste aqui. A gente mandou um put no 1, user1. A gente mandou os dados que precisavam mandar. E isso aqui retornou um valor pra gente que é o mesmo user que a gente inseriu com email, username e novos. Vamos ver?

**[01:33:37]** TaskTest vai dar erro de formatação? Não! Ah, maravilhoso! Olha, olha que lindo, olha que cremoso, funcionou. TaskUpdateUser. Mas se ligue, se ligue, se ligue numa coisa aqui agora, presta atenção na tela. MissOne. Ou seja, tem um bloco de código que a gente não testou.

**[01:34:03]** Olha que legal, mano. Então, vamos lá. Firefox, eu vou, sei lá, eu estou no Zen, Zen Browser. E qual que é o caminho? HTML cove index. Eu quero abrir o arquivo de cover e... Sério, ninguém precisa ser doente mental de abrir isso aqui pelo Shell, né? Mas tudo bem, eu sou. Vamos lá. Olha o que que aconteceu aqui. Tudo foi coberto pelos testes. Menos, menos, menos o quê? Essa linha aqui, olha.

**[01:34:37]** O rise não foi testado. Nunca entramos nessa linha no bloco de código, porque a gente fez aquele negócio que a gente chama de branding, né? Tipo assim, em algum lugar do código tem um if, e o nosso teste não entra nesse if. Então, não está coberto. Massa? Ou seja, a gente testou, mas não testou tudo. Tudo bem? Tudo bem e não testar tudo? Tá tudo certo.

**[01:35:11]** É o nosso primeiro erro aqui. A gente não entra nesse if-user, tal, tal, tal. Massa, legal. Temos esse problema. E agora eu vou fazer o delete. Massa, vou fazer um endpoint de delete. Aí vocês estão falando, bota o "-50". Vamos cobrir? Não! Eu não vou fazer isso. Isso aí, eles são de casa para vocês. Mas vamos fazer o delete primeiro. Antes de tudo...

**[01:35:40]** Antes de tudo, vamos fazer o delete. Antes de a gente ir embora hoje, vamos fazer o delete. Mas eles são de casa. Você, você, na sua casa. Olha aqui pra mim, você vai fazer o teste. Não eu. Massa? Então vamos lá. Arroba app.delete. E aí pra gente deletar, a gente segue essa mesma odisseia aqui de cima, né? Pra deletar, precisa ser user ID e tal.

**[01:36:09]** Porque eu preciso deletar alguém, eu preciso falar quem eu quero deletar, né? Então, eu vou deletar o user com ID e tal. Sempre que eu deleto, aí aqui existe uma grande confusão. Aqui vai dar... vai dar briga aqui, né? Alguém vai falar, não, mas aí retorna com o seu que? Retorna com o seu que lá? O delete tem... tem alguma coisa aqui, um ponto específico, que o delete...

**[01:36:37]** Retorna, retorna dados, é uma grande discussão na comunidade. O meu delete vai retornar dados, porque sim. Então, delete, se não retornar nada, retorna 204. Se retornar alguma coisa, retorna 200. Eu vou retornar 200. Mas sou então HTTP, porque vou retornar o status que a gente recebeu. Então, é o status code esse aqui.

**[01:36:59]** O modelo de resposta vai ser o user public. Ah, mas quem precisa saber do usuário que deletou? Não importa, eu quero responder assim. Então, a response model, ele vai responder o user public. Poderia não responder nada. Poderia não responder nada. Vai de cada um. Massa, então, def, delete, user. E aí, o delete user, ele é mais simples, né? Porque a única coisa que ele precisa receber é o ID de quem vai ser deletado.

**[01:37:31]** ele não precisa saber qual é o... o jeizão aqui, né? Porque eu só tô falando, mano, deleta aí. E aí ele retorna os dados, ó, tô deletando você. Era esse... essa coisa que eu tô deletando aqui. Massa, simprão, simprão. E aí o que que a gente vai fazer? A gente precisa montar. A gente precisa buscar lá na lista o registro que a gente quer deletar aqui, né? Então, vamos lá. Quem é o dedo, o objeto, pipipipi, papapó aqui.

**[01:38:01]** Quem é essa pessoa na nossa lista? Então é o ID-1, ou seja, passei 3, ele vai pegar a posição 2 da lista e vai dar um del. Eu vou simplesmente pegar esse registro aqui, então vamos lá. Eu quero saber quem é ele, qual é o número dele, qual é a coisa que ele vai retornar aqui. Então eu vou dar um del nisso aqui, porque ele vai deletar esse registro da base. Eu poderia fazer isso de várias formas, eu posso pegar um pop.

**[01:38:32]** pedir pra ele trazer esse registro pra mim poderia ser também uma forma então posso falar o seguinte ó dá um pop no user-1 aí ele vai tirar da lista e vai me dar isso aqui aí eu posso retornar ele return sim prão assim como é que você vai retornar um ID do usuário que não existe mais então mas eu vou retornar e falar eu estou retornando é essa a ideia que eu estou retornando o ID existia na época né

**[01:39:00]** Durante isso aqui. Então, eu vou fazer esse rolezinho aqui. Só que tem um ponto aqui, né? Aí vai repetir de novo aquela história, né? Tipo assim, e se eu pedir um pra deletar alguém que não existe? Então, e se eu fizer tal XPTOYZ de coisas malucas lá? Então, eu tenho que fazer sempre isso aqui, né? Então, eu vou ter que ter aquele if de novo. Então, se for menor do que um ou se for diferente do lendo, da tabesa e tal, a gente vai pegar isso aqui e vai retornar.

**[01:39:32]** Ah, lá fora. Massa? O... O Cox... Mandou aqui. Nesse caso, é melhor criar um teste para cada cenário do método implementar mais esse teste para englobar tudo. Cada coisa é um teste separado e isolado. De... De... De... Quebra! É importante que um teste não dependa do outro, ok? A gente está num formato ludic hoje. Mas a ideia é que nada dependa de nada aqui para acontecer. Beleza, vamos ver se a gente consegue fazer o delete?

**[01:40:13]** Então, a gente tem aqui, vamos lá, vamos lá, vamos lá, vamos lá, vou dar o F5, ó, delete de outra cor, delete vermelho, vermelho que quebra tudo. Então, vou dar um post, vou criar aqui o nosso 1, ou seja, agora temos o username StringUser, eu vou listar ele aqui pra gente ver se tá tudo certo. Então, ó, tá aqui, na listinha. Massa, agora a gente vai deletar ele. Vamos lá, então, try it out, delete 1.

**[01:40:41]** Execute, voltou pra gente, foi esse usuário que a gente deletou da base de dados. Então username, tal, tal, tal, tal, tal. Se a gente vier aqui no get agora, esse usuário não pode mais estar lá, né? E ali está vazia, o que significa que terminamos o ciclo. Terminamos o ciclo. Uma outra coisa importante é o seguinte, o delete, se eu deletar o zero que não existe,

**[01:41:06]** UserNotFound, só deletar o 1, que agora não tem mais ninguém, também tem que dar 404 UserNotFound. Lindo, ó, maravilhoso. Falta o quê? Um teste pra isso aqui, né? E o teste é muito sim pra um, né? É aquela coisa maravilhosa, né? Então, vamos lá. DefTestDeleteUser.

**[01:41:31]** do client. A gente sempre tem client, client é linda, né? Fala, fala. Nossa, não ficou legal essa fixture aqui. Ficou linda, né? Vai, fala, fala pra mim. Então, a gente vai chamar o client, vai chamar o método delete, delete. E a gente vai deletar o users, barra um, né? O user um. Por que a gente vai deletar o user um? Porque o user um foi quem a gente deletou, foi quem a gente criou, né? Nesse teste aqui, ó, que tal que, ó.

**[01:41:58]** Teste ou hippie lunch, né, mas tudo bem, tá aqui. Essa é a ideia. Então isso aqui vai dar um response. E aí o response que ele tem que dar é que ele deletou esse, essa coisa aqui ó, esse aqui ó. Ele deletou o Bob. Por quê? Porque o Bob foi inserido no outro teste. Não era pra inserir ele aqui, não era pra ele ter aqui, não, mas... Tudo bem, tudo bem.

**[01:42:24]** E aí, a gente tem o response aqui e a gente precisa garantir que voltou 200, né? Então, assert response.status.code é igual a HTTP status.ok. Se, só aquela coisa, se não voltar nada, ele é, como é que é o 204? Eu esqueci o 204, no content. Se voltar sem nada, se não tivesse essa resposta, seria no content. Então, ok.

**[01:42:52]** Mas, então, em teoria, esse teste agora ele passa, porque ele deleta o único usuário que tinha que foi inserido no outro teste, que nem deveria ter sido inserido. Mas, é isso, vamos rodar o teste? Yay! 100%! Ó, é o Vivo Replay, é replay, mano. É replay, toda hora fica rodando o mesmo teste do novo aqui, nunca termina. Legal, funcionou, ok, nice. Temos mais um miss aqui, vou voltar lá no browser, vamos ver o que que é.

**[01:43:32]** De novo, ó, tudo testado, menos os branchings, os ifs que caminham aqui pelo lado, né? Massa, 93%. É, 96%, 97% de coverage, ó, que lindo. 93% no arquivo, 95% no total, né? Legal, funciona, massa, lindo, maravilhoso. Porém, com tudo entretanto, todavia...

**[01:44:05]** Ainda não tá 100%, né? Não tá 100% por vários motivos, né? O primeiro motivo é o mais importante do que não ter cobertura de 100% do código é um teste ser interdependente do outro, né? Um teste é acoplado com um teste que rodou antes. Isso não pode acontecer, ó, de novo. Alguém falou que vai dar essa justificativa no trabalho? Não fui eu que disse isso aí, hein, mano? Se me usarem como justificativa, é mandar o link dessa live aqui. Não fui eu que disse, hein?

**[01:44:38]** Mas é isso, então a gente precisa resolver esse problema, que a gente vai resolver lá na aula 5, e falta fazer essas branchings, esses ifs por onde o código entra, assim, o código está vindo aqui, assim, aí ele faz um... puxa uma perna para o lado, né? Então a gente vai ter que resolver isso. E a função de vocês é resolver isso aqui, né? Então vocês vão ter que escrever um teste com 404, né? Para o endpoint de pute. Esse é o primeiro exercício.

**[01:45:07]** O segundo exercício é fazer o teste do 404 do delete. O terceiro aqui, aí o terceiro é uma coisa mais bonitinha aqui, que é o seguinte, a gente vai ter que criar um endpoint de get, ó, um endpoint de get que pegue users id. Massa? Então é pra você fazer a mesma coisa que a gente fez no put no delete, sabe que tem aquele user id lá no final? Chavinha user id.

**[01:45:38]** Então eu quero que vocês façam um endpoint disso para que a gente possa fazer um get de um user só. Ou seja, em vez de retornar sempre a lista com todo mundo, é para fazer esse esquema de retornar um só. Ou seja, me dá o dado da bug, que era o id3. Então eu passo o 3 e ele retorna a bug. Ah, me dá o do regs, que era o 1. Então a gente vai fazer...

**[01:46:03]** esse esquema e aí como ele também pode dar erro porque o ID pode não existir vai ter que fazer um teste para 404 e vai ter que fazer um teste para 200 esse é o exercício lição de casa então para semana que vem exercício lição de casa e obviamente não esqueça de responder o quiz não pode esquecer de responder o quiz em mano quiz tá aqui para ser feito ok massa

**[01:46:33]** e aí para a próxima aula tem o esquema sobre a gente vai mexer com banco de dados na próxima aula e aí agora tipo assim todos os suplementares são suplementares assim não precisa ver e tal mas eu gostaria tipo de verdade de verdade se você tiver um tempo no final de semana por obisequio sabe tipo assim olha do amor

**[01:47:03]** que eu tenho por vocês aqui. Por Obiséchio, assistam essas duas lives aqui. A Live 258 e a Live 211. A Live 258 vai explicar como funciona a biblioteca de banco de dados que a gente vai usar. O Toolkit, que é o SQL Alchemy. E a Live 211 explica como funciona o esquema de banco de dados evolutivos. Então, sério. Por favor.

**[01:47:33]** por favor a gente vai explicar um pouco se você não tiver tempo tem família eu entendo mas se você tiver um tempo assista essas duas lives e dessa vez eu tô pedindo com todo amor no coração assim por favor vai ser muito útil na próxima aula e porque vocês já vêm com algumas perguntas vocês não vão me fazer assim saca então assistam essas duas lives a 258 e a 211 se der tempo

**[01:48:02]** Se sabe, ah, tô sem fazer nada. Assiste a 207, a 207 é importante. Mas essas duas aqui, eu preciso que você assista. Pra gente conseguir conversar na semana que vem. Saca, ah, não deu tempo, tudo bem, ok? Mas se der tempo, sabe, tá ali ó, vou dormir mais cedo hoje não, assiste essas duas lives aqui. Por favor. Legal?

**[01:48:29]** Duno, tem como pegar o código das aulas para fazer o exercício? Então, André, a ideia é que você faça a aula, né, mano? Tipo assim... Tipo assim, eu quero que você faça o código todo, né? Só que tem códigos que eu não vou fazer, mas... Assim, a ideia é que você faça o teu próprio código, vai fazendo junto com a gente, vai brincando... Então, deixa eu dar um git status aqui...

**[01:48:51]** Beleza, a gente alterou o app, a gente criou mais esquemas, a gente criou mais testes e criamos esse arquivo com o ftest, né? Eu vou dar um git add out para todo mundo aqui, implementando rotas crude. Olha que comite bonito aqui. Massa, e eu vou dar um git push e subiu. Tá lá, lindo, maravilhoso. Quem quiser pegar pode pegar lá o código, quem quiser comparar pode comparar. Tá tudo lá. Legal, então respondo um quiz.

**[01:49:24]** Façam os exercícios e tudo mais. Aí o Lu está perguntando se essa aula está atualizada. Sim. Todas as aulas estão atualizadas. Na verdade, o curso em vídeo era que estava desatualizado. Pra caramba. Massa? Então agora que a gente comitou, subiu isso aqui. Deixa eu falar meus últimos recados aqui. Puro biséculo. Assistam as duas lives. Façam os exercícios do quiz. E...

**[01:49:58]** Tá liberado, quem quiser ir agora pode ir. Mano, eu tô liberando todo dia mais cedo hoje, 10 minutos mais cedo, hein? Quem tiver coisa pra fazer pode ir, mas quem tiver perguntas pode me perguntar. E de novo, sabe? Respeito o tempo da galera, mano. Pergunta de coisa da aula, mano. Não é pra perguntar, nossa, que editor de texto é esse aí? Que cor de fonte. Tá ligado? Tipo assim, perguntas da aula. Porque a gente sabe que tem gente que precisa dormir, mano. 10 horas da noite.

**[01:50:29]** Ah, bug, não assistirei esse final de semana, pois estarei no Pai Caxias, mando um abraço para a galera lá do Pai Caxias. Então, é isso, a gente viu, tipo assim, a gente misturou os dois conceitos, a ideia era essa, tipo assim, na aula passada a gente viu muita teoria e a ideia dessa aula era ver totalmente a prática das coisas que a gente implementou lá atrás, né? Então, se ninguém tiver perguntas aqui, a gente se despede, dá um beijo e se vê na terça-feira, de novo, né?

**[01:51:03]** E aí a gente vai conversar sobre essas coisas, sobre banco de dados, sobre migração de dados, sobre testes com banco de dados e cositas mais. E aí, se você chegou no fim, não deu tempo de fazer sua pergunta, manda lá no grupo da Telegram e a gente conversa. Massa, mas ó, assiste essas duas lives, pelo amor de Deus. Para a gente ganhar tempo na próxima aula. Bom, beijo para vocês, ó, e tchauzinho.

