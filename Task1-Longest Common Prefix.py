strs = input().split()

pri = strs[0]
for i in range(1,len(strs)):
    while not strs[i].startswith(pri):
        pri= pri[:-1]

        if pri == "":
            print ("")
print(pri)

