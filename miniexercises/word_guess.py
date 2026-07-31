import random

name=input("enter your name:\n")
print(f"\nWelcome! {name}")

words=["lion","tiger","giraffe","deer","elephant","cheetah","lepoard",
       "bear","donkey","monkey","panda","buffalo","wolf","camel","horse",
       "zebra","kangaroo"]

word=random.choice(words)

print("\nguess the word")
guesses=""
turns=12

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed+=1
    if failed==0:
        print("\nCongrats!! You win......")
        print("\nThe word was: ",word)
        break

    guess=input("\nenter the letter:\n").lower()
    if len(guess)!=1:
        print("enter single letter")
        continue

    if guess in guesses:
        print("\nYou have already guessed this letter")
        continue
    guesses+=guess

    if guess not in word:
        turns-=1
        print(f"\nYou have {turns} left")

    if turns==0:
        print("\n You Lost!!")
        print("\nThe word was: ",word)
        

    

    
