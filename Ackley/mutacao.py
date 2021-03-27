from numpy.random import randint, uniform, normal
import numpy as np
from constants import TAU, TAU2, TAU3, MIN_PACE
from Individuo import Individuo
from copy import deepcopy

def mutacao(individuo: Individuo, tipo):
    if tipo == 1:
        mutacao_uniforme(individuo)
    elif tipo == 2:
        mutacao_nao_normal(individuo)
    elif tipo == 3:
        mutacao_sigma(individuo)
    elif tipo == 4:
        mutacao_sigma_2(individuo)
    elif tipo == 5:
        mutacao_roubada(individuo)


def mutacao_uniforme(individuo: Individuo):
    original = deepcopy(individuo)
    novos_genes = [gene if 5 > randint(0, 101) else uniform(-15, 15) for gene in individuo.genes]
    individuo.genes = novos_genes
    if original.fitness > individuo.fitness:
        individuo.genes = original.genes

def mutacao_nao_normal(individuo: Individuo):
    original = deepcopy(individuo)
    sd = np.std(individuo.genes)
    for i in range(len(individuo.genes)):
        x = individuo.genes[i]
        limInferior = (x - sd) % 15
        limSuperior = (x + sd) % 15
        x = uniform(-limInferior, limSuperior)
        individuo.genes[i] = x
    
    if original.fitness > individuo.fitness:
        individuo.genes = original.genes

def mutacao_sigma(individuo: Individuo):
    original = deepcopy(individuo)
    for i in range(len(individuo.genes)):
        # print(individuo.paces[0])
        individuo.paces[0] *= np.exp(TAU * normal())

        individuo.paces[0] = max(individuo.paces[0], MIN_PACE)
        
        individuo.genes[i] = individuo.genes[i] + individuo.paces[0] * normal()
    
    if original.fitness > individuo.fitness:
        individuo.genes = original.genes


def mutacao_sigma_2(individuo: Individuo):
    original = deepcopy(individuo)
    for i in range(len(individuo.genes)):
        individuo.paces[i] = individuo.paces[i] * np.exp(TAU2 * normal()) + TAU3 * normal()

        individuo.paces[i] = max(MIN_PACE, individuo.paces[i])

        individuo.genes[i] = individuo.paces[i] * normal()
    if original.fitness > individuo.fitness:
        individuo.genes = original.genes

def mutacao_roubada(individuo: Individuo):
    for i in range(len(individuo.genes)):
        x = individuo.genes[i]
        x *= uniform(0, 1)
        individuo.genes[i] = x
