x = 50
y = 40
z = 30

print(x)
print(y)
print(z)

if x > y:
    print("x has greater number:", x)
elif y > x:
    print("y has greater number:", y)
elif x == y:
    print("x and y have the same number")
elif z < x:
    print("z is greater number", z)
elif x > z:
    print("x is greater than z")
else:
    print("x and z have same number")
