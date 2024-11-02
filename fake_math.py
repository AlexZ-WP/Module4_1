def divide_fake(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second

if __name__ == '__main__':
    print(divide_fake(69, 3))
    print(divide_fake(3, 0))




# второй вариант кода при second = 0 выдаёт ошибку??? при других значениях работает
#     a = first / second
#     if second == 0:
#         return 'Ошибка'
#     else:
#         return a
#
# print(divide_fake(63, 0))