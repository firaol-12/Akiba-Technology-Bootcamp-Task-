x=int(input())
y=[]
o=0
e=0
sum=0
for i in range(x-1):
    n=i+1
    sum+=n
    y.append(n)
    if n%2==0:
        e+=1
    else:
        o+=1
print(e)
print(o)
print(sum)