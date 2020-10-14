import random
import sys

x = ["1","2","3","4","5"]

def check_number(randnum,usernum):
    if randnum == usernum:
        return "Right guess"
    else:
        return "Wrong"

def play():
    usernum = None
    while usernum not in x:
        usernum = input("Enter number between 0-5 : ")
        if usernum == "q":
            sys.exit()
    
    randnum = random.choice(x)

    print(f"Computer choose : {randnum}")
    print("You" + check_number(randnum,usernum),end="\n\n")

if __name__ =="__main__":
    while True:
        play()