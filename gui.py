import random
import time
import tkinter as tk

# Declare the MathGame class
class MathGame:
    # This is the constructor
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Multiplicação")

        self.acertos = 0
        self.erros = 0
        self.tempo = 0
        self.inicio = 0
        self.fim = 0
        self.questao_atual = 1
        self.numero_de_perguntas = 10
        

        # First number in the equation. It's the 7 in 7 x 8
        self.num1_label = tk.Label(master, text="")
        self.num1_label.grid(row=0, column=0)

        # The "x" in the equation
        self.x_label = tk.Label(master, text="x")
        self.x_label.grid(row=0, column=1)

        # Second number in the equation. It's the 8 in 7 x 8
        self.num2_label = tk.Label(master, text="")
        self.num2_label.grid(row=0, column=2)

        # The answer entry box
        self.caixa_de_resposta = tk.Entry(master)
        self.caixa_de_resposta.grid(row=0, column=3)

        # Listen for the Enter key to be pressed and call the enviar_resposta method
        self.caixa_de_resposta.bind("<Return>", self.enviar_resposta)

        self.botao_enviar = tk.Button(master, text="Enviar", command=self.enviar_resposta)
        self.botao_enviar.grid(row=0, column=4)

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.grid(row=1, column=0, columnspan=5)

        self.botao_de_sair = tk.Button(master, text="Sair", command=master.quit)
        self.botao_de_sair.grid(row=3, column=4)

        self.proxima_pergunta()

    def numero_aleatorio(self):
        return random.randint(1, 10)

    # Este método mostra a próxima pergunta. Ele é chamado quando
    # o usuário clicar no botão Enviar ou quando ele pressionar Enter
    def proxima_pergunta(self):
        if self.questao_atual > self.numero_de_perguntas:
            self.mostrar_resultados()
            return

        self.num1 = self.numero_aleatorio()
        self.num2 = self.numero_aleatorio()

        self.num1_label.config(text=str(self.num1))
        self.num2_label.config(text=str(self.num2))
        self.caixa_de_resposta.delete(0, tk.END)

        self.questao_atual += 1
        self.inicio = time.time()

    # Este método é chamado quando o usuário clica no botão Enviar
    # o parâmetro "event=None" é necessário para que o método possa
    # ser chamado pela tecla Enter
    def enviar_resposta(self, event=None):
        self.fim = time.time()
        answer = self.caixa_de_resposta.get()

        if answer.isdigit() and int(answer) == self.num1 * self.num2:
            self.acertos += 1
            result_text = "Acertou! :)"
        else:
            self.erros += 1
            result_text = "Errou! :("

        self.show_next_screen(result_text)

    # Este método exibe o resultado e a próxima pergunta
    def show_next_screen(self, result_text):
        # Mostra o resultado
        self.label_resultado.config(text=result_text)
        # Mostra a próxima pergunta
        self.proxima_pergunta()  

    # Este método é chamado quando o usuário respondeu todas as perguntas
    def mostrar_resultados(self):
        self.tempo = self.fim - self.inicio
        self.tempo = round(self.tempo, 2)

        result_text = f"Você acertou {self.acertos} perguntas e errou {self.erros}.\n"
        result_text += f"Você levou {self.tempo} segundos para responder as perguntas."

        # Esconde a caixa de resposta e o botão Enviar
        self.caixa_de_resposta.grid_remove()
        self.botao_enviar.grid_remove()
        # Esconde as labels com os números
        self.num1_label.grid_remove()
        self.x_label.grid_remove()
        self.num2_label.grid_remove()
        # Mostra o resultado
        self.label_resultado.config(text=result_text)

root = tk.Tk()
game = MathGame(root)
root.mainloop()