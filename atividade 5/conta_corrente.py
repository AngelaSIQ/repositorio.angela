from conta_bancaria import Conta_bancaria

class conta_corrente(Conta_bancaria):
    def  __init__(self, titular, cpf, saldo=0, numerocc=None):
        super().__init__(self, titular, cpf, saldo)
        self.numerocc = numerocc


    def mostrarcc(self):
        return f"titular: {self.titular}, cpf: {self.cpf}, numero da conta: {self.numerocc}, saldo: {self.saldo:.2f} "
