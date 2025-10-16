x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#----------------------------------------------------------------#

x = "GREAT"

def myfunc():
  x = "FANTASTIC"
  print("PYTHON IS " + x)

myfunc()

print("PYHTHON IS " + x)

#---------------------------------------------------------------------#

x = "Awesome"

def myfunc():
  global x   #To change the value of 'x' a global variable is used in a function, (global) keyword:

  x = "FANTASTIC"

myfunc()

print("Python is " + x)
