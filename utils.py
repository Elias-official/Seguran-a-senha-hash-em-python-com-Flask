import secrets
import string


def mostrar_forca(pontos):

    if pontos <= 1:
        print("Senha Fraca")

        gerar = input("Deseja gerar a senha? (y/n) ou continuar com esta senha? (c): ")

        if gerar == "y":
            chars_seguro =(
                string.ascii_letters + string.digits + "!@#$%&*_-"
            )

            senha = "".join(secrets.choice(chars_seguro) for _ in range(12))

            print(f"Senha gerada: {senha}")

        elif gerar == "c":

            print("Continuando com senha fraca...")

        else:
            print("Digite outra senha.")

    elif pontos <= 3:
        print("Senha Média")

        confirmar = input("Deseja utilizar esta senha? (y/n): ")

        if confirmar == "n":
            print("Escolha outra senha!")

    else:
        print("Senha Forte!")

def barra_forca(pontos):

    if pontos <= 1:
        barra = "[██--------]"
        nivel = "Fraca"

    elif pontos <= 3:
        barra = "[██████----]"
        nivel = "Média"

    else:
        barra = "[██████████]"
        nivel = "Forte"

    print(f"{barra} {nivel}")

