# Transcrição da Aula: aula-08.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:04]** Olá pessoas, boas-vindas. Há mais uma live do nosso Curso de Festa IPI. Eu sou o Dono Sauru e olá pessoas. Como vão vocês? Vocês estão me ouvindo bem? Vocês estão me vendo bem? Só para saber se está tudo funcionando? Galera, antes de tudo, eu queria dizer uma coisa. Eu tô meio gripado, então se eu pausar para espirrar ou para doce, desculpe em diante mão, assim. Talvez eu faça isso muitas vezes na live de hoje.

**[00:00:33]** Ainda não estou muito legal para ficar falando, mas é só um aviso. Beleza? Então, se estiverem me ouvindo, se estiverem me vendo, vamos lá. Hoje a gente vai conversar sobre programação assim, Bruno. É sobre como transformar o nosso projeto em assim.

**[00:00:52]** Basicamente, essa é a ideia da nossa aula de hoje. Então, a gente tem um projeto, a gente trabalha com Fast API e tudo mais, e agora é a ideia que a gente introduza, assim que aí ou, ou usar, assim que ir ao 8, aqui dentro. Então, é sobre isso, sobre isso a nossa aula de hoje. E, bom, quem precisar já sabe, tem o material de texto. No material de texto tem umas imagens aqui.

**[00:01:18]** que talvez eu recorra elas aqui para ficar mais simples, porque são coisas que não cabem muito bem no slide, mas a gente pode scroll lá, então talvez eu venho aqui em alguns momentos. Massa, então, tem bastante coisa lá. Eu tentei traduzir a sala de uma forma menos massante, porque eu testo...

**[00:01:37]** Eu vi que às vezes dá uma truncada em alguns momentos. Então, o que a gente vai conversar hoje? Eu vou tentar introduzir os conceitos de programação assíncrona e dei um enfoque na palavra introduzir, porque é literalmente uma introdução de verdade, né?

**[00:01:55]** Aí a gente vai tentar refatorar, a gente não vai tentar, eu espero que a gente consiga refatorar a aplicação inteira para usar a 5IO, tanto a parte do Banco de Dados quanto a parte do Festival IPA, que são dois lugares. E aí os testes, também tem alguns LANs que precisam conversar melhor com essa parte acíncrona, tanto os testes em si quanto as fixtures, tem algumas fixtures importantes que a gente vai ter que transformar em acíncrona e tudo mais.

**[00:02:24]** E bom, antes de a gente começar aqui e passar pra isso, eu quero saber de vocês se vocês têm alguma experiência com programação acíncrona. Se essa é a primeira vez que vocês estão vendo isso, vocês assistiram a live que eu recomendei, né? O material da última live sobre programação acíncrona, então quero saber de vocês aí. Enquanto isso, eu agradeço aqui o Leonardo. Obrigado, mano, valeu demais. Espero que você esteja curtindo e, mano, esse super chat me ajuda muito. Então, valeu.

**[00:02:52]** Bom, na primeira parte aqui, enquanto vocês vão me respondendo, eu queria conversar com vocês sobre o esquema a parte do bloqueio da aplicação, né? O que que acontece e por que que a aplicação fica bloqueada e por que que assim que é legal e nesse sentido? Bom, basicamente, a forma como a gente está construindo a nossa aplicação tem alguns momentos, né? Em que a gente conversa com sistemas externos, né?

**[00:03:22]** De vez em quando, você pode pensar que na nossa aplicação não tem muitos momentos, a gente tem o banco de dados, mas isso serviria para qualquer outro tipo de conexão externa. A gente poderia usar um storage, a gente poderia recusitar uma outra PI. Tem vários momentos aqui que isso acontece. Então, a gente está pensando nisso como bloqueio de IO.

**[00:03:49]** E aí, aiou, né? É input, output. E quando eu digo bloqueio, a gente fica com essa cara tipo assim, nossa, a aplicação tá travada e tudo mais. Na verdade, a aplicação, ela fica em um estado que a gente chama de IDOL, né? Em inglês, que ela tá aguardando alguma coisa acontecer, né?

**[00:04:07]** Basicamente, toda a nossa aplicação, ela se baseia nisso, né? A gente vai receber a requisição, a requisição faz o quê? Valido o esquema, né? Antes de entrar, né? Se não, ele dá 422 no Piedantic. Aí, depois, ele se conecta ao banco de dados, né? E aqui, eu não tô dizendo uma conexão real pro banco de dados, porque é a Ingenie que faz isso, mas a gente levanta a Session, né? E a Session se comunica com a Ingenie e tal, e nesse momento, a gente tá aguardando a Iona.

**[00:04:34]** Eu falo ó, preciso performar uma ação no banco de dados. E aí essa ação, a gente fica aqui esperando que alguma coisa aconteça. A aplicação não está travada, ela não está em estado nenhum, ela está simplesmente aguardando que alguma coisa aconteça. Ou seja, a gente chama isso às vezes de bound.

**[00:04:58]** Alguma coisa está limitando a aplicação, e essa coisa é um input altput. Massa? Fernanda, obrigado aí pela Melhoras, e ela lembrou de deixar o like, então deixa um like aí para a gente poder espalhar esse conteúdo na internet para mais pessoas. Então, basicamente, toda vez que a nossa aplicação fica parada esperando alguma coisa, a gente está aguardando um agente externo de I.O. A gente fala que essas operações são bloqueantes.

**[00:05:29]** Lembrem disso, ela é bloqueante porque a minha aplicação está parada.

**[00:05:35]** Esperando alguma coisa acontecer, e essa coisa vem de fora, é de Iona. A gente tá enviando alguma coisa, a gente manda um output e fala ó, banco, faz essa busca pra mim. Aí o banco tá fazendo essa coisa, enquanto isso a gente tá esperando o banco voltar, então o input. Então são esses bloqueios que a gente tem na aplicação. E a aplicação fica parada nesse estágio tipo assim, ah, o que que eu vou fazer agora?

**[00:06:02]** eu dependo da resposta de alguma coisa, não? Então é esse esquema, então a gente vai ali do esquema, conecta, faz algumas operações, aí a gente aguarda o banco de dados de novo, a gente repassa uma coisa, faz um commit, faz um select, faz um update, e aí depois a gente retorna ao recurso. Então você está vendo que dentro da nossa aplicação a gente tem esses dois momentos, quando a gente está conversando com o banco de dados que é o único sistema externo que a gente tem, a coisa é bloqueante por natureza, não é?

**[00:06:32]** Trazendo isso para uma coisa bem mais palpável, aqui a gente tem o nosso código de update que a gente faz. Então lembra que no update a gente requisita a session, então a session conecta na engine do banco e depois a gente pede o current user para saber quem é o usuário que está logado a partir do token que ele enviou no JWT.

**[00:06:54]** E aí, depois a gente vê qual que é o usuário e tudo mais, a gente faz algumas operações com o RM, depois a gente dá o commit, dá o refresh, retorna isso aqui para o usuário. Basicamente, se você for parar para pensar numa questão de fluxo, o que está acontecendo aqui, né? Então, conecta no banco de dados, aí algumas operações vão, aí repassa para o banco, aí a gente volta, faz mais algumas operações, repassa para o banco e tudo mais, a gente fica nesse ping-pong, com o banco de dados.

**[00:07:23]** e toda vez que a gente faz essa chamada externa para o sistema externo, a gente fica esperando a resposta. Aí alguém pode pensar que isso aqui, tipo assim, nossa, mas isso é muito ruim, né? Porque isso demora muito tempo. Então, as respostas são muito rápidas. Elas são respostas de milissegundos. Só que durante esses milissegundos, a gente está esperando a aplicação fazer alguma coisa.

**[00:07:49]** Sabe, é um tempo perdido da aplicação. A aplicação está rodando, mas ele está aguardando, está bloqueada, porque para fazer o próximo passo, pensa de forma procedural. Linha 1, linha 2, linha 3, está esperando a resposta. Aí para ele ir para a linha 4, a coisa tem que voltar.

**[00:08:08]** Então, existem várias formas de bloqueio. Dentro da nossa aplicação, nesse momento, a única coisa que bloqueia o fluxo é o banco de dados. Então, a gente está nesse pontinho aqui. São milissegundos, mas ainda assim, são probleminhas, pequenininhas, né? Só que uma coisa que tem que ficar clara aqui, que é uma coisa que geralmente confunde as pessoas,

**[00:08:33]** Olha que eu já vi umas buscas no banco demorarem mais do que isso, né? É, então. No nosso caso, estou dizendo, demora alguns milissegundos. Mais uma coisa que precisa ficar clara aqui, e agora eu quero que você preste atenção nesse mantra aqui junto comigo. O bloqueio é da aplicação.

**[00:08:53]** O bloqueio é da aplicação. Comenta no chat aí para ficar martelado na cabeça. O bloqueio é da aplicação. Massa, lembra que a gente estava falando sobre a SGI? A gente tem um servidor, que é o UVcorn e o UVcorn ele não é bloqueante. Massa, então o nosso aplicativo é quem está bloqueado.

**[00:09:20]** Massa, a web comunica com o banco de dados e é quem está bloqueado. O servidor não está bloqueado. Massa, faz sentido isso aqui? O servidor, ele nunca deixa o servidor de aplicação, ele nunca deixa de receber as mensagens.

**[00:09:41]** Como a nossa aplicação está bloqueada, a gente está processando uma requisição por vez, mas o servidor recebe todo mundo que chega, né? A gente chama isso aqui, por exemplo, no Yuvicorn, na pilha TCP de uma maneira geral, no protocolo TCP, que é a camada de transporte, quando essas coisas chegam na porta em que a gente está ouvindo, a gente vai criando um backlog.

**[00:10:07]** Isso o próprio protocolo faz isso, não é o UV-Corn. E aí, por padrão, o UV-Corn recebe 2048 chamadas no backlog. Massa? Então, daquele jeito que a gente roda, UV-Corn, tal, tal, tal, ou FastAPI, DEV, XPTO, a gente pode receber e esperar, né, para responder 2048 requisições.

**[00:10:35]** e tudo isso vai ficando no backlog. Então, beleza, chega aqui, a gente recebeu uma coisa. Aí a gente retorna. Pô, já tinha outra que chegou no backlog, então a gente retorna, a gente processa a próxima. E assim a gente vai nesse ciclo. Então existe um backlog, né, um lugar onde estão armazenadas, sei lá, uma pila, né? Então cada requisição que chegou está em ordem e aí a aplicação ela vai retornando uma por vez.

**[00:11:04]** Massa, faz sentido isso aqui? Então, quem está bloqueado por IOU é a nossa aplicação. Não é o servidor da aplicação, não é o UVCorn. Massa, entendidos aqui, esse é o mantra, o bloqueio não é do servidor, o bloqueio é da aplicação. Massa, Jiu, obrigado por atualizar seus membros, ó.

**[00:11:35]** Beijo pra você. Valeu. Isso me ajuda muito. Aí deixa eu voltar aqui pra cá. Tanto que uma das características de um servidor, né, é porque a galera pode pode estar se perguntando, ah, mas como é que isso funcionava, por exemplo, antes de ter programação acíncrona no Python ou quando a gente usava Flask ou Django, que é bloqueante por padrão, não tem suporte a programação acíncrona ou concorrente, como a gente chama em português.

**[00:12:07]** O servidor pode fazer cópias da nossa aplicação. Ou seja, eu tenho um servidor aqui e o servidor gerencia várias cópias da minha aplicação. A gente chama isso de workers, né? Então são os workers da aplicação. E isso aqui criou três cópias da nossa aplicação. Então, o UVCorn tem um algoritmo dentro dele que se chama round robin.

**[00:12:40]** E aí, cada requisição que o cliente chegar, se a gente estiver nesse caso, cliente um, dois, três, ele vai mandar para que a gente estiver desocupado. Pô, manda um para cá, aí o segundo request vem para cá, o terceiro request vem para cá, era assim que funcionava antes dos frameworks terem suporte à programação acíncrona. Então, se a gente rodar isso aqui, o uv-corn e tal, tal, tal, fest zero app aqui, que é o nosso, a nossa aplicação, que não é exatamente isso aqui, né? Porque é...

**[00:13:09]** Feste API zero aqui. Sem te rodar isso aqui lembrando que eu já estou no no ambiente virtual, né? Meu bem invitativo aqui. Olha o que que acontece.

**[00:13:22]** O Uvicorn está ouvindo na porta oito mil, mas ele levantou um, dois, três processos diferentes. Ou seja, tem três cópias da nossa aplicação ouvindo. E isso aqui é o do próprio Uvicorn. Ou seja, mesmo a aplicação estando bloqueada, a gente consegue responder três por vez. Faz sentido? Ah, mas eu preciso de vinte. Legal. Está aqui. Vinte processos.

**[00:13:53]** que a gente vai conseguir responder por vez rodando a nossa aplicação. Então, o servidor não é bloqueiante, quem bloqueia é aplicação, de novo, tem que sempre ficar claro, né? O Kai falou, entendido, meu camarada, o bloqueio é da aplicação. Obrigado pelo teu super chat, mano. Tamo junto. Então, dessa forma aqui, a gente pode subir any workers para trabalhar dentro da nossa aplicação. E aí, a gente vai...

**[00:14:23]** Responder três por vez, mesmo a aplicação tá ando bloqueada. Ah, tá parado esperando a Iona, tá em Aido, né? Esperando alguém respondeu a Iona, não importa. Tem o outro disponível? Tenho. Então ele responde...

**[00:14:37]** A próxima requisição. E o próximo. Aí beleza. Ah, mas aí chegou 4. O que que acontece? Ele cai nesse esquema, né? Então fica no backlog do UV-CORN. Quando alguém liberar, a gente sobe a próxima. Então a ideia aqui não é que processa-se 1 por vez. Pode-se processar n por vez. Mas não deixa de ser bloqueante. Fez sentido isso aqui?

**[00:15:02]** A ideia principal aqui é tirar essa coisa, desgrudar, que a aplicação está bloqueada, mas o servidor continua ouvindo, respondendo e trabalhando normalmente. O Everton disse, do, só para ficar claro, o bloqueio da aplicação, exatamente. Muito bom, pera aí. Então, o bloqueio da aplicação. Massa, ficou claro.

**[00:15:33]** Espero que tenha ficado claro que a gente é capaz de responder várias requisições ao mesmo tempo, mesmo sendo bloqueantes.

**[00:15:45]** E aí quando a gente para para pensar nisso, a gente tem que parar para pensar como é que uma aplicação não seria bloqueante, né? Como é que a gente não travaria nesses milissegundos ou segundos, às vezes, como disse o... como disse o Takoni, pô, já vi uns que demoram bem mais, então, como é que a gente faz para aplicação não ser dessa forma? Então, para aplicação não ser dessa forma, a gente vai usar um conceito do Python que se chama corrotinas, né?

**[00:16:14]** Existe esse assunto aqui de corrotinas só para fazer um adendo. Ele tem corrotinas sincronas, corrotinas acíncronas. Existem outros tipos de coisas concorrentes como tasks, como futures, mas eu vou me limitar no escopo aqui para fazer sentido para a gente, o mais simples. Então, em Python, existem essas coisas que são corrotinas.

**[00:16:42]** Para definir uma corrotina em Python, basicamente a gente precisa com que a função se chame com essa combinação de palavras aqui. Assim que def. Ou seja, eu falo que essa função ela é assíncrona. O que que significa assíncrono? Então vamos lá. Assíncrono tem uma palavra que chave, que é tipo assim, escalonado, né?

**[00:17:15]** Significa que essa função pode escalonar, né? Ela pode ser trocada, né? Então, em algum momento a gente está processando uma coisa, e a gente troca e faz a outra coisa, e a gente troca e processa essa outra coisa, e a gente vai escalando, né? Trocando entre coisas. Vocês querem um exemplo de escalonamento? Eu gosto muito do que Luciano Ramalho deu uma vez em uma palestra, eu gosto bastante, e aí eu quero contar para vocês. Jordani, muito obrigado.

**[00:17:45]** É só pegar a máquina maior e subir 10 works. Exatamente. Sobe 20, 30, 50, escala, horizontal, né? Daniel, muito obrigado, mano. Eu estou super chat. Valeu, meu querido. Tamo junto. Vocês me ajudam muito. Então, vamos pensar no que é um processo de escalonamento. Vocês já viram aquela pessoa no circo girando pratos? Sabe? Só para a gente ver se eu acho uma imagem aqui. Vocês já viram isso aqui? Uma pessoa fazendo isso aqui?

**[00:18:27]** Girando pratos. Você vê que a pessoa, ela gira um prato por vez, né? Ela sobe lá, ela gira o prato, aí o prato fica girando em cima. Aí o prato continua girando lá. Aí ela vem e pega e gira o outro prato. E aí depois ela fica nessa dinâmica, girando o prato, só o prato que está parando. Faz sentido isso? Isso é escalonamento. O girador de pratos processa, ele trabalha no prato que está girando.

**[00:19:00]** É o escalonamento. Caldeirão do Hulk tinha direto. Memórias, né? Então, legal. É o escalonamento. E como é que a gente diz pro Python que essa coisa é escalonável, né? A gente usa essa palavra chamada await. Então, sempre que a gente quer transformar a função numa corrotina, ou seja, uma função que pode ser escalonada, a gente usa assim que deve.

**[00:19:32]** E toda vez que a gente vai falar, olha, aqui eu vou esperar a yo, sabe? Aqui eu vou bloquear. Aí eu uso essa palavra chamada await. E quando a gente usa await, o girador de prato vai para o próximo. Ou seja, eu estou esperando o prato parar de girar. Então pode ir para o próximo, e aí ele gira o próximo. Massa! E aí esse momento de escalonamento é o await.

**[00:20:04]** Ou seja, transformamos a função em uma corrotina, então colocamos a sinc. Então toda a função com a sinc é uma corrotina sincronona. A gente pode chamar só de corrotina aqui. E aí toda vez que eu for...

**[00:20:21]** Depender de algo, ou eu vou travar, sabe? A aplicação, falar, olha. Agora eu vou fazer a way, agora eu vou fazer bloqueio. Por exemplo, session.scalars roda um select no user. Saca, isso aqui é uma função que a gente tem no código. Aí eu boto essa palavra na frente, await, ou seja...

**[00:20:41]** Roda isso aqui, roda esse bloco de código, esse bloco de código vai ficar pendente, enquanto isso está acontecendo, vai fazer outra coisa. Fez sentido isso aqui? Qual é a função dessas duas palavras, async e await? De verdade, eu estou tentando ir devagar para a gente ir conversando sobre isso juntos, assim. Eu não me importo se a gente vai que fazer, partir essa aula no meio e fazer outra, tá tudo bem?

**[00:21:12]** Fez sentido isso aqui. A função, né? O que exerce, né? O assim que é weight. Vladimir, obrigado, mano. Pra tomar um monstreio gelado, ó. Tamo junto. Valeu demais. Bom, eu vou seguir aqui, né? Porque ninguém me disse nada, mas... Enquanto vocês vão conversando comigo, a gente vai vendo. Sempre que você... É tipo a mãe falando, vai fazer outra coisa. É tipo... Sabe quando você tá... Quando você tá fazendo comida?

**[00:21:48]** Você só consegue mexer uma panela por vez, né? Saca, então você tá prestando atenção em uma coisa só, né? Você não consegue girar uma mão pra frente e outra pra trás. Você só tem duas, e a terceira, se você precisar ir pra frente e a outra pra trás, assim. Sabe, é esse esquema. E... Uma coisa interessante é que, pô, Jordani, obrigado, mano, pelo teu superchat. Tamo junto, velho. Ó! Valeu demais, mano. Provei o bali. Uma coisa legal aqui...

**[00:22:22]** É o seguinte, quando a gente roda uma função em Python, né, sei lá, def xpto, a gente retorna um valor, né, return 42, por exemplo. A resposta para tudo, né, então xpto. Olha o que que aconteceu, retornou 42, né, é uma função Python. Normal, tradicional, uma coisa que a gente faz toda hora. Se essa função fosse uma corrotina, ela começasse com a palavra reservada, assim que, se eu tentasse executar essa função xpto, ele não deixa eu executar.

**[00:22:54]** Está vendo? Ele falou, ó, isso aí que você criou é um objeto de corrotina. Ele não executa, ele não me deu 42. Saca? Entendeu? Então, ele sempre retorna esse objeto corrotina. E aí, para essa corrotina ser executada, alguém tem que executar a corrotina. Ou seja, o código diretamente ao chamar não vai ser executado. Ele criou, criei essa corrotina.

**[00:23:28]** Quem é que executa as corrotinas, né? E aí é uma coisa que a gente chama de event loop, em inglês, ou um loop de eventos. E aí um loop de eventos é uma coisa muito mirabolante aqui, né? Imagina o seguinte, lembra do burro do Shrek que ele vai para tão, tão distante e aí ele fica perguntando, já chegou? Já chegou? Já chegou? Já chegou?

**[00:24:02]** Lembra dessa parada? Já chegou? Já chegou? Já chegou? Já chegou? Que sai com criança no carro? É esse esquema. Já chegou? Já chegou? Então, qual é que é a parada aqui? O event loop, ele cria uma fila em memória com várias corrotinas, né? É como se ficasse uma coisa assim, né? Tipo, vamos pensar. Ele tem o xpto, o xpto e o xpto pra executar.

**[00:24:31]** Aí você está vendo o que tem aqui ó, corrotina, corrotina, corrotina, corrotina. Ou seja, ele pega uma corrotina por vez e ele executa. E aí quando ele encontra um await, ele larga isso aí na fila de novo, chegou aqui, então a gente pega, a gente vai tratando um por um, a gente pega o primeiro, analisa. Aí quando a gente encontrou o await, a gente sabe que vai demorar, a gente pega o segundo da lista.

**[00:25:04]** A gente pega esse aqui, então a gente tava olhando esse aqui. Pô, encontrei um await, aí ele pula pro próximo. Aí ele vai executando até chegar o próximo await. E aí ele vai pulando pro próximo. E aí o que que acontece? Quando tá todo mundo bloqueado, ele fica voltando nisso aqui e fica pra todo mundo. A resposta de aí hoje já chegou? Não. Próxima. A resposta de aí hoje já chegou? Não. Próxima. A resposta de aí hoje já chegou?

**[00:25:33]** Então ele vai executando todos os códigos, até encontrar os Awaits e aí ele troca. Então lembra do escalonamento, é isso que Eventloop faz. Ele pega, executa até o Await, aí ele joga para lá, aí ele pega o próximo, executa até o Await e joga fora. E vai jogando nessa lista, né?

**[00:25:52]** Nessa Kiwi, não é? É uma fila de coisas que tem para ser processado. E ele vai trocando. E aí, quando ele termina de processar todo mundo, ele fica... Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já chegou a resposta? Já

**[00:26:17]** fez sentido isso aqui então existe uma coisa em Python que processa corrotinas essa coisa é o event loop do async.io né se a gente for lá e falar só lá importe async.io essa é a forma ruim de usar o async.io mas eu acho que vai fazer sentido aqui pra vocês então eu tenho async.io aqui async.io e aí eu peço get event loop falou me dá o loop de eventos aí eu falo loop

**[00:26:50]** Roda, run, until complete. Roda até terminar a corrotina xpto. Pronto, olha a resposta aqui. 42. Olha que massa. Olha que super interessante isso aqui. E aí o loop roda e dá o resultado. E aí se a coisa tiver várias paradas aqui dentro, tipo assim, a weight, a weight, a weight, ou assim que aí eu tenho um slip.

**[00:27:32]** E aí eu vou dar um slip de 10 segundos aqui dentro. E aí vamos rodar o xpto de novo. Mas está vendo que ele não para, né? Ele não dá slip. Aí a gente vai conversar sobre isso depois. Mas a gente dá um slip de troca. Só para falar, olha. Escalou, né? Mas é essa coisa. Se você for rodar um código acíncron, né? O acínque aí eu tenho rum. rum. Aí você passa a corrotina que você quer aqui.

**[00:27:59]** E assim que... esqueci o Iona. Assim que é o Run. Aí ele tá falando olha, esse negócio que você deixou aqui, olha o erro, olha o erro que é interessante. Olha, deu um erro aqui nessa, tá essa coisa, que você tem uma corrotina chamada Sleep, e você nunca espera por ela. Então dá um await aí, Barça. Aí você vai lá e dá um await. Aí agora você executa de novo. Olha, travou por 10 segundos. Olha que sensacional.

**[00:28:31]** Aí ele tá travado. Como a gente não mandou o loop rodar nenhuma outra coisa, ele deixa passar. Tem algumas funções no sync.io, né? Por exemplo, o sync.io.getter, que você passa uma lista de funções aqui, por exemplo. Ah, vou passar o xpto, xpto e xpto. Aí você tem que pedir para ele rodar isso aqui, né?

**[00:28:57]** Então tipo assim, assim caiou, run, tal, tal, tal, tal, tal. E aí ele vai rodando todas essas coisas que você quiser e ele fica nesse. Já chegou, já chegou, já chegou, já chegou. Então é uma piada aqui, mas é pra vocês entenderem esse esquema aqui. Quem é mais sagaz aqui já notou uma coisa que ficou nesse slide aqui. Olha, olha isso aqui. Node.js Event Loop.

**[00:29:24]** Quem tinha anotado que na minha imagem tinha o Node.js Event Loop? Alguém tinha anotado isso aqui? Ou não? Ou fui só eu? Esse slide está com esse Node.js Event Loop porque eu peguei de um site que tinha essa imagem do Event Loop que eu quis usar, está aqui embaixo. Mas aqui é a explicação do Node.js. Só que...

**[00:29:53]** Lembra que a gente usa uma coisa em Python, que a gente usa toda hora, que é o uv-corn? O uv-corn, ele usa um loop de eventos do Python, que não é o loop do assim que a eu, que a gente pediu, assim que a eu é o ponto get-event-loop. Ele usa um uv-loop. Ele usa uma coisa chamada uv-loop. E aí, uv-loop é a base do uv-corn, por isso que ele se chama uv.

**[00:30:27]** no começo e aí o UV o UV loop é implementado em uma biblioteca chamada LibUV para quem quiser prestar atenção depois então a gente tem aqui, vamos lá a gente tem o UV Horn que roda o loop acíncrono UV loop que usa uma biblioteca chamada LibUV por baixo a LibUV

**[00:30:56]** é a mesma biblioteca que é usada no event loop do Node.js. Então, se a gente ver aqui, então, LibUV é LibUV. Olha que interessante. É a mesma biblioteca para todo mundo. Todo mundo usa o loop UV. Aqui, ó, o Node.js, a Julia, a outra linguagem, o UV loop.

**[00:31:30]** E tudo mais, tá vendo? Todo mundo usa a mesma biblioteca C por baixo dos planos, que é essa biblioteca chamada LibUV. Massa, então fica aí a título de curiosidade isso aqui. Então é isso que faz, então essa biblioteca LibUV lida com as entranhas do sistema operacional.

**[00:31:53]** E fica pegando aqui, ele queria várias threads no sistema para ficar esperando coisas e tudo mais. E aí, a gente tem esse processo que é o loop, que é o UV loop, que fica rodando aqui, roda, roda, roda, roda, roda, já chegou, já chegou, já chegou, já chegou. Então ele fica conversando com coisas do sistema operacional e respondendo para a gente ao mesmo tempo. Legal isso aqui? Então, é basicamente esse funcionamento disso aqui por baixo dos planos. Aí...

**[00:32:27]** Tem uma outra palavra aqui, né? Tipo assim, fora o escalonamento, né? Vamos começar pelos escalonamentos, né? O escalonamento é o que o loop faz ao trocar entre corrotinas. Mas, lembra, a gente falou isso. Toda vez que a gente encontra um await, a gente pula, né? De um lado para o outro. Então, o loop escalona toda vez que ele tem um I.O. Um bound de I.O., um bloqueio de I.O.

**[00:32:57]** E a cooperatividade, que é uma palavra que vai aparecer muito, co-op e tal, se sua estudar assim, que aí é habilidade de passar a vez. Ou seja, o await torna o meu código cooperativo. Então eu falo, olha, vou bloquear aqui agora.

**[00:33:15]** E aí o loop escalona. Então é uma junção das duas coisas. O loop tem que ter a capacidade de escalonar entre tarefas, só que as tarefas têm que dar a opção do loop. Elas têm que cooperar com o loop para ele poder fazer o escalonamento. Então basicamente essa é a resposta que a gente está procurando aqui. Então a gente precisa fazer com que a nossa aplicação coopere com o UV loop.

**[00:33:42]** e, por consequência, é cooperar com o UV-Corner. Ou seja, se o nosso código tiver essas palavrinhas, assim que, em todo o endpoint e ao 8, em toda a trava, o loop de eventos ou servidor da nossa aplicação, que é o UV-loop, já resolve a situação. Ou seja, lembra daquela brincadeira que a gente estava vendo aqui atrás?

**[00:34:11]** você não precisa ter várias cópias você precisa ter uma só e aí você vai recebendo vários clientes porque você fala olha tô na trava aí o que que o que que a aplicação faz pega a próxima do backlog começa a trabalhar então ela vai responder de forma cooperativa toda vez que ela tiver uma trava

**[00:34:34]** Por conta disso, o loop do UVCorn vai passando para a gente as coisas e essas coisas vão acontecendo de forma concorrente. Ou seja, como se fosse ao mesmo tempo. Lembra? Não é ao mesmo tempo. Ele lê até encontrar a trava e aí ele escalona. Então tudo o que a gente precisa fazer é escrever um código cooperativo. Porque se a gente escreveu um código cooperativo, o escalonamento já é dado pelo servidor da aplicação.

**[00:35:03]** Fez sentido isso aqui? Essa coisa maluca que eu falei? Eu sei que são muitos termos e tudo mais. Eu sei, eu tenho noção disso. Mas a ideia é tipo assim, não é entender minúcias da coisa, mas entender o que está acontecendo em alto nível para a gente poder escrever o código. Fez sentido? Me contem aí. Mano, se você tiver a pergunta, agora é a hora da pergunta. Pô, mas e aí o negócio do bloqueante? Se você estiver vendo offline depois deixa o comentário aqui.

**[00:35:35]** Então, lembrando, a gente não faz escalonamento. É isso que precisa ficar claro. Não fazemos escalonamento, escreveu um código que pode cooperar com o escalonamento. Massa? Então, a gente vai começar pelo banco de dados, porque o banco de dados é em si a grande questão desse loop. Mas nem só ele, né? Porque lembra que a gente também está recebendo inputs do Yuvicon? Então, a gente tem que conseguir receber inputs

**[00:36:06]** e jogar Outputs para o banco e ao mesmo tempo a gente tem que fazer isso aqui, então a gente vai virar num loop cooperativa, que é muito maluco dentro da aplicação. Então, vamos lá. Para o banco de dados funcionar, a gente precisa falar para o SQL Alchemy que ele vai trabalhar com a 5IO. A primeira função que chegar num await vai ter prioridade ou ela vai ter que esperar até o loop terminar as outras. Não, então, o loop...

**[00:36:39]** Ele vai iterando, né? Imagina uma fila, literalmente, uma fila. Saca, você chega no supermercado e aí vai ficando uma pessoa atrás da outra. É como se a pessoa, a pessoa que está lá, caixa de supermercado, tivesse passando a compra de uma pessoa de cada vez. Se você é o último da fila, você vai ter que esperar os awaits de todo mundo que já estava na frente. Mas a sua vez chega.

**[00:37:10]** e se a sua responder primeiro quando ele quando ele passar já chegou já chegou já chegou já chegou e a sua já chegou a sua sai primeiro não existe uma relação do primeiro que chega o primeiro que sai é tipo assim eu atendo o primeiro eu atendo o primeiro que chega e retorno o primeiro que eu tiver a resposta do bloqueio

**[00:37:35]** Não existe uma questão da fila, assim, se eu receber 10, eu vou olhar o primeiro, olhar o segundo, olhar o terceiro, até encontrar o await de todo mundo. Mas a gente vai fazer de forma cooperativa, todo mundo, e depois a gente vai passando ali e terminando as operações. A gente não faz múltiplas operações de uma vez, mas a gente faz um pedaço de cada.

**[00:37:58]** O que dá a impressão de que a gente está processando muita coisa. Mas a gente faz um pedaço de cada, enquanto a gente está bloqueado, enquanto aquela requisição, aquele pedaço está bloqueado. Então estou esperando o banco ou processo o outro. Aí começa a esperar o banco desse e a gente vai trocando isso aí. Essa é a arte do escalonamento. Aí tem uma pergunta aqui do Saigui que é o seguinte. Calma, eu não preciso mais explicitar os workers.

**[00:38:30]** Se meu código estiver preparado para o UVcon, para isso o UVcon resolve. Então, o UVcon, você pode rodar três workers, por exemplo, e ser concorrente na aplicação. Lembra que eu falei, a aplicação é bloqueante, mas o server não? O server e a aplicação são coisas diferentes. Eu posso ter, vamos voltar aqui nos slides, pera aí.

**[00:38:59]** eu posso ter três cópias e todas as cópias serem não bloqueantes o que significa, por exemplo, vamos supor que eu tenho seis cópias e eu tenho dez requisições cada uma vai lidar com três e uma com quatro, né? é tipo tudo junto ao mesmo tempo saca? pode ser concorrente e paralelo ao mesmo tempo

**[00:39:30]** Faz sentido isso? Você pode ser acíncrono e trabalhar com workers. Nada impede uma coisa da outra. O ideal é que as duas coisas andem juntas, né? Hugo, muito obrigado, mano. Valeu demais, velho, ó. Beijão pra você, velho. Isso me ajuda muito, mano. Aí... Aí, o Everton fez uma pergunta aqui que ele falou. Não existe concorrência, então. Existe. Escalonamento é concorrência.

**[00:40:03]** Eu recebi várias coisas e vou processar uma de cada vez, mas intercalando entre elas. Isso é concorrência. O que você está perguntando é sobre paralelismo. E paralelismo é resolver duas de uma vez. E aí, como a gente obtém paralelismo? A gente obtém paralelismo assim. Então, aqui estou rodando a aplicação três vezes. Saca? Então, eu posso responder...

**[00:40:31]** Eu estou trabalhando em três ao mesmo tempo. Mas só que esse três eu posso estar escalonando e cooperando 50, mas estou processando três ao mesmo tempo. Então, ao mesmo tempo, é paralelo. Concorrencia é esse negócio de um tequinho de cada, vai escalonando. Faz sentido? Deu para entender?

**[00:41:00]** Ah, o resto de perguntas. Ele usa o Psycopg3, a gente vai usar o Psycopg3, mas só lá na aula do Psycop. A gente não tá aqui ainda. Massa, deu pra sacar tudo aqui? Legal? Pode me dar perguntas, eu tô aqui pra isso. Esse é o objetivo. Se não fosse pra responder as coisas, não fazia live, né?

**[00:41:25]** Então, vamos lá. Como é que a gente faz o banco de dados não ser bloqueante, né? Então, o SQL Alchemy, né? A partir da versão 1.4, então, a 1.4, a 2.0, 2.0, qualquer coisa, todas elas já vem com a Sync Ion embutido. Elas já suporta a Sync. Por padrão. Obviamente, a gente vai dar uma mexida no código para tornar ele cooperativo, mas por padrão, o SQL Alchemy já suporta a Sync.

**[00:41:55]** Uma coisa que tem que acontecer aqui é o seguinte. O SQL Alchemy usa para fazer concorrência uma biblioteca chamada Greenlight, que é essa biblioteca aqui. Green é de pequenas threads, né? A gente chama threadsinhas, threads só de interpretador e não de sistema operacional, de threads verdes, ou seja, green threads. E aí, quem cria essas green threads é o Greenlight.

**[00:42:34]** E aí, o Skelial que me usa essa biblioteca Greenlight por baixo dos panos. Isso é importante ficar explícito. Algumas plataformas, e aí o exemplo aqui é o Apple Silicon, né? Silicon é o ARM da Apple, lá, o M1, M2, M3. Algumas variações de sistemas operacionais malucas não têm scripts pré-compilados do Greenlight. Então há...

**[00:43:04]** A boa coisa é tipo assim, estalho, suporte, explícito, assim caiu. Ele já tá instalado na nossa aplicação. Se você vier procurar no Lock aqui, né? Você vai ver que o Greenlight já tá aqui. Opa, eu quero o Pi Pro de Lock aqui. Você vai ver que o Greenlight já tá instalado aqui. Mas se você tiver uma plataforma dessa maluca, tipo Apple Silicon ou sei lá...

**[00:43:27]** um rodando num... Risk 5, por exemplo? Talvez não tenha, aí você tem que compilar esse pacote. E a forma de deixar isso explícito é instalar o assim que eu. Massa? Então, deixa assim. Uma coisa, agora eu preciso falar uma coisa aqui que é o seguinte. Para quem estiver vendo essa aula no futuro? No futuro quando? Não sei. Quando o SQL Alchemy 2.1 sair,

**[00:44:00]** que ainda está em desenvolvimento, o Greenlight não vai vir mais por padrão, então sempre terá que ser explícito a instalação do assim que aí ou para que seja sincrono. Massa, só queria deixar isso aqui, porque no futuro pode ser que alguém esteja vendo isso aqui. Alguma relação de cores disponível no servidor? Não, não necessariamente. Porque imagina o seguinte, o seu computador está rodando quantas threads agora?

**[00:44:28]** Saca, tipo assim, sei lá, milhares, né? Só o seu navegador deve ter, sei lá, umas 200 threads abertas, você tem 200 núcleos. Então, o computador, o funcionamento do computador é dessa forma. Você tem 8 núcleos, mas você tem 8 milhões de threads rolando no seu sistema. Então, ele... o...

**[00:44:55]** O seu sistema, tipo assim, o seu hardware tem 8 núcleos e ele roda, sei lá, vamos supercar hyper thread, então ele roda 16 threads. Porém, com tudo entretanto, todavia, você tá rodando.

**[00:45:10]** milhões de processos então o sistema operacional o uso do computador é um exemplo disso ele é concorrente porque tem que executar dois mil processos rodando agora na sua máquina só que ele é paralelo porque ele tem oito núcleos funcionando ao mesmo tempo faz sentido essa analogia então é concorrente e paralelo ao mesmo tempo atenção galera de dois mil e vinte e sete não sei se vai demorar tanto assim para sair dois um mês atenção galera do futuro

**[00:45:38]** Então, legal. Só que aí a gente está usando o SQ Lite, né, como banco de dados. E o SQ Lite, a biblioteca padrão do Python, ela não lida bem com concorrência. Ela não funciona sincronamente. Então a gente vai instalar essa bibliotequinha aqui chamada AIO-SQ Lite. Sempre que você vê uma biblioteca que começa com essas três letras AIO, significa Asynchronous Input Output.

**[00:46:08]** Massa, então quer dizer que é a versão assíncrona de uma biblioteca que a gente já conhece. Então a gente vai instalar o IOSKLIGHT para falar que a gente vai se comunicar com esse banco de dados que a gente está usando em memória lá para brincar de forma assíncrona. Então a gente vai instalar isso aqui, então. Poetry, Edge, IOSKLIGHT. Massa, Simplon, instalando o suporte assíncrono para o banco, para o R&M, lá no...

**[00:46:41]** Lá no nosso ponto ENV, para falar que a gente vai usar a conexão acíncrona, é só a gente adicionar esse mais IO SQLite da nossa UI. Então, vamos lá no nosso ponto ENV. Aí é aqui onde a gente tinha isso aqui, né? Total, total, total, total. A gente botou mais IO SQLite. Agora, a nossa aplicação está usando o banco acíncrono. A nossa aplicação não é acíncrona, mas o banco já é acíncrono.

**[00:47:13]** E aí, como é que a gente faz isso aqui, né? Como é que a gente torna esse processamento essa coisa toda a síncron aqui dentro? Bom, aonde a gente cria a engine, né? Então, vamos no nosso código agora. Lá a gente tem o nosso arquivo chamado database.py. Tá vendo que aqui a gente tem esse create engine? Então, a gente não vai usar ele. Nem o session do RM aqui. Vamos deletar isso aqui. A gente vai...

**[00:47:43]** Na extensão do SQL Alchemy, então from sqlalchemy.xt de extension, na extensão do async.io, a gente vai importar o createAsyncEngine. Ou seja, crie uma conexão com o banco de dados de forma assincrona. Massa? E a partir dessa conexão, a gente vai criar uma sessão assincrona.

**[00:48:14]** Então, async session. Deixa eu colocar aqui de um jeito que dê pra vocês lerem o código. Mas é basicamente isso, então a gente vai usar esse async session. Legal. Só que pra isso aqui suportar corrotinas, a gente vai ter que falar o seguinte, async def. Massa, ou seja, pedir a sessão agora é uma corrotina, não é mais uma forma

**[00:48:51]** Saca, a gente não está mais pegando a função executando. A gente vai tornar isso aqui bloqueante. Tornar isso aqui não bloqueante. Ou seja, isso aqui agora é uma corrotina. E aí, para o bloco WIF funcionar acincronamente, a gente usa acinc-wif. Pronto. Agora, toda a nossa conexão com o banco de dados vai acontecer de forma acíncrona. Tanto pedir a sessão vai ser acíncrono, quanto...

**[00:49:18]** A sessão vai ter suporte a SYNC. Ou seja, dentro disso agora tudo começa a ficar mais maluco agora. Tudo é a SYNC. Ou seja, se isso aqui é uma corrotina, quando eu for tentar executar isso aqui, isso já dá margem para o escalonamento lá na frente. Olha que massa! Então com poucas coisas a gente já consegue ir escalonando aqui. Massa! Uma boa prática que a gente tem aqui é o seguinte, que é esse Xpy On Comet.

**[00:49:51]** Geralmente, quando a gente comita o código, quando a gente dá o session.comite aqui, ele tem a opção de fechar a sessão ou não. Só que como a gente está usando a síncrono, eu não sei se já fechou a sessão, já passou, não sei onde tava, de onde vem para onde vai, então...

**[00:50:15]** A boa prática é dizer para a sessão nunca terminar. Ela termina quando acabar o bloco de Sink Session, mas ela não expira quando dar o Comet. Massa? Legal isso aqui? Peraí que eu vou tossir de novo. Legal. Aí o Tenebu mandou aqui. E não precisa trocar o Await no lugar do Weald? Não. Aqui a gente está retornando isso aqui para lá, não é Await. Aqui não tem espera.

**[00:50:59]** Saca, a gente vai, tá passando isso aqui, delegando pra frente. Legal? O Yago falou, não sei se já foi abordado, mas o que acontece internamente quando a gente chama Get Session sem Awade? Bom, a gente viu que dá erro de chamada de Awade lá atrás, né? Ele dá um pouquinho de coisa. Legal? Massa? Então essa é a coisa pra gente suportar o assim que aíou aqui.

**[00:51:31]** Beleza, que mais que a gente precisa instalar para isso aqui funcionar? Bom, como a gente vai rodar as coisas de várias formas aqui, e o teste também precisa suportar assim que a eu, a gente vai instalar o PiTest assim que a eu. Ou seja, o suporte do PiTest para ele trabalhar com assim que a eu. Ou seja, para poder ter assim que def de teste, para poder ter assim que def de fixture, tudo mais, a gente usa essa extensão que é o PiTest assim que a eu. Massa?

**[00:52:03]** É só isso, né? O PyTest não tem uma forma tradicional para lidar com isso aqui. Uma coisa que a gente precisa fazer aqui, lá na configuração do PyTest, é falar que a gente vai usar as fixtures, vão estar no escopo de function. E aí, como eu sei que trabalhar com escopos vai ser uma coisa mais complicada, que a gente vai ter que debater, porque eu não sei o quê? Para a gente não precisar entender isso aqui,

**[00:52:32]** Para não cair mais um assunto, porque hoje a gente está nesse loop de assim caiu aqui, a gente vai discutir o que significa o escopo das fixtures lá na Ola11. Massa? Combinado? Então, por agora, a gente só vai colocar essa opção aqui no Pi Project, lá na parte do PiTest.

**[00:52:59]** A gente só tá falando, toda vez que a gente usar uma fixture do assim que aí, ó, o escopo dela é função. Uma fixture normal que a gente usa. Sempre que ela rodar, ela é uma função. Mas, ok, é simples assim. Ela não dura por mais tempo do que a execução da função que tem aquela coisa. Só pra gente não se aprofundar muito nisso, a gente vai conversar mais sobre escopos na aula 11. Legal? Aí, o que a gente tem que fazer aqui, né?

**[00:53:29]** Para a gente falar que a fixture é a sincrona, porque agora a nossa conexão com o banco de dados é a sincrona, a gente vai ter que mudar a nossa sessão do banco de dados. E isso aqui está lá nas fixtures que a gente tem que estão lá no conf-test. Lembra, a gente tem uma fixture que pega o banco de dados aqui. Então a gente precisa mudar ela com todos aqueles esquemas. Precisa ser a sync-def, aqui precisa ser create-async-engine.

**[00:54:00]** Aqui precisa ser Async Session. É a mesma coisa que a gente fez lá atrás, né? Legal? Async Session. Aí aqui precisa ser Async Reef. E aqui ficou Engine Engine, né? Espera aí. Async Engine. Só que o Piedest, por padrão, ele não suporta Fixture Asynchronas, né? Então a gente vai ter que usar aquela extensão que a gente acabou de instalar, né? Então vou me importar aqui.

**[00:54:32]** Deixa eu tirar os imports que a gente não está mais usando, esse CreateEngine está aqui, e esse Session do RM que a gente também não está mais usando. E aí, aqui do PiTest, a gente vai fazer o seguinte, ImportPiTest, assim que eu. E aí, em vez de uma fixture tradicional, que é essa que a gente usa, a gente vai trocar isso aqui por ArrobaPiTest assim que eu, ponto Fixture. Ou seja, dizer que isso aqui é uma fixture.

**[00:55:01]** e ela é a sincrona, porque ela executa código a sincrona dentro dela, cria uma engenha sincrona, faz todo esse processo aqui dentro todo de forma a sincrona. Aí, tem uma grande coisa aqui que é o seguinte, eu vou copiar esse código aqui e eu vou explicar para vocês o que ele faz aqui. Vai ser mais simples do que eu explicar no slide.

**[00:55:30]** Então legal, o que acontece aqui? Toda vez que a gente roda a criação do banco de dados, a criação das tabelas, você concorda comigo que a tabela não pode ser criada de forma sincrona? Você concorda comigo? Imagina o seguinte, que eu vou criar uma tabela e... Cria tabela nas ordens erradas ou várias coisas criam a tabela no banco ao mesmo tempo, de forma concorrente. Você concorda comigo que isso é um problema?

**[00:56:05]** aqui dentro. Então a gente começa a Engine e fala pra ele olha, begin de começo e pra rodar isso aqui, você quer que cria os metadados, cria as tabelas de forma sincrona. Então a gente só faz isso aqui pra rodar sincronamente. Você não quer rodar as coisas de forma a sincrona. Aí você fala pra ele olha, Run Sync. Cria a tabela de forma sincrona. Não faz sentido criar as tabelas de forma a sincrona.

**[00:56:37]** Faz sentido isso aqui? E aí, aqui a gente tem esse pedacinho aqui do Async Session, que foi o que a gente discutiu ali pra trás. Uma coisa que faltou eu colocar aqui foi a URL correta, né? Porque agora a gente tá trabalhando com isso assíngono, né? Em memória. E basicamente, a partir de agora, a gente pode usar essa session de forma assíngono. E tá tudo funcionando aqui. Legal?

**[00:57:08]** Aí aqui tem um negócio que herdava Session, aqui a gente vai ter que trocar para a Sync Session, só para ficar certinho, ele já deu alguns erros aqui, mas tudo bem, a gente vai cada coisinha no seu tempo, é só para eu poder fechar esse arquivo sem nenhum erro de importos. Então, agora a gente transformou a connicação que a gente tem no banco em a sincrona. Aí a gente criou as tabelas de forma sincrona, porque é necessário.

**[00:57:39]** E aí, agora a gente vai mexer no nosso próprio teste, né? A gente tem um teste aqui, que é o teste do banco de dados, lembra que a gente fez aqui? E esse teste ele é completamente sincrono, né? Só que lembra que a sessão, ela não é mais sincrona. A sessão agora é assim que? Só pra ficar claro aqui. Lembra que isso aqui é assíncrono. Então o que que a gente vai precisar mudar isso aqui?

**[00:58:09]** Para executar o código que funciona cooperativamente, a gente vai ter que trocar isso aqui para AsyncDefinant, como sempre. E aí, o PiTest não tem suporte a coisas acíncronas por padrão, né? E como é que a gente vai resolver isso aqui? Só para deixar anotado o tipo certinho, eu vou deixar aqui. Então, o PiTest não consegue executar testes acíncronos. Então, a gente tem que falar para ele, olha, importo o PiTest aqui em cima. Vamos lá, aqui.

**[00:58:41]** import pyTest e a gente fala para o pyTest que esse teste, então pyTest.mark, a gente está marcando esse teste como a sincronona. Então a gente fala pyTestmark, assim caiu. Massa? Aí estou explicando para o pyTest falando, olha, esse teste aqui em específico, ele roda de forma a sincronona. Aí lembra, olha aqui a operação com o banco de dados. A gente não está dando um commit aqui?

**[00:59:14]** Então, quando a gente faz commit, a gente tá transacionando com o banco de dados. Então, eu preciso falar pra ele, olha, pode escalonar aqui, porque aqui é um momento de espera. E aí, a session também, a wait aqui, porque a gente vai fazer uma busca no banco de dados. E essa busca, ela também é a síncrona. Fez sentido o que a gente fez nesse código aqui? Lembra, a gente não controla o event loop.

**[01:00:02]** a gente só está dizendo olha o nosso código precisa ser cooperativo então como a nossa sessão é a síncrona eu preciso olha isso aqui vai demorar isso aqui vai demorar vai fazer outras coisas enquanto a gente está fazendo isso aqui aí o o ruzi o ruzi fez uma pergunta interessante que ele falou porque que o ed não é a síncrona

**[01:00:30]** E por que não coloca no Edge? Porque o Edge, ele adiciona, lembra da aula do SQL Alchemy que a gente teve atrás? O Edge adiciona na sessão. Quando a gente usa o Comet, é que a gente faz a transação. Lembra daquele esquema do Unity of Work, que a gente pegava tudo, colocava em memória. E só quando a gente dá o Comet, é que a gente transaciona com o banco de dados. Então o Edge está adicionando em memória, na sessão. Ele não está fazendo I.O.

**[01:01:02]** Ele está colocando dentro da memória da própria aplicação. Está na Session. Fez sentido aqui. Então, a gente só vai colocar o Await nas operações que efetivamente existem a Ion. Nas operações que existem a Ion. Então, comite, transacciona com banco de dados. E o Scalar também transacciona com banco de dados. E aí a gente deixa.

**[01:01:31]** Aí o Lisandro fez uma pergunta interessante aqui. Por que esse wif não é a sync? Porque esse wif é um código que a gente fez. Esse mockdbtime aqui é um código sincrono, que a gente mesmo fez aqui. Que retorna essa função aqui. E essa função, ela é sincrona. Então, a gente só usa a syncwif quando o gerenciador de contexto é a sincrona.

**[01:02:05]** Nesse caso não é. É síncrono, é normal. Porque a gente fez isso ser síncrono. Ah, poderia ser assim? Poderia até, mas não tem necessidade. Massa? Agora, vamos fazer o seguinte? Vamos rodar esse teste pra gente ver o que que rola? Pra ver se tudo funciona da forma como a gente esperava que funcionaria. Ah, beleza. Ele falou que a nossa linha tá muito longa aqui. Bateu no limite, né? Então eu vou quebrar essa linha aqui.

**[01:02:43]** e vou rodar o teste de novo. Aí ele reclamou dar ordem... Ah, lembra que a gente tinha feito aquele import só para ficar fácil de ler? Então eu vou dar um task-format aqui. E agora eu vou dar um task-test e vou pedir para ele rodar só o teste do banco de dados. Aí olha que interessante, o PaiTest está falando aqui ó, tem o plugin do NIO, né? Então NIO, qualquer forma de IO, e tem o plugin do assim que IO.

**[01:03:13]** Ele está falando que está rodando uma street com aquele esquema de function que a gente já colocado e passou o teste. Vamos rodar esse teste e esquecer um await aqui? Só para ver o que que acontece. Ele deu erro. Olha o erro que deu aqui. Runtime warning corrotim, assim que secha um Scala, que é o que a gente executou aqui.

**[01:03:42]** Ou seja, acabou o código, aquilo nunca foi escalonado, não foi esperado e por não ter sido esperado, a gente não conhece o resultado e ele deu erro. Massa? Então, é esse erro a gente vai ter que lidar com ele várias vezes aqui, toda vez que a gente olhar o código e tiver que esperar e não esperar alguma coisa que deveria ser esperado.

**[01:04:07]** Massa, aí se a gente rodar agora de novo, beleza, passou, a gente implementou o async no teste, na fixture, no banco de dados. Fez sentido isso? Massa, você viu que eu não tenho que controlar loop nenhum, ficar pensando em como essa coisa vai ser executada? O Python resolve isso. A gente só precisa...

**[01:04:36]** Escrever o código de forma cooperativa. O resto, o framework que o pai teste assim que a IOU resolve, o FES-API vai resolver, o Yuvicorn vai resolver. Tudo que a gente precisa é só falar a hora. Aqui tem a IOU, aqui tem a IOU, aqui tem a IOU. E marcar isso. Massa, uma coisa que eu quero fazer com vocês agora é refatorar toda a nossa aplicação para usar a 5iô. Sim!

**[01:05:03]** A gente vai mudar toda a nossa aplicação para usar ela assim que aí. Só que lembra que a gente tem uma cobertura de teste sensacional? Então a gente não tem que se preocupar com isso. Por quê? Simplesmente porque os testes vão mostrar para a gente aonde a gente está errando. E essa é a técnica de refatoração que eu vou usar aqui com vocês. No outro a gente foi entendendo conceitos, aqui literalmente a gente vai rodar o teste e ver o que acontece. Aí uma coisa que eu queria dar o recurso para vocês aqui é o seguinte.

**[01:05:35]** "-k", no pai teste, então, pai teste "-k", você escreve qualquer groselha e tudo que demete nessa keyword, por isso, k, de palavra-chave, a gente vai escrever isso aqui, então, "-k", qualquer coisa, a gente roda o teste e vê o que acontece. Legal? Então, essa é uma técnica de refatoração que eu vou usar aqui pra vocês. Se a gente rodar aqui, vai ver que falhou, aí ele falou o seguinte, olha, create user, olha o erro que ele deu.

**[01:06:06]** Create User, Atribute Error, Corroutim, Objects, No Hazel, Atribute User Name, Runtime, Warning, assim que Session Scalar, World was Never Awaited. Ou seja, não funcionou porque a gente colocou a sessão a síncrona, mas nada está esperando que isso funcione de forma a síncrona. Então, puta, eu estou na frente, é que eu vou me tirar da frente. Que é o seguinte, para a gente listar todos os testes que tem no nosso projeto,

**[01:06:33]** O PyTest tem uma flag chamada CollectOnly. E aí a gente vai chamar essa flag CollectOnly, chamar todos os testes, e ver todos os testes que a gente tem. E a gente vai refatorando um por um aqui. A gente vai rodando o teste e vendo o que acontece. Refatoração simples, né? Então, ó, o que a gente tem aqui?

**[01:06:56]** Quando a gente roda o Collect Only, ele vai dar várias respostas pra gente. Aí ele fala, olha, tem o pacote Testes, tem o pacote Alf, tem o pacote TestDB, tem o Test Security, tem o Test User, e a gente tem vários testes pra várias coisas aqui. Se vocês estão fazendo os exercícios, obviamente vocês têm muito mais testes do que eu. E era esse o objetivo mesmo. Então, eu vou começar pelo Alf. Massa? Pera aí. Então, eu vou começar pelo Alf.

**[01:07:34]** que é o que está menos medonho aqui. Porque a gente só tem um... uma coisa aqui, né? Vamos começar por ele aqui, vai? Então, no Alph, né? O que que a gente tem aqui? O único teste que a gente tem é esse teste GetToken, né? Que chama o Tolkien. Se a gente rodar esse teste, a gente vai ver que vários problemas vão começar a aparecer aqui. E é o primeiro. Obrigado aí, porque me desejou saúde. Teste GetToken. Ó, ele falou aqui...

**[01:08:04]** com o routine nunca foi aguardada, né? Então aí você vai ver que lá no router tal rolou umas coisinhas, então vamos tentar entender esse teste primeiro, então a gente vai começar pelo teste. Então a gente está no teste off e o teste que a gente pegou para olhar foi esse aqui, né? Test getToken, a gente rodou esse comando. Aí olha que interessante, o que que esse teste faz? Ele pega, né? Ele recebe o client e ele recebe o user.

**[01:08:35]** Massa, vamos lá nessa fixture de cliente e ver o que está acontecendo. Bom, ela pega o Fast API e tal, muda, troca a sessão por uma sessão acíncronana. Beleza, então aqui já tem um ponto. E aí a outra coisa que ele usa é a fixture de user, né? E essa fixture de user, ela recebe session e session virou acíncronana. Então o que que a gente vai ter que fazer aqui?

**[01:09:08]** transformar todas essas operações que a gente faz com o banco em as sincronas, né? Então aqui, ó, o commit, await, session, commit, refresh, também chama com banco de dados, await, legal. Só que lembrando, essa fixture, ela é sincrona, né? Como é que a gente vai chamar uma coisa sincrona dentro de um código? Então, a sync. E aí, por ela ser a sincrona, ela não pode mais ser uma fixture aqui, então ela tem que ser uma fixture do...

**[01:09:39]** Pai teste assim caiu, né? Ponto fixture. Agora, em teoria, deve dar um outro erro, né? Vamos pensar aqui. Vamos rodar e ver o que acontece agora. Legal. Aí ela rodou aqui e ela deu um erro lá dentro da nossa aplicação agora, no post. Quando ele chamou o Tolkien aqui, ele falou o seguinte, olha...

**[01:10:11]** com o Routine, object, noResultButtePassword. Aonde está esse código? Saca, assim que secha um ScalarNeverWaited. Então, você está vendo que aqui ele tem um Scalar aqui? E esse Scalar precisa ser aguardado? Então, vamos lá no nosso arquivo agora, e vamos brincar com ele aqui. Ele está no Howters de Alf, porque a gente refatorou a aplicação. E aí, aqui...

**[01:10:45]** O Session Scalar aqui precisa ser aguardado, né? Só que aí tem toda aquela história, né? Então isso aqui precisa ser awaitable, né? Precisa ser aguardado. Só que aí você tá vendo que a nossa Session aqui, ela é mentirosa, né? Porque ele fala aqui pra gente que... Pera aí. Ele fala aqui pra gente que a nossa sessão que a gente vai receber é uma sessão do R&M.

**[01:11:11]** E a gente não recebe mais essa sessão do RM. Então a gente vai ter que mudar isso aqui. Isso aqui é a sync session. A sync session. Então a gente não recebe mais session. Isso aqui é uma sessão acíncrona. Legal. Só que aí a gente está no código aqui e a gente deu esse await. Só que como é que a gente vai dar esse await numa função que é acíncrona?

**[01:11:42]** Então legal, a gente precisa escalonar, só que pra escalonar precisa ser uma corrotina. Legal. Assim que def. Show! Vamos rodar o teste de novo agora e ver o que que acontece? Oh! Maravilhoso. Não? Não é lindo? Não é lindo demais, só que... É sensacional. Desculpa, eu me empalgo, eu adoro assim que eu... Marcos, obrigado mano. Pela coquinha com coxinha.

**[01:12:16]** Valeu, mano. O frango eu vou passar, mas a coxinha com a carinha de jaca assim... Legal. Funciona. Incrível. Eu roubei várias cenas aqui, né? Porque eu tenho slide pra isso, eu tenho slide pro A8, eu tenho slide pra testar de novo, eu tenho slide da Fisher, eu tenho slide do Anotated, eu tenho tudo aqui, né? Eu fui fazendo tudo. Só... Só o quê?

**[01:12:50]** Robane, todos os slides. Bom, agora vamos para o... Alf... A gente terminou o Alf. Vamos para o... Users agora? Então, deixa eu tirar isso aqui. A gente vai lá para o Users. Aí a gente tem aqui o Users. E a gente tem os testes do Users. Legal, quais são os testes do User? Collect Only. Vamos ver tudo que é do User. Então, aqui no...

**[01:13:25]** Cadê Users? A gente tem isso aqui. Create User, Read User, Update User, Delete User, Update Integrity Error. Mas então vamos um por um aqui, né? Então teste Create User. Lembrando, uma coisa que a gente já tá aqui no Users, lembra que isso aqui, o tipo não é mais Session, né? É Assink Session, né? Então já vamos arrumar isso aqui. Aí ele importou aqui em cima, né? O Assink Session.

**[01:13:56]** E aí eu vou remover essa chamada do ORM aqui, pra tipagem ficar correta. Bom, a gente pode usar o teste pra fazer isso aqui, a gente vai ver que o teste vai dar o resultado que a gente precisa, né? Então, o que a gente quer aqui? A gente quer o teste create user. Legal, deu erro, deu um erro muito maluco. Aqui, ó, o teste DB passou, mas o teste create user do banco falhou, né? Então, vamos lá olhar o que que é. Ó, quando ele foi chamar create user,

**[01:14:29]** ele tentou chamar aqui o DB user session scholar ou seja, de novo, aquele problema. Então, a gente está aqui no create user, que é o teste que a gente acabou de pegar para brincar, vamos lá. É o create user. A gente não consegue criar isso aqui porque isso aqui precisa de await. Precisa ser aguardado, beleza. Só que, para ser aguardado, precisa ser uma corrotina. Legal. Vamos rodar de novo?

**[01:15:01]** Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

**[01:15:38]** Vamos para o próximo, vamos pegar o Collect Only, ver o que mais no User precisa ser arrumado aqui, então a gente tem o Read Users, vamos rodar ele, então Task Test, Minus K, Test Read Users, bom beleza, Scalers Never Waited, ou seja, de novo a mesma coisa, então aqui no Get a gente está pegando isso aqui, mas isso nunca é usado, então vamos lá, Await, só que aqui a gente tem um problema.

**[01:16:14]** Porque isso não é uma corrotina. Cansaram de ouvir nem a palavra corrotina hoje. Vamos rodar os testes? Deu um erro maluco aqui, hein? Async session scalar was never awaited. Peraí, lê essa mensagem de erro comigo. Async session ponto scalar was never awaited. Aqui a gente não está usando scalar. A gente está usando escalars no plural.

**[01:16:56]** Então de onde vem esse escala que ele está reclamando aqui? Você está vendo que eu não consigo ver muito bem aqui, né? Ele só está falando que deu erro, não dá para entender muito bem aonde que aconteceu e tudo mais. O erro está aqui, ó, no current user. Lembra que a gente definiu o current user? Só que o current user que a gente tem, ele usa essa função, né? Lá do que a gente definiu no security, get current user.

**[01:17:27]** E aí o que que acontece? GetCurrentUser usa Session. Só que esse tipo aqui é a SyncSession, né? A SyncSession. E para isso aqui se é a SyncSession, vamos lá. Então a gente muda aqui, né? XT, a SyncSession, ok. Aqui veio a Sync... Ah, faltou a SyncIO aqui, né? Ponto, a SyncIO. A gente vai ter que pegar isso aqui. E como isso aqui agora...

**[01:18:00]** É a Sync Session? Pra ele poder ser assim que de novo tem que ser uma corrotina, assim que deve. Legal? Aí a gente sabe que ó o escala de onde ele tá aqui. Aqui faltou o Await. Aí estourou de novo o tamanho da linha. Hmm, interessante. Ele só tinha dado um warning aqui pra gente, né? O teste passou em si, né? Vamos rodar? Legal. Sem warning agora.

**[01:18:29]** Está tudo funcionando. Isso, esse erro iria se repetir para todos, né? Para todos os testes do user, né? O create user, o read user. Agora a gente tem o update user. Vamos pegar o update agora e ver o que acontece. Então, dash update users. Não pegou nenhum teste, é porque update user no singular, né? Legal. Olha o que aconteceu. Várias coisas. Tem que corrigir o session. Aonde tem que corrigir o session?

**[01:19:17]** só para eu saber porque eu não sei de onde vocês estão tirando esse que eu tenho que corrigir aqui porque a gente corrigiu todos aqui então a gente tem o update user e update user ele deu aqui ó assim que refresh was never awaited vamos lá de novo agora no users a gente está agora no update e no update a gente tem aqui duas chamadas né o comment await e o session refresh

**[01:19:53]** Update também, mais lembrando, pra ser awaitable, pra poder esperar tem que ser uma corrotina. Vamos lá de novo agora, Update User. Beleza, passou mais um. Lindo, lindo, lindo, lindo, lindo. Vamos pegar e agora fazer esse esquema de novo. Collect Only, a gente foi no Update User, a gente tem o Delete User.

**[01:20:17]** Então vamos lá. Task, Test, Minus K, Delete User Qual que é o problema do Delete User? Comite was never awaited. Mesma coisa. Não é tão difícil fazer esse effecto, né? O difícil é entender o que essas coisas significam, né? Async, Await, Await. Massa, rodou o delete. Ah! De novo, lindo, maravilhoso, ó. E aí, o último que faltou aqui, né? Do nosso Collect.

**[01:20:54]** Aqui nessa brincadeira foi o Update Integrity Error, mas ele deve funcionar, porque a gente já atualizou o Integrity Error, né? Legal, passando. Pô, super rápido, super simples de ir fazendo aqui, né? Então, aqui tinha o endpoint Get, o de Put, o Delete. E agora vamos rodar o Task Test e ver tudo que tá rolando. Vamos ver se a gente esqueceu de alguma coisa? Task Test. Lindo!

**[01:21:31]** Temos uma aplicação assim, que não é? E tudo que a gente precisou fazer foi definir a sync e definir a weight. Toda vez que a gente tinha uma espera, não é tão complicado de deixar a aplicação assim, não? Afinal, refatorado está. Lindo. Agora, a partir disso, de uma forma bem simples, a gente conseguiu fazer com que a nossa aplicação fosse concorrente. Só colocamos a 5 weight.

**[01:22:05]** Não fizemos nada demais, porque lembrando, né? Ah, mas por que que foi tão simples de fazer isso? Beleza, a gente teve que mudar algumas coisas, em como a session era definida, ai ou light, eu não sei o que, mas beleza, depois a gente veio botando assim que a waiting tudo. Porque, de novo, quem executa o loop, é o loop. Saca, não tenho que me preocupar com isso. Funciona de uma forma bem simples. Aí o Takoni deixa um comentário que é muito legal.

**[01:22:37]** Cara, testes salvam muito, sim, é por isso que a gente escreveu o teste, a gente repartora de uma forma muito simples. Agora a aplicação está mil vezes mais rápida, sim. Eu fiz caquinha e coloquei o away no client get dos testes. Não, porque a requisição é sincrona, né? Lembra, o cliente é sempre sincrono. Quem precisa ser sincrono é a aplicação. E quando a gente usa o cliente, cliente.get, cliente.post, o cliente é sincrono.

**[01:23:07]** Lembra? Quem requisita nossa aplicação não está preocupado em como vai acontecer ele. Ele está mandando uma requisição e quer a resposta. A requisição bate no loop. E o loop resolve todas as coisas. Então o cliente não precisa ser acíncrono. Algumas pessoas via várias implementações colocando isso como acíncrono, mas não precisa ser. Legal. Funcionou, tudo bem. Mas tem uma coisa muito estranha aqui. Olha isso aqui.

**[01:23:52]** Esses dois aqui são importantes. Você está vendo que dentro do Halter, ele está colocando 18 linhas que a gente não cobriu? E o Alph também está colocando 6 linhas que a gente não cobriu. Mera, antes da nossa aplicação, dava quase 100%, mano. Por que que diminuiu a cobertura? Vamos olhar o nosso coverage aqui? Vamos lá. Então, a gente tem que pegar aqui no...

**[01:24:18]** Só estou usando o Zem Browser. De novo. Você pode abrir dando dois cliques no HTML, não é? Mas tudo bem. HTML Cov Index. E vamos olhar aqui. O que está acontecendo aqui no nosso user? Que tem 18 Missings de cobertura. Caraca! Olha o que aconteceu com a cobertura do nosso código.

**[01:24:49]** Ele tá falando que a gente nunca viu se não tinha o user, ele tá falando que nunca chamou SessionEd, SessionCommit, SessionRefresh, ele nunca retornou o userDB. É como se a gente não tivesse testando esse Endpoint. Olha que doido, o Get também, nunca chamou Return. Olha que louco, o Put nunca atualizou nenhum usuário. E o Delete, que nunca retornou ninguém. Não, não, vamos ver o Alph. Caralho, o Alph nunca foi testado. O que aconteceu, mano?

**[01:25:33]** Que loucura, meu amigo! Que doidera é essa? Vocês viram que a gente refatou... Não, não, não. Peraí, peraí, peraí. Vamo, vamo, vamo comigo aqui. Vocês viram que a gente testou isso aqui, né? Create, user, read, update, delete, erro de integridade. A gente testou o Tolkien, testou a criação do usuário. Que, que, que, que aconteceu? Por que que não tem cobertura?

**[01:26:12]** Porque a cobertura não funciona sincronamente. Sim, sim, sim, sim. Eu tenho que falar pro coverage que eu tô usando coisas assimcronas. Senão ele não tem como saber. Porque lembra que ele escalonou a coisa? Ah, ele chamou a Wait e depois do A Wait ele não volta mais. Porque o Event Loop foi pra outro lugar, ele foi resolver outra treta. Aí...

**[01:26:43]** A gente ficou com essa cobertura. Olha como isso é interessante. Quando ele encontra o primeiro await, ele para de cobrir tudo, ó. Await. Putsperei aqui, aí como o loop foi resolver outra treta, ele perdeu tudo que tinha pra baixo. É como se o código não tivesse cobertura. Olha que maluco. Aqui ó, no primeiro await, nada foi executado depois. Chegou no primeiro await que é o commit, nada foi executado depois. Então legal.

**[01:27:13]** A gente tem que falar pra ele, pro coverage, que ele suporta threads, threads é preciosidade aqui, eu não me importo muito, mas ele suporta greenlets. Lembra que todas as green threads, né, aquela coisa, a concorrência do assim que aí eu, acontece via greenlets? A gente falou isso a alguns slides atrás aqui, né? Se achou que essa informação aqui tava aqui de besta, né? Então eu preciso falar pro, pro coverage, olha...

**[01:27:48]** tem coisas sendo executadas via Greenlit. Então, olha com atenção se não tem nada escalonando aí. Vamos lá no Pi Project agora? A gente pode ir lá no fim agora. E colocar isso aqui, ó. Fala, olha. Para a ferramenta de Coverage, quando ela rodar, for executada, a concorrência deve ser avaliada via threads ou Greenlit. Olha que interessante. Vamos rodar os testes de novo agora?

**[01:28:33]** Ufa! Agora, olha o nosso user, tem seis, não é dezoito. Tem dois! Não é seis. Vamos voltar lá no coverage agora? Eeeeeee! Cubriu tudo! Onde não tá coberto é porque era cobertura de exercícios, né? Que vocês tinham que implementar. Mas agora tá tudo sendo visto. Ufa! Aí eu só me falou que a tipagem permanece como session. Mas é session, né? Aqui, ó.

**[01:29:10]** Essa session é essa variável de tipo aqui, ó. Essa session aqui remete a esse código aqui, ó. Isso remete a essa variável. Faz sentido? Agora está tudo coberto, ou seja, resolvemos o problema da cobertura sincrona. Rodamos, deu tudo certo. Mas tem outro problema. Nossa, você está vendo que assim caiu, mano? Tipo assim, é legal, é simples e tal, mas tem que mexer em tudo, mano, em tudo, em tudo.

**[01:29:56]** Se não as coisas param de funcionar. Vamos rodar a migração aqui, a gente não alterou nada no código. Eu quero aplicar a migração. Aplicar a migração. Vamos lá. Alambic, Upgrade, Hedge. Vamos ver o que acontece? Tenta aplicar no banco. Não funciona mais a migração. Porque o banco é a síncron. Aí ele está falando, olha, deu muito louco aqui a parada. Aí ele está falando, Greenlight Spawn.

**[01:30:31]** Ou seja, a chamada do Greenland has not been called. Can't call a wait only where... Tipo, onde o IO a temp... Tipo, isso aqui tá no lugar errado? O que que tá acontecendo, mano? Não! Não! Então, não funciona. E aí, o que que a gente tem que fazer? Isso aqui é um problema lá do nosso Envy. Lembra que lá no ponto Envy a gente falou que o banco agora...

**[01:31:00]** Lembra que o nosso arquivo de migração, o nosso envi-fio aqui, das migrations, ele usa os settings, né? E os settings lê do nosso ponto envi e o nosso ponto envi aponta para o banco de dados da sincrona, o io-light. Então, como é que eu resolvo esse problema? A gente vai criar migrações a sincronas.

**[01:31:28]** A migração é a síncrona. Não, a migração roda síncrono, mas dentro de código a síncrona. Sim. Sim, é isso mesmo. Sim, é isso, é isso. Então legal, vamos lá no nosso código do env.pacelon. A gente tem aqui dentro essa função chamada Run Migrations Online. Aí o que a gente vai fazer dentro dessa coisa?

**[01:31:59]** a gente vai simplesmente fingir que essa função nunca existiu legal mas eu não vou remover ela daqui porque a gente vai usar o código dela depois mas peraí então a gente vai criar uma nova função run migrations online

**[01:32:19]** A função tem que ser sincrona, né? Porque a função era sincrona. Então a gente vai importar o acinqueio. Lembra que a gente falou... Como é que a gente roda código acíncron dentro do sincrono? Lembra lá atrás? A gente falou, se quiser rodar um código sincrono, uma corrotina, a gente dá o acinqueio run. Vamos lá, importe acinqueio. acinqueio.run uma corrotina qualquer aqui. Aí a gente vai ter que escrever essa corrotina. Ah, mas o acinqueio precisa estar importado dentro da função, não.

**[01:32:50]** Pode colocar ele lá em cima. Eu só coloquei ele aqui embaixo só para simplificar a vida, né? Mas ele pode ficar lá em cima. Tá tudo bem. E aí? Olha que interessante esse código que a gente tem aqui. Essa função run migrations online. Olha o que que ela faz. Ela pega. Eu vou descomentando isso aqui. Eu vou remover os comentários. Espera aí, que não me importa muito os comentários isso aqui. A função ficou mais simples aqui, né?

**[01:33:20]** Então, a gente precisa conectar na Engine pela configuração, né? Então, a gente vai ter que pegar aqui, ó, a Sync Engine from Config, e não mais o Engine tradicional. Então, aqui, ó, em vez de a Sync Engine from Config, a Engine from Config, a gente vai para a Sync Engine from Config. Ah, massa! Então, a gente vai trocar isso aqui para ser assíncrono. Só que ser assíncrono?

**[01:33:51]** Qual é o problema de ser sincrono? Quem lembra? Quem lembra? Se eu vou precisar usar o weight, o que que eu tenho que fazer? Tem que ser um async def, não? Async def. Uuuuh, legal. E aí o que que a gente vai fazer aqui ó? Lá dentro da conexão aqui ó, a gente pegou, criou a async, a engine async. Pô, isso aqui! Pra quem tá pensando, nossa, que código mirabolante esse da migração, é exatamente o código que a gente fez.

**[01:34:32]** lá no... no... na fixture, né? Ah, ele pega os arquivos da configuração de forma síncrona, vai ter um... uma pull, né? Que a gente configurou uma pull estática lá. Só que aqui, ó, esse... connectable aqui, ele não é mais... ele é a sync, né? Lembra? A sync? Então... a sync. Uuuuh! Massa! E aí, a gente vai trocar essa parte aqui...

**[01:35:04]** A gente vai tirar tudo aqui, basicamente. A gente vai falar, olha, pra conexão que a gente tem, essa conexão, a gente vai pedir pra que ele rode as migrações de forma sincronona. Deixa eu voltar o código que tava aqui. Só pra ficar bonitinho. A gente tá mudando isso aqui. Aí eu vou falar o seguinte, olha, roda esse código da conexão de forma sincronona. Aí a gente vai pegar esse código que tem aqui.

**[01:35:33]** e vai chamar uma função que roda a migração asynchronous, que é aquele bloco de código que a gente removeu daqui. Eu chamei essa função de run async migration, só para ficar igual ao que está no slide. Run async migrations. Pode se deixar online, mas tudo bem. Run async migration, então é essa a função que a gente vai rodar aqui. Então, run async migrations.

**[01:35:59]** Legal. E aí, aquele bloquinho que a gente tinha aqui embaixo, a gente vai escrever essa nova função que a gente vai chamar de faz a migração, executa a migração. Vamos lá? Assim que def do run migrations, que era o bloquinho que a gente tinha lá fora. E aí, o que a gente precisa para rodar isso aqui? A gente precisa daquele contexto que a gente tinha aqui, que pega a conexão aqui, né?

**[01:36:39]** Aí a gente vai receber a conexão porque é um parâmetro que o Run Sync vai passar para a gente. Então a gente vai receber essa conexão. E aí o que acontece? Essa função pode ser sincronona, não precisa ser a sincronona. Context Run Migrations. A gente desmontou aquilo que a gente tinha em várias funções para poder rodar isso de forma a sincronona. Olha que bonitinho. É exatamente o mesmo código. Só que agora ele suporta conexão a sincronona.

**[01:37:15]** Só que lembrando, essa função da migração, ela tem que ser sincrona. Só que como a engenhar a sincrona, ela tem que rodar um pedaço a sincrona. Só que a migração em si, o ato de fazer a migração é sincrona. Então, a gente teve que, como a conexão precisa ser a sincrona, a gente botou esse bloco no meio. Fez sentido que a gente fez aqui?

**[01:37:48]** Não precisa entender a fundo desse código aqui, porque é código de migração. Inclusive, esse código aqui eu copiei da documentação do Alembic. Não tem nenhum mistério aqui. Async using async.io with Alembic. Juro. Esse é exatamente o código do Alembic aqui. Não fiz nada mágico, eu copiei o que tava aqui e saiu usando. Embora que a gente foi fazendo junto aqui, né?

**[01:38:34]** Então, a gente conecta no acícrono, manda rodar 5 à migração. E é literalmente isso, a gente pega a conexão, o target e manda rodar a migração. É simples. É simples quando a gente entende. Eu assim com a limbic, é exatamente essa sensação. Tipo assim, ah...

**[01:39:01]** Vou botar aqui para ver o que é. Copicola, vejo se funciona. Agora a gente consegue rodar a migração. Upgrade head. Funciona sincronamente. Lindo. O Sagui falou que preciso pegar com calma depois. Se assistiu a Live do Alembic, que eu coloquei na referência para ter assistido lá antes de a gente falar do banco de dados, ajuda bastante a entender essa parte aqui, né? A Live do Alembic. Legal. Agora temos migração.

**[01:39:40]** E acabou, agora é perguntas. Acabou, porém, com tudo entretanto e toda a via, vou fazer o commit aqui, pera aí, vai. Juntem as perguntas. Vou adicionar tudo mesmo, refatorando a estrutura do projeto, suporte assim, caiou, para uma forma não bloqueante, gitpush, quem quiser pegar lá, senhora Lembe que manda nós obedecer, sim. Legal.

**[01:40:09]** Agora é hora de eu responder perguntas pra quem chegou aqui e tem coisa pra resolver aí, seguir a vida. Uma coisa que eu, um pedido que peço encarecidamente. Na próxima aula, a gente vai usar, a gente vai conversar sobre randomização de dados. E o sentido de randomizar dados, sei lá, em vez de ter que ficar pensando no nome a José Maria Fausto, é, sabe?

**[01:40:44]** fulano, ciclano, a gente vai trabalhar com randomização, uma coisa que você não pensa em nada, você fala o nome. Ah, idade. Então a gente vai introduzir alguns conceitos de randomização de testes na próxima aula, então fica aí quem puder assistir a aula onde eu explico randomização do zero, que é a live de Python 281, ficarei muito grato.

**[01:41:11]** É obrigatório? Não. Porque nada nessa vida é obrigado. Mas, por enquanto, entretanto, vamos conversar sobre randomização. Então, a gente vai melhorar os testes que a gente tem na próxima aula e... porque a gente vai precisar testar o JWT para ver o que acontece, fica íntegro, se você não fica, como é que cria 500 dados diferentes? Então, a gente vai usar randomização. E aí, a gente tem uma live sobre randomização, vale a pena dar uma assistida. Por favor, ajudem.

**[01:41:41]** A gente, Faker, Effector e Boy. Maravilhoso, né? Aí o Lucas mandou uma pergunta aqui. É melhor refatorar o projeto ou começar ele assim? Depende, Lucas. Porque a grande questão aqui é o seguinte. Ó, só pra lembrar, Dino, antes de eu começar a responder as perguntas, tem dois exercícios a essa aula. Então lembra que você teve que criar vários endpoints aí nos exercícios. Então você vai ter que refatorar eles pra 5 ao 8. Massa?

**[01:42:14]** E a gente tem o read-route, que é aquele que retorna o olamundo, também transforme ele com o suporte em assim que é eu. Tem o quiz, o quiz da aula, então responde o quiz e beleza. E é isso. Aí agora eu vou responder as perguntas aqui que a gente recebeu. Então vamos lá. Escolher o nome de filho não é fase, então randomiza.

**[01:42:49]** A Lucas mandou. Então, é melhor refatorar o projeto ou começar ele assim. Geralmente, o código acíncrono é mais difícil de uma maneira geral. Como nesse exemplo, a gente está usando uma condição muito propícia, porque o UV loop...

**[01:43:09]** que é a implementação da Lib, o V, o Python, etc. Ele simplifica o processo desse esquema de escalonar, de resolver... Tipo assim, o UV loop, ele é maravilhoso, sabe o que é? Ele resolve o problema. Então, nesse caso, você poderia começar a sincrono quanto, não como 5. Você viu que não tem uma diferença muito gritante no código. Porém...

**[01:43:38]** em alguns momentos você vai ter regras de negócio que são as sincronas tipo assim ah preciso gerar um relatório aí esse relatório tem que pegar no seu que aí tipo assim aí você começa a pensar em um milhão de coisas que precisam ser feitas de forma a sincrona e

**[01:44:05]** Aí a coisa começa a ficar maluca. O código acíncron começa a ficar muito mais difícil. Então assim, de verdade assim, do fundo do meu coração, começa a sinc, sinc, começa a sincronou. E aí conforme a necessidade for aumentando, por que você vai começar a aplicação? Vamos ser bem sincero, né? Você não é o Facebook, né, Luca? Mas não é tirando sarro de você, não. Tipo assim, não pensa nesse sentido. Pô, quando a gente tá fazendo a aplicação,

**[01:44:35]** A gente nem sabe se a aplicação vai ter cinco usuários, tá ligado? Aí você vai escrever um código que é muito mais complicado para atender cinco pessoas. Saca. No nosso exemplo aqui do To Do List, eu duvido, mano, que três workers não resolveria o problema. Saca. Então, começa 5, sincronou mesmo, e aí conforme a aplicação for escalando, se houver necessidade, aí você vai pensando nisso.

**[01:45:12]** Saca. Tá tudo bem começar sincrono. Ah, legal. Mas se você já manja de assim, começa sincrono mesmo. Mas aí a questão é aquela voz da experiência, já sabe o que você tá fazendo. Geralmente as coisas não costumam dar muito certo no começo. Saca.

**[01:45:30]** É legal usar a síncrono por conta do desperdício, né? Tipo assim, você desperdiça recursos quando você está guardando. Saca, é melhor para o meio ambiente, é melhor para o planeta, a máquina já está rodando, que mal tem que processar mais ao mesmo tempo, sabe? Tipo, tá tudo bem, tá ligado? Porém, como tudo entretanto, todavia, não existe uma real necessidade no primeiro momento. Respondi tua pergunta, Lucas. Tipo assim...

**[01:46:03]** E desculpa, se parece que eu tirei sarro no momento... Ah, você não é o Facebook, tipo assim. Você não vai receber 50 mil pessoas no primeiro dia da aplicação, saca? Então... Esse problema é um problema que a gente quer ter, sabe? Tipo assim, pô, a minha aplicação trava em produção. É o problema que eu quero ter. É o problema que a gente vai gastar, queimar a massa cinzenta pra resolver. Mas de começo, tipo assim, não precisa, saca?

**[01:46:32]** Como você prova que a aplicação tá assim, que de verdade? Pô, precisa provar que a aplicação é assim? Você não prova, né, mano? Você não tem como provar, você mostra o código fonte. Saca, meio nesse sentido que eu tô falando, só que não... Por que que você provaria? Você quer alguma coisa assim, cara? Aí perguntaram se eu já vi o Nest assim que caiou? Nest assim que caiou é aquele do Event Loop, dentro do Event Loop? É?

**[01:47:01]** Sim, eu já ouvi falar, mas eu não me recordo. Tanto que eu não me recordo. Mas se for isso, eu já ouvi falar disso em algum momento. Já me adiantando, vai ter live sobre configuração de logs no projeto? Não. Eu comecei a trabalhar com logs no projeto de uma forma geral em uma branch que era para sair nessa versão do curso na 4, mas nunca saiu. Então, se você quiser ver, tem uma branch aqui, ela está atualizada, inclusive.

**[01:47:35]** que você pode dar uma olhada no que está rolando e tudo mais, é a Live 3.2.2 Logging. Mas eu nunca achei, eu não cheguei a implementar isso, então a gente não vai fazer isso no curso, pelo menos dessa vez, quem sabe, numa versão futura, em algum momento, no texto, isso ganhe. Saca esse sentido. Faz sentido ter uma parte da aplicação assim que outra, assim que vai.

**[01:48:04]** No momento de transição, enquanto uma coisa está sendo implementada, pode ser. Não tem problema. Está tudo massa. Não vai ter um impacto muito significativo nisso, assim. Como um infeliz que teve começar um projeto sabendo no momento de existir uma exigência de grande desempenho da aplicação. Comecei sincrono. E boa sorte para o meu... E boa sorte para o meu eu do futuro resolver. Mano, você está interligado, tipo assim.

**[01:48:43]** Quando o problema chegar, a gente resolve, né? Tem aquela frase do... do... do Nuff, né? Que é o seguinte, otimização prematura é a raiz de todo mal, né? Então... tem esse ponto, né? Saca, você vai otimizar uma coisa que você não precisa, vai tornar sua vida muito mais complicada... para nada. Saca. Sei lá, um benchmark, contar a quantidade de requisições por segundo, o usuário final perceba. Sei lá, não tem como fazer isso, tipo assim.

**[01:49:15]** Não tem como saber se está rodando paralelo, concorrente, tudo mais, o usuário vai notar se estiver lento. Fala, nossa, se manda o bagulho, leva cinco minutos para responder. Aí o usuário vai notar, nossa, dá time-out na aplicação. Faca, fora disso é irrelevante. Tanto que você escala horizontal, né, com workers, a gente fez isso a vida inteira. Aí eu só vou falar, prova para sim que é um load test. Não. Não.

**[01:49:45]** Saca, eu posso fazer uma aplicação sincrona que roda mais rápido do que uma aplicação sincrona e responder a mesma quantidade de requests. Se estiver numa curiosidade sobre isso, o Miguel, que é um dos contribuidores do Flask, Miguel Greenberg, ele tem um benchmark muito famoso, que é tipo assim, ignore todos os benchmarks, inclusive esse. Aqui ó, é isso aqui. Ignore todos os benchmarks de performance, inclusive esse.

**[01:50:22]** E aí ele prova, nesse texto, que não existe uma diferença real de performance entre sincrono e sincrono. A diferença existe, mas ela é irrelevante. E aí ele usa, mano, várias coisas sincronas, várias coisas sincronas e tudo mais, pra mostrar que tipo assim, a diferença de performance é irrelevante. A diferença de carga talvez seja melhor ou pior, mas tipo assim, é irrelevante.

**[01:50:57]** Tudo bem, esse benchmark você pode falar, não, mas é um benchmark feito, tá, tá, tá, mano. É um benchmark bom, dá uma lida, dá uma olhada, tira suas próprias conclusões, rode os testes que ele rodou e vê o que que acontece. Mas é um benchmark bom, assim, para olhar as coisas, o throughput das coisas e tudo mais. Então vale a pena dar uma lida nisso aqui, para quem tiver curiosidade sobre isso.

**[01:51:29]** Então não precisa, precisa, né? Porque você pode lidar com aplicações que tem muitos bloqueios. Então precisa. Só que tipo assim, a questão é que tipo assim, é mais rápido, não é mais rápido, mas é não bloqueante. Saca, esse é o ponto, tipo assim, não é para ser rápido devagar, é para não bloquear. Faz sentido isso?

**[01:51:52]** A gente não está discutindo o bagulho, tipo assim, ah, essa implementação é mais performática do que essa. Não! A gente está falando, a minha aplicação tem bloqueios. Eu vou remover os bloqueios. Não quer dizer que vai ficar mais rápido. Não quer dizer que vai ficar mais eficiente. O código vai ficar muito mais difícil de programar, mas ele não bloqueia. É esse o ponto. Falando sobre escalonamento horizontal com workers, vamos entrar em detalhes no curso? Não.

**[01:52:22]** O máximo que a gente chegou nisso foi o que a gente viu nessa aula, a gente não vai entrar nisso aí. Se você quiser, tem uma live de Python em que a gente discute isso. Eu não lembro exatamente, mas é a live sobre o WSGI. Tem uma live específica onde a gente fala sobre isso, então já tem material sobre isso aqui no canal. Eu não lembro qual é o número da live, eu sei que a live chama...

**[01:52:47]** WSGI e Unicorn, é o título da live, mas eu não lembro qual é o número, se alguém quiser mandar o número aí depois, é cinto e alguma coisa. Bom, se ninguém tiver mais perguntas, a gente se vê na terça-feira que vem para conversar sobre que que é a aula da semana que vem, a gente vai transformar, a gente vai resolver os problemas do JWT, né? Aqui, eu tornar o sistema de autenticação mais robusto, então se alguém quiser dar uma lida na aula,

**[01:53:20]** Na aula que vem a gente vai falar muito sobre testes, sobre randomização, sobre como parar o tempo nos testes e tudo mais. Vai ser bem divertido. Então a gente se vê na terça-feira. Beijo pra vocês, deixem suas dúvidas aqui. É cento e um, Lucas. Obrigado, Lucas. Aí, se vocês precisarem de alguma coisa, eu tô lá no group também. A gente pode ir debatendo, pode ir conversando. Um beijinho pra vocês, ó. E, ó. Tchau, tchau.

**[01:53:54]** Até semana que vem. Oh, 5 minutos mais cedo hoje, hein? Tá liberando, tô liberando todo dia mais cedo, hein? Beijinho. Tchau.

