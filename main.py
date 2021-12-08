import unittest
from functional import Fun

while True:

    time_list = []  # тимчасовий список для продуктів який передається як атрибут при створенні екзампляра класу Fun
    # в рядку 14
    while True:  # нескінченний цикл основної програми

        print('input: product name, finish order, show list, end')  # введення необхідної команди для роботи з програмою
        enter = input()  # значення команд по черзі: введення бажаного продукту; закінчити додавати товар у
        # замовлення; показати список замовлень; завершити програму

        if enter in ('finish order', 'show list', 'end'):  # якщо дані команди введені то -
            break  # перервати внутрішній цикл прийняття замовлень
        else:  # якщо ж ми ввели будь яке інше слово
            time_list.append(enter)  # добавити його як продукт у тимчасовий список

    if time_list:  # якщо список не пустий, а значить містить товар:
        product = Fun(time_list)  # створюєм екземляр product класу Fun і передаємо йому список
        product.make_order()  # виконати функцію make_order() що формує замовлення

    if enter == 'finish order' and time_list:  # якщо юзер ввів дану команду і список не пустий, то
        product.fill_list()  # заповнити список усіх замовлень

    elif enter == 'show list':  # якщо ввели дану команду, то
        if Fun.getL():  # перевірити чи список замовлень не пустий
            product.show()  # вивести список усіх замовлень ([ ( item`s_summa, {product: price, product: price} ),
            # ( item`s_summa, {product: price, product: price} ) ])
        else:  # у випадку пустого списку
            print('empty list')  # вивести рядок "список пустий"

    elif enter == 'end':  # якщо ввели дану команду, то
        break  # програма перериває зовнішній цикл і закінчує роботу
