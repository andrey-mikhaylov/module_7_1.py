from os.path import exists


class Product:
    def __init__(self, name: str, weight: float, category: str):
        """
        'Potato', 50.0, 'Vagetables'
        :param name: название продукта (строка).
        :param weight: общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        :param category: категория товара (строка).
        """
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """
        :return: строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
        """
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def __write_file(self, file_products: str):
        with open(self.__file_name, 'w') as f:
            f.write(file_products)

    def get_products(self):
        """
        считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        """
        if exists(self.__file_name):
            with open(self.__file_name, 'r') as f:
                file_products = f.read()
        else:
            file_products = ""

        return file_products

    def add(self, *products):
        """
        принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products,
        если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
        """
        file_products = self.get_products()
        need_update = False
        for new_product in products:
            if str(new_product)+'\n' in file_products:
                print(f'Продукт {new_product} уже есть в магазине')
            else:
                file_products += str(new_product)+'\n'
                need_update = True

        if need_update:
            self.__write_file(file_products)


def test():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
    """
    Вывод на консоль:
    Первый запуск:
    Spaghetti, 3.4, Groceries
    Potato, 50.5, Vegetables
    Spaghetti, 3.4, Groceries
    Potato, 5.5, Vegetables
    
    Второй запуск:
    Spaghetti, 3.4, Groceries
    Продукт Potato, 50.5, Vegetables уже есть в магазине
    Продукт Spaghetti, 3.4, Groceries уже есть в магазине
    Продукт Potato, 5.5, Vegetables уже есть в магазине
    Potato, 50.5, Vegetables
    Spaghetti, 3.4, Groceries
    Potato, 5.5, Vegetables
    
    Как выглядит файл после запусков:
    Potato, 50.5, Vegetables
    Spaghetti, 3.4, Groceries
    Potato, 5.5, Vegetables
    """


if __name__ == '__main__':
    test()


"""
2023/11/15 00:00|Домашнее задание по теме "Режимы открытия файлов"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

Пример результата выполнения программы:
Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
Как выглядит файл после запусков:



Примечания:
Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
Не забывайте закрывать файл вызывая метод close() у объектов файла.

Файл module_7_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""