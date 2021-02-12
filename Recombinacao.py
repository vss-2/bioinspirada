from random import randint

# Exemplo do Slide
# input:
# pai1 = [1,3,5,2,6,4,7,8]
# pai2 = [8,7,6,5,4,3,2,1]
# p_crossover = 3
# output: [1, 3, 5, 4, 2, 8, 7, 6] [8, 7, 6, 2, 4, 1, 3, 5]

def Recombinacao(gene1, gene2):
    p_crossover = randint(0,len(gene1)-1)
    # print(p_crossover)
    slice1 = gene1[0:p_crossover]
    slice2 = gene2[0:p_crossover]

    for i in gene2[p_crossover:]:
        if i not in slice1:
            slice1.append(i)
    for i in range(8):
        if(len(slice1) < len(gene1)):
            slice1.append(slice2[i])
        else:
            break

    for i in gene1[p_crossover:]:
        if i not in slice2:
            slice2.append(i)
    for i in range(8):
        if(len(slice2) < len(gene2)):
            slice2.append(slice1[i])
        else:
            break
    
    return slice1, slice2

# print(recombinacao([1,3,5,2,6,4,7,8], [8,7,6,5,4,3,2,1]))
