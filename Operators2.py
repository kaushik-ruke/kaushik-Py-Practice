x = ["python", "Flask"]
y = ["python", "FLask"]
z = x

print(x is z)
print(x is y)
print(x == y)

#--------------------------------------------#

x = ["apple", "banana"]                                     
y = ["apple", "banana"]                                #true

print(x is not y)

#---------------------------------------#

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)                                          #true
print(x is y)                                          #false because different memory location

#-------------------------------------------------------#

#MEMBERSHIP OPERATOR

Language = ["C++","C","PYTHON","JAVA"]

print("PYTHON" in Language)
print("C" not in Language)
print("C++"not in Language)

#-------------------------------------------------------#

#OPERATOR PRECEDENCE

print((6 + 3) - (6 + 3)) 
print(100 + 5 * 3)       #multiplication has higher precedence so it get calculated first
print(5 + 4 - 7 + 3)     # + and - have the same precedence so we have to follow the rule of left to right calculation

