import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return "animal: " + str(self.age) + ": " + str(self.name)

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat: " + str(self.age) + ": " + str(self.name)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def __str__(self):
        return "person: " + str(self.age) + ": " + str(self.name)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
        self.activities = ["studiez", "dorm", "mananc", "netflix"]

    def __str__(self):
        return "student: " + str(self.age) + " : " + str(self.name) + " : " + str(self.major)

    def change_major(self, major):
        self.major = major

    def speak(self):
        print(random.choice(self.activities))


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        return (self.get_parent1() == other.get_parent1() and self.get_parent1() == other.get_parent2()) or (
                    self.get_parent2() == other.get_parent1() and self.get_parent2() == other.get_parent2())

    def __str__(self):
        return "rabbit " + self.get_rid()


r1 = Rabbit(1)
r2 = Rabbit(2)
r3 = Rabbit(3)

print(r1)
print(r2)
print(r3)

r4 = r1 + r2
r5 = r2 + r1
r6 = r3 + r1
print(r4 == r5)

print(r4.get_parent1())
print(r4.get_parent2())
print(r6.get_parent1())
print(r6.get_parent2())
# a = Animal(4)
# a.set_name("Lucky")
# print(a)
# cat = Cat(5)
# print(cat)
# s = Student("Name", 21)
# print(s)
# s.change_major("Computer-Science")
# print(s)
# s.speak()
# s.speak()
# s.speak()
