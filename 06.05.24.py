class A:  #кластын аты
    attr = "Hello world" #кластын атрибуты
    def hello (self): #метод
        print(self.attr)
obj1 = A()
hello= obj1.hello()
print(hello)


class Person:
    def __init__(self, firstname, age, name):
        self.firstname = firstname
        self.name = name
        self.age = age

    def my_method(self):
        print("Менын атым" + self.firstname + self.name)
p1 = Person("Dauren", 8, "Dauletbai")
p1.my_method()


class Person2:
    def __init__(self, name, age, firstname=" "):
        self.firstname = firstname
        self.name = name
        self.age = age

    def my_method(self):
        if self.firstname:
            print("Менын атым " +  self.firstname + self.name +  str(self.age))
        else:
            print("Менын атым "+  self.name + self.age)
p1 = Person2("Dauren", 18,"Dauletbai")
p1.my_method()
p2 = Person2("Dauren", 18)
p2.my_method()


class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def method(self):
        print("Car-", self.mark, self.model, str(self.year))


p1 = Car("Toyota", "Camry", 2018)
p1.method()
