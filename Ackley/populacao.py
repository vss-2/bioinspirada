from Individuo import Individuo
from constants import GENE_SIZE
from numpy.random import uniform

def inicializar_pop():
    populacao = []

    while len(populacao) < 100:
        i = [uniform(-15, 15) for _ in range(GENE_SIZE)]
        if i not in populacao:
            populacao.append(i)

    return [Individuo(genes=i) for i in populacao]

