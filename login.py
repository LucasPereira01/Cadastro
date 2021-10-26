from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser


# Criar Nossa Janela
janela = Tk()
janela.title("Coffe Brange - Acess Panel")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="icons/coffee-beans.png.ico")


# =====Carregando imagens======
logo = PhotoImage(file="icons/coffee.png")


# ========widgets========
FrameEsquerdo = Frame(janela, width=200, height=300,
                      bg="saddle brown", relief="raise")
FrameEsquerdo.pack(side=LEFT)
FrameDireita = Frame(janela, width=395, height=300,
                     bg="saddle brown", relief="raise")
FrameDireita.pack(side=RIGHT)

LogoLabel = Label(FrameEsquerdo, image=logo, bg="saddle brown")
LogoLabel.place(x=50, y=100)

UsuarioLabel = Label(FrameDireita, text="Login:",  font=(
    "Century Gothic", 20), bg="saddle brown", fg="white")
UsuarioLabel.place(x=5, y=100)

SenhaLabel = Label(FrameDireita, text="Senha:", font=(
    "Century Gotic", 20), bg="saddle brown", fg="white")
SenhaLabel.place(x=5, y=150)

UsuarioEntry = ttk.Entry(FrameDireita, width=32)
UsuarioEntry.place(x=100, y=110)

SenhaEntry = ttk.Entry(FrameDireita, width=32, show="*")
SenhaEntry.place(x=100, y=160)




def bdLogin():
    login = UsuarioEntry.get()
    senha = SenhaEntry.get()
    if(login == "" or senha == ""):
        messagebox.showerror(title="Login Info",
                             message="Preencha todos os Campos")
    else:
        DataBaser.cursor.execute("""
         SELECT * FROM Cliente
         WHERE (Login = ? AND Senha = ?)
         """, (login, senha))
        VerificaLogin = DataBaser.cursor.fetchone()
        try:
            if(login in VerificaLogin and senha in VerificaLogin):
                UsuarioLabel.place(x=5000)
                UsuarioEntry.place(x=5000)
                SenhaLabel.place(x=5000)
                SenhaEntry.place(x=5000)
                BotaoLogin.place(x=5000)
                BotaoCadastro.place(x=5000)
                btnlogout = ttk.Button(
                    FrameDireita, text="Sair", width=20, command=janela.destroy)
                btnlogout.place(x=150, y=250)

        except:
            messagebox.showerror(title="Login Info",
                                 message="Login ou Senha Invalida!!")


# ====Botoes===
BotaoLogin = ttk.Button(FrameDireita, text="Login", width=20, command=bdLogin)
BotaoLogin.place(x=140, y=225)


def btnCadastro():
  # removendo Widgets de login
    BotaoLogin.place(x=5000)
    BotaoCadastro.place(x=5000)

    NomeLabel = Label(FrameDireita, text="Nome:", font=(
        "Century Gothic", 20), bg="saddle brown", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(FrameDireita, width=32)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(FrameDireita, text="Email:", font=(
        "Century Gotic", 20), bg="saddle brown", fg="white")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(FrameDireita, width=32)
    EmailEntry.place(x=100, y=66)

    def SalvarBanco():
        nome = NomeEntry.get()
        email = EmailEntry.get()
        login = UsuarioEntry.get()
        senha = SenhaEntry.get()

        if(nome == "" or email == "" or login == "" or senha == ""):
            messagebox.showerror(
                title="Erro", message="Não Deixe Campo Vazio. Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO CLIENTE(Nome, Email, Login, Senha) values(?, ?, ?, ?)
            """, (nome, email, login, senha))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Informações de Cadastro",
                                message="Cadastro Efetuado com Sucesso")

    BotaoSalvar = ttk.Button(FrameDireita, text="Salvar",
                             width=20, command=SalvarBanco)
    BotaoSalvar.place(x=50, y=250)

    def VoltarLogin():
        # removendo  Widgets do cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        BotaoSalvar.place(x=5000)
        Voltar.place(x=5000)
        # Trazendo  de volta Widgets  do login
        BotaoLogin.place(x=140, y=225)
        BotaoCadastro.place(x=170, y=260)

    Voltar = ttk.Button(FrameDireita, text="Voltar",
                        width=20, command=VoltarLogin)
    Voltar.place(x=210, y=250)


BotaoCadastro = ttk.Button(
    FrameDireita, text="Cadastro", width=9, command=btnCadastro)
BotaoCadastro.place(x=170, y=260)

janela.mainloop()
