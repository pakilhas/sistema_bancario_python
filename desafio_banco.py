
def menu():
     
    menu = '''
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [m] Sair
    ========== Bank ==========


    '''
    return input(menu)

def depositar (saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("deposito realizado com sucesso")
        print(f"saldo atual R$:{saldo:.2f}")
        print("Depositado".center(30, "#"))
        print(extrato)

    else:
        print("Apenas Valores Positivos")
    
    return saldo, extrato

def sacar (*,saldo, valor, extrato, limite, limite_saques, numero_saques):
    if valor > saldo:
        print("Saldo Indisponivel")
        print(extrato)

    elif valor > limite:
        print("Limite maximo de saque é R$ 500 ")

    elif numero_saques >= limite_saques:
        print("Limite de Saque atingido") 

    elif valor > 0:
        saldo -= valor
        numero_saques = numero_saques +  1
        print("Saque realizado com sucesso")   

    else:
        print("Apenas valores positivos são permitidos")

    return saldo, extrato, numero_saques       

   


def extrato_exibir (saldo, /, *, extrato, limite, numero_saques ):
    extrato += f"Em conta: R$ {saldo:.2f}\n Limite de Saque: R$ {limite:.2f}\n Quantidade de Saques diario: {numero_saques}\n"
    print(extrato)
    

    return saldo, extrato

def main ():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
       
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
            
        
        elif opcao == "s" :
            #print(saldo)
            valor = float(input("Valor que deseja sacar: "))                
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite= limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)

        elif opcao == "e" :
            saldo, extrato = extrato_exibir(saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
            
main()
