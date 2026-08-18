# Transcrição da Aula: aula-14.mp3

<!-- engine: faster | modelo: small | idioma: pt -->

**[00:00:07]** Olá, pessoas. Boa noite. Eu sou o Dono Sauro. E como é que vocês estão? Vos vindas a nossa última aula do Curso de Faixa API, né? Tudo que é bom!

**[00:00:19]** Chega ao fim, em algum momento. E hoje eu não trouxe nem slides assim, eu tenho algumas coisas escritas aqui pra gente dar uma olhada, pra gente conversar, mas a ideia é ser um papo mais informal pra gente ver o que está acontecendo, conversar com vocês, entender o que vocês acharam, vocês gostaram, colher o feedback de vocês, entender um pouco mais...

**[00:00:41]** sobre o que vocês acham que faltou ou qualquer outra coisa desse gênero, mas é isso. Eu queria um feedback, eu esqueci de pedir no começo, vocês estão me ouvindo, vocês estão me vendo, pra eu não ficar falando sozinho. Um tempão, pra às vezes eu fico, e aí tá tudo bem também. Bom, se tá todo mundo me respondendo, pode ser que esteja todo mundo me ouvindo, então tudo bem.

**[00:01:10]** Bom, sobre o que eu queria falar hoje com vocês? Eu queria dar uma olhada para trás, não é aquele momento de retrospectiva de olhar para trás e conversar sobre o que que a gente viu hoje, o que que aconteceu? Esse momento também tem um lugar reservado no texto para a gente conversar sobre isso. E outra coisa que eu quero falar com vocês hoje é sobre o projeto final, porque sim, agora...

**[00:01:39]** Eu fiz a minha parte, que a gente fica aqui conversando e teve a aula e tudo mais, e agora é a hora de vocês, né? Vocês chegaram no final do curso. Parabéns, né? E aqui tem um vídeo de dez horas do Parabéns, Parabéns, do... Eu duro de um anime muito famoso por aí.

**[00:02:03]** Bom, qualquer ideia aqui, né? Do projeto final, né? Lembra que eu falei lá no começo, lá na primeira aula, a gente conversou e falou, ó, vai ter certificado, aí eu falei, pô, vai ter um certificado simbólico, né? Pra quando a gente terminar isso aqui e dar uma olhada, deixa eu clicar aqui nos slides. Os slides são... Eu acho que tem slides aqui, slides. Lembra quando eu falei lá no começo, né? Tipo assim, pô, vai ter um certificado simbólico lá na primeira aula.

**[00:02:37]** E, bom, chegou a hora da gente conversar sobre ele, né? Pra quem integrar até novembro vai ter um certificadinho bonitinho, né? Esse é o meu certificado de que eu conclui o projeto. Eu mesmo emitir um certificado pra mim de brincadeira, né? Mas tudo bem, a ideia é que vocês façam e aí eu imito isso aqui simbolicamente. Bom, pra quem acompanhou o curso...

**[00:03:03]** todo foi fazendo, foi fazendo os exercícios, aqui não deve ter nenhum grande mistério, né? Pra conversar, né? A ideia desse projeto que ele se chama MADER, M-A-D-R, né? MADER, que é o meu acervo digital de romances, né? Eu queria um nome que desce uma sigla que a gente pudesse pronunciar e aí fiquei tipo, beleza, romances, livros, né? Eu fiquei um tempão pensando, pô, qual que é o nome que eu daria pra isso aqui?

**[00:03:31]** E a ideia aqui é que a gente faça um projeto muito parecido com o que a gente desenvolveu no curso e foi conversando e foi vendo as coisas, né? E a ideia é ter um gerenciamento de livros de uma biblioteca, por exemplo. Então, a gente tem o controle de acesso, gerenciamento de contas, aí a gente vai usar a JWT, aí vai ter que criar a conta, alterar a conta, fazer deletar a conta, gerenciar os livros, né? Então, tem o crud e a gente insere os livros, você pega qualquer um.

**[00:04:05]** Ah, temos aqui Miguel de Cervantes. Don't shot. Massa. Então como é que a gente vai fazer? A gente vai pegar Miguel de Cervantes, cadastrar esse romancista, que foi o nome que eu dei pra isso. E aí a gente vai lá e depois pega esse romancista que foi cadastrado, a gente cadastra o livro. Isso aqui serviria pra qualquer coisa, né? Geralmente a gente costuma usar isso aqui pra produtos, né? Mas eu queria deixar isso de uma forma mais lúdica, né? Porque, pô, ah...

**[00:04:33]** Cria aí uma estante de produtos e aí, tipo assim, produtos fornecedores, saca? Daria pra fazer desse jeito também, mas eu preferi que a gente fizesse uma coisa mais legal, né? Porque livros são muito mais legais do que contas apagando. Então, a ideia é essa. É fazer essa peizinha e tudo mais. Pedro, muito obrigado, mano. Ó, valeu demais pelo carinho, mano. Espero que ajude.

**[00:04:59]** esse conteúdo que a gente fez e obrigado pelo Super Chat, mas isso me ajuda muito melhor continuar fazendo essas coisinhas aqui.

**[00:05:07]** Então, aí eu queria fazer esse sistema gerenciador de livros e tal. Só que, como se a gente fosse o nosso TCC, né? O nosso trabalho de conclusão de curso. Ou as pessoas que costumam chamar isso aqui de teste técnico. Vamos fazer um teste técnico. Enterprise Business. Eu coloquei até aqui brincando. Enterprise Business. Bom, não era minha ideia ser Enterprise Business, então a gente fez um sistema de gerenciamento de livros. Aqui, para quem quiser dar uma olhada e tudo mais, qual que é a ideia, né?

**[00:05:36]** é que a gente tenha três routers, um router de contas, um router de livros, um router de romancistas e aqui tem todos os esquemas, tipo assim, dos requisitos que a gente precisa atender para fazer o sistema funcionar. Então beleza, eu queria criar uma conta e aí o esquema já está aqui também.

**[00:05:55]** Aí esse esquema deve ser validado com o Pai Dente, que tem todas as coisinhas. O retorno, 201, com o ID e meio e tal. E aí eu coloquei algumas coisas. A senha deve ser criptografada, não sei, serida no banco, coisas que a gente fez. Não é necessário fazer o login no sistema para enviar uma requisição para o sendpoint. Ele não pode ser bloqueado, porque como é que eu vou criar uma conta se eu não tenho uma conta e... Você entendeu.

**[00:06:19]** Aí tem aqui, né, tem alguns avis de erro, né, conflito, e aí se a gente for clicar no conflito, tem aqui uma explicação do que quer pra voltar, e tudo mais, as mensagens de erro, o 409 que teria que voltar aqui. Aí eu coloquei um desafio a mais aqui pra brincar com vocês, de sanitizar os dados no banco de dados, que é a ideia de tipo assim, ah, entrou machado de assist, tipo assim, capitalizado, a gente salva...

**[00:06:44]** Tudo minusculezinho. Manoel, espaço, passo, passo, passo, passo, passo, passo, bandeira. Então, a gente vai normalizando as coisas. Então, uma coisinha simplona de sanitização aqui. Manipulação de string simples. Aqui não precisa de muita coisa. E aí, aqui tem a descrição de tudo o que precisa ser feito. O put, o delete, o post para criar o Tolkien, o refresh do Tolkien. Aí tem aqui as condições, o JWT, o tempo que deve ter, o algoritmo que deve ser usado.

**[00:07:11]** Aí aqui tem uma ideia dos livros, como é que a gente faz esse cadastro, esse tipo de coisa. Então eu preciso do ano, preciso de quem escreveu o livro, preciso aqui do ID, de quem escreveu o livro, né? Um relacionamento, aquela coisa que a gente aprendeu a fazer, né? Tudo user. Aí aqui a gente tem o café da manhã dos campeões, que é um livro do Kurt Vonnegut.

**[00:07:34]** Aí o retorno, ele retorna o ID, aí tem o delete do livro, patch, todas essas coisinhas que a gente viu, tudo no curso. Aí o get explica, né, as queries strings, por nome, por ano, se alguém quiser saber todos os livros de, sei lá, 1900, a gente tem aqui, ó, memórias próximas de Brascovas, café da manhã dos campeões, os esqueminhas e tudo mais.

**[00:07:57]** Aí, olhando aqui por cima, vocês conseguem ver, e aí eu quero o feedback de vocês, que é exatamente o que a gente fez no curso, não tem muito rodeio, mas a ideia é, tipo assim, meter a mão na massa fora de um código aquele que não foi o que a gente fez junto, né? Acho que não tem nada de outro planeta, né? Aí aqui tem essa indicação, eu salvei aqui um lugar pra gente conversar sobre os erros, né? Você pode fazer os seus, né? A ideia não é restringir, né? Mas...

**[00:08:26]** Dá umas ideias para quem potra ver o que eu respondo aqui. Então erro de permissão, erro de autenticação, os não encontrados, erros de conflito e tudo mais. Separei algumas coisas aqui. Nossa, está ruim isso aqui. Talvez eu arrumei depois. Deixa eu colocar. Vou jogar o flashbang aqui. Então aqui tem as tabelas, o DER, o Diagrama de Entidade e Relacionamento. Então aí aqui o relacionamento no R&M, para ver o que acontece.

**[00:09:02]** E aí, se precisar daquele... Puta, precisa de um empurrãozinho. Como é que faz mesmo aquela coisa? Eu deixei aqui uma... Uma coisinha... Ah, como é que faz um backpopulante? Não sei se sabe. Aquelas viagens do ORM aqui.

**[00:09:14]** E aqui no final eu deixei algumas coisas que são os casos de teste, os cenários de teste estão prontos aqui, porque eu entendo que embora a gente tenha testado muita coisa, a gente viu cobertura de testes, a gente conversou sobre todas essas coisas, eu sei que em alguns momentos cria os próprios testes, sabe? É o momento que ainda... sabe? Pô, o que que eu tenho que testar exatamente em cada lugar, né? Então a ideia aqui eu trouxe o...

**[00:09:45]** Os cenários aqui, ó, da criação de contas, então beleza. Isso aqui é uma linguagem chamada Gherkin, que é um esquema de escrever testes mesmo, tipo assim, quem usa BDD, Frameworks, tipo Behave e tal. Então tem aqui, ó, quando enviar um post em barri-user com esse JSON, devo receber 201, o JSON deve conter e tal, tal, tal, tal, esses meio que vão transformando isso aqui em código. Eu coloquei os testes do caso de erro, testes de autenticação, pra enviar o Bertoken e tal, aquela coisa que a gente viu.

**[00:10:16]** Aí tem os testes de contas, os testes de livros, também deixei aqui o gerenciamento dos romancistas, para quem quiser brincar. Aqui a gente cadastra a Clarice Lispector e aí tem que ter o Jason Conte na Clarice Lispector e tudo mais. Manoel Bandeira, aqui a busca de romancistas por filtro, então fui dando uma organizada aqui para ficar mais simples para quem precisar fazer esse tipo de coisa. Bom, e aí como é que funciona esse projeto? Basicamente você pode fazer ele com as ferramentas que...

**[00:10:47]** Vocês quiserem, mas usando as coisas que a gente viu no curso. Então, a ideia é que vocês façam isso usando o Python 311mais, que é o que a gente fez, de forma geral. Confess API, usando SQL Alchemy. Ah, posso usar o Mongo, se eu quiser, como Benny? Eu preferia que fizesse com SQL Alchemy, para a gente entender essa coisa.

**[00:11:10]** E aí, muitas vezes, durante esse curso, a gente viu aquela pergunta repetida, várias vezes. Não, por que que não usa outra ferramenta no lugar do Poetry? Por que que não usa o Pipe? Por que que não usa o VM? Não, por que que não usa o UV? Por que que não usa o PDM? Então deixe aí livre aqui. Você gosta do Poetry, usa o Poetry, você quer usar o UV, usa o UV, você quer usar o PDM, o Hatch, o High, o Pipe. Fica à vontade. Qualquer ferramenta que suportar o Pi Project, quase todas, hoje em dia, dá para fazer isso aqui. Aí precisa do Postgres.

**[00:11:40]** containers, então a ferramenta que você preferir, às vezes você não gosta de Docker, igual eu. Eu não gosto de Docker, mas se você quiser, pode usar, tem o Podman, tem o Kubernetes, pode usar o Nerd CTL, qualquer outra coisa nesse formato, e usar o PyTest. Usar Tox, Nox, é exatamente isso aí, fica à vontade, pode usar o que quiser, a ideia é entregar essa API e fazer esse esquema. O Germano falou, precisa ter assim que?

**[00:12:10]** É claro, a gente aprendeu assim que no curso, por que que não vai fazer com assim? Estudamos assim que? Por que que não vai fazer assim? Aí o Caio mandou um super chat aqui. Caio, muito obrigado, mano. Valeu demais. Tamo junto, mano. Espero que ajude. O objetivo era esse, né? Ah, mas eu não gosto do pytest. Foi o que a gente aprendeu, a gente vai usar o pytest, né?

**[00:12:36]** E aí, qual que é a ideia disso aqui, né? Então, aqui tem tudo, né? Toda essa coisa do projeto, tudo que precisa fazer, todos os endpoints. Isso aqui é legal, porque às vezes você quer saber. Ah, eu tenho um portfólio que eu queria mostrar na entrevista de emprego para falar que eu já fiz alguma coisa. Tá aí. Porque esse projeto a gente não fez, né, junto. Então, não tem aula, a gente vai fazendo junto, né? Tipo assim, você vai. E aí, a ideia agora, mané, usa o grupo, tira em dúvidas e tudo mais. A ideia é a gente se ajudar.

**[00:13:06]** e fazer as coisas juntos, não? Então, ah, pô, eu tô fazendo isso aqui, tal, vamos se ajudando, tem até novembro, então, junho, a gente tá em junho, julho, agosto, setembro, outubro, novembro, tem cinco meses pra fazer isso aqui e vai fazendo, massa. E aí, como é que vocês entregam isso aqui pra mim, né? A ideia é essa, como é que vocês entregam esse rolezinho pra mim?

**[00:13:33]** Eu quero que vocês hospedem uma plataforma de Git, qualquer, aí pode ser no GitHub, no GitLab, no Codeberg, onde vocês preferirem aqui. E lá no nosso projeto tem um maixo no repositório, que é essa aqui, que é 135, onde estão todos os projetos de todo mundo que foi entregue até agora.

**[00:13:58]** Então, a galera que fez a versão do ano passado e tudo mais, então tem várias submissões aqui. É que o Git dá uma cortada aqui, Lola da Mais e tal. Mas tá aqui. Aí todo mundo que fez o do ano passado, eu mandei aqui, né, então todos os certificados estão aqui, e aí é a mesma coisa que eu vou fazer de novo depois com os certificados de quem mandar. Então, a ideia... Eu não tenho como saber como emitir o certificado pra vocês, né, de novo. Eu não tenho como emitir o certificado se vocês não mandarem na ispa, então...

**[00:14:28]** Façam isso, algumas pessoas mandaram e-mail no ano passado falando, eu fiz, mas tipo, polimca aí na issu. O objetivo é esse, então criam o repositório em qualquer git que você quiser, na Codeberg, no GitLab, no GitHub e no... E sobe aí, massa. Aí aqui embaixo, pera aí, deixa eu achar aqui. Aqui. Eu não coloquei algumas coisas aqui nesse projeto, mas eu gostaria que elas tivessem implícitas para vocês. Eu quero que vocês tentem fazer o deploy.

**[00:15:01]** O projeto precisa estar com deploy? Não precisa não, não precisa. Já pensou eu tenho que acessar e aí tipo eu levo três meses pra acessar. Então não precisa fazer o deploy, mas a ideia é que vocês façam o código, né? Pensa que a aula do deploy ela foi só um luxo, né? Tipo assim.

**[00:15:15]** Ela foi uma coisa a mais que a gente fez, não se preocupem com isso. Então não precisa fazer o deploy se não quiser, mas a ideia é que vocês façam todo, construam essa estrutura, façam o CI, a integração contínua, tentem rodar os testes todas as vezes, usem as ferramentas, a gente viu um ferramental incrível aqui durante esse curso inteiro, então a ideia é que vocês brinquem com isso, se divirtam e...

**[00:15:41]** Saca, entregue isso. É legal pra vocês, né? Pra gente ver o que está acontecendo. E aí aqui no site, depois, se alguém quiser ver depois os projetos das outras pessoas...

**[00:15:51]** Tem aqui, né? Tem uma página com todos os projetos. Às vezes você quer olhar o de alguém e falar, pô, eu não sei o que fazer aqui. Então, o legal de estar todo mundo junto é que você pode vir aqui e falar, tipo assim, ah, eu quero ver esse aqui do Thiago. Ah, o Docker está no abril separado. Então, tem uns comentários aqui. Ó o do Tacone, a PI assim que ele fez templates. Então, cada um foi viajando na sua própria viagem, porque a ideia é essa, né?

**[00:16:14]** Ó, o Globosco fez com Dev Containers, ele roda via Kubernetes, lembra? Eu falei pode estar livre aqui, a ideia é que vocês se divirtam e aí como cada pessoa vai fazendo um jeito diferente, você pode lá e pega e acessa, tipo assim, deixa eu ver esse aqui do germano. Então tá aqui, entra aí, dá uma fuçada e tudo mais. A ideia é que a gente aprenda em grupo e tem o grupo também no Telegram pra gente se comunicar e trocar a ideia e tudo mais. Aí depois no final a ideia é que todo mundo fique aqui nessa página.

**[00:16:42]** como uma breve lembrança de tudo que eu coloquei de repositório aqui, né? Então a ideia do projeto final não tem nada demais, assim, né? É exatamente as coisas que a gente viu durante o curso todo. E aí eu ficaria muito feliz se vocês fizessem isso aqui, né? Assim, não porque...

**[00:17:08]** Eu falo, nossa, tem que fazer, mas por que é uma forma de aprender? Você tem um recurso a mais, com tudo que a gente fez. Criar uma coisa nova da tua cabeça, com as tuas ideias e tudo mais. Não está aí, olha o Germano, olha o meu aí, foi exatamente o dele que eu abri. E não foi pensado porque ele está aqui na live. Então a ideia é essa, vocês têm aqui o projeto, entrem, brinquem, façam, se divirtam, compartilhem com as outras pessoas.

**[00:17:35]** A ideia é que daqui pra frente vocês vão levando o curso, né? Na ideia de vocês aí, no que vocês acharem legal, mas não esqueçam de mandar na Brent, porque aí depois, na Brent não, na IXO, porque aí depois eu emito o certificado e tal, e a gente vai deixando a coisa mais rica, né, pra todo mundo. João, obrigado, mano, ó. Valeu pra você tornar membro, mano. Tamo junto. Me ajuda muito essa parada. Legal, entendido? Vocês têm alguma dúvida sobre esse projeto final e tudo mais? Me contem, porque agora é a hora, né?

**[00:18:07]** Nunca mais vou falar de facem-piai aqui, brincadeira, mestre. Então agora é o momento. Então tipo assim, tá tudo aqui, eu tentei deixar o mais explícito possível, mas se vocês forem tendo dúvidas, talvez eu venha, mexo aqui na página, troco uma coisinha ou outra para ajudar todo mundo. Massa.

**[00:18:27]** Bom, o que mais que eu queria falar para vocês aqui agora? Então a gente fechou essa parte, até novembro eu vou dar certificado para todo mundo que enviar os projetos e aí agora eu quero focar nessa parte aqui com vocês da despedida, né? Irá surgir quando começamos a fazer, né? As dúvidas, sim, né? Não, mas aí eu falo alguma pergunta referente ao processo e tudo mais, não? Então, legal, olha, agora que eu falei tudo do certificado e tudo mais, falei do projeto de conclusão...

**[00:18:59]** Eu queria falar uma coisa antes de a gente entrar nessa pira, que brilhado mano, pra vocês terem me acompanhado nessas jornadas. Todo esse curso foi feito por uma campanha de financiamento coletivo que a gente fez alguns anos, então esse curso...

**[00:19:17]** Ele não foi de graça, eu recebi uma grana para fazer ele, de todo mundo. Todo mundo deu um pouquinho. A maioria das pessoas que pagou, que financiou esse curso, nem veio assistir o curso, porque a ideia era ajudar de uma forma geral. Então, a galera me ajudou, me deu uma grana para eu conseguir me manter durante esse tempo e, bom, faz três anos que eu estou mantendo isso aqui. A gente fez uma versão no ano passado, a gente fez essa versão agora.

**[00:19:43]** O texto tá andando muito, né? Pra quem acompanha pelo material de texto. A gente já tá na quarta versão do material de texto. E antes de finalizar esse ciclo, da minha parte, ainda vai sair a versão 4.1 com algumas mudanças que a gente foi fazendo durante a aula. Lembra que a gente falou? Ah, e se a gente colocar um negocinho no pai dêntico aqui e um outro negocinho ali? E aí eu fui... Eu fui pegando aqui. E aí quem quiser acompanhar esse trampo que eu tô fazendo aqui tem...

**[00:20:14]** Ele está aqui. Então, minha ideia é, antes de finalizar isso aqui, lançar essa última release com os tópicos aqui do SpyDentics que a gente viu, uma coisa nova que entrou no Fast API, que é no... O Alph Password Bear lá que a gente usa, que a gente dá o depends lá para pegar a credencial, agora ele consegue especificar aonde está o refresh. O que é sensacional, eu já implementei isso aqui, só não merginei na página ainda, então quem quiser ver, como é que está?

**[00:20:46]** É uma diferença sutil, mas já está aqui. Então, se vocês quiserem dar uma olhada, aqui ó, mundo é pouca coisa, né? A gente só adicionou o refresh, o RL, mas já é uma coisa mais na documentação que tem um ganho legal aqui. Agora ele mostra onde a gente atualiza o Tolkien, uma coisa que não acontecia antes, então fui dando umas melhoradinhas aqui.

**[00:21:13]** Que tipo de vagas ou projetos reais usam o Fast API? Qualquer projeto que você precisar fazer uma API, você pode usar o Fast API. E a maioria das vagas que eu tenho visto é para isso mesmo. Fazer APIs com o Fast API. Tem uma coisa, a galera tem usado muito para fazer APIs de machine learning e tal, então muito, muito legal.

**[00:21:40]** Muito bom, não sou programador, mas estou contente assistindo umas quatro, cinco vezes por aula. Porque estamos juntos, mano. Qualquer coisa, tem o grupo lá pra gente trocar ideia e tudo mais. Bom, a gente chegou nesse final do processo aqui e, bom, pra quem acompanhou desde a primeira aula, a gente viu um monte de coisa aqui, né? Literalmente a gente viu muita coisa. A gente conversou o básico sobre FastAPI, a gente viu como é que fazer, como fazer API.

**[00:22:09]** como lidar com o sincronismo da API, a gente entendeu o servidor de aplicação, o Yuvicon, a gente aprendeu o básico sobre HTTP de uma forma geral, como funciona, os templates, a comunicação, verbos, tal. Foi legal, a gente viu um pouco de Docker, como doquerizar nossa aplicação Python, a gente aprendeu um pouco de testes.

**[00:22:39]** Germano falou, poderia passar essas vagas? Mano, olha no linkadim, velho. Abre o linkadim e busca. Fast API, mano. Tem muita vaga lá. Acho que no começo da campanha eu mostro, tipo, no vídeo da campanha eu mostro uma curva que tinha, né? Meia mais três. Esse está bem maior agora. Então a gente viu um pouco de testes. A gente viu um pouco de TDD, mas não tanto quanto eu gostaria, né? Eu queria que a gente tivesse feito mais testes antes, mas a gente aprendeu muito sobre testes, né? A gente viu não só sobre testes em geral, né? Mas a gente aprendeu...

**[00:23:10]** As coisas do teste, os testes de três fases, o arrange act assert, a gente viu fixers, a gente viu randomização de dados, a gente viu os factors, a gente aprendeu a conectar subcontainers e tudo mais dentro dos testes e fazer toda essa relação.

**[00:23:27]** A gente trabalha com banco de dados, migrações, autenticação, autorização, a gente viu a integração contínua, a gente fez o deploy, a gente aprendeu o esquema dos paytentics, de serialização e mais um monte de coisa. Pô, eu gostei, eu achei que foi bem proveitoso de uma forma geral. A gente viu bastante coisa.

**[00:23:55]** a gente viu muita coisa mesmo assim e aí eu queria perguntar de vocês assim vocês já tinham mexido com todas essas coisas não tipo assim às vezes a gente nunca mexeu com autenticação com testes e tudo mais que que foi novidade para vocês dentro desse esquema assim né e além do que que foi novidade o que que vocês mais gostaram de mexer né eu sou muito tendencioso para falar sobre isso mas a parte mais legal para mim

**[00:24:19]** é sempre essa parte de fazer os testes, né? Eu me diverto muito, assim. Vocês vêem que a gente vai fazendo, aí eu testo, e aí volta, e vai, e pega, bota o break e ponte, dentro do teste, vai fazendo. Pra mim essa é a parte mais legal, assim, né? Essa... essa coisa, né, de olhar o código com uma outra ótica, né? Sempre quando a gente tem esse sentido de aprendizado, muitas vezes a gente não...

**[00:24:45]** No match com testes. Foi uma coisa que eu fiz questão desde o começo. A gente começa o primeiro endpoint, a gente bota o teste lá, a gente vai testando tudo e exercício de teste e tudo mais. Essa é uma parte que pra mim eu peguei um mais pesado que eu pude. E é tipo assim, pesado no sentido. Tipo assim, todo a hora tem teste, tem que ter teste.

**[00:25:08]** Porque, na vida real, essa coisa que acontece, né? Tem que fazer testes, tem que fazer as coisas. Alfredo, muito obrigado, mano. Valeu demais. Pelo super chat, tamo junto. Ó, o germano falou que, com a Lembic, ó o Red, né? Falou que vem do mainframe. Que massa. O Ale falou, já tinha mexido com o FastAPA empresa antes, mas o estrutura do curso me ajudou a implementar durante um processo seletivo. Pô, que massa, que massa, Harano. Que legal saber disso, assim, de todo mundo.

**[00:25:38]** E bom, voltando aqui, vamos lá. Eu queria falar por vocês que eu fiz outras coisas aqui no período do canal e tudo mais, a gente tem vários outros conteúdos de Fast&Py, que não são especificamente um curso, são lives, são coisas que elas foram acontecendo durante a existência do canal de uma forma geral. A gente já está quase na live 300 aqui no canal, mas tipo assim, lá na metade do...

**[00:26:06]** da minha vida útil do canal, a gente viu WebSockets. Aí eu coloquei alguma coisa aqui, porque a gente não tinha visto durante o período. Então a gente não viu durante o curso e tem várias coisas que a gente não viu. Porque não dava pra abordar tudo. Eu falei um pouco sobre WebSockets.

**[00:26:26]** na live 164, que é uma boa coisa, que é uma coisa legal, um recurso muito foda do FES8i, que a gente não viu. A gente também não trabalhou com templates, a gente gerou um HTML na mão, mas quando você precisa de HTML, JavaScript, e todas essas coisas, tem essa live aqui, que é a live 164. E aí fica de um material extra aí, se vocês quiserem ver. E...

**[00:26:52]** Tem bastante coisa nessa live, a gente fala sobre a sincronismo, sobre pooling, sobre várias coisinhas que a gente não viu no curso, então achei que valeu a pena deixar ela aí como uma referência, para vocês olharem depois, às vezes tem curiosidade, e, pô, se fazer uma conexão persistente, pô, tem aqui. A data de entrega é até o fim de novembro, Adonai, que eu vou receber as coisas. Deixa eu ver o que mais vocês mandaram aqui. Eu usei Django muito tempo,

**[00:27:28]** Já, e tinha feito umas APG test com FHPR, mas nunca tinha feito um projeto inteiro desses. Essa parte é interessante, passo por todas as fases do desenvolvimento. Tem algumas coisas que eu não falei aqui, que eu não coloquei na...

**[00:27:42]** na nossa retrospectiva aqui, mas a gente falou sobre outras coisas, que tem a ver com o gerenciamento do projeto e tudo mais, que foram legais lá no começo, na primeira aula a gente configurou, tem o Ruff, o Linter, o Formatter, tem o TaskPine, a gente foi aprendendo o Poetry, o PpX, são ferramentas que vêm no ambiente de uma forma geral, que combina com o que o Caio falou aqui de passar por todas as fases do desenvolvimento.

**[00:28:10]** Eu tinha acompanhado o tutorial com essa mesma stack, mas o deploy era na digital hoje. Pô, legal, legal também. Pra mim foi a refatoração. Como programei pouco, estou acostumado a fazer tudo no arquivo só. Pô, que massa, que massa. Aí, ó, e essa parte que eu levei menos em consideração, né? Eu tentei deixar estruturado o suficiente, mas eu falei na aula, né? Pô, tem várias formas de fazer essa refatoração ficar melhor e tudo mais. A gente vai usar os recursos do framework, né? Mas tem muitas coisas mais, né?

**[00:28:38]** O alarm falou, lembra que doca, integração, backend, DB, autenticação, OCI, tudo isso foi novo pra mim, aprendi muito com o curso. Pô, que legal, mano, que legal. Espero que ajude, né? O objetivo era esse. Tudo mesmo, me ajudou um projetinho que estou brincando com Flask, esse curso me ajudou a formular o meu projeto, tive 180 graus de melhoria, foi que massa. Quanto testes passam, um sentimento diferente. Sim, quando dá o verdinho, assim, no final, eu me dá um negócio assim, eu fico tipo, pô...

**[00:29:08]** Que legal, né? Que massa, né? Mas foi interessante ter essa visão mais abrangente da parte de baixo. Pô, legal. Muita coisa que eu não tinha visto. A parte do DB com o test, foi uma das coisas que eu achei mais interessante. Pô, legal, legal. Deixa eu tuci aqui rapidinho.

**[00:29:36]** Aí o adulto falou, acrescenta o módulo sobre observabilidade, testes de carga, manutenção de pessoa alogada. Então, já tem material sobre isso aqui no canal, né? Eu não vou falar sobre isso dentro do curso, porque a gente já fez isso. Então, tipo assim, e é com festa IPA exatamente o que a gente faz, né? Então, eu queria isso do curso, eu nem coloquei isso no curso, porque a gente já fez esse material, ele já tá pronto aqui no canal, né?

**[00:29:59]** A Marcos falou, muito obrigado pelo curso Maratoneia As Aulas Fiz os Projeitos Pessoais para a Facul, porque o coincidência foi chamada por um projeto na faculdade quando os requisitos eram justamente festas de API. Pouco legal, Marcos! Parabéns aí, sucesso nessa parada. E, bom, que mais que a gente não viu, né? Tem essa outra parte que eu deixei aqui que é uma outra forma de fazer APIs, que não são APIs nessa forma de endpoints fixos e tudo mais, que é uma forma de fazer o GraphQL.

**[00:30:34]** Geralmente quando a gente trabalha com desenvolvimento móvel, quando a gente vai fazer back-end para o desenvolvimento móvel, mobile.

**[00:30:45]** como alguém gosta de me corrigir sempre. A gente costuma usar um outro tipo de API, que é um API que o front ou o cliente diz quais são os dados do back que ele quer obter. E não é uma forma tipo assim fechada. Pô, barra no seu que traz o dado. Então ele vai reformulando toda a query de uma forma diferente e tudo mais. E aí a gente tem essa live aqui do Throwberry, que é uma ferramenta que a gente coloca junto com o FastAPI.

**[00:31:12]** para fazer GraphQL, que é essa forma de requisitar APIs de forma mais performática possível, então tem aí também. Tem aqui o material sobre isso. Outra coisa que tem aqui é o SQL Model. Muita gente, quando trabalha com o Fast API, trabalha com um outro RM, porque é um RM criado pelo criador do Fast API, que é o SQL Model. Ele usa como base o SQL Alchemy.

**[00:31:44]** Eu acho o SQL Alchemy a melhor escolha de todas, né? Sempre vou reiterar isso, porque ele é muito bom. Mas, geralmente, às vezes você vai chegar num projeto e você vai se dar conta de que o que usa lá SQL Modo, eu confesso API. Moringa, muito obrigado, mano. Valeu. Tamo juntão, mano. Valeu demais.

**[00:32:07]** Me ajuda muito esses super chats. E aí vocês precisarem aqui? Tem uma alona sobre a SQL Model e no final a gente integra o SQL Model com o FastJpy no fim dessa aula aqui. Então é um jeito legal de olhar as coisas, né? Uma outra coisa, uma outra abordagem que o FastJpy também faz que é muito legal é de trabalhar com componentes, renderização no front, né? E aí foi criado uma biblioteca pela galera do Piedantic que é o FastUI, né?

**[00:32:36]** que é uma é uma ferramenta ela tá com baixa manutenção agora no futuro ela vai voltar né tem umas explicações aqui pra quem quiser mas é basicamente uma coisa pra fazer uns frontzinhos malucos assim saca a esse links e tal botões modais e tudo mais tudo usando o fast API renderizando do back

**[00:33:00]** E essa biblioteca é o Fast UI, é uma biblioteca de user interface, UI de fazer telas e tudo mais, com o próprio Fast API, como base. E aí se vocês quiserem dar uma olhada nisso aqui e tal, a gente fez uma live sobre isso também, algum tempo atrás, que é a live 259. Então tá aí também, então bom, tem materiais para ir para todos os lados, tem...

**[00:33:25]** de Y, tem outro RM, tem GraphQL, tem WebSockets, então vocês precisarem de materiais opcionais, né? Coisas que a gente não abordou no curso têm esses outros materiais todos feitos com fastchapion, né? Então é muito legal e tem várias outras coisas para conhecer, né? Então antes de eu entrar aqui no próximo passo, deixa os próximos passos, deixa eu ler o que vocês escreveram aqui. Consegue dar uma palhinha só para dizer o que são WebSockets? Então Lucas, a ideia do WebSockets

**[00:34:00]** que a gente faça o seguinte. Imagina que a gente tenha uma conexão que ela precisa ser persistente. Vou dizer dessa forma. Então imagina, por exemplo, que eu estou fazendo um aplicativo que é um GPS. Então pensa que no GPS a gente tem que ficar acompanhando, né? Aonde a coisa que a gente está indo, né? O carro, uma bicicleta, uma moto. Saca, nesse esquema, então você vai acompanhando a rota.

**[00:34:29]** Então o WebSockets é a ideia de ter essa conexão persistente e a gente fica trocando dados, né? Então eu falo pro server, ó, tô conectado em você, vai me mandando os dados. E aí, conforme as coisas vão atualizando, a gente vai trazendo, né? Uma outra forma de o WebSockets, a mais clássica, é com chats, né? Então, por exemplo, vocês estão escrevendo aí e eu tô vendo as mensagens, né? Tô recebendo as mensagens de vocês. E elas estão aparecendo aqui na tela. Sabe essas mensagens? Isso aqui...

**[00:35:00]** Exatamente isso aqui que vocês estão vendo. Isso é uma aplicação de WebSocket. Então eu conecto na API e isso aqui foi feito com o Fast API. Também foi feito com o Fast API. Então eu estou conectado, né? Esse navegador, que está mostrando essas mensagens para vocês, está conectado no meu back-end e aí conforme vocês vão mandando, o back-end vai mandando informação para o front e ele vai atualizando isso aqui em tempo real.

**[00:35:31]** Então, não é tempo real, sabe assim, tem uma latência, mas é uma conexão persistente. Faz sentido, Lucas, isso aqui? Fez sentido? Então, essa é uma das formas. Tô adorando que eu conheço o Festa Hipertens, dando todos os dias consumindo conteúdo, eu tô empolgado. Pô, que massa, mano. Espero que ajude, de alguma forma. O Rodrigo falou, também foi muito bom ver as imigrações, porque na minha cabeça, e acho de muita gente, se o banco tem que ser atualizado e tal, o ideal é ir pro MongoDB. Mas, claramente, não é assim, não.

**[00:36:08]** A gente vai usando essa coisa. Mac Loving. Muito bom, Nickname. E a foto do Mac Loving. Valeu por se tornar membro. Rodrigo, também. Beijo pra você. Valeu aí, mano. Vocês me ajudam demais. Isso é ótimo. Obrigado pelo curso. Gostei bastante. Pô, que legal. Então, vamos continuar conversando aqui. A ideia.

**[00:36:36]** Agora que a gente sabe a base, é que vocês consigam construir outras coisas usando Fast API, não? Não necessariamente Fast API em si, né? Vocês entenderam, né? Porque a gente viu muitas outras coisas que servem para tudo, né? A gente viu testes que você pode usar com qualquer outro framework web Python, com qualquer aplicação Python, a gente viu um básico de web que serve para qualquer outro framework, a gente viu um básico de Async que serve para qualquer coisa, né? Então, mas falando especificamente de Fast API,

**[00:37:04]** Eu gostaria de dar alguns passos pra vocês, pra vocês poderem ir explorando coisas mais fundas, né? Depois. Vocês lembram que quando a gente tava fazendo o Deploy,

**[00:37:14]** A gente se deparou com aquela coisa, tipo assim, pô, a gente tá olhando o que tá acontecendo na aplicação em tempo de execução. Lembra que a gente chegou lá no fim do deploy e a gente tava vendo, pô, tiveram X requisições, tá consumindo X de memória, né? Então, o nome disso são métricas. Então, métricas de como a aplicação tá rodando em produção. Gustavo, ó, muito obrigado, mano. Valeu por se tornar membro do canal.

**[00:37:41]** Então, essas coisas são métricas, né? Então, é interessante, né? Pra gente saber como a aplicação tá rodando no mundo, na vida real, ela tá lá fora, tá rodando, tá acontecendo. E, pra isso, tem várias coisas que a gente não viu no curso, né? Que são coisas mais aprofundadas de olhar em produção, né? Então, a gente tem logs, né? Que a gente não viu no curso. Eu cheguei a começar a trabalhar a implementação de logs pra essa versão, mas eu acabei deixando...

**[00:38:08]** Então tem logs, a gente tem métricas, que foi uma coisa que a gente também não viu. Tem traces, que são uma forma de entender como a aplicação está rodando no dia a dia, em produção. E aí a gente junta todas essas coisas, esses pilares, e cria uma coisa que a gente chama de observabilidade.

**[00:38:30]** Então é muito interessante, eu recomendo muito, vocês tenham uma olhada sobre isso, sobre observabilidade, então como trabalhar com logs, a gente tem live sobre logs aqui, como trabalhar com tracing, com rastreamento, distribuído, entender quanto tempo a aplicação passa no banco, por onde ela passou dentro da nossa aplicação e tudo mais, e métricas, entender quanto a nossa aplicação está consumindo em produção, quanto essas coisas estavam...

**[00:38:58]** Pensando, né? Tipo assim, pô, saca, ah, quantos erros a minha aplicação deu essa semana? Então, essa parte de observabilidade é muito importante, e aí foi que alguém tinha falado, ah, você não pense em fazer um adendo de observabilidade pra colocar essas coisas em produção, a gente já fez isso no canal e tem, tipo assim, uma série de muitas lives aqui sobre...

**[00:39:21]** observabilidade usando uma biblioteca chamada Open Telemetry que é tipo assim o super assumo da observabilidade então aqui tem uma introdução observabilidade a gente conversa sobre métricas a gente conversa sobre tracing, rastreamento distribuído a gente conversa sobre logs e depois a gente vê tudo isso aqui na prática então é como se fosse um outro curso aqui e tá tudo isso aqui, tá tudo isso já tá no canal, você pode assistir

**[00:39:49]** e brincar e tudo mais e aprender mais sobre como ver as coisas em produção, como construir um dashboard daquele e tudo mais, que essa é a parte mais importante. Depois que a gente aprende a fazer a aplicação web, a gente tem que aprender a manter ela, manter ela online. Então essa é uma das partes importantes aqui. E que a gente não viu nada no curso porque são coisas diferentes.

**[00:40:18]** Um outro ponto que eu deixei aqui que eu considero que é super importante de aprofundar aqui é a coisa de anotação de tipos, né? A gente viu muito por cima esse assunto, né? A gente usou o type annotated pra fazer o depends, né? Aí tinha lá aquelas coisas de meio, meio string, map string, né? Aquele tipo de coisa, né?

**[00:40:45]** que é um material que a gente não aprofundou, né? O FCPI pode ser usado muito com essa parte de tipos, a gente tentou evitar o máximo possível, ok? Eu acho que esse é um dos assuntos mais difíceis do Python. E aí, se vocês precisarem de mais material sobre isso, o sistema todo de tipos do Python está descrito na página de sistema de tipos. Então, isso, infelizmente, não tem tradução.

**[00:41:08]** Mas tem muita coisa aqui, estático, dinâmico, gradual. Todas essas coisas têm uma página inteira de documentação do próprio Python explicando tudo isso aqui. Ah, como é que funciona aquele tipo annotated? Que a gente não viu como que funcionava. Então tem uma página da documentação específica explicando como ele funciona e tudo mais. Foi uma coisa que a gente deu uma passada muito por cima. Mas entender isso aqui, juntar com o Fast API pode trazer muitos ganhos e...

**[00:41:38]** É uma coisa muito interessante. Eu deixei uma nota que minha, que no futuro a minha ideia é escrever o material sobre tipagem gradual. E é isso exigiria outra campanha e tudo mais no futuro. Eu tenho muitas ressalvas sobre isso e talvez a gente fale sobre isso em outro momento. Tem outras coisas que a gente não viu do FastAPI, que são super interessantes, como tarefas em background.

**[00:42:07]** que é tipo assim, ah, eu rodei uma coisa assim, mas aí eu quero ficar resolvendo mais algumas coisas enquanto eu mando um e-mail pra alguém que ficou, sabe? Pra assim, ah, mando um duzentos falando, eu recebi sua mensagem. Mas aí depois, saca, depois a gente vai resolver isso aqui, né? Tipo assim, eu te mando um e-mail. Saca, então, fechei o pé inteiro, eu tenho um módulo de tarefas em background. Lá no apêndice B do curso, eu deixei algumas coisas aqui, né? Deixa eu...

**[00:42:40]** que a gente não viu no curso e tem bastante coisinha legal aqui. Então tem o mínimo de templates aqui. Então você precisa trabalhar com templates e tudo mais a criar uma coisa que renderiza HTML, CSS, JavaScript. Eu deixei um exemplo aqui de como fazer isso.

**[00:42:57]** Tem um negócio de tarefas em background, né? Que é processamento dessas coisas que podem acontecer depois. Ah, vou enviar uma mensagem para um sistema de mensageria e salvar uma coisa no banco depois que eu já respondi. Então, Fecha API tem umas coisas para fazer isso. Eu deixei um exemplo muito simplório aqui, muito simples, mas está aqui também, né? Eu não sei se eles chegaram a explorar os apênteses do curso, porque tem três, né? E tem isso aqui. Aí eu explico aqui da uma coisa

**[00:43:29]** Simplona, sobre isso aqui. O FESIPiA também tem outro recurso que a gente não viu, que é o Lifetime, o ciclo de eventos, que é tipo assim, ah, como fazer uma coisa que vai rodar antes, ah, a aplicação subiu, então configura umas coisas, a aplicação vai descer e configura as outras coisas, que é o Lifespan. Deixei um exemplo aqui, se implore também, mas tem muita coisa que dá para explorar aqui dentro desse universo, e aí nesse apenso eu deixei essas coisinhas.

**[00:43:58]** para serem exploradas, né? O template, essas tarefas em backgrounds e o evento de life cycle. Mais do que isso, eu recomendo que vocês tenham uma olhada na própria documentação do FASHAPI, porque tem muito mais coisa, né? E a documentação do FASHAPI, eu acho que o português, se não tiver 100% traduzido, tá quase tudo traduzido na documentação. E tem bastante coisa aqui, então...

**[00:44:31]** Tem vários recursos, recursos para aprender, as referências, a API. Então, pô, dê uma olhada aqui, tem bastante coisa caso vocês querem evoluir, mas nessa parte de Fast API tem muita coisa legal aqui. E acho que é isso, né? Tipo assim, a gente viu e vocês viram que aqui só aqui eu fui desdobrando muita coisa, né? Que tipo assim, pô.

**[00:44:58]** Tem WebSockets, eventos de ciclo de vida, tarefas em background, renderização de templates, tem muitas coisas que a gente não viu. E a gente viu muita coisa no curso. Mas a ideia era mostrar para vocês que tem esse próximo passo para dar, não é? Então, tem observabilidade, tem tarefas em background, tem GraphQL, tem WebSockets. Então, existe um universo inteiro daqui para frente, não é? Vocês olharem, entenderem e tudo mais.

**[00:45:29]** E eu espero que vocês tenham se divertido nessa jornada aí comigo, assim, né? A gente fez bastante coisa, não? Eu entendo que, saca, teve um churn, né? Uma taxa de evasão, né? Falando em português, né? Porque a gente tá no Brasil. Teve uma taxa de evasão muito grande, né? Eu entendo. Tipo, a aula, a primeira aula de configurar o ambiente, ela é um divisor de águas, não? Tipo assim. Tipo, dela pra segunda diminui 60% o número de pessoas no curso.

**[00:46:01]** Então, pô, parabéns pra quem acompanhou, chegou até o final, né? Eu sei que tem muita coisa ainda pra ver, né? Você viu que a gente viu muito, muito, né? Eu considero que a gente fez muita coisa. É projeto, é rough, é autenticação, eu não sei o que. E tudo isso é introdução, né? A gente molhou o dedinho, né? Na água, né? Pensa que a gente tá no oceano inteiro, a gente molhou o dedinho, assim, do pé.

**[00:46:30]** E foi o começo da coisa, né? Então, tipo assim, tem muito caminho pra percorrer pela frente. Eu espero que vocês se divirtam, tanto quanto eu me divirto, estudando isso e olhando isso todo o tempo, né? Saca? Então, eu espero que vocês tenham gostado disso. E agora, eu queria tirar esse momento final pra gente conversar mesmo. Eu queria entender de vocês...

**[00:46:57]** O que vocês acharam? Como é que as coisas estão rolando pra vocês? Vocês têm perguntas? Vocês gostariam de fazer? Às vezes nem é pelo do curso em si, às vezes você quer perguntar uma coisa, saca? Aproveita, tira esse momento, vamos conversar, né? É tipo assim, é a ponta do iceberg, exatamente, a gente viu é a pontinha de tudo, né? Mas tem muita coisa ainda, tem um mar, um oceano inteiro pra se explorar, né? Pra gente ver, a gente viu a parte do iceberg menos do que o que ainda tá pra fora, né?

**[00:47:29]** Eu acho que o pessoal fica bestificado com tanta informação, uns uns mesmo, que não dá nenhum like, que é isso, mano. É legal dar um like, ajuda a gente, né? Chegar mais pessoas, mas tá tudo bem. Em minha defesa o user de Windows todo o ambiente deve um desafio. E você fez muito em fazer funcionar no Windows, cara. Eu me esforcei o máximo, né? Uma das últimas coisas que eu implementei agora

**[00:47:59]** Foi essa parte do assim que não estava funcionando muito bem no Windows. Meus últimos commits foram para tentar fazer o CI funcionar com isso, né? Aqui. Ter o workflow funcionando no Windows foi um grande desafio aqui. E aí eu consegui rodar o postgres no Windows porque não funciona o Docker. Ah, foi uma rola aqui. Mas eu consegui integrar isso aqui para funcionar. Testar a última aula, testar as migrações, entender como funciona, tudo.

**[00:48:33]** Foi um esforço grande para fazer tudo funcionar no Windows. Espero que vocês tenham gostado. Espero que vocês tenham conseguido reproduzir isso de uma forma mais legal. É do sensacional. Já estou recomendando. Obrigado, mano. Eu assisti a primeira versão de Leves. Então eu só entrei em uma outra dessa nova versão. Tá tudo bem. Tá tudo bem.

**[00:49:08]** O que eu vou fazer é uma pergunta, o que é o seguinte? Você já colocaria em produção o projeto com conhecimento até aqui? É seguro e consistente e tal? Dá para colocar assim. O grande ponto é o seguinte, você vai fazer um projeto com tudo que a gente viu aqui já é o suficiente, às vezes mais do que o suficiente para fazer um projeto. O grande ponto aqui é que a gente sabe todo o suficiente com que a gente viu para fazer o projeto.

**[00:49:40]** O problema das partes que a gente não viu são as partes de colocar essa improdução, saca? Então ter que lidar com muitas requisições, ter que entender a necessidade do cliente, o que a gente aprendeu é muito técnico.

**[00:49:54]** sobre código, mas a gente não sabe o técnico sobre infra, a gente não tem aquele feeling de entender a vontade das pessoas, mas se você sabe o que você quer fazer, pode colocar no ar, o que a gente viu está certo. Mas é bom o suficiente. O problema é claro, tem aquela coisa de a infraestrutura, as outras coisas e tudo mais, você for colocar num passo o que a gente fez está mais do que o suficiente aqui.

**[00:50:24]** Ah, Julia, muito bom aprender de verdade, não com curso de IA. Obrigado, Julia, eu também acho. Eu tive que colocar na página... Alguém estava me perguntando esses dias, ah, você usou o chat GPT para escrever isso aí? Eu tive que colocar aqui, né? Tipo, tá na home do repositório aqui, né? Tipo, escrito por humano, não por IA. E é por isso que tem vários erros aqui, né?

**[00:50:54]** Ah, o Rodrigo perguntou o seguinte, se você fosse um recrutador, o que poderíamos fazer a mais nesse projeto? Pra você falar, poxa, esse cara, mina, estudou muito e fez algo bem diferente. Bom, Rodrigo, você é bem sincera contigo. Se eu fosse um recrutador, eu nem olharia o teu código. Recrutador não leia código. Mas eu entendi o seu ponto de vista, tipo assim. O que que você...

**[00:51:30]** O que você poderia fazer a mais, mano? Tipo assim, eu diria que entender o que a gente fez aqui já é muito, já é um a mais, tá ligado? Assim, a gente passou um tempo conversando sobre redes, então, entenda o que a gente viu sobre redes, mais a fundo, protocolo HTTP, como funcionam validações, JSON, sabe? Esse tipo de coisa, mais fundamental, eu acho que é o grande diferencial.

**[00:51:59]** que é o que poucas pessoas têm, é a base da coisa. Tipo assim, ah, porque que o Roof aponta uma regra como uma prática em X lugar? Entender isso. Entender o que funciona no HTTP? Ah, porque que a gente viu, fez quatro workers, ele subiu quatro, o processo, o que que tá acontecendo ali? Sabe, essas coisas pra mim são diferencial. E não o código. Sabe, eu acho que entender o porquê aquelas decisões estão sendo tomadas é muito mais importante do que ter uma coisa com...

**[00:52:29]** 50 mil funcionalidades a mais, saca? Eu considero a base o mais importante. Então, vamos ver. Parabéns, Edu, resumindo o curso. Qualidade. Obrigado pelos forços de dedicação. Pô, tamo junto. WSL não seria a mágica do negócio? Mano, nem toda PC rota WSL. Tem que lembrar sempre disso. Wagner mandou. Queria te agradecer pela sua disponibilidade, dedicar um tempo da sua vida para eu transmitir seu conhecimento. Obrigado, Wagner. Eu espero que tenha ajudado.

**[00:53:06]** O resto de perguntas seria muito complicado colocar a Clean Architecture no FESJPI. Eu tenho opiniões muito fortes sobre isso porque eu acho que Clean Architecture não é resposta para nada. Toda vez que a gente pensa em padrões, os padrões foram feitos e pensados em linguagens estáticas.

**[00:53:31]** que não são dinâmicas e linguagens compiladas, que não permitem manqueir pete, então tipo assim, eu acho que eu não quero dar minha opinião a respeito disso assim. Saca, tipo assim, pô, não é complicado de fazer, mas se eu faria, é outra pergunta, saca? E eu não quero entrar nesse lugar.

**[00:53:51]** Minha máquina é antigona, 2 cores com Windows 10, está tudo rodando. Estava certo que levantei um AVM com calim... Ah, é massa, Junior. O segredo é ir melhorando para frente. Para não ir de Ritali, não sei o que é Ritali.

**[00:54:07]** Eu deus que pergunto, a chat repete para escrever é a menos pessoas têm curiosidade sobre isso. A Julia falou adicionar open telemetry, talvez sim, é só uma coisa muito importante, mas eu acho que os fundamentos são muito mais importantes do que isso. Porque se você entender o fundamento, você vai entender por que precisa de open telemetry. Saca, é isso o ponto.

**[00:54:28]** RH não quer que você fale de código, quer que você fale de você, sim. E aí, quanto mais você conseguir colocar as coisas, a gente sai melhor do outro lado. Não dá para abraçar o mundo, galera. Conhecer pessoas de banco, infra-sec e juntar os esforços, trocar ideia, vai ser mais produtivo do que tentar fazer tudo sozinho. Exatamente. O Germano falou, eu fiz essas arquiteturas no projeto. Não recomendo. Exatamente.

**[00:55:03]** Saca, eu acho que é legal entender essas coisas de arquitetura. Eu acho que os enterprise patterns são mais importantes do que a questão de arquitetura limpa. E aí é uma coisa que você pode trazer. Pô, eu quero fazer um caso de uso aqui.

**[00:55:20]** Pô, é mais interessante. Quero fazer uma camada de serviço. É mais interessante do que ficar nesse caso, nossa, vamos colocar, transformar nosso arquivo, nosso código, que poderia ser três, três arquivos, fazer ele ficar com 25 pastas, tá ligado? Mas eu tenho uma opinião muito forte sobre isso e vai de você, assim. Se você quiser aprender sobre essas coisas, vai olhar lá o canal do Programador Llama. Ele tem uma opinião bem mais flexível a respeito disso do que eu.

**[00:55:48]** Aí o Fabrício Coelho, você perguntou se dormentoria ou consultoria, mano, eu dou aula particular para algumas pessoas, aí você quiser me manda um e-mail, o meu e-mail é o do canal aqui mesmo, e a gente conversa. É boa, tudo bem, concordo, tenta dominar tudo de tudo, só causa futuração e tem perdido, porque muita coisa você não usa, continuamente esquece, então, o Edu e você deram a espaço. Então, eu acho que é assim, mano.

**[00:56:18]** aprende o básico aprende o fundamento saca a gente tudo que a gente fez aqui é um crude saca é o básico do básico mas entender esse básico do básico saca é importante e não é entender não é fazer o básico do básico saca tipo assim

**[00:56:40]** É muito fácil fazer um API, você cria lá, cria 4, tem de ponte, bota nos decorador e faz a parada. Mas entender o porquê cada coisa tá ali é a coisa mais importante pra mim. Bom, mas só tem mais alguma coisa que vocês queiram me falar, agora é a hora. Então, a gente finaliza aqui, vai dormir, vai curtir o final de semana pra quê? Vai descansar amanhã, no sábado e domingo, fazer o TCC, né?

**[00:57:20]** Bom, eu queria dizer que estou muito feliz e muito triste ao mesmo tempo, né? Saca, faz três anos que eu estou mantendo isso aqui, eu não, eu... Sabe? Até que enfim chegou ao fim. Saca, até que enfim chegou ao fim. Então, espero que vocês tenham gostado, Saca. Diz tudo.

**[00:57:45]** Eu ainda pretendo gravar um vídeo desse material ainda, mas eu posso mortem pra explicar tudo que aconteceu na campanha, o que eu achei que foi bom, o que eu achei que não foi ruim, emitir as minhas opiniões sobre isso. Mas eu preciso dar um afastamento do material durante algumas semanas pra repensar sobre isso. Botar a caixola. Quem é um Edu fora das telinhas? Que tipo de projeto está envolvido? Cara, eu estou envolvido nesse projeto. Esse projeto é o meu projeto.

**[00:58:13]** A live de Python, como uma forma geral, é o projeto. E eu estou tocando isso aqui já faz 8 anos. Esse curso é um spin-off do que a gente costuma fazer semanalmente há 8 anos. Então, isso é eu. Eu gosto de fazer música. Não sei se vocês repararam, né? Tem o violão aqui, tem uma guitarra aqui.

**[00:58:41]** tem um sintetizador aqui, essa é minha pira, e eu gosto de fazer isso com música. Eu gosto de fazer isso de música com programação. É uma coisa que eu gosto de me divertir muito com isso. E o livro? Que livro? O livro de typing. Obrigado. Pô, valeu, mano. Valeu pelo carinho todo mundo aqui. Já tem data para 2026? Não. Essa é a última edição do curso.

**[00:59:11]** Não vai ter turma de 2026, o curso acaba esse ano. Eu vou entregar 4.1 no texto, vou fazer o Pós-Mortem e acabou, mano. Faz três anos que eu estou escrevendo esse projeto, tipo assim, eu estou cansado já. Não vai ter versão para 2026, talvez daqui cinco anos quando tudo mudar, talvez eu refaça, mas não vai ter uma versão 2026, tipo assim. Não agora.

**[00:59:44]** Pô, Edu, agora você vai ter tempo para fazer os projetos aleatórios? Sim, agora eu vou ter tempo para voltar a tocar as lives de Python semanalmente, né? É isso. Três anos, virou especialista em fazepiai, né? Mais uma jornada que termina. O que vem depois, Edu? Bom, o que vem depois tem as lives de Python, mano. Aqui, ó. Todo o cronograma das lives de Python está aqui, né?

**[01:00:18]** Eu vou mudar algumas coisas agora que eu estou mais livre com o tempo depois do pós-mortem. O cronograma vai ser alterado, mas basicamente todas as lives estão aqui, o que eu pretendo fazer até o fim do ano e as datas. Então tem gerenciadores de projeto, Polars, Bill Ertoga, NoSQL, LogFiring.

**[01:00:43]** para identificar as novidades do 3, 4, WebAssembly, para identificar o V2, o V. Então está tudo aqui. Aí tem algumas coisas, eu quero terminar aquela série de NLP que foi pausada durante o curso, tem alguns outros materiais aqui que tem data e a ideia é essa.

**[01:01:10]** Campanha coletiva é bacana, mas a pressão para construção deve ter sido fácil. Então, eu quero falar mais sobre isso no pós-mortem. Eu vou tirar umas duas semanas para pensar sobre isso e eu quero escrever o pós-mortem desse material explicando o que eu achei de ter feito isso. Foi muito dolorido para mim, cansativo. Eu gostei muito do resultado, mas eu não sei se valeu o tanto que eu apanhei nesses últimos anos por causa disso.

**[01:01:41]** Esse curso foi naruto tipo den. Se tiver mais um, vai virar bolo. Que besteira, mano. O prêmio GB vai mudar para prêmio casé, visto referência para a nova geração. É que o GB é muito mais legal, né? Porque tem um mistério, entendeu? O que é GB? O que é GB? É o mistério do prêmio GB. Saudades de pai e de inferno de pessoa no mesmo parágrafo.

**[01:02:15]** Voltaremos com projetos aleatórios, não faz três anos que eu estou todo o tempo livre que eu tenho, eu estou escrevendo isso aqui. Então, a ideia é voltar com isso. Eu... E aí, eu quero fazer uma pergunta aqui para vocês, para quem está aqui. Vocês chegaram aqui por causa do curso, tem alguém que não conhecia o canal antes e tudo mais? Tipo, vocês chegaram aqui para ver o curso e tudo mais? Como é que foi essa experiência para vocês?

**[01:02:49]** E para a volta, né, que eu tô falando de mudar as datas, eu já tô com as coisas planejadas aqui do que eu quero fazer, do que eu não quero fazer. E aí, eu tô vendo pra fazer agora, depois que eu voltar a tirar esses dias, pra falar de plug-in, que é o sistema de plug-in, sobre o Bane, sobre o FastStream, e fazer uma live sobre a internacionalização que eu tô querendo fazer há muito tempo. Garba de bolegto. Muito bom, muito bom. Estou acompanhando curto somente no site, por texto. Estou perdendo muita coisa nas lives. Pô, nas lives tem as perguntas, mano.

**[01:03:24]** E as perguntas, Wilkman, levam às vezes as coisas para um lado que não tem no texto, saca? Muita coisa. Então, tem bastante coisa diferente aqui. Basicamente, tudo o que a gente fez é o que está no texto. Mas, às vezes, a forma muda. Então, não acho que está perdendo, mas tem coisas. E os 30 dias de pai. 30 dias de pai não acabaram, né? Tipo assim.

**[01:03:50]** Uma fatalidade, né? Tipo assim... Nesse período eu acabei perdendo a minha mãe, né? Então meio que eu fiquei sem terminar os 30 dias de Python, né? Eu conheci o canal no curso do ano passado, Caminho Sem Volta. Cheguei através do PyCode, ó, que massa, que legal. Do quando eu ficar milionário com a minha API bala, eu vou te financiar pra todo ano ter curto de FSH. Não faz isso comigo, você me odeia? Você... É fã ou reita, né? Tipo assim. É fã ou reita, né? Tipo assim.

**[01:04:23]** Então, para quem está aqui, para quem chegou no final, eu quero fazer um convite para vocês, para vocês entrarem lá no grupo do Telegram, no grupo da live de Python mesmo, que é o foco aqui do canal e tudo mais. Então, entrem aí, lá a gente troca muita ideia, conversa sobre tudo de Python, não tem o esquema fechado do Curio de Fast API.

**[01:04:52]** E é a base para onde saem os conteúdos que vem daqui, né? A gente passa e fica discutindo sobre vários assuntos, então apareçam por lá. Que mais eu queria fazer? Eu queria deixar um beijo para vocês, né? Todo mundo parou com as perguntas, então obrigado pelo carinho de vocês, todo mundo que acompanhou o curso. Tem pessoas que talvez não voltem mais, então valeu por acompanhar. Façam o TCC e a gente se vê daqui alguns dias.

**[01:05:23]** Eu quero tirar uns dias pra dar uma relaxada. Tirar essa pressão desses três anos descrevendo isso aqui. E... A gente se vê. Um beijo pra vocês. Ó. E valeu por acompanharem essa jornada aqui junto comigo. Ó. Valeu, galerinha. Até mais.

