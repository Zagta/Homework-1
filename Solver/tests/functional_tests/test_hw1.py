from unittest import result
import pytest
from Solver.main import ArgumentException

# Тест из п.3 - нет корней
def noRootsTest(solver):
    a, b, c = 2, 0, 1
    result = solver.solve(a, b, c)

    assert [] == result

# Тест из п.5 - два корня кратности 1
def twoRootsTest(solver):
    a, b, c = 1, 0, 1
    result = solver.solve(a, b, c)

    assert [1, -1] == result

# Тест из п.7 - один корень кратности 2
# И тест из п.11 - один корень кратности 2, дискриминант меньше заданного эпсилон
@pytest.mark.parametrize(
    ('a, b, c'),
    [
        (1, 2, 1),
        (1, 0, 1e-7),
    ]
)

def oneRootsTest(a, b, c, solver):
    result = solver.solve(a, b, c)

    assert [-1, -1] == result

# Тест из п.9 - коэффициент a не равен нулю
def nonZeroACoeff(solver):
    a, b, c = 0, 1, 2
    with pytest.raises(ArgumentException):
        solver.solve(a,b,c)

# Тест из п.13 - коэффиценты не числа
@pytest.mark.parametrize(
    ('a, b, c'),
    [
        (1, 1, '1'),
        (1, '1', '1'),
        ('1', '1', '1'),
    ]
)
def nonNumericCoeff(a, b, c, solver):
    with pytest.raises(ArgumentException):
        solver.solve(a, b, c)