'''
print(type(5/2))    #type float

A = "  Kaushik  Ruke  "
print(A.strip())      # remove entire white space 
print(A.lstrip())     # remove white space at beginning 
print(A.rstrip())     # remove white space at end

A = [10,45,7,18]
maximum = max(A)     # this function will return the maximum number in List
print(maximum)

square = lambda x: x * x
print(square(5))  # this is a type of anonymous function in python

text = "hello"
new_text = text.replace('l', 'e')     # the 1st asked letter L will get replaced with the letter E....resulting in the output "Heeeo"
print(new_text)  # Output: heeeo 

import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

class P:
    def m1(self):
        print('Parent')
class C(P):
    def m2(self):
        print('child')
c=C()
c.m1()
c.m2()      # here the Output will be Parent and then Child

name = "Hello World"
print(type(name))


A = [ 12, 14, 35, 67, 47]
print(len(A))


# IF THE RETURN STATEMENTS IS NOT USED INSIDE THE FUNCTION, THE FUNCTION WHILE RETURN 'NONE'.

try:
    print(file_name)
except:
    print("Error in the line")
    
# "POP()" REMOVES THE LAST ELEMENT OF LIST.

# SET() CREATE AND EMPTY SET IN PYTHON

S = input("Enter the A String:")
vowels = "aeiouAEIOU"
count = 0

for ch in S:
    if ch in vowels:
        count +=1
        
print("vowel Count:", count)


from datetime import datetime

# Get current date and time
now = datetime.now()

# Format it nicely
#formatted = now.strftime("%A, %d %B %Y %I:%M:%S %p")

# Display it
print("Current Date and Time formatted",now)
'''

# 'def' is the Word to Define the function in Python.

# PYTHON IS 'DYNAMICALLY' TYPED LANGUAGE.

#input() IS THE BUILT-IN FUNCTION IN PYTHON TO OBTAIN INPUT FROM USERS.

# for loop is to iterate the over the Sequence

# PYTHON IS A CASE SENSITIVE LANGUAGE

result = int("10")+1
print(result)

len([1,2,3,4])
print(len)

Num=int(input("Enter A Number : "))
if Num % 2 == 0:
    print("Its Even Number")
else:
    print("Its Odd Number")
    
    
# PALINDROME :

'''text = input(" Enter A String : ")
cleaned_text = text.replace(" ","").lower

if cleaned_text == cleaned_text[::-1]:
    print(f'"{text}" is a palindrome.')
else :
    print(f'"{text}" is not a palindrome.')
    
'''


# 

# Input string
text = "for only solution"

# Initialize lists
chars = []
odd_digits = []
even_digits = []

# Process each character
for ch in text:
    if ch.isalpha():
        chars.append(ch)
    elif ch.isdigit():
        if int(ch) % 2 == 0:
            even_digits.append(ch)
        else:
            odd_digits.append(ch)

# Sort each list
chars.sort()
odd_digits.sort()
even_digits.sort()

# Print results
print("Characters:", chars)
print("Odd digits:", odd_digits)
print("Even digits:", even_digits)