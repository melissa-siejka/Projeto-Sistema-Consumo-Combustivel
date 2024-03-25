from tkinter import Tk, Label, Button, Entry, Place
from tkinter import *
def Consulta():
    janela = Tk()
    janela.geometry("800x600")
    janela.title("Tela Inicial")
    janela.configure(bg="#8ab54e")
    janela.iconbitmap("Imagens\icone_coamo.ico")
    img = PhotoImage(file="Imagens\imagemcoamo.png")
    Label(janela, image=img).pack()

    janela.mainloop()
Consulta()