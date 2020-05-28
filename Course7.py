from functools import reduce

a = [(1, 2), (3, 4), (5, 6), (7, 8)]
a.sort(key=lambda x: x[1])

# print(a)

number_list = range(-5, 5)
# print(list(number_list))
less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)
squared = list(map(lambda x: x ** 2, items))
# print(squared)

product = 1
l = [1, 2, 3, 4]
for i in l:
    product *= i
product = reduce(lambda x, y: x * y, l)
# print(product)

a_list = [1, '2', 'a', 22, 0, 4]
squared_ints = [e ** 2 for e in a_list if isinstance(e, int)]
# print(squared_ints)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: x + y, numbers))

d1 = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
d = {k.lower(): v   for (k, v) in d1.items()}
