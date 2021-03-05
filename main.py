import csv
import sys
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
    
    print('Resultado do {} \n\
        Quantas execuções o algoritmo convergiu: {}/{} \n\
        Média do Fitness Médio {} \n\
        Média do Desvio Padrão: {} \n\
        Número de Indivíduos Convergentes: {} \n'
        .format(arqnome[7:], r1, execs, r2, r3, r4))
    
    f = open(arqnome[:-4] + 'resultado.txt', 'w+')
    f.write('Resultado do {} \n\
        Quantas execuções o algoritmo convergiu: {}/{} \n\
        Média do Fitness Médio {} \n\
        Média do Desvio Padrão: {} \n\
        Número de Indivíduos Convergentes: {} \n'
            .format(arqnome[7:], r1, execs, r2, r3, r4))
    f.close()
    

    return

def main():

    if('--help' in sys.argv):
        print('\033[93m'+'Parâmetros: \n\
            --geracional True ou False. Padrão: False. \n\
                Indica se a seleção de sobreviventes utilizada será a geracional \n\
            --mutacao 1 ou 2. Padrão: 1. \n\
                Escolhe entre as duas opções de mutação \n\
                1: Mutação de troca de posição entre 2 valores \n\
                2: Mutação de troca de valores de uma região \n\
            --pop 0 à n (inteiro). Padrão: 100. \n\
                Define o tamanho "n" da população \n\
            --tabuleiro 0 à n (inteiro). Padrão: 8. \n\
                Define o tamanho do tabuleiro (e rainhas nele) \n\
            --roleta True ou False. Padrão: False. \n\
                Indica se o método de seleção dos pais vai ser roleta \n\
            --cruzamento 1 ou 2 ou 3. Padrão: 1. \n\
                Escolhe entre as três opções de recombinação \n\
                1: Cut and crossfill crossover \n\
                2: Cycle Crossover \n\
                3: Partially Mapped Crossover \n\
        '+'\033[92m')
        print(sys.argv)
        exit()
    else:
        print('\033[93m'+'Se tiver dúvidas, execute: py main.py --help'+'\033[0m')
    
    geracional = roleta = False
    mutacao = cruz = 1
    pop = 100
    tab = 8

    # Parser
    for sargs in range(0, len(sys.argv)):
        try:
            if sys.argv[sargs] == '--mutacao':
                mutacao = int(sys.argv[sargs+1])
            if sys.argv[sargs] == '--geracional':
                geracional = eval(sys.argv[sargs+1])
            if sys.argv[sargs] == '--roleta':
                roleta = eval(sys.argv[sargs+1])
            if sys.argv[sargs] == '--pop':
                pop = int(sys.argv[sargs+1])
            if sys.argv[sargs] == '--tabuleiro':
                tab = int(sys.argv[sargs+1])
            if sys.argv[sargs] == 'cruzamento':
                cruz = int(sys.argv[sargs+1])
        except:
            print('Erro de formatação do input!')
            exit()
    # print(mutacao, geracional, roleta, pop, tab, cruz)

    with open(file=arqnome, mode='w', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(['Execução', 'Execuções Necessárias', 'Fitness Médio', 
            'Desvio Padrão do Fitness', 'Número de Indivíduos Convergentes'])
    
    for i in range(1, execs+1):
        p = Populacao(n=tab, popsize=pop)
        p.generateSolution(geracional=geracional, roleta=roleta, tiporecomb=cruz, tipomut=mutacao)
        ind_conv = [j.fitness for j in p.pop].count(1)
        ind_fit_med, ind_fit_dp = mean([j.fitness for j in p.pop]),    std([j.fitness for j in p.pop])
        
        print('Execuções Necessárias: {} \n\
            Fitness Médio: {} \n\
            Desvio Padrão: {} \n\
            Número de Indivíduos Convergentes: {} \n'
            .format(p.ger-1, ind_fit_med, ind_fit_dp, ind_conv))

        escrever(i, p.ger-1, ind_fit_med, ind_fit_dp, ind_conv)
    avaliacao()
    return

if __name__ == '__main__':
    arqnome = 'Testes/teste{}.csv'
    while os.path.isfile(arqnome.format(arquivo)):
        arquivo += 1
    arqnome = arqnome.format(arquivo)
    main()

# py main.py --mutacao 2 --geracional True --roleta False --pop 8 --tabuleiro 9 --cruzamento 1
