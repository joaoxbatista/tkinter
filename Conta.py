#-*- coding:latin1 -*-
#Authors: Joao Batista Gomes Silva, Erick Oliveira de Souza
#Github: jhonxbatista
#E-mails: jhonxbatista@gmail.com, erickdynsouza@hotmail.com

class Conta:

	def __init__(self, numero = None, saldo = None):

		self.numero = numero
		self.saldo = saldo
		self.historico = []
	def __str__(self):
		return "Numero da Conta: "+self.numero+"\nSaldo: "+str(self.saldo)

	def deposito(self, valor):
		if valor > 0:
			self.saldo += valor
		else: 
			raise ValueError

	def saque(self, valor):
		if valor > 0 and (self.saldo-valor) >=0:
			self.saldo -= valor

		else:
			raise ValueError

	def extrato(self):
		string = "Numero da conta: "+str(self.numero)+"\n"
		
		for operacao in self.historico:
			string += operacao+"\n" 

		return string
	def saldo(self):
		print self.saldo

	def addHistorico(self, tipo, valor):
		operacao = "-------------------------------------------\nOperação: "+str(tipo)+" Valor: "+str(valor)+"\n-------------------------------------------"
		self.historico.append(operacao)
		
