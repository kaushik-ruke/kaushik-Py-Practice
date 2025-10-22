thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[-1])

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:5])

thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[:4])

thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[2:])

thistuple = ("apple", "banana", "cherry")
if "tomato" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print("not is fruits")


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)     # add item


thistuple1 = ("apple", "banana", "cherry")
y = ("orange","watermelon","mango")
thistuple1 += y

print(thistuple1)


# unpacked tuples

fruits = ("apple", "banana", "cherry", "spinach")

(green, yellow, red, black) = fruits

print(green)
print(yellow)
print(black)
print(red)


# use of asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry","mango")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)


# joining tuples 

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

fruits1 = ("apple", "banana")
fruits2 = ("kiwi","mango")

print(fruits1 + fruits2)