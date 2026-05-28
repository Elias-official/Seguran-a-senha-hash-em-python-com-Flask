from utils import *
from bruteforce import *
from interface import *
from getpass import getpass

senha = getpass("Digite a sua senha: ")

pontos = verificar_forca(senha)

barra_forca(pontos)

mostrar_forca(pontos)

hash_senha = gerar_hash(senha)

print(f"Hash: {hash_senha}")

salvar_hash(hash_senha)

senha_verificar = input("Digite a senha para verificar: ")
hash_verificar = input("Digite a verifica hash: ")

try:
    if verificar_hash(senha_verificar, hash_verificar):
        print("Senha verificada!")
    else:
        print("Senha incorreta!")

except ValueError:
    print("Hash Inválida!")


senha_real = senha

brute_force_demo(senha_real)