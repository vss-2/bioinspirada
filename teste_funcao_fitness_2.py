# Input usado
# k = [1, 0, 4, 7, 2, 5, 6, 3]
# k = ['110', '000', '010', '111', '101', '011', '001', '100']
# k = [int(x, 2) for x in k]
''' Representação gráfica
. x . . . . . .
x . . . . . . .
. . . . x . . . 
. . . . . . . x
. . x . . . . .
. . . . . x . .
. . . . . . x .
. . . x . . . .
'''
''' (linha, coluna): ataque 
Output:
Ataques da 0, 1: 1
Ataques da 1, 0: 1
Ataques da 2, 4: 1
Ataques da 3, 7: 2
Ataques da 4, 2: 1
Ataques da 5, 5: 3
Ataques da 6, 6: 1
Ataques da 7, 3: 2
Quantidade de ataques: 12
'''
# Criar def aqui: parametros (dar replace k[xb] por self.gen[xb], replace nos 8 por len(self.gen))
qtd_ataques = 0
increments = [-1, 1]
n = len(k)
for i in range(n):
    # x == linha == valor na posicao do gene
    # y == coluna == posicao do gene
    x, y = k[i], i
    xb, yb  = x, y
    ataques = 0

    for dx in increments:
        for dy in increments:
            xb, yb = x, y
            while(0 <= xb < n and 0 <= yb < n):
                if xb != x and yb != y and xb == k[yb]:
                    ataques += 1
                xb += dx
                yb += dy
    
    print('Ataques da {}, {}: {}'.format(x, y, ataques))
    qtd_ataques += ataques

print('Quantidade de ataques: {}'.format(qtd_ataques))

