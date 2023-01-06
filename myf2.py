"""Документация модуля. Описывает работу классов и функций. 
Размещается в верхней части файла (начиная с первой строки).
"""
def tricky_func(self):
    """Описывает работу функции tricky_func."""
    i = 10


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки 
        документации.
        """
        i=101


print(__doc__)
print('---------')
print(tricky_func.__doc__)
print('---------')
print(Test.__doc__)
print('---------')
print(Test.first.__doc__)