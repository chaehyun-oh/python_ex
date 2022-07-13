from unittest import result


def add(a, b):
    return a + b

def minus(a, b):
    return a - b

print(add(5, 10))
print(minus(5,10))

def my_add(*numbers):
    return numbers

result = my_add(1, 2, 3)
print(result, type(result))

def my_func(**kwargs):
    return kwargs

result = my_func(name='luke', age='20', gender='male')
print(result, type(result))