# Transcrição da Aula: aula-02.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:08]** Olá pessoas, boa noite, boas-vindas a mais uma live aqui do nosso Curio de Festa API. Eu quase falei live de Python pelo costume. Eu sou o Dono Sauru e espero que vocês estejam bem aí. Quem chegou agora, boa noite. Pra quem já tinha dado boa noite aqui no chat, boas-vindas e bom dia, boa tarde, né? Porque a web não tem horário, qualquer pessoa.

**[00:00:30]** Tá sempre disposta aí pra assistir isso em qualquer horário. Bom, antes eu começar eu queria saber um feedback de vocês. Se o som tá ok, se o vídeo tá ok, está tudo certo. Vocês estão me ouvindo, vocês estão me vendo. Às vezes deu tudo errado e eu tô aqui falando sozinho durante um tempo, né? Então, é raro, mas acontece sempre, né? Pelos boas noites, sequências de boa noite, eu acredito que tá tudo funcionando certo, né? Então, é isso. Vamos lá pra nossa segunda aula hoje.

**[00:01:00]** Ah, me responderam que estava tudo ok. Ah, eu tenho uma pergunta para fazer antes da aula começar. Vocês fizeram o exercício e o quiz da aula passada deu tudo certo? Tudo na paz? Rolou tudo certinho? Só para perguntar assim, né? Não cobrando assim, mas só para saber. Vai que, né?

**[00:01:31]** Bom, então, no nosso encontro hoje, a gente vai conversar um pouco sobre introdução ao desenvolvimento web. Eu queria dizer o seguinte, já, logo diante mão, que tem o material em texto, né? Aquela coisa de sempre, vocês podem sempre dar uma olhada, dar uma consultada, tá tudo lá, bonitinho, arrumadinho, então, quem precisar, pode recorrer o material de texto sempre, tá tudo aqui, tudo que a gente tá falando.

**[00:02:00]** Bem explicadinho e bonitinho, então é isso. A segunda coisa que eu queria dizer é que é o seguinte, uma introdução ou desenvolvimento web, ela pode passar por vários caminhos, por vários lugares e tudo mais. Eu selecionei alguns lugares muito quietinhos, muito específicos para a gente conversar.

**[00:02:19]** para a gente criar uma base, mas essa base com muitas aspas aqui, teórica sobre desenvolvimento web. Porque para falar sobre o web, a gente precisa conversar sobre rede, sobre protocolos, sobre tipos de comunicação, sobre arquiteturas de rede, e são muitas coisas, né? Então, a ideia é a gente fazer uma introdução, dar um passinho, saber, molhar o dedão na água, assim. Não tem o objetivo de cobrir todo o assunto, porque...

**[00:02:47]** Seria impossível, a gente poderia ficar 5 anos aqui falando sobre essa introdução. Então, bom, é alguns conceitos básicos, noções e iniciais sobre rede, sobre HTTP, sobre API, sobre a OpenAPI, como aquele esquema de documentação funciona, introduzir alguns esquemas do pá idêntico e tudo mais, mas a gente vai devagarzinho entendendo essa coisa. E bom!

**[00:03:16]** O primeiro passo aqui é entender o que é o web. E eu estou vendo aqui que tem gente vendo do que likes dados. Deem likes para isso chegar em mais pessoas. Não é porque eu quero ser pop, é porque pode ajudar mais gente. Então vamos lá. A gente tem a web. Sempre que a gente se refere à aplicação web, a gente está falando de coisas que funcionam numa rede. A rede pode ser qualquer tipo de coisa. A rede da nossa casa...

**[00:03:46]** A rede, se ela está no celular, no wi-fi, você está no computador, pro lugar, houve um meio físico, saca? Com um cabo conectado, sabe esse tipo de coisa? Isso forma uma rede. Qualquer lugar onde a gente consiga conectar mais de dois dispositivos, né? Então, dois ou mais, a gente pode falar que isso é uma rede de computadores, né? Existem vários tipos de rede, a teoria de rede vai dar...

**[00:04:17]** Uma grande variedade de coisas aqui. Deixa eu agradecer aqui o Albano, pelo por se tornar membro. Tamo junto. Valeu demais, mano. Valeu, Zão. Isso me ajuda muito. Então, voltando aqui. Quando a gente fala sobre esse esquema, né, de redes, então a gente vai se referir a redes locais, né, como redes LAN. LAN significa Local Area Network, né? Network de rede, área.

**[00:04:49]** um perímetro mesmo, um espaço local e L de local. Ou seja, é a rede que a gente tem em casa, basicamente. Eu tenho um...

**[00:04:58]** um roteador aqui em casa. Basicamente todo mundo que estava assistindo isso aqui, se não estiver assistindo pelo 4G, está me vendo por um roteador passando, trafegando essa informação. E às vezes você tem vários outros dispositivos, você tem um computador, você tem um celular, você tem um computador de mesa, você tem um notebook, tem tablet, uma televisão. Dependendo de hoje em dia até a máquina de lavar, está na sua rede local, né?

**[00:05:23]** E a gente tem redes de longa distância, né? Aí a gente sai de casa, né? Então, por exemplo, que são 1.

**[00:05:30]** I wanted wide, wide area, network, então são vários roteadores interconectados, então vamos supor que eu saio daqui, a gente sai do meu PC, do meu PC vai para o roteador, e esse roteador vai passando por vários outros roteadores até que a gente se encontre em algum lugar, que esse lugar é o servidor do YouTube, que está distribuindo para todo mundo. Então a gente sempre está partindo de um pressuposto que existem coisas

**[00:05:57]** ligadas em redes, de forma às vezes guiada, com cabos, às vezes o cabo da internet chega na sua casa, fibra, às vezes você tá pro meio não guiado, né? Tipo Bluetooth, Wi-Fi, Rádio. E aí essa junção de várias pequenas redes, a gente chama de Web, que é a rede mundial. Fazia muito tempo que eu... que eu não falava isso, né, mas é...

**[00:06:29]** A rede mundial de computadores. Eu adorava quando a gente falava isso pra quem é mais velho, né? Se conectem à rede mundial de computadores, né? É muito legal. Então, a rede é nada mais é do que essa coisa, né? Esse monte de dispositivos interconectados. E por interconectados, significa, tipo assim, eu tô mandando a minha conexão pro YouTube, vocês estão acessando o YouTube, YouTube transmite isso pra vocês e vai todo nesse esquema.

**[00:06:56]** Quando a gente está falando de desenvolvimento de aplicações web, e aí sendo um pouco mais específico, a gente quer dizer que as aplicações funcionam em rede, ou via rede, guiadas pela rede. Ou seja, para você acessar a aplicação que a gente faz, a gente entra por via, por exemplo, a maioria das vezes via DMS. Você quer entrar aqui no YouTube? Você digita, né? youtube.com ou https.barrabarryoutube.com.

**[00:07:24]** Então, essa é uma maneira em que a gente se comunica, né? Então, a gente vai até lugares, às vezes por nome, que é via DNS, às vezes a gente vai via IP, que é o endereço, né? Sabe, quando a gente já configurou aquele roteador em casa, você fala, pô, 1.92, 1.68, 1.1, 1.1, conecta no roteador para mudar a senha do Wi-Fi, sabe? Esse tipo de coisa.

**[00:07:51]** Então, nesse esquema, a gente está pensando em um web nesse sentido de se comunicar. E a nossa aplicação, ela tem que estar disponível em algum lugar para que a gente possa fazer esse tipo de coisa.

**[00:08:07]** Um esquema legal aqui é que a gente tem que pensar em como isso funciona, né? E trazendo um pouco mais para dentro, assim, tipo assim, uma coisa mais unitária, a gente está falando em arquiteturas de rede específico, arquiteturas de comunicação, né? A mais comum e para a gente aqui, nesse descontexto de fazer aplicações web, é essa de cliente servidor. Ou seja, eu mando uma requisição...

**[00:08:34]** pra alguém, ou seja, ah, eu quero ir lá na API do Donossauro, então eu vou colocar lá no browser. O browser é o cliente. Saca? E aí a gente vai lá. HTTP, dois pontos, barra-barra, FastAPI do 0.donossauro.com. Aí você tá lá no browser, o browser é o cliente, né? Acontece uma comunicação de rede, ou seja, a gente tá direcionando isso pela rede.

**[00:09:02]** pedindo alguma coisa, né? A gente tá fazendo uma requisição pro servidor. E aí o servidor, que é uma máquina... Eu acho interessante falar alguma coisa aqui, né? Porque existe um mito, né? Tipo assim, nossa, mas vai colocar a coisa no ar, num servidor, na cloud, né? Na Núvem, na AWS, na Magalubin, não. Digital Ocean. Saca, meio que...

**[00:09:27]** Quando a gente fala de cloud, computing, computação e nuvem e roda aplicação no servidor, o servidor é uma máquina igual ao que você tem em casa. O servidor é um PC na casa do outro, sabe? Não pense em coisas muito mirabolantes, não, porque uma máquina com super disponibilidade é um computador que você está pagando para usar um pouquinho por mês.

**[00:09:49]** saca às vezes é um computador virtualizado tudo mas não tem problema basicamente é isso a gente tá rodando essa aplicação nesse servidor e o servidor é só o nome servidor vem só de servir né porque ele responde as mensagens as requisições que a gente faz pra ele então basicamente essa é a infraestrutura principal né arquitetura principal de quando a gente tá falando sobre

**[00:10:13]** desenvolver aplicações em rede. É a principal, não quer dizer que é a única, existem várias outras, mas pra gente é isso aqui que importa. Então, você vem aqui no browser, por exemplo, a gente vai, sei lá, no Dunossauro, tal, tal, tal, eu vou abrir aqui meu network do browser aqui e vou clicar aqui no dunossauro.com. Aí você vai vendo que ele fez várias requisições, ele foi, deu um rolê por aí, passou por vários lugares.

**[00:10:41]** Aí ele trouxe aqui a imagem que a gente pediu aqui no RIDM, tem algumas outras coisinhas que ele vai buscando, mas basicamente é esse tipo de comunicação que a gente faz. A gente pediu, ó, me dá o FESH API do zero, o arquivo.

**[00:10:59]** A versão aqui 4.0 e a gente enviou essa requisição e a gente obteve uma resposta que é um arquivo HTML e tudo mais que aconteceu aqui. Não tem nenhum mistério né. Pensa quando a gente está usando um navegador alguma coisa do gênero. A gente está simplesmente emitindo uma mensagem na rede e a gente está falando assim.

**[00:11:24]** Rede, procura a HTTP dos montos barra-barra do Nosaurus e aí chegando lá tem uma máquina, essa máquina que, por via das dúvidas, é um servidor, mas o seu computador também pode ser um servidor, ele vai ver o que que veio e falar, um, interessante essa mensagem que você me mandou. Aí ele executa uma tarefa lá por trás e traz esse resultado pra gente, né? É a mesma coisa que acontece naquela, esse aqui eu ia mostrar pra vocês depois.

**[00:11:53]** naquela aplicação que a gente estava desenvolvendo aqui, né? Então, por exemplo, quando a gente roda o servidor do Fast API, modo de desenvolvimento lá, então que a gente dá o Poetry Run, Task Run, ou só Task Run, se você estiver no ambiente virtual, meio que ele levanta um servidor e esse servidor está dentro da nossa máquina. Saca, é mais ou menos isso que está acontecendo. E aí, quando a gente vai lá no cliente, ou seja, o cliente...

**[00:12:22]** padrão da web é um navegador, né? Então, vamos lá. Quando a gente faz isso aqui, localhost8000 e a gente recebe esse olamundo, o que que aconteceu? Basicamente, a gente mandou para o servidor, a nossa máquina, ao mesmo tempo ela é o servidor e o cliente aqui dentro do modo desenvolvimento. É muito massa pensar nisso, né?

**[00:12:44]** Então, se a gente for olhar aqui no network, vou dar um F5, você vai ver que a gente foi lá, a gente bateu no localhost, localhost é um nome que a gente dá para a nossa própria máquina, né? A gente fala que é o nosso desenvolvimento local, ou host local, ou seja, quem está rodando aqui nesse momento. A gente costuma chamar isso de loopback. E a gente fez essa requisição aqui e veio a resposta, que é esse olamundo em geizão aqui, né? A gente vai conversar sobre isso mais para frente.

**[00:13:13]** Mas não tem muito um mistério sobre isso, né? Está vendo que a nossa própria máquina tem o browser, a nossa própria máquina roda o servidor, então meio que a rede ela está acontecendo aqui nesse momento nessa coisa que a gente vai chamar de loopback, ou seja, a máquina processa tudo, mas poderiam ser o servidor, sei lá, lá na...

**[00:13:32]** Quando eu penso em algum lugar, eu sempre penso na França. Estou aqui na França, museu do Louvre, é um meme muito antigo, mas tipo assim, a gente envia essa requisição, ela navega pela rede, passeia por aí e processou o que a gente enviou e traz. É massa, é isso aqui que acontece. E aí, eu me adiantei aqui no slide, mas basicamente é isso. Quando a gente usa essa flag, deve...

**[00:13:57]** do Fast API, a gente está subindo, levantando um servidor, ou seja, falando, a nossa aplicação vai ser servida por alguma coisa que é um servidor. E aí a gente chama isso aqui de servidor de aplicação, a gente vai ver isso mais na frente, mas adiantando, ou seja, a gente tem essa parte para trás. Quando a gente dá o Fast API, deve tal, tal, tal, ele serve a nossa aplicação Python e a gente via cliente, acessa isso e faz essa comunicação.

**[00:14:29]** Quando a gente roda o servidor do Fast API, algumas pessoas devem ter notado uma mensagem que ele deixa aqui, né? Eu vou sair aqui e vou rodar de novo. Ele está falando que está servindo aqui, peça atenção na mensagem, vamos ler junto aqui. Ele falou o seguinte, olha, estou subindo, está estartando o servidor de desenvolvimento e tal.

**[00:14:59]** Aí o setor de desenvolvimento está em tal lugar, o server está aqui, você pode acessar a documentação, mas aqui no final vem uma mensagem muito importante que a gente tem que lembrar aqui. Ele falou isso aqui, ó. Para atenção, nessa linha aqui, quem não está olhando a tela dá uma olhada agora. Ele falou o seguinte. Uvicorn running on 127.001.2.8000. Uvicorn, a gente não falou sobre isso ainda, né?

**[00:15:28]** O Yuvicorn, ele é a coisa que permite que o Python faça esse esquema de colocar-se na rede. Saca, então é ele que é responsável por servir a aplicação.

**[00:15:43]** Aí por isso a gente chama ele de servidor de aplicação. E aí toda vez que a gente roda esse esquema do Fast API, ele fala, uvcorn running. Ou seja, é o uvcorn que é o servidor, não é o Fast API. O Fast API tem uma malemolência ali, uma coisinha que a gente fala, olha, Fast API deve, mas por baixo dos panos ele tá rodando o uvcorn.

**[00:16:06]** que essa paradinha que ele fala. E ele fala, ó, WeaverCon está aqui e a gente está olhando WatchFiles, né? Ou seja, toda vez que a gente modifica, porque a gente está em Dev, toda vez que a gente modifica, ele restarta o servidor, né? Então eu vou colocar aquilo que eu tinha colocado aqui. Ó, ó o que ele fez. Ele falou, ó.

**[00:16:23]** Vi uma coisa, uma detecção aqui de mudança no arquivo FastAPI0 App Reloading. Aí ele desligou o servidor e ligou o servidor de novo. Então a gente consegue fazer essa dinâmica aqui via UVCorn. Então não é o FastAPI que serve a aplicação. FastAPI é onde a gente escreve a aplicação.

**[00:16:44]** Aí, pra quem tiver curiosidade, mas nerdice afundo disso, o que especifica isso é uma pep do Python, né? Uma Python enhancement propósito, que se chama pep333 ou pep33333. 3 vezes 3 ou 4 vezes 3. Então, especifica esse esqueminho aqui. Legal? E aí, o Yuvikorn, ele é uma coisa que se chama ASGI.

**[00:17:14]** E a SGI significa Asynchronous, é bonito, né? Vou falar a língua da Luciana Gimenez aqui, né? Tipo assim. Asynchronous Server Gateway Interface. Ou seja, é um servidor Asynchronous, que é o S, né?

**[00:17:32]** A Synchronal Server. E a gente tem um Gateway, que é uma coisa que é por onde a gente vai passar, né? Um portãozinho interface. Ou seja, é quem processa as requisições pra gente e traz isso do outro lado. Aí alguém tentou fazer uma analogia aqui, que falou tipo assim. O Uvicorn é o iOS do Python. Não, o iOS da Microsoft, ele é um servidor web.

**[00:17:59]** O ASGI, ou UVCORN, ou qualquer outro WSDI dessa camada do Python, não é um servidor web. É um servidor de aplicação. É um pouco diferente o conceito. A gente pode falar sobre isso em algum outro momento. Então, a ideia, então, é que a gente tem a nossa aplicação, que foi escrita usando o FastAPI, ela é processada, ou seja, ela passa, ela recebe da rede.

**[00:18:25]** por meio do UVcorn. Então o UVcorn é o servidor. Ele repasse para nossa aplicação, nossa aplicação processa, devolve para o UVcorn, no sentido de rede, e aí isso é despachado para o cliente de volta. Se você quisesse, você poderia chamar o UVcorn nativo na mão. Sem nenhum problema, né? Em vez de fazer Fast API, que é o que a gente faria aqui, né? Então que seria o Fast API dev e a gente passa o Fast API 0 app.py.

**[00:18:59]** Então, quando a gente faz isso aqui, em vez de fazer isso e deixar o FastAPI subir a aplicação, a gente pode nós mesmos chamarmos o UVCorn para fazer esse tipo de coisa. Então, você poderia falar o seguinte, em vez de FastAPI, dev, tal, tal, tal, deixa eu abrir o shell aqui, para ficar mais simples o comando. Em vez de dar PoE, você poderia fazer tipo assim, UVCorn, ou seja, o UVCorn sirva alguma coisa, a gente vai falar.

**[00:19:29]** que a gente tem a pastinha FastAPI0, cada um deu o nome que quis aqui, né? Então FastAPI0, aí a gente vai falar, olha, dentro do FastAPI0 tem um arquivo chamado app.py, então a gente quer dentro da pasta o arquivo app, aí dentro desse arquivo tem uma variável, que é a variável do server aqui dentro, e a gente pode dar dois pontos app.

**[00:20:00]** E aí, a gente subiu a aplicação, ela funciona da mesma forma que a gente tinha antes, só que a gente estartou a aplicação pelo Yuvikorn. Tem alguma diferença em fazer isso? Por baixo dos panos? Ooooo... Ooooo...

**[00:20:19]** Por baixo dos panos o test API, né, aquela linha de comando CLine, né, o command line interface, ou aquilo que a gente escreve no shell, chama o uivicorn por baixo dos panos. Então é a mesma coisa. Mas pra especificar, mostrar pra vocês que isso aqui é possível, né? Então a gente tá aqui. Massa? Então é esse o rolezinho aqui dentro. Aí estão falando que eu uso VIN, não, eu não uso VIN, eu uso GNU e MAX.

**[00:20:48]** No fundo, o Python é escrito em C e essa interface é exigente também? Não necessariamente, pode ser escrito em Python. Uma coisa não interfere na outra. Legal? Aí, vamos pensar o seguinte. Até esse momento, a gente está rodando dentro da porta de loopback. Ou seja, o nosso próprio PC serve para nós mesmos. Nessa porta que a gente chamou de 8000 aqui, que é o padrão.

**[00:21:19]** Ele já sobe na porta oito mil. O Fast API Run é um atalho para o UV Corn? Sim, basicamente isso. É para você padronizar assim, mas você poderia usar outro servidor aqui, como, sei lá, o Geo Unicorn, o Hypercorn, existem várias alternativas aqui. Legal? Aí quando a gente faz isso aqui, basicamente, rodama aqui, eu vou subir com o Fast API mesmo, porque eu acho mais bonito, tem mais mensagens aqui dentro. Aí o que que acontece aqui?

**[00:21:53]** Está vendo que ele deu esse endereço 127.001? Tem uma piada na internet que fala, não existe lugar como 127.001, não existe lugar como o nosso lar. É a nossa casa, é da onde a gente está vindo, né? É um endereço específico para nos referir a nós mesmos. Ou seja, e por padrão, na porta 8 mil.

**[00:22:15]** O que quer dizer porta? Quer dizer que a máquina suporta 64 mil portas. Ele escolheu uma, que é a 8 mil. Se você tiver trabalhado com outra linguagem em algum momento, algumas linguagens abrem outras portas, a 5 mil. O Hugo, que é um negócio de blog, sobe a 13 e 13, então cada um brinca com isso. Sobre a pergunta de WebSockets, isso sai totalmente fora do escopo da aula, mas dá e tem uma live sobre isso aqui no canal.

**[00:22:42]** Legal? Então a gente tá nesse loopback. A nossa própria máquina conversando com a nossa própria máquina. Não dá pra eu servir, sabe? Dá pra servir vários browser, várias coisas dentro da nossa própria aplicação, mas eu não consigo jogar isso na rede. Eu não consigo falar, sabe? Tem alguém em casa? Alguém aí na sua casa? Consegue falar? Olha a API que eu tô fazendo aí, mano. Que muito louco. Não dá, não dá pra fazer isso, né? E aí que entra...

**[00:23:10]** O esquema do host aqui, né? Que eu posso dizer para o UVCorn que eu quero servir a minha aplicação, mas não em um modo de loopback.

**[00:23:22]** Eu quero dizer que eu quero disponibilizar, eu quero que você abra essa porta, que padrão é oito mil, na rede, ou seja, para que outros dispositivos possam conectar aqui dentro. Essa é a diferença, basicamente, do servidor de desenvolvimento para o servidor que roda de verdade, vou dizer assim. Essa é a aplicação aqui do host. Então, se eu vier aqui e falar o seguinte, olha, na hora de rodar, bota o host aqui.

**[00:23:50]** Então, vamos lá. Menos-menos-host. Isso pode ser feito no UV-Corn também, se você preferir. 0.0.0.0. Isso aqui é um IP, um endereço que eu digo para o Python aqui. Não só para o Python, mas para várias coisas. Eu estou falando, olha. Serve isso aqui em rede. E aí, a partir disso aqui, qualquer outro dispositivo conectado na minha rede,

**[00:24:21]** pode visualizar o que está acontecendo aqui dentro. Então, por exemplo, ah! Chironinho, obrigado pelo, ó, pelo... por entrar no clube de membros. Então, vamos ver agora o seguinte, eu não sei qual é o IP da minha máquina. Não sei. E é o IP na rede local, né? Então, como é que eu faço isso? Se você estiver no Windows, você faz o seguinte, IP config, massa, no Linux, é IPADDR.

**[00:24:56]** E aí, se você estiver em qualquer outro sistema, eu não sei dizer, se alguém puder me ajudar, massa. Aí eu consigo ver aqui que o meu endereço de P na rede local é esse aqui ó, 192.168.15.11. Não, isso é apenas na minha rede, é na LAN, eu estou na rede de casa.

**[00:25:17]** Isso aqui, a gente pode acessar outros dispositivos. É assim que funciona, por exemplo, na padaria, na locadora, sei lá, na lanhouse, em qualquer lugar que você queira colocar aqui dentro. Massa. Então, a gente pode fazer esse esquema aqui. Eu vou dar uma sugestão pra gente fazer de outra forma, mas tudo bem. Eu vou entrar aqui, por enquanto, só pra mostrar pra vocês que eu tô em outro lugar aqui. Pera aí. Puta...

**[00:25:49]** Eu esqueci o nome do... da aplicação que mostra o dispositivo móvel aqui. É... Pai... SCRC... Pai... C-Pai. Isso. Aqui. Legal. Vocês estão vendo o meu celular daqui. Então se a gente descobriu IP que a gente acabou de ver aqui, que era esse aqui, 192, 168 e tal, a gente consegue acessar isso, que não está conectado no meu celular de forma nenhuma. Então, 8 mil.

**[00:26:27]** Aí tá aqui ó, o nosso olá mundo tá aqui na rede. Via rede, lindo, maravilhoso. Então dentro de casa você pode fazer esse tipo de coisa. Se você quiser, se você tiver a fim, rola. Se você não tiver, não souber como descobrir o seu IP, o IP da sua própria máquina, eu deixei aqui um comando do Python, né? Isso aqui tá na página, então pra vocês não terem que copiar aqui.

**[00:26:56]** Está aqui na página dessa aula. Socket. Ah, não é socket. O que eu deixei aqui no comando? Era socket, não é? É socket. Talvez eu tenha deixado isso minimizado aqui. Aqui, ó. Está nesse tópico aqui, usando Fast API na rede local. Como fazer isso aqui funcionar. Então, se você não souber como descobrir seu próprio IP, você pode fazer isso com Python. Aí você abre o terminal do Python, isso é da Python.

**[00:27:32]** E aí você vai digitando aqui, import sockets, pega aqui, conecta, via na porta 80 de um servidor de DNS qualquer. E aí você vai trazer aqui, ele vai dar o IP que a gente tinha, um 9.2, um 6.8, um 15.10, que é o mesmo que tinha lá. Então você não souber como fazer no seu sistema operacional, a gente está aqui, então você pode, tem um bloquinho de código explicando como fazer isso aqui.

**[00:28:02]** Então, basicamente, ele vai te dar o IP. E aí, com o IP, você pode acessar onde você quiser. Em outro dispositivo, você pode mandar o IP e falar, oh, acessa aí. Sei lá, tem alguém na sua casa, sua mãe, seu pai, sua esposa, seu marido, filho. Saca, pode mandar o IP e falar, olha, mano. Funcionando. Olha aí, meu olá mundo. Massa, é massa demais, é massa demais. Então, a gente pode...

**[00:28:27]** fazer esse tipo de coisa e disponibilizar para as pessoas. É bonito, sabe? Mostrar, compartilhar o aprendizado com as pessoas e tudo mais. Eu pelo menos me divirto bastante com isso. Espero que seja divertido para vocês rodar para a aplicação dentro de casa, porque eu gosto muito disso. Massa? Então, legal.

**[00:28:51]** Para a gente partir para o próximo tópico aqui, aí perguntarei como eu faria para ter um DNS na rede local. Você precisaria de um servidor de DNS, mas não é o assunto dessa aula aqui, nem de longe. Mas você pode subir um servidor de DNS em casa. Está tudo massa. Testei no celular, deu certo. É assim que funciona a famosa intranete. Sim, intranete de casa é a mesma da empresa. Assim, às vezes a empresa tem mais redes. Mais subredes, mas é esse basicamente o esquema.

**[00:29:20]** Então, vocês viram que não tem nenhum mistério, nenhuma coisa muito mirabolante aqui. Vocês viram como que serve a coisa? É simples. Quando a gente for colocar isso aqui lá no servidor, o web, lá no C aonde, o que vai mudar isso. Você vai colocar o menos-menos host e vai abrir a porta e fala, ó, conecta aí na minha aplicação. E aí a gente tá lá no... na cloud, né?

**[00:29:43]** Cloud Computer, o computador dos outros, você vai fazer só isso. Host, tal, tal, tal. E aí ele serve a aplicação e a gente consegue acessar de fora, né? Porque lá existe um IP público, né? Onde a gente consegue acessar que não é o nosso, né? De classe C de dentro de casa. Um nove, dois, um meia, oito. Vai dar um IP de verdade, a gente pode acessar esse IP, porque vai ficar disponível. Então não tem muito mistério em pensar em como você vai rodar em produção. É literalmente... Não é... Não tem deve no comando. Mas é isso que vai acontecer.

**[00:30:13]** quando a gente rodar lá na frente. Massa! Então a gente entendeu que existe essa interconexão, existe o cliente servidor, a gente como cliente acessando via browser ou via qualquer outra coisa, existe o servidor, só que como é que acontecem essas conversas? Então, por exemplo, eu mando uma mensagem, falo ó,

**[00:30:38]** Mando a mensagem para alguém, para algum servidor, né? Eu sou o cliente, quero acessar o FastAPI do 0.dunossauro. O meu site, vou usar o meu site como exemplo, porque é mais simples, dunossauro.com. Eu quero ir lá no dunossauro.com, então existe um modelo padrão de como funciona o web. Essa é uma prática normal aqui. E apesar de existir muitas outras coisas,

**[00:31:02]** Para o contexto do que a gente está falando aqui, a gente precisa pensar em algumas coisas. Existe uma forma de localizar as coisas, e quando eu digo localizar as coisas, eu estou dizendo aonde essa coisa está. Como é que eu chego até lá?

**[00:31:18]** Só que então precisa ter um endereço, igual a gente viu um 9, 2, 6, 8, 15, 10, era isso meu? E na casa de vocês deu um outro, diferente e tudo mais, então a gente pode se conectar dessa forma e conversar dessa forma, né? Caio, obrigado pelo teu super chat, mano. Me ajuda muito isso, velho. Valeu. De mais.

**[00:31:37]** E aí a gente precisa de um localizador, né? Alguma coisa que a gente use pra fazer isso. E é daí que vem o termo URL, né? Sabe aquele negócio de digita no browser? http www.google.com

**[00:31:51]** DuckDuckGo.com, sabe? Aquilo faz parte de uma forma de encontrar, de localizar o recurso que você quer na rede mundial de computadores. Então, é simplesmente, eu quero falar com a. Então, eu mando uma mensagem e tenho que falar onde essa coisa está. E aí, a gente usa esse esquema, que é o URL, que é um localizador uniforme de recurso. Recurso é qualquer coisa que a gente queira pegar na rede, ou seja, eu preciso

**[00:32:20]** da UIP e tal, não sei o que, barra dox, aquele tipo de coisa. Então tudo que a gente quer acessar de dentro de um servidor é um recurso, é um localizador porque a gente descreve até onde ele vai e a gente tem uniforme porque é uma forma comum de fazer isso, vou dizer desse jeitinho. Massa, uma outra coisa interessante aqui é o HTTP, ou seja, o segundo pilar.

**[00:32:49]** Então, aqui é como encontrar as coisas. O HTTP é um protocolo. E aí, leias, penses em protocolo como a forma em que a gente vai se comunicar. Então, por exemplo, o Caio, que estava aqui, que mandou um superset aqui para a gente.

**[00:33:07]** Ele falou o seguinte, opa! Boa noite, meu querido. Então, o que que acontece? O Caio falou comigo numa língua que eu entendo, sabe? A gente estabeleceu um padrão de comunicação entre todos nós que estamos aqui. Vocês estão me assistindo, eu estou falando português e vocês estão entendendo o que eu estou falando, porque existe uma regra para que a gente possa se comunicar e se entender. Basicamente, um protocolo de rede estabelece esse tipo de coisa.

**[00:33:35]** Eu te chamo, como é que é seu nome? É Caio, por exemplo, ou Wesley, que mandou a última mensagem aqui. Então, eu me direciono a ele falando em português, falando em uma língua, falando em um dialeto, uma coisa específica pré-estabelecida entre a gente. Saca? Então, as coisas vão acontecer da maneira em que a gente combinar. E aí, o HTTP, ele é um conjunto de regras. Saca, que a gente vai usar para falar um com o outro.

**[00:34:03]** Aí o junior colocou aqui que é um acordo, um contrato, pode ser uma boa metáfora essa também, que é uma forma de como a gente vai estabelecer a comunicação. Ou seja, se eu mandar um zero e um pra você, você tem que saber responder o zero e um que eu te mandei, é basicamente isso. Então o protocolo base da web é o HTTP. HTTP significa hypertext transfer protocol. Hypertext é hipertexto, né?

**[00:34:30]** Ou seja, documentos de texto com tags e transfer de transferência, eu transfero de lá para cá e pedi protocol. Ou seja, então é um acordo que eu, cliente e o servidor, vamos nos comunicar a partir de hipertesto, pela transferência de hipertesto.

**[00:34:51]** E aí o HTML, que é o terceiro conceito fundamental aqui dentro, que é a linguagem de hipertexto que a gente usa na web. Ou seja, quando eu peço alguma coisa, aquela mensagem vem formatada, pagina bonitinha, né? Você entra no Google e aí tem lá uma caixinha e tal. Sabe, aqueles elementos são elementos definidos nessa linguagem que é o HTML. Massa?

**[00:35:18]** Então, vamos... Queria entender se para você está tudo massa aqui, né? Esse padrão, essas coisas e tudo mais. Quando a gente fala de URL, a gente está falando basicamente disso aqui. Não é nada muito de outro mundo, né? Olha como é o URL. O URL fala, olha. Esse é o protocolo que eu vou usar, HTTP. Eu não sei se vocês já viram em algum lugar, né? Às vezes, usa FTP, que é o File Transfer Protocol. A gente tem o SMTP, que é o de e-mail.

**[00:35:50]** A gente tem vários outros protocolos que a gente pode usar aqui dentro. E o HTTP é essa forma de se comunicar na web via páginas, trocando hipertexto. Então, basicamente toda vez que eu comece o URL, mesmo que eu não coloque isso aqui, eu coloque, sei lá, dunossauro.com, vamos ver. Dunossauro.com. No fim das contas, ele está usando aqui por baixo o HTTP ESO, dois pontos, barra barra, dunossauro.com.

**[00:36:20]** Olha que massa, então essa é a minha página. Então a gente usa esse protocolo mesmo quando a gente não diz nada no browser, como cliente, é sempre HTTP ou HTTPS. E o HTTPS é o Secure, a HTTP, né? Então é o Hypertext Transfer Protocol, seguro. O S é de seguro, porque ele encrypta a mensagem.

**[00:36:45]** Aí a gente tem um endereço, esse endereço pode ser um número de P, igual a gente fez aqui, 127.001.192.168.10.5. Pode ser qualquer outra coisa. Vocês viram quando eu entrei no dunossauro.com? Eu não coloquei a porta que a gente usa, porque o HTTP por padrão, ele usa a porta 80. Ou seja, se eu quisesse vir aqui e falar, olha, conecta no dunossauro, tal, tal, tal, na porta 80.

**[00:37:17]** Aí ele falou, não é seguro, porque a porta 80 trafega HTTP. E aí a gente tem a porta do HTTPS, que é uma outra coisa, mas essas coisas são padrões aqui, né? Então, a gente faz esse esquema. Então esse é o começo da URL, né? A gente tem um protocolo, um endereço, uma porta. Basicamente isso. Quando a gente não especifica o protocolo, a gente sabe que HTTP é o HTTPS.

**[00:37:47]** a porta por padrão, ou é a porta do HTTP, ou é a porta do HTTPS. Massa? Legal? E aí é ORL, depois disso tem algumas outras coisas, né? Então ela tem um caminho, barra caminho, barra recurso, barra query, barra fragmento, a gente pode acessar várias dessas coisas, né? Vocês viram que no link da aula, né, a gente vai lá pro FES, API, do 0.dunossauro.com, barra, 0, barra...

**[00:38:20]** 4.0, ou seja, que é o caminho, a gente está indo para a versão 4. O recurso é aula 01, por exemplo. 02, que é a aula que a gente está hoje, né? Basicamente aqui, deixa eu abrir aqui. Ó, essa URL tem tudo, né? Que a gente pode mostrar aqui. Então, a gente tem o protocolo, o endereço, a gente tem algumas coisas aqui. A gente vai ter, deixa eu voltar aqui no slide para ficar mais simples de olhar, a gente tem o caminho, o recurso, né?

**[00:38:58]** Então esse aqui é o caminho, esse aqui é o recurso que a gente quer, e aqui é a coisa que a gente chama de fragmento, fragmento. Então a gente tem tudo aqui. A única coisa que a gente não tem aqui é o aquarestring, mas a gente vai ver isso em algum outro momento. Guarda esse ponto de interrogação aqui, que a gente vai usar esse esquema mais para frente. Massa? Então a URL é isso. Olha como é massa. Então eu falo, olha...

**[00:39:29]** Quando eu digito essa URL, eu estou falando o seguinte, olha, via protocolo HTTPS, vai nesse lugar aqui, o que eu quero é esse caminho aqui, ou seja, N4.0, o recurso que eu quero é o 2, e o fragmento que eu quero é esse aqui, usando o Fast API na rede local. Olha que massa, então você consegue especificar via um URL exatamente o que você quer, o que você está procurando lá do outro lado.

**[00:39:56]** É basicamente essa função da URL. Então, a gente diz como a conexão vai acontecer e baseado no que a gente está enviando de um lado para o outro. Fez sentido isso aqui? É muita coisinha, né? É muito... muitas coisinhas pequenininhas e tudo mais. E a gente vai trocando essa ideia e tudo mais. E o que seria o .com, .io, .br, .gov é parte do...

**[00:40:28]** É parte do endereço. É o lugar onde a gente está no domínio. Então, por exemplo, a ponto com é de company. Ponto IO, ponto BR de Brasil, ponto GOV de governo, sabe? Então, basicamente, cada coisa pega o que quer aqui dentro e você compra isso, ponto org, se você for uma organização, sabe? Esse tipo de coisa. Mas, em teoria, qualquer um pode comprar qualquer domínio. Você vai lá e fala, ó, eu quero ponto IA.

**[00:40:58]** Pode ser, está tudo massa, você pode comprar ele. Aí estão falando de coisas de HTPS, bom, meu objetivo não é falar sobre HTPS, a gente não vai falar sobre isso.

**[00:41:10]** O S incripta não é real não, ele incripta o corpo da mensagem. A gente não chegou nesse lugar ainda, a gente vai chegar daqui a pouco. Massa, então dá uma segurada. Ponto beleza! Então, o HTTP, que é esse protocolo que a gente está usando para se comunicar, o Hyper Text Transfer Protocol, ou o protocolo de transferência de hipertexto,

**[00:41:33]** É a ideia de que a gente tem esse modelo cliente servidor, então eu estou mandando uma coisa e o servidor vai me responder alguma coisa. E aí esse protocolo, essa forma, esse acordo, sabe, esse bagulho que a gente combina antes, ele tem mais ou menos essa cara, né? Então quando a gente envia uma coisa via HTTP, a gente está trafegando uma mensagem de um lado para o outro. Então, por exemplo, olha...

**[00:41:59]** Aqui existe várias coisinhas, né, que fazem parte do protocolo, que são interessantes a gente ver. Então, por exemplo, ó, eu tô emitindo uma mensagem, e essa mensagem é um get, ou seja, get traduzido, a gente vai fazer o quê? Com get, a gente vai, pega alguma coisa. Então, me dá aí, servidor, tô te pedindo alguma coisa. E essa coisa tá em que lugar? No barra. E que protocolo a gente tá falando? HTTP 1.0, na versão 1.0.

**[00:42:31]** Aí tem algumas coisas na mensagem aqui, isso aqui daria pra fazer tipo assim, se ela não assim iguala só sobre a mensagem, mas eu tô indo por cima assim, mas se a gente tá falando, olha, aceito qualquer coisa, ou seja, se você quiser me mandar a qualquer tipo de pertexto, eu vou aceitar. E aí os encodes que eu aceito, né, GZIP quer dizer que vai estar zipado, compactado pra trafegar menos dado na rede, a conexão é do tipo keep a live, ou seja, mantém ligado aí pra nós.

**[00:43:01]** E aí, esse é o host, né? Pra onde a gente tá indo, o user agent, que foi quem fez essa requisição, por exemplo, se fosse no browser, isso aqui seria, sei lá, Mozilla Firefox, Google Chrome, ou qualquer outro tipo de coisa aqui. Mas, então, a gente envia essa mensagem. Então, a gente tá falando, olha, eu tô dando um get no caminho, tal, e eu aceito qualquer coisa que você me mandar de volta. E aí, ele vai trazer a resposta pra gente, né? Esse foi na nossa própria aplicação, né? Então ele falou, ó...

**[00:43:31]** Usando HTTP 1.1 que foi o que você me mandou, eu estou te mandando 200 OK. E aí 200 aqui significa é um tipo de resposta, de status code, a gente costuma chamar isso aqui. Então ele vai me dar, está falando 200 é o status de que deu certo. OK, estou te retornando aí o que você me pediu.

**[00:43:53]** E aí esse é o tamanho da mensagem, 24 bytes. O tipo do conteúdo que eu estou te mandando está em JSON, que é uma coisa que a gente vai ver. A data em que isso aqui aconteceu foi essa data aqui. E quem é o servidor, ou seja, do mesmo jeito que você sabia quem foi que pediu, o cliente a gente sabe quem foi que respondeu. E aqui no caso é o UVCorn, que mandou essa resposta.

**[00:44:15]** E aí, aqui embaixo, está o conteúdo da mensagem, né? Então, isso aqui é sobre o protocolo, né? A mensagem que a gente envia. Essa é a mensagem que o protocolo retorna, além daquela coisa, né? Ou seja, está mandando um content-type, né? Um dado do tipo JSON. JSON. JSON. Chame como quiser, isso aqui. Nossa, fez sentido isso aqui? Então, a gente localizou, falou qualquer recurso que a gente queria e mandou, né?

**[00:44:44]** Se a gente fizer isso aqui, pelo shell, dá pra ver. Tem algumas coisas, sei lá, o HTTPi, né? HTTPi. É uma ferramenta de shell, você pode instalar ela com Pipex, né? Então, Pipex, install HTTPi. Se você quiser rodar isso aqui, só pra ver, né? Eu vou usar isso aqui, só como exemplo. Então, eu vou falar o seguinte, HTTP, sei lá, dunossauro.com. Eu quero ir lá pro dunossauro.com. Então, eu tô emitindo uma requisição pra ele. Aí ele falou, olha!

**[00:45:13]** HTTP 1.1 não existe essa página que você está pedindo, porque essa página é HTTPS. Aí ele deu 301, que é um outro código de minha resposta, falou, foi movido permanentemente. Aí ele falou, redirecione para a HTTPS, do nostro.com. Ou seja, se a gente tentar HTTPS...

**[00:45:35]** Aí ele retornou pra mim e ele retorna exatamente aquilo. O hipertexto aqui, o corpo da mensagem que ele emitiu e aqui em cima está toda a informação, deu 200 OK. Aí tem coisa de cache, a data, a tag, quem é o servidor? É o Netlify, que é lá onde eu estou usando. Olha que massa. Então toda essa comunicação acontece via essa troca de mensagens e é basicamente isso que vai, é o corpo.

**[00:46:03]** de envio e o corpo de resposta é assim que a gente troca a ideia massa aí beleza aí estão fazendo outras perguntas de coisas que a gente vai falar mais lá na frente e tudo mais mas tudo bem então aquela parte a gente viu né do do do cabeçalho né ou seja o início da coisa a gente chama de cabeçalho e isso aqui é o corpo então

**[00:46:31]** tem a parte onde ficam as informações e tem a parte onde tem o resultado da mensagem. A gente já acabou falando, né? Content type, né? Ele veio o application de ASON, porque a nossa aplicação retorna de ASON, mas poderia ser text.html, igual essa que a gente fez aqui agora, né? Peraí que eu fiz caquinho aqui. Então, ó, tá vendo que ele retorna um montão de HTML aqui? Essa é o HTML da minha página. E em algum lugar ele vai falar aqui, ó, content type.

**[00:47:01]** Text HTML, que é o padrão da web, né, para afegar HTML. Então, todas essas informações vão e voltam dependendo de como a gente se comunique ou estabelece uma conexão web. E aí, para a gente enviar esse tipo de mensagem, lembra que no cabeçalho tinha aqui um get.

**[00:47:19]** Ou seja, basicamente tudo que a gente faz é get. Ah, me dá aí informação do recurso tal. Mas às vezes a gente quer enviar outros tipos de mensagem no HTTP, né? Existe além do get, que é pra pedir alguma coisa, ou seja, aqui a tradução é recuperar recursos, eu odeio isso. É tipo assim, mano, me dá essa página aí, me dá esse dado aí, te vou dar mais fácil de entender. Aí a gente tem o método post, e aí o post é quando eu tô dando alguma coisa pro servidor e falando, ó, cria isso aí pra mim.

**[00:47:49]** sabe e aí um exemplo padrão isso aqui sabe quando você tá batendo a folha de ponto é só para traumatizar todo mundo aqui você falou cria uma entrada aí na folha de ponto falar que eu entrei hoje

**[00:48:00]** 8.48 da noite. Saca? Então você tá enviando uma mensagem que você quer que o servidor persista, né? Que ele crie um novo recurso a partir disso. Então essa é a ideia do post. Ou seja, crie um compromisso na minha agenda. Vai ter uma nova live de Python. Então você tá vendo que a gente manda uma mensagem e essa mensagem cria conteúdo no servidor. A gente tá dando recurso pro servidor criar coisas. Mas criar coisas não quer dizer tipo assim, ah...

**[00:48:27]** faz um mortal triplo carpado, são recursos, sabe? Ah, eu tô te dando ABCID, e aí te dou isso, e aí você cria isso, a partir de, sei lá, um formulário que eu preenchi, cria o meu cadastro, um evento que a gente vai cadastrar e tudo mais. Então, a gente vai trocando essa ideia e vai conversando aqui dentro. E a gente tem o pute.

**[00:48:53]** E o que é o PUT? O PUT é uma forma de atualizar esse recurso. Tem outro, né? Tem o PUT, tem o PAT. Existem vários outros verbos, eu estou colocando só os mais tradicionais aqui. Tem o HED, tem várias outras coisas. E aí o PUT é para a gente atualizar alguma coisa, sabe? Tipo assim, ó, você enviou o pagamento de uma conta, aí a conta muda o estado, né? Então, por exemplo, você deu o GET e pediu a conta.

**[00:49:16]** Aí quando alguém criou a conta, sei lá, a conta de luz, aí deu post, criou essa coisa. E aí quando você está lá, você pagou, ele viu o put, altera o recurso. Ou seja, sabe quando você fala put que se me assenha, aí ele estimando uma coisa para você atualizar a sua senha? Então aquilo é uma forma de atualização. Saca, então o put serve para isso. Ou seja, mudar seu nome, mudar sua...

**[00:49:42]** sua foto de perfil atualizar a hora que você vai no médico sabe esse tipo de coisa então tem mudanças nos recursos e a gente tem o delete e o delete bom ele por si só é auto explicativo né ele deleta o recurso então aqui a gente pede aqui a gente cria que a gente altera e aqui a gente deleta esse recurso então são os verbos mais tradicionais aqui do http get post put delete

**[00:50:07]** As vezes a gente usa o patch que também serve para atualizar, mas ele atualiza de forma parcial, a gente vai ver isso lá na frente. Massa, legal, então é basicamente esse o esquema aqui que a gente troca de informações. Então a gente envia no cabeçalho o que a gente quer que o servidor faça com a mensagem que a gente enviou para ele. E aí, basicamente, sabe aquela função que a gente tinha aqui? Olha que massa!

**[00:50:39]** Agora todas as coisas fazem sentido aqui. Vamos voltar lá no código que a gente tinha feito aqui? Deixa eu apagar isso aqui. Agora não tem um mistério muito grande no código que a gente fez no dia, sabe, na aula passada. Olha aqui, a gente criou uma aplicação FastAPI e aí a gente tem um GAT, ou seja, isso aqui, essa função, vou separar aqui.

**[00:51:06]** Essa função readRoot é o que vai ser chamado quando o servidor receber um get, ou seja, um pedido get no cabeçalho, a gente vai enviar no recurso barra, olha que massa, ou seja, não tem nada para dentro, é só barra. Quando eu mandar no barra, ou seja, na raiz, no root do repositório, ele vai me enviar essa mensagem, ou seja, eu tô pedindo a página padrão.

**[00:51:34]** E quando eu pedir a página padrão, ele vai me retornar um olá mundo. Por padrão, ele já é Jason, porque eu fechei API e faz esse tipo de conversão aqui. Mas saca, não tem nada de muito absurdo aqui. Se a gente entende o básico do fundamento da web, a gente consegue entender o que o framework está fazendo por baixo dos panos. Saca, então, ó, o nosso aplicativo, quando receber uma mensagem de get no caminho barra, ele vai retornar isso aqui.

**[00:52:06]** Simples. Parecia mais difícil, né? Além de ser só um decorador, que é uma coisa ridículamente simples, cara, esse framework é muito lindo, né? Pode falar. Todos eles, né, da geração do bobo para a frente, assim, o Flask, o Festa de IPA, eles funcionam mais ou menos nessa ideia, ou Black Sheep, o Robin, e é muito massa. Porque é basicamente uma aplicação pura do conceito da web, que a gente acabou de ver. Fez sentido agora esse código? Pra quem tinha chegado aqui e tinha meio que dado uma viajada,

**[00:52:38]** que eu falei mano não precisa entender agora a gente vai entender na próxima aula o que que é cada coisa dessa olha que massa como isso aqui funciona e aí uma outra coisa interessante aqui é o teste que a gente escreveu lembra que a gente escreveu um teste né e olha o que que a gente fez basicamente olha tudo tudo faz sentido

**[00:53:09]** A gente criou um cliente, um cliente, fez uma requisição via cliente, via método get no caminho barra da URL, e a gente veio, viu se retornou OK, lembra que o cabeçalho quando dá certo ele retorna OK, viu se retornou OK, e viu se a mensagem no corpo o Jason era esse, olá mundo. Caraca, é bonito isso aqui, né?

**[00:53:39]** Você viu que não tem nenhum mistério nesse código? O código é literalmente a aplicação do conceito da web por simples. Olha! Não, para, olha, olha isso aqui. É delicioso, não é? Fala, fala pra mim. JVCS, obrigado, mano. Tamo junto. Valeu, Apple Super Chat. Entendeu isso aqui?

**[00:54:02]** Cara, isso aqui lindo, é lindo, é maravilhoso. Sou suspeito pra falar, sou suspeito, eu fiz um curso disso aqui, eu sou suspeito pra falar. Mas vocês viram isso aqui? É aplicação clara e simples da parada? É literalmente o conceito aplicado na prática. E depois vem alguém falar que não é pra aprender conceito, né? Bom, não quero entrar nessa polêmica aqui. Então legal, a gente viu duas respostas hoje, né? A gente viu o... o... o duzentos, né?

**[00:54:34]** que deu ok? 200 é tipo assim, deu bom. E a gente viu o 301, né? E o 301 é uma mensagem de redirecionamento. Lembra quando a gente deu a HTTP aqui para o dono sauro? Ele falou, ó, 301. Foi movido. Olha que massa!

**[00:54:57]** Então, dentro dessa brincadeira aqui existe uma lista de códigos e esses códigos são divididos em classes, códigos de resposta. Então, sempre quando a gente recebe um código 100 é informativo, sabe? Tá te dando uma informação, ó, recebi aqui, mas amanhã eu vejo. Sabe esse tipo de coisa? Ah, é, néis, é isso aí. Não mudou, não. Saca, esse é o 100.

**[00:55:20]** O 200 é que deu certo, ou seja, 200 é OK, deu bom, 201 é created, deu certo. Aí a gente tem o 300, que é essa classe do redirecionamento, ou seja, movi pra cá, encontrei o que você queria. Saca, então, pô, massa demais, lindo. E aí tem os 400, né? O 400 é o erro no cliente.

**[00:55:48]** Ou seja, quer enganar o cliente. Então o 400 serve esse tipo de coisa. Quando o cliente fez caquinha na requisição, por exemplo, imagina que a gente está aqui nesse servidor do Fast API e eu peço um endereço que não existe, né? A gente sabe que só existe o barra, né? Então vamos lá, localhost 8000. A gente sabe que existe só o barra aqui, né?

**[00:56:15]** E ele deu esse ok olá mundo. Mas se a gente pedisse um recurso que não existe? Batatinhas fritas. Aí ele deu o 404, not found. Quando a gente vê o 400, significa que o cliente fez alguma coisa errada. A gente já tem o bad request quando foi feito meio esquisito. A gente tem o 404, que a gente acabou de ver que é o not found. A gente tem coisas, como que eu vou dizer? Tem o 422, que é o erro que a gente mais vai ver.

**[00:56:48]** no mundo. Saca, aqui, porque não foi formatado, então toda vez que o servidor retorna a 400, significa que o cliente fez alguma coisa errada.

**[00:57:01]** E a gente tem o 500, que é quando o servidor fez caquinha. Ou seja, a gente recebeu uma coisa que a gente não soube o que fazer com aquilo. Então aí o servidor dá 500. Então são essas as classes de eu, 100, 200, 300, 400 e 500. A documentação disso aqui, tá numa página do IANA, que é o Orgon, né? O Internet Assigner Number Authority. Não interessa muito o que isso quer dizer, mas é isso. Aqui ó.

**[00:57:30]** É um órgão que rege algumas coisas da internet, o Iana. E aqui tem a especificação de todos os erros. Então, se você quiser ver qualquer coisa aqui, ó, deu 100. 100 é, continua aí. Beleza, massa, manda mais. Aí, pô, tem um monte, um monte, um monte, um monte. São muitos erros aqui. Muitos, muitos status de resposta aqui. O meu preferido é o Aena Teapot.

**[00:58:06]** Não tá aqui o ANT-POD? Ah, que triste. Porque é um código de meme.

**[00:58:14]** Sabe? Então aqui tem todas as especificações e aí se você quiser ver, pô, como é que funciona o 200? E aí tem uma RFC, que é uma especificação de onde isso foi definido e tal. E aí você pode vir aqui e ver todas as definições, todo o documento, tudo isso aqui é aberto porque é um protocolo padrão da internet, né? Então você pode ver o que que aconteceu, que a gente estava falando. O que que é um resource? O que que é uma representação? Conexão, cliente, mensagem, user agents? Tá tudo especificadinho aqui.

**[00:58:43]** Tintin por Tintin. E aí, se você quiser ver isso de uma forma lúdica, porque nem todo mundo quer entrar no Iana, você pode ver o HTTP cats. Que é uma explica... uma... É 418, a antipote tava lá? Eu não vi. Mas beleza. Seguindo aqui. Ó, aí você pode ver, tipo assim, de uma forma mais lúdica. Processing. Tô processando. Saca, tem um monte de coisa aqui. Found. Encontrei.

**[00:59:27]** 404, not found. Não encontrei. E aí tem esse aqui de gatinho pra quem gosta de cachorro, tem uma HTTP with dogs. E aí, sei lá, são formas de ver isso aqui de uma forma mais didática. Saca? Então tem isso aqui. Aí você pode ver, oh, 404.

**[00:59:56]** Not found, é o cachorrinho procurando a parada, não encontrou. Mas beleza, essas são representações lúdicas, né? Se você precisar da explicação de verdade, vá no Iana, né? Pelo amor de Deus. Ah não, esse cachorrinho é mais bonitinho, vou retornar esse status code. Não. Massa, veja o código no Iana. Por favor, pelo bem da nossa amizade. Então, vamo lá.

**[01:00:22]** Então, de todos eu separei alguns pra gente ver, né? A gente já falou sobre vários, né? 200 OK que deu certo, 201 que criou, 404 não deu bom, não achamos que você tava pedindo. O 422 é quando você mandou a coisa, mas mandou errado. Sabe tipo assim, ah, manda aí pra mim seu nome, seu nome é um texto. Aí você vai falar tipo assim, pô, mandei um número. Qual que é o seu nome? 7. Aí ele vai falar, pô. Caramba, mano, era pra ser um número.

**[01:00:49]** Era pra ser um nome, não era pra ser um número, né? Então, esse é o 422. E a gente tem o interno servererror, que é o 500, que é tipo assim, toda vez que a gente fizer caca, vai dar 500 na nossa aplicação. Massa?

**[01:01:10]** explicando no meu trabalho, que estou tomando decisões com base em imagens ligadas. Muito bom. Então, por padrão, aí agora vem partes importantes do Festa API. Por padrão, o Festa API sempre retorna 200 OK. Sempre. Sempre, sempre, sempre.

**[01:01:31]** E aí você pode falar isso, né? Porque a gente tem uma regra no Python, né? Que explícito é melhor do que implícito. E aí você pode falar pra ele, olha, status code aqui, ó. Vai retornar 200. Aqui dentro do bagulhinho, do fecha IPA aqui, ó. Pera aí, deixa eu diminuir aqui, meu... minha fonte aqui ficou imensa. Status code, aí você pode falar, olha. Retorna 200. Massa. Se você falar que retorna 201 aqui, toda vez que você rodar aqui, sei lá, o barra aqui...

**[01:02:03]** Ó, ele retornou 201, created. Se você retornar qualquer coisa aqui para ele, ó, é 404. Retornou, 404, not found. Ou seja, você consegue dizer para o Fast API exatamente o que está acontecendo aqui, o que está rolando, de onde vem, para onde vai, e tudo mais. Então você consegue especificar isso aqui. Aí você fala, bom, esse retorna 200, né, porque um get sempre dá certo. Em teoria, o get sempre dá certo. Então a gente pode vir aqui, então, from HTTP do Python em portes, sei lá.

**[01:02:37]** import http status e aí você pode falar aqui de uma forma mais bonita né ok massa ou seja toda vez chamar essa rota o retorno é 200 ok deu nice legal chamou 200 lindo maravilhoso incrível massa então esse é o 200 ok

**[01:03:06]** Um outro, uma outra coisa, né? A gente discutiu bastante sobre HTTP, mas a outra coisa que ficou faltando aqui é o HTML, né? E o HTML é a coisa mais fundamental da internet. Sem HTML, a gente já vê as mensagens assim, né? Imagina se eu mando uma mensagem e volto isso aqui pra você. Um JSON muito louco. Não, né? Um dicionário Python, sei lá, se chama isso aqui do que você quiser. Por enquanto.

**[01:03:39]** Saca, imagina, você requisita a página, então o HTML é o que faz essa coisa ficar bonita assim, né? Ficar estilosa assim, sabe? Conseguir ver as mensagens, o cliente consegue entender o que foi respondido pra ele. Então essa é a ideia do HTTP. Ou do HTTP, não, do HTML. Desculpem. Então o HTML é uma linguagem de marcação, né? HT de hypertext, lembra? HTTP.

**[01:04:11]** HTTP faz o quê? Transporta hipertexto. E aí, o HTML é a linguagem de marcação de hipertexto. Então, basicamente é isso. Então, o HTML é aquela coisa, né? Tipo assim, eu acho que não vai falar muito sobre HTML, mas é tipo, você fala, ó, é um arquivo HTML, tem um head, né? Tem um cabeçalho, tem um corpo, tem...

**[01:04:34]** Títulos, tem parágrafos, a gente renderes imagem e tudo mais. Aqui eu estou citando HTML porque ele é o padrão das coisas. Aí perguntaram se Python faz isso ou usa JavaScript. Não, mano, Python é Python. Por que eu usaria JavaScript por baixo? Mas tudo bem, não faz sentido isso. Tipo assim, é Python respondendo requisições, recebendo e tal. Não tem nada de JavaScript aqui no meio, não. Legal, então a gente faz isso aqui.

**[01:05:04]** Mas lembrando, a gente tá vendo, é pra estudo, a gente não vai usar HTML no curso, mas a gente poderia fazer isso se a gente quisesse. Olha que lindo, que maravilhoso isso aqui. Basicamente, se eu tivesse uma outra função aqui, eu vou mudar o nosso ReadRoot aqui. E aí aqui...

**[01:05:25]** uma coisinha que a gente tem aqui, esse Response Class. Por padrão, lembra que o Response Type do FastAPI é sempre um JSON? Então a gente poderia mudar aqui o Response Class e falar que ele vai retornar pra gente um HTML. Então a resposta vai ser HTML não JSON, que é o padrão que a gente sempre retorna. Então você poderia vir aqui e falar o seguinte, olha, From FastAPI...

**[01:05:51]** Ponto Responses importe HTML response. Só para a gente falar, olha, isso aqui está especificamente respondendo o HTML. Por padrão, Fecha IPI sempre retorna aquele adicionário, JSON, aquela coisinha bonitinha. Mas aí, basicamente, tem que aparecer. Olá, mundo no título da página, ou seja, na barrinha. E aí tem que escrever Olá, mundo em título, né? H1. Vamos ver o que que rola aqui. Ó, o servidor já restartou aqui.

**[01:06:21]** Então, vamos lá. Localhost 8000, que é o lugar onde a gente está, no barra Olá Mundo. Maravilhoso, não? Aqui, se você ver aqui, nosso Olá Mundo, que era o que estava no título. Então, o Fashion API também consegue trabalhar com HTML, consegue trabalhar com templates e várias outras coisas, mas não vai ser o nosso foco principal aqui dentro desse curso. Mas se você precisar fazer isso, você pode e dá para fazer.

**[01:06:52]** Não definindo HTML dentro do return, mas tudo bem. Funciona, tá ligado? Mas não faça isso. Procure por templates. E aí, se vocês quiserem se aprofundar mais nesse assunto, lá no curso, lá no curso em texto, tem o lugar aqui que tem os apensas. Aqui, ó, próximos passos. Pra quem tiver curiosidade sobre isso, existe uma coisa sobre templates aqui. Ah, como é que roda o arquivo HTML? Como é que eu coloco os...

**[01:07:20]** o style css como é que eu faço pra definir tem plates tem tudo aqui o nosso curso não vai falar sobre isso é só sobre json mas tá tudo aqui todas essas coisas estão disponíveis aqui a sério obrigado pelo super chat mas estamos junto valeu ele falou só pra agradecer to migrando o php pleno pra pai tão pleno seu conteúdo me ajuda muito também estou começando a criar conteúdo pra dev pô tamo junto meu que isso depois manda o link aí pra nós

**[01:07:50]** lá no grupo do Telegram, para a gente saber. Então, a gente faz esse tipo de coisa aqui. Olha que massa! Então, tem suporte a HTML aqui. Só que, como eu disse, um passo para trás. Embora o HTML seja um dos pilares principais da web, a gente não vai usar ele aqui no curso. A gente vai falar só sobre API Geizon. Não é tipo assim. Embora o HTML tenha sua importância, ele...

**[01:08:26]** Tem essa coisa de estilo, mostrar as coisas, como o cliente vai renderizar os dados, a gente não vai falar sobre isso. Não é o foco do nosso curso, mas é possível. Mas... E o que é que acontece, né? A gente tá falando de Fast API, e aí o que é Fast API, né? Fast é de rápido, né? E a PI que raios é a PI, né? A PI significa Application Programming Interfacy.

**[01:08:51]** bonito, né? Como diria Luciana Gimenez. E aí o que que rola aqui, né? APIs, quando você pensa em interfaces, são formas de se comunicar com outras coisas, né? Então, application, interface. Então, são formas de se comunicar com uma aplicação e programing, né? Porque você programa essas interfaces, né? Então, é mais ou menos esse esquema. E aí o que que rola? Pra quem quiser saber, ah, o que que é um API, por exemplo? Uma API

**[01:09:23]** É uma forma como você abre uma porta, por exemplo. Vamos pensar que a porta é um software. E aí você vai falar, preciso abrir a porta. Então toda a porta tem um, sabe, uma interface por onde a gente interage com ela. Tem uma maçaneta, tem um buraco de chave, onde a gente gira a chave, tem um mecanismo ali dentro. Então as interfaces são uma forma como a gente vai interagir com a aplicação.

**[01:09:50]** Massa, e quando a gente está falando sobre APIs, o app, basicamente, é tudo aquele conjunto de coisas que a gente falou. Então, HTTP, URL, HTML, JSON, hypertexto, sabe? Todas essas coisas definem uma interface, um protocolo padrão por onde a gente conversa com esse tipo de coisa.

**[01:10:15]** Massa, então dá pra fazer esse tipo de coisinha aqui. A raiz perguntou se retorna a outros formatos, você pode customizar da forma como você quiser. Não necessariamente vai ter um protocolo, um application, um content type, porque você quer, mas sempre tem. Você sempre pode customizar das coisas. Então, legal. Modernamente, né, a gente diz que a PS trafega um JSON, né? E JSON é esse esquema que a gente viu aqui, né, de...

**[01:10:45]** Traficar essa coisa que tem chave e valor, né? Que em alguns lugares a gente chama de hash map, em JavaScript a gente chama de objeto, em Python a gente chama de adicionário. Então o JSON é essa coisa, né? É uma notação de objetos JavaScript. É um padrão da web, basicamente, para traficar e trocar dados. Ou seja, a gente não troca como a informação vai ser marcada, como ela está sendo apresentada na web, a gente costuma usar só o dado que a gente quer trocar. Ou seja, qual é a mensagem que eu estou emitindo aqui?

**[01:11:16]** Olá mundo, é isso. Qual que é o CPF? Qual que é o não sei o que? Qual que é o não sei o que é lá, sabe? São coisas pequenas e simples que a gente pode mandar de uma forma simples aqui. Então, é só troca de dados, né? Então, é mais fácil descrever, é simples de interpretar, de gerar com máquinas, né? Mas o cliente não sabe ler isso e 90% dos casos.

**[01:11:44]** E... E aí, o que que acontece? Erroneamente aqui, hein? E aqui eu quero que você expresse atenção no que eu vou falar aqui, para ninguém sair me corrigindo depois. Erroneamente, a gente chama APIs que trafegam JSON de API REST. Mas para ser uma API REST, precisa se trafegar HTML. Precisa se ter HATOAS, que é Hypertext.

**[01:12:13]** As the engine of the application state, ou seja, o estado da aplicação é definido por hipertexto. Então, para ser REST, precisa ser HTML. Então, API.json não é REST. API.json troca dados, RPC, comunicação de máquina. Massa? Então, legal. O termo original para APIs REST é com HTML. A gente não vai fazer uma API REST, a gente vai fazer uma API que trafega

**[01:12:42]** JSON. Massa, legal. Então, é esse o esquema que a gente quer aqui. Uma API que não é REST, uma API que trafega JSON.

**[01:12:54]** E aí? E aí que entra esse negócio de modernos, né? Porque quando a gente fala de API moderna, tudo retorna a Jaze. Ah, retorna a Jaze não pro front. Tipo assim, legal, é uma forma, trafega menos dados, trafega esse tipo de coisa dentro dessa estrutura, dentro dessa anotação. É legal porque é leve, é menor, funciona bem, a gente vai de lá pra cá. Mas não é muito legal, né?

**[01:13:17]** Saca, mas assim, não é muito legal quanto o HTML, que o cliente lê e renderiza e tudo mais, é só troca de informações mesmo. Então, é esse esquema aqui. E aí, esse é o JSON. Vamos olhar um JSON que não seja lá no mundo? É mais ou menos isso aqui. Então, imagina que eu falei, tipo assim, ah, me vê todos os livros escritos por Selinger e Bugakov. Saca, pedindo no sistema da livraria.

**[01:13:45]** Aí ela falou, olha, temos um objeto aqui, ou seja, objeto J-Zone, que é esse, abre fechas aqui, e aí tem uma chave chamada Livros, dentro dessa chave tem uma lista de coisas, e aí você vai falar, olha, tem um livro que é título, apanhador no campo de Senteio, o autor é o Salinger, o ano é 1945, e está disponível, esse a gente não tem, matar no catálogo. E a gente tem o outro, que é o Mestre Amargarida, do Mikhail Bugakov,

**[01:14:15]** 1966 e tá disponível. Massa! Então é só coisa aqui. Esse é o JSON, essa é a estrutura. Você tá vendo que não tem qual é o título? Qual é no seu quê? Saca, aonde tá? Isso aqui é um header, isso aqui é um body, isso aqui é um parágrafo, não tem nenhuma especificação de qual é o estado que a coisa vai aparecer no browser. Então por isso a gente usa JSON. Quando a gente não precisa trafegar...

**[01:14:43]** a estrutura da página e sim só os dados. Pra gente isso aí. Vai falar, REST seria tipo um... com templates de india? Sim, porque no final você vai retornar HTML estruturado, né? Vai seguir hate-oas, pode ser HTML, pode ser... Jinja, pode ser esse tipo de coisa. Eu adorei essa coisa do Randall... que o Randall Trice mandou.

**[01:15:08]** Mas tá em falta. Adorei, né? O livro do do Salinger aqui. Então, essa é a cara do Jason. Então, a gente trafega dados de A pra B ou de B pra A e assim a gente vai trocando. Ou seja, o cliente pegou aquela URL e mandou, ó, eu preciso dos dos livros, tá? Não sei o quê, tá? A gente recebeu essa resposta aqui que tem um content type Jason. Mas tem, mas acabou, ótimo.

**[01:15:33]** Então, legal. Quando a gente fala sobre essa estrutura de conversar sobre Jason, o Jason, por isso ele não tem o formato da coisa, sabe? Você não tem uma hierarquia, uma coisa que o cliente vai saber ler, a gente costuma firmar contratos entre o cliente e o servidor. E aí a gente fala, olha, quando você, quando eu te mandar, ah, você volta pra mim e...

**[01:16:01]** O que eu vou te colocar aqui vai ser uma coisa mais ou menos nesse formato, ou seja, tem uma chave Livros, dentro da chave Livros tem uma lista, dentro da lista tem...

**[01:16:11]** esses campos, título, autor, ano e disponível, e o título é sempre uma string, o autor é sempre uma string, o ano é sempre um inteiro, o disponível é sempre buliano. Saca, então é essa coisa. Chegou a burocracia, é muito bom, né? Então, a gente costuma fazer contratos, porque como o cliente não vai conseguir renderizar o que a gente vai mandar, eu tenho que especificar ou documentar, ou até versionar a versão de como a gente trafega e conversa sobre isso aqui, né?

**[01:16:39]** Então, é para isso que entram os esquemas. Sabe, aquele esqueminha, tipo assim, no esquema, é exatamente isso. Quando eu mandar isso, você vai me retornar a isso. Ou melhor, o servidor está falando, olha, segundo a minha documentação, quando você me mandar uma lista de livros, te retornarei dessa forma. Então, o cliente sabe o que esperar, já que ele não consegue renderizar, porque não é um formato padrão. Mas, é isso que significa um contrato.

**[01:17:09]** E aí, pra fazer os contratos, a gente usa uma biblioteca Python chamada ByDentic.

**[01:17:14]** e pai Dantic vende pedantic, né? Tipo assim, traduzindo para português, é pedante, é alguém que é chato com burocracia de esquemas e contratos. Então ele vai documentar a nossa API a partir dos dados que a gente fornecer para ele, mas ao mesmo tempo ele vai ficar validando, falou, ó, você me mandou o ano e escreveu o ano assim?

**[01:17:40]** 1.945? Para, né? Não. Não é assim. Eu falei que era inteiro. E aí, se não foi inteiro, ele reclama. Saca, então? A PI é pedante. Ela é documentada, mas ela é chata nesse sentido. Então, isso vai trazer essa coisa do esquema, né? De documentar como a forma da coisa vai ser relacionada, o que que o servidor recebe e como o servidor.

**[01:18:10]** retorna, saca? E aí dentro desse esquema ele vai fazer a documentação, viu o padrão OpenAPI que a gente viu lá no Swagger, viu no Redock, mas a gente vai ver de novo. Porque sim. Então, legal, aqui dentro do nosso projeto eu vou criar essa... por extenso até vai, agora imagina inúmeros romanos.

**[01:18:35]** Adorei, Pedro. Então, a gente vai criar um arquivo dentro do nosso projeto. Se você usou FastZero dentro do FastZero e tudo mais, dentro da pastinha do projeto aqui dentro, deixa eu voltar para aqui do jeito que eu estava antes. E eu quero deixar aquele OK aqui, pera aí. Então, a response, o que que eu tinha deixado aqui? Status Code. E aí o Status Code é HTTP.

**[01:19:06]** status.ok. Massa, então foi aqui mais ou menos que a gente tinha parado o nosso código, né? Então aqui dentro eu vou retornar o seguinte, dentro da nossa pastinha, onde está o app no mesmo nível aqui, eu vou criar um novo arquivo que se chama esquimas.py. Ah, por que que não faz o mesmo arquivo? Não sei. No dia eu achei que seria mais legal criar em outro.

**[01:19:31]** É basicamente essa resposta aqui nesse primeiro momento. E a gente vai importar o paydentic aqui. Aí alguém vai me perguntar, precisa instalar o paydentic? Não precisa, porque quando a gente instalou o Fast API Standard, o Fast API padrão, ele instalou essa biblioteca que se chama paydentic. E aí agora a gente vai pegar essa coisinha aqui, né? Vamos olhar para ele. Então, from paydentic import base model.

**[01:19:58]** Ou seja, a gente vai criar, a gente vai... tem um modelo base. E a partir disso aqui, eu vou falar que a gente vai criar um... documentar um esquema de troca de mensagens aqui. Então, eu vou falar o seguinte, olha. Existe uma classe que eu vou chamar de Message Class. Message. E ela é um BaseModel. Basicamente isso aqui. Aí, a partir disso aqui, eu vou falar, olha. Toda vez que essa mensagem estiver envolvida na documentação, ela tem que ter uma chave.

**[01:20:26]** E essa chave é message. Message. E o tipo do dado que vai ter que vir na mensagem é uma string. Massa! Então aqui eu já comecei a burocratizar a coisa.

**[01:20:41]** Eu não retorno mais isso aqui, mestre Jolamundo. Eu retordo um esquema de mensagens, um contrato de mensagens, que tem uma chave mensagem e que tem um corpo de texto que vai vir ali dentro, né? Então, a chave sempre vai ser essa e o valor sempre vai ser desse tipo, embora ele varia de coisa pra coisa, né? Massa, né? E... fez sentido isso aqui?

**[01:21:11]** O pai dente seria apenas para documentar, caso eu vier fora do padrão, a própria função retornaria. Mano, ele não documenta, ele documenta, ele valida tanto a entrada quanto a saída, a gente vai ver algumas coisinhas aqui. Mas então chegamos aqui, temos essa mensagem aqui. Antes da gente colocar isso no código aqui, eu não sei se eu coloquei aqui. Beleza, eu já coloquei, mas eu vou ignorar meus slides agora por enquanto.

**[01:21:37]** Eu vou subir nossa aplicação, a nossa aplicação tá rodando aqui, porque ela nunca para de rodar. E eu odeio colocar nesse show porque ele vai quebrando, né? Então deixa eu ir pra lá. CD, Git, Fast, API... Zero. Aqui onde a gente tava. LES. Legal? Deixa eu matar esse servidor aqui. Porque eu não consigo ficar vendo aqui o que ele tá fazendo. É muito pequeno pra mim. Então legal. Aí eu vou rodar aqui, então...

**[01:22:10]** para rodar o servidor. Legal, ele está servindo aqui e aí eu quero ir com vocês lá na documentação, então localhost 8000. A gente está no olamundo, deixa eu dar um docs aqui para a gente ir lá para o Swagger, aquela pagineta que a gente tinha aqui. Olha o que que acontece quando a gente entra aqui. Você vai ver que ele fala, olha, quando retornar 200 vai retornar 200, porque é o padrão do Fast API. Ele retorna um status de sucesso, o tipo é application JSON.

**[01:22:39]** E o valor de exemplo é uma string. Você sabe que a gente não está retornando uma string, né? Você sabe? Isso aqui não é uma string. É um objeto, um objeto JavaScript, não é? Um JSON ou um dicionário dentro do Python. Mas ele não documenta isso. Mas quando a gente envia, funciona, ó. Massa, bala, pinga. Mandei aqui, execute. Ele falou, fiz isso aqui, aceita JSON. E ele trouxe aqui.

**[01:23:07]** Olá mundo, mas o resultado esperado era string, não era isso aqui. Então é aí que a gente começa a documentar a coisa. Vamos lá, eu vou falar o seguinte, vou quebrar tudo aqui direitinho. Só para a gente ter várias coisinhas aqui, várias linhas para ficar mais explícito. Então a gente tem esses status code e é aqui eu vou falar o seguinte, response model. E eu vou falar que ele vai retornar o message, que é essa coisa que a gente...

**[01:23:42]** Colocou lá no esquimas e aí eu vou importar ele aqui dentro, né? Então, sei lá, FromFestAPI0.schemas import message, aquela mensagem que a gente tinha ali. Como o servidor está em modo de desenvolvimento, ele restartou aqui, né? Ele deu erro, mas a gente rodar de novo, porque eu salvei antes de colocar. Agora, vamos voltar lá no docs e ver o que acontece aqui, vou dar um F5.

**[01:24:10]** Agora ele está falando do seguinte, olha, 200 vai dar ok essa resposta, só que o tipo da coisa é message string, tem um esquema aqui, tem um objeto chamado message dentro da minha resposta, que tem uma chave message, que é obrigatória, por isso tem esse asterisco aqui e vai voltar sempre a uma string, ou seja...

**[01:24:34]** Agora a gente está dizendo para o cliente, quando ele chama essa parada, a gente vai receber esse esquema. Massa, né? Então a gente acabou de documentar como isso vai funcionar. E aí, se a gente mudasse aqui, o created, que é o 201, quando a gente roda a documentação, ele muda aqui também, a code 201. Então a gente fica linkando uma coisa com a outra aqui. Então tudo o que a gente escreve aqui fica documentado lá.

**[01:25:07]** E aí, vamos fazer um teste aqui, vamos retornar uma coisa que não é isso aqui. Vamos retornar a senhora returning 123. E vamos ver o que acontece aqui, ó, a aplicação já subiu de novo, tal. Vamos rodar e ver o que acontece. Try it out, execute. Ele deu um internal server erro, ou seja, deu 500. E ele falou o seguinte aqui, olha, o pai dente que deu erro.

**[01:25:34]** Ele falou, FastAPI Inception Responsive Validation Error. Ele falou, olha, a nossa resposta devia ser um dicionário. Aqui, ó, input should be a value de dictionary ou object to extract fields from. Aí o que a gente enviou foi o input 123. Então não tem, não tem a estrutura que a gente combinou que é retornar para o cliente. Então deu 500, deu erro interno na nossa aplicação. Se a gente retornasse um objeto, qualquer...

**[01:26:00]** que tivesse o título errado aqui, né, a chave errada mensagem em português. Blá. Renunciou aqui, subiu de novo, se eu rodasse agora, ele deu outro erro 500. Ele falou o seguinte, olha, lá no campo era para ter um campo chamado message na resposta, mas veio um mensagem. Então tá errado. Você não tá cumprindo o contrato que você deu com a pessoa. Então ele faz também a validação do dado. Isso é muito foda.

**[01:26:34]** Então, ele não deixa a gente enviar informações erradas para o cliente. Ele cria esse acordo, esse esquema e faz exatamente o que a gente queria. Que isso seja respondido aqui. Olá mundo, então retornou certinho. Muito massa, muito massa. Quando colocar API em produção, vai ficar rodando no terminal, vai ficar rodando no terminal, lá do servidor. Pai Dante, que nesse caso está fazendo o que o Marshmallow faz na definição de contrato sim? É...

**[01:27:10]** É a mesma esquema do marshmallow aqui. Faz a mesma coisa. Legal? Aí o germano falou, dá pra colocar message, message olamundo. Também daria pra fazer assim. Também daria pra fazer um objeto, né? Mas como a gente tá falando de JSON, eu vou deixar isso aqui pra depois. Mas você poderia falar o seguinte. Chave, message, pay. Você poderia fazer desse jeito. Com um objeto do pai dente que respondendo.

**[01:27:39]** Não é muito nossa praia agora, mas é isso. Funciona dessa forma, ele documenta e a gente traz esse esquema pra cá. Se você quiser mudar isso aqui, né, esse Fast API que fica aqui em cima, você quer dizer falar, minha API top, você pode mudar aqui, tá aí, tô aí e falar, minha API bala.

**[01:27:59]** Aí ó, aí ele troca aqui também. Então, tudo que você escreve lá, ele vai trocando aqui e vai entrando na documentação. Tanto que esse read-root que tá aqui é também o nome da função. Se a função fosse read-root batatas, tá aqui ó, read-root batatas. Então, a gente faz esse tipo de coisa, a gente vai conversando e trocando ideias dos dois lados. Massa! Lucas, obrigado mano pelo teu super chat. Fez um programa do Dormelhor. Pô, tamo junto, ele, valeu. Obrigado, mano.

**[01:28:33]** Legal, então essa é a parte do FastAPI, essa é a ideia que ele tem aqui, né? Então você vai combinando ele e ele vai validando os dados e vai fazendo as coisas, vai documentando, vai dando a estrutura dessas coisas que a gente precisava lá no Swagger. Aí você pode ir lá no Redock e no Redock também fica do mesmo jeito, bonitinho aqui. Em vez de Docs, localhost.redock aqui.

**[01:29:02]** Ele ficou aqui ó, minha API bala, e ele falou aqui ó, a resposta disso aqui é o message string, sempre aqui, que a gente chama esse local host. E ele fala aqui ó, message is required, string de message tal, application JSON, ele dá todas as explicações aqui na documentação pra gente fazer esse contrato né, como alguém falou lá, vem a burocracia, e é exatamente esse o estilo, o extinto da coisa que a gente quer aqui dentro. Massa!

**[01:29:35]** Então, legal. Perguntas? Juntem as perguntas agora para a gente conversar enquanto a gente finaliza essa coisa da aula aqui. O exercício de hoje é que vocês criem um endpoint, ou seja, isso aqui, uma coisinha dessa aqui, um lugar onde a gente possa bater aqui, ou seja, um get em algum lugar.

**[01:30:11]** que retorne olamundo usando HTML e que você vá lá no arquivo testes.testapp e cria um teste para isso aqui. Ou seja, é para criar uma nova rotinha aqui, um novo recurso de Get que retorne HTML. Tem que retorna HTML. O HTML tem que ter a mensagem olamundo e vocês têm que testar.

**[01:30:42]** esse esquema. Ficou claro o que é pra fazer no exercício? Ou seja, é simplão, é criar uma nova rota, uma coisa dessa aqui, que retorne HTML, e esse HTML tem que ter olá a mundo e a gente tem que testar esse esquema. Se não ficou muito claro, por favor, falem comigo. Legal, então é basicamente isso aqui que a gente tinha aqui dessa coisa de converter pra documentação e tudo mais. E aí tem o quiz.

**[01:31:16]** Não esqueçam de ir fazer o quiz. Tem muitas perguntas aqui. E isso são perguntas relacionadas com o que a gente viu hoje, né? O que que é o modelo cliente servidor? O que que é o uvcorn? O que significa o RL? O que que você faz com as... quais são as opções do RL? Qual campo não tá no cabeçalho? O que que o verbo pute faz? Saca? É... É esse esquema aqui. Legal?

**[01:31:46]** Então responda um quiz, faça um exercício, o exercício está aqui na aula 2, que é a aula 0,2. Tem a descrição aqui do exercício do que precisa se fazer aqui. Massa? Então, legal. Lembrando que eu vou responder perguntas sobre a aula, porque não tem sentido a gente ficar desperdiçando o tempo de quem tem que aguardar a cedo amanhã, tem criança para botar para dormir. Então, legal.

**[01:32:19]** Por aqui a aula acabou, ó, já vou avisando já. Por aqui a gente chegou no fim do que a gente queria aqui, eu vou responder as perguntas, se tiver perguntas em vi, quem quiser descansar por favor, tá liberado. Da aula. Aí perguntaram se dá pra usar a classe, não. O framework é um framework de funções. Se você quiser usar a classe, usa outro framework. Até dá, mas acho que assim, não é ideia. Aí o Pedro perguntou se tem como...

**[01:32:48]** Tem como proteger a documentação. Tem, dá pra desabilitar também. Não precisa... Não precisa desse esquema aqui. Sem testes hoje. O teste que a gente tem passa, mano. Vamos rodar o teste. Aqui. Poetry run task test. Ele deu erro nos imports aqui, então deixa eu dar um format. No run test. Espera aí, o que que aconteceu aqui? Was never import... Ah, beleza. Eu tô no lugar errado, aí não roda mesmo.

**[01:33:30]** Pronto, o nosso teste está passando aqui. Porque a gente não mudou nada, né? A gente só documentou o que precisava, né? O nosso teste está funcionando. Do jeitinho que a gente fez. Então, vamos lá.

**[01:33:59]** Não sei porque eu estava pensando que o FESIPR é só para back-in, mas pode conseguirmos fazer pras no app dentro da função. Isso é o usual. Não, não. Então, Lucas, eu tinha mandado aqui uma parte, aqui tem uma pênsica aqui no material de texto aqui, que eu falo sobre como usar templates, Jinjas, CSS e tudo mais. Então, está aqui. Quem quiser dar uma olhada depois, a gente não vai falar sobre isso no curso, mas está tudo aqui. Tem uma forma de fazer isso funcionar e tal. Então...

**[01:34:28]** Tá documentadinho aqui. Ah, então legal. Deixa eu ir voltando aqui. Deixa eu voltar pra gente responder as coisas. A forma de usar os verbos é só pelo decorador, sim. É a forma padrão de usar. Se você quiser fazer de outra forma, tipo assim, mano, vai pra outro framework, a ideia desse é essa, tá ligado? Tipo assim. Ah, eu quero fazer com classe, eu quero fazer tipo, mano, vamos seguir a regra do framework, tá ligado?

**[01:34:59]** Para quê, saca? Você pode criar objetos que passam... Clássido ainda faz um pod também. Melhor para você. Quem é isso? Obrigado. Me senti até... Feliz aqui. O exercício da reprodução do curso é uma mesma coisa, mas pode deixar tudo misturado ou é melhor criar duas aplicações separadas. Não! Essa é uma pergunta importante que o Hess fez aqui. O exercício faz em outro lugar? Não, o exercício faz parte do curso. O exercício faz parte do projeto do curso.

**[01:35:31]** Por isso que eu falei, lá dentro do app cria uma parada, dentro do arquivo de testes, faz esse rolezinho. A ideia é essa. A ideia aqui é que todo exercício seja feito dentro do projeto do curso. Lá na frente você vai ver que tipo assim, eu vou mandar mudar uma coisa que a gente fez na aula anterior. Então a ideia é que tudo fique dentro do esquema. Massa. Muito legal a documentação inclusive. Pô, é muito massa mesmo.

**[01:36:07]** aqui mais que a gente tem aqui. Deu fazer testes usando Postman, usando Docals ao Postman. Os testes, mano, você faz usando testes. Tipo assim, eu sei que pareceu grosso da forma que eu falei, mas tipo assim, pra fazer testes a gente faz escrevendo testes da forma como a gente fez aqui, né? Tipo assim, vem aqui, vai lá no teste, escreve uma parada e testa.

**[01:36:32]** É assim que a gente vai testar a aplicação. É que hoje a gente não mudou nada, então por isso a gente não escreveu teste. A gente veio aqui, reformulou algumas coisas, porque eu precisava explicar alguns conceitos de web. Mas tipo assim, a ideia é que tirar o suegro da sua vida, tirar o postman da sua vida, insone, HTT-PAI, não.

**[01:36:51]** O mesmo tempo que leva para você fazer um request no postman, leva para você escrever três linhas de código e deixar testado para sempre. Então, vamos colocar isso aqui no teste. Du, para que serve os apentes? Apentes são coisas extras. Não tão necessariamente ligados com material, mas são algumas coisas extras. Tipo assim, tem um apente de instalação, de versões que a gente usou, um...

**[01:37:19]** com algumas outras coisas, mas tipo assim, são informações extras que não fazem parte do escopo do curso, mas elas estão lá porque tem alguma relevância dentro do assunto. Como que debogo um teste? A gente vai ver isso quando a gente for escrever testes porque eles vão dar errado e vão dar muito errado. O Dave perguntou qual é a diferença do Yuvicorn para o Nginx. O Nginx é um servidor web. Ele é feito para servir páginas da HTTP, fazer proxias, reversos e tudo mais. O Yuvicorn é um servidor de aplicação.

**[01:37:52]** é um servidor que serve a aplicação python ele não é um servidor web massa o luiz falou 130 17 likes tenho certeza que ela tão boa que a galera até esquece obrigado aí por lembrar luiz deixe um like nos de embora massa então para finalizar aqui deixa tudo bonitinho eu vou só dar o nosso comit aqui para subir aqui adicionando

**[01:38:26]** esquema de mensagem, é só isso que eu vou fazer aqui. Então, git add ponto, git commit adicionando o esquema de mensagem, git push. Fechou aqui. Vamos embora. Olha como eu sou legal. Liberei mais cedo, hein. Liberei mais cedo hoje, hein. Que professor bom esse, hein.

**[01:38:58]** Aí perguntaram se eu posso falar sobre a questão do REST. Mano, entra lá no grupo do Telegram, Leonardo. Isso, mano, gerou uma discussão imensa lá. Mas a gente pode, basicamente, quem inventou o termo REST, né? Foi uma pessoa numa tese de doutorado, né?

**[01:39:16]** um acadêmico e pra ser REST precisa ser hatoas, né? Precisa ser hipertexto como a engine de troca de mensagem. Então, pra ser REST, tem que trafegar HTML. Essa é a definição original. Se precisar, eu mando... eu mando... mais informações, links lá no grupo e tal, se vocês quiserem. Mas, basicamente, é a tese de doutorado do Roy, né? Aqui. Então, vamos lá.

**[01:39:46]** Roy Rest. Aqui ó, é o Roy Fiderman. É, eu escrevi ao contrário mas tudo bem. Aqui deve estar a dissertação dele. Cadê, cadê, cadê, cadê, cadê. Ah... Presentation, tal, tal, tal. Mano, em algum lugar tem que ter essa informação do Roy aqui. Aqui ó, essa é a dissertação do Roy em PDF. Se alguém quiser depois, tá aqui. Eu queria pegar aqui de um lugar...

**[01:40:44]** que eu fizesse mais sentido, aqui tem HTML, mas também não tá abrindo, mano, não tá abrindo! Eu quero ver a dissertação do Roy, mas é isso aqui, aí ele vai explicar por que que REST precisa ser HTML. Legal? A boa prática é fazer teste into-end no fast.jp, roda a aplicação e fazer os testes por request, não. Teste into-end você faz fora da aplicação, você não faz dentro da aplicação, você faz fora. Então...

**[01:41:14]** É cada um, cada uma. Depende de como você quer fazer, como você quer subir. Cara, não tá carregando aqui o esquema do Roy. Aqui estão só os capítulos 5 e 6 do Roy, em que ele vai falar sobre rest e tal. Mas eu queria que carregasse os links da universidade aqui, não carregam, mas é isso. Se quiser, a gente continua debatendo isso lá no grupo. Bom, eu vou lá um beijo pra vocês, a gente se vê na quinta-feira.

**[01:41:48]** e é isso beijinho para vocês e tchau tchau

