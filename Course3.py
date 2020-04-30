x = 10
while x > 0:
    print("x is {}".format(x))
    x -= 1

for i in range(10):
    print("i is {}".format(i))

for s in "some string":
    print(s)

ex = "this is a string"

print("first char from a string: {}".format(ex[0]))
print("last char from a string: {}".format(ex[-1]))
print("slicing a string: {}".format(ex[7:11]))

exemplu = ex.replace('a', 'b')
print(exemplu)

x = "abcdf"
print("litera cautata este a: {}".format(x.find("a")))

y = "string of chars"
l = y.split(" ")
print(l)

smth = None

A = (1, 2, 1)
B = (1, 2, 1)
C = (1, 2, 3)
D = A + B
print(A)
print(B)
print(D)
print(A == B)
print(A == C)
print(A[1])

inventory = ["faina", "drojdie", "apa", "sare"]
for index, value in enumerate(inventory):
    print("item {} = {}".format(index, value))

x = [True, False, "Ana", 2, 3, ["un sir"], ("string", 5)]
print(x)

inventory.append("coca-cola")
inventory += ["pepsi"]
print(inventory)
produse_noi = ["mere", "pere"]
inventory += produse_noi
inventory.sort()
inventory.reverse()
print(inventory)
print(len(inventory))

l = inventory[:2] + ["banane"] + inventory[2:]
print(l)
lista = [0, 1, ["al doilea nivel", ["trei", 2]]]
print(lista[2][1][0])
l = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
s3 = set(l)
l2 = list(s3)
print(s3)
print(l2)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)

d = {1: 'a', 2: 'b'}

