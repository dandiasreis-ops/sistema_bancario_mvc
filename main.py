#MODEL
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def exibir_dados(self):
        return {
            "nome": self.cliente.nome,
            "cpf": self.cliente.cpf,
            "saldo": self.saldo
        }

class BancoDados:
    def __init__(self):
        self.contas = [] #lista que simula o banco de dados com a lista de contas

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        return self.contas
    
#VIEW
class View:

    @staticmethod
    def ler_dados_cliente(): #método de entrada pros dados
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        saldo = float(input("Digite o saldo inicial: "))
        return nome, cpf, saldo

    @staticmethod
    def exibir_conta(dados):
        print("\n--- Conta Criada ---")
        print(f"Nome: {dados['nome']}")
        print(f"CPF: {dados['cpf']}")
        print(f"Saldo: R$ {dados['saldo']:.2f}")
        print("--------------------\n")

    @staticmethod
    def exibir_todas_contas(contas):
        print("\n--- Lista de Contas ---")
        for conta in contas:
            dados = conta.exibir_dados()
            print(f"Nome: {dados['nome']} | CPF: {dados['cpf']} | Saldo: R$ {dados['saldo']:.2f}")
        print("------------------------\n")

#CONTROLLER
class Controller:
    def __init__(self):
        self.banco = BancoDados()  #instancia o "banco"

    def criar_conta(self):
        #recebe dados da View
        nome, cpf, saldo = View.ler_dados_cliente()

        #cria objetos do Model
        cliente = Cliente(nome, cpf)
        conta = Conta(cliente, saldo)

        #salva no banco (Model)
        self.banco.adicionar_conta(conta)

        #mostra na View
        View.exibir_conta(conta.exibir_dados())

    def listar_contas(self):
        contas = self.banco.listar_contas()
        View.exibir_todas_contas(contas)

#MAIN
def main():
    controller = Controller()

    while True:
        print("1 - Criar Conta")
        print("2 - Listar Contas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.criar_conta()

        elif opcao == "2":
            controller.listar_contas()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()