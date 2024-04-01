from ConectBD.ConexaoBancoDeDados import Veiculo
from tkinter import *
def TelaCadastroVeiculo():
    janela = Tk()
    janela.geometry("1200x600")
    janela.title("Cadastro de veiculos")
    janela.configure(bg="#c5E0B4")
    janela.iconbitmap("Imagens\icone_coamo.ico")
#    img = PhotoImage(file="imagens\imagemcoamo.png")
#    Label(janela, image=img).pack()


    titulo_tela = Label(janela, text="Cadastro De Veiculos", bg="#c5E0B4", font=("Arial", 20), fg="black")
    titulo_tela.place(x=100,y=50)

    titulo_tela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
    titulo_tela.place(x=600,y=200)  


    botao_sair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    botao_sair.place(x=350, y=450)

    botao_cadastrar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
    botao_cadastrar.place(x=300, y=450)


    LabelPlaca = Label(janela, text="Placa:", bg="#c5E0B4", font=("Arial", 14), fg="black")
    LabelPlaca.place(x=15,y=100) 
    InputiPlaca = Entry(janela)
    InputiPlaca.place(x=15, y=130)

    DT_Aquisicao = Label(janela, text="Data Aquisição:", bg="#c5E0B4", font=("Arial", 14), fg="black")
    DT_Aquisicao .place(x=15,y=150) 
    inputDataAqui = Entry(janela)
    inputDataAqui.place(x=15, y=180)

    DataBaixa = Label(janela, text="Data De Baixa:", bg="#c5E0B4", font=("Arial", 14), fg="black")
    DataBaixa.place(x=15,y=200 ) 
    inputDataBaixa = Entry(janela)
    inputDataBaixa.place(x=15, y=230)

    CapacidadeTanque = Label(janela, text="Capacidade Tanque", bg="#c5E0B4", font=("Arial", 14), fg="black")
    CapacidadeTanque.place(x=15,y=250) 
    inputCapaciTanque = Entry(janela)
    inputCapaciTanque.place(x=15, y=280)

    istatus = Label(janela, text="Istatus", bg="#c5E0B4", font=("Arial", 14), fg="black")
    istatus.place(x=15,y=400) 
    inputIstatus = Entry(janela)
    inputIstatus.place(x=15, y=430)

    CodTipoVeic = Label(janela, text="Modelo Veiculo:", bg="#c5E0B4", font=("Arial", 14), fg="black")
    CodTipoVeic.place(x=15,y=300) 
    inputTipoVeic = Entry(janela)
    inputTipoVeic.place(x=15, y=330)

    CodTipoVeic = Label(janela, text="Codigo Combustivel:", bg="#c5E0B4", font=("Arial", 14), fg="black")
    CodTipoVeic.place(x=15,y=350) 
    inputTipoComb = Entry(janela)
    inputTipoComb.place(x=15, y=380)


    janela.mainloop()

    return InputiPlaca, inputDataAqui, inputDataBaixa, inputCapaciTanque , inputIstatus, inputTipoVeic, inputTipoComb


novoveiculo = Veiculo(InputiPlaca, inputDataAqui )