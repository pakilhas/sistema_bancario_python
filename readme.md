# Opa, sou o Pakilhas
| Rede Social |                                            |
|-------------|-----------------------------|

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pablo-carvalho-93927a220/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=fff)](https://www.instagram.com/pablo_ddh/) [![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=fff)](https://discord.com/channels/1235957312477466717/1235957313076985858)
[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pakilhas)

[![DIO](https://img.shields.io/badge/D%20I%20O-%23FFF100?style=for-the-badge&logo=digitalocean&logoColor=black)](https://web.dio.me/users/pakilhas?tab=achievements)



# Sistema Bancário em Python V1.0

Este é um script em Python para simular operações básicas em um sistema bancário. Atualmente, o sistema suporta apenas um usuário (nome de usuário: `usuario`) e oferece funcionalidades como depósito, saque e visualização de extrato.

## Funcionalidades

O script oferece as seguintes funcionalidades:

1. **Depositar:** Permite ao usuário fazer depósitos em sua conta. O valor do depósito é armazenado e refletido no saldo da conta.

2. **Sacar:** O usuário pode fazer saques, com um limite de 3 saques diários e um máximo de R$500 por saque. Os valores dos saques são deduzidos do saldo da conta.

3. **Extrato:** Mostra o extrato da conta, exibindo os depósitos e saques realizados, bem como o saldo atual da conta.

## Uso

Ao executar o script, o usuário é solicitado a inserir seu nome de usuário. Atualmente, o único nome de usuário aceito é `usuario`. Após inserir o nome de usuário, o menu é exibido com as opções disponíveis. O usuário pode escolher uma opção digitando o número correspondente.

## Exemplo de Uso

```python
digite o nome do usuario: usuario

========== MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
========== Bank ==========

1
Deposito
Valor a ser Depositado: 100
deposito realizado com sucesso
saldo atual R$ 100
##########Depositado##########

2
Saldo disponivel:  R$100
Digite o Valor do Saque: 50
Saque realizado com sucesso
Saldo Atual: R$ 50
##############Saque#############

3
##########Extrato##########
Ultimo deposito Realizado: R$100
Valor do Saque: R$50
Saldo Atual: R$50
##########Extrato##########
```
Este script é um projeto de teste e pode ser expandido para incluir recursos adicionais, como autenticação de usuário mais robusta, histórico de transações e suporte para múltiplos usuários.
