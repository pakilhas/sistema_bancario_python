
def menu():
     
    menu = '''
    ========== MENU ==========
    [mu] **MENU DO USUARIO**
    [d] Depositar
    [s] Sacar
    [e] Extrato
    
    [q] SAIR
    ========== Bank ==========


    '''
    return input(menu)

def menu2():
    menu2 = '''
    ========== MENU ==========
    [c] Criar Usuario
    [cc] Criar Conta
    [e] Lista Conta
    [v] Voltar
    
    
    ========== Bank ==========
    '''
    return input(menu2)

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
        print("Saldo Indisponivel".center(30,"#"))
        print(f"Saldo Disponivel: R$ {saldo}")

    elif valor > limite:
        print("Limite maximo de saque é R$ 500 ")

    elif numero_saques >= limite_saques:
        print("Limite de Saque atingido".center(30,"#")) 

    elif valor > 0:
        saldo -= valor
        numero_saques = numero_saques +  1
        print("Saque realizado com sucesso".center(30,"#"))   

    else:
        print("Apenas valores positivos são permitidos")

    return saldo, extrato, numero_saques   
   
def extrato_exibir (saldo, /, *, extrato, limite, numero_saques ):
    extrato += f"Em conta: R$ {saldo:.2f}\n Limite de Saque: R$ {limite:.2f}\n Quantidade de Saques diario: {numero_saques}\n"
    print(extrato)
    
    return saldo, extrato

def criar_usuario(nome, cpf, usuarios, conta, agencia,/):
    if cpf in usuarios:
        print("Erro: CPF já cadastrado.")
        return None
    
    usuarios[cpf] = nome
    conta[0] += 1
    print(f"Usuário {nome.upper()}\nAgencia: {agencia}\nConta: {conta}\n Cadastrado com sucesso.".title())
    return nome, cpf, conta

def criar_conta(nome, cpf, usuarios, conta, agencia,/):

    if  cpf in usuarios:
        print("Usuario já possui conta")
        conta[0] += 1
        print(f"Usuário {nome.upper()}\nAgencia: {agencia}\nConta: {conta}\ncadastrado com sucesso.".title())
        print()

    else:
        print("Usuario não tem conta ")
        menu2()    
    
    
    return nome, cpf, conta

def val_user():
    usuarios = {}
    agencia = "0001"
    conta = [0]
    
    while True:
        opcao = menu2()
        if opcao == "c":
            nome = str(input("Informe o Nome: "))
            data_nas = str(input("Informe a Data de Nascimento: "))
            cpf = str(input("Informe o CPF: "))
            endereco = str(input("Informe o Endereço: "))
            usuario = criar_usuario(nome, cpf, usuarios, conta, agencia)
            if usuario:
                print(f"Usuário {usuario[0].upper()} com CPF: {usuario[1].upper()} foi adicionado.")

        if opcao == "cc":
            nome = str(input("Informe o Nome: "))
            cpf = str(input("Informe o CPF: "))
            usuario = criar_conta(nome, cpf, usuarios, conta, agencia)
            print()
            if usuario:
                print(f"Usuário {usuario[0].upper()} com CPF: {usuario[1].upper()} foi adicionado.")
        
        elif opcao == "v" :
            menu()

        elif opcao == "q":
            break

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
        
        elif opcao == "mu" :
            val_user()
        
        elif opcao == "q" :
            break
            
main()