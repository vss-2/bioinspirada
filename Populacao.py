from Individuo import Individuo

class Populacao:

    def __init__(self, n=8):
        self.pop = [Individuo(n) for i in range(100)]
