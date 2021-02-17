import csv
import os
from numpy import double, std, mean
from Populacao import Populacao
from recombinacao import recombinacao

arquivo = 0
arqnome = ''
execs = 30

def escrever(i, nec, med, dp, conv):
    with open(file=arqnome, mode='a', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow([i, nec, med, dp, conv])
    return

def avaliacao():
    resultados = [0,0,0,0]
    with open(file=arqnome, mode='r') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        next(leitor)
        for linha in leitor:
            if int(linha[4]) > 0: 
                resultados[0] += 1
            resultados[1] += double(linha[2])
            resultados[2] += double(linha[3])
            resultados[3] += int(linha[4])
    r1, r2, r3, r4 = resultados[0], resultados[1]/execs, resultados[2]/execs, resultados[3]
    print('Resultado do {}\nQuantas execuções o algoritmo convergiu: {}/{} \nMédia do Fitness Médio {} \nMédia do Desvio Padrão: {} \nNúmero de Indivíduos Convergentes: {}\n'.format(arqnome[7:], r1, execs, r2, r3, r4))
    return

def main():
    with open(file=arqnome, mode='w', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Execução', 'Execuções Necessárias', 'Fitness Médio', 'Desvio Padrão do Fitness', 'Número de Indivíduos Convergentes'])
    
    for i in range(1, execs+1):
        p = Populacao()
        p.generateSolution()
        exec_nec, ind_conv      = max([j.ger for j in p.pop]), [j.fitness for j in p.pop].count(1)
        ind_fit_med, ind_fit_dp = mean([j.fitness for j in p.pop]),    std([j.fitness for j in p.pop])
        print('Execuções Necessárias: {}\nFitness Médio: {}\nDesvio Padrão: {}\nNúmero de Indivíduos Convergentes: {}\n'.format(exec_nec, ind_fit_med, ind_fit_dp, ind_conv))
        escrever(i, exec_nec, ind_fit_med, ind_fit_dp, ind_conv)
    avaliacao()
    return

if __name__ == '__main__':
    arqnome = 'Testes/teste{}.csv'
    while os.path.isfile(arqnome.format(arquivo)):
        arquivo += 1
    arqnome = arqnome.format(arquivo)
    main()
