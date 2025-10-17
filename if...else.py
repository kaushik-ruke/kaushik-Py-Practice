#basic code

a = 33
b = 200
if b > a:
    print("b is greater than a")

#----------------------------------#

# ELIF

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#-------------------------------------#

#ELSE 

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#---------------------------------#

if a > b: print("a is greater than b") #short hand if
print("A") if a > b else print("B") #short hand if....else
print("A") if a > b else print("=") if a == b else print("B") 

#----------------------------------#

#AND

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")    # in AND condition both value should be correct to get OP true
elif a > b or a > c:
  print("At least one of the conditions is True") # in OR condition if the value is one correct then the OP is true