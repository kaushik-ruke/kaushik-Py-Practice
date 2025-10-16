x = 50
y = "Hades"
print(x)
print(y)

#----------------------------------------------------------#

myvar = "Lewis" 
my_var = "Charles"
myVar = "Max"
MYVAR = "Oscar"
myvar2 = "Lando"

print(myvar, my_var, myVar, MYVAR, myvar2)

print("Which variable do you want :")
print("Options: myvar, my_var, myVar, MYVAR, myvar2")

var_name = input("Enter variable name: ")

if var_name == "myvar":
    print("Value of myvar =", myvar)
elif var_name == "my_var":
    print("Value of my_var =", my_var)
elif var_name == "myVar":
    print("Value of myVar =", myVar)
elif var_name == "MYVAR":
    print("Value of MYVAR =", MYVAR)
elif var_name == "myvar2":
    print("Value of myvar2 =", myvar2)
else:
    print("Invalid variable name!")
#----------------------------------------------------------#

myVariableName = "KIMI" # Camel Case variable Type
MyVariableName = "George" # Pascal Case Variable Type
my_variable_name = "Sainz" # Snake Case Variable Type

print(myVariableName, MyVariableName, my_variable_name)

