import flet as ft


#funcao main que recebe a pagina como parametro
def main(page: ft.Page):
    
    page.title = "Meu Primeiro App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    texto = ft.Text(value="Olá, Mundo!", size=30)

    #add o texto na pagina
    page.add(ft.Column([texto]))

ft.app(target=main)
