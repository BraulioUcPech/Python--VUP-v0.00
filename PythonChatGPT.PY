import openai
import config
import typer
from rich import print
from rich.table import Table


def main():

    openai.api_key = config.ApiKey
    print("[bold green]ChatGPT API en Python [/bold green]")

    table = Table("comando", "Descripción")
    table.add_row("exit", "Para salir del chat ")
    table.add_row("new", "Crear una nueva conversación ")

    print(table)


    #Contexto del asistente
    contexto = {"role": "system",
                "content" : "Eres un asistence muy útil."}
    messeges = [contexto]

    while True:
        content = __prompt()

        if content == "new":
            print("Nueva conversación ✌️ ")
            messeges = [contexto]
            content = __prompt()

        messeges.append({"role": "user", "content": content})

        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messeges)

        ContenidoRespuesta = respuesta.choices[0].message.content
        messeges.append({"role": "assistant", "content": ContenidoRespuesta})

        print(f"[bold green]> [/bold green][green]{ContenidoRespuesta}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre que quieres hablar?:- ")

    if prompt == "exit":
        exit = typer.confirm("🅰️ Estas seguro que deseas salir? ")
        if exit:
            print("Adios ✌️")
            raise typer.Abort()
        return __prompt()

    return prompt




if __name__ == "__main__":
    typer.run(main)
