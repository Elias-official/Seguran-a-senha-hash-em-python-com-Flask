import re
import string
import secrets
import bcrypt
import hashlib
import requests

def verificar_forca(senha):
    pontos = 0

    if len(senha) >= 8:
        pontos += 1

    if re.search(r"[A-Z]", senha):
        pontos += 1

    if re.search(r"[0-9]", senha):
        pontos += 1

    if re.search(r"[!@#$%&*_-]", senha):
        pontos += 1

    return pontos

def gerar_senha():
    chars_seguro = (
            string.ascii_letters +
            string.digits +
            "!@#$%&*_-"
    )

    senha = ''.join(
        secrets.choice(chars_seguro) for _ in range(12)
    )

    return senha

def gerar_hash(senha):

    senha_bytes = senha.encode('utf-8')

    hash_bytes = bcrypt.hashpw(
            senha_bytes,
            bcrypt.gensalt()
    )

    return hash_bytes.decode('utf-8')

def verificar_hash(senha, hash_salvo):

    senha_bytes = senha.encode('utf-8')

    return bcrypt.checkpw(
        senha_bytes,
        hash_salvo.encode('utf-8')
    )

def salvar_hash(hash_senha):

    with open("senhas.txt", "a") as arquivo:
        arquivo.write(hash_senha + "\n")


def verificar_vazamento(senha):

    try:
        sha1 = hashlib.sha1(
            senha.encode('utf-8')
        ).hexdigest().upper()

        prefixo = sha1[:5]
        sufixo = sha1[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefixo}"

        resposta = requests.get(url)

        hashes = resposta.text.splitlines()

        for linha in hashes:

            hash_sufixo, contagem = linha.split(":")

            if hash_sufixo == sufixo:
                return contagem

        return 0

    except:
        return "Erro ao verificar API"

