# Observacoes das execucoes

## Default

* Não converge em todo, entre 12 a 18
* Fitness médio de +/- 0.24

## Geracional Roleta

* Todos convergiram
* Fitness médio de 0.185

## Pop 50

* Não convergiu todos: entre 19 a 21
* Fitness médio de 0.35

## Pop 50 Roleta

* Todos convergiram
* Fitness médio de 0.35

## Mutacao 2 Geracional CX

* Convergiram 14 a 16
* Fitness médio de 0.17

## Mutacao 2 Geracional Roleta CX

* Todos convergiram
* Fitness médio de 0.18

## Roleta CX

* Todos Convergiram
* Fitness médio de 0.271

## Roleta PMX
Melhor até agora
* Todos Convergiram
* Fitness médio de 0.295

## Pop 200 Roleta

* Todos convergiram, principalmente na geracao da populacao
* Fitness médio de 0.27

# Convergencia de todos

Todos com roleta, com os 3 cruzamentos diferentes
Convergir todos 10 vezes

* Aleatório
    * [762, 411, 690, 779, 293, 488, 456, 527, 566, 641]
    * Média: 561.3
    * Std: 149.27
    * 15 segundos
    * p-value: 0.88
* Cruzamento CX:
    * [602, 333, 288, 442, 514, 307, 423, 495, 313, 467]
    * Média: 418.4
    * Std: 99.735
    * 29 segundos
    * p-value: 0.46
* Cruzamento PMX:
    * [596, 501, 531, 799, 686, 998, 542, 441, 819, 695]
    * Média: 660.8
    * Std: 163.9
    * 28 segundos
    * p-value: 0.61

Os 3 são normais (parametricos) de acordo com o teste de Shapiro. Os p-values deram grandes e a hipotese nula nao foi negada

* t_test aleatorio e CX: 0.02, ou seja, a hipotese nula foi rejeitada, logo são estatisticamente diferentes.
* t_test aleatorio e PMX: 0.19, ou seja, a hipotese nula não foi rejeitada, logo são estatisticamentes semelhantes.
* t_test CX e PMX: 0.07, ou seja, a hipotese nula foi rejeitada, logo são estatisticamente diferentes.

