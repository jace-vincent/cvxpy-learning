'''
The main entry point for the CVXPY learning project.
'''

from typing import Union
import cvxpy as cp


def main() -> None:
    '''
    The main function that sets up and solves a simple optimization problem using CVXPY.
    '''
    # Example problem: Minimize x^2 + y^2 subject to x + y = 1
    x: cp.Variable = cp.Variable()
    y: cp.Variable = cp.Variable()
    objective: Union[cp.Minimize, cp.Maximize] = cp.Minimize(x**2 + y**2)
    constraints: list[cp.Constraint] = [x + y == 1]
    problem: cp.Problem = cp.Problem(objective, constraints)

    # Solve the problem
    problem.solve()

    if problem.status != cp.OPTIMAL:
        raise ValueError("The problem does not have an optimal solution.")

    print(f"Optimal value: {problem.value}")
    print(f"x: {x.value}, y: {y.value}")


if __name__ == "__main__":
    main()
