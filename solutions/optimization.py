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
                - 0 <= c1 <= 1
                - 0 <= c2 <= 1
        
'''

def objective(x):
    return

def constraint1():
    return

