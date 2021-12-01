fruit = "apple"
x = fruit[1]
print (x)
ola = 3
hola = fruit [ola - 1 ]
print (hola)

try:
    ola = "apple"
    hola = ola[7]
    print (hola)
except:
    print ("invalid")

hola = len(fruit)
print (hola)#number of characters

n = "prabesh"
o = 0
while o < len(n):
    l = n[o]
    print (o, l)
    o = o + 1
print ("so there are", o ,"letters in prabesh")

for letter in n:
    print (letter)

# to find how many "a" are there in banana'
n = "banana"
x = 0
for letter in n:
    if letter == "a" :
        x = x + 1
print ("there are ", x, "numbers of a in banana")

print (n[0:4])
print (n[2:4])
print (n[0:20])
print (n[:])

p = input("type banana")
o = 0
for letter in p:
    if letter == "a":
        o = o +1
    print (letter)
print (o)

a= "hola "
b = input("name?")
la = a + b
print (la)

p = "prabesh"
'p' in p

if 'p' in p :
    print ("yes ")

"rab" in p

"r" in p

#1
word = input()
if word < "banana":
    print("your word comes before banana")
else:
    print("it comes after banana")

#to print in lower case
ola = word.lower()
print(ola)

#to find the word comes wherre in after banana
#1 will not work right because of the lower and upper class letter
word = input()
word = word.lower()
if word < "banana":
    print("your word comes before banana")
else:
    print("it comes after banana")

dir (word)

#it finds position of words in the given string
pos = word.find("a")
print(pos)


word = word.upper()
print (word)

greet = "   hello bob    "
nstr = greet.replace("hello", "hola")
print (nstr)
ostr = greet.replace("o", "e")
print(ostr)

#strip, lstrip, rstrip removes spaces
greet = "   hello bob        "
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip())

print(greet.startswith("hello"))
print(greet.startswith(""))

greet = "hello bob"
print(greet.startswith("hello"))
print(greet.startswith("ola"))

ola = "hi its me Prabesh.Sagar.Baral from olapola"
data= ola.find("Prabesh")
print (data)
spos = ola.find(" ",data )
print (spos)
host = ola[data : spos]
print(host)
host = ola[data + 1 : spos]
print(host)

stuff = "ola\nhola"
print (stuff)
o = len(stuff)
print (o)

ola = open("Programming.txt")
count = 0
i = ola.read()
print (i)
print("number of words", len(i))
print (i[:22])

ola = open("Programming.txt")
for words in ola:
    count = count + 1
print("number of line", count)

ola = open("Programming.txt")
c = 0
for line in ola:
    if line.startswith("o"):
        c = c + 1
        print (line)
        print (c)

#now to remove spaces between the lines in above programme and print the file 
ola = open("Programming.txt")
for line in ola:
    line = line.rstrip()
    if line.startswith("o"):
        print (line)

#same programme with diff idea
ola = open("Programming.txt")
for line in ola:
    line = line.rstrip()
    if not line.startswith("o"):
        continue
    print (line)

hola = input("a file")
try :
    ola = open(hola)
except:
    print("no file")
    quit()
for line in ola:
        line = line.rstrip()
        if not "ola" in line:
            continue
        print (line)

friends = [[1,"dhrup"], 2, "bijay", "bhuwan"]
print(friends)
for i in friends:
    print (i)

friends = ["dhrup", "bijay", "bhuwan", "dorjii", "prabesh"]
for i in friends:
    print ("happy new year", i)
print (friends[1])

friends[2] = "darjii"
print (friends)

print (len(friends))

print (range(4))

friends = ["dhrup", "bijay", "bhuwan", "dorjii", "prabesh"]
print (range (len(friends)))


friends = ["dhrup", "bijay", "bhuwan", "dorjii", "prabesh"]
for i in range(len(friends)):
    friend = friends[i]
    print(friend)    

a = [1, 2, 3]
b = ["prabesh", "subekshya", "afra", "Mays", "Kaya", "Irina"]
print (a + b)
b[1:3]

b.append("baby")
b.append ("big baby")
print(b)

b = ["prabesh", "subekshya", "afra", "Mays", "Kaya", "Irina"]
"prabesh"in b

b = ["prabesh", "subekshya", "afra", "Mays", "Kaya", "Irina"]
b.sort()
print (b)

a = [1, 2, 3, 4, 5 ]
print (max(a))
print(min(a))
print(sum(a))
print(range(len(a)))

numlist = list()#creates a empty list
i = input("input a name")
numlist.append(i)
print (numlist)

# own project
# to find the first and last name from the given full name data
oal = input("your full name")
o = oal.split() 
s = 0
for i in range(len(o)):#range fuction returns a list of numbers that range from zero to one less than the parameter 
    if i == s:
        a = o[i]
        print ("your first name is", a)
        continue
    else:
        a = o[i]
print ("your last name is", a)

ola = ("prabesh;sagar;baral")
o = ola.split(";")
print (o)

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])

ola = dict()
ola["prabesh"] = 1
ola ["Afra"] = 2
print(ola)

print(ola["prabesh"])

ola["prabesh"] = ola["Afra"]+1
print(ola)

ola["Afra"] = 3
print (ola["Afra"])

pola = {"Prab":2, "Afra": 1}
print(pola)
print(pola["Prab"])

ola = dict()
ola["Prabesh"] = 1
ola ["Afra"] = 2
"Prabesh" in ola

name = dict()
names = ["Prabesh", "Subekshya", "Usha", "Tirtha","Tirtha"]
for ola in names:
    if ola not in name:
        name[ola] = 1
    else:
        name[ola] = name[ola] + 1
print(name)

#2
name = input("random names")
name = name.split()
bom = dict()
for ola in name:
    if ola not in bom:
        bom[ola] = 1
    else:
        bom [ola] = bom[ola] + 1
print (bom)

#next method of programme 2
name = input("random names")
name = name.split()
bom = dict()
for ola in name:
    bom[ola] = bom.get(ola, 0 ) + 1
print (bom)

para = ("this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start ")
para = para.split()
bola = dict()
for ola in para:
    bola[ola] = bola.get(ola, 0) + 1
print(bola)

names = {"Prabesh":1 , "Subekshya":2, "Usha":3, "Tirtha":4}
for a,b in names.items():
    print(a,b)

name = input("Enter a file")
ola = open(name)
pola = dict()
for line in ola:
    words = line.split()
    for word in words:
        pola[word] = pola.get(word, 0) +1
print(pola)
bigword = None
bigcount = None
for word,count in pola.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)#to find which word is present in biggest amount

names = {"Prabesh":1 , "Subekshya":2, "Usha":3, "Tirtha":4}
print (list(names))#converts dictionary to lists
print (names.keys())
print (names.values())
print (names.items())

# to find which is the most repeated word in a line which starts with ola
oal = input("your file")
oa = open(oal)
d = dict()
for line in oa:
    if not line.startswith("ola"):continue
    line = line.split()
    line = line[1]
    d[line] = d.get(line, 0) + 1
bigword = None
bigcount = None
for word,count in d.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)

x = ("Prabesh", "Afra", "Sube" ) #this is a tuple and it not changeable
print(x[2])
try:
    x[2] = "Subekshya"
except:
    print("tuple cant be changed")# tuple is not chnageable, no reverse, no 

t = tuple()#tuple are more efficient
dir(t)#only you can do count and index

(x, y) = ("prabesh love", "afra")
print(x)
print(y)
print (x,y)

(0, 1, 2) < (1, 2, 3)
if True:
    print("good")

("Prabesh", "Subekshya")>("Prabesh", "Afra")#prabesh are equal but S is greater than A
if True:
    print("Brother sister bond is good and Afra is life")
else: print("Only Afra is life")

d = {"subekshya":3, "prabesh":1, "Afra":2}#dictionary cant be sorted
d.items()#it changes the dictionary to tuple
sorted(d.items())#we sort the tuple which came from changing dictionary
#it is sorted by key order 

#now we sort the dictionary by changing to tuple and sort it according to the value order
d = {"subekshya":3, "prabesh":1, "Afra":2}
l = list()
for k,v in d.items():
    l.append((v,k))
print(l)
print("now sorting it")
l = sorted(l)    
print(l)
print("again reversing it")
l = sorted(l, reverse= True)
print(l)

#top 10 most common wrods in the file
f = input("a file")
f = open(f)
d= dict()
for lines in f:
    lines = lines.split()
    for word in lines:
        d[word] = d.get(word, 0) + 1
l = list()
for k,v in d.items():
    l.append((v,k))
l = sorted(l, reverse = True)
print (l)
print("now for top 10")
for v,k in l[:10]:
    print (v, k)

#1 Programme
#top 10 most common wrods in the file
try:
    f = input("a file")
    f = open(f)
except:
    print("your file name is wrong, so i put it myself")
    f = ("Programming.txt")
    f = open(f)
d= dict()
for lines in f:
    lines = lines.split()
    for word in lines:
        d[word] = d.get(word, 0) + 1
l = list()
for k,v in d.items():
    l.append((v,k))
l = sorted(l, reverse = True)
print (l)
print("now for top 10")
for v,k in l[:10]:
    print (v, k)
    
#doing 1 programme by list comprehension method
try:
    f = input("a file")
    f = open(f)
except:
    print("your file name is wrong, so i put it myself")
    f = ("Programming.txt")
    f = open(f)
d= dict()
for lines in f:
    lines = lines.split()
    for word in lines:
        d[word] = d.get(word, 0) + 1
l = list()
l = sorted( [ (v,k) for k,v in d.items() ] )#list comprehension
l = sorted(l, reverse = True)
print (l)
for v,k in l[:10]:
    print (v, k)

#new one
a=6
a==7
a>0
a<=6
a!=6
"prabesh"=="parbesh"

r = input ('your age?')
r = int(r)
if r<18 :
    print("you shall not pass kidoo")
elif r==18:
    print('just about good kiddo, get in')
else:
    print("You can pass")

a = int(input('album year'))
if a>1980 and a<1989:
    print("the album was from 80's")
elif a<1980 or a> 1990:
    print ("album was not from 1980's")

p = ["red", "yellow", "blue"]
for i in range(0,3):
    p[i]= "white"
print(p)

for x in range (0,3):
    print (x+1)
for i,x in enumerate(["hello", "tori", "bachha"]):
    print (i,x)

#doesnot print after black
squares = ["orange", "red", "orange", "red", "black", "red", "orange"]
result = []
i = 0
while squares[i]=="orange" or squares[i]=="red": 
    result.append(squares[i])
    i = i +1
print (result)

#Write a while loop to display the values of the Rating of an album playlist stored in the list
#If the score is less than 6, exit the loop
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
while PlayListRatings[i]>=6:
    rating = (PlayListRatings[i])
    print (rating)
    i = i + 1    
print ("it took",i, "songs to finally end the playlist")

#function
album_rating = [1, 2, 5, 4, 8, 9, 0 ,4]
sorted_album_rating = sorted(album_rating)
print(sorted_album_rating)
print(album_rating)
album_rating.sort()
print(album_rating)

def add1(a,b):
    """
    this is called documentation string
    """
    d = a*b
    print (a, "*", b, "equals \n", d)
    return d

add1(10,20)
help(add1)

def llll():
    print ("empty")
llll()

#album ratings of diff artists
def printrat(rate):
    for k in (rate.keys()):
        s=(rate[k])
        print ("album of", k, "is rated", s)
rate={"eena":10,"meeena":2,"reena":10,"tika":2}
printrat(rate)

def th():
    date = 1982
    return date
date = 1700
print (date)
th()#here the value of date inside function is diff than outside of function
#which means that the outer value doesnot affect the vlaue in side the functions

def Pinkfloyd():
    global sales #this "global" keyword can transfer the value of sales inside function to be effective outside as well unlike previous program where booth are differrent
    sales = "25 Million"
    return sales
print (sales)

#exception handling
try:
    s = input("Your name")
    c = int(input("Your age"))
except:
    print("unable to write data. pls use an integer in age")
else:
    print("your name is", s, "and age is", c)
    print("the data is written")
finally:#not really required in this program but is helpful for other big programs
    print("The program has ended")
