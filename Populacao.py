from Individuo import Individuo
from random import sample, randint
from recombinacao import recombinacao
class Populacao:

    def __init__(self, n=8,ger=0):
        self.pop = [Individuo(n, None, ger) for i in range(100)]
        self.pop.sort(key=lambda i: i.fitness)

    def generateSolution(self):
        ger = 1
        while self.pop[-1].fitness != 1 and ger != 10000:
            probCrossover = randint(0, 99)
            if probCrossover < 90:
                # 2 melhores de 5 aleatorios
                paisSelecionados = sorted(sample(self.pop, k=5), key=lambda i: i.fitness)[-2:]
                filho1, filho2 = recombinacao(paisSelecionados[0].getIndividuoInteger(), paisSelecionados[1].getIndividuoInteger())
                filho1 = Individuo(gen=filho1, ger=ger)
                filho2 = Individuo(gen=filho2, ger=ger)
                for i in [filho1, filho2]:
                    probMutacao = randint(0, 99)
                    if probMutacao < 40: i.mutate()
                
                self.pop += [filho1, filho2]
                self.pop.sort(key=lambda i: i.fitness)
                self.pop = self.pop[2:]
                
            ger += 1

        return self.pop[-1]