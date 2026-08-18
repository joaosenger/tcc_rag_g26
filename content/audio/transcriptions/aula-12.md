# Transcrição da Aula: aula-12.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:04]** Olá pessoas, boas-vindas! A mais uma aula do nosso curso de festa API, eu sou o Dono Sauru e espero que vocês se sintam em casa. E aí, hoje a gente vai conversar um pouco sobre integração contínua, mas antes de eu ir para os slides e tudo mais, eu só preciso daquele feedback para saber se vocês estão me vendo, se vocês estão me ouvindo, né? Se eu não estou falando sozinho, né?

**[00:00:23]** o que acontece com uma certa frequência. Então é isso. Boa noite para quem está aqui. Bom dia. Boa tarde para quem está vendo depois e boa noite também. Você vai vendo depois. Pode ser. Bom hoje eu vou dando uma introdução aqui mas eu conto com o feedback de vocês para vocês estão me ouvindo. Hoje a gente vai conversar um pouco sobre automações ou uma automação específica.

**[00:00:51]** que é dos testes no momento de integração contínua. Quem está aqui, vocês podem me falar, vocês já trabalharam com integração contínua? Em algum momento na vida, vocês conceitam a novidade? Como é que ele é para você? E aí, dependendo disso, a gente vai expandindo mais a explicação no que for possível. Então, para quem quiser, essa aula tem o texto, obviamente, como todas as outras.

**[00:01:22]** vocês podem acessar lá, se ficarem com vontade. Bom, então vamos lá. Sobre o que a gente vai falar hoje, não é? A gente vai conversar um pouco sobre a prática de integração contínua.

**[00:01:35]** que raios é integração contínua. A gente vai aprender a usar o GitHub Actions para criar workflows de integração contínua e a gente vai configurar, juntar o nosso projeto, as nossas coisas, o nosso pipeline dentro dessa integração toda para a gente ver o que acontece. Mas, então, vamos lá. O que é essa tal de integração contínua? Integração...

**[00:02:02]** Eu vou me guiar sem os slides aqui porque acho que fica mais simples, vocês vão entendendo o que eu quero dizer. Integração, basicamente...

**[00:02:11]** É toda vez que a gente junta um bloco novo de código dentro do nosso repositório, dentro do nosso projeto. A gente tem um projeto que ele está rodando, ele está fechado e a gente vai fazendo o quê? Conformamente vai cometendo no Git, a gente vai evoluindo o código. E toda vez que um código novo chega, um código novo é removido, a gente está conversando sobre a integração ou como os novos commits vão ser.

**[00:02:39]** juntados, né? Como é que eles vão ficar quando eles estiverem todos os novos que a gente tá mandando pro repositório, né? Essa é uma coisa interessante de pensar, porque às vezes eu tô trabalhando numa coisa, né? Geralmente quando a gente tá trabalhando num time, isso costuma ser um pouco mais problemático, né? Eu tô trabalhando, sei lá, na... no Halter de Chudu.

**[00:03:03]** E aí o Ruzin está trabalhando no router de autenticação. E o Caio está trabalhando no router de user. E a gente está trabalhando junto, ao mesmo tempo, fazendo três coisas diferentes, em três lugares diferentes do código. Eu sei que o Caio está rodando, ele está escrevendo os testes dele e tudo mais, e tem funcionado bem.

**[00:03:24]** Só que o Hussain está fazendo uma outra coisa, em algum momento o trabalho deles entra, vou chamar numa discordância de código, saca? E aí eu preciso, em algum momento...

**[00:03:38]** possivelmente dentro do repositório, no Git, né? E aí pode ser na plataforma, né? No GitHub, na Codeberg, no GitLab ou qualquer outra plataforma desse jeito. E a gente precisa garantir que tudo funcione quando a gente integra todos os códigos. Desde o mais simples que sou eu fazendo um push aqui, trabalhando num projeto sozinho, desde quando a gente tá trabalhando num time grande, sei lá, que tem 5, 10, 15, 20 pessoas, um projeto Open Search que recebe, sei lá.

**[00:04:07]** centenas de contribuições, então a gente precisa garantir que essas coisas estejam funcionando da forma como a gente precisa que elas funcionem, ou seja, todo código que o Ruzni fez, todo código que eu fiz e todo código que o Caio fez quando eles estiverem juntos.

**[00:04:24]** as coisas têm que funcionar, né? E aí o contínuo, né? Do integração contínua vem desse sentido, né? De a gente está integrando novos códigos, novos assets, novas coisas no repositório, de forma contínua, certo? Então, todo dia eu desenvolvo um pouquinho, dou um pâche, o Rusin desenvolve um pouquinho, dou um pâche, o Caio desenvolve um pouquinho, o Paito Anil do desenvolve um pouquinho e depois a gente tem que sempre integrar isso tudo de forma contínua.

**[00:04:53]** dentro do repositorio. Faz sentido isso que eu estou tentando explicar para vocês? Essa coisinha toda, esse passo que a gente está conversando aqui, o feedback de vocês é bem importante para mim aqui nesse momento.

**[00:05:07]** E aí, depois que eu dei essa explicada, a gente pode olhar aqui as coisas que eu coloquei no slide. A integração continua, a prática é desenvolvimento que envolve a integração regular, ou seja, com uma certa frequência, do código fonte ao repositório principal, acompanhada de testes automatizados para garantir a qualidade. E aqui, quando eu falo de qualidade, eu estou falando de qualidade de código, qualidade dos testes, sabe? Que tudo está funcionando da maneira como deveria funcionar.

**[00:05:35]** Então vamos supor que toda vez que eu faço um push ou recebo uma contribuição externa, que aqui no GitHub, que é o que a gente está usando, se chama pull request, mas no GitLab, por exemplo, se chama merge request, que é uma solicitação, um request, uma solicitação de juntar. Eu acho que o do GitLab faz mais sentido o nome. E aí o que acontece?

**[00:05:59]** A gente vai ter que configurar esse mesmo ambiente que a gente tem na nossa máquina em algum outro lugar terceiro, então sei lá. Ah, vai rodar no Linux, por exemplo, que é um ambiente de produção. Vamos pensar, a maioria dos ambientes de produção é Linux. Então, eu preciso criar um ambiente Linux lá, deixar ele falar, olha, está nessa versão tal do sistema operacional tal, da distribuição tal. E o que a gente precisa nesse ambiente? Ah, precisa ter o Pou entre instalado, as dependências do Pou, ele precisa estar aqui.

**[00:06:26]** Nosso código fonte precisa estar aqui e a partir do momento em que a gente...

**[00:06:30]** Configure esse ambiente, a gente roda os testes e a gente vai ver se aquilo passa, se aquilo não passa. E aí se funcionar, ele integra normalmente, não envia nenhuma notificação, só que caso isso fale, todas as pessoas que estão envolvidas no projeto podem receber um e-mail, sei lá, às vezes tem um bot no Telegram, às vezes tem um bot no Slack, no Microsoft Teams ou qualquer coisa desse gênero, pra gente saber que a gente tem problemas de integração nesse determinado momento.

**[00:06:58]** Como a gente está trabalhando com Python, que é uma linguagem dinâmica, né, interpretada, num sentido mais amplo, não quero me aprofundar nisso, mas os testes são muito importantes, mas o linter também é muito importante, a gente tem que fazer a parte da checagem estática, eu coloquei o teste aqui como uma coisa específica, né, mas a gente pode checar a segurança, pode rodar os testes, a gente pode...

**[00:07:21]** ver a qualidade do código, complexidade ciclomática, várias coisas que podem acontecer. E aí o que triga, isso aqui, que a gente chama de hook, que é um gancho para que esse ambiente seja criado e as coisas sejam executadas, é um push, um pull request, um merge ou qualquer ação que a gente consiga fazer no git aqui dentro. Então, basicamente, a ideia da integração continua é essa.

**[00:07:48]** entre diversas plataformas que existem. Se a gente tem...

**[00:07:54]** ferramentas de integração contínua, muito famosas, como Jenkins, por exemplo, que é uma ferramenta para pensar-se sensacional, a gente tem no próprio GitLab, a gente tem um CI para as coisas do FortGate, que é um outro sistema de Git, a gente tem o WoodKeeper CI, a gente tem várias ferramentas para fazer isso. Bom, como a gente está usando o GitHub, o GitHub tem uma ferramenta própria para fazer essa coisa, construção do ambiente e tudo mais, que é o GitHub Actions, ou...

**[00:08:24]** como ele é mais mencionado GH Actions, né? Então a ideia é que a gente tenha isso lá no servidor do GitHub, a gente vai configurar um arquivo aqui para que ele seja executado todas as vezes que a gente fizer um push, fizer um merge, fizer um pull request ou o que a gente quiser, né? Então a ideia é essa. Existe serviço já dentro do GitHub, ele é gratuito, a gente vai usar ele aqui nesse momento, mas...

**[00:08:49]** Essas coisas valeriam para qualquer outro, para qualquer outro esquema de CI e tal. Não o mesmo arquivo, não a mesma configuração, nossa configuração vai ser específica para o GitHub Actions, mas o conceito do que a integração continua faz é o mesmo para basicamente qualquer plataforma. Massa? Então, vamos lá.

**[00:09:11]** O que a gente precisa fazer, né? Aí o GitHub Action chama isso de Workflows, né? Geralmente isso aqui é conhecido como Pipeline, né? É um esquema de passos que vão acontecer um na sequência do outro e tudo mais. O GitHub chama isso de Workflow, então a gente vai usar o GitHub, então vamos lá no termo do GitHub. Vamos pensar o seguinte, eu quero pensar em como a gente vai fazer isso aqui, né?

**[00:09:33]** Vamos pensar que o nosso hook principal vai ser um push, ou seja, a gente vem, sobe para o repositório. Então toda vez que a gente subir para o repositório, a gente quer que esse hook de push seja iniciado. Aí, o GitHub Actions, ele tem vários sistemas operacionais aqui. Tem Mac, tem Linux, tem Windows. A gente vai usar o Ubuntu por padrão, porque é o Linux padrão do GitHub Actions, mas poderia ser outra coisa se você precisasse disso.

**[00:10:02]** E aí, o que a gente precisa aqui, né? Lembra que o nosso projeto tem algumas variáveis de ambiente, então a gente vai ter que configurar essas variáveis de ambiente e depois que ele subir essa máquina, tiver com as variáveis de ambiente lá dentro, a gente pode fazer os nossos passos, né? Que em inglês eles chamam de steps. Então a gente vai instalar a versão 3.3 do Python, que é que a gente está usando no projeto. A gente vai copiar os arquivos do repositório para dentro dessa máquina, dentro desse container, dentro desse ambiente que está rolando aqui.

**[00:10:31]** A gente vai instalar o poetre, instalar as dependências do projeto, as dependências de teste, e depois a gente executa os próprios testes. A gente pode executar o lindra, a gente pode fazer qualquer coisa nesse sentido. É, o Lucas falou uma coisa legal aqui. Galera, deixa um like aí, é legal, os conteúdos cheguem mais pessoas, né? E é importante que isso aconteça, né? Então, vamos lá. Como é que a gente vai construir esse workflow? Ele é um arquivo yaml, né? Bem parecido com o docker compose, que a gente...

**[00:11:02]** criou na na na aula passada e basicamente a gente divide uma coisa em jobs né então aqui a gente tem o nome o nome do nosso workflow que eu vou chamar de pipeline poderia ser testes ou qualquer outra coisa do gênero e aí aqui a gente tem o nome a gente tem um on o on é uma cláusula que diz em que momento né o quais são os hooks que a gente gostaria que fossem sabe que acontecessem no momento

**[00:11:33]** É a coisa que define se o CI vai rodar ou não, ou seja, quando toda vez que eu der um push, ele vai rodar isso aqui. Ou toda vez que eu receber um pull request, ele vai executar isso aqui. Aí depois a gente começa com jobs, né? Que são os trabalhos, as coisas que vão acontecer toda vez que um push ou que um pull request for feito aqui. Então a gente vai precisar...

**[00:11:53]** O único job que a gente tem aqui é o de testes, poderiam ter any jobs aqui, mas pra gente só isso aqui é o suficiente, aí você quiser se aprofundar mais depois, dar uma pesquisada, dar uma olhada. E aí aqui dentro tem outra cláusula que é o runs on. E aí runs a de rodar, né? Execute onde? Executa onde, tá ligado? Então a gente vai usar o Ubuntu, que é uma distribuição Linux, no latest, que é a última versão do Ubuntu, que é suportada pelo...

**[00:12:23]** Então, basicamente, esse é o começo da nossa configuração aqui. Onde é que a gente coloca isso aqui dentro do nosso projeto? Então, eu vou lá para a nossa pastinha do projeto aqui. É interessante que exista uma pastinha oculta dentro do nosso projeto. Está vendo que tem várias aqui, né? Mas a gente vai criar uma que se chama...

**[00:12:44]** ponto, porque é o culto GitHub, né? Aí você pode dar um mkdir aí contigo, mkdir, a gente vai criar uma passinha chamada ponto GitHub. Todas as coisinhas do GitHub costumam ficar dentro dessa pastinha chamada GitHub. Então tem várias outras coisas que dá pra fazer aqui, não só o action, né?

**[00:13:04]** E aí dentro dessa pasta, toda vez que a gente quer definir umas coisas de workflow de integração contínua ou CI, como a gente costuma chamar, Continuous Integration, CI, a gente pode colocar isso dentro de uma outra pasta, então tem que ter a passinha do GitHub. Dentro dessa passinha do GitHub, a gente cria uma passinha chamada Workflows, né? Então, mkdir aqui dentro GitHub, Workflows no plural, né? Tem que ser no plural se não vai funcionar, hein?

**[00:13:34]** Legal, rodou? Aqui temos a nossa pastinha Workflows. Aqui dentro do Workflows, a gente cria um arquivo e a gente dá um nome que a gente quiser para esse arquivo de Workflow. Pode ser o nome que você quiser, mas a extensão dele é YML. Então vou criar aqui. Contra o C contra o N. Eu não sei o nome que eu vou dar para isso aqui. Posso chamar de Pipeline? Posso chamar de Workflow? Qual que é nome? Eu vou chamar de Pipeline, vai? Pipeline.

**[00:14:02]** Yml, de Amel. Yes, está aqui nosso arquivo. E aí, beleza. Vamos usar as diretivas que a gente aprendeu. Então o name, então o nome vai ser pipeline. O pipeline do projeto. Aí ele é trigado quando, em algum momento, deixa eu, eu posso até aumentar a fonte aqui. Então eu quero que ele seja iniciado no push e no pull request. Ou seja, todas as vezes que a gente for...

**[00:14:29]** ou subir o código, ou alguém solicitar que alguma coisa se junte ao nosso código, se integre, uma de fora para dentro. Legal, aí a gente vai criar nossos jobs, só vai ter um nesse caso, e aí o nosso job vai chamar teste. Só para ver se eu coloquei o mesmo nome aqui, teste.

**[00:14:46]** Legal, aí lembra que tem essa identação aqui, e a identação no YAML é importante se não as coisas param de funcionar. Então são dois espaços para cada uma dessas coisinhas. Então, um, dois, o job de teste vai ser executado, então runs on, então ele roda onde? No Ubuntu Latest, que é a última versão do Ubuntu. Legal, fez sentido aqui. O que que está acontecendo? Dentro desse esquema, a gente tem um job, esse job começou...

**[00:15:17]** e ele vai ser trigado toda vez que a gente der um push. Massa, aqui dentro eu vou fazer uma coisa que não é uma boa prática, já estou avisando antes, mas que a gente vai fazer por modo de aprendizado mesmo assim, sabe? Então eu quero que vocês olhem, vejam o que está acontecendo, o que está rodando, sabe? Todas as coisas. Então, se o que triga o nosso pipeline aqui

**[00:15:42]** é sempre um push, um pull request, eu vou fazer um push só com isso aqui que a gente tem, massa. Então eu vou dar um git aqui, vou subir isso aqui, então cd2spot, cd2spot, eu vou dar um git add aqui, git add, git hub, workflows, pipeline. Aí eu vou dar um commit aqui, que eu vou chamar, eu vou falar o seguinte, olha, iniciando o, sei lá, o job...

**[00:16:08]** de testes no CI. Basicamente, eu estou dizendo aqui, se eu quiser falar que isso é uma coisa em produção, sabe, em desenvolvimento, eu costumo usar a tag Weepiance. É uma prática minha. Weep significa Work in Progress, né? Trabalho em progresso, só pra gente saber o que está rolando. Então, desde Comet, eu vou dar um push. Git push, no caso. E a gente vai olhar o que acontece lá no repositório quando a gente está rodando. Deixa eu entrar aqui na minha continha do Git.

**[00:16:39]** Deixa eu olhar aqui nos meus repositórios, está aqui o FastZero, FastIBA0. E eu quero mostrar umas coisas aqui para vocês, aqui ó, não aconteceu nada. Ele subiu isso aqui, iniciando, Job de testes no CI. Se você vier aqui, tem uma guia chamada Actions, está vendo aqui em cima?

**[00:16:58]** Então tem Code Issues por Request Actions. Se vocês quiserem, se vocês tiverem logado no GitHub, vocês conseguem ver as minhas actions. Então eu vou mandando o link aí conforme as coisas forem acontecendo. Aí você está vendo o que ele falou aqui, olha, um workflow RAM. Aí aqui está o nome do nosso comit e aí ele fala aqui qual é o arquivo que ele executou e quem foi que deu o push. E isso aqui é a Brand Main. Aí ele falou que isso aqui rodou agora.

**[00:17:25]** a manhã vai estar yesterday, claro, e que falhou. Aí que se a gente clicar aqui, a gente consegue ver o que aconteceu dentro desse job. Aí ele falou o seguinte, olha, anotações do que aconteceu. Invalide workflow file, ele falou que o nosso arquivo está inválido, porque no step defined in steps, ou seja, a gente não definiu nenhum passo.

**[00:17:50]** Mas o que eu queria mostrar para vocês aqui é esse esquema do trigger, do hook, do gancho, a coisa que acontece. Então você viu que a gente deu um push, ele leu esse arquivo de forma automática com o push e está falando para a gente o que aconteceu. Ele tentou rodar, não conseguiu, deu falha, porque não tem nenhum step configurado. Porém, com tudo entretanto, todavia, ele está funcionando. Massa fez sentido tudo que a gente colocou aqui até agora?

**[00:18:20]** Então, ele está reclamando que a gente não tem nenhum step, né? Então, vou voltar aqui para os slides para a gente olhar. Então, do mesmo nível de dentação do runs on, né? Ou seja, dentro do job de testes, a gente vai definir alguns steps aqui. Então, um, dois, um, dois, são quatro, né? Dentro do job, dentro de testes. Então, a gente vai definir os steps. Ou seja, quais passos vão acontecer dentro do noci. Então, deu enter.

**[00:18:48]** mais dois espaços, de novo. Aí, aqui a gente tem algumas diretivas, a gente tem o name, então eu vou colocar aqui, ó, ó, ó, como isso é interessante, tem que ter traço no começo, porque a gente tá, isso aqui é uma lista de passos, né? Então, a gente vai colocar um name. Aí o name aqui, eu vou dar o primeiro passo, que é, por exemplo, instalar o Python, né? Que é, instalar o Python.

**[00:19:16]** E aí você pode falar o seguinte, olha, eu quero rodar o Python aqui, e como é que eu instalo o Python? Então existem várias formas de fazer isso. Você poderia, por exemplo, usar o Poetry, daquela forma que a gente fez normalmente, né? Pessoal lá, run, poetry, install, mas aí eu teria que instalar o Poetry, mas se eu instalar o Poetry eu tenho que ter o pipi, sabe? Então vai rolar um monte de atritos aqui. O GitHub Actions por definição.

**[00:19:44]** ele tem algumas ações prontas e aí por isso que vem o nome de action então existem algumas ações prontas uma delas é esse aqui actions que é o setup python deixa eu voltar lá no aí isso aqui é uma ação padrão né se você quiser ver as ações oficiais do github elas estão todas aqui né então tem um monte de ações que você pode usar

**[00:20:13]** Start Workflow, Setup Node, TypeScript, JavaScript Action, Toolkit e tudo mais. E existe uma lojinha do GitHub Actions. Eu acho que chama Marketplace. Se eu não me engano, é esse o nome. Aqui é Marketplace. E aqui a gente tem Actions. Então você pode vir aqui, clicar em All Actions. Eu vou mandar aqui para vocês.

**[00:20:39]** E aí tem coisas que são de outras pessoas, então você pode criar sua própria action, customizado e tudo mais e usar aqui, é simplesmente um bloco de código que alguém deixou pronto.

**[00:20:49]** Aí tem vários criadores, aí tem criadores verificados, tem um monte de gente aqui, você pode olhar pela popularidade, o que que foi aqui e tal, aí é contigo, depois você vai explorando isso aqui, é tipo uma biblioteca Python, tem 50 mil, você vai brincando e vai vendo o que que acontece aqui. Uma dessas que tem prontas, que é do próprio GitHub, é aquela que a gente viu aqui, que é o Setup Python, que é a que a gente vai usar aqui, pra começar.

**[00:21:20]** E aí, toda vez que a gente quer usar uma action pronta, a gente simplesmente coloca uses aqui. Essa é a diretiva, uses. E aí, tem que ficar no mesmo nível aqui, ó. Tá vendo? Isso aqui é importante. Tá vendo que ele não tem o traço e ele fica no mesmo nível do Name aqui. Então, a gente vai usar uma coisa que é do Criador Actions, né? Ou seja, que são as Actions oficiais. O bloco pré-pronto que a gente vai usar esse aqui, chama Setup Python. E esse arroba aqui é Ethna.

**[00:21:52]** que é quando a gente fala em inglês, né? V5, ou seja, tá na versão 5. Aí dentro dessa coisa aqui existem alguns parâmetros que a gente pode passar e um deles é esse WIF aqui embaixo e aí a gente passa qual é a versão do Python que a gente tá usando. No caso, a gente tá usando a 313, então a gente vai chamar a versão 313 aqui. Então, WIF Python version 313. A partir daqui, todos os steps, ou seja, todos os passos que acontecerem

**[00:22:26]** seguintes a esse já contam com o Python instalado dentro da máquina massa fez sentido aqui cada da coisinha que a gente foi colocando aqui se tiverem dúvidas por favor agora é hora sim vamos trocando ideia

**[00:22:41]** Vamos falando comigo. E aí, de novo, vou executar uma coisa que não é uma boa prática. De novo, estou fazendo vários commits para ficar testando o CI. Mas tudo bem, a gente está aprendendo e quer ver o que está acontecendo aqui. Então, eu vou dar o meu commit aqui, iniciando o job de testes no CI, aí eu vou colocar aqui um outro whip, um trabalho em progresso, instalando o Python no CI. Só para a gente...

**[00:23:07]** Vê o que que rola aqui, então vou dar um gitpush de novo, que é um dos triggers que a gente usa aqui. Subiu, vamos voltar lá no meu repositório. Aí a gente clica aqui no FastAPI0 ou no seu repositório que eu estou usando e você vem aqui em actions. Aí ele vai provavelmente ter aqui. Aí você está vendo que essa está vermelhinha porque falhou, essa aqui está amarelinha porque ela ainda está sendo executada. Tanto que a gente vê aqui em progress.

**[00:23:36]** Se a gente clicar nela, a gente consegue ver qual é o pipeline que está rodando aqui, o pipeline. Se tivessem outros jobs, a gente veria vários jobs aqui, mas como só tem o teste. E é que tem cada passo que ele fez, né? Ele iniciou o job, ele instalou o Python, que foi essa coisa que a gente fez, aí ele rodou, né? O ActionStall você consegue vendo aqui, qualquer versão, lentes, total, total. Qual que foi a versão instalada, ele falou. Estalei o C Python na versão 3.13.5, que a gente não deu a minor, né? O último...

**[00:24:05]** O último, a gente não deu o fix, né? Que é o último numerozinho. Aí depois ele faz o post, né? E depois ele completa o job. São passos esses aqui, ó. Setup. E os posts completos são coisas que ele roda depois, assim, por padrão. Se a gente olhar, esse aqui ficou azuzinho, né? Significa que ele passou. Funcionou. Não fez nada ainda, né? Mas ele passou. Isso que é importante aqui. Uma coisa que aconteceu aqui, quando a gente tava nessa brincadeira...

**[00:24:38]** Eu não sei se vocês vão conseguir ver, mas eu vou tentar mostrar pra vocês. Por aquele job anterior ter falhado, eu recebi um e-mail, tá ligado? Aqui. Aí eu recebi um e-mail dizendo, olha, do Nossauro Flash API Run Failure, tá ligado? Então ele falhou. Não conseguiu e ele manda um e-mail pra mim falando, olha, dá uma olhada aí no que aconteceu.

**[00:25:04]** Então ele me notifica, toda vez que o job falha. Isso é muito importante dentro dessa parte aqui da gente ver o que está acontecendo. Ele não vai me notificar quando funciona. Obviamente deu tudo certo, não tem porque me notificar. Legal? Então é basicamente assim que funciona. Então essa é toda a estrutura de um workflow.

**[00:25:24]** O GitHub, a gente dá um nome, fala quando vai rodar, define alguns jobs, qual o nome do job, aonde ele vai rodar e quais são os passos. Agora a gente vai... Agora que a gente entendeu toda a estrutura, a gente vai criar o nosso pipeline, o nosso fluxo. Começou na instalação do Python. Aí eu já dei um push aqui e tudo mais, mas a gente foi fazendo junto, então tá tudo bem. Então o que a gente precisa? A gente precisa instalar o Python.

**[00:25:51]** Depois do Python, a gente precisa instalar o Poetry. Depois de instalar o Poetry, a gente precisa instalar o Poetry install. Depois disso, a gente precisa executar os testes para ver o que vai acontecer, ver se vai dar tudo certo e tudo mais. Legal? Então, vamos começar aqui, a gente fez isso aqui. E toda vez que a gente usa o setup Python, essa action aqui, ele instala o ppx para a gente no...

**[00:26:17]** essa action instala o ppx então a gente já tem o ppx faz igual a gente fez lá na aula de configuração no ppx install poetry basicamente precisa estar no mesmo nível que a gente tinha aqui em cima né então é um outro tracinho da lista aqui peraí e aí ele tem o nome

**[00:26:41]** E aqui muda a diretiva, né? Você tá vendo que ele tá usando rum e não uses, né? Toda vez que a gente usa uma ação que tá no marketplace, pronto, a gente fala, quer usar uma action que já tá pronta. E toda vez que a gente vai rodar um comando de terminal, bem parecido com o que a gente fez no Docker, a gente usa o rum, a palavra reservada rum aqui. Aí, ppx install poetry é o mesmo comando que a gente rodaria na nossa máquina, tipo assim, ah, roda aí pra instalar o poetry. Massa, legal.

**[00:27:10]** Rodou aqui de novo, a gente pode ir fazendo isso de forma interativa aqui, não tem problema. Então git e tal, aí a gente vai falar, tipo assim, instalação do ponte no ci. Estou fazendo isso aqui só de brincadeira, vocês sabem que vai rodando, vocês já entenderam o que que acontece aqui, né?

**[00:27:34]** Vocês já sacaram, acho que eu não preciso refazer isso aqui mais uma vez. Então, tá rodando aqui, enquanto roda o Job, eu vou agradecer o Muringa aqui, que me mandou um... um... um Super Chat. Valeu, mano. Ó, beijão para você, ó. Os Super Chats me ajudam demais, mano. Demais. Então legal, ó. Instalou o poll entre...

**[00:27:58]** Legal, aí ele fala que dá o resultado do PPX. Qual foi a operação do Shell? Ele falou, Creating Virtual Environment, que é o que o PPX faz, instalando o Poetry, Done. O Poetry está instalado na versão 2.1.3, usando o Python 3.12.3. Está tudo bem, porque o nosso projeto usa outra versão. Aí, tipo, pinou no PyProject.oml.

**[00:28:23]** mas está funcionando aqui. Então, legal, o que a gente faz quando a gente pega isso aqui? A gente já tem o Poetry instalado, o próximo passo é instalar as bibliotecas do sistema. Então, instalar as bibliotecas que a gente depende aqui, né? Então, instalar as dependências, a gente vai fazer um Poetry install, ele vai instalar tudo. Lembra que no Docker a gente tinha feito aquele menos-menos-with-out deve, por exemplo? Aqui eu não vou fazer isso, né? Por que que eu não vou fazer isso aqui? Claramente porque...

**[00:28:55]** A gente precisa das dependências de desenvolvimento, porque a gente vai rodar isso aqui, né? Então, instala as dependências, e depois de instalar as dependências, a gente vai rodar o nosso task test aqui. Então, executa os testes. Simplão assim, poetry run task test. Ah, eu poderia subir o ambiente virtual, poetry shell, pra depois mandar, poderia também, ativa o ambiente virtual. Roda a coisa que precisa. Mas basicamente aqui, a gente fecha o que precisava fazer, né? Basicamente...

**[00:29:30]** Tudo pronto, né? Foi até rápido, né? É, está vendo que todos os comandos rodam com o Bram, porque a gente está executando instruções no Shell. Então, vamos lá. Adicionou executando testes no CI. Gitpush. Agora vai acontecer uma coisa interessante. Eu dei esse push de propósito, porque vai dar um erro aqui, né? E é importante que a gente veja esse erro, rolando.

**[00:30:07]** instalou o Poetry, aí você vai ver que instalar as dependências vai demorar um pouco, mas dessa vez não deu. Ele falou o seguinte, o Poetry could not find PyProject.L, ou seja, está rodando lá no Home, o Worker, tal, tal, tal, fecha IPI0, fecha IPI0 que é o nome do nosso projeto, aí ele está falando o seguinte, não tem PyProject aqui.

**[00:30:29]** Por que que não tem o Byproject? Como é que meu projeto não tem o Byproject? É claro que tem, ele está aqui, né? Esse é um erro que acontece, é bem comum, foi por isso que eu quis destacar ele aqui, né? Como é que não tem Byproject? Byproject está aqui Qual é a pira dele? Então, a pira dele é que, nesses passos, a gente tem que copiar os nossos arquivos para cá Porque lembra que o Pipeline pode fazer qualquer coisa?

**[00:30:58]** Então, pode ser que às vezes a gente queira que ele faça uma coisa que não tenha interação direta com o nosso próprio código. A gente só executa uma ação quando deu push, mas... Então, eu vou copiar aqui os arquivos do repositório pra cá. Aí, eu vou colocar isso aqui como o primeiro passo, é uma coisa que eu faço, não precisa ser o primeiro, né? Tem que ser antes de dar um install só.

**[00:31:24]** E aí olha que interessante, a gente vai usar o Uses de novo, a gente vai usar o Actions e a gente vai usar uma ação chamada de Checkout, que é basicamente quando você copia as coisas do Git a gente fala que faz Checkout, né? Essa também é uma Action pronta aqui dentro, que também é do próprio GitHub, por isso que ela se chama Actions. Precisa Git clone exatamente aqui. Então aí a gente vai usar essa Action aqui. Ela está na versão 4, pode ser que ela tenha sido atualizada, não, ainda está na v4.

**[00:31:56]** Então, basicamente, o que a gente precisa fazer é falar, usa isso aqui. Eu não preciso passar mais nada, não preciso falar qual é o meu repositório e tudo mais. A não ser que eu queira clonar de outro repositório, trazer o código de outro répov para cá, aí eu preciso configurar. Como é o nosso próprio CDAL Checkout, ele já entende que a gente está usando o nosso próprio repositório como base. Então, legal? Checkout. Então, vamos lá. Git, edge, pipeline, whip.

**[00:32:25]** adicionando check out ao CI. Git, push. Vamos ver agora o que vai com C dentro dessa brincadeira aqui. Ou, eu só queria dar no action, dizer que não era pra voltar tudo. Agora a gente vai ver o CI rodando mesmo, passo por passo e todas as coisas como a gente roda na nossa máquina, né? Quando a gente dá o, aí ó, instalando as dependências, aí ele vai executar os testes.

**[00:32:58]** Legal, deu erro. De novo. Mas você viu que agora a gente tem mais info aqui, né? Ó, ele conseguiu instalar as dependências por conta do check-out, né? Então ele instalou tudo o que a gente queria, que é o REACH, DOT ENV, o PIDENTIK, plug-in do Faker, Docker. Tá tudo aqui instalado. Só que ele não conseguiu rodar. Aí vamos entender o que que acontece.

**[00:33:22]** Quando ele tenta executar a task de teste aqui, o PoetryBram TaskTest, ele está dando todos os configs aqui de onde está o Python, então você precisa debugar isso aqui, é importante. Aí ele falou, todos os testes passaram. Esse AllCheckPasseds aqui não é do teste, lembra que sempre roda o lindirante, não? Aí quando ele começou a fazer, ele foi lá e rodava aqui, lá no arquivo ConfTest, a gente chama o CreateAssyncEngine.

**[00:34:00]** Tá vendo aqui, lá no database. Então a gente vai começar com o teste chama, faz os imports, faz as coisinhas que a gente queria. E aí, lá dentro do código, no database.py, ele chama os settings. E para rodar os settings, precisa ter os settings, né? Mas a gente não tem nenhum desses arquivos de configuração configurado aqui, né? Por que isso aqui não tá aqui? Porque lembra que a gente não usa o .env, né? O .env ele tá oculto, né? Dentro do gitignore aqui, né?

**[00:34:34]** Ele está aqui, ele não sobe nunca para o repositório. E é isso, ele não sobe para o repositório, ah, tem que a gente vai fazer, a gente precisa dar um jeito de colocar essas coisas lá no RAP. Então, é para cá que a gente vai agora. Uma forma de fazer isso aqui é usando o GH, né? Para todo mundo, todo mundo que está fazendo curso, está online aqui comigo, está usando o GH. Eu falei lá no começo, ele é opcional, mas tipo assim, ele facilita horrores.

**[00:35:05]** Essa é uma das coisas que ele facilita aqui, não? Enquanto vocês me respondem, vocês estão usando o GH ou não? Eu vou mostrar as duas formas, mas... Eu vou agradecer o Lucas aqui, Lucas, obrigado. Por suco ou café, porque o Monster demais faz mal. Mano, valeu. O Rodrigo, que eu não estou usando o Zen, estou assim. Massa? Então, eu vou rodar essa paradinha aqui. Então, GH Secrets 7, ou seja, GH Machinals Segredos do meu Repositório.

**[00:35:36]** Aí a gente vai dar um set, ou seja, vai configurar as variáveis de ambiente, e aí a gente vai mandar um "-f", que é o file, e aí a gente vai passar o arquivo .env pra lá. Beleza, eu vou fazer aqui, na mão, eu vou fazer aqui com vocês, o gh, secret7-f.env, então ele vai conectar lá no meu repositório, e ele já pegou aqui, adicionando...

**[00:36:05]** Access Token Expired Minutes, Algorithm, ou seja, o Algoritmo, Database e todas as variáveis que tinham no nosso ponto INV. Database, Secret Key, Algorithmo e Access Token, ele vai subir isso aqui como segredos do repositório. Mas aí a gente só faz esse comandinho aqui e ele resolve o problema. Só que você fala, eu não estou usando o GH, então vamos lá.

**[00:36:37]** Tem um caso contrário aqui, eu deixei, isso tá no texto, né? O link tá errado aqui, só arrumar depois. Que é esse definindo segredos aqui. Gosto quando vai o link. Basicamente, dentro do repositório, já que ele não abre aqui, eu vou mandar o link assim que ele abrir ele. A gente vai ter que vir aqui no repositório, e aqui tem uma coisinha chamada settings aqui em cima, né? Aí você vem em settings. Dentro do repositório...

**[00:37:15]** Aqui embaixo, aqui ó, você tem, veio nos settings. Aí aqui no menu esquerdo, lateral, você tem o security, que é o penúltimo tópico. Aí aqui no penúltimo tópico você tem o secrets and variables, né? Segredos e variáveis. Aí você vem aqui no actions, clicou no actions, aí ele mostra que as variáveis que a gente definiu. Aí você pode falar, ah, beleza! Como é que eu faço aqui? Então você pode vir aqui e criar aqui um.

**[00:37:52]** Unir Reposter Secret. Você cria um segredo novo. Aí você vai lá e vai lá no seu Env e fala, ó, o nome do segredo é DataBase ou RL. O segredo é esse aqui, né? Pô, segredo total, total, total, total, total. Aí você vem aqui e coloca o segredo. Peraí que ele deu uma quebrada, né, por causa da minha formatação do Shell. Passou aqui, aí você deu um AddSecret.

**[00:38:16]** Ele deu erro no meu, porque já existe esse segredo aqui, mas aí você vai colocando um por vez aqui. Aí você fala, ó, eu queria editar esse aqui, aí você edita. Você vê que ele nunca mostra o valor dos segredos aqui. Então tá tudo aqui, então você pode fazer essa é a forma de fazer manualmente. A cadeia aqui, ó, definindo secrets no repositório. Aí aqui tem os passinhos certinhos, caso você precise fazer isso na mão.

**[00:38:47]** Aqui ó, acesse os settings do repositório, aí você vai em actions, cria um novo segredo, aí você coloca o nome, o valor do segredo, e depois você acaba com tudo pronto aqui, aí você vai fazendo manualmente, se você quiser. Eu prefiro usar o GH, porque o GH me poupa muito tempo, não? Muito tempo, muito tempo. Ahm... Aí falou, gerar um ponto em com secrets do GitHub, Eduardo?

**[00:39:18]** Eu não varia isso, tipo assim. O lugar de segredo é na tua máquina, no servidor, é no saber. Tipo assim, eu não criaria um arquivo que fosse visível para as pessoas verem o segredo. Não acho que é legal. Massa? Então, a gente está aqui. Eu não estou respondendo perguntas fora do assunto, menino. A gente está respondendo perguntas da aula.

**[00:39:44]** Só perguntas na aula, que tem a ver com o escopo do que a gente tá vendo. E aí, como é que a gente seta os segredos aqui, né? Então, vamos lá. Eu vou copiar um, depois a gente copia tudo e vamos explicando aqui junto. Vou voltar lá no nosso arquivo de pipeline aqui. Aí você pode colocar isso no começo, você pode colocar no fim, onde você quiser, ele vai entender que é envy. Isso aqui fica no mesmo nível do steps, tá vendo? Steps, envy. Aí você coloca qual que é o RL que você quer usar.

**[00:40:14]** E aí tem essa sintaxe aqui de variável de template aqui, não? Então aí você tem cifrão, abre chaves, abre chaves, aí você bota o que você quer, fecha chaves, fecha chaves. E aí tudo que é um segredo no nosso repositório está aqui como secrets. Então para acessar aquela binha que a gente tinha aqui, que é a binha dos segredos aqui, actions, secrets, não?

**[00:40:39]** tem secrets, tem variables, você pode ir usar variável se quisesse. Eu coloquei secrets porque é mais fácil, tá ligado? Mas poderia ser variável se você quisesse. É porque o secret que é secret, esse aqui é variável, esse aqui é variável, esse também é variável, mas tudo bem, junta tudo, não tem problema nenhum. Aí aqui você pode pegar o nome que está na secret e ou no variables, se fosse variables seria variables aqui, não muda muita coisa não.

**[00:41:09]** Você pode pegar o valor que está lá baseado no nome, mas você pode atrelar a outra variável de ambiente que você quiser ter nesse ambiente. Poderia ser qualquer outro nome, não precisaria necessariamente, sei lá, lá se chama, sei lá. Postgres, por exemplo. E aqui você atrela com database URL. Massa? Então você não precisa fazer isso aqui. Aí a gente pode fazer isso para todos os nossos nomes. Então a gente tem o secret key, o algoritmo e...

**[00:41:46]** Vou copiar tudo pra cá pra ficar mais fácil. Vocês já entenderam o que faz e o que tem dentro de cada valor, não precisa ficar explicando tudo. Então a gente tem o secret key, o algoritmo e a chave. Então agora a gente tem todas as variáveis de ambiente que a gente quer levar pra lá. Uma outra coisa que poderia acontecer aqui, sei lá, tem variáveis que são meio irrelevantes. Se você quiser colocar ela direto aqui, você poderia falar, sei lá. Variável...

**[00:42:12]** xpto, e aí você passa o valor aqui, tipo assim, batatinha. Tá tudo bem, você poderia fazer isso aqui, se for um valor que não tem problema nenhum, tá tudo certo. Massa, legal. Configuramos as variáveis de ambiente, vamos rodar de novo agora. Então, adicionamos a pipeline, adicionando envivars ao ci. Beleza, git, push, subiu de novo. Espero que tudo rode agora, né? Vamos lá em actions de novo.

**[00:42:54]** E vamos ver se vai tudo funcionar agora. Estalou o poetry, está instalando as dependências. Agora ele vai executar os testes. Acho que vai funcionar. Espero que sim. Beleza, começou. Ele já deu o pull na imagem do teste de container, que a gente definiu na aula passada. Terminou de baixar. E é isso aí. Rodou os testes. Lindo bala. Sensacional. Passou. Nossa integração foi feita com sucesso.

**[00:43:31]** Agora toda vez que alguém mandar um pull request pro nosso projeto, ou a gente dá um push, pode ser que por algum desacaso, assim, sabe? Ah, esqueci de rodar o teste. Então você consegue rodar aqui e ver se está tudo funcionando. Isso é massa, né? É muito legal. Funciona, ó, de forma incrível isso aqui, né? Aí você pode falar, mas eu queria um outro step, né? Aqui, vamos começar a brincar aqui, então, vai? Pô, beleza, porque a gente tá rodando só os testes.

**[00:44:01]** Ah, mas eu queria rodar o linter, porque pode ser que o teste roda sempre o linter antes, né? Mas pode ser que você tenha um erro de linte e aí ele quebra no step de teste, aí você não quer que isso aconteça, né? Então aí você pode vir aqui e falar o seguinte, ah, sei lá, qual que é o nome dos tasks aqui, né? Tasks. A gente tem o linte. Então a gente poderia rodar essa coisa aqui, né? Então você poderia fazer o seguinte... Pera aí que eu dei algum... Então a gente poderia falar o seguinte... Executa...

**[00:44:37]** um linter, por exemplo. Aí você pode no task lint. O massa da gente ter feito os comandos é que fica tudo mais fácil aqui, né? Tipo, fica tudo mais simples, bonito, né? Organizado. Olha, vem aqui, adicionou. Linter OCI. Pux, subiu. Bom, vocês já sabem o que vai acontecer aqui. Beleza. Alguém pode estar com uma pergunta em mente, que é o seguinte. Toda vez que eu quero testar isso aqui...

**[00:45:11]** Isso é fora do escopo da aula, mano. Aproveitar que a gente tem um tempo aqui, a gente tá conversando. Achei que vocês iriam fazer muito mais perguntas hoje. Ó, você vai ver que ele secutou o lintero aqui, ó. Já rodou. Tudo certinho. A questão é o seguinte, toda vez que eu preciso rodar isso aqui, eu preciso esperar pra subir no ciá e pra ver se vai dar certo, pra ver se não vai dar certo, tipo assim, pô, isso aqui é meio não-prático, né? Se a gente for parar pra pensar a grosso modo, né?

**[00:45:48]** fala, pô, eu tô desenvolvendo-se aí, eu preciso desse tipo de coisa? Então, existe uma ferramenta que se chama Acti. Nectus Acti, que é essa ferramenta aqui. E aí o Acti é uma forma de rodar o GitHub Actions localmente. Aí ele roda via Docker. Aí se você tiver o Docker configurado e tal, isso aqui é outra coisa, não tem nada a ver com o escopo da aula, mas tem tudo a ver ao mesmo tempo, né? Então, vocês precisarem de uma ferramenta para fazer isso.

**[00:46:26]** Aí você pode instalar o Act, tem a forma de instalar aqui, vocês dão uma olhada e tal. E tudo o que ele precisa é que o docker esteja instalado, então assistem, CTL Start, vou startup o docker. Aí, se você instalar o Act, tudo mais, você chama o Act aqui direto, então Act. Aí ele baixa a imagem.

**[00:46:52]** do Ubuntu Latest, aqui está vendo, do Act e tudo mais, e ele vai fazer todos os mesmos passos que ele faria lá no GitHub dentro da sua máquina. Então, se altera uma coisa e quer ver se vai funcionar no CI, você não precisaria fazer um PUSH e tudo mais, ficar sujando histórico de Comet. Você pode rodar tudo localmente e aí funciona bem. Massa?

**[00:47:17]** Para quem está usando isso aqui no Windows, tem alguns casos assim que não costumam funcionar muito bem. A gente conversou sobre isso aqui localmente. Aqui ó, é possível rodar o CI localmente, está no mesmo lugar aqui. Não, pera aí. Eu quero achar o tópico onde está isso aqui. Para mandar o link. Aqui ó, está no configurando o Workflow de CI aqui. Aí quem precisar tiver um problema e tal no...

**[00:47:56]** no Windows você precisa criar uma rede, tudo mais, tem aqui explicadinho que precisa fazer. Aí se você é que nem eu, que não gosta muito de usar o Docker funciona com o Podman também. E aí você pode rodar aqui. Aí você está vendo que ele fez todo o esqueminho aqui, né, ó. Instalou todas as dependências e tudo mais e ele está fazendo isso num ambiente isolado que não é a minha própria máquina. Então eu subi um container para fazer essas configurações e tudo mais, então está tudo aqui. Funciona muito bem.

**[00:48:26]** A próxima vez agora vai ser mais rápido, porque ele já baixou as imagens, né? Já vai instalar o poetre direto aqui. E aí se vocês precisarem disso, é uma forma de rodar totalmente honesta, funciona muito bem e tal. Funciona em todas as plataformas, estiver em suporte ao Dockman ou o Dockman ou o Podman, você pode rodar isso aqui. Mas só um extra aí, aí se precisar, tá aí.

**[00:49:03]** Que mais que eu queria falar com vocês a respeito disso aqui? A gente adicionou umas steps, fez algumas outras coisas e tudo mais. Esse arquivo, você pode ir brincando com ele e colocar uma tonelada de coisas aqui, o que você quiser, se você precisar de outras coisas, tá tudo bem, tá tudo rolando, funciona muito bem. Aí você fala, eu quero rodar um outro job aqui, sei lá, uma coisa para funcionar em paralelo, sei lá, roda a documentação, você poderia criar aqui um docks.

**[00:49:35]** Runs, On, sei lá, o Ubuntu Latest. E aí você pode fazer o que você precisar aqui. E aí dentro desse mesmo arquivo você vai e ele faz as coisas paralelamente, se for preciso. Uma outra coisa que você pode fazer é, ah, eu quero ver se tem um erro no meu docker. Aí você poderia rodar aqui um run no docker, build, image, tal, tal, tal e ver se está tudo funcionando, se é imagem build, se funciona da maneira que deveria funcionar.

**[00:50:07]** Mas, basicamente, é isso aqui. Não tem nenhum segredo aqui dentro dessa coisa. Recebe o e-mail todas as vezes. Todas as vezes que falha, eu recebo o e-mail, Lucas. Toda vez que quebrar, eu recebo o e-mail. Por isso que é legal se rodar o Act antes, assim. Às vezes você quer só fazer uma validação, ver uma coisinha, ver se está tudo certo. O Act resolve muito desses problemas. Então, legal. Já dei esse comit, já dei o PUSH. A gente já viu funcionando e tudo mais. E... bom!

**[00:50:38]** Eu sei que é feriado, então tem poucos slides hoje. Aqui tem o quiz dessa aula, para quem quiser entender e tudo mais. Para quem quiser responder, bom que faça. Essa aula também não tem exercício, porque o exercício de novo é tentar fazer isso aqui funcionar aqui dentro. Então, a gente vai para outra coisa. Massa.

**[00:51:10]** Então agora eu vou ficar aqui pra gente, eu vou responder as perguntas de vocês, já vi que tem várias aqui, e a gente vai respondendo junto. Mas quem quiser feria dar aí, bom feriado, né? Pra quem tá assistindo isso depois, hoje é feriado, né? Então, tudo bem. Então eu vou responder as perguntas que fizeram aqui.

**[00:51:30]** O Victor perguntou, eu sou novo aqui, acabei de escrever, do que você trata essa aula então. Essa aula é uma aula do curso que a gente está fazendo, que é um curso de Fast API. Aí, se você quiser conhecer o curso, entra aí no Fast API do zero, ponto do no salro e tal, você vai sacar o que a gente está falando aqui. Massa, vamos dar o link aí, e aí você dá uma olhada.

**[00:51:53]** Legal, vamos ver aqui. Como funciona o deploy em dev e prod, cria um gatilho para cada banco? Então, a ideia é o seguinte. Integração contínua é uma coisa. Deploy contínuo, né? Fazer o deploy é outra coisa. Então, a gente tem o Continuous Integration, que é a relação de como tudo vai se integrar. E a gente tem o Continuous Deployment.

**[00:52:22]** que a gente não chama de ci, ci, a gente chama de cd, o cd, que é a ideia de fazer deploy em uma plataforma ou em algum lugar, então a ideia é basicamente isso, só que aí muda o trigger, por exemplo. Ah, eu preciso colocar isso aqui em modo de dev, então você tem um lugar, dependendo do que você quiser usar ou de como tiver coisa, você vai criar um script para...

**[00:52:46]** fazer o deploy ali, aí você pode usar o run e tal e escrevendo aquela coisa. Você pode escrever um arquivo Python, você pode usar Ansible, que é uma outra plataforma para fazer esse tipo de coisa. E aí você vai para alguns lugares e faz o deploy, né? Aí é contigo. Aí o André perguntou, Dú, tem como separar em mais arquivos caso fique muito grande? Tem.

**[00:53:08]** Tudo que tiver na pasta de workflows, dentro da passeia do .github, workflows, ele vai rodar e aí você define o que vai rodar em cada... em cada trigger usando o home. Então você pode criar dez arquivos se você quiser aqui dentro. Não tem...

**[00:53:30]** Não tem nenhum problema aqui, né? Então você pode criar outro arquivo, e aí você fala que isso aqui é, sei lá, batatinha, e aí vai acontecer quando for PUSH, quando for Request, quando for outras coisas. O GitHub Actions, ele também tem uma outra funcionalidade que a gente não viu aqui, porque não faz muito sentido pra gente, mas é de rodar tesques periódicas. Falar, uma vez por semana eu quero ver como tá a cobertura de testes, uma vez por semana eu quero, sei lá.

**[00:53:56]** ver se tem novidades na biblioteca. Eu quero entender se, sabe, novidades no sentido de atualização. Eu preciso ver se tem alguma vulnerabilidade de segurança que saiu nova agora. Então, você pode criar workflows periódicos também e é algumas coisas que podem acontecer nesse sentido aqui. Aí eu sajo de perguntas se vai TCD, não vai TCD. A gente vai fazer o deploy na próxima aula.

**[00:54:24]** Na próxima terça, mas a gente não vai fazer contínuos deployment. A Carla falou, essa funcionalidade do GitHub é incrível, ajuda bastante no dia a dia. Então, o GitHub tem o actions, mas se você estiver usando outra plataforma, por exemplo, como o GitLab, o GitLab tem o GitLab Cine, que é a mesma coisa, só que...

**[00:54:47]** Sabe, o CI do GitLab. Se você estiver usando o Codeberg, que é o meu preferido atualmente, ele te disponibiliza o Wood Keeper CI, que é uma outra forma de rodar. Então, quase todas as plataformas de Git tem uma forma de fazer isso. Forgain, o Codeberg, o GitLab, o GitHub e todos eles, né? Até as da TALAC, não sei como é que está hoje em dia, mas eles têm o Bambu e tal. Então, basicamente, para todas as ferramentas, tem isso aqui.

**[00:55:15]** e inclusive você fala, mas eu estou dentro do ambiente da empresa, eu queria unciar e tudo mais. Tem uma ferramenta em Python para construir fluxos de pipelines, que é o BuildBot. Então você fala, eu queria construir um dentro da minha própria empresa e tudo mais. Você pode usar isso aqui, tem o BuildBot, que é um framework em Python para fazer integração contínua. Então tem isso aqui, tem o Jenkins.

**[00:55:49]** que é o mais famoso, acho de todos, aqui, Jenkins.io, que é uma ferramenta externa para fazer isso aqui, aí você sobe na sua infra e coloca e não fica com essa coisa ninhado junto com o repositório e tudo mais. Os builds do Python, por exemplo, são feitos no buildbot. Aqui, Python buildbot. Aí, se você quiser ver aqui, você pode ver...

**[00:56:28]** Todos os builds do Python, esse está buildbot.python.org Você consegue ver aqui ó, ó, o Python arquitetura... O Python está rodando agora, 26 arquiteturas diferentes aqui ó, no Fedora, no Red Hat, no CQ, arquitetura x86...

**[00:56:48]** 6, 4 e tá aqui ó, tá tudo você pode ver ao vivo que tá acontecendo, você pode ver o status da release, como é que tá agora e tudo mais, então você consegue acessar né, do Python todinho aqui, o que que tá acontecendo, eles já estão buildando 3.15 ó, 3.13 que é o que a gente tá usando, ela tá falando o que que tá acontecendo, o que que deu erro e tudo mais você consegue acompanhar né, o do próprio Python aqui.

**[00:57:13]** E é muito legal, é muito legal. Se vocês quiserem ver um pipeline mais robustão, assim, aproveitar e mostrar isso para vocês, o que a gente usa no curso de Fast API, que a gente tem o site e tudo mais, e roda os testes e ver como é que funciona tudo, o que a gente usa para construir a página do curso, ele está aqui também, aí vocês podem brincar e dar uma olhada lá. Ele roda de uma forma muito diferente aqui, até legal a gente olhar isso aqui, né? Ou quando é que ele roda, né?

**[00:57:45]** Então o repositório do curso, do curso de FastAPI, fica por curiosidade para vocês mexerem lá depois. Ele só roda, por exemplo, ele só roda quando tem autorização no código de aulas ou no workflow. Aí ele roda no push e no pull request. Aí olha uma outra coisa que tem aqui, no job de teste tem uma coisa chamada strategy. Aí a gente cria uma matriz.

**[00:58:19]** E aí ele roda o job de teste no Python 3.11, em todos os que a gente suporta no curso, né? O 3.11, o 3.12 e o 3.13. Aí ele faz uma coisa muito parecida, né? Ele faz o check-out, atualiza o sistema, instala o SQLite, porque a gente usa isso no curso. Aí ele instala o Python usando a versão da matriz, né? O 3.11, 3.12, 3.13. Ele instala o Poetry.

**[00:58:47]** Aí ele dá a instalação do Poetry, aí ele roda o lint de todos os códigos de aula, os testes de todos os códigos de aula, todos os dockers que a gente buildou pra fazer lá. A gente tem esse typos que checa por erros no código, a gente testa as migrações e tudo mais, é um build um pouco maior do que a gente tinha. E aí ele triga em push, em pull request, só que só quando são alteradas essas coisas aqui, né? Se vocês quiserem ver aqui o do Curso de Fecha API.

**[00:59:19]** Ele tá todo aqui ó, aí você vê que você roda aqui, hoje eu atualizei algumas coisas aqui Aí ele rodou três jobs, né? No 3.11, no 3.12, no 3.13 Aí você vem aqui, pode olhar o 3.11 E aí todos queimem aqui De como aconteceu e tudo mais, aí vocês podem futricar aqui nesse rap e dar uma brincada e tudo mais Tem bastante coisa aqui, né? É... É... É interessante, né? Esse tipo de coisa Então tem muita coisa legal, né?

**[00:59:51]** que dá para fazer com integração contínua. Deixa eu ver o que mais se perguntar. Esse curso é gratuito, sim. O curso está acontecendo agora, nesse exato momento. É certo que tinha perguntado, pensando em pull requests, é possível criar um trigger para quando um PR for aberto já rodar o pipeline? Sim, então é isso que acontece, né? Tipo assim, quando a gente usa esse...

**[01:00:27]** Pull Request ou um Pull Request? Toda vez que alguém manda um Pull Request pra gente, ele vai trigar os eventos aqui, né? Então, por exemplo, deixa eu criar uma coisa nova aqui, né? Só pra gente brincar aqui. Só pra vocês verem como funciona o Pull Request. Eu vou criar uma brand nova. Então, Git Checkout, menos B. Quem foi que perguntou isso aqui? Só pra eu lembrar. Foi o Sérgio. Então, eu vou criar aqui uma brand chamada Sérgio. Vou colocar o WIP.

**[01:00:55]** Só para vocês saberem o que está acontecendo. Então legal, eu vou só dar um eco aqui, né? Name, Oi, Sérgio. Aí ele vai rodar. Run, um eco, Oi, Sérgio. Massa, basicamente ele vai escrever Oi, Sérgio no pipeline. Ele vai fazer isso aqui. Oi, Sérgio. Massa, só para a gente brincar aqui e ver o que acontece. Aí criei essa brand nova aqui, então eu vou dar um git ad.

**[01:01:25]** Git commit, "-m", exemplo do pr para o sérgio. Git push. Aí ele vai falar que eu não tenho a sua branch lá, então eu vou colocar ela no upstream, né, para subir essa branch que a gente acabou de criar para o repositório. Então aqui ó, git push, sobe, né, set upstream. Pro git hub, origin e o nome da isha, e o nome da branch é whipsager, não? Beleza, subiu aqui, deixa eu ir lá no nosso projeto aqui.

**[01:01:57]** Eu estava mostrando outra coisa para vocês, vou voltar aqui no FastAPI Underline Zero, que é o que a gente está fazendo aqui no curso. Aqui, ele falou, o IP Sérgio foi subiu, tem um push recente a 19 segundos. Se eu der um compare e pull request aqui, exemplo PPR do Sérgio. Oi, estamos em aula. Aí eu vou criar um pull request aqui, create pull request. Aí é o que vai acontecer aqui. Ele está rodando aqui.

**[01:02:33]** Ah, some checks haven't completed yet, né? Ou seja, tá rodando algumas coisas. Aí ele tá rodando o pipeline do pull request aqui. Se vocês quiserem ver aqui, eu vou mandar o link. Aí ele tá rodando aqui, né? Ele rodou um do push, porque quem deu esse push foi eu, né? Aí essa canazes, porque eu sou dono do repositório, eu tenho acesso a brinte, né? Mas quando você vem de fora, só vai rodar o pull request, né? Thiago, muito obrigado pelo teu... pelo teu super chat, mano, ó. Me ajuda demais, mano. Valeu muito.

**[01:03:11]** Aí, rodou aqui, aí a gente pode mergiar o porrequest, aí a gente pode ver, né, o que aconteceu, né, porque agora tem o oisérgio aqui. Aí provavelmente ele vai ter a resposta aqui, ó. Run oisérgio, aí é a resposta. Oisérgio. Pô, muito, muito legal. Deixa eu ver o que mais ficou aqui de pergunta.

**[01:03:41]** Asse várias vezes, fazendo os exercícios, perguntei alguma aula de réu para configurar o E-Max, que rode Python da forma que você mostra. Pô, eu tenho uma playlist de E-Max que ficou aqui há muito tempo, mas ela não está atualizada aqui. Deixa eu ver aqui, estou gostando demais das aulas, me virando e pô, tamo junto, mano. Qualquer coisa que precisar, tem o grupo lá de coisa muito top, o BuildBot, o BuildWatt é muito legal. Adorio, um beijo para você.

**[01:04:07]** Ah, que mais tem aqui? Du, aí o Ulisses fez uma pergunta muito legal aqui. Ele falou o seguinte, olha, Du, o ideal é rodar os testes antes do PUSH. Isso ficaria no pré-comite ou tá errado? Então, vamos lá, vamos lá. É comum pra vocês o que o Ulisses falou aqui? Pré-comite. Pré-comite?

**[01:04:33]** Se não, eu posso explicar aqui. Existe uma ferramenta dentro do assunto git, né? Porque a gente não falou muito de git no curso. Existe o pré-comit. Existem vários hooks, né? Várias nações, igual a essa que a gente fez no próprio git, tá ligado? Aí, se a gente vier aqui, ó, git hooks, vou mandar aqui pra vocês. E aí, você pode fazer várias coisas dentro do próprio git aqui, né?

**[01:05:01]** Então aqui ó, ah, quando eu faço um re-base, posso fazer um pos-re-base, um pre-re-base, eu posso executar um preparar mensagem de comit, aí um dos hooks é o pre-comit. Ou seja, toda vez que eu faço um comit, toda vez que eu vou fazer um comit no Shell, ele executa um determinado, uma determinada ação aqui dentro. Tem pre-post para um monte de ações aqui, né?

**[01:05:30]** Aí dentro do Git aqui, deixa eu mostrar pra vocês, dentro do seu PC aí, na pastinha que você tá rodando, você tem uma pastinha do Git aqui, e aqui existem hooks, aí olha os hooks que existem aqui, ApplyPatch, CommitMessager, Post e tal, aí tem um desses hooks que se chama Precommit, e aí ele faz algumas coisas, isso aqui é um bash, né, shell script, e aí você pode configurar pra algumas ações acontecerem aqui,

**[01:05:59]** toda vez que você for fazer um commit. Aí antes de fazer um commit, ele executa uma coisa. Aí você pode colocar ele para rodar os testes aqui dentro, se você quiser. E aí tem o pré, tem o preparo commit, aí tem o push checkout, send email, update. Tem vários hooks aqui do Git. Só que provavelmente, o que o Lisa está falando aqui é de uma ferramenta Python que se chama pré-commit. Que é essa aqui, ó.

**[01:06:31]** Isso é uma ferramenta do Python, que você pode configurar no seu ambiente e tal. E aí ele executa algumas coisas, então o que que vai acontecer aqui? Você escreve um YAML, igual do GitHub, igual do Compose, e aí você pode falar o seguinte, olha, cria uns hooks aí, aí roda...

**[01:06:53]** Roda o roof, roda o teste, roda um monte de coisa, e aí quando você faz esse pre-commit install aqui, ele sobre escreve o arquivo de hook que fica dentro da pastinha do git aqui. E aí você toda vez que for acontecer, ele vai configurando algumas ações aqui dentro.

**[01:07:11]** E aí você pode mandar ele formatar o código, rodar o linter, fazer o teste, verificar n coisas, qualidade de código e tudo mais. No final das contas, ele vai usar essa ferramenta, vai colocar lá dentro da pastinha oculta do git de hooks. E aí isso acontece lá. Aí essa pergunta que ele fez aqui, agora entendidos aqui o que significa o pre-commit?

**[01:07:41]** Aí a pergunta do que o Liz fez aqui é o seguinte, o ideal é rodar os testes antes de dar o push e ficaria no pré-commit ou tá errado. Então, vamos tentar entender. O ideal é que você rode os testes sempre que você achar que existe a necessidade de rodar o teste. Os testes eles são pequenos, eles rodam rápido e eles têm esse objetivo de ser um ciclo positivo de feedback. Então você tá fazendo o rodo teste, tá fazendo o rodo teste, tá fazendo o rodo teste e aí você vai...

**[01:08:09]** Rodando o teste toda vez que for preciso. Existe inclusive até uma metodologia que se chama TCR, que é Test Commit Revert, que ele fica tipo toda hora rodando os testes e quando o teste falha ele reverte o código, é uma loucura. Mas aí o que acontece dentro disso? A ideia é que você rode os testes sempre.

**[01:08:31]** Sempre que você tiver uma dúvida, sempre que você quiser testar um comportamento, antes de fazer qualquer coisa, você roda os testes, testes são ótimos, sabe? Tem o TDD, né? Que é tipo assim, você escreve o teste e vai rodando os testes para ver se vai passando o código que você vai escrevendo, depois, né? Então você escreve o teste primeiro, então existem várias metodologias disso. E aí o que acontece?

**[01:08:54]** O ideal é rodar o teste antes de dar push? Sim, você pode colocar isso no pré-commit, você pode sempre rodar na maneira que você quiser, rodar na mão e tal. Só que a grande sacada aqui é que eu quero entender, Ulisses, se a sua pergunta é sobre o esquema do CI, né? Tipo assim, pô, por que que eu vou rodar no CI e se eu posso configurar um rook pra rodar o teste sempre antes do commit?

**[01:09:18]** É por aí que permeia a sua dúvida? Só pra eu entender se a gente tá na mesma tecla aqui. Se for isso. Enquanto ele fala, a gente vai conversando aqui sobre outras coisas. Aí o Sérgio pergunta se o Deploy vai ser feito em alguma cloud, se a gente vai fazendo Fly I On na próxima aula. E inclusive, se vocês quiserem já ir se adiantando, tentando fazer o... O Deploy certamente, como eu passei um tempão escrevendo aqui, já está aqui, né?

**[01:09:59]** Então, tá aí. Se quiser já ir tentando, acelerando a parada, então tá tudo aí. Massa? Aí o Victor perguntou, eu vim do Jan, comecei a estudar a Facebook, eu ensino tudo o que é de código, né? Eu não ensino qual editor de texto eu uso, aí é contigo, saca? Essa pergunta aqui vai. É coisa que não acaba mais, quanto informação? Ah, tamo junto.

**[01:10:32]** Então legal, aí só pra fechar essa pergunta aqui do Ulisses aqui, a gente vai descansar, vai curtir o feriado, que é o seguinte, o ideal é rodar o teste antes de dar o push e tal, legal, a ideia da integração contínua é o seguinte, menos, às vezes, e é aquilo que eu falei lá no começo da aula, não é? Assim, ah, eu tenho que rodar o teste antes de subir? É bom que você execute o teste antes de subir. Aí o Ulisses respondeu aqui.

**[01:11:01]** Isso, tipo, se você está rodando teste em dev, só permite que o PURSE, se o teste passar, tem que adicionar no CI também. Então, a ideia é o seguinte. Quando você está desenvolvendo aqui, você está na tua máquina, fazendo a feature A. Eu estou na minha máquina, fazendo a funcionalidade B, e o André está na máquina dele fazendo a funcionalidade C.

**[01:11:23]** É legal você ter o pré-comit, um rook, uma coisa assim, porque você sabe que toda vez que você faz o PUSH, o seu projeto está funcionando. Aquilo que você está mexendo, dentro do escopo das suas alterações, que você quer integrar no projeto, elas funcionam. Só que, no decorrer das coisas, eu tenho que juntar o meu cu do André com o seu, com o do Regis e com o do, sei lá, mano. Cu do Victor, que chegou hoje aqui. E quando a gente tem que juntar tudo?

**[01:11:52]** já não tem mais commit. Você entende que já está tudo na plataforma? Então eu preciso mixar essas coisas. Eu preciso juntar outras pessoas, então a integração continua vai funcionar nesse momento, que é um lugar que o pré-commit não vai poder atuar. Não existe pré-commit porque já está no repositório. Então a ideia da integração continua é literalmente integrar as coisas, então garantir

**[01:12:20]** que o trabalho de N pessoas funciona em conjunto. Massa, faz sentido? O Victor falou que foi muita coisa então, né? Porque nós já estamos na penúltima aula do curso, né? Boa, entendi. Não estava pensando em equipe. Sim, então é isso. A ideia do CI é sempre essa, né? De juntar as coisas, né?

**[01:12:49]** Porque quando você tá rodando só na sua máquina, é tudo bem. Inclusive, você pode rodar o Act, né? E o Act já rola do fluxo todo, de validação. Então vai ficar mais simples, dependendo do que aconteceu, né? Então legal, se ninguém tiver mais nenhuma pergunta, a gente fica por aqui, vamos curtir. Liberando mais cedo de novo, hein? Aí na semana que vem, a gente volta, né? Pra conversar sobre... sobre o deploy. E tudo mais. E...

**[01:13:27]** responda um quiz responda um quiz porque é importante né para fixar e bota o seu si aí para rodar aí também e aí bota mais passos inventa faz coisas dá oi pro ségio tá ligado no seu si aí também vai colocando as coisas saca é a ideia essa vai vai vai brincando vai se divertindo aí que essa essa é a coisa né bom legal se estiverem alguma dúvida sobre isso mandem lá no grupo

**[01:13:59]** No grupo do Telegram, o link está aqui na descrição, a gente vai se falando. Obrigado aí para quem ficou, né? Meu feriado, eu sei que é difícil. Beijinho para vocês, e a gente se vê na terça-feira, na semana que vem, para fazer o deploy, botar na sua aplicação no ar, pode mandar o link para os outros e falar, mano, olha o que eu fiz no curso. Fora da sua rede local, né? Então, beijinho para vocês, a gente vê semana que vem, mais dúvidas, a gente...

**[01:14:29]** Se tromba lá no grupo, se alguém precisar, dê o like e não dê o like ainda, para a galera conseguir ver depois e até a terça. Tchau!

