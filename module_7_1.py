class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        strr = f'{self.name}, {self.weight}, {self.category}.'
        return strr

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        file_get = self.get_products()
        for i in products:
            if self.get_products().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print('Продукт', i.name, 'уже есть в магазине.')


s1 = Shop()
p1 = Product('Картофель', '20.3', 'овощи')
p2 = Product('Лимон', '2.2', 'фрукты')
p3 = Product('Картофель', '20.3', 'овощи')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())