import time

class Timerer:
    def __init__(self):
        self.tempos = []
        self.tempo_inicial = None
        self.contador_ativo = False

    def iniciar(self):
        self.tempos = []
        self.tempo_inicial = time.time()
        self.contador_ativo = True

    def registrar_tempo(self):
        if self.contador_ativo:
            tempo_atual = time.time() - self.tempo_inicial
            self.tempos.append(tempo_atual)
            self.tempo_inicial = time.time()  # Reinicia para a próxima volta
            return tempo_atual
        return None

    def finalizar(self):
        self.contador_ativo = False
        return self.tempos

    def calcular_estatisticas(self):
        if self.tempos:
            media = sum(self.tempos) / len(self.tempos)
            maior_tempo = max(self.tempos)
            menor_tempo = min(self.tempos)
            return media, maior_tempo, menor_tempo
        return None, None, None
