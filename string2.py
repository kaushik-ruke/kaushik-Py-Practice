age = 36
x = "My name is John, I am " ,age
print(x)

#---------------------------------------------#

#F-string

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#-------------------------------------------------#

#Place Holder and Modifier

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#-------------------------------------------------#

#Escape Character string

t = "We are the so-called \"Vikings\" from the north." # use of \"
print(t)

'''
\'	= Single Quote	
\\	= Backslash	
\n	= New Line	
\r	= Carriage Return	
\t	= Tab	
\b	= Backspace	
\f	= Form Feed	
\ooo = Octal value	
\xhh = Hex value5
'''