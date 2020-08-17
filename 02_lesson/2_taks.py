

class shop:
    all_products = 0
    
    def __init__(self, name_shop, sold_things):
        self.name_shop = name_shop
        self.sold_things = sold_things
        shop.all_products += self.sold_things

    def __str__(self):
        return f'Name shop: {self.name_shop}\n\tSold things: {self.sold_things}\n'

    # методы объекта, которые будут увеличивать кол-во проданных товаров
    def add_sold_things(self, sold_things):
        self.sold_things += sold_things
        shop.all_products += sold_things


a = shop('"great products"', 25)
b = shop('"one thousand things"', 50)
d = shop('"Elena"', 75)
print(f'a = {a}\n b = {b}\n d = {d} Все проданые товары = {shop.all_products}')
print('\n  ***Увеличивать кол-во проданных товаров***  \n')

a.add_sold_things(75)
b.add_sold_things(50)
d.add_sold_things(25)
print(f'a = {a.sold_things}\n b = {b.sold_things}\n d = {d.sold_things} Все проданые товары = {shop.all_products}')
