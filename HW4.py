# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# n = 20
# def simple_multipliers(n):
#     spisok = []
#     for i in range(2, n):
#         if n % i == 0:
#             spisok.append(i)
#             n = n // i
#     return spisok
# result1 = simple_multipliers(n)
# print(result1)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

# list2 = [1,1,1,1,2,2,2,3,3,3,4]
# print(list2)
# def not_repeat(x):
#     list = []
#     for i in x:
#         if not i in list:
#             list.append(i)
#     print(list)
# not_repeat(list2)

# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# with open('file.txt', 'r+', encoding='utf-8') as f:
#     res = f.readlines()
#     def to_upper_excellent(list3):
#         for i in list3:
#             word = ''
#             for symb in i:
#                 if symb == '5':
#                     word = i.upper() + word
#                     list3[list3.index(i)] = word
#         return list3
#     spisok_res = to_upper_excellent(res)
#     def convert_to_string(list):
#         word_res = ''
#         for i in list:
#             word_res += i
#         return word_res
#     str_res = convert_to_string(spisok_res)
# with open ('result.txt', 'w', encoding='utf-8') as f:
#     f.write(str_res)

# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ,
# считывает текст и дешифровывает его.

# s = 'абба'
# n = -2
# def text_encryption(n, s):
#     word = ''
#     ctr = 'абвгдеёжзийклмнопрстуфхцчшщьэюя'
#     with open ('code_text.txt', 'w', encoding='utf-8') as f:
#         for i in s:
#             for symb in range(len(ctr)):
#                 if i == ctr[symb]:
#                     word = word + ctr[symb + n]
#         f.write(word)
# def text_decryption():
#     # key_open = int(input('Input a key (negative - left, positive - right: '))
#     with open('code_text.txt', 'r', encoding='utf-8') as f:
#         key_open = int(input('Input a key (negative - left, positive - right: '))
#         encrypt_word = f.read()
#         word = ''
#         ctr = 'абвгдеёжзийклмнопрстуфхцчшщьэюя'
#         ctr = ctr[::-1]
#         for i in encrypt_word:
#             for symb in range(len(ctr)):
#                 if i == ctr[symb]:
#                     word = word + ctr[symb + key_open]
#         print(word)      
# text_encryption(n, s)
# text_decryption()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

# with open('RLE_alg.txt', encoding='utf-8') as data:
#     s = data.read() + ' '
#     print(s)
#     print()
# def encrypt_rle(s):
#     encrypt_word = ''
#     count_symb = 1
#     for symb in range(len(s) -1):
#         if s[symb] == s[symb + 1]:
#             count_symb = count_symb + 1
#         else:
#             encrypt_word = encrypt_word + str(count_symb) + s[symb]
#             count_symb = 1
#     with open('RLE_alg_encrypt.txt', 'w', encoding='utf-8') as data:
#         data.write(encrypt_word)
#     print(encrypt_word)
# def decrypt_rle():
#         with open('RLE_alg_encrypt.txt', encoding='utf-8') as data:
#             s = data.read() + ' '
#         decrypt_word = ''
#         count_symb = ''
#         for symb in range(len(s) - 1):
#             if s[symb].isnumeric() == True:
#                 count_symb = count_symb + s[symb]
#             else:
#                 decrypt_word = decrypt_word + s[symb] * int(count_symb)
#                 count_symb = ''
#         print(decrypt_word)
# encrypt_rle(s)
# print()
# decrypt_rle()