print("hello world")

x = 1
print (x)

x = x + 1
print (x)

print(900)

y = 100
print (y)

x = 20
print(x)

z = x*y
print(z)

z = z+x
print(z)

a = z/x
print(a)

#** is a power
b = a**2
print(b)

# % is a mod or remainder
c = z%x
print(c)

d = 1 + (2**2) / 2 * 2 
print(d)

e = "ola" + "hello"
print (e)

e = "ola " + "hello"
print (e)

#types of variables and constants
xx = 1 #integer or int

yy = "hype"# string or str

zz = 98.9 #floating or float

print(xx, yy, zz)

print( float(20) + 60)

f = float(xx)
print(f)

g="123"#its a string
type(g)
print(g)

h=int(g)#changing the string into integer by using int function
print(h)

i=float(g)#changing the string into float by using float function
print(i)

print(h+i)

x =1
y = float(x)
print(y)

ola = input("Whats your name?: ")
print("Welcome", ola,". Thank you for coming")

tot = input("Whats your age?: ")
print("So your age is", tot, "yrs old")

#convert celsius to kelvin
cel = input("Input the temp in celsius: ")
print ("Your input temp is", cel, " C")
kel = int(cel) + 273
print ("The temp in kelvin is ", kel, " K")

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("enter rate:")
rate = float(rate)
print ("Pay:",hrs * rate)

x = 5
if x < 10 : 
    print("smaller than 5")
if x > 20 :
    print("Greater than 20")

# < less than, > greater than, <= less than or equal to, == equal to, >=greater than or equal to, != Not equal

ol = input("Input a number:")
ol = int(ol) 
if ol < 0 : 
    print(ol, "is samller than 0")
elif ol > 0:
    print(ol, "is greater than 0")
elif ol == 0:
    print (ol, "is zero")
if ol != 0:
    print (ol, "is not equal to 0")
    hl = ol%2
    if hl == 0:
        print(ol, "is even")
    else :
        print(ol, "is odd")

# skipping errrors avoiding traceback
atr = "100"
try :
    x = int(atr)
except : 
    x = "Not a integer"
print(x)


# making a programme where we can only input numbers, if we input string it will be invalid
x = input("A number: ")
try : 
    y = int(x) 
    print("Valid")
    if y > 0 :
        print("It is positive")
    elif y < 0 :
        print("Its negative")
    else :
        print("it is zero")
except :
    print("Invalid")

#next method of above programme
x = input("A number: ")
try : 
    y = int(x)     
except :
    y = -1
if y == -1:
    print("Invalid")
if y != -1:
    print ("Valid")
    if y > 0 :
        print("It is positive")
    elif y < 0 :
        print("Its negative")
    else :
        print("it is zero")

#functions
def things():
    print("ola")
    print("hello")

things()

ola = max("hello world")
print(ola)
#prints the largest thing

ola = min(1,0)
print (ola)
#prints the smallest thing thing

l = input("a two numbers")
things()
ola = max(l)
print(ola)
type(l)

def conversion():
    cel = input("Input the temp in celsius: ")
    print ("Your input temp is", cel, " C")
    kel = int(cel) + 273
    print ("The temp in kelvin is ", kel, " K")

conversion()

def posneg(ols):
    ols = int(ols)
    if ols > 0 :
        return "positive"
    elif ols < 0 :
        return "negative"
    else :
        return "zero"

print (posneg(1))
print (posneg(-1))
print (posneg(0))


def me(mo):
    if mo == "Prabesh" :
        print("My boss")
    else :
        print("Go away")
mo = input("Whats is my name?")
me(mo)

def mo():
    return "Prabesh"

print( mo(), "Hello")



def h(l):
    if l == "es" :
        return "ola"
    elif l == "en" :
        return "hello"
    else :
        return "bonjour"
a = input ("Whats your name?")
l = input("Whats your language?")
print (h(l), a)

def h(l,i):
    return l + i
l = input()
i = input()
print (h(l,i))

#same programme without int an with int
def h(l,i):
    print (l + i)
l = input()
l = int(l)
i = input()
i = int(i)
h(l,i)

def h(l,i):
    print (l + i)
l = input()
i = input()
h(l,i)

# a project
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
def computepay(h,r):
    if h > r :
        o = h -40
        l = (40 * r)+(o * r * 1.5)
        return l
    else :
        return h * r

h = input("Enter Hours:")
h = float(h)
r = input("rate")
r = float (r)
p = computepay(h,r)
print("Pay",p)

#loops
n = input ("a number")
n = int(n)
while n > 0 :
    print ("umm")
    n = n - 1
print ("done")


def h(l,i):
    return (l + i)
l = input("a number")
l = int(l)
i = input("second number")
i = int(i)
n = input ("any number")
n = int(n)
while n > 0 :
    print (h(l,i))
    n = n - 1
    print ("again!!)):")
print ("done")

while True:
    ola = input("Your name???")
    if ola == "prabesh":
        break
    print(ola,"?? Nope. Try again")
print(ola, "Hello there")

while True:
    ola = input("Username ")
    if ola != "Prabesh":
        continue #continue will take the loop to the top again if the condition matches
    print ("Welcome")
    ola = input("Password ")
    if ola == "admin":
        print ("Welcome", ola)
        break
print ("Thank you")

for i in [1, 2,  3, 4, 5]:
    print("the next number is", i)
print("done")

friends = ["Dhrup", "Bizay", "Subekshya"]
for i in friends:
    print("hello", i)
print("okay")

#to find the greates number
l = -1
print ("the largest num till now is", l)
for num in [4, 2, 3, 8, 5, 6, 67]:
    if num > l:
        l = num
    print ("the greatest number till now:", l)
print ("so the greatest is", l)

#counting in loop
z = 0
print ("there are", z , "names in total")
for i in ["ola", "pola", "hola", "lola"] :
    z = z + 1 
    print (i)
print("there are", z, "names in total ")

z = 0
print ("sum till now is is", z )
for i in [1, 2, 3, 4, 5] :
    z = z + i 
    print (i)
print("Total sum is", z)

#to find which temp is not normal
for i in [24, 54, 76, 28]:
    if i > 50 :
        print(i, "is hot temp")
print ("done")

#to find wether there is 3 in given data or not
print ("dont know till now")
f = False
for i in [1, 2, 3, 4, 5, 6, 7]:
    if i == 3:
        f = True
        print (f, "there is 3")
        break
    else :
        print ("there is no number 3 till now")
print ("Done")

#to find the smallest number
l = None  # none is a null value
print ("the smallest num till now is", l)
for num in [4, 2, 3, 8, 5, 6, 1]:
    if l is None: #there is also is not
        l = num
    elif num < l:
        l = num
        print ("the smallest number till now:", l)
print ("so the smallest is", l)

#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except :
        print("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)





