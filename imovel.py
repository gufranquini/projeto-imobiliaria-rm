class Imovel:
    def __init__(self, tipo, quartos=1, garagem=False, vagas_estacionamento=0, sem_criancas=False):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.vagas_estacionamento = vagas_estacionamento
        self.sem_criancas = sem_criancas
