from random import randint, shuffle

class Individuo:
    def __init__(self, n=8, gen=None, ger=0):
        if not gen:
            qtBits = len(bin(n-1)[2:])
            self.gen = [str(('0' * qtBits) + format(i, 'b'))[-qtBits:] for i in range(n)]
            shuffle(self.gen)
        else:
            qtBits = len(bin(max(gen))[2:])
            self.gen = [str(('0' * qtBits) + format(i, 'b'))[-qtBits:] for i in gen]
        
        self.n = len(self.gen)
        self.ger = ger
        
    def getIndividuoCompleto(self):
        return ''.join(self.gen)
    
    def getIndividuoInteger(self):
        return [int(x, 2) for x in self.gen]

    

    @property
    def fitness(self):
        # Aqui vai o cálculo de quantas 
        # rainhas estão se atacando
        genInt = self.getIndividuoInteger()
        qtAtaques = 0
        for i in range(self.n):
            # x == linha == valor na posicao do gene
            # y == coluna == posicao do gene
            x, y = genInt[i], i
            xb, yb  = x, y
            ataques = 0

            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    xb, yb = x, y
                    while(0 <= xb < self.n and 0 <= yb < self.n):
                        if xb != x and yb != y and xb == genInt[yb]:
                            ataques += 1
                        xb += dx
                        yb += dy
            
            qtAtaques += ataques

        return 1/(1 + qtAtaques)
