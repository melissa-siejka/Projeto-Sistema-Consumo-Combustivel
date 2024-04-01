from tkinter import *
from tkinter import messagebox
from datetime import *
from urllib.parse import quote
from sqlalchemy.orm import Session, mapped_column, Mapped, session
from sqlalchemy import VARCHAR, Date, NUMERIC, ForeignKey, CHAR
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.schema import Sequence
import sys
sys.path.append(r"C:\Users\mayqu\Dropbox\PC\Documents\Projetos visual Studeo\Telas")
from Telas.CadastroPessoa import Pessoa
from ConectBD.ConexaoBancoDeDados import Base


class PostoConvenido(Base):
    __tablename__ = 'PostoConveniado'
    CDPosto:Mapped[float]=mapped_column(NUMERIC(6),Sequence('POSTO_CONVENIADO_SEQ'),nullable=False, primary_key=True, unique=True)
    DTConvenio:Mapped[date]=mapped_column(Date,nullable=False)
    DTDesviculo:Mapped[date]=mapped_column(Date)
    INAtivo:Mapped[str]=mapped_column(CHAR(1))
    IDPessoa:Mapped[float]=mapped_column(NUMERIC(7,2), ForeignKey(Pessoa.id_pessoa), nullable=False)


    def CadastroPosto(self, id_pessoa, nm_posto, cnpj,  dt_convenio ):
        NovoPosto = PostoConvenido(id_pessoa = id_pessoa, 
                                   nm_posto = nm_posto,
                                   cnpj = cnpj, 
                                   dt_convenio = dt_convenio )
        Session.add(NovoPosto)
        Session.commit()
        return NovoPosto

def CadastrarPosto():
    id_pessoa = EntryIDpessoa.get()
    nm_posto = EntryNMPosto.get()
    cnpj = EntryCnpj.get()
    dt_convenio = EntryDTConvenio.get()


    try:
        novoPosto = PostoConvenido()
        novoPosto.CadastroPosto(id_pessoa = id_pessoa,
                                nm_posto = nm_posto, 
                                cnpj = cnpj,
                                dt_convenio = dt_convenio)
        messagebox.showinfo("Cadastro", f"Posto Cadastrado com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar o tipo do veículo : {str(e)}")


janela = Tk()
janela.geometry("800x900")
janela.title("Cadastro de Pessoas")
janela.configure(bg="#c5E0B4")
janela.iconbitmap("Imagens\icone_coamo.ico")
#img = PhotoImage(file="imagens\imagemcoamo.png")
#Label(janela, image=img).pack()


titulo_tela = Label(janela, text="Cadastro De Posto", bg="#c5E0B4", font=("Arial", 20), fg="black")
titulo_tela.grid(row=100,column=50)

titulo_tela = Label(janela, text="Coamo", bg="#c5E0B4", font=("Arial", 120), fg="#1B492B")
titulo_tela.grid(row=600,column=200)  


LabelNomeP = Label(janela, text="Nome Do Posto", bg="#c5E0B4", font=("Arial", 14), fg="black")
LabelNomeP.place(x=15,y=100) 
EntryIDpessoa = Entry(janela)
EntryIDpessoa.grid(row=15, column=130)

labelCNPJ= Label(janela, text="CNPJ", bg="#c5E0B4", font=("Arial", 14), fg="black")
labelCNPJ.place(x=15,y=150) 
EntryNMPosto = Entry(janela)
EntryNMPosto.grid(row=15, column=180)

labelCodigoP = Label(janela, text="Codigo", bg="#c5E0B4", font=("Arial", 14), fg="black")
labelCodigoP.place(x=15,y=200 ) 
EntryCnpj = Entry(janela)
EntryCnpj.grid(row=15, column=230)

labelData= Label(janela, text="Data", bg="#c5E0B4", font=("Arial", 14), fg="black")
labelData.place(x=15,y=250) 
EntryDTConvenio = Entry(janela)
EntryDTConvenio.grid(row=0, column=1)

botao_sair = Button(janela, text="Sair", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B")
botao_sair.place(x=350, y=500)

botao_cadastrar = Button(janela, text="Salvar", padx=50, pady=10, bd=5, font=("Arial", 12), bg="#1B492B", command=CadastrarPosto)
botao_cadastrar.place(x=15, y=500)


janela.mainloop()

