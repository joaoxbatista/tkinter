class Conta:

	def __init__(self, numero = None, saldo = None):

		self.numero = numero
		self.saldo = saldo

	def __str__(self):
		return "Numero da Conta: "+self.numero+"\nSaldo: "+str(self.saldo)

	def deposito(self, valor):
		if valor > 0:
			self.saldo += valor
			return "Valor depositado com sucesso"
		else: 
			return "Valor de deposito invalido"

	def saque(self, valor):
		if valor > 0 and (self.saldo-valor) >=0:
			self.saldo -= valor
			return "Saque realizado com sucesso"

		else:
			return "Erro ao realizar saque"

	def extrato(self):
		print self

	def saldo(self):
		print self.saldo
		