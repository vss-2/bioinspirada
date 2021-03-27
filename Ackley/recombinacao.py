from numpy.random import randint, uniform
from Individuo import Individuo

def recombinacao(pai1: Individuo, pai2: Individuo, tipo: int):
    if tipo == 1: return recombinacaoD(pai1, pai2)
    elif tipo == 2: return recombinacaoI(pai1, pai2)
    elif tipo == 3: return recombinacao_roubada

def recombinacaoD(pai1: Individuo, pai2: Individuo) -> Individuo:
    # Recombinação Discreta
    # Descrição slide: seleciona aleatoriamente um 
    # valor de um dos pais (mais usada p/ variáveis objeto)
    filho = []
    for i in range(len(pai1.genes)):
        if randint(0,2) == 0:
            filho.append(pai1.genes[i])
        else:
            filho.append(pai2.genes[i])
    
    return Individuo(genes=filho)
    
    
def recombinacaoI(pai1: Individuo, pai2: Individuo) -> Individuo:
    # Recombinação Intermediária
    # Descrição slide: calcula os valores médios
    # entre os pais (mais usada p/ parâmetros da EE)
    filho = []
    for i in range(len(pai1.genes)):
        filho.append(pai1.genes[i] + pai2.genes[i])

    return Individuo(genes=filho)


def recombinacao_roubada(pai1: Individuo, pai2: Individuo) -> Individuo:

    filho = []
    parte_pai1 = pai1.fitness / (pai1.fitness + pai2.fitness)
    parte_pai2 = pai2.fitness / (pai1.fitness + pai2.fitness)

    for g in range(len(pai1.genes)):
        filho.append((pai1.genes[g] * parte_pai1 + pai2.genes[g] * parte_pai2)/2)

    return Individuo(genes=filho)



