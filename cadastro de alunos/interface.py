# Importando dependencia do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando main
from main import *

#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando a interface

tela = Tk()
tela.title("")
tela.geometry('810x535')

# Iniciar a interface Full Screen
#SW = tela.winfo_screenwidth()
#SH = tela.winfo_screenheight()
#tela.geometry("%dx%d+0+0" % (SW,SH))
#tela.attributes("-fullscreen", 1)

tela.configure(background=co1)
tela.resizable(width=FALSE, height=FALSE)

style = Style(tela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(tela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(tela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_dados = Frame(tela, width=800, height=100, bg=co1, relief=SOLID)
frame_dados.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(tela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Criando Frame Logo
global imagem, imagem_string, label_imagem

app_lg = Image.open('img/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de Cadastro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# Abrindo a imagem

imagem = Image.open('img/logo.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
label_imagem = Label(frame_dados, image=imagem, bg=co1, fg=co6)
label_imagem.place(x=390, y=10)

# Criando funções para CRUD
# Função Adicionar
def adicionar():
    global imagem, imagem_strings, label_imagem

    # Obtendo os valores
    nome = entrada_nome.get()
    email = entrada_email.get()
    telefone = entrada_telefone.get()
    sexo = combo_sexo.get()
    data = data_nascimento.get()
    endereco = entrada_endereco.get()
    curso = combo_curso.get()
    img = imagem_string

    lista = [nome, email, telefone, sexo, data, endereco, curso, img]

    #verificando se a lista contem valores nulos
    for i in lista:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    #Registrando os valores
    sistema_de_registro.register_student(lista)

    # Limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    combo_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    combo_curso.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('img/logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = Label(frame_dados, image=imagem, bg=co1, fg=co6)
    label_imagem.place(x=390, y=10) 

    # Mostrando os valores na tabela
    mostrar_alunos()

# Função Pesquisar Alunos
def procurar():    
    global imagem, imagem_string, label_imagem
    # Obtendo o id
    id_aluno = int(entrada_procurar.get())

    # Pesquisando aluno
    dados = sistema_de_registro.search_students(id_aluno)

    # Limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    combo_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    combo_curso.delete(0, END)

    # inserindo os valores nos campos de entradas
    entrada_nome.insert(END, dados[1])
    entrada_email.insert(END, dados[2])
    entrada_telefone.insert(END, dados[3])
    combo_sexo.insert(END, dados[4])
    data_nascimento.insert(END, dados[5])
    entrada_endereco.insert(END, dados[6])
    combo_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = Label(frame_dados, image=imagem, bg=co1, fg=co6)
    label_imagem.place(x=390, y=10) 

# Função Atualizar Alunos
def atualizar():
    global imagem, imagem_strings, label_imagem

    # Obtendo o id
    id_aluno = int(entrada_procurar.get())

    # Obtendo os valores
    nome = entrada_nome.get()
    email = entrada_email.get()
    telefone = entrada_telefone.get()
    sexo = combo_sexo.get()
    data = data_nascimento.get()
    endereco = entrada_endereco.get()
    curso = combo_curso.get()
    img = imagem_string

    lista = [nome, email, telefone, sexo, data, endereco, curso, img, id_aluno]

    #verificando se a lista contem valores nulos
    for i in lista:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    #Registrando os valores
    sistema_de_registro.update_students(lista)

    # Limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    combo_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    combo_curso.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('img/logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = Label(frame_dados, image=imagem, bg=co1, fg=co6)
    label_imagem.place(x=390, y=10) 

    # Mostrando os valores na tabela
    mostrar_alunos()

    # Função Atualizar Alunos

# Função Deletar Alunos
def deletar():
    global imagem, imagem_strings, label_imagem

    # Obtendo o id
    id_aluno = int(entrada_procurar.get())

    # Deletando o aluno
    sistema_de_registro.delete_students(id_aluno)
        
    # Limpando os campos de entradas
    entrada_nome.delete(0, END)
    entrada_email.delete(0, END)
    entrada_telefone.delete(0, END)
    combo_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    entrada_endereco.delete(0, END)
    combo_curso.delete(0, END)

    entrada_procurar.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('img/logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = Label(frame_dados, image=imagem, bg=co1, fg=co6)
    label_imagem.place(x=390, y=10) 

    # Mostrando os valores na tabela
    mostrar_alunos()




# Criando os campos de entrada
label_nome = Label(frame_dados, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_nome.place(x=4, y=10)
entrada_nome = Entry(frame_dados, width=30, justify='left', relief='solid')
entrada_nome.place(x=7, y=40)

label_email = Label(frame_dados, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_email.place(x=4, y=70)
entrada_email = Entry(frame_dados, width=30, justify='left', relief='solid')
entrada_email.place(x=7, y=100)

label_telefone = Label(frame_dados, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_telefone.place(x=4, y=130)
entrada_telefone = Entry(frame_dados, width=15, justify='left', relief='solid')
entrada_telefone.place(x=7, y=160)

label_sexo = Label(frame_dados, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_sexo.place(x=127, y=130)
combo_sexo = ttk.Combobox(frame_dados, width=7, font=('Ivy 8 bold'), justify='center')
combo_sexo['values'] = ('M','F')
combo_sexo.place(x=130, y=160)

label_data_nascimento = Label(frame_dados, text="Data de Nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_dados, width=18, justify='center', background='darkblue', foreground='white', bordewidth=2, year=2023)
data_nascimento.place(x=224, y=40)

label_endereco = Label(frame_dados, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_endereco.place(x=220, y=70)
entrada_endereco = Entry(frame_dados, width=20, justify='left', relief='solid')
entrada_endereco.place(x=224, y=100)

cursos = ['Engenharia', 'Medicina', 'Sociais']

label_curso = Label(frame_dados, text="Cursos *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_curso.place(x=220, y=130)
combo_curso = ttk.Combobox(frame_dados, width=20, font=('Ivy 8 bold'), justify='center')
combo_curso['values'] = (cursos)
combo_curso.place(x=224, y=160)


# Função para enviar a imagem
def escolher_imagem():
    global imagem, imagem_string, label_imagem

    imagem = fd.askopenfilename()
    imagem_string=imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = Label(frame_dados, image=imagem, bg=co1, fg=co6)
    label_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Atualizar Foto'

botao_carregar = Button(frame_dados, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)

# Tabela Alunos
def mostrar_alunos():

    #Criando a visualização 
    list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    # Visualizar Estudantes
    df_list = sistema_de_registro.view_all_students()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h=[40,150,150,70,70,70,120,100,100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        # Ajuste da largura da coluna
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)


# Procurar aluno
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

label_nome = Label(frame_procurar, text="Procurar Aluno [Digite o ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
entrada_procurar = Entry(frame_procurar, width=5, justify='center', relief='solid', font=('Ivy 10'))
entrada_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar,command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# botões

app_img_adicionar = Image.open('img/add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar,relief=GROOVE, text=' Adicionar', width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('img/update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes,command=atualizar, image=app_img_atualizar,relief=GROOVE, text=' Atualizar', width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('img/delete.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes,command=deletar, image=app_img_deletar,relief=GROOVE, text=' Deletar', width=100,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# Linha de Separação
label_linha = Label(frame_botoes,relief=GROOVE, text='h', width=1,height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co1)
label_linha.place(x=245, y=15)



# Chamar a tabela
mostrar_alunos()



tela.mainloop()
