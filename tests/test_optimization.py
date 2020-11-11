from solutions.farm_optimization import FarmOptimization


def test_farm_optimization():

    # case_1: X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
    print('Given: X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1')
    case_1_soln = FarmOptimization(240.0, 320.0, 40.0, 30.0, 2.0, 1.0).solve()
    print('{corn} acres of corn, {oats} num acres oats'.format(corn=round(case_1_soln.x[0], 2),
                                                               oats=round(case_1_soln.x[1], 2)))

    # case_2: X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
    print('Given: X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1')
    case_2_soln = FarmOptimization(300.0, 380, 70.0, 45.0, 3.0, 1.0).solve()
    print('{corn} acres of corn, {oats} num acres oats'.format(corn=round(case_2_soln.x[0], 2),
                                                               oats=round(case_2_soln.x[1], 2)))

    # case_3: X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2
    print('Given: X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2')
    case_3_soln = FarmOptimization(180.0, 420.0, 65.0, 55, 3.0, 2.0).solve()
    print('{corn} acres of corn, {oats} num acres oats'.format(corn=round(case_3_soln.x[0], 2),
                                                               oats=round(case_3_soln.x[1], 2)))


if __name__ == '__main__':
    test_farm_optimization()
