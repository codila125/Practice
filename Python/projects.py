#the project here are just all the test practises and revision

# making a programme where we can only input numbers, if we input string it will be invalid
x = input("Enter a number:")
try:
    y = int(x)
    if y == 0:
        print ("the number is zero")
    elif y > 0:
        print("positive number")
    else:
        print ("Negative number")
except:
    print("Invalid")

#making a function for above programme
#1
def pnz(x):
    try:
        y = int(x)
        if y == 0:
            print ("the number is zero")
        elif y > 0:
            print("positive number")
        else:
             print ("Negative number")
    except:
        print("Invalid")
pnz("ola")
pnz("100")

#2
def pnz():
    x = input("Enter a number:")
    try:
        y = int(x)
        if y == 0:
            print ("the number is zero")
        elif y > 0:
            print("positive number")
        else:
            print ("Negative number")
    except:
        print("Invalid")
pnz()

#3
def pnz():
    x = input("Enter a number:")
    try:
        y = int(x)
        if y == 0:
            return "the number is zero"
        elif y > 0:
            return "positive number"
        else:
            return "Negative number"
    except:
        return "Invalid"
print (pnz())

#to only let in if the name is prabesh(loop)
while True:
    ola = input("Your Name")
    if ola == "Prabesh" or "prabesh":
        break
    print("Not allowed")
print (ola,"welcome home bruh:)))")

#bit more advanced
while True:
    ola = input("Your name ")
    if ola != "Prabesh" :
        continue
    print (ola, "Welcome, Pls enter your password")
    ins = input("Password")
    if ins == "Admin" or "admin":
        break
print ("Welcome to your own hood", ola)

#long time no see dude
print ("Long time no see dude")
