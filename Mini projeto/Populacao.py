from Individuo import Individuo
from random import sample, randint
from recombinacao import recombinacao

class Populacao:


    def __init__(self, n=8, popsize=100):
        self.pop = [Individuo(n) for i in range(popsize)]
        self.pop.sort(key=lambda i: i.fitness)
        self.cnt = 0
        self.ger = 0

    def hasConverged(self):
        return len([i.fitness for i in self.pop if i.fitness < 1]) == 0

    def generateSolution(self, geracional=False, roleta=False, tiporecomb=1, tipomut=1):
        self.cnt = 0
        self.ger = 1
        # while not self.hasConverged():
        while self.pop[-1].fitness != 1 and self.ger <= 10000:
            probCrossover = randint(0, 99)
            if probCrossover < 90:
                if roleta:
                    paisSelecionados = self.roleta()
                else:
                    # 2 melhores de 5 aleatorios
                    paisSelecionados = sorted(sample(self.pop, k=5), key=lambda i: i.fitness)[-2:]
                    self.cnt += len(self.pop)

                filho1, filho2 = recombinacao(paisSelecionados[0].getIndividuoInteger(), paisSelecionados[1].getIndividuoInteger(), tiporecomb)
                filho1 = Individuo(gen=filho1, ger=self.ger)
                filho2 = Individuo(gen=filho2, ger=self.ger)
                for i in [filho1, filho2]:
                    probMutacao = randint(0, 99)
                    if probMutacao < 40: i.mutate(tipomut)
                
                # Filhos substituem os pais na população
                if geracional:
                    for p in range(0,len(self.pop)):
                        if self.pop[p].__str__() == paisSelecionados[0].__str__():
                            self.pop[p] = filho1
                        if self.pop[p].__str__() == paisSelecionados[1].__str__():
                            self.pop[p] = filho2
                    self.pop.sort(key=lambda i: i.fitness)
                else:
                    # Remoção dos 2 piores
                    self.pop += [filho1, filho2]
                    self.pop.sort(key=lambda i: i.fitness)
                    self.pop = self.pop[2:]
                
                self.cnt += len(self.pop)
                    
            self.ger += 1
        # print(f'Geracoes: {self.ger} Avaliacoes de fitness: {self.cnt}')
        return self.pop[-1] if self.pop[-1].fitness == 1 else None

    def roleta(self):
        somatorio = 0
        for i in self.pop:
            somatorio += i.fitness
            self.cnt += len(self.pop)
        # Calcula soma do fitness total para dividir em percentual
        
        # fr = fitness_relativo, 
        # Divide os percentuais de acordo com valor fit
        fr = [(i.fitness/somatorio)*100 for i in self.pop]
        self.cnt += len(self.pop)
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

        pai1 = self.pop[roletado]

        while True:
            r = randint(0,100)
            roletado = 0
            pos_roleta = 0
            for pos, fit in enumerate(fr):
                if(pos_roleta < r):
                    pos_roleta += fit
                else:
                    roletado = pos
                    break
            pai2 = self.pop[roletado]
            if pai2 != pai1:
                break

        return [pai1, pai2]
