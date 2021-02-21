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

    def roleta(self):
        somatorio = 0
        for i in self.pop:
            somatorio += i.fitness
        # Calcula soma do fitness total para dividir em percentual
        
        # fr = fitness_relativo, 
        # Divide os percentuais de acordo com valor fit
        fr = [(i.fitness/somatorio)*100 for i in self.pop]
        # print('Divisão percentual:',fr)

        # Inicia e executa a roleta
        r = randint(0,100)
        # print('Sorteado na roleta foi:',r)

        roletado = 0
        pos_roleta = 0
        for pos, fit in enumerate(fr):
            # print(pos, fit)
            if(pos_roleta < r):
                pos_roleta += fit
            else:
                # Vai retornar o indivíduo escolhido
                roletado = pos
                break
        return self.pop[roletado]

    def selecaoGeracional(self, g):
        # G = geracao escolhida
        return [k for k in self.pop if k.ger == g]