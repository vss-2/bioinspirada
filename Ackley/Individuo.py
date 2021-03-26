from utils import fitness
from constants import GENE_SIZE
from numpy.random import uniform


class Individuo:

    def __init__(self, genes=None, paces=None):
        if not genes: 
            self.genes = [uniform(-15, 15) for _ in range(GENE_SIZE)]
        else:
            self.genes = genes

        if not paces:
            self.paces = [uniform(0, 2) for _ in range(GENE_SIZE)]
        else:
            self.paces = paces

    @property
    def fitness(self):
        return fitness(self.genes)

    def __str__(self):
        return ''.join(f'{str(g)} ' for g in self.genes)
