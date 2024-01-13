#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#В начале кортежа записано несколько равных между собой элементов. Определить
#количество таких элементов и вывести все элементы, следующие за последним из них.
#Рассмотреть возможность того, что весь массив заполнен одинаковыми элементами.
#Условный оператор не использовать.


if __name__ == "__main__":
    t = tuple(map(int, input("Введите кортеж значений через пробел: ").split()))

    count = 0
    index = 0

    while index < (len(t) - 1) and t[index] == t[index + 1]:
        count += 1
        index += 1

    print(count + 1, t[index + 1:])
    