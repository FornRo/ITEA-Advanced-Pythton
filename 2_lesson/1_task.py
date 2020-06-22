def next(x='______________________________'):
    print(x)

class Car:

    def __init__(self, brand, model, color, price, lenght=None, clearance=None, weight=None, max_load=None):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.lenght = lenght
        self.clearance = clearance
        self.weight = weight
        self.max_load = max_load


    def look_car(self):
        return f'You look on {self.brands}, {self.model}, {self.color} and this car price = {self.price}'

    def specification(self):
        return {
            'brand': f'{self.brand} / {self.model}',
            'color': self.color,
            'price' : f'{self.price} $'
        }

    def move_car(self):
        return f'car {self.brand} is moving'
    
    def stop_car(self):
        return f'car {self.brand} is stay'


class F_class_car(Car):
    def __init__(self, brand, model, color, price, lenght):
        super().__init__(brand, model, color, price, lenght)

    def look_car(self):
        return f'You look on {self.brand}, {self.model}, this car is business class: price = {self.price}'
    
    def specification(self):
        return {
            'brand': f'{self.brand} / {self.model}',
            'color': self.color,
            'price' : f'{self.price} $',
            'lenght': f'{self.lenght} m'
        }

class J_class_car(Car):
    
    def __init__(self, brand, model, color, price, lenght=None, clearance=None, weight=None, max_load=None):
        super().__init__(brand, model, color, price, lenght=lenght, clearance=clearance, weight=weight, max_load=max_load)

    def specification(self):
        return super().specification()
        return {
            'brand': f'{self.brand} / {self.model}',
            'color': self.color,
            'price' : f'{self.price} $',
            'lenght': f'{self.lenght} m',
            'clearance': f'{self.clearance} cm',
            'weight': f'{self.weight}kg',
            'max_load': f'{self.max_load} kg'

        }


next()
a = Car('BMW', 'M5', 'red', 1000,)
print(a.specification())

next()
f = F_class_car('Audi', 'S8', 'black', 3000, 3)
print(f.look_car())
print(f.specification())

next()
next('Class_jeab')

j = J_class_car('jeeb', 'CJ', 'Yelow', 2500, 2, 1.5, 1900)
print(j.specification())