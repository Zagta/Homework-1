import pytest
from Solver.main import QuadraticSolver

@pytest.fixture(scope='module')
def solver():
    return QuadraticSolver()