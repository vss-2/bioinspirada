from random import randint

# Exemplo do Slide
# input:
# pai1 = [1,3,5,2,6,4,7,8]
# pai2 = [8,7,6,5,4,3,2,1]
# p_crossover = 3
# output: [1, 3, 5, 4, 2, 8, 7, 6] [8, 7, 6, 2, 4, 1, 3, 5]

def recombinacao(gene1, gene2):
    n = len(gene1)
    p_crossover = randint(0,n-1)
    # print(p_crossover)
    filho1 = gene1[0:p_crossover]
    filho2 = gene2[0:p_crossover]

    for i in range(n):
        if gene2[(i + p_crossover) % n] not in filho1:
            filho1.append(gene2[(i + p_crossover) % n])
        
        if gene1[(i + p_crossover) % n] not in filho2:
            filho2.append(gene1[(i + p_crossover) % n])
    
    return filho1, filho2

# print(recombinacao([1,3,5,2,6,4,7,8], [8,7,6,5,4,3,2,1]))
