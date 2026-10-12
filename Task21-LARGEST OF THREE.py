x=int(input())
y=int(input())
z=int(input())

if x>y and x>z:
    print(str(x)+" is the largets")
elif y>x and y>z:
    print(str(y)+" is the largest")
elif z>x and z>y:
    print(str(y)+" is the largest")
else:
    print("there is no largest")
