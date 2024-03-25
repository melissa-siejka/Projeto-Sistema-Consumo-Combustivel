from tkinter import *
# from CadastroUnidade import TelaCadastroUnidade
# from CadastroVeiculo import TelaCadastroVeiculo


tela = Tk()
tela.title("Tela Inicial")
tela.geometry("500x500")
tela.configure(background="#dde")


def cadastrar():
    pass


BarraDeMenu = Menu(tela)
menuCadastro = Menu(BarraDeMenu, tearoff=0)
menuCadastro.add_command(label="Cadastro de Veículo", )
menuCadastro.add_command(label="Cadastro de Motorista",)
menuCadastro.add_command(label="Cadastro de Unidade", )
menuCadastro.add_separator()
menuCadastro.add_command(label="Fechar", command=tela.quit)
BarraDeMenu.add_cascade(label="Cadastro", menu=menuCadastro)
tela.config(menu=BarraDeMenu)

tela.mainloop()


