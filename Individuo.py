from random import randint, shuffle, sample

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

    def mutate(self, type=1):
        pos1, pos2 = sample(range(self.n), k=2)
        pos1, pos2 = min(pos1, pos2), max(pos1, pos2)
        if type == 1:
            self.gen[pos1], self.gen[pos2] = self.gen[pos2], self.gen[pos1]
        elif type == 2:
            self.gen = self.gen[:pos1+1] + [self.gen[pos2]] + [i for i in self.gen[pos1+1:] if i != self.gen[pos2]]


    

    @property
    def fitness(self):
        # Aqui vai o cálculo de quantas 
        # rainhas estão se atacando
        genInt = self.getIndividuoInteger()
        # Vetores de frequencia
        f_linha = [0] * self.n
        f_diag1 = [0] * (self.n * 2) # Diagonal principal
        f_diag2 = [0] * (self.n * 2) # Diagonal secundaria
        qtAtaques = 0
        for i in range(self.n):
            x = genInt[i]
            f_linha[x] += 1
            f_diag1[x + i] += 1
            f_diag2[self.n - x + i] += 1
        
        for i in range(2*self.n):
            x, y, z = 0, 0, 0
            if i < self.n: x = f_linha[i]
            y = f_diag1[i]
            z = f_diag2[i]

            qtAtaques += (x * (x - 1)) / 2
            qtAtaques += (y * (y - 1)) / 2
            qtAtaques += (z * (z - 1)) / 2

        return 1/(1 + qtAtaques)
