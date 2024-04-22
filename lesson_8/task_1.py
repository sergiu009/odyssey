# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list = []
for i in range(1,11):
    list.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for i in list:
    if i % 2 == 0:
        print(f"Numarul este par:{i}")
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
dictionary = {
    "name":"Erick",
    "age":28,
    "city":"New-York"
}
print(dictionary.items())
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(f"Element:{row}")
# CODUL TĂU VINE MAI SUS:

for i in range(1, 16):
    print(f"Numarul: {i}")

# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for i,x in enumerate(list):
    print(f"Indexul :{i} Valoarea :{x}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
nume = ["Andrei", "Albert", "Laur"]
age = [25, 19, 31]
for i in zip(nume,age):
    print(i)
# CODUL TĂU VINE MAI SUS:

    # Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista_numere = []
for i in range(1,11):
    lista_numere.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while lista_numere[0] < 50:
    for i in range(len(lista_numere)):
        lista_numere[i] *= 2
print(lista_numere)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
lista2 = []
for i in range(1,101):
    i *= i
    lista2.append(i)
print(lista2)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
sapte = 7
for i in range (1,11):
    inmultirea_cu_sapte = i * sapte
    print(f"Tabla inmultirii cu {i} x {sapte} = {inmultirea_cu_sapte}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista_de_liste = [[] for _ in range(5)]
for i in range(1,6):
    lista_de_liste[i - 1].append(i)
for j in range(5,0,-1):
      lista_de_liste[5 - j].append(j)
print(lista_de_liste)

# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for i,j in lista_de_liste:
    if i < j:
        print(f"{i}<{j} ")
        
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
numere_r = [5, 6, 10, 7, 2, 29, 173]
i = 0
while i <= len(numere_r):
    if numere_r[i] > 10:
        print(f"Numarul {numere_r[i]} este mai mare decat 10")
        break
    else:
        i += 1
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
patrat = int(input("Introdu dimenisunea patratului: "))
for i in range(patrat): 
    rand = ["*" for _ in range(patrat)]
    print(" ".join(rand))
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(7):
    for j in range(1, i + 1):
        print(j, end='')
    print()    

# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end='')
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
text = "abcdefg"

for i in range(len(text)):
    print(text[i:])

# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
i = 2
while i < 10:
    if i % 2 == 0:
        print("+-+-+-+-+-+-+-+-")
        i += 1
    elif i % 2 != 0:
        print("-+-+-+-+-+-+-+-+")
        i += 1
    else:
        i += 1
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
for i in range(1,7):
    for j in range(1,i):
        trei = 3 ** j
        print(trei,end=' ')
    print()
for i in range(2, 6):
    for j in range(i, 6):
        trei = 3 ** j
        print(trei, end=' ')
    print()
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
