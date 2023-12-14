#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Напечатать все его слова, предварительно
# преобразовав каждое из них по следующему правилу:
# •	заменить первую встреченную букву a на о;
# •	удалить из слова все вхождения последней буквы (кроме нее самой);
# •	оставить в слове только первые вхождения каждой буквы;
# •	в самом длинном слове удалить среднюю (средние) букву(ы);
# •	принять, что такое слово – единственное.

if __name__ == '__main__':
    s = input("Введите ваше предложение: ")
    end_s = ''  # конечное предложение

    # Найдем в предложении наибольшее слово
    s_words = s.split(' ')  # разделим предложение на слова
    max_word = ''
    for i in s_words:
        if len(i) > len(max_word):
            max_word = i

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
    for word in s_words:
        last_letter = word[-1]  # последняя буква
        first_letters = ['']    # создаем список нужных букв
        # Дополним список первых вхождений
        for letter in word:
            if letter not in first_letters:
                first_letters.append(letter)
        # добавим последнее слово если такого нет в конце
        if last_letter not in first_letters[-1]:
            first_letters.append(last_letter)
        # Соберем слово обратно
        result_word = ''.join(first_letters)
        # И это слово отправим в предложение
        end_s = end_s + result_word + ' '

    # Заменим первую встреченную букву а на о
    end_s = end_s.replace("а", "о", 1)

    print("Предложение после преобразований: ", end_s)
