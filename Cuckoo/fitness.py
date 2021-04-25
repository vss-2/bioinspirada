# output: fit_array,spikes,classesTR
def fitness(Weights, Nests, Data, Classes):

    # [samples, temp] = numpy.size(Data)
    samples = len(Data["data"])

    T = 1000
    fit_array = [0] * Nests
    # Cria array com 1xN (1 dimensão com N zeros)

    # Basicamente ncl = numero de membros pertencentes a cada classe
    # Então ele calcula quantas existem e guarda isso nas 3 linhas abaixo
    ncl = [0] * Classes
    for i in range(0, Classes):
        ncl[i] = len(list(filter(lambda x: x == i, Data["target"])))

    spikes = [None] * Classes
    for i in range(0, Classes):
        # Cria array Nx1 (N dimensões com 1 valor em cada)
        spikes[i] = [[] for x in range(0, Classes)]

    me = [None] * samples
    for ind in range(0, Nests):
        inx = [1] * Classes
        for i in range(0, samples):
            spikes = []
        for i in range(0, Classes):
            me[i] = mean(spikes[i])

    [crTR, classesTR] = performance(Classes, samples, spikes, me)
    fit1 = crTR
    fit_array[ind] = fit1

    return (fit_array, spikes, classesTR)
