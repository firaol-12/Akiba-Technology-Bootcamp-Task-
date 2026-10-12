num=2
atmt=0
for i in range(5):
    g=int(input())
    atmt+=1
    if g == num:
        print("Congratulations!")
        print("you guesed the number in "+str(atmt)+" attempts.")
        break
    else:
        if atmt==5:
            break
        else:
            print("try again")
            
if atmt == 5:
    print("Game Over!")
    print("You guessed the number in 5 attempts already.")