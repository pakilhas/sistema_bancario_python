class Cliente:
    
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []  


    def get_contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        for conta in self._contas:
            print(conta)
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nasc):
        super().__init__(endereco) 
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc

    def get_cpf(self,endereco):

        if endereco == "itajai":
            print('moramos em itajai') 
        else:
            print('mora em outro lugar')
       
        return self._cpf

    def get_nome(self):
        return self._nome

    def get_data_nasc(self):
        return self._data_nasc

class Conta:
    conta_counter = 1 

    def __init__(self):
        self._num = Conta.conta_counter
        Conta.conta_counter += 1  
        self._saldo = 0

    def get_num(self):
        return self._num

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de {valor} realizado com sucesso. Novo saldo: {self._saldo}')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            print(f'Saque de {valor} realizado com sucesso. Novo saldo: {self._saldo}')
        else:
            print('Valor de saque inválido ou saldo insuficiente.')

class MenuPrincipal:

    def __init__(self, opcao=None):
       
        self._opcao = opcao
        self._clientes = []  

    def get_menu_principal(self):
        return self._opcao
    
    def set_menu_principal(self, vopcao):
        self._opcao = vopcao
    
    def executar_menu(self):
        if self._opcao == 'c':
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            data_nasc = input("Digite a data de nascimento do cliente: ")
            cliente = PessoaFisica(endereco, cpf, nome, data_nasc)  
            conta = Conta()  
            cliente.adicionar_conta(conta)  
            self._clientes.append(cliente) 
            print(f"Cliente {cliente.get_nome()} criado com sucesso. Conta nº {str(conta.get_num())} criada.")
        elif self._opcao == 'd':
            cliente_nome = input("Digite o nome do cliente: ")
            for cliente in self._clientes:
                if cliente.get_nome() == cliente_nome:
                    conta_num = int(input("Digite o número da conta: "))
                    for conta in cliente.get_contas():
                        if conta.get_num() == conta_num:
                            valor_deposito = float(input("Digite o valor do depósito: "))
                            conta.depositar(valor_deposito)
                            break
                    else:
                        print("Conta não encontrada.")
                    break
            else:
                print("Cliente não encontrado.")
        elif self._opcao == 's':
            cliente_nome = input("Digite o nome do cliente: ")
            for cliente in self._clientes:
                if cliente.get_nome() == cliente_nome:
                    conta_num = int(input("Digite o número da conta: "))
                    for conta in cliente.get_contas():
                        if conta.get_num() == conta_num:
                            valor_saque = float(input("Digite o valor do saque: "))
                            conta.sacar(valor_saque)
                            break
                    else:
                        print("Conta não encontrada.")
                    break
            else:
                print("Cliente não encontrado.")
        elif self._opcao == 'l':
            for cliente in self._clientes:
                cliente.listar_contas()
        elif self._opcao == 'q':
            print("Saindo...")
        else:
            print("Opção inválida.")

men = MenuPrincipal()
while True:
    menop = input('''
    ========== MENU ==========
    [c] Criar Cliente e Conta
    [d] Realizar Depósito
    [s] Realizar Saque
    [l] Listar Clientes e Contas
    [q] SAIR
    ========== Bank ==========
    Escolha uma opção: ''')

    men.set_menu_principal(menop)

    men.executar_menu()

    if menop == 'q':
        break  
