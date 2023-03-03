import csv
class Item:
    all = []
    pay_rate = 0.7

    def __init__(self,name:str,price:int,amount:int):
        self.__name = name
        self.price = price
        self.amount = amount

        self.all.append(self)

    def __repr__(self):
        """отображение информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.amount})"

    def __str__(self):
        """отображение информации об объекте класса для пользователей """
        return self.__name
    def __add__(self, other):
        """Позволяет складывать self.amount, но при это проверяет принадлежит ли экзнмпояр к класу Item"""
        if isinstance(other, Item) == True:
            return self.amount + other.amount


    @staticmethod
    def is_integer(value: int or float) -> bool:
        if type(value) == int:
            return True
        elif str(value).split('.')[1] == '0':
            return True
        else:
            return False

    """Проверяет является ли число flot or int , но при этом float.0 тоже является int"""

    @classmethod
    def new_copy(cls):
        """Создаёт новые экзэмпляры из csv файла"""
        copies = []
        with open('items.csv', 'r', encoding="UTF-8", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @property
    def name(self):
        """Возвращает название товра"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Контролирует длину названия товра"""
        if len(value) <= 10:
            self.__name = value
        else:
            print('Exception: Длина наименования товара превышает 10 символов.')
    def get_price(self):
        return self.price
    def aply_discount(self):
        self.price = round(self.price * self.pay_rate)

class Phone(Item):
    def __init__(self,name:str,price:int,amount:int, count_sim:int):
        super().__init__(name,price,amount)
        self.count_sim = count_sim
    @property
    def sim(self):
        return self.count_sim

    @sim.setter
    def sim(self, value):
        if value <= 0:
            print('Кол-во сим карт не может быть меньше ноля')
        else:
            self.count_sim = value

    def __repr__(self):
        return f'{super().__repr__()} {self.count_sim}'

b = Item('Phone', 10,20)
c = Phone('Iphonr', 10,20,2)

print(repr(c))