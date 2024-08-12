from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return str(products)
    def add(self, *products):
        file = open(self.__file_name, 'a')
        products_true = self.get_products()
        for product in products:
            if product.name not in products_true:
                file.write(str(product) + '\n')
                products_true += product.name + '\n'
            else:
                print (f'Продукт {product.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())