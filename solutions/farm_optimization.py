from scipy.optimize import minimize

'''
    Write a generic function to compute various scenarios for the following optimization problem: 
    A farmer owns X acres of land. She profits P1 dollars per acre of corn and P2 dollars per acre of oats. 
    Her team has Y hours of labor available. The corn takes H1 hours of labor per acre and 
    oats require H2 hours of labor per acre. How many acres of each can be planted to maximize profits?
    
    Analysis:
    
        - Equations:
        
            -- objective - maximize
            
                - X * (p1 * c1 + p2 * c2) = P
                
                    
                    where:
                    
                        - X - acres of land
                        - p1 - profit per acre of land of corn ($/acre)
                        - p2 - profit per acre of land of oats ($/acre)
                        - c1 - fraction of land allocated to corn (unit-less)
                        - c2 - fraction of land allocated to oats (unit-less)
        
                    dimensional analysis:
                    
                        - acre * ( $/acre + $/acre) = $
            
            -- constraints
            
                - X * (c1 * h1 + c2 * h2) <= Y
            
                where:
                
                    - Y - hours of labor available (hr)
                    - h1 - hours of labor per acre of corn (hr/acre)
                    - h2 - hours of labor per acre of oats (hr/acre)
                    
                dimensional analysis:
                
                    - hr = acre * (hr/acre + hr/acre)
                            
                - c1 + c2 = 1
            
            -- bounds
                
                - 0 <= c1 <= 1
                
                - 0 <= c2 <= 1

X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
X = 300, Y = 380, P1 = $70, P2 = $  45, H1 = 3, H2 = 1
X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2        

'''


class FarmOptimization:

    def __init__(self,
                 acre_avail,
                 hr_labor_available,
                 prof_per_acre_corn,
                 prof_per_acre_oat,
                 hr_per_acre_corn,
                 hr_per_acre_oat
                 ):
        self.acre_available = acre_avail                    # X
        self.hour_labor_available = hr_labor_available      # Y
        self.profit_per_acre_of_corn = prof_per_acre_corn   # p1
        self.profit_per_acre_of_oat = prof_per_acre_oat     # p2
        self.hour_labor_per_acre_corn = hr_per_acre_corn    # h1
        self.hour_labor_per_acre_oat = hr_per_acre_oat      # h2
        # MAXIMIZE X * (p1 * c1 + p2 * c2) or MINIMIZE -1 * X * (p1 * c1 + p2 * c2)
        self.objective_fxn = \
            lambda c1, c2: -1.0 * self.acre_available * (self.profit_per_acre_of_corn * c1 +
                                                         self.profit_per_acre_of_oat * c2)
        # Y - X * (c1 * h1 + c2 * h2) >= 0
        self.labor_constraint = \
            lambda c1, c2: (self.hour_labor_available - self.acre_available * (c1 * self.hour_labor_per_acre_corn +
                                                                               c2 * self.hour_labor_per_acre_oat))
        # c1 + c2 = 1
        self.corn_and_oat_acre_scalar_constraint = lambda c1, c2: (1 - (c1 + c2))
        # 0 <= c1 <= 1
        self.acre_scalar_bounds = (0.0, 1.0)                # 0 <= c1, c2 <= 1

    def objective(self, x):
        # MAXIMIZE X * (p1 * c1 + p2 * c2)
        c1 = x[0]
        c2 = x[1]
        return self.objective_fxn(c1, c2)

    def constraint_1(self, x):
        # Y - X * (c1 * h1 + c2 * h2) >= 0
        c1 = x[0]
        c2 = x[1]
        return self.labor_constraint(c1, c2)

    def constraint_2(self, x):
        # 1 - (c1 + c2) == 0
        c1 = x[0]
        c2 = x[1]
        return self.corn_and_oat_acre_scalar_constraint(c1, c2)

    def solve(self):
        obj = self.objective
        bounds = (self.acre_scalar_bounds, self.acre_scalar_bounds)
        const_1 = {'type': 'eq', 'fun': self.constraint_1}
        const_2 = {'type': 'eq', 'fun': self.constraint_2}
        constraints = [const_1, const_2]
        initial_guess = (0.5, 0.5)  # half corn, half oat
        solution = minimize(
            obj,
            initial_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
        )
        return solution


if __name__ == '__main__':
    '''
        case_1: X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
        case_2: X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
        case_3: X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2        
    '''
    case_1_soln = FarmOptimization(240.0, 320.0, 40.0, 30.0, 2.0, 1.0).solve()
    case_2_soln = FarmOptimization(300.0, 380, 70.0, 45.0, 3.0, 1.0).solve()
    case_3_soln = FarmOptimization(180.0, 420.0, 65.0, 55, 3.0, 2.0).solve()
