#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Определить, сколько в нем гласных букв.

if __name__ == '__main__':
    s = input("Введите ваше предложение: ")
    # Создадим список, содержащий все гласные буквы
    list_gl = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
               'А', 'Е', 'Ё', 'И', 'О', 'У', 'Э', 'Ю', 'Я']
    count_gl = 0  # счетчик гласных
    for i in s:
        if i in list_gl:
            count_gl += 1
    print("Количество гласных букв в предложении:", count_gl)
