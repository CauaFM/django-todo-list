Introdução
O presente documento apresenta o desenvolvimento do projeto ToDo App, uma aplicação web criada com o objetivo de simplificar o gerenciamento de tarefas diárias.
A solução foi construída utilizando o framework Django, que permite o desenvolvimento ágil de aplicações web estruturadas, seguras e escaláveis. O sistema também incorpora HTML e CSS para a interface visual, buscando clareza e usabilidade.
Este documento descreve o propósito da aplicação, sua implementação, tecnologias utilizadas, funcionalidades principais, estrutura de diretórios e instruções de execução.




2. Objetivo do Projeto
O ToDo App foi desenvolvido com os seguintes objetivos:
•	Criar uma aplicação web funcional para gerenciamento de tarefas pessoais.
•	Implementar autenticação completa de usuários (login, logout e cadastro).
•	Garantir que cada usuário possua sua própria lista de tarefas.
•	Demonstrar, na prática, os conceitos fundamentais da disciplina:
o	Arquitetura de Software
o	Padrões de projeto aplicados ao Django
o	Organização modular em camadas
o	Estruturação de componentes web
Além disso, o projeto visa aplicar boas práticas de design e usabilidade, fornecendo uma experiência moderna e intuitiva.


4. Tecnologias Utilizadas

Tecnologia	                                                        Descrição
Python 3	                                                  Linguagem usada no backend
Django 5	                                                  Framework para criação da aplicação
SQLite3 	                                                  Banco de dados padrão do Django
HTML5 & CSS3	                                              Estrutura e estilização das páginas
Poppins (Google Fonts)	                                    Identidade visual da aplicação
Git & GitHub	                                              Versionamento e hospedagem do código
VS Code	                                                    Ambiente de desenvolvimento





4.Funcionalidades Principais
  4.1 Sistema de Autenticação
•	Cadastro de usuários
•	Login
•	Logout
•	Rotas protegidas para impedir acesso de visitantes
•	Interface personalizada para telas de autenticação
  4.2 Gerenciamento Completo de Tarefas (CRUD)
•	Criar tarefas
•	Listar tarefas
•	Editar título
•	Deletar tarefas
•	Marcar como concluída
•	Identificação do usuário dono da tarefa
•	Organização visual intuitiva
  4.3 Interface Moderna
•	Paleta de cores suaves (gradiente azul)
•	Cards centralizados
•	Botões estilizados
•	Animações leves
•	Layout responsivo




5.Estrutura do Projeto
Padrão Django:
todo_project/
   ├── accounts/         → Sistema de login/registro/logout
   ├── todo/             → Lógica das tarefas
   ├── templates/        → Arquivos HTML (estruturados e reutilizáveis)
   ├── db.sqlite3        → Banco de dados
   ├── manage.py         → Comando principal da aplicação

6.Descrição dos Componentes
6.1 Models
O arquivo todo/models.py contém o modelo Task, responsável por armazenar:
•	título da tarefa
•	status (concluída ou não)
•	data de criação
•	usuário relacionado
6.2 Views
Tratam:
•	Regras de negócios
•	Renderização de templates
•	Controle de autenticação
•	Processamento dos formulários
•	Ações de CRUD
6.3 Templates
•	login.html – Tela de autenticação
•	register.html – Tela de cadastro
•	index.html – Lista principal de tarefas
•	update.html – Edição de tarefas
•	delete.html – Confirmação de exclusão
•	base.html – Layout geral reutilizado




7.Como Executar o Projeto

2) Instalar dependências
pip install Django

3) Aplicar migrações
python manage.py migrate

4) Rodar o servidor
python manage.py runserver

5) Acessar no navegador
http://127.0.0.1:8000/


8. Conclusão
O ToDo App demonstra de forma clara e funcional os conteúdos trabalhados na disciplina Arquitetura de Software e Computação em Nuvem.
O projeto implementa uma aplicação real com:
•	Estrutura bem organizada
•	Separação entre camadas
•	Código versionado no GitHub
•	Interface moderna
•	Funcionalidades completas de CRUD e autenticação
