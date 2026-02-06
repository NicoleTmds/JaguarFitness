# Sistema de E-commerce — Jaguar Fitness

## Sobre o Projeto

O **Jaguar Fitness** é uma aplicação web que simula um sistema completo de **e-commerce**, permitindo que usuários realizem compras online de produtos fitness, desde a navegação pelos produtos até o pagamento e acompanhamento de pedidos.


A API é RESTful, utiliza autenticação JWT e foi pensada para ser consumida por um frontend web ou mobile.

---

## Funcionalidades Implementadas

### Autenticação
- Autenticação baseada em JWT.
- Proteção de rotas por usuário autenticado.
- Todas as operações são isoladas por usuário.

### Produtos
- Estrutura preparada para cadastro e gerenciamento de produtos.
- Produtos possuem preço fixado no momento da compra (snapshot).
- Proteção contra exclusão de produtos associados a pedidos.

### Carrinho de Compras
- Cada usuário possui um carrinho ativo.
- Funcionalidades:
  - adicionar produtos
  - atualizar quantidade
  - remover itens
- O carrinho **não é limpo no checkout**, apenas após pagamento aprovado.

### Endereços
- CRUD completo de endereços por usuário.
- O usuário pode:
  - criar
  - listar
  - editar
  - remover seus endereços
- Endereços são utilizados no checkout.

### Pedidos (Checkout)
- Criação de pedidos a partir do carrinho.
- Snapshot do endereço no momento do checkout.
- O pedido mantém os dados do endereço mesmo que o usuário altere ou exclua o endereço posteriormente.
- Status do pedido:
  - `pending`
  - `paid`
  - `canceled`

### Pagamentos
- Criação de pagamentos vinculados a pedidos.
- Validações de negócio:
  - apenas pedidos pendentes podem ser pagos
  - o pedido precisa ter endereço snapshotado
  - não é permitido mais de um pagamento aprovado por pedido
- Aprovação e falha de pagamento simuladas.
- Ao aprovar um pagamento:
  - o pedido é marcado como `paid`
  - o carrinho do usuário é limpo

---

## Modelagem de Dados

A persistência de dados é feita utilizando **PostgreSQL** como banco de dados relacional e o **Django ORM** para mapeamento das entidades.

### Tabela `products`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `name` | STRING | Nome do produto |
| `price` | DECIMAL | Preço do produto |
| `created_at` | DATETIME | Data de criação |

---

### Tabela `cart`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `user_id` | INTEGER | Usuário dono do carrinho |

---

### Tabela `cart_items`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `cart_id` | INTEGER | FK para cart |
| `product_id` | INTEGER | FK para products |
| `quantity` | INTEGER | Quantidade do produto |

---

### Tabela `address`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `user_id` | INTEGER | FK para usuário |
| `street` | STRING | Rua |
| `number` | STRING | Número |
| `district` | STRING | Bairro |
| `city` | STRING | Cidade |
| `state` | STRING | Estado |
| `zip_code` | STRING | CEP |
| `complement` | STRING | Complemento |

---

### Tabela `order`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `user_id` | INTEGER | FK para usuário |
| `status` | ENUM | pending, paid, canceled |
| `total_amount` | DECIMAL | Valor total |
| `street` | STRING | Snapshot da rua |
| `number` | STRING | Snapshot do número |
| `district` | STRING | Snapshot do bairro |
| `city` | STRING | Snapshot da cidade |
| `state` | STRING | Snapshot do estado |
| `zip_code` | STRING | Snapshot do CEP |
| `complement` | STRING | Snapshot do complemento |
| `created_at` | DATETIME | Data de criação |

---

### Tabela `order_items`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `order_id` | INTEGER | FK para order |
| `product_id` | INTEGER | FK para products |
| `quantity` | INTEGER | Quantidade |
| `unit_price` | DECIMAL | Preço unitário no momento da compra |

---

### Tabela `payment`

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave primária |
| `order_id` | INTEGER | FK para order |
| `method` | ENUM | pix, credit_card, debit_card |
| `status` | ENUM | pending, approved, failed |
| `amount` | DECIMAL | Valor do pagamento |
| `transaction_id` | STRING | ID da transação |
| `created_at` | DATETIME | Data de criação |

---

## Arquitetura do Backend

backend foi desenvolvido utilizando **Django** e **Django Rest Framework**, seguindo boas práticas de arquitetura, organização por domínio e regras de negócio.

apps/
 ├── address
 ├── cart
 ├── order
 ├── payment
 ├── products
 └── users


### Cada app contém:
- models.py: definição das entidades
- serializers.py: validação e serialização
- views.py: regras de negócio
- urls.py: definição das rotas


## Fluxo Principal da Aplicação

Usuário se autentica | Navega pelos produtos | Adiciona produtos ao carrinho | Gerencia endereços | Realiza checkout, criando um pedido | Cria um pagamento para o pedido | Pagamento aprovado: pedido marcado como pago; carrinho limpo; Usuário acompanha pedidos e pagamentos.


## Tecnologias Utilizadas

### Backend
Python | Django | Django Rest Framework | PostgreSQL | JWT | Docker | Docker Compose