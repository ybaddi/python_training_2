#function
def currentYear():
    print('2021')

def f(x,y):
    return x*y

currentYear()

print(f(3,2))
resultat = f(3,4)
print(resultat)

# #################################
list = []
numbers = [1,2,3,4,5,6,7,8,9]
characters = ['A','B','C','D','E','F']

print(characters)

print(characters[1])

print(characters[-1])

print(characters[-6])
print(max(characters))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

characters_1 = ['A','B','C',30,'E','F']
print(characters_1)

print(numbers)
numbers.append(11)
print(numbers)
# remove the last element
numbers.pop()
print(numbers)
# remove the element with index passed as param
numbers.pop(2)
print(numbers)
# remove element passed as param
numbers.remove(2)
print(numbers)
# sort in the oposite order
numbers.reverse()
print(numbers)

#  sort element
numbers.sort()
print(numbers)



# //////////////////////////////////

def carre(x): return x ** 2

def small_carre(x): return x ** 2 <20

def pair(x): return not bool(x % 2)

def impair(x): return bool(x % 2)

def puiss_3(x): return x ** 3

def apply_callback(callback, value):
    return callback(value)


print(apply_callback(carre, 3))
print(apply_callback(puiss_3, 3))

def map(callback, liste):
    new_liste= []
    for item in liste:
        new_liste.append(callback(item))
    return new_liste

def filtre(callback, liste):
    new_liste= []
    for item in liste:
        if callback(item): new_liste.append(item)
    return new_liste  

print(map(carre, [1,3,5]))
print(map(puiss_3, [1,3,5]))

print(filtre(small_carre, [1,3,5,6,8]))
print(filtre(pair, [1,3,5,6,8]))
print(filtre(impair, [1,3,5,6,8]))

liste = [1,3,5,6,8]
print(liste[1:])

def sum(x,y) : return x+y
def produit(x,y) : return x*y
def sum_1(element,liste) : return liste + [element ** 2]

def reduce(callback, liste , init_value):
    if liste == []: return init_value
    else: return callback(liste[0], reduce(callback, liste[1:], init_value))

print( reduce(sum, [1,2,3],0) )

print( reduce(sum_1, [1,2,3], []) )
print( map(carre, [1,2,3]) )


liste_1 = [1,2,3,4,5,6]

print([x ** 2 for x in liste_1])

print([x for x in liste_1 if x % 2 == 0])

print([x ** 2 for x in liste_1 if x **2 % 2 == 0])
print([x for x in [y ** 2 for y in liste_1 ] if x % 2 == 0])

# convert liste en string

liste_2 = ['b','o','n','j','o','u','r']
print (''.join(liste_2))
print (','.join(liste_2))
print ('b o n j o u r'.split(' '))

#  tableau associative

players = [
    (15, "messi"),
    (10, "maradona"),
    (1, "buffon")
]

nom = "baddi"
numero = 11
print("%s %d %s %d" % (nom, numero,nom, numero))
print("%s" % nom)

print("je suis {0} et jai {1}, je suis {0} et jai {1}".format(nom,numero))

print('\n'.join(["%s a le numero %d" % (player, numero) for numero, player in players ]))
print('\n'.join(["{0} a le numero {1}".format(player, numero) for numero, player in players ]))

# range
list = [1,2,3]
print(list)

for item in range(0,200, 10): print(item)

#  dict

words = {}

words['first'] = 'baddi'
words['second'] = 'youssef'
words['third'] = 'karim'
words['fourd'] = 'alvin'
words[9] = 'alvin'
print(words)
#  read file

filename="fichier.txt"
with open(filename) as f:
    content = f.readlines()
print(content)

filename_1="fichier.txt"
infile = open(filename_1)
data=infile.read()
infile.close()

print(data)

# write file witj flags 
# w 
# r 
# a 
# a+  append and read
# r+

f = open("resultat.txt", "w+")
f.write("hello world, \n")
f.write("I am writng in my file\n")
f.write("I am writng in my file\n")



with open("resultat.txt") as f:
    content = f.read()
    print(content)

f.close()

# neted loop

players_name = ["messi","maradona","buffon"]

players_number = [15, 10, 1]

for name in players_name:
    for numero in players_number:
        print(name + " jours avec le numero " + str(numero))

# slice

print(players_name[1:2])
print(players_name[0:2])

# multiple return

def complexfunction(a,b): 
    sum = a + b
    return sum

def getPerson():
    name = "baddi"
    age = 24
    country = "fr"
    return name,age,country

print(getPerson())

name,age,country = getPerson()
print(name)
print(age)
print(country)

# globale

b=0

def add(x): 
    global b
    b = b + x
    print(b)
    return b

print(add(3))
print(b)

# Time et Date
import time
timenow = time.localtime(time.time())
first_time = time.time()
print(time.time())
print(timenow)
year, month,day,hour,minute = timenow[0:5]
print("{0}/{1}/{2}".format(year, month, day))
print("{0} : {1}".format(hour, minute))

# time.sleep(5)
second_time = time.time()
print(second_time - first_time)

print(time.gmtime())
print(time.asctime())
print(time.ctime())

x = input("Entrer le numero 1")
y= input("Entrer le numero 2")

try:
    print(int(x)/int(y))
except ZeroDivisionError:
    print("l'utilisateur a donner une valeur zero")

print("le programme continu")

try: 
    filename_2 = open("file_not_exist.txt")
    infile = open(filename_2)
    data=infile.read()
    infile.close()

    print(data)
except FileNotFoundError:
    print("file not exist")
# except 
finally:
    x="file"
    print("dont stop the except")

print("le programme continu")
print(x)


try:
    x=1
except :
    print("failed to set x")
else: 
    print("no exception lunched")
finally:
    print("we always do this")