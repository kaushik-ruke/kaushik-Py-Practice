# normal Lists

mylist = ["Max", "Charles", "Lewis"]
print(mylist)
thislist = ["apple", "banana", "cherry"]
print(thislist)


#Allowing Duplicates

thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist1)

newlist = ["sameer","kaushik","sachin","kaushik"]
print(newlist)


#Access List

thislist = ["apple", "banana", "cherry","grapes"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry"]
print(thislist[0])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[4:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:2])

# CHANGE ITEM VALUE

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)   

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)    #will print the item that come in range of 1 to 3 but will exclude last number of range

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)    #will replace banana with new item added


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)     #will replace banana and cherry with new item


# INSERT ITEM

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "grapes")
print(thislist)

#  EXTEND LIST 

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
thislist.extend(tropical)   #this will also add a tuple 
print(thislist)

# REMOVE LIST 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)   #will remove the 1st occurrence of value in the List

# REMOVE THE SPECIFIC INDEXED ITEM

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # this will remove the last item
print(thislist) 

# USE of del

thislist5 = ["apple", "banana", "cherry"]
del thislist5[0]
print(thislist5)

thislist = ["apple", "banana", "cherry"]
del thislist      # this will remove entire LIST

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # this will clear all the item in list so now the list is empty 




