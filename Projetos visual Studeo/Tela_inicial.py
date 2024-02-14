#from tkinter import Tk, Label, Button, Entry, Pack, Place, PhotoImage
from tkinter import *
from Tela_de_cadastro import Tela_cadastro
import os
# criando janela inicial 
janela = Tk()
janela.geometry("1100x600")
janela.title("Tela Inicial")
janela.configure(bg="#C0C0C0")
janela.iconbitmap("imagens\Iconecoamo.ico")
img = PhotoImage(file="imagens\imagemcoamo.png")
Label(janela, image=img).pack()

# caminho imagem C:\Users\mayqu\Pictures\Saved Pictures\imagemcoamo
# Titulo da janela Inicial
meulabel = Label(janela, text="Seja Bem Vindo Como posso te ajuada?", font=("Arial", 16 ), fg="black", bg="#FFFFFF" )
meulabel.place(x=300,y=50) 

#botao de cadastro
botao_cadastra = Button(janela, text="Cadastrar Veiculo", padx=21, bg="#C0C0C0", pady=10,
                      font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
botao_cadastra.place(x=100,y=100) 


#botao de consulta
botao_consultar = Button(janela, text="consulta", bg="#C0C0C0", padx=55, pady=10, 
                         font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
botao_consultar.place(x=100,y=170) 


#botao de cadstro de informacoes de abastecimeno
botao_inf_abastecimento = Button(janela, text="inf Abastecimento", bg="#C0C0C0", padx=20, pady=10, 
                                 font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
botao_inf_abastecimento.place(x=100,y=240)  

# botao Cadastrar rotas
botao_sair = Button(janela, text="Cadastrar Rotas", bg="#C0C0C0", padx=25, pady=10, 
                    font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
botao_sair.place(x=100,y=310)  


#botao sair
botao_sair = Button(janela, text="sair", bg="#C0C0C0", padx=50, pady=10, 
                    font=("Arial", 12, "bold"), bd=5, highlightthickness=0)
botao_sair.place(x=100,y=380)  



janela.mainloop()