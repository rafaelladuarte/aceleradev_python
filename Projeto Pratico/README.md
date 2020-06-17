# Central de Erros

## Objetivo
Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. 
Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação 
(backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante 
que os desenvolvedores possam centralizar todos os registros de erros em um local, 
de onde podem monitorar e tomar decisões mais acertadas. 
Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.

A arquitetura do projeto é formada por:

### Backend - API
- criar endpoints para serem usados pelo frontend da aplicação
- criar um endpoint que será usado para gravar os logs de erro em um banco de dados relacional
- a API deve ser segura, permitindo acesso apenas com um token de autenticação válido

### Frontend
- deve implementar as funcionalidades apresentadas nos wireframes
- deve ser acessada adequadamente tanto por navegadores desktop quanto mobile
- deve consumir a API do produto
- desenvolvida na forma de uma Single Page Application

## Observações
- Se a aceleração tiver ênfase no backend (Java, Python, C#, Go, PHP, etc) a equipe deve obrigatoriamente 
implementar a API. A implementação do frontend não é necessária
- Se a aceleração tiver ênfase em frontend (React, Vue, Angular, etc) a equipe deve obrigatoriamente implementar 
o frontend da aplicação e o backend pode ser substituido por uma aplicação mock. A implementação da API não é 
necessária, caso o time deseje podem ser utilizados mocks.

## Wireframes
Os wireframes a seguir servem para ilustrar as funcionalidades básicas que a aplicação deverá ter, 
porém o time terá total liberdade para definir os detalhes de implementação e estratégia a ser utilizada 
no desenvolvimento.

### Cadastro

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/1-cadastro.png"/>
</p>

### Login

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/2-login.png"/>
</p>

### Dashboard

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/3-dashboard.png"/>
</p>

### Ambientes

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/4-ambientes.png"/>
</p>

### Order

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/5-order.png"/>
</p>

### Filtro

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/6-filtro.png"/>
</p>

### Detalhes

<p align="center">
<img src="https://github.com/elladarte/AceleraDev_Python/blob/master/Projeto%20Pratico/Wireframes%20Exemplos/7-detalhes.png"/>
</p>
