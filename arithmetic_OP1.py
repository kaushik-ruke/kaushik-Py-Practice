'''a=int(input("enter a "))
b=int(input("enter b "))
3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)'''

#--------------------------------------------#

#ASSIGNMENT OPERATOR

numbers = [1, 2, 3, 4, 5, 6]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 5:
    print(f"List has {count} elements")

#-----------------------------------------------------#

#COMPARISON OPERATOR

x = 34
y = 43

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


a = 5

print(1 < a < 10)
print(1 < a and a < 10)
print(1 < a and a > 10)

#------------------------------------------------------------#

#LOGICAL OPERATOR

x = 5

print(x > 0 and x < 10)
print(not(x < 3 and x > 10))
print(not(x > 3 and x < 10))
print(x < 5 or x > 10)


