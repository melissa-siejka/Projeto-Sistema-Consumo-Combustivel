from tkinter import *
def TelaCadastroUnidade():
    janela = Tk()
    janela.geometry("800x900")
    janela.title("Cadastro de veiculos")
    janela.configure(bg="#c5E0B4")
    janela.iconbitmap("Imagens\icone_coamo.ico")
#    img = PhotoImage(file="imagens\imagemcoamo.png")
#    Label(janela, image=img).pack()


    titulo_tela = Label(janela, text="Cadastro De Unidade", bg="#c5E0B4", font=("Arial", 20), fg="black")
    titulo_tela.place(x=100,y=50)

    TituloTela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
    TituloTela.place(x=250,y=200)  


    LabelPlaca = Label(janela, text="Codigo:", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelPlaca.place(x=15,y=100) 
    InputiPlaca = Entry(janela)
    InputiPlaca.place(x=15, y=130)

    label_frota = Label(janela, text="CNPJ", bg="#c5E0B4", font=("Arial", 14), fg="black")
    label_frota.place(x=15,y=150) 
    input_frota = Entry(janela)
    input_frota.place(x=15, y=180)

    tipo_modelo = Label(janela, text="Nome", bg="#c5E0B4", font=("Arial", 14), fg="black")
    tipo_modelo.place(x=15,y=200 ) 
    input_modelo = Entry(janela)
    input_modelo.place(x=15, y=230)

    tipo_de_combustivel = Label(janela, text="Minicipio", bg="#c5E0B4", font=("Arial", 14), fg="black")
    tipo_de_combustivel.place(x=15,y=250) 
    input_combustivel = Entry(janela)
    input_combustivel.place(x=15, y=280)

    tipo_de_veiculo = Label(janela, text="Endereço", bg="#c5E0B4", font=("Arial", 14), fg="black")
    tipo_de_veiculo.place(x=15,y=300) 
    input_tipo_veic = Entry(janela)
    input_tipo_veic.place(x=15, y=330)

    capacidade_tanque = Label(janela, text="Cep", bg="#c5E0B4", font=("Arial", 14), fg="black")
    capacidade_tanque.place(x=15,y=350) 
    input_capa_tanque = Entry(janela)
    input_capa_tanque.place(x=15, y=380)

    istatus = Label(janela, text="Istatus", bg="#c5E0B4", font=("Arial", 14), fg="black")
    istatus.place(x=15,y=400) 
    istatus = Entry(janela)
    istatus.place(x=15, y=430)

    data_cadstro = Label(janela, text="Data de Cadasto ", bg="#c5E0B4", font=("Arial", 14), fg="black")
    data_cadstro.place(x=15,y=450) 
    input_data_cad = Entry(janela)
    input_data_cad.place(x=15, y=480)

    BotaoSalvar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    BotaoSalvar.place(x=15, y=580)

    BotaoSair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    BotaoSair.place(x=450, y=580)



    janela.mainloop()

TelaCadastroUnidade()