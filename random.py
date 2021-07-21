import random
number=random.randint(1000,1010)
print("WHAT IS THE PASSWORD OF THIS DEVICE?[HINT=IT IS BETWEEN 1000 TO 1010]")
chance=0
while chance < 6:
    guess=int(input("ENTER THE PASSWORD:"))
    if guess == number:
        print("DEVICE UNLOCKED")
        break
    else:
        print("WRONG PASSWORD")
    chance += 1
if not chance < 6:
    print("THE DEVICE IS LOCKED FOR 10 DECADES")