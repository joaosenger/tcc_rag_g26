# Transcrição da Aula: aula-01.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:08]** Olá pessoas, boa tarde, boa noite no caso, ou bom dia, dependendo do horário que você está vendo isso, a internet não tem horário, né? Mas tudo bem, eu sou o Dono Sauro, para quem não me conhece, olá, e eu queria ver com vocês um feedback antes da gente começar, se o som está legal ao seu vídeo, se vocês estão me ouvindo, se vocês estão me vendo, às vezes não está nada funcionando, eu fico falando sozinho aqui, antes da gente começar. O River já falou que o som está maneiro, então significa que a gente pode começar.

**[00:00:39]** Massa? Então, bom. Sobre o que a gente vai conversar hoje, né? Essa é uma live sobre o curso de Fast API, né? São de 2025. E a gente vai configurar o nosso ambiente hoje. Eu queria dizer de antemão, assim, de verdade. Quem nunca configurou um ambiente Python e tá aqui, levanta a mão aqui no chat, por favor. Eu quero dar uma mensagem especial para você. Pessoinha amada.

**[00:01:13]** Talvez essa live seja mais complicada do que de costume. As coisas costumam dar errado em alguns determinados momentos, em que a gente não prevê. Para quem nunca configurou o ambiente, às vezes é meio cansativo, é meio desgastante.

**[00:01:28]** São muitas ferramentas e pra que serve isso, pra que serve aquilo? A gente vai passando por isso junto, sem problema, não esquenta com isso. A gente tem o grupo lá do Telegram pra tirar as dúvidas, pra gente conversar direitinho, então não fica com essa parada, tipo assim, nossa, deu errado, vou desistir. Às vezes isso é um pouquinho chato, às vezes demora um pouco, então pra quem nunca configurou um ambiente, sabe, isso aqui é meio...

**[00:01:55]** Além de ser tedioso, porque são muitas coisas, às vezes dá um desespero, porque as coisas começam a dar errado. Então, calma, a gente vai junto, tá bom? Eu queria deixar essa mensagem de acalanto, sabe, um abraço, pra gente começar isso junto, às vezes é complicado. Então, não desista. Pra quem tá no esquema com a gente, tem aqui, né, o livro texto, ou qualquer outra coisa que o vale aqui, com tudo o que a gente tá falando, então, você preferir dar uma lida...

**[00:02:27]** Sabe? Às vezes a gente apanha um pouco, então tem bastante coisa aqui, tem bastante insumo, vale a pena dar uma olhada. E perguntando, ir no grupo, ir no... Sabe?

**[00:02:39]** importante aprender erra é sim foi o que o que o andré deixou aqui né sim isso é importante mas isso aqui é uma coisa que costuma ser um pouco mais tediosa mesmo e às vezes dá errado então não fala nossa sabe no passado eu ficava olhando isso aqui falava nossa mas acho que eu sou muito burro mesmo porque eu não consigo reproduzir o ambiente do jeito que as pessoas fazem sabe e aí eu sei que isso é um pouco chato e desgastante mas vamos vamos junto

**[00:03:06]** Então, sobre o que a gente vai falar de fato nessa aula, né? Agora que eu já dei minha mensagem e meu abraço, hoje a gente vai configurar o nosso ambiente de desenvolvimento. E quando eu digo configurar um ambiente de desenvolvimento, é instalar as ferramentas que a gente precisa para que tudo funcione. Como é que a gente gerencia um projeto Python? Que ferramentas que a gente coloca para gerenciar o ambiente, para...

**[00:03:32]** formatar o código para rodar os testes, para automatizar comandos, que configuração que a gente faz, então é sobre isso que a gente vai falar e criar um ambiente que consiga ser singular para todo mundo, para que a gente possa um ajudar, sabe? Fala aqui, pô, germano, deu erro aqui, e aí a gente troca a ideia, sabe? E aí a gente vai todo mundo junto no mesmo ambiente, saca? Aí depois a gente vai falar sobre a instalação do FastAPI e as dependências, né?

**[00:04:02]** configurar todas essas ferramentas, né? Porque não adianta só a gente instalar e conhecer, né? A gente vai ter que configurar tudo. E a gente vai fazer o nosso primeiro Hello World com o FastAPI hoje. Massa e depois a gente vai fazer os testes desse Hello World, porque o foco, né? Eu falei no vídeo passado, um dos focos principais pra mim é que a gente consiga, olha, então me ligando de spam aqui. Vem no meio da aula. De novo.

**[00:04:35]** Muito bom, deixa eu desativar a sincronia aqui. Se não, quando o SPAN liga, não para, tá ligado? Pronto. Do nada, coisas que acontecem ao vivo é assim mesmo. Então a gente vai fazer tudo isso juntos. Então o que a gente precisa para o nosso ambiente de desenvolvimento? É uma coisa como esse não é um curso introdutório de Python, a gente não vai configurar, tipo assim, sei lá, vou falar que editor de texto você deve usar na sua máquina. Eu presumo que você já tenha um editor aí.

**[00:05:08]** Eu vou usar o GNU e Macs, que é o editor de texto que eu uso geralmente, mas qualquer editor serve aí o que você estiver usando. Você estiver usando o Kate, é legal, estiver usando o VIN, estiver usando o iMac, estiver usando o VS Code, se estiver usando, sei lá, o PageArmy, qualquer coisa que vai servir, desde que seja um editor que você goste. Se você quiser a minha recomendação de um editor legal, falar, eu não tenho nenhum aqui, eu recomendo o Kate.

**[00:05:34]** É um editor muito legal, ele é livre, ele é leve e ele não rouba seus dados, igual aquele que todo mundo usa. Um editor de texto, ou um editor de texto, depois do editor de texto a gente tem um terminal, basicamente todo mundo tem um terminal. Então eu tenho...

**[00:05:56]** o Terminator aqui, e aí qualquer um que você tiver aí, se for Ghost e Utilix, isso aqui mais para quem está no Linux, né, o iTerm, para quem está no Mac, o Windows Terminal, se estiver no Windows, pode ser o WSL normal, pode ser o PowerShell, pode ser até o CMD também. Tá tudo bem.

**[00:06:18]** Aí a gente vai precisar de uma versão suportada do Python atualmente e qualquer versão maior do que a 3.9. Igual ou maior do que a 3.9. Aí o Germano perguntou se eu vou mostrar como fazer um ambiente no Mac. Não vou mostrar porque eu não tenho um Mac. Se alguém quiser me dar um Mac de presente eu gravo o vídeo, mas eu não tenho como fazer isso.

**[00:06:39]** A RAPA perguntou, esse ambiente serve para outros projetos? Sim, serve para tudo. Tirando a parte do Fast API, mas em geral, testes, linters, tudo isso serve para qualquer coisa. Então, é uma boa prática para todos os outros projetos que vocês quiserem usar. E a gente vai usar uma ferramenta chamada PPX, que é uma ferramenta que instala coisas globais do Python e tal. É muito legal, funciona muito bem e a gente vai instalar isso junto, mas já estou dando aqui as coisas que a gente vai ter no nosso ambiente.

**[00:07:08]** Quinto e não menos importante, a gente vai usar o Poetry, que é uma ferramenta que gerencia projetos Python. Ou seja, a gente vai criar nosso pacote usando Poetry, ele gerencia a criação dos ambientes virtuais, ele gerencia a instalação de versões do Python. Então, é o componente central, né? A pedra angular que segura o nosso arco aqui, né?

**[00:07:33]** E aí, algumas coisas de Git são importantes, tipo assim, o basicão de Git, a gente vai dar git commit, git push, git add. Só isso. Então, suber o basicão de Git vai ser de boa aqui. E aí, o Docker, para criar o contêiner na nossa aplicação, também faz parte do ambiente de desenvolvimento, mas isso a gente vai usar só lá na aula 11. Então, de novo, algumas pessoas perguntaram no grupo, será que eu preciso do Docker? Tipo assim, tá tranquilo, por enquanto.

**[00:08:01]** E se não tiver experiência com Git e Docker, também tá tudo bem. Porque eu deixei alguns conteúdos listados aqui, né? Então, o Teo, meu amigo, Teo Calvo, tem um curso inteiro de Git, aí tipo assim, pô, eu nunca mexi com Git, não sei nada, aqui tem umas três aulinhas aqui do Teo de Git, que são muito boas, dá pra tirar, sair do zero, assim, é muito massa, falou também, nunca mexi com Docker. Então, o GFerson, né, nosso outro amigo...

**[00:08:30]** do Linux chips ele tem uma playlist inteira de docker também então sabe são conteúdos livres assim como esse que a gente está produzindo agora então se vocês quiserem pode brincar saca tá tudo bem e aí se você tiver alguma dúvida sobre putz eu preciso instalar sei lá o docker mas eu não sei aonde eu pego as coisas que eu preciso não

**[00:08:53]** Não vai baixar lá no baixo aqui, né? Tipo assim, tem um apenso inteiro explicando aqui, ele tá com a data, então como é que está o Pipex, tem algumas coisinhas aqui, como está o Poetry, onde a gente baixa o GH, que é uma ferma da gente que vai falar daqui a pouco, o Docker, o Docker Compose, o Git, então tem todas as coisinhas aqui nesse apenso, então pode dar uma olhada lá se for preciso.

**[00:09:19]** Massa, aí fizeram uma pergunta aqui, tipo assim, eu posso usar o vmv? Não. Você vai entender por que daqui a pouco, porque a gente vai alterar a versão do Python. E o vmv não tem a capacidade de fazer isso. Então, é um ponto aqui. Então, vamos lá. A primeira ferramenta que a gente vai usar é o pipi x, ou pipi x. O pipi x é uma ferramenta que tem um nome bastante engraçado, né? A gente costuma usar o pipi, né?

**[00:09:49]** Bom, geralmente todo mundo já foi instalar alguma biblioteca Python em algum momento e se deu de conta que a gente roda o pipi. A gente pega e fala, olha, pipi legal. Funciona. Pipi significa é um acrônimo recursivo que significa pipi install package. Massa pipi install package. E aí essa ferramenta, o pipi x, ou pipi x,

**[00:10:15]** É uma ferramenta que também é mantida pelo mesmo pessoal que desenvolve o Pipe, que é o Pipe A, que é o Python Package Authority, a autoridade de pacotes do Python. É o mesmo grupo de pessoas que desenvolve isso. E o Pipe X, ele tem esse X aqui no final de executable, ou seja, de executável, né? X é de executa. Então a ideia do Pipe X

**[00:10:44]** é instalar pacotes de forma global na nossa máquina. Então eu falo, eu quero instalar o Poetry. Aí está vendo que o Poetry não é uma dependência do nosso projeto.

**[00:10:56]** Então, como é que eu instalo o Poetry sem colocar ele dentro do projeto, então o PPX serve para essa coisa. Tem várias coisas que dá para instalar com o PPX, ferramentas Python de maneira geral, a gente costuma usar o PPX, é uma boa prática para lidar com isso. E como é que a gente instala o PPX, né? Então, vamos lá. Eu vou fazer primeiro no Windows, porque eu acho que...

**[00:11:16]** O pessoal costuma ter mais dificuldade para rodar essas coisas no Windows, então a gente vai fazer junto aqui. Eu tenho uma máquina aqui que não tem nem o Python, então só para dar uma coisa, às vezes você vai tentar rodar um comando que eu rodei aqui e fala, pô, não funciona, então a gente vai sempre junto. A ideia é essa, sem problema nenhum. Então eu estou aqui nessa máquina, deixa eu colocar fullscreen para a gente conseguir ver.

**[00:11:43]** Então, a gente vai lá no Python.org, né? O site do Python, baixo Python, se você já não tiver o Python instalado, então Python.org. E aí, para o Python funcionar no terminal que a gente vai usar o tempo inteiro, ó, você pode baixar a última versão. Qualquer versão maior do que maior ou igual a 3.9 funciona, porque são versões mantidas no Python, né? Mas se a preferência der para usar a última, pode usar a última. Então, a gente baixa aqui, fez o download.

**[00:12:14]** Legal? Na hora de instalar o Python, para o Python funcionar no terminal, ele tem essa coisinha aqui ó, que é aqui ó, use o admin e faça isso aqui ó, adicione o Python xz ao perf, senão a gente não consegue digitar Python de dentro do terminal, o que é uma coisa primordial para a gente aqui. Massa, então vou dar um yes aqui, a gente segue enquanto ele instala, vou responder as perguntas aqui.

**[00:12:43]** O germano perguntou, precisa ter um processador muito bom pra rodar o FGPA? Não, qualquer máquina vai rodar isso aqui, tá ligado? É coisa, tipo assim, a gente vai fazer o deploy disso, a máquina onde a gente vai fazer o deploy tem um núcleo e 256 MB de memória e roda bem. Então, não fica muito, sabe, não se preocupa muito com esse requisito, porque esse requisito é tranquilo. Legal, aí passou, instalou o Python, às vezes você não tinha.

**[00:13:13]** Beleza. Close. Quando a gente abrir o shell a gente vai ter o Python aqui instalado, né? Então você pode vir aqui e dar um Python só pra ver se tá tudo rolando. Exit. Legal. Tá funcionando. Então eu vou dar um Python.

**[00:13:28]** menos m, m é para executar um módulo do Python, qualquer módulo que seja, que o Python seja capaz de executar, e aí você vai dar o pip, que é o pip que é o pip install package, e a gente vai instalar pip install o pip x aqui, pip x. Então essa é a recomendação para quem está no Windows, é uma forma simples de fazer. Aí ele vai falar, olha, parece que a gente conseguiu instalar e tudo mais, só que se eu rodar pip x aqui...

**[00:13:58]** Funcionou, às vezes não funciona. Deixa eu tentar sair daqui para ver se vai dar tudo certo agora quando eu restartar o show. PPX. Legal, às vezes o PPX tem alguns problemas para ser executado na máquina e é uma coisa normal que vai acontecer sempre. Então você faz o seguinte aqui, Ensure, Ensuri, Ensure Path. É esse comando aqui que vai fazer com que o PPX seja...

**[00:14:27]** executado e encontrado dentro da nossa aplicação. Basicamente isso, então a gente tem o Pipe X aqui. Esse é o processo. Para quem não usa Windows e tal, vem de outro sistema operacional, é só essa coisa que vai mudar que essa forma de instalar aqui, eu vou até desligar essa máquina aqui. E para quem usa outro sistema operacional, por exemplo, ah, eu sou do Linux, então você vem aqui Lima...

**[00:14:56]** Eu vou só subir uma máquina virtual aqui pra gente, só pra gente ter uma máquina virtualzinha aqui funcionando. Aí o Cels falou, eu tive problema pra configurar, tive que mudar o path, então provavelmente quando instalou, não clicou lá no path. Então, por exemplo, eu tô no Ubuntu, que é o mais comum de todos, né? Então aqui eu tenho uma máquina do Ubuntu. Massa.

**[00:15:29]** Aqui ó, o bonto. E aí no bonto pra gente instalar, a gente dá o... Ou o Eric falou, pra quem já tem o pip instalado, precisa desinstalar. Então, Eric, a única coisa que eu gostaria que tivesse é que se o Python que roda esse pip seja numa versão atual, ou seja, tem que ser 3.9 pra frente, ou seja, 3.9, 3.10, 3.11, 3.12, 3.13, vai funcionar. Massa.

**[00:15:57]** Aí, aí, legal, voltando pra cá. Então, você tá no Ubuntu, que é o mais padrão aqui de todos, você vem e dá um sudo, apete, install, ppx. Pra quem tá no Linux, essa é a recomendação. Aí você fala, ah, eu tô no Mac, eu não consigo simular o esquema do Mac aqui, mas ele é instalado via Homebrew. Então, eu deixei aqui, no material de texto, aqui eu tenho aqui, instalação do ppx aqui. Aí, na documentação, que é a página pra onde vai,

**[00:16:26]** tem a recomendação de como adicionar, instalar no macOS, que é isso aqui. Brille, Instal, PPX. Essa é a recomendação aqui no Mac. Então, para todos os sistemas, isso aqui vai funcionar bem. Então, aí ele já está aqui, PPX. De novo, sempre que você quiser garantir, sei lá, você vai digitar PPX, talvez não funcione, então você dá um PPX, Ensure, Path.

**[00:16:54]** Aí você fecha o Shell e abre de novo ou dá um Surge no seu BashRC. Eu estou usando o Bunto como base porque 80% do pessoal deve estar usando alguma Debian. Então Debian, Bunto, Linux, Mind e tudo mais. Se você estiver no Fedora, por exemplo, é DNF, Instal, Pipex. E se você estiver no Arte, que é o meu caso, sei lá...

**[00:17:21]** Pac-Man, menos S, Python, traço PPX. Massa? Então essas são as instruções aqui para rodar isso. Deixa eu só parar essa máquina virtual aqui, senão eu estou rodando mil máquinas virtuais daqui a pouco, a minha máquina quebra. Legal. Então desliguei esse Windows só para garantir que está tudo funcionando. Legal, aqui também parei para garantir que, senão daqui a pouco, minha máquina trava e a gente não faz nada.

**[00:17:53]** Legal, então vamos, todos nós temos essa coisa. Aí o David fez uma pergunta que não tem nenhuma relação com a aula, eu vou dizer só sim, mas aí depois tu vê por si só. Tá perguntando se o Pipe implementa uma PEP específica, implementa e é isso, massa. Então, legal. Rolou isso aqui no Windows, se precisasse, se não conseguir, você pode rodar o Python, menos M, Pipe X, Instructor, PEP, ou seja, ou...

**[00:18:24]** ppx in share path, ou se daqui o ppx não existe, você pode rodar esse comando aqui, python-mppx in share path. Legal? Aí com isso, a gente tem uma instalação global do ppx, que a gente consegue instalar qualquer coisa. Ou seja, qualquer ferramenta Python que seja um executável de terminal, a gente consegue rodá-la via ppx.

**[00:18:47]** Por exemplo, eu uso um negócio aqui para gerar QR-Code, chama Segnon. É uma aplicação Python, então eu posso instalar ela via PPX. Ah, eu vou usar o Poetry, então a gente usa, instala o Poetry pelo PPX. Essa é a recomendação aqui. Então legal, a gente tem aqui o PPX rodando.

**[00:19:06]** Para todo mundo, em todos os sistemas, você deu um instalou com Homebrew, instalou no gerenciador de pacotes, instalou no Windows via pip. Legal, temos o ppx rodando, o comando. A coisa que a gente tem que fazer aqui é dar um ppx install poetry. Uma coisa bem simples aqui, eu devia ter deixado o shell aberto aqui.

**[00:19:32]** Porque a gente roda numa máquina que não é a minha, que não tem o ppx instalado, seria legal. Ah, e uma coisa que eu não falei aqui sobre o ppx, se você estiver usando via wsl, você segue a recomendação do apt instalar o ppx aqui. Não é para instalar desse jeito com o pip. Legal? Combinado? Então se você estiver no wsl, você pode instalar com apt.

**[00:20:00]** Então legal, aqui nessa máquina a gente tem o ppx, mas se a gente for rodar a gente não tem o poetry, tá vendo? Poetry não existe. O que a gente faz aqui? Então a gente dá um ppx install poetry. O tamanho da letra tá legal aí, vocês estão conseguindo enxergar? Então é basicamente isso, ppx install poetry.

**[00:20:38]** Ainda não entendi a diferença de instalar com o pip dentro de uma vnv normal e o pipx. O pipx deixa as coisas globais. Aqui ó, você está vendo que eu não estou dentro de nenhum ambiente virtual? Eu digito poetry, e agora a gente tem o poetry funcionando aqui. O seu insure path tem que ter rodado lá antes. Massa, então a gente tem o poetry.

**[00:20:59]** Legal? Então o Poetry vai ser a pedra angular de toda a nossa instalação, de todo o nosso sistema, é com ele que a gente vai criar o nosso pacote, é com ele que a gente vai fazer qualquer coisa aqui dentro. Aí perguntaram, o HTT-PAI seria o caso de instalar pelo PPX? Sim, é uma ferramenta boa, né? O Too Long, várias outras ferramentas, todos esses utilitários são legais para instalar via PPX. Massa, é isso. Legal? Então temos aqui o Poetry.

**[00:21:32]** uma das coisas que ficou obsoleta da versão passada é que o poetry antes tinha um comando que chamava poetry shell que entrava no ambiente virtual e esse comando não existe mais e ele é uma mão na roda mas não é que ele não existe mais ele foi externalizado como ele era muito grande ele virou um plugin do próprio poetry então a forma de instalar ele aqui é dessa forma a gente usa o ppx e a gente fala em vez de instalar a gente fala inject

**[00:22:00]** E a Inject quer dizer o seguinte, lá onde você instalou o Poetry, aqui, quando você instalou o Poetry, você colocou ele num lugar, então você injeta esse pacote, que é o Poetry Plugin Shell, dentro do Poetry. Massa para eles funcionarem bem juntos. Então, é basicamente esse comando que a gente vai rodar aqui. Então, ppx Inject Poetry Shell, e deixa eu colocar aqui para baixo.

**[00:22:30]** ppx inject poetry shell a partir desse momento ele vai instalar ou seja instalar isso dentro do ambiente que ele criou poetry e aí a gente pode dar um poetry shell que ativa o ambiente virtual ele tá falando ó não posso porque não existe pi project pontom l aqui tá tudo bem porque não tem mesmo mas essa é a resposta esperada depois que a gente instala né e aí esse é o passo de instalação do poetry que a gente precisava ter aqui dentro

**[00:22:59]** Legal, vou sair dessa máquina, agora eu acho que tudo eu posso fazer da minha própria máquina. Massa, instalamos o Poetry, e aí se você tiver alguma dúvida, de novo, você pode vir aqui no... lá no apense das instalações. Aí estão perguntando se tem problema usar Activate. Activate não ativa o ambiente virtual, é só o Poetry Shell que ativa. O Activate mostra aonde você vai para habilitar o ambiente virtual.

**[00:23:31]** Então lembrando, aí se tiver dúvidas de novo, tem aqui um apêndice só dessas coisas, das ferramentas e tudo mais, você vai caçando, cavucando aqui e a gente vai achando elas, ok? Então legal, seguindo aqui, então a gente vai criar o nosso projeto agora. A gente pode dar qualquer nome pra ele, mas eu vou dar um nome...

**[00:23:55]** Fast 0, que é o nome que a gente usou padrão dentro do curso de maneira geral, porque o curso chama Fast API do 0, só que eu quero diferenciar, então eu vou colocar um Fast 0 a 5, ou Fast a 5, não sei. Fast API do 0, a gente pode pensar no nome, você dá o nome que você quiser para o seu projeto aí. E aí, uma coisa é importante aqui.

**[00:24:18]** Lembra que a gente tá no shell, a gente tá rodando esses comandos dentro do shell? Então é interessante que você vá pro lugar onde você costuma colocar as coisas aí dentro do sua máquina. Então, por exemplo, ah, sei lá, cd-git eu costumo, eu tenho uma pasta-git onde estão todos os meus projetos aqui dentro. Então, a gente pode fazer o seguinte, então aqui onde eu tô eu vou dar um poetry, new, new significa que a gente vai criar um novo projeto.

**[00:24:49]** Massa, e aí eu vou dar um nome pra ele, sei lá. Eu acho que eu quero chamar de FESTE0, eu vou chamar de FESTEIPI0 dessa vez. E bom, antes da ENTER, se você já deu ENTER, deleta a pasta, a gente vai colocar uma configuraçãozinha aqui, que é o seguinte, menos menos flat.

**[00:25:15]** Existem duas formas de criar projetos em Python. Existem projetos que são aninhados por namespace. Não sei se vocês já olharam. Você entra no projeto, no repositório e ele tem uma pasta chamada SRC. Ou você coloca o pacote para fora, que é o modo flat.

**[00:25:39]** Eu prefiro desse jeito, sem a pasta SRC. Mas isso é uma questão de gosto. Então, como eu escrevi isso aqui, eu vou seguir o meu gosto. Mas se você quiser, pode não colocar o flat. Então, ele vai chamar FastAPI 0. Então, esse é o comando dessa versão que eu estou usando aqui, online. Aí me perguntaram aqui, ah, dúvida, o veopoetry. PDM.

**[00:26:07]** Então, legal. Aí, aqui, a gente criou essa pastinha. Se a gente der um tree nessa pastinha, FastAPI0. Eu acho que o meu comando é esse aqui. List3. Então, ele criou essa estrutura pra gente aqui. Ele criou uma pasta chamada FastAPI0.

**[00:26:31]** Dentro dessa pasta, a gente tem uma pasta que é o nosso projeto, FastAPI0, e ele criou um Dunderinit aqui. Aí ele já criou pra gente uma pacinha de testes, né? O Poetry é legal porque ele já gera esse boilerplate de como o projeto vai funcionar. Aí ele criou um Readme.

**[00:26:48]** que é onde a gente vai escrever as coisas para deixar no Git depois, a minha versão do projeto de FastAPI e tal, e aí ele criou um PyProject.toml, que é o arquivo aonde a gente vai especificar todas as nossas dependências. A parte mais difícil já foi, sim, a parte mais difícil é fazer essas coisinhas funcionarem do jeito que a gente queria. E aí ele criou isso aqui para a gente, então ele criou essa estrutura aqui. Legal?

**[00:27:16]** É uma estrutura bem simples, bem básica, a gente pode vir aqui e entrar nela. Feche... Feche API zero, que é o nome do nosso projeto. Você tem uma LS aqui, ou um Gears, se você tiver no Windows, você consegue ver os arquivos que estão aqui dentro. Legal, super simples, já temos a estrutura base do nosso projeto usando Poetry. Tá vendo que é mais simples do que ter que criar cinco pastas e tudo mais, sabe? Então é mais de boa.

**[00:27:47]** Uma coisa, lembra que eu falei lá atrás que você poderia ter qualquer versão mantida do Python? Ou seja, você pode ter a versão 3.9, a versão 3.10, a versão 3.11, a versão 3.12, a versão 3.13, 3.14, que é a versão mais nova agora? Eu vou fazer o seguinte.

**[00:28:07]** Como a gente está padronizando o ambiente para a gente poder se ajudar a ter os mesmos erros e rodar do mesmo jeito, eu vou instalar a versão 3.13 do Python aqui via Poetry. Ou seja, independente se você estiver rodando o Python na versão 3.9, 3.10, 3.11, 3.12 ou até na 3.13, a gente vai instalar uma versão do Python que vai funcionar para o nosso projeto.

**[00:28:32]** Mas aí a gente garante que todo mundo está rodando na mesma versão, todo mundo vai ter os mesmos erros e vai funcionar da mesma forma. Então a ideia aqui é que a gente faça um poetry, Python, ou seja, a gente vai chamar o subcomando Python do comando poetry e a gente vai passar um install. Install. Aí você pode falar, eu quero instalar, eu quero fazer o curso na versão 3.11, sei lá. Eu recomendo que você faça na versão mais nova.

**[00:29:03]** Então, 3.13. Aí ele tá falando que eu já tenho isso aqui instalado, tudo bem, eu vou dar um reinstall só pra mostrar pra vocês como é que fica a carinha do comando aqui. Se a instalação for feita via pyenv, vai dar algum BO, eu recomendo que você faça a mesma que a gente tá fazendo aqui. Mas se você quiser fazer diferente, sabe? É a escolha de cada pessoa. Aí legal, ele falou, fazendo o download, instalando o Python 3.13, o C Python.

**[00:29:34]** Feito. E ele está aqui, ó. Ele testou e viu que está tudo bem. Done. Ou seja, a versão 3.13 do Python está instalada via Poetry. Então, se eu quisesse fazer um Poetry Python List para ver todas as versões que tem aqui instaladas no meu sistema, a gente pode fazer. Aí você vai ver no meu sistema é... é triste aqui, né?

**[00:29:57]** Olha quantas versões do Python eu tenho aqui. 3, 13, 3, 3, 3, 2, 3, 12, 9, 3, 11, 11, 3, 9... Sabe? Tem algumas instaladas via pyenv, tem outras... Sabe? Meu ambiente é muito louco. Mas no seu, provavelmente, ele vai ter essa, essa aqui ó. Que foi a que a gente acabou de fazer. O 3.13.2... Manager, né? Quem tá manuseando essa versão é o Poetry.

**[00:30:29]** E aí, a partir disso aqui, a gente funciona. Legal que vocês viram que quem está usando paenvi, listas, versões do paenvi, está tudo bem também, vai funcionar. Então, a partir disso aqui, a gente vai falar para o Poetry, para ele usar a versão 3.3.

**[00:30:50]** Mas, então, eu vou dar um poetry envy, que é de ambiente, e eu vou falar para ele, olha. No ambiente que a gente vai usar, usa a versão 3.13. Eu quero mostrar para vocês aqui o que veio nesse arquivo aqui. Nesse arquivo Pi Project. Ele está usando a versão 3.13.

**[00:31:10]** que é a versão que eu tenho o Pipe X instalado. Mas lembra, como você podia já ter o Python instalado em outra versão, provavelmente ele vai estar com esse valor diferente aqui. Então, a gente vai falar para o Poetry. Poetry, Envy, então, para o nosso ambiente, use a versão 3.13. Aí, ele fez o seguinte aqui, criou um ambiente virtual. Create Virtual Envy do Fast API 0 em algum lugar.

**[00:31:41]** no seu provavelmente vai dar um outro lugar mirabolante e tá tudo bem é isso mesmo e aí a gente configurou ele falou olha estamos usando a versão 3.13 do python nesse projeto e acabamos de criar um ambiente virtual legal massa temos essa coisa aqui uma coisa legal aqui é o seguinte pra gente reduzir o escopo e garantir que tá tudo funcionando da maneira como a gente gostaria que funcionasse

**[00:32:14]** O ideal é falar o seguinte, olha, qualquer versão maior do que o 313 funciona o nosso projeto, porque é uma garantia, pelo menos esperada, que toda a versão maior que o 313 tenha todos os recursos que a gente está usando agora, mas o 4.0 não. Então a ideia é que a gente altere o nosso arquivo aqui no Require Spider, e passe para ele uma versão mais correta.

**[00:32:42]** que a gente espera que fosse, né? Então eu vou abrir aqui o meu... no meu editor aqui, junto com vocês, FastAPI0, que é o nome do nosso projeto aqui. Então aí a gente tem esse arquivo PyProject.tom meu aqui, que era o que a gente tava olhando lá no show. E aí ele tá aqui ó, 3.13, então qualquer versão maior que o 3.13 funciona aqui. Lembrando que se você gerou no 3.9 ele vai ficar assim.

**[00:33:09]** 0, 3, 9 ou 0, 3, 10. Como a gente instalou e falou para ele usar no Env, a 3, 3, então a gente pode colocar aqui. 3, 13, vírgula. Eu quero dizer que funcione qualquer uma menos, sei lá, qualquer uma que seja maior ou igual ao 3, 13, né, o sinal de maior igual e menor do que a versão 4.0, por exemplo. Então ele vai funcionar sempre desse negócio aqui. Legal?

**[00:33:43]** Aí o Enri falou aqui, esse comando PoetryEnv 3.13 tem que ser usado dentro da pasta do projeto. Sim, sim, dentro da pasta do projeto. Boa observação, Enri. Então você tem que estar dentro da pasta do projeto para poder executar o PoetryEnv-Jubes. Legal? Agora a gente já tem um projeto inteiro configurado com Poetry, tudo certinho, com as versões legais aqui. Aí, se você quiser se ver, inscreve um readme maneiro aqui.

**[00:34:15]** com o Dunossauro 2025 Pay, sabe? Então não está aqui, tem seu readme aí, você coloca suas coisas, suas informações, brinca e tudo mais para ficar tudo certinho aí, para a gente poder ir para a frente. Legal, versão do Python resolvida, ambiente configurado, tudo certinho, a gente pode dar um poetry install, ou seja, que ele vai criar o ambiente virtual para a gente aqui dentro, mas lembra que quando a gente deu o Envy Use já estava funcionando, então...

**[00:34:45]** É só para falar, olha, instala aqui, está tudo certinho. Ele falou, instalamos o nosso projeto dentro do nosso ambiente virtual. Nenhuma mágica, ele já tinha criado o ambiente virtual quando a gente deu envius, mas o Poetry Install é interessante quando você pega o projeto de outra pessoa que tem o arquivo Pie Project e precisa instalar, aí você fala, Poetry Install, aí ele instala todas as dependências e tudo mais, é um comando mais para frente, mas é legal a gente falar dele enquanto a gente está falando do Poetry.

**[00:35:14]** Massa? Então, eu sei que... Legal, a gente tá aqui falando de... de PSHA-PA e o curso, né? Por que a gente não instalou o PSHA-PA ainda? Por que a gente tá falando de Poeta, de PPX, de qualquer outra coisa, né? Então, vamos instalar o... o... o PSHA-PA dentro do nosso projeto. O PSHA-PA tem várias versões, uma minimal e tal, pra gente padronizar, eu vou usar a versão padrão, a versão standard. Então, a gente vai lá no Shell, onde a gente tá dentro do nosso projeto, certo?

**[00:35:46]** e dá um Poetry, Edge, Fast, API e a gente vai falar que a gente quer essa versão, a versão padrão, a versão standard. Mas se você estiver usando isso aqui no Windows, pessoas do Windows, só me responda uma coisa, eu sei que tem aspas aqui, mas eu não sei exatamente se é aqui ou se é dentro do standard para que a gente vai fazendo essa instalação no Windows ou no ZSH ou no FISH, quem usa determinais alternativos, então eu vou colocar aspas aqui.

**[00:36:18]** Mas não é necessário. Aí, olha o que aconteceu aqui.

**[00:36:24]** Ele falou o seguinte, olha, instalou um monte de, um monte de coisas. Ele instalou o UV Loop, que é o loop, ele instalou o UV Corn, que é o servidor da aplicação, ele instalou o Typer, que permite com que a gente faça um CLI aqui, ele instalou o PIDENT, que é uma ferramenta de validação, HTTPX, que é uma ferramenta que a gente vai usar nos testes, o DINJA, que é para renderizar HTML, e ele instalou o próprio FastAPI, o Starlet, então ele instalou um monte de coisinhas aqui. Se a gente for olhar...

**[00:36:53]** É desse jeito mesmo? Com as aspas assim. Obrigado, Caio. Aí você vai ver que aqui no nosso arquivo Pi Project, ele colocou aqui como Dependences. E aí ele está aqui como FastAPI Standard. Ou seja, no Windows não precisou de aspas. Legal, massa. Valeu aí pela informação. Então ele instalou o FastAPI Standard e ele falou o seguinte, olha.

**[00:37:26]** Está na versão 0, 115.2, que é a versão que a gente está usando nesse curso aqui, é a versão que a gente vai usar até o fim. Ah, no futuro vai sair uma versão maior do que tal. Legal. Lá no material de texto tem um apêndice, que é o apêndice C.

**[00:37:49]** que são as versões instaladas. Então sempre que você, sei lá, se passou um tempo, você está assistindo isso aqui em 2027, as versões usadas nessa apresentação estão todas aqui.

**[00:38:06]** Todas, então aqui ó, o Fast API tá nessa versão aqui que a gente acabou de colocar. Aí quando é correr do curso a gente vai estar lá outras coisas, mas elas estão todas pinadas daqui. Aí se for necessário você vem aqui copi o Dependence com o Fast API na versão certinha que a gente tem aqui. Massa, tudo rodando. Gostei do poeta que ele joga uns emojis, sim. É bem legalzinho mesmo, eu também gosto.

**[00:38:32]** Então a gente já tem o FastAPI instalado na nossa aplicação, no nosso projeto, no nosso ambiente e lindo, maravilhoso. Foi dolorido, eu sei que essa coisa de instala o PPX, do PPX, instala o POM entre, do POM entre aquele projeto, sabe? Eu falei que isso era um pouco chato de fazer, mas o curso era do zero, lembra? Então a gente não tinha nada e agora a gente já tem tudo funcionando. Gostei do comentário da técnica aqui, tipo assim, alô pessoal de 2027, né? Então...

**[00:39:03]** Se você estiver fazendo isso no futuro, dá uma checada nas missões para ver se elas estão batendo, tudo certinho. Massa? Vamos lá! Então, a primeira coisa que a gente vai fazer hoje é criar uma função e um arquivo, né? A gente vai criar esse arquivo aqui, chamado... Aqui, estava no FESTE0, né? Mas a gente vai criar isso dentro da estrutura que a gente colocou aqui, porque qualquer coisa vale aqui, né? Você pode ter usado outro nome. FESTEAPIXYZ com...

**[00:39:33]** Live na Twitch, sabe? Você pode ter colocado o nome do pacote do jeito que você quiser. Mas, basicamente, dentro da pasta do projeto aqui, que a gente colocou como FastIPI0, a gente vai vir aqui e vai fazer o seguinte. Vai criar um novo arquivo que a gente vai chamar de app.py. Ah, pode chamar de Juvenal? Não. É pra criar um arquivo chamado app.py. Porque... depois os comandos não casam.

**[00:40:03]** O nome do seu projeto pode ser o que você quiser, mas o arquivo tem que chamar app.py para a gente seguir essa padronelização que a gente está tomando aqui. Legal, eu vou criar uma função aqui, que eu vou chamar de ReadRoot, certo? Uma coisa simples aqui. Então, def, talvez esteja um pouco pequeno, eu vou chamar de ReadRoot. Tá lá, leia a raiz. E eu vou retornar qualquer coisa aqui. Eu vou retornar um dicionário, padrão do Python aqui.

**[00:40:31]** Eu vou falar que a gente vai chamar feste de oclinhos. Eu vou retornar uma mensagem aqui, message. E eu vou retornar o Olamundo. Olamundo. Vocês sabem que se você não retorna o Olamundo, na primeira... Na primeira... No primeiro exemplo, você cai na maldição do Olamundo, né? E eu sei que ninguém quer ficar aqui rolando, sabe? Falando, nossa, tá dando tudo errado. Se não faz o Hello World, sempre dá errado depois.

**[00:41:02]** Brincadeiras à parte, como é que a gente vai rodar isso aqui? Eu quero fazer um experimento com vocês para mostrar como as coisas são dentro do Festa API aqui. Então, a gente vai abrir o nosso shell dentro do arquivo onde a gente está aqui, lembra? Então, a gente está lá no shell, dentro do projeto. A gente está aqui no Git, Festa API do zero, Festa... Festa um de oclinhos. Sabe? Da forma como a gente quiser aqui.

**[00:41:30]** E lá dentro da pasta, existe dentro da pasta com o nome que a gente criou, então vamos lá. A gente vai dar um Python, e aqui dentro a gente tem esse Fast API 0 que a gente criou, e aqui dentro tem a pastinha app.py, certo? Eu quero abrir isso aqui de um modo interativo do Python, que é com "-i". Mas assim, então, "-i", vai abrir o shell do Python com esse arquivo...

**[00:41:58]** app.py já carregado em memória. Massa. E aí a gente vai fazer da mesma forma como a gente sempre faz. O que retorna a função readRoot, né? Então eu vou chamar aqui. ReadRoot.

**[00:42:14]** E aí é uma função do Python normal, né? Coisa que a gente costuma fazer no dia a dia, corriqueiro, para quem está acostumado a brincar com o Python. Se a gente viesse aqui e fizesse o seguinte, print, read e root. Por exemplo, chamando a função, quando a gente rolar seu arquivo, sabe, daquela mesma forma, Python tal, ele print a mensagem. É isso, basicamente, uma função Python normal, tradicional, que a gente usa no dia a dia. E qual é a pira do FastAPI aqui?

**[00:42:44]** A grande ideia do FastAPI é que a gente vai simplesmente dar um insumo para ele e falar, olha, do FastAPI importa o FastAPI, cria o objeto FastAPI e fala para ele que toda vez que a gente bater no barra, ele vai retornar essa função pela rede. É, isso é mágico, não?

**[00:43:04]** É muito simples, né? É muito, muito, muito, muito simples. Desculpa, eu acho. Saca, então vamos lá dentro do nosso... do nosso arquivo app.py. Então eu vou vir aqui e vou fazer o seguinte. Ah... From, FastAPI, Import, FastAPI, Grandão. Com letras maiúsculas. Aí eu vou dar um nome para essa coisa de app. Porque a gente está fazendo um aplicativo nada mais justo. E eu vou chamar o FastAPI e vou criar uma instância.

**[00:43:33]** desse Fast API aqui. A partir do momento em que eu der o arroba app.aí a gente vai entender daqui a pouco o que significa esse get aqui. Não esquenta com isso por enquanto. Eu vou colocar um barra aqui. Ou seja, quando alguém bater lá no nosso site, na nossa aplicação que estiver rodando na internet ou dentro da nossa própria máquina, quando alguém bater lá na home ou na raiz, na root...

**[00:44:02]** A gente vai ler e retornar essa mensagem aqui pra ele. Juro, é super simples. Hello World com Fast API. Vai, fala, fala. Pode falar, pode falar. É simples, não é? É bonitinho, né? É bonitinho. Fala, fala pra mim. Não é lindo, não é lindo. Super simples. Para, para, para. Não brinca comigo. É super legal aqui. Então, agora a gente criou, a gente precisa executar esse código, né? E como é que a gente executa isso?

**[00:44:33]** Simplesmente assim, FESTE API deve FESTE0 app.py Juro, simples, BEAUTIFUL, né? Como disseram aí no chat. O Leon falou de Java decorator, já teve essa magia nos frameworks web, né? Você faz uma coisa e a sua função fica na internet.

**[00:44:59]** Só que aí agora, a gente vai tomar uma agora muito legal. Como é que roda isso aqui? Você chama o FastAPI aqui. Você fala FastAPI.

**[00:45:08]** Aí você fala, olha, Fast API, sobe isso aqui pra mim, ou seja, inicia, dá um start na nossa aplicação e modo de desenvolvimento. Então, Fast API deve, e aí a gente passa o mesmo caminho que a gente tinha ali atrás. Deixa eu comentar isso aqui. Lembra que a gente fez isso aqui? Paí tão roda a nossa aplicação, quer o que a gente costuma fazer no Shell ou da Play lá na ideia?

**[00:45:31]** Se a gente fizer o seguinte, Fast API Dev, ou seja, levanta isso aqui em produção pra gente, isso já vai estar magicamente no ar. Eu menti pra vocês. Eu menti. Não funciona. E por que não funciona? Porque lembra, a gente não tá no ambiente virtual que a gente precisava que isso aqui estivesse.

**[00:45:58]** E como é que a gente faz para isso aqui rodar dentro do ambiente virtual? O Poetry tem um comando mágico aqui, que a gente pode falar o seguinte, Poetry Run, ou seja, Poetry executa o próximo comando que eu mandar aqui para você, como se fosse no ambiente virtual. E aí a gente roda, Poetry Run, e ele executa. E aí, está funcionando. Calma, a gente vai voltar nesse comando aqui.

**[00:46:32]** Mas eu quero brincar aqui, eu quero brincar com vocês. Ele abriu isso aqui, um endereço de loopback, né? Então, HTTP 127 001. A gente pode copiar aqui, copiar esse endereço. E lá no navegador agora, no seu browser. Olá, mundo! Você tá aqui, ó, o nosso message. Olá, mundo! Ó, lindo!

**[00:47:02]** maravilhoso como disseram como como disse a ju beautiful exatamente olha que simples mano que bonitinho tá tá na rede pei é exatamente eu adoro falar isso é pei funciona maravilhoso e aí o que acontece eu odeio aí aí aí é uma questão muito pessoal minha assim

**[00:47:29]** Eu odeio ter que digitar comandos e comandos imensos e que não fazem sentido nenhum, tá ligado? Odeio, odeio. Você pode gostar, pode ser do seu fetil. Você fala, nossa, eu vou rodar a minha aplicação. Poetry Run, FastAPI Deb, FastAPI Underline Zero, pá, dá, dá, dá, dá. É muito chato. Então, uma forma de evitar ter que escrever Poetry Run para rodar a coisa dentro do ambiente virtual, lembra que a gente tinha dado aquele...

**[00:48:02]** Inject lá atrás do Poetry Shell. A gente fez isso alguns slides para trás aqui. Aqui, a gente colocou o plug-in do Shell. Então agora a gente pode simplesmente fazer o seguinte. Poetry Shell. Não, tem que decorar, né, velho? Eu odeio ter que decorar as coisas. Aí ele falou o seguinte, olha.

**[00:48:30]** Eu habilei aqui, eu rodei num ponto, um lugar e eu ativei o shell aqui, ó. Spawning, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal, tal,

**[00:49:07]** Tá ativado. Flash API. Legal, não funciona! Isso é uma coisa que poderia ter acontecido. Saca, às vezes o ambiente virtual não funciona do jeito que a gente quer. Acontece? Lembra que eu falei? Essa aula é a favor de frustração, tá ligado? Tipo assim, as coisas dão errado. E eu tentei fazer as coisas darem errado o máximo possível hoje.

**[00:49:36]** Para você não se sentir, sabe, uma pessoa solitária em casa e fala, nossa, mano, no meu não roda, no meu não funciona. Você pode ativar esse ambiente na mão aqui, né, que foi o que a gente ia falar, vai, se eu desce poetry, envy, activate. Aí ele mostrou aonde e tal, como ativo o meu ambiente virtual, eu poderia fazer isso aqui, source, tal, tal, tal. E agora ele habilitou o meu ver envy aqui.

**[00:50:07]** Massa, você poderia rodar isso aqui também se você quiser. Se você estiver no Windows, o comando talvez não seja search. Mas aí ele vai ativar o ambiente virtual. Deixa eu sair daqui. Deixa eu sair desse shell. Vou entrar de novo aqui. E vou rodar o Inject aqui na minha máquina. ppxinject.poitrepluginshell. Vou dar um menos, menos força. Legal, agora vou voltar lá no meu Git, Fast API.

**[00:50:37]** Underline 0 e vou dar um Poetry Shell. Fast API? Ainda não funcionou, sabe? Às vezes falha. Tá tudo bem. O Fast API, o Poetry, tem um comando pra lidar com isso, que é o Poetry Self-Ed e a gente instala a extensão. Eu deixei aqui também na configuração do ambiente. Porque às vezes dá pau, mano. Eu tive que remover uns arquivos lá atrás, então você pode rodar isso aqui, ó.

**[00:51:11]** Poetry, Self-Ed, tal, tal, tal. E aí, tipo assim, se der uma coisa errada, tal, ele permite com que você abra isso aqui. Aí, falando aqui, o It's Me Piase mandou aqui. O comando Poetry Shell tem que ser rodado dentro da pasta do projeto contendo o pyproject.l. Sim, é exatamente isso aqui. É o lugar onde a gente está. É o lugar onde tem o pyproject.l.

**[00:51:43]** Então tem várias formas de escapar disso, então você tem o Poetry Invictivate que mostra como ativar, você tem o Poetry Shell que às vezes funciona, às vezes não funciona. É impressionante, aí alguém falou aqui, pare de usar o Poetry Shell porque falhava com frequência. Da galera tudo funciona bem, então é exatamente, eu vou contar um segredo para vocês aqui. Aqui ó, rodei de boa, primeira vez aqui rodando, eu vou contar um segredo para vocês.

**[00:52:12]** eu deletei um arquivo do meu poetry para conseguir simular essa situação, porque na minha sempre funciona. Eu tive que deletar um arquivo do poetry ali. Então legal, vocês rodaram um poetry shell, né? E aí ele deu aquele search, tal, tal, tal, para quem não conseguiu. Aí ele vai mostrar aqui o nome do seu ambiente virtual. Deixa eu consertar o meu aqui.

**[00:52:42]** Eu deixei um comando aqui pra resolver isso aqui. Peixel. Que abre o shell sem ele estar quebrado, né? Massa? Então legal, vamos voltar aqui na máquina aqui, onde a gente deixou o stop default aqui, eu vou startar essa máquina. Pra ver se funciona, pô, entre shell normal. Desmistificando na minha máquina funciona. Pô, eu me esforcei aqui pra simular todos os erros, porque na máquina de todo mundo dá erro sempre. Aí eu falo, na minha funciona, mano.

**[00:53:13]** Por que que na sua não? Então eu vou lá no meu FastAPI0 e aqui a gente tem o Poetry Shell. Ah, peraí. No Search File, o Director Python. Python. Aí eu preciso instalar isso aqui ó. Para funcionar do jeito que está a minha instalação aqui. Ou eu poderia fazer o Poetry Python. Instal. Tá vendo? Eu estou em outro ambiente, não é o meu. 3.13.

**[00:53:46]** Talvez agora funcione. Ah, vamos ver. Agora o Poetry Shell. No such file, Python. É por causa do apete aqui. Então, sudo apete, install. Python is Python 3. É o nome do pacote que ele queria aqui. No bonto. Eu já sou azarado, na minha nunca funciona. Ó. POSIXPEF, tal, tal, tal. Python, ó, ele tá falando de erro na versão aqui. Poetry.

**[00:54:30]** Envyuse 3.13. Aí eu estou num sistema read-only, que eu não consigo mexer aqui. Tá vendo? Tipo, é sempre complicado, tá ligado? Aí vai dando erro, vai dando coisas e tal. Vocês viram que tem jeito de sair disso aqui, né? Se tudo der errado, você pode usar o poetry run. Porque é uma opção, é a mais viável. Vamos lá, cd, git.

**[00:55:02]** Fast API, Underline 0. Aí você pode rodar o Poetry Run, Fast API, tal, tal, tal. Fast API 0, App.py. Pode dar um monte de erro aqui. Faltou deve aqui, né? Deve. Ô Regis, quer dizer que não existe um caminho único? Não, na máquina de cada um do ambiente vai dar um erro diferente, tá ligado?

**[00:55:33]** Eita, vamos entrar em Docker. Não, não vamos entrar em Docker. Mas a questão é essa, tipo assim. Eu queria mostrar pra vocês que às vezes dá errado. E aí quando dá errado, calma. Nem sempre dá pra ganhar todas. Saca. Onde eu tô aqui? CD Geet. Geet? Eu não tô na minha pasta, né? Então, na máquina de alguém funcionando aí, alguém teve algum problema bizarro parecido com esses?

**[00:56:21]** Pergunta sincero, minha máquina nunca decepciona, independente do que eu baixo, sempre dá erro. Mas é essa, essa era a coisa, tipo assim, na máquina de alguém der um erro, aqui rodou liso no WSL, aqui fala que o Fast API não está instalado, mas você instalou? Tipo, você rodou esse passo aqui, né? Tipo assim, vou mandar o comando aqui.

**[00:57:01]** Tipo assim, é esse o objetivo. Rodou ali iso e tal. Vou falar o seguinte, eu quebrei meu poetry de propósito aqui para tentar simular todos esses erros bizarros aqui. O rodou certinho, mas tarde eu vou fazer um teste no Windows and PowerShell. No Windows não deu erro, por incrível que pareça eu testei aqui antes da gente começar e funcionou bem assim. A arte WSL nunca é decepcionante, depois de fazer o poetry shell...

**[00:57:30]** Executei o Fast API, Missing Command, mas eu estava no Windows. Beleza! Mas se eu der o Inject do PPX, é importante. Para garantir que tudo funciona, nunca tive problemas com o POS. Eu também não, mas a gente vai tentando simular o erro de todo mundo. Então, Victor, talvez você não esteja no mesmo ambiente. Talvez você não esteja na pasta do projeto. Lembrando que para rodar isso aqui, você tem que estar na pasta do projeto. Você tem que ter dado o Edge.

**[00:58:08]** esse crução é delicinha não é tem que ter paciência tá ligado mas a primeira vez coisa que eu tenho na vida deu pau no meu note só com sursy com run não funciona com run tem que funcionar outra coisa né outra coisa outra coisa vou falar o seguinte se você já tinha as coisas instaladas na sua máquina atualize né porque tipo assim é uma outra problema que pode dar massa tudo certo podemos seguir aqui

**[00:58:51]** O meu funcionando aqui só é um peixão. Por isso que vale o ouro. Não, não, tem que ser sincero aqui, tá ligado? Tipo assim. Aí, rodou no Windows 7, rodou no C é onde? Legal. Massa tem várias formas da gente contornar os erros. E se alguém tiver com erro, lembra. Vai lá no grupo do Telegram. Bota lá, eu tô tentando rodar aqui. Não tá funcionando. Saca. Não tá funcionando. Eu tô rodando X, tá me retornando Y.

**[00:59:21]** Manda lá, a ideia do grupo é que a gente se apoie nesse tipo de coisa, saca? E aí a gente fica lá, tira dúvidas e conversa, senão as coisas não é nada do mesmo, tá ligado? Tipo assim, tá tudo bem, sabe? Pode acontecer de dar erro e tá tudo certo. Massa, fala hoje, tem que rodar isso aqui, deu erro. Eu tô nessa pasta, eu tô não sei o quê, e a gente vai seguindo junto pelo caminho possível. Massa?

**[00:59:50]** Nem tudo são flores, às vezes dá erro, falei paciência, calma e tudo mais. Só pra quem deu que o FastAPI não tava instalado? Provavelmente é porque não instalou o FastAPI, então tá aqui. Tem alguém aqui que não tá no grupo do Telegram? Por favor, manda o link aí que a gente vê pra outras pessoas poderem entrar. Então é legal. Beleza, FastAPI deve FastZeroApp. Funciona. Quem tiver no grupo, manda o link aí.

**[01:00:22]** pra quem não tá ainda chegou lá massa ó eu vou eu não sei se agabita aqui deixa eu abrir aqui o telegram deixa eu pegar o link do grupo aqui ó tá aí entrem lá no grupo vamos trocar a ideia a ideia que a gente consiga resolver tudo junto todo mundo certinho massa legal chegamos aqui executamos o código passamos por tudo isso junto a ideia é que quando esse comando rodar né o

**[01:01:10]** O Poetry, Run, Fast API, Dev, tal, tal, tal, ou só o comando, sem nenhuma dessas coisas. Tipo assim, você conseguiu habilitar o ambiente virtual, sem dar erro, tal. Tentei simular o máximo que deu aqui pra mim. Então, Fast API, Dev, Fast API do zero, App.py. Subiu aqui. Massa, legal.

**[01:01:43]** A gente acessa no browser, vê se funciona, de novo, estou voltando aqui, recapitulando, porque às vezes não deu alguém erro aí, e aí deu um tempo de resolver, a gente foi brincando aqui. Massa, todo mundo conseguiu ver essa tela aqui? Todo mundo conseguiu ver o Hello World no browser? Pegou o endereço que deu aqui, copia, e cola lá no navegador. A panheia mais funcionou, aqui foi, sim, Massa. Então era isso o objetivo.

**[01:02:32]** Aí a galera tá falando de colocar o ambiente virtual... Não, o ambiente virtual fica fora do projeto mesmo, é normal. É uma config padrão. Se você quiser, dá pra mudar depois. Então eu tô vendo aqui vários sims. Aqui foi sim, sofri, apanhei, mas foi... Pô, massa, lindo. Maravilhoso. Então eu vou seguir aqui. Posso seguir? Perguntando com paz e amor no coração aqui. Posso ir pra frente? Todo mundo conseguiu executar aí? Espero que sim.

**[01:03:05]** Qualquer coisa, manda lá no grupo, a gente tenta resolver junto como uma comunidade, ok? Beleza, quando a gente instala o festival, por padrão, quando a gente roda ele, lembra que ele tá aqui rodando, né? Aí ele mostrou esse tipo de coisa aqui, ele falou, olha, estamos estartando o servi...

**[01:03:30]** O Development Server, o servidor de desenvolvimento. Aí ele falou que achou uma pasta lá no meu arquivo aqui, né? Então, barra Home, barra do Nosaru, barra Git, barra tal, tal, tal. Ele falou, dentro da pasta FESHA API 0 tem um app. E lá no app tinha o app do FESHA API que estava funcionando lá.

**[01:03:50]** Então, ele está usando de dentro da Passafest API Underline 0, o arquivo, aqui ó, ponto app, dois pontos, o objeto app, que tinha lá dentro. Massa? Então, é esse caminho que ele está falando aqui, que ele está construindo aqui dentro. Então, geralmente, ele vai mostrar essa mensagem zona, assim, um testão no Shell, e aí o que ele está falando é isso. Tipo assim, estamos tartando...

**[01:04:20]** dentro do arquivo da pasta tal, tem um arquivo chamado app, dentro desse arquivo app tem uma variável chamada app. É basicamente isso que ele está falando. Serviu, subiu, a gente acessa na porta 8000 e ele falou, olha, existe a documentação do projeto. Então, se a gente copiar esse link aqui e abrir ele, deixa eu abrir em Neutab, deixa eu copiar, vai. Vamos fazer direitinho. Ele abriu uma documentação do projeto aqui.

**[01:04:50]** E aí ele falou, olha, Fast API, total, total, versão, beleza. Aí ele falou, dentro do default, que é o padrão que a gente abriu, é como a gente não nomeou nada, é default. Existe um endpoint chamado ReadHoot. Olha que massa, foi o nome que a gente deu pra ele aqui. ReadHoot. E aí, tem o get aqui, que é o método, você pode vir aqui e fazer o seguinte, try it out. Ou seja, tenta rodar aí. Tenta rodar pra nós.

**[01:05:20]** E aí você dá um execute, ó, beleza, tem que clicar no try to out primeiro, aí depois você clica no execute, e ele mostra aqui pra gente, olha, message, olá mundo, 200, deu tudo certo, então você consegue testar isso aqui e rodar os comandos e conectando as coisas pela página da documentação, ou seja, ele vai dar pra gente uma documentação executável, né? Eu vou mandar o link caso alguém tenha perdido aí.

**[01:05:47]** É isso aqui, né? É o seu localhost, 8000 barra docs. Então, ele abre essa documentação aqui pra gente. Beleza, você vai falar, pô, mas tá documentando o quê? Não tem nada, tá? Ele gerou a documentação automática da coisa simples, possível, pequena, que era isso aqui que a gente acabou de fazer. É o código que a gente tinha. E Rafa, obrigado, mano, por se tornar membro. Ó, valeu. Tamo junto.

**[01:06:21]** E aí, ele já criou a documentação, que foi o que aqui falou. Já tem doc, já. Já subiu a doc. E ele sobe dois formatos de doc. O primeiro formato de doc, a gente vai conversar sobre isso mais nas aulas que virão à frente, mas eu só queria mostrar que já funciona. Tem um outro formato de documentação, esse aqui se chama Swagger. Eu deixei aqui no slide. Ah, ok. Swagger.

**[01:06:46]** E a gente pode testar isso aqui dinamicamente, entrar na página, clicar, faz um request, ver o que retorne e tal. E aí ele tem um outro formato que também vem em padrão, que é o HIDOC. E aí o HIDOC é barra, em vez de docs, é barra HIDOC. E aí ele abre uma outra documentação, e essa documentação não é executável igual a outra, mas ela é bonitinha, né? Assim, olha, é do tipo geizão que a gente vai falar na próxima aula e tal.

**[01:07:17]** Mas aqui, retorna qualquer coisa. Aqui, você vê as coisas que estão rolando. Aqui é uma documentação mesmo. E lá no barra Docs, esse é o barra Redoc. Vou mandar aqui de novo. Esse é o barra Redoc. E no barra Docs, Docs com S, plural, Docs. No barra Docs, você consegue executar. É a documentação executável.

**[01:07:51]** Legal, então tá aqui, mostrou a resposta, a mesma resposta que daria se a gente acessasse pela Interwebs. Massa? Isso aqui é lindo, maravilhoso, está rodando, ou seja, já subiu a documentação, já está funcionando no ar, ele tem uma documentação executável e fora a função nós escrevemos três linhas de código, mano. Olha isso, olha isso!

**[01:08:23]** Não, para, para, para. É muito legal esse framework, tá ligado? Deu tudo de graça com três linhas de código, sabe? A gente colocou aqui e falou, olha, essa função é uma função normal, o Python que retorna às coisas, bota esse decorador aqui e ela ganha superpoderes de trafegar na rede, de ser documentada, de, sabe, é lindo, é massa, é simples. Aí o Swagger faz as mesmas coisas que o Postman, não.

**[01:08:53]** O Swagger é uma documentação executável. O Postman é uma biblioteca para... É uma aplicação para fazer requisições. Que eu não sou muito fã, inclusive. Legal! Perdemos muito tempo aqui, né? Mas eu digo que a gente investiu o tempo. Eu não gosto de dizer que a gente perdeu. A gente investiu o tempo fazendo tudo funcionar e tudo mais. Roda, sobe, testa, vê, vai, volta, o show não funciona, deu erro. Não sei o que lá na minha máquina. Explodiu. EpiPx, não sei o que. Legal!

**[01:09:23]** A gente terminou as coisas, viu o que dá para rodar, o Fast API viu que as coisas saem no browser, funcionam, tudo mais. Agora eu quero configurar com vocês o resto do ambiente de desenvolvimento. E aí, essa coisa aqui que foi alguém que tinha me perguntado lá no começo da aula, isso aqui serve para tudo, sim, serve para todos os projetos que você quiser mexer na vida, essa parte que a gente vai fazer agora. São boas práticas para gerenciar um ambiente de desenvolvimento saudável. Massa?

**[01:09:56]** Então legal, a gente vai usar algumas ferramentas aqui. E aí, eu já quero dizer de antemão, eu escolhi uma ferramenta que representa cada coisa que a gente pensou aqui, tá ligado? Tipo assim, ó...

**[01:10:12]** Para formatar, para fazer lint, para rodar teste, para não se aquelar. Alguém vai falar, ah, mas eu não gosto do PiTest. Igual tão aí falando, não. O outro framework, eu não sei o que. Sabe, tipo assim, eu tive que escolher uma ferramenta para cada coisa, então a gente vai usar as ferramentas que eu escolhi. Simples. Ah, mas eu não gosto do formatador do Roof, eu gosto do Black. Eu gosto do Blue. Ah, eu gosto, em vez do PiTest. Por que a gente não usa o Word? Vamos usar...

**[01:10:37]** O que eu escolhi aqui, tá ligado? Tipo assim, ah, mas, task by, eu prefiro usar Justice que é feito com Rust, beleza. Eu escolhi essas paradas aqui. Massa, é isso. Eu escolhi uma ferramenta que representa cada grupo de coisa. Você pode usar o que você quiser aí na sua máquina, mas depois eu não vou ficar dando ajuda com coisa que eu também não sei mexer, hein. Então, vamos padronizar esse ambiente aí. Beleza. Eu escolhi uma ferramenta que chama Ruff.

**[01:11:09]** E Ruff é de, sabe, o barulho que faz o trovão assim, Ruff! Ele é um linter e um formatador de código. Aí, eu teste outras e aprendo com os erros. Sim, mas não me culpe pelos seus erros. Depois. Então, o que que é um linter? É uma ferramenta que procura erros no código. Ela vai falar, hum! Por sua conta e risco, gostei.

**[01:11:40]** Sabia essa variável que você colocou aqui no código? Por que essa variável chama X? Saca? Tipo, por que chama X essa variável? Então o Linter vai olhar e vai falar tipo assim, ah, eu não gosto muito desse nome aí, hein? É nome estranho. Saca, então o Linter faz esse tipo de sugestão, nossa! E essa linha aí tem 200 caracteres, mano, é sério mesmo?

**[01:12:11]** Sabe? Ele vai forçar boas práticas. E ele tem um formatador de código que pega o código e formata nessas boas práticas que a gente gostaria que ele colocasse aqui. O paytest é uma ferramenta de... para escrever testes, um framework de testes, um test runner, ou seja, é onde a gente vai passar a maior parte do tempo. Sabe? Brincando aqui.

**[01:12:35]** Então é aqui que a gente vai escrever testes. E a gente tem o TaskPie, porque vocês viram aqui qual que é a Odisseia, né? Poetry Run, Fast API, Dev, não sei o que, não sei o que, daqui a pouco a gente vai fazer uns 15 comandos, e ninguém lembra mais o nome do comando. Então TaskPie, ele é uma coisa que cria tarefas com nomes que a gente consegue fazer. Estou tipo assim, ó, TaskServe, roda o servidor.

**[01:12:58]** Ah, lindo! Task test, roda o teste, em vez de ter que ficar pie-test.minus-cov, não sei o que, não sei o que lá, sabe? É isso. É isso. Legal? Então a primeira coisa, a primeira ferramenta que a gente vai instalar é o rough. Legal, lembrando de novo, tem que estar na pasta da onde a gente está, da onde está o pie project, o nosso projeto. E a gente vai dar um pointer, add. E aí a gente tem esse minus-minus-group. E aí, minus-minus-group, quer dizer que a gente vai instalar.

**[01:13:29]** uma ferramenta em um grupo específico. E é esse grupo que eu estou chamando de DEV, que é o grupo de desenvolvimento. Aí você vai falar, por que eu não posso dar igual ao do FastAPI? Pou e triad e FastAPI, eu tenho que dar pou e triad menos, menos grupo, deve, bref. Porque é o seguinte, quando a gente for colocar uma aplicação no ar para funcionar em produção lá no servidor, você não quer instalar a biblioteca que formata a código.

**[01:13:57]** na aplicação em produção. Só vai ficar mais pesado, vai ficar mais lento. Então, na hora de fazer o deploy, na hora de rodar a aplicação, a gente só leva o que precisa para executar. Você não quer um ambiente gigantesco. Você quer o mais simples de tudo. Então, a gente vai instalar num grupo de desenvolvimento e esse grupo de desenvolvimento a gente não bota em produção. Marcia, faz sentido? Então, vamos rodar aqui. Vamos ver o que acontece.

**[01:14:29]** a pão entre em edge menos menos group então menos menos group deve e aí a gente vai instalar o rough rough né trovão legal temos o rough aqui funcionando legal instalamos o rough e aí a gente precisa configurar ele né e aí aqui vou vou dizer bem a verdade aqui

**[01:15:00]** Aqui eu vou impor a minha vontade. Se você não gostar da minha vontade, tá tudo bem. Configura no seu. Antes que alguém já pergunte sobre isso aqui. Lá dentro do arquivo byproject.meu, a gente começa a escrever as configurações da ferramenta. Eu vou deixar aqui embaixo, aqui no fim, para ficar mais padronizado para todo mundo aqui. Então, como é que a gente configura uma ferramenta no arquivo de configuração do projeto, né? Byproject. Então, a gente coloca tu...

**[01:15:29]** que é ferramenta em inglês e eu vou falar rough aqui agora a gente vai falar o seguinte olha eu quero que toda linha de código tenha no máximo 79 colunas ou seja 79 colunas quer dizer o que? 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9 e aí se a linha tiver mais de 79 colunas ele vai falar

**[01:16:02]** Está errado. Bota em 79. Massa é isso. Bota em 79. E aí quando ele formatar o código, se você escreveu 200 caracteres, 200 colunas no arquivo, quando a gente rodar o rough, ele vai colocar em 79 caracteres. Legal? Ah, por que 79 caracteres? Porque existe uma boa prática de código em Python. Ela está descrita na PEP 8.

**[01:16:27]** PEP é Python enhancement proposal, proposta de melhoria do Python, e a PEP 8 dá o code style do Python. E por padrão, o code style do Python recomenda que todas as linhas tenham 79 caracteres. E é isso aqui que a gente vai usar. Massa, 79 caracteres ou 79 colunas por linha. E aí, aqui, eu vou colocar essa config aqui, que é o extend-exclude, ou seja, o...

**[01:16:54]** Excludes, são pastas aonde eu não quero mexer, eu não quero que ele olhe. Aí você vai falar, pô, mas que pasta é essa migrations? Nem existe, não existe ainda, mas é uma coisa que a gente vai mexer lá na frente que vai gerar código automático e vai botar dentro dessa pasta de migração. E eu não quero aquele formate código que eu não escrevi, então eu vou excluir essa pasta aqui, só por padrão.

**[01:17:22]** E aí, quando a gente vai configurar o rough aqui, aí falaram que poderia redondar para 80, mas é 80, né? É porque começa no 0. Então de 0 a 79 são exatamente 80 caracteres. Esqueceu do 0, né? Então legal, aí o que a gente quer olhar de boas práticas aqui dentro? Então eu quero olhar se os import estão em ordem alfabética.

**[01:17:56]** Ou seja, quero que import A na linha de baixo vem import B, na linha de baixo vem import C, na linha... Eu vou colocar em ordem alfabética. Então, quem faz isso é o I sort. Então, é a configuração I do rough. Aí, aqui tem o Pi Flakes, que procura por algumas coisas de boas práticas de código. Então, é F de Flakes.

**[01:18:23]** Aí a gente vai procurar por erros de estilo de código, avisos sobre estilos de código, a gente vai procurar por erros de boa prática aqui, tipo assim, aquela variável que chama x, y, aqui vai ordenar, aqui vai procurar erros, tipo, meio mirabolantes, ah, é o nome com camel case, sabe? Você escreve uma função em Python assim, def minha função, assim.

**[01:18:49]** Então, essa não é uma boa prática em Python, porque a boa prática é que as funções sejam escritas em Snakecase, ou seja, em letras minúsculas com Underline. Então, ele vai ficar checando todas essas coisas. Então, erro de boa prática e tudo mais. E o PT aqui é do PyTest. E o PL é do PyLint. Massa, então, EDI Sort, F de Flakes, E de...

**[01:19:14]** Style. W de warning. As letras não fazem sentido. Tá tudo bem, entendeu? Tá tudo bem. Tá tudo bem. E como é que a gente configura isso aqui? A gente vai criar uma outra tabela no Pi Project aqui, que é a mesma coisa, do 2.rough.link. Ou seja, são as configurações de boas práticas que a gente quer olhar.

**[01:19:44]** e a gente vai selecionar todas aquelas letrinhas que a gente colocou lá. Então é I, I sort, flake, style, warning style, pie link, pie test. Então a gente vai colocar isso aqui. E aí tem uma coisa que é preview aqui que ele mostra.

**[01:20:04]** o que tá errado no shell, então, acho que vai ser legal. A gente vai entender o que cada uma dessas coisinhas faz daqui a pouco, mas a ideia é essa, então, recomendo todas boas práticas pra gente colocar aqui. Isso serve pra qualquer projeto, não só pra esse que a gente tá fazendo, isso é importante dizer, e mantém o Cold Style padronizado. E aí que é a importância disso aqui. Ou seja, se eu escrevo com 200 caracteres e o Leon escreve com 90,

**[01:20:35]** quando formatar vai colocar o 79. Ah, se eu gosto de colocar a variável x, aí ele vai olhar por x, não. Então ele vai dar os mesmos erros para todo mundo e deixar o código padrão.

**[01:20:49]** padrão no sentido de ter integridade, olha, eu vou falar uma palavra bonita aqui agora padrão no sentido de ter integridade conceitual você vai olhar o código e o código vai parecer que foi escrito pela mesma pessoa mesmo que seja um 10 pessoas escrevendo porque ele segue um padrão mas esse é o objetivo disso aqui e aí a gente vai para uma outra parte que aquela é que mostra os erros né o linter ele mostra o que está errado e a gente tem o formatador

**[01:21:20]** que é o format, ou seja, roda aí e arruma todas essas caquinhas que a gente fez no código, linhas cumpridas, coisas erradas e tudo mais. Então, é a mesma esquema. tu.ref.format e a gente vai habilitar o preview aqui. Massa é isso aqui. E aí, por último, aqui tem um quote style.

**[01:21:45]** E o que é coach? Coach é aspas, né? Então é o estilo de aspas que você quer usar. E eu vou usar coach style single. Ou seja, eu quero escrever aspas assim, em vez de escrever aspas assim. Massa? Então a boa prática no meu projeto é que se escreva aspas simples.

**[01:22:12]** Só vai escrever aspas duplas quando você tiver que escrever. Caixa d'água. Aí você usa aspas simples. Massa legal, então é uma padronização que eu quero botar no nosso projeto. Vamos formatar usando aspas simples. Ah, mas eu prefiro aspas duplas. Tudo bem, fiz o que eu pude. Massa, lembrando de novo, são as minhas preferências de projeto.

**[01:22:38]** Aí alguém vai falar, tem alguma vantagem em usar aspas simples em vez de aspas duplas? Só gosta de aspas duplas? Quem tem? Todos os dedos na mão e as duas mãos. Tenta digitar shift aspas de olho fechado com a mão só, sem todos os dedos. Não funciona, tá ligado? Vamos deixar acessível, porque a gente pode, então deixa. Saca, legal? Então vamos usar o rough que é essa coisa que a gente configurou aqui.

**[01:23:13]** Eu vou dar o seguinte, rough, lembrando, estou no ambiente virtual, então poetry, run, rough, ou poetry shell e depois poetry run rough, a gente vai falar que a gente quer que ele cheque o nosso código, então vou falar o seguinte, cheque. Aí você pode botar o ponto ou não na frente, aí é agosto, eu tenho mania de colocar o ponto, porque eu acho que explícito é melhor do que implícito. Mas aí, olha o que ele falou aqui pra gente, ele já deu erros.

**[01:23:45]** Ele falou o seguinte, olha, Festa API 0, app, na linha 5, na coluna 1, era esperado que tivesse duas linhas em branco e tem só uma. Massa, aí ele tá falando aqui, ó. Aqui, na linha 5, tem esse erro aqui, E302. Lembra E, o que que é o E? Estyle. Tô me sentindo aquele professor de usão para lembrar do nome das coisas, né?

**[01:24:23]** estáio, é com o e. Aí ele falou, tem um erro de estilo de código. Ou seja, nas boas práticas do Python, é esperado que antes da definição de todas as funções, estejam duas linhas puladas. Então, antes de escrever uma função, pule duas linhas. Legal? Agora, se a gente rodar de novo aqui, o check, aqui, ele vai falar, olha, passou. Ou seja, se passou, significa que não tem nenhum erro. Legal, vou voltar o erro pra cá.

**[01:24:56]** e vou checar de novo. Então ele falou, tem um erro de style aqui. E aí se a gente quiser, a gente pode falar o seguinte, olha, rough, formata pra mim. Aí ele formatou o arquivo. Se a gente der o check de novo, ele falou, passou. Ou seja, quando a gente rodou, então vou deixar aqui, tudo grudadinho aqui. E aí eu vou rodar no meu shell aqui dentro, pra vocês verem a magia acontecendo aqui, né? Então poetryramrefformat.

**[01:25:29]** Aí ele fez toda a magia, ele formatou, deixou bonito. Se tivesse tudo uma gangrena, sabe aquele negócio tipo assim, aquele código que... Ninguém gosta. Olha aqui, você escreveu um código assim, pensa que o negócio é poesia, é bonito, tá ligado? Pula, tem pausas, várias linhas. Não precisa fazer um aglutinado de coisas, sabe? Se deixar tem gente que vai só aqui assim, funciona.

**[01:26:01]** Mas, aí você pede pelo formatar e ele fala, pera aí. Ah, tranquilo, deixa bonitinho aí pra nós. Ou seja, então ele vai ficar procurando esses erros assim. Se a gente deixasse daquele jeito que tava, toda grana no código aqui ó, vou colocar aqui o check. E aí você vai ver que ele deu vários erros aqui ó. Aí ele falou o seguinte ó.

**[01:26:27]** Você tá botando o import, tá colocando o código no lugar que não é pra colocar porque a linha de import, então ele deu I. O que que é I? Ah, e sorte, né? Então deu erro de import. Aí depois ele falou o seguinte, olha, tem o edge style aqui, 702, você definiu muitas coisas na mesma linha usando semicolum, né? Que é ponto e vírgula. Aí depois ele falou, olha, se você for usar ponto e vírgula tem que colocar o espaço, pelo menos isso, né?

**[01:26:55]** Então ele foi dando vários erros aqui, e aí o legal é gente lendo os erros e ver o que aconteceu em cada lugar. Mas você pode vir aqui, rodar o format, e ele fala, blum, pronto, limpo, lindo, maravilhoso. Parece que eu sei escrever um código Python charmoso. Então essa é a função do ref. Mostrar os erros de estilo de código...

**[01:27:17]** e também arrumar as coisinhas quando a gente usa o formatador. Aí, lembra que eu falei que eu queria aspas simples? Toda vez que ele encontrar aspas duplas, se for possível, ele converte em aspas simples. Então, mantenha a padronização, aquela integridade de conceitual. Aquela coisa lindinha, bonitinha. Legal? Aí o Roof é assim. Agora entra o PiTest.

**[01:27:44]** Pling! É, gostei! Bei! O pai teste é o framework de teste que a gente vai usar, então nada mais justo do que a gente instalar ele também, porque a gente está configurando um ambiente de desenvolvimento. Então poetry add-group deve, aí a gente vai instalar o pai teste, que é a ferramenta que a gente vai usar para escrever testes, e a gente vai usar o pai teste cove.

**[01:28:08]** e Cove é de Coverage, ou Coverage, quem quiser falar bonito assim, Luciana Gimenez, mas é a cobertura de código, ou seja, eu testei isso aqui, a gente vai vendo isso no decorrer das aulas, mas é tipo assim, será que eu testei isso aqui? Acho que talvez, pode ser que sim. Aí o Cove, esse plug-in do Bytesh, ele disse se a gente testou um bloco de código ou não, então é maravilhinho, então, por que não?

**[01:28:38]** Então legal, o Poetry Edge Group, então a gente vai instalar o PiTest e o PiTestCov. Legal, aí ele instalou o Coverage, que é uma outra coisa, o Plug, que é o que pluga os plugins. E é isso. E aí a gente vai configurar o PiTest, que é uma outra coisa, pra falar, olha, toda vez que eu rodar o comando PiTest, execute daqui, o ponto é aqui, né, nesse lugar. Então a gente vai colocar isso aqui.

**[01:29:14]** Então eu vou copiar aqui, vai, vamos lá, mais rápido. Então a gente está aqui, oh, pull of tu, ou seja, tu, a ferramenta, pai teste, então, inoptions, as opções de inicialização, quer dizer que a gente vai rodar. O Python.pf é aqui, ou seja, exatamente aonde estamos executando, o ponto significa isso. Então quando eu rodar, pai teste, ele sabe que a pasta que ele tem que rodar é a pasta onde está o pai project.toml.

**[01:29:47]** Aí ele roda. Massa. E aí eu coloquei isso aqui, um add-opt, então adicione opções e eu quero tirar o warning aqui. E às vezes uma biblioteca que a gente usa tem uma coisa deprecada e aí fica um monte de mensagem na tela. Isso aqui é opcional, você não precisa colocar. Eu só estou colocando para não ficar aparecendo mensagens esquisitas no meio do curso que não tem nada a ver com as coisas que a gente quer fazer. Saca!

**[01:30:13]** Esse rough pode ser usado para refatorar o codebase da empresa? Pode! Se você quiser ser a pessoa que está em todos os blames do código da empresa, você pode fazer isso. Seria bom separar esses grupos de teste de dev no Poetry? É porque teste é desenvolvimento, né? Se você quiser, você pode fazer isso. Eu... Eu geralmente tudo o que é de dev eu boto em dev, né? Testas pra mim é uma etapa de desenvolvimento. Legal, então configurando o pie-test...

**[01:30:46]** E aí, olha que massa aqui, a gente vai rodar o pai teste. Lembra que eu falei que tinha um monte de comando e que precisava ficar decorando? Como é que roda o pai teste? Pai teste, ponto. Vamos lá, pai teste. Ou seja, não precisa botar o ponto porque a gente falou que o pai Dompef é aqui. Então, pai teste. Ele falou, não coletei nada. No tests run. Ou seja, não rodou nenhum teste.

**[01:31:12]** Então, eu vou fazer o seguinte, eu vou colocar aqui, menos, menos, cove, ou seja, eu quero saber o que do meu código não está testado. Provavelmente nada, porque... A gente não escreveu nenhum teste. Mas eu vou falar o seguinte, eu quero que seja a nossa pastinha lá, né? Então, a nossa pastinha do curso agora é FastAPI, né? Então, FastAPI, Underline Zero.

**[01:31:38]** E aí eu vou falar o seguinte, mostra um monte de informação aí pra mim, o menos veia de verbozo, verbozo quer dizer que é chato, sabe? Fica aí, falando pra caralho, verbo rágico, sabe? Fala muito, eu gosto disso. Aí ele falou o seguinte, olha, rodou, aí ele falou que não rodou nenhum teste, mas ele deu um resultado muito massa aqui pra gente, ele falou o seguinte, olha,

**[01:32:03]** Tem cinco statements. O que quer dizer? Statements é linha de código. Vamos lá no código? A gente tem cinco statements. Uma linha, duas linhas, três linhas, quatro linhas, cinco linhas. Ou seja, embora a gente tenha oito linhas, a gente só tem cinco, que são efetivamente código, né? Então, a gente roda isso aqui. E aí ele falou, olha, lá nesse arquivo, app.py, tem cinco statements e tem miss. Ou seja, a gente perdeu todos. E aí...

**[01:32:37]** 0%. Ou seja, a gente não tá testando nada, não deu nada. Se a gente quiser ver, a gente pode ver isso de uma forma bonita. Coverage HTML. Aí ele falou pra gente, olha, escrevi um arquivo aqui, html.cobindex. Aí você pode vir aqui no seu browser e abrir esse arquivo.

**[01:33:01]** Ou se você for alguém como eu, você faz isso aqui, ó. Ah, esse é o browser que eu estou usando aqui, então eu vou lá no html-cov-index. Aí ele abriu esse arquivo no browser. Mas nada impede você vir aqui no browser e dar control-o e buscar o arquivo também, não precisa ser sadomasoquista, fica abrindo tudo no show. Mas basicamente ele falou o seguinte, olha, esses são os arquivos que tem no nosso projeto. Esse é o app.py, que a gente tem 5 statements e perdeu 5.

**[01:33:27]** olha que massa se a gente clica nele ele tá falando pra gente olha de todo nosso arquivo a gente tem cinco missings ou seja perdemos tudo a gente não tá testando nada sabe aquele código bonito bom assim nasce que você manda pra produção e fala quem testa o cliente na minha máquina funciona é basicamente assim tudo vermelho não escreveu nenhum teste legal massa a gente vai resolver isso mas

**[01:33:55]** É interessante vocês saberem que dá para ver isso aqui. E isso aqui se chama cobertura de código. Vou voltar lá para os slides. Agora, a gente entra no Tasking, pai. E é Tasking, pai. Não é Tasking, pai. É Tasking, pai. Com I. Tenho I no meio. I. Não se esqueça que tem um I aqui. Massa, é possível importar esse tool config dentro do arquivo? Você poderia fazer. É o que as ferramentas fazem.

**[01:34:34]** Quando faz isso aqui, quem testa é o cliente, pelo amor de Deus, mano. Eu nunca quero ouvir vocês falando isso, mano. Por favor.

**[01:34:41]** Aqui é o momento de aprender a boa prática. Então, cês lembram aqui? Pô, como é que roda o projeto? Cê lembra agora? FastAPI dev Fast0APIAPI.py Como é que roda o checador? RoughCheck. Como é que formata? RoughFormat. Como é que testa? Pai teste menos menos cove igual a FastAPI underline zero menos vvv. Como é que gera cobertura?

**[01:35:12]** Covereis de HTML. Pô! Vocês já viram que isso aqui. Quem é que quer lembrar esses comandos aqui, né? Não, não. Pelo amor de Deus. Eu não quero saber, mano. Eu não quero, sabe? Tipo assim, pô, por que, mano? Todos esses comandos, tá ligado? Sabe... O testepay, ele é uma solução pra isso no sentido de tipo assim. Eu não me odeio. Então eu vou fazer os comandos tipo assim. Run. Test. Pô, eu não quero ficar rodando. Pai, teste, cove, tal, tal, tal, tal, tal, tal, tal. Pô, não, não.

**[01:35:46]** Então, a gente vai adicionar ele lá no grupo, né? Então, a gente vai dar um poetry edge groupie, menos menos deve, taskie, pai, massa, lindo, maravilhoso, vamos lá. Então, poetry edge, menos menos groupie, é taskie, e, e, taskie, não esquece o i, porque pros fluentes em inglês não tem i aqui no meio. Taskie, pai.

**[01:36:17]** Ah, legal, criei um grupo TaskPy, esqueci o deve, falei, tanto esqueci o deve. Legal, espero que ele não tenha criado um arquivo aqui pra mim. Não, tá tudo certinho. E aí aqui no TaskPy, a gente pode falar o seguinte, olha, chamo o comando link pra mim. Vamos lá configurar isso, alguém? Então a gente vai criar de novo aqui um tool, aí ponto TaskPy.

**[01:36:48]** vai criar as tasks aqui e aí a gente tem aqui o lint aí a partir de agora toda vez que eu quiser rodar o linter eu não preciso escrever rough check eu chamo task lint em vez de saber rough checking é ponto sem ponto legal é task lint legal executa uma tarefa executa uma task qual task lint simples vir um comando maravilhoso lindo bonito

**[01:37:22]** Aí você... Pô, qual que é o comando de formatação? Format. Task Format. Lindo! Isso aqui? Não, não, pera. Pô, vocês acham mesmo que eu ia ficar rodando, escrevendo, toda vez, Fast API, Dev, Fast API, Underline Zero. Pô, não, não, não, não, não. Run, né? Run! Por favor, run! E aqui é o nosso projeto de Fast API Zero, né? Legal! Task...

**[01:37:57]** Run. Bota o servidor de pé. Pô, que massa! Ah, mas eu não tô no ambiente virtual. Poetry Run Task Run. Pô, isso aqui é lindo, isso aqui é maravilhoso. Quem nunca tinha usado o TaskPie aí, levanta a mão aí no chat, pra eu saber. Se a empolgação de quem nunca tinha usado isso é tão grande quanto a minha todos os dias que eu uso, né? É, pode ser, pode ser que você goste. Eu amo.

**[01:38:29]** E aí a gente tem o task test, né? Que é aquele mesmo comando que a gente já tinha visto, né? Feste API, da, da, da, aqui é Feste API zero, né? Lembrando que eu coloquei o nome diferente de propósito. Legal! Aí aqui eu coloquei mais umas opções aqui pra deixar aqui, né? O menos S é pra mostrar o STD alt, o menos X é pra parar quando falha. Massa? Legal! É isso aqui, vou deixar esses comandos. Pô!

**[01:39:03]** Task test. Ó, maravilhoso. Lindo, bonito. Aí agora vem o momento. Existem comandos chamados pré e post. Agora a coisa fica linda. Ou seja, eu posso rodar um comando antes do outro comando ou depois. Ou seja, depois do teste, lembra que tinha que gerar o covereio de HTML para saber se ele funcionava?

**[01:39:47]** Legal, agora não preciso mais. Se o comando de teste der certo, porque nem sempre ele vai dar, ele gera o post teste. Falas que teste, ele não gerou o coverage. Por quê? Porque não deu certo o comando, né? Ele não rodou nenhum teste. Aí a gente tem o post teste. Aí ele gera. Mas, em teoria, só o teste vai ser suficiente. E a gente tem o pré teste, né? Pré teste. Que roda um comando antes do teste.

**[01:40:18]** Ou seja, antes do teste, vê se a formatação está certa. Se a formatação estiver certa, a gente roda o teste. Se não, ele quebra. Vamos quebrar a nossa aplicação aqui, deixa bem daquele jeito assim. Legal. Então, vou rodar o teste aqui. Então, um task... Vamos lá. Put, run, task, test. Aí ele falou... Ele não rodou o teste. Por que que ele não rodou o teste? Porque deu erro antes.

**[01:40:43]** no pré teste, no lente. Ou seja, ele vai ficar executando o pré antes, se o pré funcionar, ou seja, se o código estiver bem bonitinho, no CodeStyle da galera, ele roda o teste. Se ele não tiver, ele quebra antes. E aí, se o teste rodar com sucesso, ele roda o PostTest e gera aquele HTML pra gente. Então, ele funciona como uma cadeia, né? Se o primeiro der certo, ele roda o segundo, se o segundo der certo, ele roda o terceiro.

**[01:41:13]** pré-task e post-task. Então, aí ele vai funcionando, alinhando as coisas. Então, funciona muito bem, assim. E aí, no final, eu queria que a coisa ficasse parecida com essa. E deixa eu agradecer o Chax aqui para virar membro. Ó, valeu demais, mano. Tamo junto. E aí, a minha configuração final é isso aqui, que eu vou deixar. Então, a gente vai ter o lint, o format e o test, o pretest e o post test que a gente já criou.

**[01:41:47]** E aí eu vou criar um preformat que corrige umas outras coisinhas antes. Aí mandar uma pergunta. Tem alguma vantagem em usar o TaskPie no lugar do Makefile? Tem, você não precisa instalar o Makefile. Isso aqui você instala junto com o projeto, porque é Python, né? O Makefile é uma ferramenta externa que não funciona em todos os sistemas operacionais, tipo assim. Já tentou rodar o Make no Windows? Você vai descobrir que nem tudo funciona da forma como você quer.

**[01:42:25]** Então, legal, aí a gente roda aqui o task lint. E aí, ele lintou aqui. Se a gente der o format, ele roda algum comando antes. E assim ele vai entrando nessa cadeia de coisas aqui dentro. Massa, maravilhoso. Então, essa é a ideia. Então, em vez de ter que ficar toda vez sofrendo com qualquer coisa lá, tipo assim, ah, mas aí eu preciso rodar o make, tal nos organes, lá de cinco comandos. Não, é simples.

**[01:42:57]** Quer testar rodo teste, ele rodo preteste ou post teste? Quer formatar, rodo format, ele rodo pré-format. Quer lintar, rodo lint. Lindo, maravilhoso, simples, bonito, ó. Perfeito. Legal, então esse é o Test Kipai. Com isso, eu finalizo a nossa ideia de configuração do projeto. Agora a gente volta pro código, né? Porque a gente configurou um monte de coisa e tal, mas a gente não sabe se tá funcionando. A gente não escreveu nenhum teste. Você lembra?

**[01:43:32]** Top, já passei raiva com indão no make. É, acontece. Lembra? Isso aqui é a nossa cobertura de teste. Ou seja, não tem nada. Não tem nada. Tá tudo feio. Legal, vamos escrever um teste? Pra mostrar pra vocês que não é nenhum bicho de sete cabeças escrever um teste, a gente tá desmistificando várias coisas aqui, deixando tudo bonitinho, assim. Por que não fazer um teste? Então, legal. O Fast API, ele é lindo, maravilhoso, cremoso, porque ele já tem um cliente de teste.

**[01:44:02]** Então, a gente pode vir aqui dentro da nossa pastinha Testes. Legal? Então, aqui, a gente estava no FastAPI0, agora eu vou vir aqui na pastinha de Test. E aí, eu vou criar aqui um arquivo, todo arquivo do PyTest, por padrão, tem que começar com o nome TestUnderline. Então, é TestUnderline. Aí, TestUnderline, o quê? A gente está testando o app. Então, eu vou deixar como TestApp.py. Sabe o nome simples?

**[01:44:31]** bonitinho para a gente começar algumas coisas aqui. Então, legal, para eu testar a minha aplicação, eu preciso conseguir acessar a aplicação. Então, o Fast API tem uma coisa que chama Test Client. Então, vamos lá. From FastAPI.testClient import TestClient. Legal. E aí, lá da minha aplicação agora, eu vou importar o nosso arquivo, né? O nosso app, que é o que a gente quer testar. Esse app aqui.

**[01:45:00]** Então, eu preciso acessar que ela pasta lá, então como que ela chama? FastAPI0. Então, from... Opa! Estou digitando coisas em lugares esquisitos. From FastAPI0, que é o nome do nosso projeto, ponto app, que é o nome do nosso arquivo, import app, que é o nome da nossa variável.

**[01:45:28]** Massa, então eu estou pegando isso aqui e trazendo para cá. Perguntaram qual que é a diferença do FastAPI Client do próprio PiTest. Porque o Client do PiTest não é o Client do FastAPI, então... E o FastAPI... E o PiTest não tem Client, né? É... Algumas outras coisas que dão esse cliente para ele. Por padrão, não existe uma fix, seu chamado Client. Massa, aí eu vou pegar o meu teste Client aqui e vou falar o seguinte, olha...

**[01:45:57]** Esse é o meu cliente, cliente. Então, passa para mim o app que a gente tinha lá. Legal, massa. Com isso agora, o Fast API, teste cliente, importou a nossa coisa aqui, esse app que a gente tinha, e transformou esse app num cliente que a gente consegue conversar com ele. Se a gente rodar o teste agora, você vai ver que deu erro aqui, ó. Falou, ó, organize isso aí, está errado. Formate.

**[01:46:34]** Tudo bem, desculpa, não estou mais aqui, format. Legal, ó, precisava pular uma linha, porque a boa prática do import é assim, primeiro as coisas de fora, aí pula uma linha as suas coisas que você escreveu, ou seja, isso aqui é biblioteca, isso aqui é meu, então pula-se uma linha. Massa, então vamos lá, tosque teste, aí ele falou o seguinte, olha.

**[01:47:01]** Rodei umas coisas aqui, mas eu não rodei nenhum teste, porque eu não escrevi nenhum teste ainda. A gente só fez esses imports muito malucos. Só que com esses imports, vamos rodar o post-test, porque o teste deu errado, então vamos rodar o post-test. Ele escreveu post-test, noDataReport, ou seja, não escreveu nada, não tem nenhum teste. Deu tudo errado. Coverage, HTML, noDataTrueReport, porque não tem teste.

**[01:47:33]** Bem, a gente escreveu o código no arquivo de test, mas não tem teste, porque todo teste precisa ser uma função em Python. E aí a gente vai testar essa função e ver se ela funciona da maneira como a gente quer que funcione. Ou seja, quando a gente chama isso aqui, vamos lá, então def, teste, todo teste do Python test também tem que começar com o nome test underline. Então vamos falar o seguinte, olha, def, test underline, e aí eu coloquei o nome aqui. Root, que é o nome da coisa que a gente tinha chamado aqui, né?

**[01:48:06]** Ou seja, root é barra, é a primeira barra da coisa. Então teste root, aí a gente pode escrever o seguinte, deve retornar, olá mundo. Massa, não é isso o que precisava fazer? Então a gente precisa que ele retorne, olá mundo, a mensagem que a gente tinha lá. Então eu vou trazer esse cliente aqui pra dentro assim ó.

**[01:48:31]** E aí eu vou falar o seguinte, olha, cliente, faz uma requisição para mim aqui, cliente.get, chama o get, ou seja, lembra? Isso aqui é get, get. Então vai lá na função que tem o invólucro, né? O wrapper, a coisa em volta, que corresponde a esse barra aqui.

**[01:48:54]** precisava do poet... Não, a gente tá fazendo de vários jeitos aqui. Não precisa, se você tiver num ambiente virtual ativo, não precisa. Então eu vou falar o seguinte, olha, vai lá e faz uma requisição nesse esquema aí. E aí eu vou pegar o re-s-ponse, ou seja, a resposta disso aqui. E aí eu vou falar o seguinte, assert, que é uma palavra garanta, que o que veio aqui no response...

**[01:49:23]** Lembra que a gente retorna uma coisa que é um JSON, né? Um parecido com o dicionário. Então, JSON é igual, igual a... Message... Olá, mundo! Mas eu acho que é isso, né? Eu acho que é isso. Quero conversar mais com vocês sobre essas coisas aqui, mas pera aí, é só pra gente ver se tá testando, se tá funcionando. Ahm... Deixa eu habilitar o ambiente virtual aqui, então vamos lá. Task... Test. Aí ele falou, ó, tá com erro, mano.

**[01:49:56]** tá mal diagramado esse código aqui porque tem um pedaço em branco aqui legal a gente tira legal aí ele rodou o teste e deu erro olha que massa ele falou o seguinte olha a mensagem que veio no app aqui é olá mundo a está vendo que quando a gente mandou ele falar um montão no menos verboso ele mostra aqui pra gente ele falou ó

**[01:50:22]** A mensagem que veio, a mensagem que a gente está esperando aqui, olá mundo, não é a mesma que veio lá, porque lá veio o, o, lá mundo, né, maiúsculo assim, né. Então a gente tinha esse erro aqui, o, lá mundo. Então vamos rodar de novo aqui. Legal, não funcionou ainda, porque o olá mundo que veio lá da aplicação tinha um ponto de exclamação no final. E ele tá aqui ó, dando a diferença aqui ó, é aqui, é aqui, ele tá falando pra gente.

**[01:50:52]** Então, a gente tem aqui que vir aqui e colocar Tchê, né? Aqui, olá mundo. Taos que teste, rodou, passou. Massa, lindo, maravilhoso, incrível, divino. E aí ele tá dando aqui, é porque aqui ele deu um erro aqui, né? Que ele falou o seguinte, olha. No data to report. E aí aqui ele precisava fazer o fest API, né? Que é o nome do nosso projeto. Lembrando que eu mudei o nome da pasta, né?

**[01:51:21]** A enchinha é corrigido isso, mas depois eu copiei e colei e dei uma errada. Legal, então agora ele vai mostrar pra gente aqui no final, aqui ó. Roach, esse é o post test, né? Então ele rodou, falou ó, um teste passou e ele escreveu Roach, HTML, post test, tal, tal, tal. Vamos lá no navegador agora de novo e vamos dar um F5 aqui nesse arquivo? Legal, ou seja, ele rodou e executou tudo aqui. Ou seja, tudo tá testado, porque ele passou por todas as linhas enquanto estava fazendo esse tipo de coisa.

**[01:51:52]** Mas tudo funciona muito bem. E aí, antes da gente terminar esse teste aqui, eu queria explicar um pouco pra vocês sobre o que está acontecendo nesse teste. Embora a gente precise de um conhecimento de HTTP que a gente vai ter na próxima aula, é interessante eu discutir com vocês a taxonomia do teste. Como é que esse teste acontece, né? O teste que a gente está usando aqui, ele é basicamente um teste de três etapas, né? Então, eu vou escrever aqui assim.

**[01:52:22]** esse teste tem três etapas. A gente costuma chamar isso aqui de AAA. Então no primeiro A a gente tem o arrange, no segundo A a gente tem o act e no terceiro A a gente tem o arrange, act, assert. Massa? No run está errado também? Ah, obrigado.

**[01:52:54]** É o famoso copicola, em vez de mexer. Obrigado, Leandro. Então, a gente tem isso aqui. O Arrange Act Assert. Ou seja, para chamar a função que a gente quer chamar aqui, que é quem está com o invólucro do barra, a gente precisa configurar algumas coisas antes. Então, isso aqui é o arranjo da coisa aqui. Ou seja, o que a gente precisa antes disso aqui? Então, esse é a fase de Arrange.

**[01:53:27]** Aí o que que acontece? Depois que a gente passou, conseguiu as coisas que a gente queria, a gente precisa afirmar alguma coisa, a gente precisa agir, ou seja, chama o bloco de código, que a gente quer testar, né? Isso aqui, na teoria de testa, a gente vai chamar de SUD, que é o System Under Test, a coisa que está sendo testada. A gente vai conversar sobre isso nas próximas aulas, nos quinhentas a cabeça. Mas é só uma introduçãozinho aqui. Então, aqui a gente...

**[01:53:57]** aciona, age, faz com que a coisa que a gente quer testar seja executada. Então, executa a coisa, o su-t, system-andertest. E aqui no final, a gente quer dar o assert, ou seja, assert é fazer uma afirmação, é uma garantia. Então, garanta que a é a. Ou seja, garanta que algo é aquela coisa. Então, garanta que algo é algo aquilo que a gente quer especificamente seja

**[01:54:28]** resolvido, respondido aqui, né? Então, essa é a ideia. Então, aqui a gente carregou os dados que a gente precisava para testar, aqui a gente fez o Act, ou seja, a ação do teste, e aqui a gente tem o Assert, que é a garantia de que essa coisa está funcionando como deveria estar. Uma outra coisa que a gente poderia ver aqui, né, tipo assim, dentro dessa parte dos testes,

**[01:54:54]** É o seguinte, bem, se a resposta do servidor é a mesma que a gente queria aqui, se é o status code. Então eu vou garantir isso com vocês e falar o seguinte, olha, para quem já é mais conhecido do...

**[01:55:09]** dos HTTP, a gente vai falar sobre tudo isso na aula que vem, hein? É só o preview, aqui, né? Então, a gente tem o response.status code, a gente quer garantir que isso aqui veio OK. Então, a gente pode vir aqui da biblioteca do Python e fazer o seguinte, olha, fromhttp.htttpstatus. Importhtttpstatus, a gente fala, olha, deu certo a requisição.htttp.ok.

**[01:55:36]** Mas, assim, então, a gente garante que veio a resposta que a gente esperava, ou seja, que deu bom 200. Esse é um teste bem simples, né? Mas eu espero que dê para pegar aqui a ideia, a essência do negócio. Arrange, Act, Assert. Então, arruma a casa, chama o que precisa chamar e garante que o que precisava funcionar funciona. Se a gente der o teste que teste...

**[01:56:00]** ele garantiu e falou, olha, veio o Lamundo quando a gente agiu, chamou essa função que estava em VOLUCRO aqui, do get barra, foi o que a gente fez, chamou get barra e aqui a gente configurou as coisas que a gente precisava para esse tipo de momento aqui para poder executar o teste. Massa!

**[01:56:27]** E aí, essa é a arquitetura de um teste. Geralmente, ela é feita dessa forma. Então, arrange, act, assert. Algumas coisas têm... Algumas teorias de teste, algumas outras escolas vão dizer que o teste não tem três, tem quatro fases. Que é o setup, exercising, assert, tear down. Aí, geralmente, a gente usa essa híbrida aqui. 3.4, arrange, act, assert, tear down.

**[01:56:57]** Se for preciso, né? Então essa é a ideia da estrutura de um teste com Fast API aqui. Então legal, pra gente finalizar, embora pra casa, eu quero comitar esse projeto aqui com vocês, né? Vamos subir ele no Git, para as outras pessoas poderem ver e tudo mais, né? Então eu vou subir aqui, então vamos lá. Eu vou rodar com Pipe X, eu vou instalar uma coisinha, eu só vou rodar uma coisinha que se chama IGNR. IGNR significa Ignore.

**[01:57:24]** Ou seja, eu vou criar um arquivo com coisas que eu não quero subir para o repositório. Se vocês forem olhar o projeto, depois que a gente começa a importar, as coisas, ele fica todo sujo aqui, ó. Tem esse paycache, eu não quero subir o Coverage para o repositório. E, sabe, tem coisas que eu não quero ir para lá, se a gente der um shift, a gente vai ver que tem aqui cache do paytest, cache do roof, sabe? Eu não quero subir essas coisas para lá. Então, o IGNR é uma biblioteca que resolve esse tipo de problema. Ou seja, bota dentro de um arquivo as coisas que a gente quer ignorar. Então...

**[01:57:56]** Como a gente só vai rodar isso uma vez, o PPX pode executar uma biblioteca externa de terceiros, então a gente vai fazer o seguinte. PPX, RAM e GNR. Ah, PPX, RAM e GNR. Peraí que eu fiz alguma coisinha aqui. Ah, tá, bem legal. Pra chamar o GNR, eu preciso passar pra ele o que eu quero ignorar, né? Então, eu quero ignorar os arquivos Python, menos P, Python.

**[01:58:27]** Aí ele gerou, ignora o cache do Ruff, ignora as variáveis de ambiente, ignora os Pi Package, Pi Project, todas aquelas coisinhas aqui. Então ele cria um arquivo pra gente certinho. Então o que você precisa fazer é colocar isso no arquivo do Git chamado Git e Ignore, com um ponto no começo. Ele precisa ser um arquivo oculto aqui dentro. Legal?

**[01:58:53]** Aí ele criou um arquivo aqui no nosso repositório, no nosso projeto que é oculto aqui, tá aqui. Ignore. Ou seja, todos aqueles paycash que a gente tinha lá e não vai subir o rough, o paytest para ficar limpo o nosso repositório e subir só as coisinhas bonitinhas. E aí eu vou dar um git init aqui para a gente começar um repositório novo. Então git init.

**[01:59:20]** Ponto, criamos um repositório a partir de agora. E aí ele falou o seguinte, tem seis arquivos aqui, git, status, então são esses aqui. O teste, o pyproject, o lock, o fest0 que é a nossa pastinha, o readme, e o ignore. Massa, e aí eu vou usar uma ferramentinha que se chama gh, você pode fazer isso na mão e lá no site do git hub, criar as coisinhas, eu vou usar o gh repo create aqui. Ele vai perguntar, cria um novo repositório pro...

**[01:59:52]** From scratch e tal. E tudo mais. Então eu vou falar o seguinte, olha. PUSH, ou seja, SOB. Esse repositório que a gente está aqui, local, que a gente acabou de criar, git init, pro git hub. Certinho. Aí ele vai falar, onde está? Lembra o ponto, é onde a gente está agora, no local. Aí vai ser Fast API Underline Zero. Aí eu vou criar na minha conta. Talvez não apareça as opções para vocês, mas eu vou criar aqui no... do NoSauro.

**[02:00:24]** Aí o description, apresentação de FastAPI 2025. Ação do curso, vai. Massa? Vai ser público? Quero adicionar o remoto? Quero que ele suba, configure todas as coisas pra mim lá no GitHub? Sim. Vai ser orange? Ok. Adicionou o remoto pra lá, então já tá tudo certinho. Ele já criou o repositório lá no Git, tudo mais. Se a gente for lá na minha conta no Git, vou pegar aqui, ó.

**[02:01:03]** Ele criou aqui, git hub do no sauro, aqui ó, esse é o RL do repositório. Vou mandar aqui pra vocês, vocês quiserem olhar. Opa, tá aqui. Tá aqui, o meu repositório tá aqui, foi criado, só que ele tá vazio, né? Então eu vou dar um git, edge, ponto, pra adicionar tudo que a gente criou aqui, git commit-m, criando, repositório. Aí eu vou colocar aqui aula01, criando o repositório.

**[02:01:41]** Legal, aí ele vai subir tudo isso pra lá, vou dar um gitpush e todo mundo consegue acessar, né? Aí ele tá falando, ó, você quer subir pra orange? Lembra que ele perguntou aqui atrás? Você quer que isso aqui se chame Origin? Sim, então eu quero subir pra lá. Gitpush set upstream, Origin main. Massa, tá aqui o resultado da nossa aula de hoje aqui. Pei! Eu tinha esquecido que eu tinha colocado isso aqui.

**[02:02:15]** Então, a ideia inicial é essa, você cria seu repositório, sobe, e agora a gente está com tudo configurado, né? A gente está com o... o FESHIPI configurado, as coisas, as bibliotecas, todos os roledsinhos, todas as coisas que a gente precisava fazer, e subiu isso aqui para lá. Então, legal, no final das contas, o ideal é que todo mundo tenha conseguido subir seu repositório. Essa é a missão dessa aula, olha. E aí tem um exercício, claro, porque toda aula tem exercício.

**[02:02:45]** Então, o exercício dessa aula é terminar esse pedaço, né? Que a gente fez junto aqui. Então, cria um repositório para acompanhar o curso, né? Ou seja, bota teu nome, tuas coisinhas, sua configuração, as coisas que você fez e sobe para uma plataforma. Pode ser o GitHub se você tiver conta no GitHub, mas pode ser no GitHub Labs se você não gostar do GitHub, pode ser no Codeberg se você odeia código proprietário.

**[02:03:11]** E a ideia é que você compartilhe isso com a gente lá no eixo 91 do repositorio. Vamos ver aqui, então a gente está aqui no do Nossauro, aí tem aqui o Fast API 2.0, aí a gente tem aqui umas eixos e tem uma eixo que é eixo 91 aqui de número 91. E aí todo mundo que fez o curso colocou aqui o seu próprio repositorio.

**[02:03:37]** Então, tem uma galera aqui, tipo, mais de 300 pessoas, linkaram os repositórios aqui, e aí você pode ir vendo, aprendendo com as outras pessoas e tal. Tá tudo aqui. O navegante que estava aqui no chat, o Rafael, ele tá aqui também, ó. Então, todo mundo que tá aqui, fez o curso em algum momento, e tá todas as referências de todo mundo. Você pode ir lá e ver o nome que a pessoa deu, que ferramenta que ela escolheu, se ela deixou de fazer de um jeito ou de outro. Então, tá tudo aqui. Essa é a primeira...

**[02:04:08]** Essa é a primeira lição, é o nosso primeiro exercício. Chegar no fim da configuração e subir no repositório do Git, público, para a gente poder compartilhar e trocar experiências. O Ricardo falou, colocou hoje o dele aqui. Olha eu ali, tá todo mundo aí. Pô, massa, legal, não? Pô, bastante gente fez esse material, então... Tá muito legal. Esse é o primeiro exercício. E aí, todo mundo tem que responder o quiz dessa aula aqui, de preferência, é isso.

**[02:04:41]** Então, tem algumas perguntas aqui para vocês responderem depois com calma. Lembra? No final de semana, no final de semana aí, não precisa ser agora, vai descansar. Então, qual é a função do PPX? Qual é a função do Poetry? O que que faz o comando FastAPI Dev? Ao que se refere o endereço 127, o que que faz o group Dev? Qual a função do TaskPy? O payTest é o quê? Qual a ordem de execução de um teste? O que que faz essa linha aqui no código? Então...

**[02:05:12]** tem aqui o quiz pra você pegar e fixar algumas coisas essa aula é muito comprida porque tem que saber se está tudo funcionando e tal então tipo assim ela não é fluida então meio que dá pra ir pegando as coisas e vendo tudo certinho pontinho por pontinho né Leon muito obrigado mano pelo teu super chat tamo junto ó valeu meu querido e aí

**[02:05:41]** Antes da gente ir embora, tem alguma coisa aqui que é suplementar para a próxima semana de maneira geral. Eu sei que a gente, eu quero explicar na semana que vem como que funciona um teste, o que é aquele negócio de arrange, act, asserte, o que que é o negócio de HTTP, viu, get, retorno ok e tudo mais, a gente vai ver tudo isso na semana que vem.

**[02:06:09]** Mas, por encontro de entretanto, todavia, tem o material suplementar aqui. Ele está lá na página da aula, se você quiser, você não quiser abrir os slides, né? Está aqui, ó, na página da aula, aqui, configuração. Aqui embaixo, tem o material suplementar.

**[02:06:26]** Então é assim, eu sei que nem todo mundo tem tempo, mas fala, pô, tô meio perdido nessa parada aí. Eu acho que eu preciso de uma base para poder acompanhar esse rolêzinho aí. Então tá sempre aqui. Todas as aulas, basicamente, têm essa parte de material a suplementar. Então tem uma aula que eu dei ontem pão sobre uma introdução de testes.

**[02:06:46]** uma introdução de pi-test, pi-test fixtures, que é uma coisa que a gente vai começar a usar na próxima aula, na próxima semana, no geral. Então, tem aqui, na página da aula, tá tudo aqui. Todas as instruções que a gente fez, todos os suplementares, as leituras, o exercício tá aqui. Se tiver alguma dúvida pra resolver o exercício, tem os exercícios resolvidos, mas nesse caso, o exercício é seguir a aula, então, meio que não tem muito o que fazer.

**[02:07:15]** Mas é isso, responda um quiz que é muito importante para fixar as coisas na cabeça. Massa, entre lá no grupo, eu não sei se todo mundo entrou no grupo, vou puxar orelhinha de novo para a gente ver o que está acontecendo, para todo mundo poder entrar lá.

**[02:07:33]** E se tiver dúvida, se não conseguir responder alguma coisa, se alguma coisa ficou muito subjetiva. Lembrando que o nosso objetivo hoje era só configurar o ambiente. Então a gente queria saber se estava tudo funcionando, se as coisas tinham dado certo, se os comandos estão certinhos e tudo mais. Eu tentei simular alguns cenários de erro aqui, algumas coisas meio mirabolantes. Pode ser que eu não tenha conseguido simular o teu cenário. Então pergunto lá no grupo.

**[02:08:02]** É isso. Espero que tenha dado certo de vocês, que vocês tenham gostado disso. Semana que vem, na terça-feira, a gente vem em volta para uma introdução ou web. Então a gente vai entender o que é aquele get, o que é o barra, o que é JSON no retorno.

**[02:08:20]** Por que o teste chama GAT, sabe? Esse tipo de coisa. Por que o Assert deu 200? Hoje a ideia era garantir que o PaiTest estava funcionando dentro da nossa configuração. Então, a ideia era a gente tentar fazer tudo isso aqui. Ah, aí, ó. Falaram que ontem a agenda deu 404 no link da descrição. Ah, beleza. Eu vou ajustar depois. Mas quem precisar da agenda do curso, antes de eu arrumar, ela está aqui no Aulas. Espera aí, vamos lá. Aulas.

**[02:08:55]** aulas sincronas 2025, é quem quiser a agenda para não perder, aí falaram aí, esqueceram do like, bem lembrado Lisandro, isso ajuda a chegar em mais pessoas nesse material, então tá tudo aqui, se vocês precisarem...

**[02:09:12]** E eu estou sempre a disposição lá no grupo para a gente trocar essa ideia para ver o que está acontecendo. Eu espero que vocês tenham gostado dessa aula. Eu avisei lá no começo que essa aula ia ser massante, ela é meio chata, porque configurar todas as coisas é muito chato. E a gente acabou passando um pouquinho do tempo porque esse assunto demanda, entra no Windows, entra no Linux, vai, configura, tal, não sei o que. Mas eu espero que vocês tenham conseguido acompanhar, que tenha dado certo.

**[02:09:41]** Manda pra mim tudo lá no AISHO95, sobe, sobe o seu repositório. Eu quero ver, mano, eu quero ver, sabe? Ah, eu fico muito feliz, tá ligado? A motivação é quando o negócio funciona e vocês me mostram lá, ó, deu certo. Maravilhoso, então a gente se vê na terça-feira da semana que vem pra dar uma introdução ao web.

**[02:10:03]** E aí perguntas a gente deixa lá para fazer lá no grupo e a gente aguarda para a próxima aula. Beijo para vocês, a gente se vê terça-feira. Tchauzinho e beijinho.

