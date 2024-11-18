# Sistema de Gerenciamento de Inventário

## Visão Geral do Projeto
Este é um sistema de gerenciamento de inventário desenvolvido em Django que permite o controle de produtos, pedidos e funcionários. O sistema possui autenticação de usuários e diferentes funcionalidades para gerenciamento de estoque.

## Arquitetura do Sistema
O projeto é construído usando o framework Django e segue uma arquitetura MVC (Model-View-Controller). Está organizado em dois principais aplicativos:

1. **Dashboard**: Responsável pela funcionalidade principal do sistema
2. **User**: Gerencia autenticação e registro de usuários

### Estrutura de Diretórios
```
inventoryproject/
├── dashboard/           # Aplicativo principal
├── user/               # Aplicativo de autenticação
├── templates/          # Templates HTML
├── static/             # Arquivos estáticos
└── asert/             # Assets administrativos
```

## Funcionalidades

### 1. Gerenciamento de Produtos
- Cadastro de produtos com nome, categoria e quantidade
- Categorias disponíveis:
  - Papelaria
  - Eletrônico
  - Alimento
- Visualização de estoque atual

### 2. Sistema de Pedidos
- Criação de pedidos vinculados a produtos
- Registro automático de data e hora
- Associação com funcionário responsável
- Controle de quantidade solicitada

### 3. Gestão de Usuários
- Registro de novos usuários
- Sistema de login personalizado
- Logout seguro
- Proteção de rotas por autenticação

## Esquema do Banco de Dados

### Modelo: Product
```python
- name: CharField(max_length=100)
- category: CharField(choices=['Papelaria', 'Eletronico', 'Alimento'])
- quantity: PositiveIntegerField
```

### Modelo: Order
```python
- product: ForeignKey(Product)
- staff: ForeignKey(User)
- order_quantity: PositiveIntegerField
- date: DateTimeField(auto_now_add=True)
```

## Sistema de Autenticação

### Formulários
1. **CreateUserForm**
   - Campos: username, email, password1, password2
   - Herda de UserCreationForm

2. **LoginForm**
   - Campos personalizados para username e password
   - Interface em português
   - Estilização com classes Bootstrap

### Fluxo de Autenticação
1. Registro de usuário com validação de dados
2. Redirecionamento para dashboard após registro bem-sucedido
3. Sistema de login com mensagens de feedback
4. Proteção de rotas com decorator @login_required

## Instalação e Configuração

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install django
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

## Guia de Uso

### Acessando o Sistema
1. Acesse http://localhost:8000
2. Faça login ou registre uma nova conta
3. Acesse o dashboard principal

### Gerenciando Produtos
1. Acesse a seção "Produtos"
2. Adicione novos produtos com nome, categoria e quantidade
3. Visualize o estoque atual

### Criando Pedidos
1. Acesse a seção "Pedidos"
2. Selecione o produto desejado
3. Informe a quantidade
4. Confirme o pedido

### Visualizando Relatórios
1. Acesse o dashboard principal para visualizar estatísticas
2. Verifique histórico de pedidos
3. Monitore níveis de estoque

## Segurança
- Todas as rotas do dashboard são protegidas por autenticação
- Senhas são armazenadas com criptografia
- Sistema de sessão seguro
- Proteção contra CSRF em formulários

## Manutenção
- Backup regular do banco de dados recomendado
- Monitoramento de logs para identificar problemas
- Atualização regular das dependências para segurança