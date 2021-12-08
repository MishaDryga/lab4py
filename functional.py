# щоб не будувати базу продуктів і цін(що не є моєю задачею) я просто генерую ціни
from random import randint


class Fun:
    __order_list = []  # список замовлень
    __flag = 0  # перевірка списку (чи оновлений)

    def __init__(self, enter):  # створення екземпляра
        self.enter = enter  # вхідний список
        self.__order = {}  # вхідний словник

    def __add(self, i):  # метод додавання товару до замовлення
        self.__order[i] += randint(1, 100)  # додавання товару і його ціни до словника

    def __assign(self, i):  # добавити товар у словник
        self.__order[i] = randint(1, 100)  # добавлення товару і його ціни

    def make_order(self):  # метод перенесення замовлення у екземпляр замовлення
        for i in self.enter:  # для кожного товару у вхідному списку
            if i in self.__order:  # якщо товар уже є у словнику
                self.__add(i)  # добавити його ціну до ціни першого зразка
            else:  # інакше
                self.__assign(i)  # добавити його в словник

    def fill_list(self):  # формування списку замовлень
        Fun.__order_list.append((sum([i for i in self.__order.values()]), self.__order))  # екземпляру класа
        # __order_list добавити кортеж з сумою замовлення та словником з товарами і їх цінами
        Fun.__flag = 1  # список оновлений

    @staticmethod
    def srt():  # сортувати за ціною
        if Fun.__flag:  # якщо список не пустий
            Fun.__order_list = sorted(Fun.__order_list)  # то сортувати по спаданню ціни (пріоритет найвища сума)

    @staticmethod
    def show():  # вивести список замовлень у термінал
        Fun.srt()  # сортувати список
        print(Fun.__order_list)  # вивести
        Fun.__flag = 0  # список не оновлений

    @staticmethod
    def getL():  # перевірка списку
        return bool(Fun.__order_list)  # вертає чи пустий список (1 чи 0)

    @staticmethod
    def order_list():  # метод доступу
        return Fun.__order_list  # вертає список замовлень

    def order(self):  # метод доступу
        return self.__order  # вертає словник

    def flag(self):  # метод доступу
        return self.__flag  # вертає показник оновлення

    @staticmethod
    def test_sort():  # special edition
        i = 0
        end = len(Fun.__order_list)
        while 1:
            if i + 1 < end and Fun.__order_list[i] < Fun.__order_list[i + 1]:
                Fun.__order_list[i], Fun.__order_list[i + 1] = Fun.__order_list[i + 1], Fun.__order_list[i]
            i += 1
            if i == end:
                return True
