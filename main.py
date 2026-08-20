import flet as ft
import mysql.connector 
from dotenv import load_dotenv
import os
import re

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
    texto = ft.Text(value="Bem-vindo a Nesvt!", size=30 ,color="white",text_align=ft.TextAlign.CENTER)
    page.bgcolor = "black"
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False   # impede arrastar e mudar o tamanho
    page.window.maximizable = False #impede maximizar a tela

    input_user =ft.TextField(label="Nome de Usuário")
    input_email = ft.TextField(label="Email ")
    input_password = ft.TextField(label="Senha", password=True, can_reveal_password=True)


#---------------------------Functions--------------------------------------#
    def roteCadastro(e):
        page.clean()
        page.add(container_cadastro)
    def cadastro_click(e):
        #Criar funcao para inserir banco de dados 
        if not input_user.value or not input_email.value or not input_password.value:
            print("Por favor, preencha todos os campos.")
            return
        if not validate_email(input_email.value):
            print("Por favor, insira um email válido.")
            return

        cursor.execute(
                "INSERT INTO usuarios (nome,email, senha) VALUES (%s, %s,%s)",
                (input_user.value, input_email.value,input_password.value)
            )
        conexao.commit()
        print("INSERIDO")


    def roteLogin(e):
        page.clean()
        page.add(container_login)
    def login_click(e):
        #verifica se nao esta vazio o input
        if not input_email.value or not input_password.value:
            print("Por favor, preencha todos os campos.")
            return
        if not validate_email(input_email.value):
            print("Por favor, insira um email válido.")
            return
        cursor.execute(
                "SELECT * FROM usuarios WHERE email = %s AND senha = %s",
                (input_email.value, input_password.value)
            )
        result = cursor.fetchone()
        if result:
            print("Login bem-sucedido!")
            page.clean()
            page.add(ft.Text(value=f"Bem-vindo, {result[1]}!", size=30))
        else:
            print("Email ou senha incorretos.")

    def validate_email(email):
        # Função para validar o formato do email
        
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None


#--------------------------Pages--------------------------------------#
    #container da area de cadastro
    PageCadastro = ft.Container(
        #criacao de um content / column dentro do container 
        content=ft.Column(
            controls=[
                texto,  
                input_user,
                input_email,
                input_password,
                ft.Button("Entrar", on_click=cadastro_click),
                ft.TextButton("Já possui uma conta? Faça login",  on_click=roteLogin)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=  ft.Alignment.CENTER ,
        expand=True
    )

    PageLogin = ft.Container(
            #criacao de um content / column dentro do container 
            content=ft.Column(
                controls=[
                    texto,  
                    input_email,
                    input_password,
                    ft.Button("Entrar", on_click=login_click),
                    ft.TextButton("Nao possui uma conta? Faça o cadastro",  on_click=roteCadastro)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=  ft.Alignment.CENTER ,
            expand=True
        )
    
    
    page.add(PageCadastro)


ft.run(main)