from random import randint

# Exemplo do Slide
# input:
# pai1 = [1,3,5,2,6,4,7,8]
# pai2 = [8,7,6,5,4,3,2,1]
# p_crossover = 3
# output: [1, 3, 5, 4, 2, 8, 7, 6] [8, 7, 6, 2, 4, 1, 3, 5]

def recombinacao(gene1, gene2, type=1):
    n = len(gene1)
    filho1, filho2 = [], []
    if type == 1:
        p_crossover = randint(1,n-2)
        # print(p_crossover)
        filho1 = gene1[0:p_crossover]
        filho2 = gene2[0:p_crossover]

        for i in range(n):
            if gene2[(i + p_crossover) % n] not in filho1:
                filho1.append(gene2[(i + p_crossover) % n])
            
            if gene1[(i + p_crossover) % n] not in filho2:
                filho2.append(gene1[(i + p_crossover) % n])
    
    # Cycle crossover
    # Source: https://codereview.stackexchange.com/questions/226179/easiest-way-to-implement-cycle-crossover
    elif type == 2:
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

print()
print(recombinacao(range(1, 10), [9,3,7,8,2,6,5,1,4], type=2)) # Exemplo do slide
# print(recombinacao([1,3,5,2,6,4,7,8], [8,7,6,5,4,3,2,1]))
