from sigmoid_check.python_odyssey.lesson_10 import Lesson10

# Înainte de a începe, trebuie să instalați librarie `sigmoid_check` rulând comanda `pip install sigmoid_check==0.0.3` în terminal

# VERIFICATION PROCESS
session = Lesson10()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
Utilizați list comprehension.
"""

# CODUL TĂU VINE MAI JOS:
def task_1():
    list = [i for i in range(1,11)]
    return list
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(task_1))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
Utilizați list comprehension în proces
"""

# CODUL TĂU VINE MAI JOS:
def task_2():
    list_2 = [i ** 2 for i in range(1,11)]
    return list_2
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
Utilizați list comprehension în proces.
"""

# CODUL TĂU VINE MAI JOS:
def task_3():
    list_3 = [i for i in range(1,11,)if i % 2 != 0]
    return list_3
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(task_3))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
"""

# CODUL TĂU VINE MAI JOS:
def task_4(n):
    lst_aplatizata = []
    for row in n:
        for element in row:
            lst_aplatizata.append(element)
    return lst_aplatizata

matrice = [[1, 2], [3, 4], [5, 6]]
print(task_4(matrice))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până la 10.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
"""

# CODUL TĂU VINE MAI JOS:
def task_5(n:int) -> list[str]:
    return list("par" if i % 2 == 0 else "impar" for i in range(1,n+1))
listaa = task_5(10)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(n):
    dict = {i: i*i*i for i in range(1,n+1)}
    return dict
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(task_6))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
"""

# CODUL TĂU VINE MAI JOS:
def task_7(n):
    lst_3x = {i*3 for i in range(1,(n // 3) + 1)}
    return lst_3x
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(task_7))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna media aritmetică a numerelor din listă.
Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
"""

# CODUL TĂU VINE MAI JOS:
def task_8(n: list):
    media = 0
    for i in range(0,len(n)):
        media += n[i]
    media = media / len(n)
    return media
lista = [2,20,18,40]
# CODUL TĂU VINE MAI SUS:


# VERIFICATION PROCESS
print(session.check_task_8(task_8))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` dacă numărul este par, altfel `False`.
Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_9(n):
    par = True
    if n % 2 == 0:
        return par
    else:
        par = False
        return par
print(task_9(7))
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_9(task_9))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
"""

# CODUL TĂU VINE MAI JOS:
def task_10(name, varsta, oras):
    return f"Nume: {name}, Varsta: {varsta}, Oras: {oras}"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_10(task_10))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_11" care acceptă o listă variabilă de numere și returnează valoarea maximă.
Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
"""

# CODUL TĂU VINE MAI JOS:
def task_11(n: list):
    return max(n)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_11(task_11))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
Exemplu: Pentru numărul 5 rezultatul va fi 120
"""

# CODUL TĂU VINE MAI JOS:
def task_12(n: int):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_12(task_12))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
"""

# CODUL TĂU VINE MAI JOS:
def task_13(x,y: int):
    return x+y,x*y
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_13(task_13))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane și returnează textul "minor" dacă vârsta este sub 18 ani, "adult" dacă vârsta este între 18 și 65 ani și "senior" dacă vârsta este peste 65 de ani.
Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
"""

# CODUL TĂU VINE MAI JOS:
def task_14(x) -> str:
    return "minor" if x < 18 else "adult" if x <= 65 else "senior"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_14(task_14))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_15(x: str) -> bool:
    return x == x[::-1]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_15(task_15))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_16" care acceptă un string și returnează același string cu literele inversate.
Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
"""

# CODUL TĂU VINE MAI JOS:
def task_16(word: str) -> str:
    return word[::-1]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_16(task_16))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează numărul de cuvinte din string.
Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
"""

# CODUL TĂU VINE MAI JOS:
def task_17(word: str) -> int:
    return len(word.split())
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_17(task_17))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
"""

# CODUL TĂU VINE MAI JOS:
def task_18(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_18(task_18))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_19(numar: int) -> bool:
    if numar <= 1:
        return False
    for i in range(2, int(numar**0.5) + 1):
        if numar % i == 0:
            return False
    return True
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_19(task_19))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_20(numar: int) -> bool:
    if numar <= 1:
        return False
    
    suma_divizorilor = 1
    
    for i in range(2, int(numar**0.5) + 1):
        if numar % i == 0:
            suma_divizorilor += i
            if i != numar // i:
                suma_divizorilor += numar // i
                
    return suma_divizorilor == numar

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_20(task_20))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_21(numar: int) -> bool:
    numar_str = str(numar)
    puterea = len(numar_str)
    armstrong = sum(int(cifra) ** puterea for cifra in numar_str)
    return armstrong == numar
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_21(task_21))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
def task_22(numar: int) -> bool:
    numar_str = str(numar)
    suma = 0
    for i in numar_str:
        suma += int(i)
    return numar % suma == 0
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_22(task_22))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
"""

# CODUL TĂU VINE MAI JOS:
def task_23(n: int) -> list:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_23(task_23))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
"""

# CODUL TĂU VINE MAI JOS:
def task_24(numar: int) -> list:
    divizibl = []
    for i in range(1,numar + 1):
        if numar % i == 0:
            divizibl.append(i)
    return divizibl
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_24(task_24))
print(session.get_completion_percentage())
# VERIFICATION PROCESS

# Aceste sarcini te vor ajuta să înțelegi și să aplici list comprehensions în Python pentru a crea și manipula structuri de date într-un mod eficient și concis.
