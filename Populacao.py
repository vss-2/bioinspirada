from Individuo import Individuo

class Populacao:

    def __init__(self, n=8,g=0):
        self.pop = [Individuo(n, None, g) for i in range(100)]
