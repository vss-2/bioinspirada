from Individuo import Individuo
from constants import GENE_SIZE, MAX_GERACAO
from selecao_pais import selecao_pais
from recombinacao import recombinacao
from mutacao import mutacao
from numpy.random import uniform, randint
from random import sample
from copy import deepcopy


class Populacao:

    def __init__(self):
        self.populacao = []

        while len(self.populacao) < 50:
            i = [uniform(-15, 15) for _ in range(GENE_SIZE)]
            if i not in self.populacao:
                self.populacao.append(i)
        
        self.populacao = [Individuo(genes=i) for i in self.populacao]
        self.populacao.sort(key=lambda i: i.fitness)

        self.geracoes = 0

    def gerar_solucao(self, tipo_recombinacao=1, tipo_mutacao=1, tipo_selecao_pais=1, tipo_selecao_sobreviventes=1):
        while self.geracoes < MAX_GERACAO and self.populacao[-1].fitness < 1:
            self.geracoes += 1
            print(f'{self.geracoes} {self.populacao[-1].fitness}')
            filhos = []

            for _ in range(400):
                paisSelecionados = selecao_pais(self.populacao, tipo_selecao_pais)
                filhos.append(recombinacao(paisSelecionados[0], paisSelecionados[1], tipo_recombinacao))

            for i in range(len(filhos)):
                mutacao(filhos[i], tipo_mutacao)

            # (mi, lambda)
            if tipo_selecao_sobreviventes == 1:
                filhos.sort(key=lambda i: i.fitness)
                self.populacao = filhos[-50:]
            # (mi, lambda)
            elif tipo_selecao_sobreviventes == 2:
                for i in range(len(self.populacao)):
                    mutacao(self.populacao[i], tipo_mutacao)
                
                self.populacao += filhos
                self.populacao.sort(key=lambda i: i.fitness)
                self.populacao = self.populacao[-50:]


            self.populacao.sort(key=lambda i: i.fitness)
            
    




