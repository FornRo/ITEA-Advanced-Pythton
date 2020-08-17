# Создать класс комплексного числа и реализовать для него арифметические операции.
import re


class CompleksNumbers:
    """
    >>> a = CompleksNumbers('3x')
    >>> a + a, a - a, a * a, a / a
    ((6.0, 'x'), (0.0, 'x'), (9.0, 'x'), (1.0, 'x'))

    >>> b = CompleksNumbers('3y')
    >>> a + b
    'Комплексные числа не совпадают'
    """
    error1 = 'Класы не совпадают'
    error2 = 'Комплексные числа не совпадают'
    def __init__(self, com_num):
        self.com_num = com_num
        compleks_numbers = re.findall(r'(\d+)(\w)', com_num)
        self.number, self.leter = float(compleks_numbers[0][0]), compleks_numbers[0][1]

    @staticmethod
    def is_instance(other):
        return True if isinstance(other, CompleksNumbers) else False

    def is_label_identical(self, other):
        return True if self.leter == other.leter else False

    def __repr__(self):
        return f'CompleksNumbers("{self.number}{self.leter}")'

    def __str__(self):
        return f'CompleksNumbers: {self.number}, {self.leter}'

    def __add__(self, other):
        if self.is_instance(other):
            return (self.number + other.number, self.leter) if self.is_label_identical(other) \
                else self.error2
        else:
            return self.error1

    def __sub__(self, other):
        if self.is_instance(other):
            return (self.number - other.number, self.leter) if self.is_label_identical(other) \
                else self.error2
        else:
            return self.error1

    def __mul__(self, other):
        if self.is_instance(other):
            return (self.number * other.number, self.leter) if self.is_label_identical(other) \
                else self.error2
        else:
            return self.error1

    def __truediv__(self, other):
        if self.is_instance(other):
            return (self.number / other.number, self.leter) if self.is_label_identical(other) \
                else self.error2
        else:
            return self.error1


# a = CompleksNumbers('6x')
# b = CompleksNumbers('3x')
# c = CompleksNumbers('2x')
# d = CompleksNumbers('2y')
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a + 1)
# print(a - 1)
# print(a * 1)
# print(a / 1)
# print(a + d)
# print(a - d)
# print(a * d)
# print(a / d)

if __name__ == "__main__":
    import doctest
    doctest.testmod()