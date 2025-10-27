# default Parameter Values :

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#-------------------------------------------------#

def my_func(country = "USA" ):
    print("Hello...i am from",country)
    
my_func("India")
my_func("sri-lanka")
my_func("pakistan")
my_func()
my_func("russia")

#-------------------------------------#

#Keyword Arguments :

def my_function(pet, name):
      print("I have a", pet)
      print("My", pet + "'s name is", name)

my_function(pet ="Cat", name = "rocket")


def my_func(animal,name):
    print("i have an",animal)
    print("My",animal+ "'s name is", name)
    
my_func(animal="horse",name="letty")

#---------------------------------------------#

# Mixed Positional and Keyword Argument

def my_function(animal, name, age):
      print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


def my_func(friend, name, age, sport):
     print("i have a", age,"year old",friend, "named", name,"he plays", sport," to well")
     
my_func("athlete", name= "alex", age= 25, sport="cricket")

#----------------------------------------------------------#

# Passing Different Data Types:

def my_function(fruits):
      for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]     # sending list as argument
my_function(my_fruits)


def my_function(person):
      print("Name:", person["name"])
      print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}       # Dictionary as argument 
my_function(my_person)


def my_function():
      return ["apple", "banana", "cherry"]     #this function will return List

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def my_function():
  return (10, 20)             # this function will return in tuples

x, y = my_function()
print("x:", x)
print("y:", y)


