from numpy.random import randint
from Individuo import Individuo

def recombinacaoD(pai1: Individuo, pai2: Individuo) -> Individuo:
    # Recombinação Discreta
    # Descrição slide: seleciona aleatoriamente um 
    # valor de um dos pais (mais usada p/ variáveis objeto)
    filho = []
    for i in range(len(pai1.genes)):
        if randint(0,2) == 0:
            filho.append(pai1.gene[i])
        else:
            filho.append(pai2.gene[i])
    
    return Individuo(genes=filho)
    
    

def recombinacaoI(pai1: Individuo, pai2: Individuo) -> Individuo:
    # Recombinação Intermediária
    # Descrição slide: calcula os valores médios 
    # entre os pais (mais usada p/ parâmetros da EE)   

    filho = []

    for g in range(len(pai1.genes)):
        filho.append((pai1.genes[g]+pai2.genes[g])/2)

    return Individuo(genes=filho)
