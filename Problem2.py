import numpy as np
from scipy.optimize import linprog

"""
First, Definition of the objective function (maximise Z):
The objective function is defined as an array c, 
where the coefficients are multiplied by -1 because linprog minimises instead of maximising
"""
c = [-3, -2]

"""
Definition of constraints: 
The constraints are specified by the matrix A (coefficients of the constraints) 
and the vector b (right-hand sides of the constraints)
"""
A = [
    [2, 1],  # Coefficients of the constraint 2x + y ≤ 10
    [1, 3]   # Coefficients of the constraint  x + 3y ≤ 12
]

"""
Definition of the Upper Limit of Constraints
"""
b = [10, 12]

"""
Definition of Limits for x and y using bounds
"""
x0_bounds = (0, None)  # x >= 0
x1_bounds = (0, None)  # y >= 0

"""
Problem solving using lingpro
"""
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

"""
If the solution is successful, the optimal values of x and y as well as the maximum value of Z are displayed
"""
if result.success:
    print("Optimum values:")
    print(f"x: {result.x[0]}")
    print(f"y: {result.x[1]}")
    print(f"Maximum value of Z: {-result.fun}")
else:
    print("An optimal solution could not be found.")
