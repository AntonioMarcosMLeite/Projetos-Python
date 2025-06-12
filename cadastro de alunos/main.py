import sqlite3 
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudantes.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome TEXT NOT NULL,
                           email TEXT NOT NULL,
                           telefone TEXT NOT NULL,
                           sexo TEXT NOT NULL,
                           data_nascimento TEXT NOT NULL,
                           endereco TEXT NOT NULL,
                           curso TEXT NOT NULL,
                           imagem TEXT NOT NULL)''')
        

    def register_student(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, telefone, sexo, data_nascimento, endereco, curso, imagem) VALUES (?,?,?,?,?,?,?,?)",(estudantes)) 
        self.conn.commit()

        # Mostrando a mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro realizado com sucesso!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados

    def search_students(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_students(self, novo_valores):
        query = "UPDATE estudantes SET nome=?, email=?, telefone=?, sexo=?, data_nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?"
        self.c.execute(query, novo_valores)
        self.conn.commit()

        # Mostrando a mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com ID:{novo_valores[8]} foi atualizado!')

    def delete_students(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        # Mostrando a mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi excluido!')

# Criando uma instancia do sistema de registro
sistema_de_registro = SistemaDeRegistro()


