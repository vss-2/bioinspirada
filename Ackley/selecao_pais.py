from random import sample

def selecao_pais(populacao, tipo):
    if tipo == 1:
        return selecao_aleatoria(populacao)
    elif tipo == 2:
        return selecao_elitista(populacao)


def selecao_aleatoria(populacao):
    return sample(populacao, k=2)


def selecao_elitista(populacao):
    return sorted(sample(populacao, k=5), key=lambda i: i.fitness)[-2:]
