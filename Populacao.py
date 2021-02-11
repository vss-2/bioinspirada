from Individuo import Individuo

class Populacao:

    def __init__(self, n=8,ger=0):
        self.pop = [Individuo(n, None, ger) for i in range(100)]
