#1)Создать список из N элементов (от 0 до n с шагом 1).
#  В этом списке вывести все четные значения.
from random import randint

n = 100
my_list = []

list(map(
    lambda _: my_list.append(randint(0,100 +1)),
    range(n))
)
# my_list.sort()
print(list(filter(lambda x: x % 2 == 0,  my_list)))
