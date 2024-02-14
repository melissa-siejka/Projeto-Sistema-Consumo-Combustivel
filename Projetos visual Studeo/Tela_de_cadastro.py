#from tkinter import Tk, Label, Button, Entry, Place
from tkinter import *
def Tela_cadastro():
    janela = Tk()
    janela.geometry("1200x600")
    janela.title("Cadatro de veiculos")
    janela.configure(bg="#C0C0C0")
    janela.iconbitmap("imagens\Iconecoamo.ico")
#    img = PhotoImage(file="imagens\imagemcoamo.png")
#    Label(janela, image=img).pack()


    titulo_tela = Label(janela, text="Cadastre as informaçõe do veiculo", bg="#D3D3D3", font=("Arial", 16), fg="black")
    titulo_tela.place(x=500,y=50) 


    botao_sair = Button(janela, text="Salvar", padx=50, pady=10, bd=5, )
    botao_sair.place(x=500, y=500)

    botao_cadastrar = Button(janela, text="Gravar", padx=50, pady=10, bd=5)
    botao_cadastrar.place(x=50, y=500)


    label_placa = Label(janela, text="Placa do Veiculo:", bg="#D3D3D3", font=("Arial", 14), fg="black")
    label_placa.place(x=15,y=100) 
    input_placa = Entry(janela)
    input_placa.place(x=15, y=150)

    label_frota = Label(janela, text="Número Frota:", bg="#D3D3D3", font=("Arial", 14), fg="black")
    label_frota.place(x=200,y=100) 
    input_frota = Entry(janela)
    input_frota.place(x=200, y=150)

    tipo_modelo = Label(janela, text="Modelo:", bg="#D3D3D3", font=("Arial", 14), fg="black")
    tipo_modelo.place(x=15,y=200 ) 
    input_modelo = Entry(janela)
    input_modelo.place(x=15, y=250)

    tipo_de_combustivel = Label(janela, text="Combústivel:", bg="#D3D3D3", font=("Arial", 14), fg="black")
    tipo_de_combustivel.place(x=0,y=400) 
    input_modelo = Entry(janela)
    input_modelo.place(x=25, y=450)

    istatus = Label(janela, text="Istatus", bg="#D3D3D3", font=("Arial", 14), fg="black")
    istatus.place(x=0,y=320) 
    istatus = Entry(janela)
    istatus.place(x=25, y=350)
    janela.mainloop()

Tela_cadastro()