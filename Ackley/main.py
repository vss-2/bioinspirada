from Populacao import Populacao
from timeit import default_timer as timer
import pickle

# Recombinacao
# 1 == discreta
# 2 == intermediária
# 3 == roubada

# Mutação
# 1 == Uniforme
# 2 == std
# 3 == sigma1
# 4 == sigma2
# 5 == roubada

# Selecao de pais
# 1 == Aleatoria
# 2 == Elitista

# Selecao Sobreviventes
# 1 == (mi, lambda)
# 2 == (mi + lambda)

# with open('a', 'wb') as arquivo:
#     pickle.dump({'populacao': [1, 2, 3]}, arquivo)

# with open('a', 'rb') as arquivo:
#     a = pickle.load(arquivo)
#     print(a)

combinacoes = [
    [1,1,1,1],
    [2, 2, 2, 1],
    [3, 1, 1, 2],
    [2, 3, 2, 1],
    [2, 4, 2, 1],
    [2, 4, 2, 2],
    [1, 5, 1, 2],
    [3, 5, 2, 1]
]

for combinacao in combinacoes:
    ti = timer()
    p = Populacao()
    p.gerar_solucao(combinacao[0], combinacao[1], combinacao[2], combinacao[3])
    tempo = timer() - ti
    with open(''.join(str(c) for c in combinacao), 'wb') as arquivo:
        pickle.dump({'populacao': p.populacao, 'execucoes': p.geracoes, 'tempo': tempo}, arquivo)


