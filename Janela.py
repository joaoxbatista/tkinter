#-*- coding:latin1 -*-
#Authors: Joao Batista Gomes Silva, Erick Oliveira de Souza
#Github: jhonxbatista
#E-mails: jhonxbatista@gmail.com, erickdynsouza@hotmail.com

from Tkinter import *
import sys
from Conta import Conta

#Color
danger_color = "#E74C3C"
success_color = "#2ECC71"
primary_color = "#3498DB"
warning_color = "#E67E22"
dark_color = "#2C3E50"
light_color = "#ECF0F1"

class MainWindow():

	#Construct method
	def __init__(self, contas = {}):

		self.window = Tk()
		self.contas = contas
		#1 - Setting attributes of window
		self.caption = "Banc System - UFAL"
		self.width = 720
		self.height = 480
		self.left = 150
		self.top = 20

		self.background = dark_color
		
		#2 - Setting configuration
		self.window.minsize(self.width, self.height)
		self.window.maxsize(self.width, self.height)
		
		self.window.title(self.caption)
		self.window['bg'] = self.background
		self.window.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.left)+"+"+str(self.top))

		#3 - Setting Objects and Layout

		#3.1 - Labels
		lb_title = Label(self.window, text="Banc System - Universidade Federal de Alagoas", bg=self.background, fg=light_color, font=("Helvetica", 16), pady=40, padx=120)
		
		#3.2 - Buttons
		btn_create =  Button(self.window, text="Criar conta", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.conta)
		btn_consult =  Button(self.window, text="Saldo", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.saldo)
		btn_saki =  Button(self.window, text="Saque", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.saque)
		btn_deposit =  Button(self.window, text="Deposito", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.deposito)
		btn_extract =  Button(self.window, text="Extrato", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.extrato)
		btn_exit =  Button(self.window, text="Sair", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.sair)

		#Draw
		lb_title.grid(row=0, column=0)
		btn_create.grid(row=1, column=0, pady=10)
		btn_consult.grid(row=2, column= 0, pady=10)
		btn_deposit.grid(row=3, column=0, pady=10)
		btn_saki.grid(row=4, column=0, pady=10)
		
		btn_extract.grid(row=4, column=0, pady=10)
		btn_exit.grid(row=5, column=0, pady=10)
		
		#Main Loop Window
		self.window.mainloop()

	#Action Obter Saldo
	def getSaldo(self, numero, mensagem):
		status = 0
		for numero_conta in self.contas:
	 		if numero.get() == numero_conta:
				
	 			mensagem['text'] = self.contas[numero_conta].sald()
	 			mensagem['bg'] = light_color
	 			status = 1
		
		if status != 1:
			mensagem['text'] = "Conta inexistente!"
			mensagem['fg'] = light_color
	 		mensagem['bg'] = danger_color
		
				
	#Action Criar Conta
	def criarConta(self, numero, mensagem):
		try: 
			for numero_conta in self.contas:
				if numero.get() == numero_conta:
					raise ValueError

			conta = Conta(numero.get(), 0)
			self.contas[numero.get()] = conta

			texto = "Cadastro Realizado com Sucesso!"
			cor = success_color

		except ValueError:
			texto = "Conta já existente!"
			cor = danger_color

		mensagem['text'] = texto
		mensagem['bg'] = cor
		mensagem['fg'] = light_color
	#Action Depositar
	def depositar(self, numero, valor, mensagem):
		try: 
			for numero_conta in self.contas:
				if numero.get() == numero_conta:
					
					self.contas[numero_conta].deposito(float(valor.get()))
					self.contas[numero_conta].addHistorico('Deposito', float(valor.get()))

					texto = "Deposito Realizado com Sucesso!"
					cor = success_color

		except ValueError:
			texto = "Erro ao realizar deposito!"
			cor = danger_color

		mensagem['text'] = texto
		mensagem['bg'] = cor
		mensagem['fg'] = light_color

		# for numero in self.contas:
		# 	print self.contas[numero]

	#Action Sacar
	def sacar(self, numero, valor, mensagem):
		try: 
			for numero_conta in self.contas:
				if numero.get() == numero_conta:
					
					self.contas[numero_conta].saque(float(valor.get()))
					self.contas[numero_conta].addHistorico('Saque', float(valor.get()))
					texto = "Saque Realizado com Sucesso!"
					cor = success_color

		except ValueError:
			texto = "Erro ao realizar saque!"
			cor = danger_color

		mensagem['text'] = texto
		mensagem['bg'] = cor
		mensagem['fg'] = light_color
		# for numero in self.contas:
		# 	print self.contas[numero]

	#Action Gerar Extrato
	def gerarExtrato(self, numero, mensagem):
		try: 
			for numero_conta in self.contas:
				if numero.get() == numero_conta:
					
					texto = self.contas[numero_conta].extrato()
					cor = light_color

		except ValueError:
			texto = "Erro ao realizar saque!"
			cor = danger_color

		mensagem['text'] = texto
		mensagem['bg'] = cor

	#-----------------------------------------

	#Janela Conta
	def conta(self):

		self.window = Tk()
		self.caption = "Banc System - Criar conta"
		self.width = 720
		self.height = 480
		self.left = 150
		self.top = 20

		self.background = dark_color
		self.color_label = "#fff"
		#2 - Setting configuration
		self.window.minsize(self.width, self.height)
		self.window.maxsize(self.width, self.height)
		
		self.window.title(self.caption)
		self.window['bg'] = self.background
		self.window.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.left)+"+"+str(self.top))


		#3 - Setting Objects and Layout

		#3.1 - Labels
		lb_title = Label(self.window, text="Banc System - Criar conta", bg=self.background, fg=self.color_label, font=("Helvetica", 16), pady=40, padx=220)
		lb_ent_number = Label(self.window, text="Insira o numero da conta",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		lb_msg = Label(self.window, text="", fg=dark_color, bg=dark_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		
		#3.3 - Buttons
		btn_create = Button(self.window, text="Create", width=29, bg=success_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=lambda:self.criarConta(ent_number, lb_msg))
		
		#Draw
		lb_title.grid(row=0, column=0)
		lb_msg.grid(row=1, column=0, ipadx=85, ipady=12, pady=10)
		lb_ent_number.grid(row=2, column=0)
		ent_number.grid(row=3, column=0, ipady=5, ipadx=5, pady=20)
		btn_create.grid(row=4, column=0)

		#Main Loop Window
		self.window.mainloop()

	#Janela Saque
	def saque(self):

		self.window = Tk()
		
		#1 - Setting attributes of window
		self.caption = "Banc System - Saque"
		self.width = 720
		self.height = 480
		self.left = 150
		self.top = 20

		self.background = dark_color
		self.color_label = "#fff"

		#2 - Setting configuration
		self.window.minsize(self.width, self.height)
		self.window.maxsize(self.width, self.height)
		
		self.window.title(self.caption)
		self.window['bg'] = self.background
		self.window.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.left)+"+"+str(self.top))

		#3 - Setting Objects and Layout

		#3.1 - Labels
		lb_title = Label(self.window, text="Banc System - Saque", bg=self.background, fg=self.color_label, font=("Helvetica", 16), pady=40, padx=260)
		
		lb_ent_number = Label(self.window, text="Insira o número da conta",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		lb_ent_value = Label(self.window, text="Insira o valor a ser retirado",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		
		lb_msg = Label(self.window, text="", fg=dark_color, bg=dark_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		ent_value = Entry(self.window, width=30)
		#3.3 - Buttons
		btn_create = Button(self.window, text="Confirmar", width=29, bg=success_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=lambda:self.sacar(ent_number, ent_value, lb_msg))
		
		#Draw
		lb_title.grid(row=0, column=0)

		lb_msg.grid(row=1, column=0, ipadx=85, ipady=12, pady=10)

		lb_ent_number.grid(row=2, column=0)
		ent_number.grid(row=3, column=0, ipady=5, ipadx=5, pady=10)
		
		lb_ent_value.grid(row=4, column=0)
		ent_value.grid(row=5, column=0, ipady=5, ipadx=5, pady=10)

		btn_create.grid(row=6, column=0, pady=10)

		#Main Loop Window
		self.window.mainloop()

	#Janela Deposito
	def deposito(self):

		self.window = Tk()
		
		#1 - Setting attributes of window
		self.caption = "Banc System - Desposito"
		self.width = 720
		self.height = 480
		self.left = 150
		self.top = 20
		self.background = dark_color
		self.color_label = light_color

		#2 - Setting configuration
		self.window.minsize(self.width, self.height)
		self.window.maxsize(self.width, self.height)
		
		self.window.title(self.caption)
		self.window['bg'] = self.background
		self.window.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.left)+"+"+str(self.top))

		#3 - Setting Objects and Layout

		#3.1 - Labels
		lb_title = Label(self.window, text="Banc System - Deposito", bg=self.background, fg=self.color_label, font=("Helvetica", 16), pady=40, padx=220)
		
		lb_ent_number = Label(self.window, text="Insira o numero da conta",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		lb_ent_value = Label(self.window, text="Insira o valor a ser retirado",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		
		lb_msg = Label(self.window, text="", fg=dark_color, bg=dark_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		ent_value = Entry(self.window, width=30)

		#3.3 - Buttons
		btn_deposit = Button(self.window, text="Confirmar", width=29, bg=success_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=lambda:self.depositar(ent_number, ent_value, lb_msg))
		
		#Draw
		lb_title.grid(row=0, column=0)
		lb_msg.grid(row=1, column=0, ipadx=85, ipady=12, pady=5)
		
		lb_ent_number.grid(row=2, column=0)
		ent_number.grid(row=3, column=0, ipady=5, ipadx=5, pady=5)
		
		lb_ent_value.grid(row=4, column=0)
		ent_value.grid(row=5, column=0, ipady=5, ipadx=5, pady=5)

		btn_deposit.grid(row=6, column=0, pady=20)

		#Main Loop Window
		self.window.mainloop()

	#Janela Saldo
	def saldo(self):

		self.window = Tk()
		
		#1 - Setting attributes of window
		self.caption = "Banc System - Saldo"
		self.width = 720
		self.height = 480
		self.left = 150
		self.top = 20

		self.background = dark_color
		self.color_label = "#fff"

		#2 - Setting configuration
		self.window.minsize(self.width, self.height)
		self.window.maxsize(self.width, self.height)
		
		self.window.title(self.caption)
		self.window['bg'] = self.background
		self.window.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.left)+"+"+str(self.top))

		#3 - Setting Objects and Layout

		#3.1 - Labels
		lb_title = Label(self.window, text="Banc System - Saldo", bg=self.background, fg=self.color_label, font=("Helvetica", 16), pady=40, padx=220)
		lb_ent_number = Label(self.window, text="Insira o numero da conta",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		lb_saldo = Label(self.window, text="Seu saldo aqui", fg=dark_color, bg=light_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		
		#3.3 - Buttons
		btn_consult = Button(self.window, text="Consultar", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=lambda:self.getSaldo(ent_number, lb_saldo))
		
		#Draw
		lb_title.grid(row=0, column=0)

		lb_ent_number.grid(row=1, column=0)
		ent_number.grid(row=2, column=0, ipady=5, ipadx=5, pady=10)
		lb_saldo.grid(row=4, column=0, ipadx=85, ipady=12, pady=10)
		btn_consult.grid(row=3, column=0, pady=10)

		
		#Main Loop Window
		self.window.mainloop()

	def extrato(self):

		self.window = Tk()
		
		#1 - Setting attributes of window
		self.caption = "Banc System - Extrato"
		self.width = 720
		self.height = 480
		self.left = 150
		self.top = 20

		self.background = dark_color
		self.color_label = "#fff"

		#2 - Setting configuration
		self.window.minsize(self.width, self.height)
		self.window.maxsize(self.width, self.height)
		
		self.window.title(self.caption)
		self.window['bg'] = self.background
		self.window.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.left)+"+"+str(self.top))

		#3 - Setting Objects and Layout

		#3.1 - Labels
		lb_title = Label(self.window, text="Banc System - Emissao de extrato", bg=self.background, fg=self.color_label, font=("Helvetica", 16), pady=40, padx=220)
		lb_ent_number = Label(self.window, text="Insira o numero da conta",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		lb_extract = Label(self.window, text="Resultado do extrato aqui", fg=dark_color, bg=light_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		
		#3.3 - Buttons
		btn_gerar = Button(self.window, text="Gerar", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=lambda:self.gerarExtrato(ent_number, lb_extract))
		
		#Draw
		lb_title.grid(row=0, column=0)

		lb_ent_number.grid(row=1, column=0)
		ent_number.grid(row=2, column=0, ipady=5, ipadx=5, pady=10)
		
		lb_extract.grid(row=4, column=0, ipadx=85, ipady=12, pady=10)

		btn_gerar.grid(row=3, column=0, pady=10)
		
		#Main Loop Window
		self.window.mainloop()

	def sair(self):
		sys.exit()
	
