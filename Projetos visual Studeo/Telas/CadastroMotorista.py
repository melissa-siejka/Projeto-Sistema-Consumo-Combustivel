from tkinter import *
def TelaCadastroMotorista():
    janela = Tk()
    janela.geometry("800x900")
    janela.title("Cadastro de veiculos")
    janela.configure(bg="#c5E0B4")
    janela.iconbitmap("Imagens\icone_coamo.ico")
#    img = PhotoImage(file="imagens\imagemcoamo.png")
#    Label(janela, image=img).pack()


    titulo_tela = Label(janela, text="Cadastro De Abastecimento", bg="#c5E0B4", font=("Arial", 20), fg="black")
    titulo_tela.place(x=100,y=50)

    titulo_tela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
    titulo_tela.place(x=600,y=200)  


    BotaoSair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    BotaoSair.place(x=350, y=550)

    BotaoSalvar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    BotaoSalvar.place(x=15, y=550)


    LabelRequizicao = Label(janela, text="Número da Requizição", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelRequizicao.place(x=15,y=100) 
    InputiPlaca = Entry(janela)
    InputiPlaca.place(x=15, y=130)

    LabelFrota = Label(janela, text="Frota Do Veiculo", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelFrota.place(x=15,y=150) 
    InputFrota = Entry(janela)
    InputFrota.place(x=15, y=180)

    LabelMatricula = Label(janela, text="Matricula do Motorista", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelMatricula.place(x=15,y=200 ) 
    InputiMatricula = Entry(janela)
    InputiMatricula.place(x=15, y=230)

    LabelCodPosto = Label(janela, text="Codigo Do Posto", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelCodPosto.place(x=15,y=250) 
    InputCodPosto = Entry(janela)
    InputCodPosto.place(x=15, y=280)

    LabelHodometro = Label(janela, text="Hodomettro Do Veículo", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelHodometro.place(x=15,y=300) 
    InputHodometro = Entry(janela)
    InputHodometro.place(x=15, y=330)

    LabelCodConbustivel = Label(janela, text="Codigo  Do Cobustivel", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelCodConbustivel.place(x=15,y=350) 
    InputCodCombustivel = Entry(janela)
    InputCodCombustivel.place(x=15, y=380)

    LabelIstatus = Label(janela, text="Valor", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelIstatus.place(x=15,y=400) 
    InputIstatus = Entry(janela)
    InputIstatus.place(x=15, y=430)

    LabelQantLitro = Label(janela, text="Quantidade de Litros ", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelQantLitro.place(x=15,y=450) 
    InputQantlitro = Entry(janela)
    InputQantlitro.place(x=15, y=480)

    LabelData = Label(janela, text="Data ", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelData.place(x=15,y=500) 
    InputData = Entry(janela)
    InputData.place(x=15, y=530)


    janela.mainloop()

TelaCadastroMotorista()