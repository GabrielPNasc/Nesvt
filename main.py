import flet as ft


def main(page: ft.Page):

    #Criando Titulo e alinhamento da página inteira
    page.title = "Meu Primeiro App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    texto = ft.Text(value="Bem-vindo a Nesvt!", size=30)


    def login_click(e):
            #Criar funcao para inserir banco de dados 
            page.add(ft.Text(value="Login realizado com sucesso!", size=20, color=ft.Colors.GREEN))


    #container da area de login
    container_login = ft.Container(
        #criacao de um content / column dentro do container 
        content=ft.Column(
            controls=[
                texto,  
                ft.TextField(label="Usuário"),
                ft.TextField(label="Senha", password=True, can_reveal_password=True),
                ft.Button("Entrar", on_click=login_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=  ft.Alignment.CENTER ,
        expand=True
    )
    
    

    page.add(container_login)


ft.run(main)