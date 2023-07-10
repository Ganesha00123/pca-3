import time
import random

def main():
    print("Bem-vindo ao jogo da multiplicação!")
    print("Lhe daremos 10 questões de multiplicação. Responda o mais rápido que puder.")
    print("Boa sorte!\n")

    # Variáveis
    acertos = 0
    erros = 0
    tempo = 0
    inicio = 0
    fim = 0

    # Loop para as 10 perguntas
    for i in range(10):
        # Números aleatórios de 1 a 10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        # Aqui fazemos a pergunta
        print(i + 1, "ª pergunta: Quanto é", num1, "x", num2, "?")
        inicio = time.time()
        answer = int(input("Answer: "))
        fim = time.time()

        # Verifique se a resposta está correta
        if answer == num1 * num2:
            print("Acertou!")
            acertos += 1
        else:
            print("Errou!")
            erros += 1

        print("")

    # Calculamos o tempo total
    tempo = fim - inicio
    # Arredondamos o tempo para duas casas decimais
    tempo = round(tempo, 2)

    # Aqui mostramos os resultados
    print("Você acertou", acertos, "questões e errou", erros, "questões.")
    print("Você levou", tempo, "segundos para responder todas as questões.")

main()