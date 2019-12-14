'''один из вариантов, не совсем правильный. Вычисляет по значениям ASCII'''
# a = input("A stroka")
# b = input('B stroka')
# len_b = len(b)
# sum_b = sum(ord(i.upper()) for i in b)
# otvet = 0
# for i in range(len(a)):
#     # try:
#     if sum(ord(j.upper()) for j in a[i:len_b+i]) == sum_b:
#         otvet = 1
#         print('YES')
#
#
# if otvet != 1:
#     print('No')

"""Рабочий Вариант"""
a = input("A stroka")
a = a.upper()
b = input('B stroka')
b = b.upper()
check = 0

for i in range(len(a)-2):
    print(a[i:len(b)+i])
    if a[i:len(b)+i] in b:
        check = 1
        print('Yes')
        break
if check == 0:
    print('No')


