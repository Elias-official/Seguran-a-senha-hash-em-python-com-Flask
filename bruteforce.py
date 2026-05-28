from itertools import product
import  string
import time

def brute_force_demo(senha_real):

    charset = (string.ascii_letters + string.digits + "!@#$%&*_-")

    tamanho = 10
    tentativas_por_segundo = 1_000_000

    combinances = len(charset) ** tamanho
    tempo_segundos = combinances // tentativas_por_segundo

    dias = tempo_segundos / 86400
    anos = dias / 365

    print(f"Combinações: {combinances:e}")
    print(f"Tempo estimado: {anos:2e} anos")

    inicio = time.time()

    tentativas = 0

    if len(senha_real) >= 12:
        print("Senha muito forte para demonstração.")

    else:

        for tentativa in product(charset, repeat=len(senha_real)):
            tentativa = "".join(tentativa)
            tentativas += 1

            if tentativas % 1000000 == 0:
                print(f"Tentativas: {tentativas}")

            if tentativa == senha_real:
                fim = time.time()

                return (
                    f"""
                    Senha encontrada: {tentativa}<br>
                    Tentativas: {tentativas}<br>
                    Tempo: {fim - inicio:.4f}s
                    """
                )
            return "Senha não encontrada"