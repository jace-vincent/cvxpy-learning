'''
The main entry point for the CVXPY learning project.
'''

from typing import Union
import cvxpy as cp
import pytest


def minimize_two_vars() -> None:
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
    optimal_value: Union[float, None] = None
    constraints: list[cp.Constraint] = [x >= 2, y <= 3]
    problem: cp.Problem = cp.Problem(cp.Minimize(x**2 + y**2), constraints)
    problem.solve()
    optimal_value = problem.value
    if problem.status not in ["optimal", "optimal_inaccurate"]:
        return None

    if optimal_value is None:
        raise ValueError("The problem does not have an optimal solution.")

    print(f"Optimal value: {optimal_value}")
    print(f"x: {x.value}, y: {y.value}")

    return None


def main() -> None:
    '''
    The main function that sets up and solves a simple optimization problem using CVXPY.
    '''
    try:
        minimize_two_vars()
    except ValueError as e:
        pytest.fail(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
