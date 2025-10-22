thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Add sets

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# update with iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# remove set value

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)

#2nd WAY
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
print(thisset)


# frozen sets

x = frozenset({"apple", "banana", "cherry"})
y=frozenset({"charles","max","oscar"})
print(x)
print(type(x))
print(y)
print(type(y))