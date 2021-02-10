from random import randint, shuffle

class Individuo:

    def __init__(self):
        self.gen = []
        for i in range(8):
            str_bin = str('000' + format(i, 'b'))[-4:]
            self.gen.append(str_bin)
        shuffle(self.gen)
        
    def getIndividuoCompleto(self):
        return ''.join(self.gen)
    
    def getIndividuoInteger(self):
        return [int(x, 2) for x in self.gen]

    @property
    def fitness():
        # Aqui vai o cálculo de quantas 
        # rainhas estão se atacando
        n = 0
        return 1/(1 + n)