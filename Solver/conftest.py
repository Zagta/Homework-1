import pytest
from main import QuadraticSolver

@pytest.fixture(scope='module')
def solver():
    return QuadraticSolver()