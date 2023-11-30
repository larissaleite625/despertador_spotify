import tkinter as tk
from main import despertador
import datetime
import time

def iniciar_despertador():
    # Obter a hora do despertar do usuário
    hora_despertar = datetime.datetime(2023, 6, 28, 17, 51)  # Exemplo: 28 de junho de 2023, 17:51

    # Loop até o horário de despertar ser alcançado
    while True:
        agora = datetime.datetime.now()
        if agora >= hora_despertar:
            despertador()
            break
        else:
            tempo_restante = hora_despertar - agora
            tempo_restante_str = str(tempo_restante)
            label_tempo_restante.config(text="Tempo restante: " + tempo_restante_str)
            janela.update()
            time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente

# Criar a janela principal
janela = tk.Tk()

# Criar um rótulo para exibir o tempo restante
label_tempo_restante = tk.Label(janela, text="Tempo restante: ")
label_tempo_restante.pack()

# Criar um botão para iniciar o despertador
botao_iniciar = tk.Button(janela, text="Iniciar Despertador", command=iniciar_despertador)
botao_iniciar.pack()

# Executar o loop principal da interface gráfica
janela.mainloop()
