from flask import Flask, render_template, request, jsonify
from utils import *
from bruteforce import *
from interface import *

app = Flask(__name__)


@app.route("/gerar_senha")
def gerar_senha_route():

    senha = gerar_senha()

    return jsonify({
        "senha": senha
    })


@app.route("/", methods=["GET", "POST"])
def home():

    resultado = ""
    classe = ""
    mensagem = ""

    if request.method == "POST":

        senha = request.form["senha"]
        opcao = request.form["opcao"]

        if opcao == "1":

            pontos = verificar_forca(senha)

            if pontos <= 1:

                resultado = "Senha Fraca"
                classe = "fraca"

                mensagem = (
                    "Deseja gerar uma senha forte "
                    "ou continuar mesmo assim?"
                )

            elif pontos <= 3:

                resultado = "Senha Média"
                classe = "media"

                mensagem = (
                    "Tem certeza que deseja "
                    "usar essa senha?"
                )

            else:

                resultado = "Senha Forte"
                classe = "forte"

                mensagem = "Senha segura."

        elif opcao == "2":

            hash_senha = gerar_hash(senha)

            salvar_hash(hash_senha)

            resultado = hash_senha

        elif opcao == "3":

            hash_senha = request.form["hash"]

            try:

                if verificar_hash(senha, hash_senha):

                    resultado = "Senha Verificada"

                else:

                    resultado = "Senha Incorreta"

            except ValueError:

                resultado = "Hash Inválido"

        elif opcao == "4":

            resultado = brute_force_demo(senha)

        elif opcao == "5":

            vazamentos = verificar_vazamento(senha)

            if isinstance(vazamentos, str):

                resultado = vazamentos

            elif vazamentos > 0:

                resultado = (
                    f"Senha encontrada em "
                    f"{vazamentos} vazamentos!"
                )

            else:

                resultado = (
                    "Senha não encontrada "
                    "em vazamentos."
                )

    return render_template(
        "index.html",
        resultado=resultado,
        classe=classe,
        mensagem=mensagem
    )


if __name__ == "__main__":
    app.run(debug=True)