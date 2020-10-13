from numpy import random

print("Guess and enter two number between 1-5")

a = list(map(int,input("Enter one number : ").strip().split()))

x = random.randint(5)

if x in a:
    print("win")
if x not in a:
    print("lose")