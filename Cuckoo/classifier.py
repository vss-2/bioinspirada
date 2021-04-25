from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

Lb = -20
Ub =  20

iter      = 100
Nests     = 40
lambda    = 1.5 
pa        = 0.25
alpha     = 1
Tolerance = 0.90
fitness   = 'fitness' # Pode ser 'fitness' ou 'fitness2'

for dataset in [load_iris(), load_wine(), load_breast_cancer()]:
    # Divide treino em 25% e teste em 75%
    DataTrain = dataset['data'][:len(dataset['data'])//4]
    DataTest = dataset['data'][len(dataset['data'])//4:]
    Classes = len(dataset['target_names'])
    features = len(dataset['data'][0])
    dim = features - 1

    [x, iter, fitness_array, weights] = cuckoo_search(fitness, Tolerance, dim, Lb, Ub, Nests, DataTrain, Classes, iter, lambda, alpha, pa)

    [crTR, spikesTR, classesTR] = fitness(x, 1, DataTrain, Classes)
    [crTE, spikesTE, classesTE] = fitness(x, 1, DataTest, Classes)
    print('Percentual de reconhecimento usando conjunto de treino: ', 100*crTR)
    print('Percentual de reconhecimento usando conjunto de teste: ', 100*crTE)
