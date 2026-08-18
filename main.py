import flet as ft
import mysql.connector 
from dotenv import load_dotenv
import os
#carregando o .env
load_dotenv() 
#conectando no database
conexao = mysql.connector.connect(
    host= os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

cursor = conexao.cursor()

def createDatabase():
    cursor.execute("CREATE DATABASE IF NOT EXISTS Nesvt;")
    cursor.execute("USE Nesvt;")
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            senha VARCHAR(255) NOT NULL
        );''')

def main(page: ft.Page):

    createDatabase()
    #Criando Titulo e alinhamento da página inteira
    page.title = "Meu Primeiro App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    texto = ft.Text(value="Bem-vindo a Nesvt!", size=30 )

    input_user =ft.TextField(label="Nome de Usuário")
    input_email = ft.TextField(label="Email ")
    input_password = ft.TextField(label="Senha", password=True, can_reveal_password=True)




    def cadastro_click(e):
        #Criar funcao para inserir banco de dados 
        cursor.execute(
                "INSERT INTO usuarios (nome,email, senha) VALUES (%s, %s,%s)",
                (input_user.value, input_email.value,input_password.value)
            )
        conexao.commit()
        page.clean()
        page.add(container_login)
        print("INSERIDO")



    def login_click(e):
        print("aaaaaaaaaa")




    #container da area de cadastro
    container_cadastro = ft.Container(
        #criacao de um content / column dentro do container 
        content=ft.Column(
            controls=[
                texto,  
                input_user,
                input_email,
                input_password,
                ft.Button("Entrar", on_click=cadastro_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=  ft.Alignment.CENTER ,
        expand=True
    )

    container_login = ft.Container(
            #criacao de um content / column dentro do container 
            content=ft.Column(
                controls=[
                    texto,  
                    input_email,
                    input_password,
                    ft.Button("Entrar", on_click=login_click)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=  ft.Alignment.CENTER ,
            expand=True
        )
    
    

    page.add(container_cadastro)


ft.run(main)