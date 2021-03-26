import numpy as np
from numpy.random import uniform
from constants import GENE_SIZE

def ackley(individuo):

    somatorio1 = sum([x**2 for x in individuo]) / GENE_SIZE
    exp1 = np.exp(-0.2 * np.sqrt(somatorio1))
    parte1 = -20 * exp1

    somatorio2 = sum([np.cos(2 * np.pi * x) for x in individuo]) / GENE_SIZE
    exp2 = -np.exp2(somatorio2)
    # parte2 = exp2 + 20 + 1
    parte2 = exp2 + 20 + np.exp(1)

    return round(parte1 + parte2, 5)

def fitness(individuo):
    return 1 / (1 + ackley(individuo))





