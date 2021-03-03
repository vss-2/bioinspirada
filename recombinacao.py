from random import randint
import numpy as np

# Exemplo do Slide
# input:
# pai1 = [1,3,5,2,6,4,7,8]
# pai2 = [8,7,6,5,4,3,2,1]
# p_crossover = 3
# output: [1, 3, 5, 4, 2, 8, 7, 6] [8, 7, 6, 2, 4, 1, 3, 5]

def recombinacao(gene1, gene2, tipo=1):
    n = len(gene1)
    filho1, filho2 = [], []
    if tipo == 1:
        p_crossover = randint(1,n-2)
        # print(p_crossover)
        filho1 = gene1[0:p_crossover]
        filho2 = gene2[0:p_crossover]

        for i in range(n):
            if gene2[(i + p_crossover) % n] not in filho1:
                filho1.append(gene2[(i + p_crossover) % n])
            
            if gene1[(i + p_crossover) % n] not in filho2:
                filho2.append(gene1[(i + p_crossover) % n])
        
        return filho1, filho2
    
    # Cycle crossover
    # Source: https://codereview.stackexchange.com/questions/226179/easiest-way-to-implement-cycle-crossover
    elif tipo == 2:
        cycles = [-1] * n
        cycle_id = 0
        cyclestart = (i for i, v in enumerate(cycles) if v < 0) # construtor que vai manter os indices dos cycles < 0
        for pos in cyclestart:
            # print(pos, end= " ")
            # print(cycles)
            # Quando cycle[pos] != -1, fechou o ciclo
            while cycles[pos] < 0:
                cycles[pos] = cycle_id
                pos = gene1.index(gene2[pos])
            
            cycle_id += 1

        filho1 = [gene1[i] if n % 2 else gene2[i]
                for i, n in enumerate(cycles)]
        filho2 = [gene2[i] if n % 2 else gene1[i]
                for i, n in enumerate(cycles)]
        
        # print(cycles)
        return filho1, filho2

    elif tipo == 3:
        # Source: https://stackoverflow.com/questions/53254449/how-to-perform-partial-mapped-crossover-in-python3
        
        ''' Exemplo usado no slide (que resulta em apenas no output: [9 3 2 4 5 6 7 1 8]):
            parent1 = [1,2,3,4,5,6,7,8,9]    
            parent2 = [9,3,7,8,2,6,5,1,4]
            firstCrossPoint = 3
            secondCrossPoint = 7
        '''

        parent1 = gene1
        parent2 = gene2

        firstCrossPoint = np.random.randint(0,len(parent1)-2)
        secondCrossPoint = np.random.randint(firstCrossPoint+1,len(parent1)-1)

        # print(firstCrossPoint, secondCrossPoint)

        parent1MiddleCross = parent1[firstCrossPoint:secondCrossPoint]
        parent2MiddleCross = parent2[firstCrossPoint:secondCrossPoint]

        temp_child1 = parent1[:firstCrossPoint] + parent2MiddleCross + parent1[secondCrossPoint:]

        temp_child2 = parent2[:firstCrossPoint] + parent1MiddleCross + parent2[secondCrossPoint:]

        relations = []
        for i in range(len(parent1MiddleCross)):
            relations.append([parent2MiddleCross[i], parent1MiddleCross[i]])

        # print(relations)

        # As recursões servem pra "traçar as retas do slide", ou seja:
        # ir de um pai ao outro pai para encontrar onde está o inteiro correspondente, 
        # caso esteja na região de crossover ou não

        def recursion1(temp_child , firstCrossPoint , secondCrossPoint , parent1MiddleCross , parent2MiddleCross) :
            child = np.array([0 for i in range(len(parent1))])
            for i,j in enumerate(temp_child[:firstCrossPoint]):
                c=0
                for x in relations:
                    if j == x[0]:
                        child[i]=x[1]
                        c=1
                        break
                if c==0:
                    child[i]=j
            j=0
            for i in range(firstCrossPoint,secondCrossPoint):
                child[i]=parent2MiddleCross[j]
                j+=1

            for i,j in enumerate(temp_child[secondCrossPoint:]):
                c=0
                for x in relations:
                    if j == x[0]:
                        child[i+secondCrossPoint]=x[1]
                        c=1
                        break
                if c==0:
                    child[i+secondCrossPoint]=j
            child_unique=np.unique(child)
            if len(child)>len(child_unique):
                child=recursion1(child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
            return(child)

        def recursion2(temp_child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross):
            child = np.array([0 for i in range(len(parent1))])
            for i,j in enumerate(temp_child[:firstCrossPoint]):
                c=0
                for x in relations:
                    if j == x[1]:
                        child[i]=x[0]
                        c=1
                        break
                if c==0:
                    child[i]=j
            j=0
            for i in range(firstCrossPoint,secondCrossPoint):
                child[i]=parent1MiddleCross[j]
                j+=1

            for i,j in enumerate(temp_child[secondCrossPoint:]):
                c=0
                for x in relations:
                    if j == x[1]:
                        child[i+secondCrossPoint]=x[0]
                        c=1
                        break
                if c==0:
                    child[i+secondCrossPoint]=j
            child_unique=np.unique(child)
            if len(child)>len(child_unique):
                child=recursion2(child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
            return(child)

        child1=recursion1(temp_child1,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
        child2=recursion2(temp_child2,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)

        # print(child1, child2, sep='\n')
        return child1.tolist(), child2.tolist()

# print()
# print(recombinacao(range(1, 10), [9,3,7,8,2,6,5,1,4], tipo=2)) # Exemplo do slide
# print(recombinacao([1,3,5,2,6,4,7,8], [8,7,6,5,4,3,2,1]))

# print(recombinacao([1,2,3,4,5,6,7,8,9],[9,3,7,8,2,6,5,1,4], tipo=3))
# Nota: resultados mudam a cada execução devido ao random no ponto crossover, sette lá em cima :) 