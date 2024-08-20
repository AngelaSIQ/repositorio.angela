class Conta_bancaria:
    def __init__(self, titular, cpf, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo

    def mostra_conta(self):
        return f"titular: {self.titular}, cpf: {self.cpf}, Saldo: {self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito {valor:.2f}, Saldo atualizado{self.saldo:.2f}"
        else:
            return "Valor inválido!"

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque {valor:.2f}, Saldo atualizado:{self.saldo:.2f}"
        else:
            return "valor inválido"

    def verificar_saldo(self):
        return f"Saldo {self.saldo:.2f}"


class Conta_corrente(Conta_bancaria):
    def __init__(self, titular, cpf, saldo=0, numerocc=None):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc

    def mostrarcc(self):
        return f"titular: {self.titular}, cpf: {self.cpf}, Número conta Corrente: {self.numerocc}, Saldo: {self.saldo:.2f}"


class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, saldo=0, rendimento=0.02):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        return f"Rendimento: {self.rendimento * 100:.2f}% "

    def render(self):
        self.saldo += self.saldo * self.rendimento
        return f"Rendimento bem sucedido Saldo atualizado: {self.saldo:.2f}"


def criar_conta_corrente(contas):
    titular = input("titular: ")
    cpf = input("CPF: ")
    numerocc = input("Número conta corrente: ")
    contas[cpf] = Conta_corrente(titular, cpf, numerocc=numerocc)
    return "sucesso!"


def criar_conta_poupanca(contas):
    titular = input("titular: ")
    cpf = input("CPF:")
    contas[cpf] = Conta_poupanca(titular, cpf)
    return "sucesso!"


def depositar(contas):
    cpf = input("CPF: ")
    if cpf in contas:
        valor = float(input("Valor do deposito: "))
        return contas[cpf].depositar(valor)
    else:
        return "Conta invalida!"


def sacar(contas):
    cpf = input("CPF: ")
    if cpf in contas:
        valor = float(input("Valor sacado:"))
        return contas[cpf].sacar(valor)
    else:
        return "Conta invalida!"


def verificar_saldo(contas):
    cpf = input("cpf: ")
    if cpf in contas:
        return contas[cpf].verificar_saldo()
    else:
        return "Conta invalida!"


def ver_rendimento(contas):
    cpf = input("CPF: ")
    if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
        return contas[cpf].ver_rendimento()
    else:
        return "Conta invalida!"


def aplicar_rendimento(contas):
    cpf = input("CPF: ")
    if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
        return contas[cpf].render()
    else:
        return "Conta Poupanca invalida!"


def menu(contas):
    while True:

        print("\nMenu:")

        print("1. Conta Corrente")

        print("2. Conta Poupança")

        print("3. Depositar")

        print("4. Sacar")

        print("5. Verificar Saldo")

        print("6. Verificar Rendimento")

        print("7. Aplicar Rendimento")

        print("8. Sair")

        opcao = input("digite uma opção: ")

        if opcao == '1':

            print(criar_conta_corrente(contas))

        elif opcao == '2':

            print(criar_conta_poupanca(contas))

        elif opcao == '3':

            print(depositar(contas))

        elif opcao == '4':

            print(sacar(contas))

        elif opcao == '5':

            print(verificar_saldo(contas))

        elif opcao == '6':

            print(ver_rendimento(contas))

        elif opcao == '7':

            print(aplicar_rendimento(contas))

        elif opcao == '8':

            print("Saindo...")
            break

        else:
            
            print("Opção inválida")


if __name__ == "__main__":
    contas = {}  
    menu(contas)     