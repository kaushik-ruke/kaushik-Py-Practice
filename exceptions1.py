        
try:
  print(x)
except:
  print("An exception occurred")


#-------------------------------------------------------------#

try:
    print(x)
except NameError:
    print("there is error in Naming")
except :
    print("an exception has occurred")
    
#-------------------------------------------------------------#

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#this will print thr TRY and ELSE condition.

#-------------------------------------------------------------------#

#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

#-----------------------------------------------------------------------------------------#

#RAISE EXCEPTION:

x = -1

if x < 0:
    raise Exception("Sorry no Negative numbers Allowed")

y = "Hello"
if not type(y) is int:
        raise Exception("ONLY NUMBERS ARE ALLOWED")
      
      
#------------------------------------------------------------------------------------------------------------#

# User Input Value

#1st way

print("Enter your name:")
name = input()
print(f"Hello {name}")

#2nd Way

name=input("enter your name")
print(f"hello {name}")

#----------------------------------------------------------------------------------------------#

name1 = input("Enter your name:")
print(f"Hello {name1}")
fav1 = input("What is your favorite car brand:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite F1 driver:")
print(f"Do you want a {fav2} {fav1} to drive by {fav3}")

'''
#--------------------------------------------------------------------------------------------------#

import math

x = input("Enter a number: ")

# find the square root of the number
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

#--------------------------------------------------------------------------#

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")

#only integers will be accepted here
#----------------------------------------------------------------------------#
'''
