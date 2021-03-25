# Input usado
# k = [1, 0, 4, 7, 2, 5, 6, 3]
k = ['110', '000', '010', '111', '101', '011', '001', '100']
k = [int(x, 2) for x in k]
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
# https://towardsdatascience.com/computing-number-of-conflicting-pairs-in-a-n-queen-board-in-linear-time-and-space-complexity-e9554c0e0645
qtd_ataques = 0
n = len(k)
# Vetores de frequencia
f_linha = [0] * n
f_diag1 = [0] * (n * 2) # Diagonal principal
f_diag2 = [0] * (n * 2) # Diagonal secundaria
for i in range(n):
    x = k[i]
    f_linha[x] += 1
    f_diag1[x + i] += 1
    f_diag2[n - x + i + 1] += 1

for i in range(2*n):
    x, y, z = 0, 0, 0
    if i < n: x = f_linha[i]
    y = f_diag1[i]
    z = f_diag2[i]

    qtd_ataques += (x * (x - 1)) / 2
    qtd_ataques += (y * (y - 1)) / 2
    qtd_ataques += (z * (z - 1)) / 2
print('Quantidade de ataques: {}'.format(qtd_ataques))

