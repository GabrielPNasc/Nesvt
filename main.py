import flet as ft


#funcao main que recebe a pagina como parametro
def main(page: ft.Page):
    
    page.title = "Meu Primeiro App"


    page.vertical_alignment = ft.MainAxisAlignment.START    
    page.horizontal_alignment = ft.CrossAxisAlignment.START


    texto = ft.Text(value="Olá, Mundo!", size=30)

    ContainerText = ft.Container(
        content=texto,
        alignment="center",
        expand=True
    )

    #add o texto na pagina
    page.add(ContainerText)

ft.app(target=main)
