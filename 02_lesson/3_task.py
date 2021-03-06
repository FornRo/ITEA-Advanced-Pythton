class dote:
    
    def __init__(self, x, y, z):
        self.dikt = {'x': x, 'y': y, 'z': z}

    def __str__(self):
        return (
            f'{self.dikt["x"]},' +
            f'{self.dikt["y"]},' +
            f'{self.dikt["z"]}'
        )
    
    def __abs__(self):
        result = dict()
        for i in ('x', 'y', 'z'):
            if self.dikt[i] < 0:
                result[i] = self.dikt[i] * -1
            else:
                result[i] = self.dikt[i]

        return result.values()

    def __add__(self, other): # +
        result = dict()
        for i in ('x', 'y', 'z'):
            result[i] = self.dikt[i] + other.dikt[i]
        return result.values()
    
    def __sub__(self, other): # -
        result = dict()
        for i in ('x', 'y', 'z'):
            result[i] = self.dikt[i] - other.dikt[i]
        return result.values()

    def __mul__(self, other): # *
        result = dict()
        for i in ('x', 'y', 'z'):
            result[i] = self.dikt[i] * other.dikt[i]
        return result.values()

    def __truediv__(self, other):
        result = dict()
        for i in ('x', 'y', 'z'):
            result[i] = self.dikt[i] / other.dikt[i]
        return result.values()

    def get_item(self, key):
        key = key.lower()
        return self.dikt[key]


pt_a = dote(1, 2, 3)
b = dote(-1, -2, -3)
# получения
if True:
    print(pt_a.get_item('X'))
    print(pt_a.get_item('y'))
    print(pt_a.get_item('z'))
    print(b)

if True:
    print(f'\ta = {pt_a} \tb = {b}')
    print(f'{pt_a + pt_a} \t\ta + pt_a')
    print(f'{pt_a - pt_a} \t\ta - pt_a')
    print(f'{pt_a * pt_a} \t\ta * pt_a')
    print(f'{pt_a / pt_a} \ta / pt_a')
    print(f'{abs(b)} \t\tabs(b)')