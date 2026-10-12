n=int(input())
count=0
while n > 0:
    count+=n%10
    n//=10
print(count)