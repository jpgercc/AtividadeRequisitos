import time

class Timerer:
    def __init__(self):
        self.tempos = [] # Inicializa o array de tempos
        self.tempo_inicial = None # Inicializa o tempo inicial como None
        self.contador_ativo = False # Inicializa o contador como False

    def iniciar(self):
        self.tempos = []
        self.tempo_inicial = time.time() # Inicializa o tempo inicial
        self.contador_ativo = True

    def registrar_tempo(self):
        if self.contador_ativo:
            tempo_atual = time.time() - self.tempo_inicial # Calcula o tempo atual
            self.tempos.append(tempo_atual) # Adiciona o tempo atual ao array 
            self.tempo_inicial = time.time()  # Reinicia para a proxima volta
            return tempo_atual
        
        return None # Se o if nao for satisfeito, a funçao ira retornar None

    def finalizar(self):
        self.contador_ativo = False
        return self.tempos

    def calcular_estatisticas(self):
        if self.tempos:
            media = sum(self.tempos) / len(self.tempos) # Calcula a media
            maior_tempo = max(self.tempos) # Calcula o maior tempo
            menor_tempo = min(self.tempos) # Calcula o menor tempo
            return media, maior_tempo, menor_tempo
        return None, None, None # Se o if nao for satisfeito retorna None para cada uma 