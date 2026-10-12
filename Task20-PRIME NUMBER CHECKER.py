n=int(input())

if n<2:
    print("not Prime")
else:
    p=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            p=False
            break
    if p:
        print("Prime")
    else:
        print("not Prime")