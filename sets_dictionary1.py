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

# loop Dictionaries 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1 = {
    "brand": "Ferrari",
    "model": "F1 SF-25",
    "year": "2025"
}
for x in thisdict.keys():
  print(x)
for x in thisdict.keys():
    print(x)

#---------------------------------------#
    
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1 = {
    "brand": ":Ferrari",
    "model": ":F1 SF-25",
    "year": ":2025"
}
for x,y in thisdict.items():
  print(x,y)
for x , y in thisdict1.items():
    print(x,y)
    
# Copy dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2": child2,
  "child3": child3
}

print(myfamily)

#----------------------------------------------#

child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}

for key, value in myfamily.items():
  print(key + ":")
  for subkey, subvalue in value.items():
    print("  " + subkey + ":", subvalue)