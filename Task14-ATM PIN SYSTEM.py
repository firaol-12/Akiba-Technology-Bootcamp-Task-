a=3
for i in range(3):
    x=int(input())
    a-=1
    if x != 1234:
        print("Incorrect PIN.")
        print("Attempts remaining: "+str(a))
    elif x == 1234:
        break


