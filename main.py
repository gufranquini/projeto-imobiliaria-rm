import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.imovel import Imovel
from servicos.gerador_orcamento import gerar_orcamento

# Exemplo de uso
imovel = Imovel(
    tipo="apartamento",
    quartos=2,
    garagem=True,
    sem_criancas=True
)

gerar_orcamento(imovel)
