'''
The main entry point for the CVXPY learning project.
'''

from typing import Union
import cvxpy as cp


def minimize_two_vars() -> Union[float, None]:
    '''
    Create a CVXPY objective to minimize the sum of squares of two variables.

    Args:
        x (cp.Variable): The first variable.
        y (cp.Variable): The second variable.

    Returns:
        Union[float, None]: The optimal value of the optimization problem, or None if infeasible.
    '''
    x: cp.Variable = cp.Variable()
    y: cp.Variable = cp.Variable()
    constraints: list[cp.Constraint] = [x + y == 1, x >= 2, y <= 3]
    problem: cp.Problem = cp.Problem(cp.Minimize(x**2 + y**2), constraints)
    result: float = problem.solve()
    if problem.status not in ["optimal", "optimal_inaccurate"]:
        return None
    return result


def main() -> None:
    '''
    The main function that sets up and solves a simple optimization problem using CVXPY.
    '''
    x: cp.Variable = cp.Variable()
    y: cp.Variable = cp.Variable()
    optimal_value: Union[float, None] = minimize_two_vars()

    if optimal_value is None:
        raise ValueError("The problem does not have an optimal solution.")

    print(f"Optimal value: {optimal_value}")
    print(f"x: {x.value}, y: {y.value}")


if __name__ == "__main__":
    main()
