# CLASSES in python

class myclass:
    x = 5
p1 = myclass()
print(p1.x)


#del(p1)

class myclass1:
    x =20 
p1= myclass1()
p2= myclass1()
p3= myclass1()

print(p1.x)
print(p2.x)
print(p3.x)

#-----------------------------------------------------------------------------------#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1= Person("kaushik",21)

print(p1.name)
print(p1.age)

#---------------------------------------------------------------------------#

#without INIT function

class Person:
    pass

p1= Person()
p1.name = "JOHN"
p1.age = "54"

print(p1.name)
print(p1.age)

# ----------------------------------------------------------------------------------- #

class Person1:
    def __init__(self, name, age=17):         # 17 is default parameter
        self.name = name
        self.age = age
        
p1 = Person1("willy")                         # this will contain Default Value
p2 = Person1("sameer",27)
p3 = Person1("Kaushik",21)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.age, p3.name)

# age parameter has Default Value In IT.

class Person:
      def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Kaushik", 21, "Mumbai", "India")
p2 = Person("sameer", 27, "Pune", "India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

print(p2.name)
print(p2.age)
print(p2.city)
print(p2.country)

#---------------------------------------------------------------------------------#

class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Oscar", 25)
p1.greet()

#-------------------------------------------------------------------#

class Person2:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def greet(self):
        print("I drive a", self.color, self.brand)
        
p1 = Person2("Red", "BMW")
p1.greet()

#------------------------------------------------------------------------#

# CLASS PROPERTIES

class Person:
      def __init__(self, name, age):
         self.name = name
         self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#--------------------------------------------------------------------#

# ACCESS PROPERTIES

class Car:
      def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("BMW","M5 Competition")

print(car1.brand)
print(car1.model)

print(car2.brand)
print(car2.model)

#---------------------------------------------------------------------------#

class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26      # here the property of Age has been Modified from 25 to 26.
print(p1.age)

#-----------------------------------------------------------------------------#

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name)  # This works
# print(p1.age)  # This would cause an error

# in This the 'del' function will the obj in class

#-----------------------------------------------------------------------#

class Person:
    species = "Human"  # Class property

    def __init__(self, name):  # Must be indented inside the class
        self.name = name  # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#--------------------------------------------------------------------------#

class Person:
      lastname = ""

      def __init__(self, name):
        self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "clark"

print(p1.lastname)
print(p2.lastname)

#------------------------------------------------------------------#

class Person:
      def __init__(self, name):
        self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

#---------------------------------------------------------------------#

# METHOD WITH PARAMETERS

class Calculator:
      def add(self, a, b):
        return a + b

      def multiply(self, a, b):
        return a * b

calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(4, 7))

#--------------------------------------------------------------------#

class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

#------------------------------------------------------------------------#

class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

#-----------------------------------------------------------#

class Person:
      def __init__(self, name, age):
       self.name = name
       self.age = age

      def celebrate_birthday(self):
       self.age += 1
       print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

#------------------------------------------------------------#