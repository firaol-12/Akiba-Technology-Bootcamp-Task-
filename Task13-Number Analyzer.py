x=[]
a=0
e=0
o=0
for i in range(10):
    y=int(input())
    a+=y
    x.append(y)
    if y%2==0:
        e+=1
    else:
        o+=1

z=sorted(x)
print(z[-1])
print(z[0])
print(a)
print(a/2)
print(e)
print(o)



