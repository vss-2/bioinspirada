from Individuo import Individuo
from random import choices, randint
from recombinacao import recombinacao
class Populacao:

    def __init__(self, n=8,ger=0):
        self.pop = [Individuo(n, None, ger) for i in range(100)]
        self.pop.sort(key=lambda i: i.fitness)

    def generateSolution(self):
        ger = 1
        while self.pop[-1].fitness != 1:
            probCrossover = randint(0, 99)
            if probCrossover < 90:
                # 2 melhores de 5 aleatorios
                paisSelecionados = sorted(choices(self.pop, k=5), key=lambda i: i.fitness)[-2:]
                filho1, filho2 = recombinacao(paisSelecionados[0], paisSelecionados[1])
                filho1 = Individuo(gen=filho1, ger=ger)
                filho2 = Individuo(gen=filho2, ger=ger)
                ger += 1


        return self.pop[-1]