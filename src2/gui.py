import tkinter as tk
import time  # Importação correta para o uso do time.time()

class TreinoNadadorGUI:
    def __init__(self, master, timer):
        self.master = master
        self.master.title("Registro de Tempos do Nadador")
        self.timer = timer
        
        self.label_instrucoes = tk.Label(master, text="Pressione 'Iniciar' para começar o treino.")
        self.label_instrucoes.pack(pady=10)

        self.botaoiniciar = tk.Button(master, text="Iniciar", command=self.iniciar_treino)
        self.botaoiniciar.pack(pady=5)

        self.botaoregistrar = tk.Button(master, text="Registrar Tempo", command=self.registrar_tempo, state=tk.DISABLED)
        self.botaoregistrar.pack(pady=5)

        self.label_tempo = tk.Label(master, text="Tempo: 0.00 segundos", font=("Helvetica", 14))
        self.label_tempo.pack(pady=20)

        self.botaofinalizar = tk.Button(master, text="Finalizar Treino", command=self.finalizar_treino, state=tk.DISABLED)
        self.botaofinalizar.pack(pady=5)

        self.label_resultados = tk.Label(master, text="")
        self.label_resultados.pack(pady=10)

    def atualizar_tempo(self):
        if self.timer.contador_ativo:
            tempo_atual = time.time() - self.timer.tempo_inicial
            self.label_tempo.config(text=f"Tempo: {tempo_atual:.2f} segundos")
            self.master.after(100, self.atualizar_tempo)  # Atualiza a cada 100ms

    def iniciar_treino(self):
        self.timer.iniciar()
        self.botaoiniciar.config(state=tk.DISABLED)
        self.botaoregistrar.config(state=tk.NORMAL)
        self.botaofinalizar.config(state=tk.NORMAL)
        self.label_resultados.config(text="")
        self.atualizar_tempo()  # Começa a atualizar o tempo exibido

    def registrar_tempo(self):
        tempo_registrado = self.timer.registrar_tempo()
        if tempo_registrado is not None:
            self.label_tempo.config(text=f"Tempo da volta: {tempo_registrado} segundos")
            if len(self.timer.tempos) == 10:
                self.botaoregistrar.config(state=tk.DISABLED)
                self.label_tempo.config(text="10 voltas registradas!")

    def finalizar_treino(self):
        tempos = self.timer.finalizar()
        if tempos:
            media, maior, menor = self.timer.calcular_estatisticas()
            resultados = (
                f"Tempos registrados: {tempos}\n"
                f"Média dos tempos: {media:.2f} segundos\n"
                f"Maior tempo: {maior:.2f} segundos\n"
                f"Menor tempo: {menor:.2f} segundos"
            )
            self.label_resultados.config(text=resultados)
            self.botaoiniciar.config(state=tk.NORMAL)
            self.botaofinalizar.config(state=tk.DISABLED)
