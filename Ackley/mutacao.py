from numpy.random import randint, uniform, normal
import numpy as np
from constants import TAU, TAU2, TAU3, MIN_PACE
from Individuo import Individuo

def mutacao(codigo, individuo: Individuo):
    if codigo == 1: r

def mutacao_uniforme(individuo: Individuo):

    novos_genes = [gene if 5 > randint(0, 101) else uniform(-15, 15) for gene in individuo.genes]
    individuo.genes = novos_genes

def mutacao_uniforme_2(individuo: Individuo):
    sd = np.std(individuo.genes)
    sd_lower = sd if sd < 0 else -sd
    sd_upper = sd if sd > 0 else -sd

    for i in range(len(individuo.genes)):
        lower = uniform(-15, sd_lower)
        upper = uniform(sd_upper, 15)
        x = uniform(lower, upper) + individuo.genes[i]
        if x > 15: x = x % 15
        if x < -15: x = -(x % 15)

        individuo.genes[i] = x

        

def mutacao_sigma(individuo: Individuo):
    for i in range(len(individuo.genes)):
        individuo.paces[0] *= np.exp(TAU * normal())

        individuo.paces[0] = max(individuo.paces[0], MIN_PACE)
        
        individuo.genes[i] = individuo.genes[i] + individuo.paces[0] * normal()


def mutacao_sigma_2(individuo: Individuo):
    for i in range(len(individuo.genes)):
        individuo.paces[i] = individuo.paces[i] * np.exp(TAU2 * normal()) + TAU3 * normal()

        individuo.paces[i] = max(MIN_PACE, individuo.paces[i])

        individuo.genes[i] = individuo.paces[i] * normal()
