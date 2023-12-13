#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Напечатать все его слова, предварительно
# преобразовав каждое из них по следующему правилу:
# •	заменить первую встреченную букву a на о;
# •	удалить из слова все вхождения последней буквы (кроме нее самой);
# •	оставить в слове только первые вхождения каждой буквы;
# •	в самом длинном слове удалить среднюю (средние) букву(ы);
# •	принять, что такое слово – единственное.

import sys


if __name__ == '__main__':
    s = input("Введите ваше предложение: ")

    # Проверим, есть ли в предложении единственное наибольшее слово
    s_words = s.split(' ')  # разделим предложение на слова
    max_word = ''
    for i in s_words:
        if len(i) > len(max_word):
            max_word = i
        elif len(i) == len(max_word):
            print("В предложении более одного самого длинного слова",
                  file=sys.stderr)
            exit(1)

    # Удалим из наибольшего слова средние буквы
    if len(max_word) % 2 == 1:
        # Индекс средней буквы для нечетного
        middle_index = len(max_word) // 2
        # Удаляем среднюю букву
        max_word_save = max_word  # сохраняем слово для проверки
        max_word = max_word[:middle_index] + max_word[middle_index + 1:]
        # Собираем предложение обратно с учетом
        # отредактированного максимального слова
        s = ' '.join([word if word != max_word_save else max_word for word in s_words])
        print(s)
    else:
        # Индексы средней буквы для четного
        middle_index = len(max_word) // 2
        # Удаляем среднюю букву
        max_word_save = max_word  # сохраняем слово для проверки
        max_word = max_word[:middle_index-1] + max_word[middle_index + 1:]
        # Собираем предложение обратно с учетом
        # отредактированного максимального слова
        s = ' '.join([word if word != max_word_save else max_word for word in s_words])

    # Оставим в слове только первые вхождения букв
    # и удалим все вхождения последней буквы
    