import numpy as np
from random import uniform, randint

def ackley(individuo):

    somatorio1 = sum([x**2 for x in individuo]) / 30
    exp1 = np.exp(-0.2 * np.sqrt(somatorio1))
    parte1 = -20 * exp1

    somatorio2 = sum([np.cos(2 * np.pi * x) for x in individuo]) / 30
    exp2 = -np.exp2(somatorio2)
    parte2 = exp2 + 20 + 1

    return round(parte1 + parte2, 5)

def fitness(individuo):
    return 1 / (1 + ackley(individuo))

def inicializar_pop():
    populacao = []

    while len(populacao) < 100:
        i = get_individuo()
        if i not in populacao: populacao.append(i)
    
    return populacao


def get_individuo():
    return [uniform(-15, 15) for _ in range(30)]

def recombinacaoD(pai1, pai2):
    # Recombinação Discreta
    # Descrição slide: seleciona aleatoriamente um 
    # valor de um dos pais (mais usada p/ variáveis objeto)
    if randint(1,2) == 1:
        return pai1
    else:
        return pai2

def recombinacaoI(pai1, pai2):
    # Recombinação Intermediária
    # Descrição slide: calcula os valores médios 
    # entre os pais (mais usada p/ parâmetros da EE)
    return (pai1+pai2)/2
