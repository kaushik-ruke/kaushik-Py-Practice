cars = ["Ford", "Volvo", "BMW"]
print(cars)

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

print(car1)
print(car3)

cars = ["Maruti", "Toyota", "Hyundia"]
x = cars[0]
print(x)


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
      def __iter__(self):
       self.a = 1
       return self

      def __next__(self):
       x = self.a
       self.a += 1
       return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

''' 
       Method	Description
append()	Adds an element at the end of the list
clear() 	Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()   	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list 
'''