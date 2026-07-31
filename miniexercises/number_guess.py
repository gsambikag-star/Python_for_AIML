import random
num=random.randint(1,100)
print("guess the number between 1 to 100")

count=0

while True:
    n=int(input("enter the number:\n"))
    count+=1
    if n==num:
        print(f"Guessed the number correctly in {count} attempt(s)")
        break
    elif n<num:
        print("Guess is lower than the number")
    else:
        print("guess is higher than the number")