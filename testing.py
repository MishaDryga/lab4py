from unittest.main import main
from functional import Fun
import unittest


class TestOrders(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Fun.getL(), False)  # перевіряє чи пустий список

    def test_obj_and_attr(self):
        obj = Fun(['a', 'b'])  # створюєм екземпляр класу
        obj.make_order()  # викликаємо метод перенесення замовлення у екземпляр замовлення
        self.assertTrue(obj.order())  # чи непустий словник
        for i in obj.order():  # перебираєм словник
            self.assertTrue(i)  # чи не пусте значення
            self.assertIsInstance(i, str)  # чи значення і належеть типу рядок
        self.assertIsInstance(obj.order(), dict)  # чи масив належить типу словник

    def test_filling_list(self):
        obj = Fun(['a', 'b'])  # створюємо екземпляр з атрибутами а b
        obj.fill_list()  # сформувати список замовлень
        self.assertTrue(obj.order_list())  # чи пустий список замовлень
        self.assertTrue(obj.flag())  # чи пуста змінна flag

    def test_show_method(self):
        obj = Fun(['a', 'b'])  # створюємо екземпляр з атрибутами а b
        obj.show()  # вивести на екран
        self.assertEqual(obj.order_list(), sorted(obj.order_list()))  # перевірка чи правильно впорядковані елементи
        self.assertEqual(obj.flag(), 0)  # чи flag = 0

    def test_special_edition(self):
        obj = Fun(['a', 'b'])  # створюємо екземпляр з атрибутами а b
        obj.fill_list()  # сформувати список замовлень
        self.assertEqual(obj.test_sort(), 1) # перевірка закінчення циклу


if __name__ == '__main__':
    import xmlrunner
    run = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=run)