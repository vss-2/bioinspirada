# Input usado
k = [1, 0, 4, 7, 2, 5, 6, 3]
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
for i in range(len(k)):
    x, y = i, k[i]
    posicao = (x,y)
    xb, yb  = posicao[0], posicao[1]
    ataques = 0
    while(xb >= 0 and yb >= 0):
        if(xb != posicao[0] and yb != posicao[1]):
            if(yb == k[xb]):
                ataques += 1
        xb -= 1
        yb -= 1

    xb, yb = posicao[0], posicao[1]

    while(xb < 8 and yb < 8):
        if(xb != posicao[0] and yb != posicao[1]):
            if(yb == k[xb]):
                ataques += 1
        xb += 1
        yb += 1

    xb, yb = posicao[0], posicao[1]

    while(xb < 8 and yb < 8 and xb >= 0 and yb >= 0):
        if(xb != posicao[0] and yb != posicao[1]):
            if(xb == k[yb]):
                ataques += 1
        xb += 1
        yb -= 1

    xb, yb = posicao[0], posicao[1]

    while(xb < 8 and yb < 8):
        if(xb != posicao[0] and yb != posicao[1]):
            if(yb == k[xb]):
                ataques += 1
        xb -= 1
        yb += 1
    
    print('Ataques da {}, {}: {}'.format(x, y, ataques))
    qtd_ataques += ataques

print('Quantidade de ataques: {}'.format(qtd_ataques))
