Projeto desenvolvido para a disciplina de Topicos Especiais de Informatica da FATEC Ribeirão Preto

Alunos:
* Aline Mizumukai
* Caio Damasceno Pellicani

<br>

---

### Para executar utilize o comandando : `flask run`

---

<br>
## Requisitos

* Implementar uma aplicação que contenha pelo menos dez interfaces gráficas (UI).
    - O tipo de UI pode ser definido pelos integrantes: Console, Formulário ou Web.

* Armazenar dados de maneira persistente utilizando o SGBD da sua preferência.
    - Os dados precisam ser armazenados em pelo menos três tabelas.
    - Para cada tabela codificar na UI no mínimo três operações, dentre elas: Insert, Update, Delete e/ou Select.

* Elaborar, necessariamente, as seguintes UI:
    - Login: em que o usuário deverá fornecer um  nome de usuário  e uma  senha. O acesso as funcionalidades do sistema ocorrem apenas para usuários previamente cadastrados.

    - Sobre:   que   apresente   dados   do   projeto   {tema   escolhido   e   objetivo}   e   dosdesenvolvedores: {nome completo e código de matrícula}.

    - Menu: em que o usuário poderá escolher a opção desejada da aplicação.

* Implementar uma funcionalidade que exporta todos os dados da aplicação no formato JSON. O arquivo deve ser compactado no formato zip.

* Implementar uma funcionalidade para importa dados.
    - Os dados devem ser disponibilizados em um endereço da web.
    - Usar o módulo Requests ou URLlib.
    - Armazenar os dados importados em uma tabela.o
    - Apresentar os dados importados em uma UI da aplicação.