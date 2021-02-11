from random import randint, shuffle

class Individuo:
    def __init__(self, n = 8, gen=None):
        if not gen:
            qtBits = len(bin(n-1)[2:])
            self.gen = [str(('0' * qtBits) + format(i, 'b'))[-qtBits:] for i in range(n)]
            shuffle(self.gen)
        else:
            self.gen = gen
        
    def getIndividuoCompleto(self):
        return ''.join(self.gen)
    
    def getIndividuoInteger(self):
        return [int(x, 2) for x in self.gen]

    

    @property
    def fitness(self):
        # Aqui vai o cálculo de quantas 
        # rainhas estão se atacando
        n = 0
        return 1/(1 + n)