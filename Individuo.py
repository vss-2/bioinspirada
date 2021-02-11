from random import randint, shuffle

class Individuo:
    def __init__(self, n = 8, gen=None, ger=None):
        if not gen:
            self.gen = [str('000' + format(i, 'b'))[-3:] for i in range(n)]
            shuffle(self.gen)
        else:
            self.gen = gen
            
        if not ger:
            self.ger = 0
        else:
            self.ger = ger
        
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