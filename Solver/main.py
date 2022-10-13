import math
from typing import List

# Класс для кастомной ошибки
class ArgumentException(Exception):
    pass

# Класс для решения квадратного уравнения ax^2 + bx + c = 0
class QuadraticSolver:
    # Метод вычисления дискриминанта
    def _calculateDiscriminant(self, a: float, b: float, c: float) -> float:
        
        return math.qrt(b) - 4 * a * c

    # Метод нахождения корней уравнения
    def _calculateSquareRoots(self, D: float, a: float, b: float) -> float:
        sqrtFromD = math.sqrt(D)
        rootA = (-b + sqrtFromD) / (2 * a)
        rootB = (-b - sqrtFromD) / (2 * a)
        
        return [rootA, rootB]
    
    # Метод решения квадратного уравнения
    def solve(self, a: float, b: float, c: float, eps: float = 1e-5) -> List[float]:
        # ###
        # Находим дискриминант
        D = self._calculateDiscriminant(a, b, c)

        # Если меньше нуля, то нет корней
        if (D < 0):
            return []
        
        # Если по модулю меньше заданного эпсилона
        if (abs(D) < eps):
            rootA, rootB = self._calculateSquareRoots(0, a, b)
            return [rootA, rootB]
        
        # Если больше или равен заданного эпсилона
        rootA, rootB = self._calculateSquareRoots(D, a, b)
        
        return [rootA, rootB]