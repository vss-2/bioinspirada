from Individuo import Individuo

class Populacao:

    def __init__(self):
        self.pop = [Individuo() for i in range(100)]
