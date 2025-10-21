#LOOP LIST

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry", "grapes" , "Watermelon"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 2
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]            # 2nd way to print all the elements in a List

# LIST COMPREHENSION

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)         # this will print the item which contain only 'A' in it


# 2nd Way 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango","watermelon","papaya"]
newlist1 = [x for x in fruits if x != "apple"]
newlist2 = [x for x in fruits]
newlist3 = [x for x in range(10)]
newlist4 = [x for x in range(10) if x < 5]
newlist5 = [x.upper() for x in fruits]
newlist6 = ['hello' for x in fruits]
newlist7 = [x if x != "banana" else "orange" for x in fruits]

print(newlist1)
print(newlist2)
print(newlist3)
print(newlist4)
print(newlist5)
print(newlist6)
print(newlist7)
  
  
#SORT LIST

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)   # SORT ALPHANUMERICALLY

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)      # SORT NUMERICALLY

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)    # REVERSE ALPHANUMERICAL

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)     # REVERSE NUMERICALLY

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)  # CASE INSENSITIVE SORT...Output WILL START FROM KIWI AND THEN REST

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)  # REVERSE ORDER OF INSENSITIVE....MEANS LOWER CASE LETTER WILL TAKE 1ST IN LIST

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)    # ENTIRE LIST WILL REVERSE FROM THERE ORDER

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist2 = list(thislist)
print(mylist2)

thislist = ["apple", "banana", "cherry","guava","melons"]
mylist3 = thislist[:4]
print(mylist3)

# JOIN LIST

# 1st way:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#2nd Way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#3rd way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

