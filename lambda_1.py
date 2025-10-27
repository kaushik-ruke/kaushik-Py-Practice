# lambda function basic

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c, d : a + b * c / d
print(x(10, 20, 5, 4))

#--------------------------------------------------------------------#

def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)

print(doubler(11))


def myfunc1(n):
      return lambda a : a * n

mytripler = myfunc1(3)

print(mytripler(12))

#----------------------------------------------------------------

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mytripler(11))
print(mydoubler(30))



numbers = [1, 2, 3, 4, 5]                         # printing in list format
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))         # odd number finding condition
print(odd_numbers)


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


#------------------------------------------------#

# recursion function

def countdown(n):
      if n <= 0:
         print("Done!")
      else:
        print(n)
        countdown(n - 1)        # condition for reverse order

countdown(5)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        n * factorial(n-1)     
        print(factorial(5))



def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))



def sum_list(numbers):
      if len(numbers) == 0:
        return 0
      else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


# find the max value in list:

def find_max(numbers):
      if len(numbers) == 1:
       return numbers[0]
      else:
       max_of_rest = find_max(numbers[1:])
      return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))


import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))                       # generator will start make the value and start putting in list.



def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
  
  
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)


