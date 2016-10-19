#-*- coding:latin1 -*-
#Author: Joao Batista Gomes Silva
#Github: jhonxbatista
#E-mail: jhonxbatista@gmail.com

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

	def contaController(self, numero, mensagem):
		conta = Conta(numero.get(), 0)
		
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
		lb_msg = Label(self.window, text="Conta criada com sucesso!", fg=self.color_label, bg=danger_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		
		#3.3 - Buttons
		btn_create = Button(self.window, text="Create", width=29, bg=success_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=lambda:self.contaController(ent_number, lb_msg))
		
		#Draw
		lb_title.grid(row=0, column=0)
		lb_msg.grid(row=1, column=0, ipadx=85, ipady=12, pady=10)
		lb_ent_number.grid(row=2, column=0)
		ent_number.grid(row=3, column=0, ipady=5, ipadx=5, pady=20)
		btn_create.grid(row=4, column=0)

		#Main Loop Window
		self.window.mainloop()

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
		lb_title = Label(self.window, text="Banc System - Saque", bg=self.background, fg=self.color_label, font=("Helvetica", 16), pady=40, padx=220)
		lb_ent_value = Label(self.window, text="Insira o valor a ser retirado",fg=self.color_label, bg=self.background, font=("Helvetica", 12), pady=5)
		lb_msg = Label(self.window, text="Saque realizado com sucesso!", fg=self.color_label, bg=danger_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		
		#3.3 - Buttons
		btn_create = Button(self.window, text="Create", width=29, bg=success_color, fg=light_color, height=2, highlightthickness=0,bd=0)
		
		#Draw
		lb_title.grid(row=0, column=0)
		lb_msg.grid(row=1, column=0, ipadx=85, ipady=12, pady=10)
		lb_ent_value.grid(row=2, column=0)
		ent_number.grid(row=3, column=0, ipady=5, ipadx=5, pady=10)
		btn_create.grid(row=4, column=0)

		#Main Loop Window
		self.window.mainloop()

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
		
		lb_msg = Label(self.window, text="Saki successfully", fg=self.color_label, bg=danger_color)
		
		#3.2 - Entry
		ent_number = Entry(self.window, width=30)
		ent_value = Entry(self.window, width=30)

		#3.3 - Buttons
		btn_deposit = Button(self.window, text="Confirmar", width=29, bg=success_color, fg=light_color, height=2, highlightthickness=0,bd=0)
		
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
		btn_confirm = Button(self.window, text="Gerar", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0)
		
		#Draw
		lb_title.grid(row=0, column=0)

		lb_ent_number.grid(row=1, column=0)
		ent_number.grid(row=2, column=0, ipady=5, ipadx=5, pady=10)
		
		lb_extract.grid(row=4, column=0, ipadx=85, ipady=12, pady=10)

		btn_confirm.grid(row=3, column=0, pady=10)
		
		#Main Loop Window
		self.window.mainloop()

	def sair():
		sys.exit()

	#Construct method
	def __init__(self, contas = None):

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
		btn_consult =  Button(self.window, text="Saldo", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0)
		btn_saki =  Button(self.window, text="Saque", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.saque)
		btn_deposit =  Button(self.window, text="Deposito", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.deposito)
		btn_extract =  Button(self.window, text="Extrato", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.extrato)
		btn_exit =  Button(self.window, text="Sair", width=29, bg=primary_color, fg=light_color, height=2, highlightthickness=0,bd=0, command=self.sair)

		#Draw
		lb_title.grid(row=0, column=0)
		btn_create.grid(row=1, column=0, pady=10)
		btn_deposit.grid(row=3, column=0, pady=10)
		btn_saki.grid(row=2, column=0, pady=10)
		
		btn_extract.grid(row=4, column=0, pady=10)
		btn_exit.grid(row=5, column=0, pady=10)
		
		#Main Loop Window
		self.window.mainloop()

	