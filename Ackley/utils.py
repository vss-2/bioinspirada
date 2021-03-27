import numpy as np
from numpy.random import uniform, randint
from constants import GENE_SIZE
import math

def ackley(individuo):
    somatorio1 = sum([x**2 for x in individuo]) / GENE_SIZE
    exp1 = np.exp(-0.2 * np.sqrt(somatorio1))
    parte1 = -20 * exp1    
    somatorio2 = sum([np.cos(2 * np.pi * x) for x in individuo]) / GENE_SIZE
    exp2 = -np.exp(somatorio2)
    parte2 = exp2 + 20 + np.exp(1)

    # return round(parte1 + parte2, 5)
    return parte1 + parte2

def fitness(individuo):
    # return round(1 / (1 + ackley(individuo)), 5)
    return 1 / (1 + ackley(individuo))
