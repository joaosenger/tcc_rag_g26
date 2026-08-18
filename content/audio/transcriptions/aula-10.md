# Transcrição da Aula: aula-10.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:09]** Olá, pessoas! Boas-vindas! Há mais um dia aqui do nosso Curso de Facha IPI. Hoje a gente está na aula 10, para quem não me conhece o Dono Saulo e Boas-vindas. Sinta-se em casa aqui com a gente. Antes de eu começar, não é aquele feedback que é sempre bom. Vocês estão me ouvindo, vocês estão me vendo. Só para a gente saber se está tudo certo. Boa noite aí todo mundo que chegou. E é isso. Ovo e óleo bem. Então, está top.

**[00:00:39]** Estamos aqui. Legal. Então hoje a gente vai fazer um crude para um gerenciador de tarefas, que era o objetivo inicial do nosso projeto. A gente passou um tempão criando essa coisa que era um esquema de gerenciamento de usuários e tudo mais. A gente construiu toda a base. Agora a gente precisa programar alguma coisa nessa aplicação. E a ideia aqui é que a gente faça isso no dia de hoje.

**[00:01:08]** Bom, como sempre, vale relembrar que a gente tá na 4.0, né? Então, quem quiser o livro texto ou qualquer outra coisa que o vale, o material em texto, tá tudo disponível pra ser consultado e tudo mais. Pra quem estiver acompanhando em texto e vendo a aula, eu inverti um pouco a ordem das coisas pra gente fazer um vídeo, mas o material é o mesmo. Bom, e o que a gente vai fazer? Então, a gente vai criar...

**[00:01:37]** algumas rotas para fazer um gerenciador de tarefas. Então, a gente vai criar tarefas. Tarefas, quando eu digo tarefas, estou falando num tio do list, né? A gente vai ver mais afundinho o que que é. E bom, beleza.

**[00:01:49]** A gente vai criar todo o crude, né? Hoje é tipo uma mega revisão, né? Todo o crude dos gerenciadores de tarefas, um router específico e tudo aquilo, fazer com que só o usuário do dono da tarefa possa acessar e modificar elas e criar um montão de testes e tudo mais. Basicamente a nossa aula de hoje é um atacadão, né? Um juntadão de tudo o que a gente fez até agora. Então, hoje é meio model speedrun de tudo o que a gente vê no curso, como se fosse uma revisão mesmo.

**[00:02:16]** Bom, como é que funciona um tio do list, né? Pra quem nunca viu um tio do list, eu fiz um tio do list uma vez quando a gente tava fazendo o curso de Selenium, que foi alguns anos atrás. Basicamente, um tio do list é uma coisa parecida com essa, né? A gente registra uma tarefa, beleza? Eu tenho coisas pra fazer, né? Sei lá, eu tenho que comprar comida e no mercado tal e comprar, sei lá, arroz.

**[00:02:46]** é urgente ou não essa tarefa, sei lá, a gente coloca na fila de coisas pra fazer a outra coisa que você tem pra fazer, sei lá, dormir eu tenho que escovar o dente e essa aqui é urgente beleza, aí ficou aqui na frente, as outras não tem descrição, sei lá, essa aqui eu tô fazendo já escovei o dente, tô indo no mercado comprar comida

**[00:03:08]** E, sei lá, depois eu durmo e tal, e a gente fica com esses estados pendentes, né? Como se fosse um cambam de tarefas a fazer mesmo. É basicamente isso que a gente vai fazer hoje. Só que, obviamente, sem essa coisa de front e tudo mais, é tudo no back. Mas para quem nunca viu um tio do list, tá aqui, né? Esse é o formato dele, né? Então, é basicamente isso que a gente vai fazer.

**[00:03:31]** Endpoints para criar tarefas, alterar tarefas, deletar tarefas, criar um router para isso, criar testes, criar fixtures, sabe? Tudo. Então, por isso, né? Um speedrun de tudo isso. Então, beleza. A gente vai por partes hoje, porque como a gente vai fazer muitas coisas?

**[00:03:53]** Como eu resumão de tudo, né? Eu espero que eu não tenha que ficar explicando todas as raízes das coisas, né? Hoje a gente vai programar mais com os recursos que a gente construiu durante, sei lá, as outras dez aulas, né? As outras dez dias que a gente se encontrou aqui. Então, a gente vai criar um halter, a gente vai criar uma nova tabela no banco, a gente vai relacionar as duas tabelas, né? De users com a de Tudus, novos esquemas, novos endpoint e muitos testes, né? É isso. Então...

**[00:04:21]** O primeiro endpoint sempre aquele que é um pouco mais chato, porque tem que fazer toda a estrutura, então vamos lá. Primeira coisa que a gente vai fazer é criar um router novo. Bom, router, a gente já sabe, a gente tem um lugar certinho dentro da nossa aplicação para fazer isso, né? Tem os routers aqui, então eu vou criar um que se chama todo.py. Só para ver se eu coloquei o nome certo, é isso aqui.

**[00:04:47]** Bom, aí a gente vai. Todas as coisas que vão ser Tudus, todas as coisas do crude, vão ficar dentro desse lugarzinho, quentinho, dentro do nosso coração. Então, como é que a gente cria o Halter? Então, FromFestAPI Import Halter. API Halter. Aí, vou só ver o nome que eu deixei aqui, eu deixei Halter mesmo, para ficar igual ao material, né? Então, Halter, API Halter.

**[00:05:17]** Beleza, a gente tem um roteador de umas coisas que a gente precisa interagir para ver como elas vão funcionar. Então, a gente tem o tags, né? E a gente tem o prefix. Para a gente evitar de ter que ficar reescrevendo muitas coisas. Bom, qual que é a tag do Tudu? É Tudus, né? Não tem muito mistério. E o prefix também, a mesma coisa. Então, Tudus, isso aqui para ficar lá documentado, né? Uma classificação no Swagger, né? Na nossa API.

**[00:05:47]** E o prefix é a base, a raiz da URL que a gente vai usar aqui, que eu vou chamar de chudu também, barra chudu. Bom, com isso aqui a gente já tem um roteador, né? E o que a gente precisa fazer? A gente precisa pegar isso aqui e plugar na nossa aplicação, né? Lá no app, onde a gente tinha as coisinhas.

**[00:06:07]** E aí fica nesse esquema, né? Fez sentido aqui como é que a coisa vai expandindo? Isso é uma pergunta sincera, porque lembra que a gente deu uma refatorada para tirar tudo que estava meio bagunçado e a ideia aqui é essa, né? Então, toda vez que a gente precisar criar um conjunto, né, um domínio de operações novas dentro da aplicação, a gente cria um roteador lá no mantém tudo o que precisa lá e a gente traz aqui para o app para ter um lugar central onde a gente centraliza todas as coisas.

**[00:06:36]** fez sentido isso só pra saber mesmo conversando de boa albano muito obrigado mano pelo teu super chat e espero mano que você vá melhor aí nessa recuperação que eu sei que você tá doentinho mano então melhoras aí então legal a gente tá no routers aqui eu vou importar o to dos

**[00:06:57]** o nome do nosso arquivo, eu ia falar, eu falei que iria chamar Tudus, então eu vou mudar o nome do arquivo só para ficar certinho com que a gente está no texto, né? Então, não vou deletar, mas eu vou renomear. Tudus.py. Yes, pronto. Agora a gente importa do Tudus. A gente registra ele aqui como mais um halter, né? O Tudus halter. A partir desse momento, se a gente subia a nossa aplicação, né? Com task RAM.

**[00:07:27]** Vamos rodar aqui. Então, só voltar para a raiz do repositorio. All the way to Ram Task Ram. E se a gente falar no browser, no localhost 8000, que é onde a gente estava aqui, ainda não subiu. Em teoria tem que estar aqui. Ah, beleza. Só estava um pouquinho demorado. Docs.

**[00:07:56]** Vai ver que a gente tem aqui, né? O default, o alpha users, mas ele não apareceu nenhum, né? Essa é uma característica interessante do Face API, que quando a gente cria um router que não tem nenhum endpoint, ele não documenta isso. Ele não criaria uma classificação para ninguém aqui. Então, isso é ótimo. Tem um lugar que a gente confia que está tudo certinho, né? Isso é muito massa. Então, legal. Agora a gente criou esse roteador, a gente vai começar a implementar as coisas aqui.

**[00:08:26]** E aí o que que a gente precisa implementar aqui? A primeira coisa é o endpoint de create, né? Eu vou seguir a mesma ordem que a gente fez nos users, né? Então a gente precisa de um halter, e a gente já tem ele, então halter.post, a gente vai criar alguém aqui. E como a gente já tem o prefixo, então vai ser só barra, né? E o que que eu dei aqui? O nome?

**[00:08:58]** Aí essa rota vai ser assim porque todo o nosso projeto está sincrono, né? A partir desse momento, ele tem que detectar o refresh e tem que aparecer esse endpoint lá na dock para ficar tudo certinho na minha API bala. Aí eu dou os novos e depois eu dou risada sozinho. Pronto, a gente já tem aqui uma documentação dos Tudus funcionando. Tudo bonitinho.

**[00:09:22]** É tanto Run que parece que a música Psycho Killer é, você poderia habilitar o ambiente virtual, nem só dar o Task Run, depois não precisaria de tudo isso. Mas tudo bem. Deixa eu agradecer o Tiago aqui enquanto a gente vai fazendo essas coisas. Obrigado, mano. Beijão pra você, velho. Valeu demais.

**[00:09:42]** Isso me ajuda muito, esses super chats. Então a gente tem isso aqui, a gente não tem nada, né? A gente não sabe qual é o formato que o Tudu vai ter, o que que a gente vai ter que retornar, a gente não sabe o modelo de resposta, a gente tem ruim de ponte. Já é um bom lugar para começar, né? Então eu quero criar um esquema, né? E aí eu vou usar o próprio esquemas lá. Aí aqui entra uma coisa, né? Poderia criar uma pasta e separar os esquemas por domínio, se fosse necessário, mas eu não vou seguir essa abordagem.

**[00:10:13]** Porque, não. Mas se você quiser, você pode. O Albano falou que faltou eu, mas eu dei teu beijinho aqui atrás, mano. Desigir até melhoras. Então, vamos lá. A gente vai vir nos esquemas agora e a gente vai criar um novo esquema aqui.

**[00:10:48]** que é o class, eu vou deixar no mesmo esquema que a gente tinha, Tudu Esquima e Tudu Public, que a gente tinha o User Esquima e o User Public. Então vamos lá, Tudu, Esquima, ele é um BaseModel, e agora a gente vai começar a desenhar como é que esse Tudu List vai se parecer aqui.

**[00:11:10]** Então, eu imagino que a gente vai usar uma estrutura mais ou menos assim, onde a gente tenha o nome da tarefa que a gente quer fazer. Então, sei lá, dormir. A descrição da tarefa, né? Description. Description. Sei lá, porque é bom. E aí a gente tem o estado dessa tarefa, né? Que eu vou chamar de stage.

**[00:11:38]** Então, é mais ou menos esse JSON que vai trafegar aqui. Então, aí o state, a gente pode pensar naquele campanha que a gente tinha aqui atrás, né, que eu brinquei com vocês. Então, pode ter um tu-du, né, que é a fazer o doing, que é o fazendo o feito, mas aí a gente precisa poder jogar no lixo, tem alguns outros estados que a gente pode pensar aqui. Mas, basicamente, a gente tem o status, ó, doing.

**[00:12:02]** Mas eu acho que, por enquanto, a gente pode trabalhar com o modelo dessa forma aqui, bem simples. Então, a gente tem o name, que é uma string. A gente tem description, só pra não escrever errado. S, T, R. E a gente tem o state. E o state aqui, eu quero fazer uma coisinha que a gente ainda não fez aqui. Que é o seguinte, eu quero definir uma lista.

**[00:12:29]** de possibilidades enumeradas, ou seja, eu quero que seja o 1, ou 2, ou 3, ou 4, sabe nesse sentido. Então, para a gente não poder ter estados intermediários malucos, eu quero pensar que a gente vai fazer o seguinte, eu tenho um estado que vai ser... Tudu, um estado que vai ser doing, um estado que vai ser done, um estado que vai ser trash, para coisas que você jogar na lixeira aqui...

**[00:12:53]** Então, eu separei aqui mais ou menos. Então, a gente tem um draft que é um... Ah, que eu ainda não mandei, mas sei lá. Ele está em algum lugar para a gente terminar ele depois. To do, do-ing, né? Então, a fazer, fazendo, pronto e uma lixera. Básica, caso você precise depois, fala, nossa, dele tem um negócio que eu não precisava deletar, aí você tem um lugar para consultar na API. Caso você precise disso, só o front, por exemplo, precise disso. E aí, eu vou fazer isso aqui.

**[00:13:23]** usando essa brincadeira aqui do Python que se chama Enum. Enum é uma classe que só tem que tem estados finitos. Saca, então toda a instância de Chudu Stage ela vai ser algum desses aqui. Ou vai ser Draft ou Chudu ou Duin ou Dony ou Trash. Lembra quando a gente faz no front um Select Box na que a gente vai ter que escolher uma opção? A ideia é essa.

**[00:13:48]** Então, eu vou importar o Enum do Python aqui pra gente brincar. E onde eu vou fazer isso aqui? Eu vou fazer isso lá no Database. Ah, por quê? Porque a nossa no Database não, no Models. Por que a gente vai fazer aqui? Porque o nosso modelo do banco de dados também vai usar a mesma coisa. Então, vamos lá. From Enum import Enum. E aí aqui eu vou criar essa classezinha de Enum. Class.

**[00:14:16]** Aí a gente tem o state, ou to do state. E aí ela é um string, porque o objeto é de texto e também é um enum. E aí a gente tem aqueles estados, esse aqui, esses estados finitos, só pra não ter que ficar escrevendo draft, tu, tal, tal, tal, beleza, a gente usa o prontinho aqui. Legal, basicamente são esses atributos que a gente vai poder ter aqui, então o estado é finito. Mas só faz sentido isso aqui?

**[00:14:52]** o estado ser finito. Então, a gente vai colocar aqui no state, a gente vai importar aquele to do state. To do state. Aí aqui no meu editor ele já importou aqui direitinho, mas está aqui. Fast zero, models, to do state. Ou seja, a gente tem estados finitos para a gente poder entrar com esses dados. Então, toda vez que alguém mandar, vai ter que mandar o nome, a descrição e o estado, o state.

**[00:15:28]** Se a gente for aqui, a gente já tem uma entrada aqui, que é o Tudu, que a gente tem aqui. Tudu, e aí ele é o Tudu State. Ou o Tudu Esquima aqui no caso, que é o esquema que a gente vai esperar receber. Antes da gente implementar qualquer coisa, eu quero ver uma coisa na documentação com vocês, pra vocês entenderem como essa coisa se manifesta no Swagger. Olha aqui, quando eu for mandar o meu estado aqui...

**[00:16:00]** A gente ainda está aqui, com string, tal, tal, tal. E por padrão, ele já vem draft. Olha que interessante. Ele escolheu, selecionou um estado que a gente pode usar aqui. E aqui no to do esquema, se a gente for ver o estado, a gente sabe que ele é finítoa. Ele é draft to do, doing, done e trash. Ou seja, se a gente não mandar nenhuma dessas coisas para cá, ele vai dar 422, né? Unprocessable entity.

**[00:16:31]** Porque a gente tá mandando um valor que não é o valor que a gente deveria receber aqui. Então meio que ele junta as coisas aqui, né? Então dá opções finitas aqui dentro. Fez sentido esse N1 aqui? Enquanto vocês me respondem pra gente saber se deu tudo certo, deixa eu agradecer o Jordani aqui. Jordani, obrigado, mano, pelo teu super chat. Valeu, mano. Vocês me ajudam demais com essa parada. É óbano falou, o ID não seria melhor usar...

**[00:17:00]** algo único mesmo, tipo um UID? O ID também é único, o ID do banco de dados ele não se repete nunca. Então a gente vai usar isso, mas lá na frente. Legal, então é isso aqui. Se a gente mandar aqui, sei lá, batata e mandar executar, a gente tomou um 422. E aí, olha o erro, como é sensacional. Input should be draft to do, doing, done, or trash.

**[00:17:38]** Tá vendo? Então, o input que a gente recebeu foi batata, mas a gente precisava enviar uma coisinha dessa aqui. Então, ele já dá o contexto, o expected, falando para a gente exatamente o que deveria ser enviado aqui dentro. Poderia definir um padrão para o state, no caso? Draft, se nada foi enviado, poderia. A gente não viu isso aqui no curso, né? Tipo assim, não está planejado para falar disso, mas você poderia fazer o seguinte, field e passar um default aqui, né?

**[00:18:09]** Por exemplo, o default vai ser Tudu. Saca? Aí você poderia, em vez de chamar Tudu aqui, você chama o TuduState.tudu, assim, porque ele é uma classe. E aí agora, o padrão, caso não seja enviado, é o Tudu. Vamos ver o que acontece aqui? F5. Aqui, o stage. O padrão é Tudu. E se ele não foi enviado, então vamos tirar aqui. Tirar essa virgula daqui. Enviou.

**[00:18:43]** Ele não respondeu nada, porque a gente não programou a resposta, mas por padrão, quando a gente não envia, fica Tudu. Mas eu quero que isso sempre seja enviado. E aí é que esse parâmetro é o default, caso não tenha ficado claro. Você poderia fazer dessa forma. Inclusive, eu vou até deixar aqui. Por que não? Então, se a gente não enviar, o state é Tudu. Fez sentido aqui, Pedro?

**[00:19:12]** O que que aconteceu aqui? O que que a gente fez? Então a gente limitou esse campo para, por padrão, usar o Tudu. A gente poderia usar o fio de pra várias outras coisas aqui, mas eu vou me limitar nesse momento a isso aqui. Massa? Vou me respondendo, eu preciso do feedback de vocês pra gente ir andando aqui. Então eu vou criar um outro coisa que vai ser um Tudu Public, que é isso aqui, que erda daquele esquema que a gente já tem.

**[00:19:45]** que é isso aqui, então ele erda todas as características aqui de cima, então ele tem Name, Description, State e OID que é o inteiro, que aí é o esquema que a gente vai retornar quando for chamado o nosso endpoint aqui. Então deixa eu fechar esse app, voltar aqui no ToDoos, então o ResponseModel, o ResponseUnderlineModel vai ser o esquema que a gente vai importar daqui que é o ToDo.

**[00:20:21]** Public, que é o Tudu público, né? O Jordane falou, abre o maixo pra pôr isso no texto, pode ser, pode ser. Tem mais um momento aqui que eu vou querer falar com vocês do Field de novo e a gente pode pensar numa outra forma disso. Então vamos fazer o seguinte aqui, vamos retornar o Tudu, Return Tudu, só pra ver o que acontece. Ele não vai funcionar, né? Porque ele não tem ID, né? Então vamos lá, tá aqui. 9.5.

**[00:20:53]** Try it out, state to do por padrão. Tentamos responder, mas ele deu internal servererror, né? Porque a gente não mandou o id, né? O id tá faltando aqui. A gente mandou o seguinte, a name string, description string, state to do. Mas a gente não mandou...

**[00:21:13]** esse esquema pra cá. Legal? Implementamos aqui o primeiro endpoint, a gente tem os modelos que a gente precisa, o esquema de entrada, o esquema de saída, aí a gente precisa fazer o resto das coisas agora, né? Que é o seguinte, a gente tá todo mundo, qualquer pessoa pode mandar uma requisição aqui, né? E a gente não quer que isso aconteça, né? Então, por exemplo, aqui eu tenho que limitar que só vai criar um to do quem tiver user, né?

**[00:21:45]** Esse é um dos pontos, né? Então, a gente precisa daquela coisinha que a gente definiu lá que era o current user, né? E a gente precisa também da session. Então, a gente precisa da session e do user aqui. Legal. Como é que a gente lembra? Como é que a gente fez para definir aqui? A gente tinha o tipo annotated, né? Vamos lá. From typing import annotated. E aí a gente vai falar que session é annotated.

**[00:22:18]** de alguma coisa, né? Então só vamos passar aqui. Session. E o user era o current user, né? Que também é um annotator de alguém aqui, né? A gente pode usar dois pontos aqui, se preferir, que é o certo, né? E é que a gente vai pegar o current user. Legal. Para fazer a session, a gente precisa do async session aqui, né?

**[00:22:49]** que é do SQL Alchemy, então, da extensão do SQL Alchemy, a gente tem esse annotated aqui, e aqui é igual, né? Não sei o que fiquei na cabeça aqui. A Sync Session, e aqui a gente vai pegar o User, né? Que é do nosso modelo 1, lá que a gente tem aqui, que a gente não importou nesse arquivo ainda. Então, From, Fast API, 0.Models, Import, User.

**[00:23:22]** Aí a gente precisa passar os campos aqui que a gente quer. Então, a Session ela vem do Database, né? Então, vamos lá agora de novo. Então, From Fast API 0.database import Gatch Session. Isso aqui, ganho Gatch Session. E aqui o User, que a gente vai passar, ele é o Gatch Current User, né? Que a gente definiu lá no Security.

**[00:23:53]** Então, from FastAPI0.secured import get current user, que são as coisas que a gente precisa aqui. Aí, para essas coisas serem executadas da maneira que a gente quer, a gente vai ter que passar o depend aqui, né, do FastAPI. Então, depends. Opa, eu estou no type aqui, pera aí. Depends.

**[00:24:18]** Então, a gente fala que isso aqui depende, né? Vai injetar o GetSession e aqui a gente vai injetar o CurrenteUser. Pronto. A partir de agora, para fazer essa interação aqui, a gente precisa estar logado, né? Vamos ver o que que acontece aqui? Na API, vai ter que ter um cadeadinho aqui, né? Off Users To Doos. Aí, pronto. Tem o cadeadinho. Então, a gente precisa logar para poder estar aqui dentro.

**[00:24:49]** Então a gente vai ter que gerar o token, fazer aquele processo que a gente definiu de autorização por conta do current user aqui que a gente pegou. Mas até então sem nenhuma grande novidade aqui, a gente fez exatamente o que a gente já fez em todos os outros casos. Acho que a única novidade que a gente ganhou aqui foi esse enum para poder enumerar, fazer as coisas mais simples aqui, nesse ponto. Massa, fez sentido até aqui?

**[00:25:21]** e vão conversando comigo, vão conversando comigo. Beleza. A gente fez tudo o que precisava, só que para a gente persistir, tem um ID e fazer essa parte do trabalho, agora a gente precisa criar uma tabela, né? E a tabela, ela também não foge muito daquele esquema que a gente viu antes, né? Ela tem o título, a description, o estado, o ID. A gente não passa quando inicia a tabela, ele é a chave primária, né?

**[00:25:55]** E o nome da tabela é Tudus. Basicamente, o que a gente já tinha feito aqui antes, né? É bem parecido, né? Só que a diferença dessa tabela aqui é que para a gente se saber, depois a gente vai ter que fazer um relacionamento, né? Eu preciso saber quem é o user que é o detentor, né? Quem tem essa... esse...

**[00:26:22]** Esse tchudu, essa tarefa a fazer, ela pertence a alguém. Alguém vai ter que criar essa tarefa. Então a gente vai precisar fazer uma associação entre essas duas tabelas aqui dentro. E aí é para isso que entra esse foreign key, chave estrangeira. Aí o foreign key vem do escaleal, que deixa só importar, e a gente discute aqui o que está rolando.

**[00:26:52]** Então a gente está falando que dentro dessa tabela tem uma chave estrangeira, ou seja, uma chave, um campo que é de outra tabela, e de qual tabela é isso aqui? Então é da tabela Users, que é essa aqui, que está mapeado com string. Então é da tabela Users, o campo ID dessa tabela. Então agora a gente sabe que toda vez que alguém for persistir uma coisa no banco,

**[00:27:24]** A gente vai ter que passar quem é que gerou essa tabela. Fez sentido até aqui, tá tudo certo? E olha que interessante, uma outra coisa que a gente fez é esse state aqui, que ele tem o MAPED e o MAPED dele é to do state. Ou seja, no banco de dados isso aqui também vai ser uma restrição. Então, só vai poder ser armazenado na tabela o draft to do, do, endone e trash.

**[00:27:52]** Basicamente, essa é a relação que a gente tem aqui no primeiro momento. Aí, alguém vai falar, bom, mas e se eu quiser do user saber qual é os Tudus? Então, a gente vai fazer isso daqui a pouco. Vamos começar com um relacionamento mais simples possível aqui. Massa, vão conversando comigo. Tá todo mundo quietinho hoje. É o que a gente vai fazer? Basicamente, vamos criar um Tudu, né? Quando alguém mandar aqueles dados pra gente aqui. Que é esse Tudu que a gente recebeu.

**[00:28:25]** A gente vai chamar a tabela de Tudu, que a gente não tinha chamado ela nesse arquivo ainda. Então, a gente tem aqui Tudu. Aí a partir desse Tudu, a gente vai precisar do user ID, lembra? O relacionamento que a gente fez. E como a gente tem o user, a gente vai trazer ele daqui. User.id. É o primeiro ponto aqui. Essa é a única relação que vem de um lugar diferente. E aí todas as outras coisas, o name, é name que eu dei aqui, ou é title.

**[00:29:01]** É title, hum, desculpa. Eu vou arrumar os esquemas pra ficar igualzinho aqui, aqui tá name, mas aqui é title. É title e description. Só pra caso eu tenha inscrito errado, isso aqui? Description. Então massa, então o title dessa, disso aqui é o que veio no chudu, ponto, title. O description é o chudu, ponto, description. E o state é o chudu.

**[00:29:35]** ponto state. Aí é que a gente preencheu, né? Com um campo de outra tabela aqui, só pra lembrar isso aqui, ficar certinho. Criar uma pasta pra enumos, router, model, se é útil, se faz sentido organizar assim, cara, cada um organiza do jeito que gosta mais e que funciona melhor, né? Eu ainda não vejo sentido em a gente fazer uma separação tão grande de coisas, né? Quando a gente começa a organizar demais, a gente coda de menos, né, sabe?

**[00:30:11]** Então, o que que a gente precisa fazer agora? A gente tem a session, a gente adiciona isso aqui na session, add esse Tuduzinho que a gente criou aqui. Aí eu coloquei DB Tudu, só pra ele não ficar reclamando o nome aqui, vou deixar o mesmo nome, DB Tudu. Aí a gente vai dar o inserir ele no banco, né? Então await session.commit. Aí como a gente quer o ID aqui, await session.refresh.db.tudu.

**[00:30:49]** Aí a gente pode retornar o db2. Porque agora a gente tem o id nesse user aqui. Massa? Já subiu aqui, vamos ver o que que rola se a gente consegue inserir isso aqui. Agora a partir do momento em que a gente vai fazer um login primeiro, né? Então aí o fluxo fica um pouco mais complicado. Eu preciso vir aqui, eu preciso criar um user, né? Porque você acha que eu lembro algum aqui, né? Eu provavelmente eu tenho esse aqui, né? User example string, vamos ver? Não tinha, mas agora a gente tem.

**[00:31:30]** Então o userExampleStringString. Vamos logar, pedir nosso token, try it out. A gente pode logar aqui, ó, porque fica mais fácil também aqui no autorize. Então o nosso username aqui é o email, né? E a nossa senha é String. Então é String, arrobaexample.com.

**[00:31:59]** Acho que é isso. Vamos logar, autorize, não autorizado. Não lembra a senha, pera aí. É user, arrubexample. É isso que deu errado. Então vamos autorizar de novo, user, arrubexample, string. Autorize, beleza. Estamos logado, ou seja, agora a gente pode acessar tudo que tem cadeadinho. Nos Tudus, vamos criar esse Tudu aqui. String, string, Tudu. Só para ver se está tudo funcionando. Try it out.

**[00:32:33]** Execute. Legal. Name, description, state to do. Ah tá, porque ainda tá com... Eu não dei F5. Agora vai. Title. Execute. Not authenticated. Legal. Porque a aplicação reiniciou, então a gente vai precisar do lugar de novo. String. Authorize. Não salva isso aqui. Mandar de novo agora. Deu internal server error.

**[00:33:08]** Deu um erro interno aqui. O que aconteceu? Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

**[00:33:46]** Porque apenas criar o esquema não precisou fazer uma migração. Sim, é isso que deu erro aqui. A gente não tem migrations, né? Então agora entra a hora de a gente fazer a migração desse esquema aqui. Então, como é que a gente cria uma migração? A Lambic. Deixa eu entrar no Shell para ficar mais simples. A Lambic. Eu tenho exatamente a instrução que eu queria colocar aqui no slide, só para ficar com os mesmos nomes aqui. A Lambic Revision.

**[00:34:21]** Autogenerate, Create To Do Tables. Legal, criamos essa nova versão da migração e a gente pode aplicar, né? Alambic, Upgrade, Hedge. Legal, então fomos para a última versão da migração. Se a gente quiser olhar aqui, vamos ver o que que redicionou nessa migração aqui. Versions, Create To Doos, essa aqui de baixo. Olha que massa, a relação que ele fez aqui.

**[00:34:56]** Então ele falou, ó, isso aqui é um inteiro, isso aqui é um inteiro, isso aqui é um inteiro. Olha o stage. Isso é no banco. Olha que massa. No banco, ele colocou esse enum do SQL Alchemy aqui. S-I-D-S-K-L-Alchemy, enum, draft to do, doing, done, trash. Aí o name é to do stage. A gente não colocou uma relação aqui, né? Saca. Não colocou uma relação aqui por default no banco, então...

**[00:35:26]** Ele está com um logo falso, mas não interessa aqui, né? E aí ele fala que, olha, temos uma fora aqui também, né? Então, a gente tem esse campo, né? Que é o User ID, que é o inteiro, e aí ele é uma chave estrangeira, né? Esse User ID é referenciado no Users ID, que foi aquela relação, o constraint que a gente fez aqui no Models. Então, ele também é refletido na Migration. Então, agora está tudo aqui.

**[00:35:58]** A nossa aplicação vai restartar de novo. Aqui vai restartar de novo, então a gente pode fazer de novo aquele esquema. Vamos lá? A gente vai ter que logar. Qual que é o user padrão? É esse aqui. User, tal, tal, tal. Copy. Então, vamos autorizar. Eu tenho que dar um F5, né? Autorize. Isso aqui, assim, é string. Authorize, beleza. Close. Vamos tentar criar agora o nosso studio. Try it out.

**[00:36:34]** Execute! Legal! Oh, funcionou! Olha que massa! A gente tem o título, a string, a description string, o stage to do, e o ID é um. Pô, muito massa! O meu editor de texto é o GuinuiMax. Legal! Tudo funcionando aqui. Bonitinho! Então agora entra aquele momento que a gente vai ter que fazer o quê? Testes, né? Testes! Testes!

**[00:37:11]** Bom, esse teste também não tem nada de mágico. Eu vou copiar ele aqui e a gente vai debater ele lá. Só que agora a gente não tem um teste aqui, né? Um teste de Tudu. Seria legal a gente fazer já que a gente tá seguindo os domínios certinhos aqui. Então, vamos criar um teste underline Tudus.py. Yes! Olha que interessante isso aqui.

**[00:37:46]** A gente não fez nada de mágico aqui, comparado, é de novo, aquele negócio que eu tava falando na aula passada. Você viu como construir a caminha pra gente poder deitar depois em cima? É muito melhor, tá ligado? Assim, pô, por que que ficou prestando atenção em tanto detalhe, cria fixture e faz um negocinho certinho que vai pra cá, que cria um cliente, saca? Olha como é criar aqui, né, um... um Tudu aqui.

**[00:38:18]** Basicamente a gente não tem que fazer nada, estão me ligando aqui, desligar meu telefone. Então a gente tem, basicamente aqui ó, o client e o token, beleza. O client já tá cadastrado na aplicação e tudo mais, fez aquele negócio, mentiu pro banco, a gente pega o token, o token já tem o token do usuário que já existe na base de dados, então a gente simplesmente manda o bare token pra autorizar, né, do get current user, a gente vai passar tudo que a gente quer.

**[00:38:55]** o title, o description e o state. E depois a gente verifica se o que voltou tem o mesmo título que a gente enviou, se a descrição que a gente colocou é a mesma que estava lá, se veio o IG e o state, a mesma coisa. Bom, você viu a gente, às vezes a gente reclama desse negócio, fala tipo assim, nossa, é muito difícil escrever os testes, tipo assim, os primeiros levam muito tempo, mas depois as coisas vão se encaixando assim, né? Vamos ver o que que rolou aqui. Então, a task test.

**[00:39:29]** Beleza, vamos precisar formatar, então, task format. Não fiquei quebrando muito a cabeça com isso. Nice, passou. Cadê aqui, ó? Test, create, to do. Lembrando, lembra? A técnica para rodar só ele, a gente dá um minus k aqui, pega o nome, e é isso. Rolou, teste passando, bonitinho. Maravilhoso.

**[00:40:02]** Pô, qual foi o esforço que a gente teve que fazer pra testar depois que a gente passou cinco dias escrevendo, né? Saca, não precisa, não precisa. Então, legal. Funciona, a gente já testou ali, né? Tudo que faz a relação entre as coisas, inserir no banco, o que que rola aqui. Agora, a gente vem pra um momento que é um pouco mais crítico aqui, de dentro desse estado da migração aqui dentro.

**[00:40:33]** Teste passando de primeira, lindo, maravilhoso, né? Agora, eu queria mostrar pra vocês o seguinte. Como é que a gente relaciona, né? A gente tem a relação, né? De que todo o Tudu tem um user. Só que a gente não sabe, pela tabela de users, quais são os Tudus que ele tem, né? E aí entra uma parada muito legal aqui do SQL Alchemy. Que é o seguinte, eu vou falar que a gente tem esse campo Tudus. Aí esse Tudus, ele vai mapear...

**[00:41:06]** para uma lista de do Tudu. Aí isso aqui tem que ser exatamente uma string. Porque como isso aqui está definido antes, né? Saca, isso aqui está definido depois, né? O Tudu só existe aqui, então a gente pode colocar a string aqui. Algumas pessoas mais avançadinhas vão querer fazer um negócio aqui, que você faz o seguinte, From, Dunder Future, Import, Anotations. Você pode fazer isso aqui também. E aí você tirar esse...

**[00:41:39]** tudo daqui. É uma forma. Aí esse Dunder Future Annotations permite que ele avalie depois as anotações de tipo. Aí você poderia colocar sem string. Aí é contigo que você gostar mais. Eu vou manter assim.

**[00:41:55]** Mas aí você fala, nossa, eu quero usar o Dunder Future. Beleza, pode usar. Tá tudo permitido. A partir do Python 3.14, que é a versão que sai esse ano, em 2025, não vai precisar mais dessas strings malucas aqui nem do Dunder Future, então vai ficar maravilhoso. Então, o que que eu quero aqui, né? Então, a gente vai precisar criar uma relação aqui, então a gente vai chamar isso de relationship.

**[00:42:22]** E aí esse relationship, ele vem aqui do ORM aqui, ó. Eu tô na frente, pera aí. Aqui, a gente vai chamar essa coisa importada do ORM. Então, fromsqlalc.orm import relationship. E aí, aqui, a coisa começa a ficar meio maluca. Como é que eu tenho que relacionar essas duas coisas aqui? Então, o que é que tá relacionado, né?

**[00:42:52]** Esse campo, ele precisa ser iniciado? Não, né? Eu não quero que quando eu montar o modelo, eu tenha que passar quais são os users aqui dentro, né? Saca, não faz muito sentido aqui dentro. E aí, tem esse outro rolezinho aqui que é o Cascade. Aí, eu vou parar pra gente entender o que que acontece aqui. Beleza. Init Fals, a gente já viu? Quando a gente iniciar, né?

**[00:43:23]** Quando a gente estanciar esse objeto, a gente não quer que seja passado tudo, não faz sentido. A gente vai passar esse cascade aqui. Cascade é tipo de cascata, sabe? De uma coisa amarrada na outra. E o que eu estou dizendo aqui? Nesse delete orphan aqui e all. Vamos tentar entender. Eu quero que todos os...

**[00:43:50]** TUDUS, de um determinado user, sejam deletados quando ele for deletado. Faz sentido isso aqui? Então, beleza, o user que está na nossa base de dados tem, sei lá, 50... 50 pessoas, 50 TUDUS aqui dentro. Então, quando eu deletar ele, eu não quero que tenha coisas órfãos, né? Ou seja, tarefas na tabela de TUDUS aqui que não tenham um usuário real na base de dados.

**[00:44:21]** Então a gente vai deletar tudo e os Orphans. Saca, então não vai ter nenhuma coisa, sei lá, o user do ID 1 foi deletado, então todas as tarefas dele vão ser também. E aí vocês me explicam, aí vocês sacaram, fez sentido isso que eu estou falando, porque sim, é importante, senão a gente fica aqui e explica mais esse conceito, eu sei que é um pouco mais complicado mesmo.

**[00:44:48]** É o Jordani mandou aqui. O iniciente que não consegue fazer 100% de uma primeira vez terá que fazer várias migrations, como deixa uma bagunça de migrations. Ao longo do tempo, todos os erros ficam lá sujando das migrations. Não necessariamente, mano, não necessariamente. Porque a migração, ela é o versionamento do banco em relação à aplicação, né? Se você, sei lá, você fez uma tabela que ficou meio tronche, você vai ter que deletar hoje.

**[00:45:15]** Se você precisa voltar a aplicação do jeito que ela estava ontem, sei lá, você precisa voltar na migração de ontem, sei lá, a versão da aplicação de ontem precisa daquela migração meio esquisita, né? Que a gente tinha antes. Então, não é que fica sujo, a migração não é para ser limpa, a migração é para representar o estado do banco de dados em relação à aplicação naquele comit específico.

**[00:45:42]** A gente tá versionando como as tabelas do banco vão ser naquele momento da aplicação. Faz sentido isso, Jordan? Pra limpar o banco, né? Apagar os órfãos. Exatamente isso. Aí tu fazes uma pergunta, esse spring boot, cara, não, é um curso de fast API de Python, não tem muita relação com isso. E aí, tem um outro ponto aqui que a gente precisa ver, que é o lazy. E eu vou colocar o select in, que é o seguinte.

**[00:46:14]** Todas as vezes que eu buscar um user no banco de dados, aí ele tá aqui como lazy, que é preguiçoso, ele não vai carregar essa coisa. Só que aí eu tô passando um select IN aqui. E o que o select IN quer dizer aqui? Quer dizer que toda vez que eu puxar o user, fizer selecionar ele no banco de dados, ou seja, select, sei lá, na tabela de users, onde o user tem um ID 5, ele vai me trazer todas...

**[00:46:43]** As tasks que essa pessoa fez, todos os to-dos que ela tem para serem resolvidos ali. E eles vão ser recebidos numa lista. E é uma lista de to-dos. Ou seja, se eu tiver um user que tem 15 to-dos, quando eu chamar esse user a gente vai trazer ele para a frente. Você pode mudar esse modo, existem várias outras coisas, sei lá. Eu só quero que for quando for no join e tudo mais, para um fim didático que a gente vai fazer aqui, eu vou usar o select in.

**[00:47:14]** Mas existem várias outras formas e vocês podem procurá-la no doc.esquelial.com Isso aqui dá assuntos, sei lá, por uns 5 dias conversando. Então essa é a ideia aqui do relacionamento. Está vendo que isso aqui agora está relacionado com a tabela de baixo? Vou rodar os testes porque eu quero mostrar uma coisa para vocês agora. Um dos nossos testes falhou. E qual teste em específico? É o teste do Create User.

**[00:47:54]** lá no teste DB. Lembra que eu falei que toda vez que a gente selecionar... Opa, é no teste DB aqui. Lembra que eu falei que toda vez que a gente selecionar um user, ele vai trazer uma lista com todos os Tudus que ele tem? Então eu vou precisar passar esse campo aqui. Tudu, uma lista vazia. Ele não tem nenhum Tudu amarrado a ele. Mas foi essa a diferença que deu aqui, ó.

**[00:48:28]** A left contains one more, que é o ToDoos, a coisinha aqui. Se a gente for olhar a diferença, ele veio com todos os dados, mas esse dado do Selecting não está aqui. Como a gente está fazendo um Select Simples, se esse modelo fosse jointed, olha o que vai acontecer aqui. Também quebra. Mas antes que alguém pense, tipo assim, pô, vai ficar diferente e tal.

**[00:48:59]** Aí o Resident falou, eu poderia fazer esse Select posteriormente? Tipo assim, fazer fora do user? Sim, você poderia fazer. E aí é por isso que eu falei, mano, vai dar uma olhada nos tipos de Lazy, porque são muitos aqui. Você tem, por exemplo, no load, que não carregam os...

**[00:49:20]** os relationships você tem o subquery que faz uma subquery para pegar isso você tem o immediate que traz junto na hora não só no select quando você chama o user ele já carrega tudo então tem tem várias formas de fazer esse relacionamento eu não quero entrar muito em detalhes nisso aqui mas você poderia falar no load não traz saca então aí aqui é uma relação em como você vai querer lidar com isso aqui no construtor aqui desse

**[00:49:49]** desse objeto, de modelo aqui. Eu vou usar o Select In, porque eu acho que é o mais simples aqui no momento, mas vale dar uma olhada na documentação e entender qual vai ser melhor para a sua regra de negócio, para o momento da coisa que você está usando, né? Fez sentido isso aqui, aí rodei os testes, ele falhou, a gente arruma com colocando, né, o tio 2 aqui.

**[00:50:12]** E aí, se tivesse um Tudu aqui, a gente teria que preencher ele nesse teste. Mas esse teste específico não tem. Recomendo que vocês façam isso. Criam um Tudu aqui também e vejam o que rola. Saca. Para brincar, para ver o que acontece. Se não, a gente não acaba nunca isso aqui. Beleza. A gente vai agora para o Endpoint de Get.

**[00:50:47]** Que é a parte que a gente não fez ainda, né? A gente fez o create, agora a gente precisa fazer o read. Porque o join-ed mudou pra chudu. Não, é a mesma coisa. É a mesma resposta que deu. Tanto no join... Ah, porque o join-ed fez isso? Então, é o negócio de entender como funciona esse relacionamento lazy. Eu acho que se a gente ficar aqui, a gente vai ficar tipo, muito tempo.

**[00:51:12]** Saca, o join é de melhor, o select causa erro de N mais 1, então tem várias complicações aqui, várias diferenças que a gente vai ter que pensar nisso. E aqui o select causa erro de N mais 1, mas a gente está usando o select IN e não o select. Massa? Então o select IN é diferente de select. Massa? Tem que dar uma olhada nisso aqui. Galera, eu preciso muito...

**[00:51:40]** Tussi aqui, pera, é só um segundo aqui, que eu acho que eu vou ter que ir no banheiro, açoar o nariz, um, um segundinho aqui. Perdão por isso. Perdão aqui pela saída aqui, eu ainda estou meio doente, hein, então estou tussindo, tá saindo muito catarro aqui, então, perdão por isso. Beleza? Ah, não só pra que vai usar, mas onde, do como, então, é, é, é muita coisa, depende da sua regra específica de negócio, do que vai influenciar nessa coisa que você quer fazer exatamente, então...

**[00:54:07]** É de ocasião para ocasião o modo lazy aqui. Beleza, então vamos lá. Agora a gente vai fazer o get. E o get, eu quero que a gente possa fazer uma query string mais elaborada. A gente trabalhou com as query strings lá no user, só que a query string só tinha limit e offset. Então você poderia trazer 1 ou poderia trazer n.

**[00:54:32]** e a ideia aqui é que eu quero que a gente consiga filtrar por tudo né então beleza eu quero todos os títulos eu quero todas as descrições eu quero sei lá saca então eu quero todos os títulos que contém xpto eu quero todos os descrições que contém sei lá dormir saca então a ideia é que a gente possa mexer nisso aqui aí vocês lembram que na outra aula a gente tinha criado um filtro né aqui nos esquemas né a gente já tinha criado esse filtro né

**[00:55:02]** Então, a gente vai se basear nele, porque a gente também vai querer o limit e o offset, só que a gente vai, além de paginar, a gente vai poder pegar mais características. A gente tem um monte de opções aqui, né? Então, eu vou trazer para cá, só para a gente não ter que ficar escrevendo, e aí eu vou explicando. Olha que interessante aqui. Então, a gente está falando, olha.

**[00:55:30]** Que lá no filtro, no Endpoint, quando a gente mandar com aquele string, a gente pode mandar e elas são opcionais, né? Então é uma string ou none, uma string ou none, um to do ou none, ou seja, a gente vai passar só o que a gente quer filtrar, ou seja, todos são opcionais. Então a gente quer o título, a gente quer a descrição, a gente quer o estado, a gente vai poder limitar, falar, eu quero todas que o título contém, sei lá, batata.

**[00:55:59]** Mas limita para mim em 5, saca? Então a gente consegue manipular tudo isso aqui junto na mesma querestrinha, né? Então a gente vai emitindo aqueles pontos de interrogação e vai colocando um monte de coisinha que a gente quiser aqui. Aqui também tem uma coisa do Field, né? Que eu vou me antecipar aqui. Eu tenho certeza que alguém vai perguntar. Bom, mas e se eu quiser limitar que o título tenha, sei lá, só a partir de 3 caracteres?

**[00:56:28]** Porque quando você faz aquele campo de busca na front, você não quer ficar a pessoa digite A e ele busca no banco. A digita A, B, aí busca no banco de novo. A, B, C busca no banco de novo. Então a gente pode fazer uma limitação aqui. A gente pode começar com uma propriedade. E aí você pode passar o seguinte aqui. Você pode falar um field igual a gente tinha feito, onde o default é nana.

**[00:56:51]** De novo, se quiser deixar explícito, ficar foi mais fácil. E a gente pode passar uma propriedade aqui, que é o MinLength. Aí você pode falar, olha, o mínimo que eu quero para uma descrição de título é 3. E aí para a pessoa também não meter tudo no description, você pode falar, eu quero o máximo aqui, o MaxLength. Ah, sei lá, qual que é o máximo que eu quero? O máximo é ser 20.

**[00:57:21]** Para também, porque tem problema, né? O RL também não suporta um tamanho infinito. Aí você pode trabalhar isso da maneira que você quiser. Isso aqui não está nos slides, não está no texto, tá? Porque a gente começou a discutir essa coisa de Field. E aí, se alguém quiser abrir a eixo e falar, olha, coloca lá o Minho Max Lenf nesse campo, pode abrir uma eixo lá no Field, no... no... no... no repositorio. Quebrou porque ficou Tudu e Tuduz.

**[00:57:55]** O que que quebrou exatamente? Não tem nada quebrado, tá tudo funcionando aqui. Massa fez sentido esse esquema aqui? Então, é tudo opcional. O título, a descrição, o estado, o offset e o limit, eles vão sempre vir, mas eles têm sempre default, valores default aqui, né? Porque a gente tá passando esses valores. Então, vamos voltar lá no todos e vamos começar a criar isso aqui, né? Acho que eu coloquei aqui certinho.

**[00:58:28]** A gente precisa, como a gente vai listar tudo, a gente precisa que o usuário esteja logado, então o curro a gente usa, a gente precisa dar session, porque a gente vai cutucar o banco de dados, e a gente precisa do filtro, com o tipo query, que é aquela coisa que a gente tinha definido na outra aula, que a gente viu mais ou menos como manipular ali. Então, vamos brincar agora. Então, router.get.

**[00:58:59]** E aí o get é barra também, né? Porque é todos. A gente não tem o response model pra isso, a gente vai montar daqui a pouco. Então assim que def, qual que é o nome que eu dei aqui? List todos. E aí a gente vai precisar receber aqueles campinhos, né? Então eu preciso que o user esteja logado, então user é corrente user, accession é accession e a gente vai ter esses filters aqui, né? Eu vou chamar de todofilter.

**[00:59:39]** que aí é do tipo annotated, igual a gente fez quando a gente quer falar que um esquema é o esquema de query string e a gente faz dessa forma aqui. Então aí eu passo o objeto query do fetch API aqui em cima, vamos lá. Fetch API query. Então é do tipo query e a gente vai ter que passar o modelão que a gente quer aqui, do esquema. E aí o esquema que a gente quer aqui é o filter. Chudu. Pronto.

**[01:00:16]** Agora a gente recebe tudo que a gente precisa. Todos os filtros, a sessão e o user que está logado, para a gente saber de quem a gente vai ter que retornar e filtrar essas coisas que a gente está pegando aqui dentro. Massa, vamos ver como é que se manifesta lá na hora de pegar isso aqui, porque a gente tem várias queries strings. Eu acho que é um bom exercício, né? Ver isso lá no Swagger. Vou dar um F5 aqui, a gente vai lá para o To Do's, a gente tem o Get agora.

**[01:00:50]** E olha como ficou legal isso aqui. Aí eu falo, eu quero Offset, Limit, Title, aqui ó, MainLength, 3, Minimum, 0, já ficou tudo anotadinho aqui. O Description e o State. Ficou como um Select. Olha que massa. Então, quando a gente for pedir um User, a gente pode se dar um luxo de chamar várias coisinhas aqui e ir passando tudo. Ah, aqui era 2D, né? Eu deixei errado aqui. Peraí, deixa eu arrumar aqui.

**[01:01:34]** Deus, é isso. Legal, então é assim que fica esse esquema aqui, eu estava respondendo essa mensagem do Jordan aqui. Olha que massa a nossa busca, tem vários detalhes, várias coisinhas que a gente pode ir passando aqui e ver o que acontece. Pô, fica bonito, né? Aquele objeto Queryman, isso aqui é essa junção do esquema.

**[01:02:06]** com o QL, faz tudo ficar bonitinho, tudo encaixadinho no seu lugar, tudo, ó, é fofinho, né? Então, vamos voltar aqui nos slides. Como é que a gente vai fazer isso aqui, né? Agora, a gente vai aprender novos recursos do SQL Alchemy aqui. E eu vou começar ele por aqui, em cima, né? Vamos começar a construir essa brincadeira aqui. Então, a gente vai fazer a mesma coisa que a gente fez, né? Sempre...

**[01:02:40]** Select, tal, tal, tal, então tem que importar o Select do SQL Alchemy, então From SQL Alchemy Import. Select, para a gente poder fazer essa busca. Olha que doido isso aqui. A gente vai começar a criar uma query aqui. Só que essa query ela tem vários condicionais aqui. Então a gente vai selecionar lá no Tudu.

**[01:03:05]** No Tudu, não é no user, tá vendo? Na tabela do Tudu, a gente vai procurar aonde estão os users IDs que correspondem ao user que está logado na aplicação. Aí no final disso aqui, a gente vai executar isso aqui, então await session.scholars.query. Aqui, então a gente vai...

**[01:03:36]** Como é que eu dei o nome aqui? Tudus. Só para ficar com isso aqui. Tudus. E aí, o que acontece? Como todos os parâmetros no filtro são opcionais, aí a gente vai ter que saber o que que veio, o que que deixou de ver, como é que está isso aqui, né? Então, a gente vai ter que ver. Se o Tudu Filter, né? Tem alguma coisa que a gente quer, né? Então, beleza, a gente quer saber se tem título aqui, né? Então, if Tudu Filter tem title.

**[01:04:08]** Se tiver title, a gente vai fazer uma coisa. A gente vai fazer outro if aqui. Alguém vai falar, é um monte de if, poderia virar no seu quê? Tipo assim, mano. Não tão preocupado com limpeza, calisthenia de objetos aqui, a gente quer aprender a usar o QueerString, vai? Então, aí a gente vai perguntar de novo, vai?

**[01:04:42]** State. Então, a gente vai fazer todas essas perguntas aqui. E aí a gente vai concatenando as coisas nessa query que a gente montou aqui. Ou seja, essa query não foi executada porque a gente vai passar mais coisinhas para ela aqui, para a gente ir penteando ela. Então, por exemplo, se tiver o filtro, eu quero que a query adicione mais uma coisa. Ou seja, um filtro na query. Então, Filter.

**[01:05:13]** e a gente vai fazer que tipo de filtro? Então a gente vai usar o Tudu aqui, e a gente vai perguntar se o Tudu, esse objeto Tudu que a gente quer, o campo title dele, o campo title dele, contém o que veio no filtro. E aí a gente sobre escreve a Query aqui. Fez sentido isso aqui? Então a gente está perguntando, a gente está adicionando, então select,

**[01:05:50]** Então seleciona o Tudu onde a gente tem o user marcado aqui, o user ID. Se tiver um título, a gente vai adicionar nessa query um filtro para ver se o título contém o que veio na query string. Massa? Me contem isso, faz sentido. Enquanto eu respondo o murinho aqui, obrigado, mano. O Monster, valeu, mano. Vocês me ajudam demais aqui. Fez sentido? Espero que sim.

**[01:06:30]** A gente vai refazer essa mesma query aqui. Ele vai sobre-escrever, cara, mas ele perde a anterior? Não! A gente está usando ela como base aqui. Então, é essa query mais isso aqui. Não está sobre-escrevendo, tipo assim, de verdade. Está sobre-escrevendo a variável, mas a gente está adicionando mais coisas em cima do que já tinha antes. E bom, aí para o description aqui, a gente vai fazer a mesma coisa.

**[01:07:04]** A gente vai pedir a query, e vai falar o seguinte, olha query, ponto filter, de novo. A gente quer filtrar todo o chudu, ponto description, e saber se ele contém a coisa aqui. Vamos dizer que entendi pra não atrapalhar a aula. Que isso, mano, pode perguntar, o objetivo é esse, a gente tá aqui pra isso. Eu só não respondo as perguntas, tipo assim, que não tem cabimento com a aula, né, mas tudo bem. A gente quer o description, e a gente quer saber...

**[01:07:33]** se veio o campo de descrição aqui. Então, beleza, se mandou título de description, ele sobre escreve a query e vai colocando mais coisas aqui dentro. No final, ele vai criar uma query monstrone, assim, né? Tipo, where to do id, user id, end, filter, tem isso aqui em outra coisa, sabe? Que ele vai montando um monte de coisinhas aqui. E aí, se tiver o state que a gente quer aqui, então, a gente vai sobre escrever a query de novo query.filter.

**[01:08:04]** E a gente vai falar o seguinte, olha, o to do ponto state é igual, igual, aqui não é container, aqui é idêntico, né? Porque são valores possíveis só, né? Então, a gente quer saber se é igual ao to do filter ponto state. Massa? Esse é todo o esquemão desse get aqui, pra gente validar todos aqueles campos. Ah, mas daria pra fazer isso de uma outra forma, tal, que ficaria mais bonito, pô.

**[01:08:34]** É o ifizão aqui pra gente entender o que está acontecendo. Ah, mas tem uma técnica de refatoração, não sei o quê. Não vou entrar nesse mérito aqui agora. Legal? Aí a gente tem essa query aqui embaixo que passou por esse caminho e a gente pode aplicar o limit aqui. Limit. Offset. Que são valores que vêm do base aqui. Que é do esquema. Que é do filter page. Ou seja, tudo isso aqui está aqui também, então vamos lá.

**[01:09:08]** O limit é o todofilter.limit e o offset é o todofilter offset. Massa, interessante isso aqui, né? E aí a gente retorna todos os todos que dão match nesse esquema que a gente quer aqui. Todos, return todos. Olha que massa, então a gente passa um montão de coisas aqui.

**[01:09:44]** Ah, tem título, então um filtro título. Tem inscrição, filtro descrição, tem estado, filtro estado. Tem limit offset, testo limit offset também. E a gente junta tudo aqui. Porque o filter e não o where. Porque o filtro, na minha opinião, ele é mais explícito, né? Eu tô fazendo isso aqui, onde isso aqui? Mas eu poderia usar where também, não tem problema. Aqui, ó, tenta que você for ver o filter. O filter é um where.

**[01:10:21]** Saca? Como eu estou trabalhando com filtros aqui, eu acho mais explícito deixar filtro, mas é a mesma coisa. Nada muda. O filter é um alias para o air. Tento que ele está aqui, ó. Sinônimo de select.air. Massa? É uma questão semântica aqui para mim. Não tem nada demais. Você poderia usar o air se quisesse.

**[01:10:48]** Bom, a gente fez tudo isso aqui, a gente pode testar não porque a gente não tem um response model ainda, né? E a gente precisa de um to-do list, que é uma lista de todos os to-dos. E aí o que a gente vai fazer? Simplesmente pegar uma lista de todos que a gente tem e chamar esse modelinho aqui. Simprão, simprão. Ou seja, vários to-dos publics vão ser retornados quando a gente chamar aquele endpoint ali.

**[01:11:25]** Aí a gente precisa importar aqui para a gente não esquecer, né? Então vamos lá. Aqui onde a gente está com todos os to-dos, a gente vai importar o to-do list. O to-do list é o primeiro, o to-do list. Legal, aí a gente usa ele aqui, o response model. Response model é igual ao to-do list. Pronto, aí agora a gente tem uma resposta de várias coisinhas que a gente tem aqui.

**[01:11:55]** Bom, vocês já devem imaginar uma coisa aqui, né? Com esse tanto de if, com esse tanto de if, na hora de testar, a cobertura vai depender de quê? Descrever vários filtros. Então, vai ter que ter um montão de teste. Yeeey! Nada melhor do que escrever um montão de teste. Então, vocês sabem que eu adoro isso aqui, né?

**[01:12:23]** Então a gente pode, ó, o Harano mandou aqui, filter lembra o Django, mas para esquiar algo lindo possível, eu preciso usar as construções similares do SQL. É, é uma boa também. Então, vamos lá. Vamos começar com Factory Boy, cara. O Huzin amassou aqui, mano. Vamos criar uma Factory, porque com a Factory a gente consegue resolver todos esses problemas. Lindo. Então, vamos lá. Eu vou copiar aqui para a gente ir vendo lá.

**[01:12:54]** Isso aqui, eu vou colocar no teste dos mesmo aqui por enquanto, depois se a gente quiser a gente muda, vai para um lugar, vai para o outro, eu vou colocar isso aqui, para a gente brincar aqui. Olha que massa aqui, como a gente está pensando no teste, o teste sempre usa o primeiro user, eu vou usar um factor que faz o seguinte aqui, eu não importei o factor, então importe factory. Depois a gente muda, é só para a gente estar no mesmo lugar aqui.

**[01:13:29]** Eu vou criar um factor, a gente viu isso na aula passada, que cria um modelo de Tudu, né? Tudu é aqui, deixa eu só arrumar, Feche, API zero, pronto. O Tudu é aquele modelo lá do banco de dados que a gente tinha aqui, né? Então tem ID, TITLE, DESCRIPTION e STATE. E aí eu vou fazer o seguinte aqui, a gente vai usar um recurso que a gente não viu aqui ainda, que é esse Faker.

**[01:13:56]** Então, a gente vai pedir para o título, ele gerar qualquer título. Falou, ó. Escreve aí qualquer groselha. E para o description também. Escreve aí qualquer coisa. Então, cria um texto fake, para o título, um texto fake para a descrição. E no stage, a gente tem esse esquema que se chama Fuzzy. E aí, o Fuzzy Choice é uma forma randômica de escolher um estado. Aí, como eu estou passando esse enum para ele?

**[01:14:31]** Como eu estou jogando esse num para ele aqui, ele vai escolher, randomicamente, um estado possível aqui dentro. Massa. E aí, por padrão, ele sempre usa o User ID 1. A gente vai usar sempre o User ID 1 para testar aqui, para ver o que vai acontecer. Ah, mas eu quero testar o 2, beleza. A gente usa o 2 depois, se for necessário.

**[01:14:59]** Legal, faz sentido que essa factor faz? A gente vai pedir pra ele criar alguma coisa e a partir dessa coisa a gente vai gerar uns textos muito malucos. Vamos ver aqui como é que isso se comporta? Vamos lá. Python, menuzi no modo interativo, testes, a gente tem o teste users. Aí a gente tem aquele to do... To do factoring. To do... Ah não, eu abri no user, é o teste to do... Espera aí. Tenho to do factoring aqui.

**[01:15:32]** Aí olha que doida. Aí ele gera uma coisa pra gente muito maluca aqui, com um texto qualquer aqui. Seems worker-wander... ...to expect time put orders, tá ligado? Tipo assim, qualquer coisa aqui, qualquer groselha. O description também é qualquer groselha. E aí o state aqui é Dan, porque ele pega um estado fuzzy. Se a gente rodar de novo, o state agora é draft. Se a gente rodar de novo, o state agora é draft de novo. Draft...

**[01:16:02]** Trash, tá vendo? É, é um lorem Y mesmo aqui mesmo. Não importa muito. Mas o legal do fake aqui é que a gente pode falar, eu preciso que o título seja title, seja, sei lá, dormir.

**[01:16:19]** Então ele vai criar um QTitle, ou seja, dormir. Então a gente vai criando e a gente pode ir modificando as coisas em tempo de execução. Aí o Rafa perguntou se esse Factor ou Factor no sentido do Goff? Sim. A gente conversou um pouco mais sobre isso. Ser uma aplicação do Factor na aula passada. Mas aí você pode ir. Eu quero que o User ID seja 2, né? Legal. User ID 2. E aí você vai montando aqui, conforme você for precisando. E a grande coisa que a gente tem é o Create.

**[01:16:49]** Batch, né? Aí você fala, pô, eu quero criar cinco desses aqui, né? E aqui começa a brincadeira. Quero cinco desses. Legal. Ele criou cinco, né? Deixa eu... From, Pprint, Import, Pprint aqui. E print aqui. Pprint, disso aqui. Ele gerou uma lista pra gente aqui com cinco. Olha que massa.

**[01:17:16]** Então, ele respeita tudo o que a gente pediu, mas os outros dados, trash, don't do, eles ficam aleatórios, então simplifica para a gente testar. Foi o que a gente conversou na aula passada quando a gente introduziu o Factor Boy aqui. Massa? Então a gente vai gerar textos aleatórios para o título, textos aleatórios para a descrição, um estado randômico para o...

**[01:17:39]** para o state a partir, é randômico a partir dos estados possíveis que a gente colocou no enum e a gente tem o user ID que vai ser sempre 1, porque de preferência a gente vai testar com o user 1, mas se precisar você pode colocar o user ID 2, dependendo do que você quiser fazer aqui. Então a gente vai fazer o primeiro teste dos filtros aqui. Então o que a gente vai fazer aqui? Vou copiar e a gente vai conversando sobre ele.

**[01:18:11]** aqui no arquivo de texto, porque eu acho que é melhor do que lá no slide. Ó, a gente vai fazer o Arrange desse teste, ele é um pouco diferente agora, não? Arrange. Aqui a gente tem o Act e aqui a gente tem o Assert, não? Massa? Então, a gente vai precisar da Session nesse teste, porque a gente vai inserir N registros no banco de dados na fase de Arrange aqui. E a gente vai comitar isso aqui, não?

**[01:18:46]** Aí você está vendo que esse session aqui precisa ser a 5, né? Então é await, commit. Aí esse teste precisa ser a 5, né? A 5, def. Aí a gente tem aquele, pytest.mark.async.io aqui, né? Aquela coisinha que a gente aprendeu nos outros dias, né? Então, ó, eu vou chamar a session. Aí a session vai inserir, né? A gente tem esse book save object.

**[01:19:15]** que é tipo assim, coloca vários objetos na sessão ao mesmo tempo. Massa? Então, insere 5 de uma vez, insere N, insere uma lista de objetos, aí quais objetos a gente vai fazer? A gente vai criar em batch 5 aqui, onde o user ID é o user do user que vem da fixture. O que muda mesmo aqui no teste é só essa parte onde a gente está inserindo dados para a gente poder validar no final do teste.

**[01:19:48]** Aí a gente vai chamar, sem a query aqui, então a gente vai inserir 5 registros e a gente quer que o Tudus, que é lá do esquema, então ele volte o Tudus num tamanho, passando por nenhum filtro aqui, ele vai ter que retornar 5 pra gente, que foi o número de objetos que a gente inseriu aqui dentro. É basicamente isso que esse teste faz, então a gente...

**[01:20:18]** Inseriu 5, deu commit e espera que tudo dê certo aqui embaixo. Massa, faltou importar o pai teste aqui. Aí isso tudo fica pra cima, isso aqui ganhou espaço. Vamos rodar o teste pra ver o que acontece? Então eu vou rodar com o "-k", pra gente poder dar só esse e ver o que que tá rolando. Então eu vou rodar com o próprio pai teste, inclusive, "-k".

**[01:21:00]** Assim que se acham, não hazard book save objects. Hum, tem um erro no meu slide? Book. Ok, legal. A gente pegando erros em tempo de execução. Aqui, é edit all. Tem um erro no slide. No assim que é edit all e não book insert. Legal. Fica até mais simples de ler o código agora. Então, a gente vai adicionar a todos. Todos os cinco e vamos ver o que que rola aqui.

**[01:21:38]** Legal. Eu errei no retorno agora. Ok, legal. Agora começa a ficar interessante as coisas.

**[01:21:49]** Fecha API Exception Response Validation Error, né? Ele tá falando que o response precisaria ser um to-dos e a gente tá retornando um escalar result, né? Eu esqueci de pegar o all aqui, né? De todos. Olha como escrever teste é uma delícia. Pronto. Agora a gente tá retornando todo mundo que precisa ser retornado aqui em formato de user e não no formato escalar aqui, né? Uuuuh! Massa, agora deu um erro muito legal, ele tá falando, olha.

**[01:22:21]** Acho que vai ser removido esse book save object. Pô, legal. Obrigado pela informação, David. Aí o que ele falou, olha. Model attribute types, lock, response, message, input should be a valid dictionary, or a object to extract fields from. Ou seja, lembra que a gente já caiu nesse erro?

**[01:22:44]** algumas aulas atrás que a gente precisa que os modelos do SQLA Alchemy sejam convertidos nos modelos de resposta que a gente tinha aqui eu preciso que o Tudu Public eu preciso converter isso aqui nesse modelo que a gente tem aqui dentro porque o que que está acontecendo aqui aqui esse O

**[01:23:13]** que ele está retornando para mim aqui, embora sejam todos os chudus, eles estão em um formato meio esquisito, né? Eu deixei isso aqui no texto em algum lugar, aqui, ó. Isso aqui, ó. Precisa ser chudus, né? Isso aconteceu no outro, no outro get, que a gente está fazendo outra vez. Pronto, agora sim, é um chudu com uma lista de todos os chudus. Vamo de novo. Passou. E aí?

**[01:23:50]** Agora retornou 5, né? Se a gente for brincar aqui, né, vamos ver lá no nosso teste, vamos botar o breakpoint aqui e ver o que que ele está retornando nesse response. Então eu dei esse teste, a gente caiu no debugger, né? LL a gente vê onde está, a gente tem o objeto response aqui, né? Response.json. Aí ele trouxe várias coisas, ele trouxe um to-do com uma lista de vários objetos que a gente inseriu aqui.

**[01:24:22]** Aqui ó, o user tem id2 aqui. E ele foi trazendo todo mundo. Pra gente ver isso bonito, pp. Legal, ó, agora foi, agora tá bonito. To doz, ó, tem o primeiro que tem o description, que é um testão. Ele tem o id1, stage trash, um título. Aí a gente vai pro segundo. Description, id2, aqui era o 1.

**[01:24:47]** e ele inseriu tudo de forma sequencial aqui, aí de 4, aí de 5, e veio todo mundo, ou seja, vieram 5, se a gente pedir o length aqui, vieram 5. Ah, pera, length response jason, to dos, né, aqui. Então vieram 5, exatamente a mesma quantidade que a gente tinha inserido aqui, ou seja, o listar está funcionando. Legal? Entendemos esse teste aqui?

**[01:25:17]** Ele é meio obscuro, tem vários recursos a mais aqui, mas ele funciona direitinho. E aqui a gente tá mandando sem query nenhuma. Ou seja, se a gente rodar todos os testes agora e olhar o coverage, vamos ver o que acontece. Task test. Task format. Task... Beleza.

**[01:25:45]** aqui em algum lugar aqui ó no filter aqui deu uma linha maior do que deveria aqui no te do filter description então vamos pegar aqui aqui ele deu 80 caracteres aqui então vamos quebrar aqui legal vamos rodar de novo format beleza tudo formatado vamos testar e ver a cobertura agora então para abrir a cobertura você pode abrir com a pessoa normal ou ser maluco igual eu e abrir o browser por index.html

**[01:26:22]** Legal, legal, legal, vamos ver aqui o teste Tuduz, é o Tuduz, né? Ó, a gente testou, a gente passou por aqui, só que a gente não entrou em nenhum filtro, né? Então, a gente precisa testar os títulos, a gente precisa testar a descrição e a gente precisa testar o estado. São coisas que estão separadas aqui, né? E a gente vai precisar fazer um testinho pra cada coisa, pra garantir que tudo isso aqui tá funcionando da maneira como deveria funcionar.

**[01:26:53]** Então tem um teste que a gente pode usar o Offset Limit aqui para a gente fazer, né? Aqui, ó, vamos lá. Eu vou copiando aqui e a gente vai colocando lá nos testes e vai discutindo o que cada teste está fazendo aqui. Beleza, aqui não é mais Bulk, né? É Edge All. E aí, aqui, vira a Sink.

**[01:27:24]** Def, arroba, pai teste, ponto marque, ponto assim. Legal? Para comitar, a gente precisa dar um await aqui dentro. Mas o que a gente vai validar aqui nesse teste em específico? A gente vai inserir cinco todos aqui. Só que aí eu vou chamar a query string aqui. Deixa eu copiar essa query string para fora aqui, para a gente discutir ela.

**[01:28:00]** E ela é o seguinte, a gente vai falar que a gente quer começar do 1 e trazer 2, ou seja, a gente está limitando a query em 2 users aqui, 2 to 2 na real. Então, a gente quer 2 to 2, então é esperado que a gente volte 2 quando a gente testar com essa paginação aqui, né? A gente pagina com 2 e espera que venham só 2 na resposta e não 5, que foi o número que a gente inseriu.

**[01:28:30]** Então, basicamente o que a gente está exercitando aqui é a QueerString. Vamos rodar, ver o que acontece. A TaskFormat ficou alguma lixinho ali do que eu estava colocando. Beleza, passou esse teste aqui, que é o Tuduz aqui. Deve retornar dois. Só que se a gente for olhar aqui na cobertura, você vai ver que nada mudou, né?

**[01:28:57]** Porque o Limit e o Offset são sempre chamados, né? Porque eles sempre vêm, né? Então a gente colocou eles aqui dentro. Legal, testamos mais uma coisa, mas não garantiu nada, né? Não mudou nada no nosso coverage. Então, vamos começar a brincar agora. Agora, a gente vai inserir 5. De novo, aquela mesma coisinha que a gente tinha feito antes. A gente vai inserir 5. Só que aí, agora, a gente vai dar um título aqui, ó.

**[01:29:30]** Aí a gente tem o teste to do um e a gente procura aqui no título. O título tem teste to do um. Se tiver teste do um, ele vai retornar todos que vieram aqui dentro. A ideia é essa. Não tem nada de muito diferente. A gente só está exercitando o... Então aqui ó, a gente só está exercitando o filtro. Então é de on, a wait, a sync.

**[01:30:03]** Arroba pra ir teste, ponto, marque, ponto, assim, que aí eu. E basicamente o que a gente vai fazer é isso. Aí você pode falar, eu quero testar só um pedaço, né? Porque a gente contém, né? Poderia ser só teste aqui, não precisaria dar full matte. Igualzinho. Então, a gente inseriu 5, tem que voltar 5. A gente poderia repetir essa ação aqui? Pra fazer um teste mais elaborado, se vocês quisessem, a gente poderia colocar esse, é de all aqui?

**[01:30:32]** e colocar um outro EDOL aqui sem esse title, ou seja, tem 10 no banco de dados agora. Só que só vai voltar a 5, porque só 5 tem o título teste do. Aí você vai falar, pô, pode acontecer num momento em que aquele texto vem um texto exatamente teste do que vai falhar o teste, caraca. Não contaria com isso. Legal? Então a gente está inserindo 10 e procurando por 5 aqui dentro. Vamos ver o que rola? Task test.

**[01:31:06]** Passou. Lindo, incrível. Em teoria agora, nossa cobertura tem que ter passado pelo title. Então pela linha 48, vamos ver. E aí, testamos a linha 48. Agora ela está testada. Aqui. Agora a gente precisa fazer um filtro de description. E aí é a mesma coisa, a gente vai repetindo teste, brincando. Você pode falar, eu queria combinar um teste que testasse todos os filtros, também poderia fazer.

**[01:31:38]** Aí é contigo, do que você acha mais legal de fazer aqui. Aí a gente tem esse filtro por description. Então eu chamei a description de description, e a gente procura só um pedaço aqui, eu falei que a gente poderia ter feito dessa forma. Aqui, então ele vai testar se a descrição retorna 5, que são só os 5 que tem desque, né? Então assim que def, vamos lá. Arroba, pie-test, ponto-marque, ponto-async-ion.

**[01:32:14]** edge on await. Então, todas as coisas, a gente vai inserir cinco coisas em que o título chama description e a gente vai ver se a description começa com desking. Essa parte dos testes está encaminhado, é legal de fazer sim, né? Mas é aquela coisa que eu tinha falado lá no começo, né? Tipo assim, a gente passou um tempão construindo essa estrutura, né?

**[01:32:47]** Depois que a gente constrói toda a base as coisas ficam fáceis de testar depois, né? O problema é que geralmente a gente escreve um monte de código sem teste ou não pensa bem na arquitetura dos testes, aí depois a gente vai tentar testar e aí tem que construir toda vez uma arquitetura diferente para poder rodar o teste, né, que a gente quer rodar. Então isso aqui é o resultado de muito trabalho que a gente fez nos alunos passados. E aí passou.

**[01:33:16]** 5 to 2, 5 to 2. Vamos ver aqui? Testamos esse filtro aqui, então essa linha também está testada, essa expressão. E aí agora a gente precisa de um teste para o state. Nada mais justo, né? E vai ser exatamente a mesma coisa. A gente vai passar um state aqui. Pronto, então vamos falar, ó, um state de draft.

**[01:33:43]** A gente vai inserir 5 em draft e vai procurar pelo estado draft. Se tiver 5 com estado draft, a gente fez o que precisava pra passar também aqui. Pô, legal, né? Basicamente são testes muito parecidos, né? Existe uma forma de melhorar isso aqui drástica. Mas aí é de novo aquele negócio. Ah, vamos refatorar quando der tempo. Arrouba, pai teste, ponto marque, ponto assim que ai eu.

**[01:34:21]** Legal? Então estamos procurando por draft, vamos ver quem está em draft, se todo mundo que tiver aqui o 5 estiver em draft. Nice, funcionou o que a gente queria. Task test. Legal. Mais um para conta aqui, o que significa que a gente conseguiu cobrir tudo o que a gente se propôs a cobrir aqui. Wow, legal. Endpoint lindo, maravilhoso, testado, né? Todos os filtros 100% de cobertura desse endpoint.

**[01:34:54]** Então a gente pode partir para um outro mundo, um outro lugar, que é o delite. E o delite, ele é bem simplão de fazer, né? Tipo assim, ele não tem muita, muita firula, né? A gente vai... O backlog só cresce, assim, né? Infinito, né? Se o backlog não tiver mais tarefas do que já foram entregues um dia, não faz sentido.

**[01:35:26]** Então ó, como é que a gente vai implementar o delete? O delete se implão. A gente pega por id do choodoo, chama, vê se o choodoo user id é o desse id que a gente pediu, vê qual id do choodoo e manda pra frente. Não precisa validar o user id aqui. Ops, dev do técnico, é muito massa, é isso mesmo. Não precisa validar isso aqui, coloquei por um certo preciosismo aqui, mas não precisa.

**[01:36:01]** Aí, se não tiver o Tudu ID que a gente está procurando, a gente vai dar um status code not found, porque ele não existe. Então, vai dar 404. Se tiver, então, a gente delita, deleta, né? Delita é ótimo. A gente comita e responde, ó, test que foi deletada, né? Massa, é isso. Delite simplão. Aí, a gente não tem isso aqui. Aqui é um await, né? Aí, não precisa do commit.

**[01:36:42]** Diferente, né? Delita, né? É muito bom, né? Mistura, português com inglês, é maravilhoso. Então, a gente vai deletar esse user daqui, a gente pode dar um commit, né? Se você quiser, await.comit, afirma que não está funcionando, a gente precisa...

**[01:37:04]** importar, a gente comete um delito, né? Muito bom, muito bom. Aí a gente aqui do Fast API, a gente vai trazer o HTTP exception, pra gente poder levantar, né? Essa exceção. E pra gente falar os status, né? A gente vai importar o HTTP status lá do Python, né? Então, from HTTP import HTTP status.

**[01:37:30]** E vai retornar 404 se não tiver. E aí ele tem esse message aqui. Lembra que aquele nosso esquema genérico foi o primeiro que a gente fez lá no curso? A gente precisa importar ele aqui também. O que a gente quer aqui? Então aqui nos esquemas, esquemas eu vou importar o message aqui também. E aí o message é depois do filter. Message.

**[01:38:00]** Legal, aí o David falou, pra ver se não precisa mesmo do user de bora fazer um teste. Exatamente, né? É muito bom, eu adoro isso. Legal, pô, não tem nada de muito mágico aqui nesse teste, né? A gente tem o ID que a gente vai receber dinâmico, a session, o current user, vamos fazer uma busca no banco, e aqui precisa de um await, chamar o escalar aqui, a gente vai fazer um await.

**[01:38:28]** Se voltar voltou, se não voltar não voltou, vamos ver o que acontece. Então, como é que a gente vai saber se isso é o que funciona? Escrevendo um teste. Por quê? Porque sim. Porque sim. Eu vou fazer o do erro primeiro, vai? Porque eu acho que é mais fácil. Então, aqui, a gente vai testar um Tudu que não existe, que eu não sei porque eu deixei essa F string aqui. Bizarra. Aqui eu vou precisar do HTTP status também. Então, vamos lá.

**[01:39:05]** from http import http status. Legal, ó, vamos fazer o seguinte, a gente vai chamar o client, vai passar o token e vai mandar deletar um todo que é o todo 10. E não existe o todo 10. Por que não existe? Porque a gente não inseriu ele. Então esse teste tem que falhar, tem que dar not found 404. O que você quer deletar não tem não, mano. E aí retorna esse task not found aqui.

**[01:39:40]** Vamos ver. Task Format. Task Test. Foi, foi, foi, foi. Passou. Aqui é o Tudu. List Tudu, só que é o Delete Tudu Error. Ou seja, o 404 está funcionando. Vamos ver o que que rola aqui. F5. Legal. A gente caiu nesse exception aqui, né? Mas a gente não conseguiu fazer o delete, né? Porque a gente não inseriu ninguém.

**[01:40:12]** E aí, como a gente fez essa brincadeira de inserir várias factors e tudo mais, eu vou fazer um pouco diferente, né? Eu não vou criar uma fixture pra isso aqui, mas a gente vai chamar... Opa, peraí, eu coloquei no lugar errado. Eu coloquei o teste no arquivo de Tudus, não estou viajando aqui. É no teste Tudus.

**[01:40:49]** Olha como esse teste é diferente do que a gente tinha feito, né? A gente não vai criar um to-do base pra ficar fazendo esse tipo de coisa. Então, aqui no Arrange, olha o que a gente vai chamar. A gente vai chamar a Factor e vai passar, olha, o User Ideal User, que tá registrado no banco, que é de quem a gente tem o Tolkien. A gente vai adicionar isso aqui, então, adicionar na sessão. Await. Espera pra ver o que vai acontecer. Arroba, pai teste, ponto marque, ponto assim, que é eu. Legal.

**[01:41:23]** Basicão, né? Então a gente adiciona, na sessão faz o commit, então isso vai estar lá para quando a gente chamar o Tudu, a gente tem a relação do Tudu ID, que a gente definiu aqui. E aí se tudo der certo, ele deleta. Vamos ver o que rola? Então task test, task format. Aí aqui ele quebrou o tamanho da linha, então a gente dá um enter aqui, legal. Task format, rodou, lindo, liso, maravilhoso.

**[01:41:58]** Rodou a formatação, vamos testar e ver a cobertura agora. Ó, o teste passou, né? Aqui é o teste delete to do. Não é com erro, é o to do mesmo. E a gente passou. Tudo tá coberto aqui. Aí ficou aquela pergunta que o David falou, né? Pra ver se não precisa de user ID, bora fazer um teste. Vamos deletar ele daqui e ver se não precisa dele aqui, se é preciosismo isso aqui. Legal. Tiramos daqui. Vamos rodar de novo? Task test.

**[01:42:34]** Yay! Não precisa mesmo. Coloquei aqui só para especificar, né? Ó, a gente está buscando desse user. Mas não precisa, né? Porque como o ID de toda a tarefa é único aqui, não faz muita diferença. O fato dele estar aqui ou não. É só mais um... Preciosismo aqui, não. Mas não precisa. Não. Literalmente não precisa. E esse commit aqui também não precisa. Pode rodar sem ele.

**[01:43:01]** É porque a gente sempre dá commit no final das coisas, mas também não precisam. Roda lindo, maravilhoso, cremosinho, dive 5, 100% testado no nosso delete. E se o ID for de outro usuário? Então, essa é a questão. A gente pode deletar o ID de outro usuário? Vamos fazer esse teste? Vamos fazer esse teste? Vamos lá. Aqui, ó.

**[01:43:37]** Esse teste também não tem aqui, tipo assim, estamos fazendo de cabeça aqui. Direct order user to do. Nossa, então a gente vai deletar de outro usuário. Aí, como a gente já tem essa fixture pronta, porque a gente é lindo e maravilhoso, eu vou chamar o order user aqui. User. Massa. Aí a gente vai criar um to do. To do user. To do order user. Massa.

**[01:44:18]** E a gente vai adicionar, é de all aqui, né, vai? A gente já aprendeu é de all, então a gente vai adicionar os dois chudo aqui. O chudo user e o chudo do order user. E a gente vai tentar deletar o chudo do order user. Vamos ver o que rola? Aqui é o order user id. E aqui é o chudo id do order user.

**[01:44:50]** A gente não precisa do nosso próprio Tudu aqui, né? A gente pode usar o Dora User sempre, né? Nem precisava desse aqui. Edge. E a gente não precisa do User aqui também. Legal. Vamos tentar deletar o de outro usuário e ver o que acontece? Task test. Não conseguimos remover. Deu 404. Por quê? Porque a gente tá...

**[01:45:24]** verificando o user ID. Se a gente não verificar o user ID, o teste passa. Olha que loucura. Então, a gente consegue alertar o chudo do coleguinha e a gente não quer isso. Então, a gente deixa isso aqui e isso vai voltar ao Not Found. Porque eu não tenho a task que você quer aqui. Olha que bonito! E qual que é o task do Not Found? Qual que é a resposta do Not Found? É Detail Task Not Found.

**[01:46:04]** Legal, vamos rodar o teste de novo? Passou. Lindo, e tá com aqui com os dois. Se eu tirar isso aqui, olha que massa, o teste quebra, porque ele não vai dar not found, deu 200. Ó que bonitinho, testes de improviso aqui. Fez sentido isso aqui que a gente testou? A gente tá deletando de outro usuário e tentando pegar pra ver o que acontece? Às vezes o caso é ter um ID master e um ID que indica por usuário.

**[01:46:52]** Às vezes, o caso é ter um ID Master e um ID que inicia por usuário. Daria para fazer? Daria para fazer. Não acho que precise disso. A gente usa um relacionamento. Esse dado já está na tabela porque não usaram. Para que criar outra coisa? Então, olha que bonitinho esse outro teste. Diferente, não? Diferente do que a gente fez aqui. E a gente garante a mesma cobertura que a gente tinha antes. Bom, só faltou alguém.

**[01:47:24]** alteração desse recurso. E aí, geralmente, a gente está usando PUT no user, e agora a gente vai usar PET, porque PET é legal, vai diferente do PUT. Lembra que o PUT, toda vez que a gente precisava fazer uma alteração usando o verbo PUT, a gente tinha que enviar todos os dados?

**[01:47:47]** Ah, se eu queria mudar o e-mail, eu tinha que mandar o e-mail, a senha, o username, eu tinha que mandar tudo, todas as vezes. Todo o update tinha que enviar todos os dados. O legal do patch é que o patch carrega menos informação. E aí, tudo é opcional. Olha que massa. Pode ser title, pode ser description, pode ser state, tudo é opcional.

**[01:48:14]** Eu posso mandar ou não um título, eu posso mandar ou não uma descrição, eu posso mandar ou não um state. Aí você vai falar, pô, esse esquema é muito parecido com o esquema que a gente já tinha aqui, né? Que é esse aqui, ó, do, do filter to do. É muito parecido, né? É basicamente a mesma coisa, né? Tirando esse field aqui que a gente colocou, são os mesmos campos colocados da mesma forma, só que o, só que o filter erda dos filtros, né?

**[01:48:52]** E esse aqui é um Tudu mesmo. Esse é o filtro do Tudu, que erda de filtro, tem características de filtro, se comporta como um filtro. E esse aqui é um novo esquema de base aqui. Então todas as coisas são opcionais aqui. Massa? E aí a gente pode mandar só um pedaço da informação que a gente quer atualizar sem mandar informação toda. E como é que a gente vai fazer isso? Bem simples e bonitinho aqui também. Eu vou copiar a primeira parte.

**[01:49:25]** para a gente discutindo sobre ela, e depois eu copiou a segunda e a gente vê o que que rola aqui. Então, ó, o que que está rolando aqui nesse patch? A gente está mandando um Tudu ID, o identificador do Tudu, que é o inteiro, que é o Tudu que a gente quer atualizar, a gente depende da Session, a gente tem o User e a gente depende daquele modelo lá que é o Tudu Update, que a gente não trouxe para cá, então a gente precisa importar ele lá.

**[01:49:56]** Então, to do update. É no que a gente não tinha, eu já vou dar um passo que forma aqui, para ele arrumar na ordem alfabética ali. Legal. Então, a gente vai usar esse to do update. E aí, o que a gente vai fazer? Aquela mesma busca que a gente tinha aqui no delete, né? Ou seja, procura quem é o user ID e quem é o to do ID. E aí, por que a gente está passando isso aqui? Para eu não modificar o da Julia Pix, que está aqui no chat, né? Tipo assim.

**[01:50:26]** Então, eu não posso modificar o Tudu, que não é o meu. E aí a gente vai fazer esse game. Se não tiver o Tudu que a gente quer modificar, vai dar 404. Mas, legal? Eu vou escrever o teste do erro já, para a gente já validar essa parte aqui. Esse começo. E depois a gente implementa o resto, porque a gente vai fazendo conforme faz sentido aqui. Ó, eu vou fazer um teste que...

**[01:51:05]** A gente tem o client, a gente tem o Tolkien, a gente vai tentar fazer um patch, a gente não vai mandar dado nenhum aqui. A gente vai pegar um chudu aleatório, que é esse 10, e vai tentar alterar ele. Ele não existe, né? E o fato dele não existir vai fazer com que ele caia nesse coverage aqui, né? Nesse não existe chudu, então vai retornar 404. Então a gente já testa branding antes de implementar tudo.

**[01:51:35]** Então, task test. Legal. Olha o que ele deu aqui. Input should be a value dictionary. É legal esse erro aqui. Quem deu o erro, né? Foi nesse teste aqui. Pet to do. A gente mandou uma coisa e ele falou enable trace my log, tal, tal, tal, tal, tal, tal. O que aconteceu aqui? Faltou o await. Await. Await aqui dentro. Legal, vamos rodar de novo.

**[01:52:16]** Beleza. Passou. Se a gente for olhar o coverage, em teoria aqui, ele tem que estar tudo coberto. Legal. A gente testou o Scala, a gente chamou o Tudu, viu o que estava acontecendo e aí agora a gente traz a outra parte do Tudu que a gente tinha. Mas antes disso eu quero responder uma pergunta aqui. O RS falou o seguinte, qual a diferença de usar dados opcionais assim e usar com typing optional? Nenhuma. O optional é a mesma coisa de...

**[01:52:45]** Aquela coisa ou none. Saca, se você vier aqui, Python, e fizer o seguinte aqui. Ah, int ou none, deixa eu importar, né? From type import optional. Se a gente fizer o seguinte, int ou none, é igual ou igual a optional de int? Sim, é a mesma coisa. Ah, tem uma diferença semântica e tudo mais, mas é isso.

**[01:53:15]** Optional é sempre, envia o int, se eu não enviar ele é none. É isso que significa optional. Então, é a mesma coisa. Ou int ou none. Opcional, então é um int opcional. Se não for int, ele vai virar none, se o parâmetro não for enviado. É basicamente isso. Fique sentido? Deu para pegar aí? E aí agora, a gente vai para a segunda parte aqui, né? Dessa brincadeira. Aqui...

**[01:53:57]** Eu vou pegar, aqui, para não fazer um montão de if dessa vez, eu resolvi fazer um pouquinho diferente. Olha como é que resolve o if daqui de cima. Eu fiz um com if e vou fazer o outro sem, só para a gente acumular a massa cinzenta aqui. Olha, eu vou pegar o modelo do Tudu e vou excluir todas as coisas que não foram setadas no modelo, ou seja, tudo que é NAN. Legal, eu sei que isso é meio absurdo,

**[01:54:35]** Então eu vou dar um breakpoint aqui pra gente ver o que está acontecendo. Vou dar um breakpoint antes dele sair aqui, porque a gente já tem um teste que teste isso aqui. Legal, vamos rodar o task test aqui e a gente parou aqui dentro desse teste, dentro desse esquema. Então vamos pensar que a gente recebeu esse to do aqui. Então vamos lá, to do. Viu como ele veio todo Nanny aqui? Title, description, state. Então o que que eu vou fazer aqui? Eu vou dar um model dump nele.

**[01:55:06]** A gente já fez o model dump que converte o objeto do pai dente que no dicionário Python, então model dump. Aí ele transformou tudo com chave-valor e são none. E aí eu posso falar para o pai dente aqui que eu quero excluir os que não têm valor. Então exclude and set. True. Legal. Ele montou um dicionário vazio. Olha que massa. Então se eu tivesse um título aqui, vamos lá.

**[01:55:34]** Eu vou pegar estudo e vou falar que o título dele é batata. Massa? Então no dump a gente tem a batata nanan. Quando a gente for dar o unsat true, olha o que aconteceu. Ele deletou todo mundo que era nan. Esse é um jeito de evitar aqueles milhões de ifes que a gente tinha ali dentro. Massa? Fez sentido isso aqui?

**[01:56:10]** Só pra gente não criar 15 ifs. Tem... Tem to do, tem title, tem description, tem state. Então é um jeito de resolver. Eu deixei os duas formas aqui, aí depois se quiser refaltar o outro, você se diverte ali. E aí, aqui dentro do Python tem um rolê que a gente chama de items. Que todo dicionário tem itens. E aí ele divide as coisas em chave e valor. Então se eu quiser pegar o primeiro item disso aqui e falar, olha, chave é título, valor é batata...

**[01:56:43]** dict items is not subscriptable eu preciso eu vou transformar isso aqui em uma tupla tá bom a 0 aí a gente tem o chave é o título e o valor é o batata beleza de novo vamos lá vamos lá ver se é mais fácil aqui quando eu pego o itens aqui

**[01:57:11]** Eu tô pedindo pra ele me dar uma estrutura que é iterável, né? Ou seja, ele vai compactar, em vez de ter a estrutura do dicionário, ele fica chave-valor, como se fosse uma estrutura única aqui dentro. Mas se eu der um list disso aqui, ele só tem o título, mas se eu pedir o Itens do dicionário, ele me deu uma lista de tuplas, então tem title e batata.

**[01:57:38]** Mas se eu tivesse outra coisa aqui, vamos colocar outro rolezinho aqui, a gente quer o description aqui. Description. Vai ser frita. Aí ele transformou em uma lista de tuplas, chave-valor, chave-valor. Aí a gente vai fazer um forneço aqui e vai pegar chave-valor e vai pegar esse objeto que veio do banco e vai atualizar a chave com o valor que a gente pediu aqui.

**[01:58:10]** Tá vendo? Essa é uma forma bem mais sofisticada de fazer a coisa, né? Então, a gente vai pegar esse DB Chudu, né? Esse Chudu que a gente trouxe do banco, que tinha o ID aqui. A gente vai dar um dump nele, ou seja, transformar ele num dicionário.

**[01:58:30]** só com os campos que não são NAN, transformar isso aqui numa lista de tuplas, que não é exatamente uma lista de tuplas, e a gente vai pegar todas as chaves que vieram no modelo, com todos os valores que não são NAN, e vai trocar esse atributo específico, sei lá, o title, no débito do trocando title pelo valor que veio novo nesse formulário. É muito mais complicado fazer bonito, né?

**[01:59:02]** E é isso aqui que a gente está fazendo, então a gente vai iterar em todos os valores que não são nan, setar eles nesse objeto que a gente trouxe do banco, vai adicionar ele na sessão e comitar as alterações. E a partir desse comit a gente dá o refresh para trazer o objeto atualizado para a sessão e a gente retorna ele. Massa é um bloco de código pequeno, mas que tem muitos sentimentos aqui dentro.

**[01:59:34]** Essa é aquela hora que você fala, nossa, era melhor ter criado cinco ifs, né? Eu sei, eu sei. E é basicamente isso aqui que está acontecendo, então vai pegar todo mundo, vai adicionar na sessão e a gente se vira com retorno do que vier aqui. Massa? Vamos testar, então se isso funciona? Eu vou copiar esse teste que a gente tem aqui.

**[02:00:05]** aqui no Test2 e a gente vai fazer um Tudu que deu certo, que foi atualizado. Então, a gente comita com await, para isso o teste precisa ser async e para o teste poder rodar async, a gente tem que chamar o pytestemark.async.io. Legal, então a gente criou uma factor do user ID, adicionou ela no banco, fez o commit e a gente vai mandar aqui, um cliente com teste.

**[02:00:37]** E aí a gente vai validar se o título que voltou aqui é o teste mesmo. O problema é a primeira vez. Depois copia e cola. Exatamente isso. O problema é ter essa sacada. Depois que tem essa sacada você fala, amor, é isso aí. Você pega isso aqui e cola lá no filtro. Vai dar o mesmo resultado depois.

**[02:01:03]** E a gente quer ver se o título é igual a esse teste. Se for, significa que ele conseguiu iterar, tirar os nanes e atualizar só o campo que precisava ser atualizado aqui. Vamos ver? Task test. Lindo. Funciona. Nice. Um bloco de código complexo com um teste absurdamente simples. Com um teste bem simples.

**[02:01:43]** E aí, eu quero fazer uma pergunta para vocês aqui, antes da gente ir para o próximo slide aqui, que já são os exercícios, mas antes da gente sair e eu explicar os exercícios para vocês, eu queria fazer uma pergunta aqui. Muita gente perguntou na aula passada...

**[02:02:03]** sobre a questão do factor. Nossa, mas por que a gente usa esse factor e tudo mais e não cria uma fixture mais simples? Vocês entenderam a razão da gente ter o factor? Eu quis explicar ele numa aula em que ele não fazia muita diferença. Mas vocês entenderam o impacto que isso tem no código? Pô, a qualquer momento eu posso modificar e criar vários objetos que têm vários comportamentos diferentes dentro do teste, ali rapidinho, só vai. Saca, fez sentido isso?

**[02:02:33]** Tipo assim, por que que a gente introduziu Factor Boy no projeto agora? Tipo assim, pô, gera 10, faz um seu quê, cria um diferente, dá um mortal triplo-carpado, insere no banco de dados, saca? Essa é a ideia. Então tipo assim, a gente foi construindo cada pedrinha disso. E hoje a gente fez um crude inteiro que a gente elevou 8 aulas pra criar.

**[02:03:01]** Saca, a gente levou oito aulas para construir essa estrutura. O teste, aí tem a sessão que entra aqui, o cliente que muda na sessão, que tem a fixa, que vai e que volta do Tolkien. Saca, a gente foi construindo tudo isso aí no momento que a gente foi precisando dessas coisas. E aí você vê que agora, quando a gente precisa usar, já está tudo aí.

**[02:03:26]** Saca, usa, faz, vai. Os testes andam muito mais rápido. O difícil é começar a estrutura que segura eles aqui, né? Bom, então nessa aula, como a gente review muita coisa, eu vou pedir pra vocês fazerem tudo o que a gente já viu antes, mas não viu no projeto ainda. Então, primeiro exercício pra vocês é o seguinte.

**[02:03:56]** adicionar os campos que a gente aprendeu nas aulas passadas created at e updated at na tabela de todo eles devem ser init false deve usar funk now para criação e o campo update at precisa ter um on update beleza coisas que a gente aprendeu nas aulas passadas nos exercícios passados bom isso aí vai dar uma revir a volta em todos os testes

**[02:04:26]** Porque a gente vai precisar criar uma migração, senão isso não vai funcionar. Então, o segundo exercício é criar a migração dessas novas alterações que a gente fez na tabela. O exercício número 3 é para a gente adicionar os campos createdAt e updatedAt no esquema de saída dos endpoint, para que os valores sejam retornados na API. Aí essa alteração vai ser refletida no teste também.

**[02:04:59]** Aqui nesse esquema eu vou dar uma dica aqui que nesse exercício tem uma coisa interessante aqui. Nesse exercício vocês vão entender...

**[02:05:11]** a funcionalidade do moque do banco de dados que a gente tinha feito lá atrás. Lembra? Tipo assim, ah, mas por que eu vou ficar usando a update de Edge? Não é mais fácil chamar direto e tá tudo bem, funciona? Aqui vocês vão entender o efeito disso aqui nos testes da API e não nos testes do banco de dados. Porque como é que você vai saber que hora foi criado e que hora foi atualizado? Então aqui tem uma relação que a gente busca lá de trás também.

**[02:05:39]** Aí eu preciso cês criem um teste pro endpoint de Get, do Chudu, que a gente fez vários testes de Get, né? Mas a gente não validou o dado nunca.

**[02:05:50]** Então, eu me preocupei hoje em validar as factors, os ifs e tudo mais, mas faltou um teste para validar o que está voltando, se o texto que está voltando é o texto que está certo, se o description está certo, se o state está certo com o que a gente manda, porque a gente criou fixtures e não validou nada, né? A gente pegou o factor, né? A gente criou um factor, uma rajada de coisas, mas não validou os dados, então esse é um dos exercícios. E o quinto exercício...

**[02:06:20]** é criar um teste para validar o caso do Enum na mape de Tudu State, na tabela de Tudu. Eu quero que você escrie um teste em que você insira um Tudu na tabela. Isso aqui é um teste de banco de dados, não é um teste da API, onde o Tudu não exista. Aí isso vai dar um erro muito maluco e a gente tem que garantir que esse erro existe, porque a gente está garantindo que o Enum está sendo seguido.

**[02:06:53]** E aí vocês vão conhecer um amigo novo, que é o Pytest Rises. Que é essa coisinha aqui. Massa? Sacaram o que precisa fazer nos cinco exercícios? São vários, né, dessa vez. É tipo, implementa tudo o que a gente fez nesses esquemas novos até agora. Beleza. Não esqueçam de responder o quiz, né? Sempre tem quiz para responder.

**[02:07:26]** Aí tem pergunta aqui ó, do que que é o esquema do tio do estate? Pra que que serve o relationship? Coisas que a gente foi fazendo? O none? Pipe none? Fuzzy choice? Coisas que a gente viu nessa aula no decorrer da aula. Beleza, então eu vou pro comit aqui. Vou dar um push, vocês pegam lá depois, quem precisar desse código pronto. E bom, hoje eu passei um pouquinho, né? 10 minutos do horário.

**[02:08:02]** Mas espero que vocês me relevem, porque a gente saiu mais cedo vários dias, né? Ó. Massa, hoje não tem aula complementar para assistir para a próxima aula, porque tem um monte de exercício. E esses exercícios vão dar, sabe, vai ser para trabalhar no final de semana mesmo, para cansar de os namorados com o dué. Final de semana dos namorados, vocês vão ficar pensando em mim aí, para resolver esses problemas. Bom...

**[02:08:39]** Beleza, fechamos aqui. Um beijo pra vocês. Se tiverem perguntas sobre essa aula, manda lá no grupo, porque eu não quero mais segurar vocês aqui, né? Vão curtir, vão descansar. A gente se vê na terça-feira. E aí, a gente vai criar o quê? Na terça-feira já não lembro mais. Pera aí, pera aí, pera aí. O que é aula 11? A gente vai usar o docker na próxima aula. Então lembrem-se de instalar o docker na máquina.

**[02:09:09]** Massa para a gente conversar na semana que vem. Tem exercício difícil. Sim, sim, tem. Beijinho para vocês e é isso. Beijo. Tchau.

