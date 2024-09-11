# Sistema Bancário em Python V2.1 - Orientado a Objetos

Este é um script em Python para simular operações básicas de um sistema bancário, agora implementado com princípios de **Programação Orientada a Objetos (POO)**. Esta versão aprimorada introduz classes para representar **Clientes**, **Contas Bancárias** e um **Menu Principal**, permitindo uma estrutura mais flexível e expansível para futuras funcionalidades.

## Funcionalidades

O sistema oferece as seguintes operações básicas:

1. **Criar Cliente e Conta Bancária**:
   - Permite criar novos clientes do tipo **Pessoa Física** e associar contas bancárias a eles.
   - Cada cliente pode ter várias contas associadas.

2. **Depositar**:
   - Os depósitos são realizados diretamente na conta do cliente, com o valor sendo atualizado no saldo da conta.

3. **Sacar**:
   - Os saques são realizados de contas bancárias com verificação de saldo disponível.

4. **Listar Clientes e Contas**:
   - Permite visualizar todos os clientes cadastrados e suas respectivas contas bancárias.

## Estrutura do Código

O código está estruturado com as seguintes classes e métodos:

### Classes

- **`Cliente`**: Representa um cliente genérico. Possui um endereço e uma lista de contas.
  - Métodos principais: 
    - `get_contas()`: Retorna as contas associadas ao cliente.
    - `adicionar_conta(conta)`: Adiciona uma conta ao cliente.
    - `listar_contas()`: Lista todas as contas do cliente.

- **`PessoaFisica`**: Subclasse de Cliente. Representa um cliente do tipo pessoa física.
  - Atributos:
    - `cpf`, `nome`, `data_nasc`.

- **`Conta`**: Representa uma conta bancária. Cada conta tem um número único e um saldo.
  - Métodos principais:
    - `depositar(valor)`: Realiza depósito na conta.
    - `sacar(valor)`: Realiza saque da conta, verificando saldo suficiente.

- **`MenuPrincipal`**: Gerencia as opções do menu principal e controla as interações do usuário com o sistema.
  - Métodos principais:
    - `executar_menu()`: Executa as operações de acordo com a escolha do usuário.

### Exemplo de Menu

Ao executar o script, o usuário verá o seguinte menu para interagir com o sistema:

```text
    ========== MENU ==========
    [c] Criar Cliente e Conta
    [d] Realizar Depósito
    [s] Realizar Saque
    [l] Listar Clientes e Contas
    [q] SAIR
    ========== Bank ==========
    Escolha uma opção: 
```
## Melhorias Futuras
Este script pode ser expandido para incluir as seguintes funcionalidades:

    - Autenticação de usuários com senhas.
    - Histórico de transações para cada conta.
    - Suporte para múltiplos tipos de contas (ex: conta corrente, poupança).
    - Implementação de limites de saque diário por cliente.

## Exemplo de Uso

Aqui está um exemplo de como o sistema pode ser utilizado:

    - Criar um Cliente e uma Conta:
        O usuário pode criar um novo cliente e automaticamente associar uma conta bancária.


```
nome = input("Digite o nome do cliente: ")
endereco = input("Digite o endereço do cliente: ")
cpf = input("Digite o CPF do cliente: ")
data_nasc = input("Digite a data de nascimento do cliente: ")
cliente = PessoaFisica(endereco, cpf, nome, data_nasc)
conta = Conta()
cliente.adicionar_conta(conta)
print(f"Cliente {cliente.get_nome()} criado com sucesso. Conta nº {conta.get_num()} criada.")

```
## Realizar Depósito:
```
cliente_nome = input("Digite o nome do cliente: ")
for cliente in clientes:
    if cliente.get_nome() == cliente_nome:
        conta_num = int(input("Digite o número da conta: "))
        for conta in cliente.get_contas():
            if conta.get_num() == conta_num:
                valor_deposito = float(input("Digite o valor do depósito: "))
                conta.depositar(valor_deposito)
```
# Opa, 
| Rede Social |                                            |
|-------------|-----------------------------|

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pablo-carvalho-93927a220/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=fff)](https://www.instagram.com/pablo_ddh/) [![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=fff)](https://discord.com/channels/1235957312477466717/1235957313076985858)
[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pakilhas)

[![DIO](https://img.shields.io/badge/D%20I%20O-%23FFF100?style=for-the-badge&logo=digitalocean&logoColor=black)](https://web.dio.me/users/pakilhas?tab=achievements)

