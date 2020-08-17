from copy import deepcopy


class Steck:
    """
    - Создать класс комплексного числа и реализовать для него арифметические операцq.
    """
    def __init__(self, lst):
        self.lst = deepcopy(lst)

    def __str__(self):
        return self.lst

    def empty_lst(self):
        """
        Проверка на наличие елементов.
        """
        steck = len(self.lst)
        return steck != 0 and steck is not None


    def push_lst(self, app):
        """
        При проталкивании (push) добавляется новый элемент, указывающий на элемент, бывший до этого головой.
        Новый элемент теперь становится головным.
        """
        self.lst.append(app)
        return self.lst


    def pop_lst(self):
        """
        При удалении элемента (pop) убирается первый, а головным становится тот,
        на который был указатель у этого объекта (следующий элемент).
        При этом значение убранного элемента возвращается.
        """
        if self.empty_lst:
            del self.lst[-1]
            return self.lst
        else:
            return 'error'
        
if __name__ == "__main__":
    lst = [1, [1, 2, 3], 3]
    # lst = []
    a = Steck(lst)

    print('element check =', a.empty_lst())

    print(a.push_lst([22, 33]), 'this push in stek')

    print(a.pop_lst())