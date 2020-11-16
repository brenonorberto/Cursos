class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print('Foi sacado:',quant)
        else:
            print('Erro no Deposito!!!')

    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print('Saldo Insuficiente!!!')
        else:
            self.saldo -= quant
            print('Foi sacado:', quant)

    def consultar_saldo(self):
        return self.saldo