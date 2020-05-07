print("Course 4")


# nr = input("Enter a number: ")

# try:
#     nr = int(nr) * 2
#     print("nr * 2 is: {}".format(nr))
# except:
#     print("This is not a number!")
# else:
#     print("Everything is alright!")


# Functions

def my_function():
    print("Just a simple function")


# result = my_function()

# print("Result is {}".format(result))


def A():
    print("A")


def B():
    print("B")


def C():
    A()
    B()


# C()


def add(param1, param2):
    """
    prints the sum of the two params
    :param param1:
    :param param2:
    :return None:
    """

    return param2 + param1


# p1 = int(input("First number: "))
# p2 = int(input("Second number: "))
# print("The sum is: {}".format(add(p1, p2)))


def ziNastere(nume, varsta=18):
    print("Hello {}! Happy birthday {}!".format(nume, varsta))


# ziNastere("asd", 20)


x = 2


def test():
    x = 3
    print(x)


# print(x)
# test()


def suma(a, b, *c):
    """"add at least 2 params"""
    x = a + b
    if c:
        print("c => {}".format(c))
        for e in c:
            x += e
    return x


# print(suma(1, 2))
# print(suma(1, 2, 3, 4, 5))

def F(b, **a):
    print(a)
    print(b)


# F("param b",unu=1,doi=2)

adunare = lambda a, b: a + b

# print(adunare(1, 2))

cube = lambda x: x ** 3


# print(cube(2))


# Creati o functie care sa inlocuiasca caracterele de tip spatiu cu underline si sa inlocuiasca sirul de caractere “e”
# cu sirul de caractere “i” dintr-un sir de caractere primit ca parametru. Verificati ca este sir de caractere inainte
# de a face aceasta operatie. Returnati sirul de caractere modificat sau returnati sirul urmator daca nu a fost primit
# un sir de caracatere: “Dati va rog un sir de caractere” Rulati codul pentru “Merele, perele si pestele nu au E-uri”


def pb1(string):
    if not isinstance(string, str):
        return "Dati va rog un sir de caractere"

    new_string = ""
    for i in range(len(string)):
        if string[i] == 'e' or string[i] == 'E':
            new_string += 'i'
        elif string[i] == ' ':
            new_string += '_'
        else:
            new_string += string[i]
    return new_string


result = pb1("Merele, perele si pestele nu au E-uri")


# print(result)


def pb2(string):
    d = {}

    for c in string:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


# print(pb2("Merele, perele si pestele nu au E-uri"))

def pb3(cnp):
    # check for length
    if len(cnp) != 13:
        return False

    # check for numbers only
    for c in cnp:
        if c < '0' or c > '9':
            return False

    # S ( just 0 can be wrong)
    if cnp[0] == '0':
        return False

    # AA (here every number( 0-9) is fine)
    if cnp[1] < '0' or cnp[1] > '9' or cnp[2] < '0' or cnp[2] > '9':
        return False

    # LL (cnp[3] is (0,1) cnp[4] can be anything(0-9))
    if not (cnp[3] == '0' or cnp[3] == '1') or cnp[4] < '0' or cnp[4] > '9':
        return False

    # ZZ (cnp[5] is (0,1,2,3) cnp[6] can be anything(0-9))
    if cnp[5] < '0' or cnp[5] > '3' or cnp[6] < '0' or cnp[6] > '9':
        return False

    # JJ (cnp[7] is (0,1,2,3,4,5) cnp[8] can be anything(0-9))
    if cnp[7] < '0' or cnp[7] > '5' or cnp[8] < '0' or cnp[8] > '9':
        return False
    # NNN (cnp[9]->(0-9), cnp[10]->(0-9), cnp[11]->(0-9))
    if cnp[9] < '0' or cnp[9] > '9' or cnp[10] < '0' or cnp[10] > '9' or cnp[11] < '1' or cnp[11] > '9':
        return False
    # C
    control = "279146358279"
    sum = 0
    for i in range(len(cnp) - 1):
        sum += (int(cnp[i]) * int(control[i]))
    c = sum % 11
    return c == int(cnp[12])


print(pb3("1990611245027"))
