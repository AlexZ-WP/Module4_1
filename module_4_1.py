from fake_math import divide_fake as df
from true_math import divide_true as dt
print(' ')
print('Good')

print(df(69, 3))
print(df(3, 0))
print(dt(49, 7))
print(dt(15, 0))

#  Импорты пишите строго сверху программы
# 2. fake_math и true_math - это модули. Если вызываете в них функции, то делайте это в условии if __name__ == "__main__"
# 3. В главном файле вы сделали только импорт, но не вызвали функции