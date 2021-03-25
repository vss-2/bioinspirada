from Populacao import Populacao
from numpy import mean, std
from scipy.stats import shapiro, ttest_ind, ttest_rel
from itertools import combinations

def main():
    ans = []
    for tr in [1,2,3]:
        temp = []
        for i in range(50):
            a = Populacao()
            a.generateSolution(roleta=True, tiporecomb=tr)
            temp.append(a.ger)
        print(temp)
        ans.append(temp)

    # print(ans)
    # print(mean(ans))
    # print(std(ans))

    # r1 = [762, 411, 690, 779, 293, 488, 456, 527, 566, 641]
    # r2 = [602, 333, 288, 442, 514, 307, 423, 495, 313, 467]
    # r3 = [596, 501, 531, 799, 686, 998, 542, 441, 819, 695]

    for i in ans:
        print(shapiro(i))

    print()

    cruzamentos = {
        0: "Aleatorio",
        1: "CX",
        2: "PMX"
    }

    # # for i in [r1, r2, r3]:
    # #     print(ttest_ind(i))
    # print(ttest_ind(r2, r3))

    pairs = list(combinations(list(range(3)), 2))

    for p in pairs:
        print(f't_test entre {cruzamentos[p[0]]} e {cruzamentos[p[1]]}')
        print(ttest_ind(ans[p[0]], ans[p[1]]))
        print()


if __name__ == "__main__":
    for i in range(5):
        main()