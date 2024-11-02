from math import inf
def divide_true(first, second):
    #from math import inf
    if second == 0:
        return inf
    else:
        return   first / second

if __name__ == '__main__':
    print(divide_true(49, 7))
    print(divide_true(15, 0))
