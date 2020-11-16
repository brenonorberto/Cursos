from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Breno', '123.456.789-10', 39)


conta1 = Conta(cliente1, 10.00, 1000)

print(conta1.cliente.nome, conta1.consultar_saldo())

conta1.depositar(1000)

print(conta1.consultar_saldo())

conta1.sacar(1500)

print(conta1.consultar_saldo())