from numpy.random import randint
from Individuo import Individuo

def recombinacaoD(pai1: Individuo, pai2: Individuo) -> Individuo:
    # Recombinação Discreta
    # Descrição slide: seleciona aleatoriamente um 
    # valor de um dos pais (mais usada p/ variáveis objeto)
    if randint(1,3) == 1:
        return pai1
    else:
        return pai2

def recombinacaoI(pai1: Individuo, pai2: Individuo) -> Individuo:
    # Recombinação Intermediária
    # Descrição slide: calcula os valores médios 
    # entre os pais (mais usada p/ parâmetros da EE)   

    filho = []

    for g in range(len(pai1.genes)):
        filho.append((pai1.genes[g]+pai2.genes[g])/2)

    return Individuo(genes=filho)
