menu = '''
========== MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
========== Bank ==========


'''
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
usuario = input("digite o nome do usuario: ")

valor_dep = 0
valor_saq = 0

while menu != 0:
       
    if usuario == "usuario":
        opcao = input(menu)

        if opcao == "1":
            print("Deposito")
            valor_dep = int(input("Valor a ser Depositado: "))
            if valor_dep > 0:
                    saldo = saldo + valor_dep
                    print("deposito realizado com sucesso")
                    print("saldo atual", saldo)
                    print("Depositado".center(30, "#"))
            else:
                print("Apenas Valores Positivos")
                

        elif opcao == "2":
            if numero_saque < LIMITE_SAQUES:
                print(f"Saldo disponivel:  {saldo}")
                valor_saq = int(input("Digite o Valor do Saque: "))
                
                if valor_saq > 0 and valor_saq <=limite: 
                    if saldo >= valor_saq:
                        saldo -= valor_saq                
                        print("Saque realizado com sucesso")
                        print(f"Saldo Atual: {saldo}")    
                        numero_saque += 1 #contator para o saque ter limite de 3  
                        print("Saque".center(30, "#"))          
                    else:
                        print("Impossivel sacar por falta de saldo")     
                else:
                    print(f"Valor do saque tem que ser maior que 0 e o Maximo {limite}")
            else:
                print("Limite de saque atingido")
            
            
        elif opcao == "3":
                print("Extrato".center(30, "#"))
                print(f"Ultimo deposito Realizado: R${valor_dep}")
                print(f"Valor do Saque: R${valor_saq}")
                print(f"Saldo Atual: R${saldo}")
                print("Extrato".center(30, "#"))
                


        elif opcao == "0":
            print("Obrigado por usar nossos servisos")
            break
        else:
             print("Opção Invalida")    
    else:
        print("usuario não cadastrado")
        break 

                                 
        
                
            
