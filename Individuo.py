from random import randint

class Individuo:

    def __init__(self, vetor):
        self.gen = []
        for i in vetor:
            str_bin = bin(i)[2:]
            str_bin = '000'[:-len(str_bin)] + str_bin
            self.gen.append(str_bin)
            print(self.gen)
        
    def getIndividuoCompleto(self):
        return ''.join(self.gen)
    
    def getIndividuoInteger(self):
        return [int(x, 2) for x in self.gen]

    def mutacao():
        return bin(randint(0,7))[2:]
