#Zmienne
wynik = 0
tymczasowa_tablica = []
#### FUNKCJE ######


def dodawnie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def dzielenie(a, b):
    return a / b

def mnozenie(a, b):
    return a * b


#Sprawdzanie czy dzialanie ma dozwolne znaki
def sprawdzanie_dzialania_znaki(a):
 for znak in a:
    znak = str(znak)
    if znak != "1" or znak != "2" or znak != "3" or znak != "4" or znak != "5" or znak != "6" or znak != "7" or znak != "8" or znak != "9" or znak != "0" or znak != "*" or znak != "/" or znak != "+" or znak != "-" or znak != "(" or znak != ")":
        return 0
    else:
        return 1

# wykonywanie operacji

def dzialanie(a):

    for i, znak in enumerate(a):
        znak = str(znak)
        if znak == "1" or znak == "2" or znak == "3" or znak == "4" or znak == "5" or znak == "6" or znak == "7" or znak == "8" or znak == "9" or znak == "0":
            cyfra = cyfra  + znak
        if znak == "*" or znak == "/" or znak == "+" or znak == "-":
            tymczasowa_tablica.append(cyfra)
        if i == len(a):
            tymczasowa_tablica.append(cyfra)






# sprawdzanie czy sa nawiasy

def dzialanie_nawiasy(a):
 start_nawias = 0
 end_nawias = 0
 for i,znak in enumerate(a):
    znak = str(znak)
    if znak == "(":
        start_nawias = i
 for i, znak in enumerate(reversed(a)):
    znak = str(znak)
    if znak == ")":

        end_nawias = len(a) - i

 print(a[start_nawias:end_nawias],start_nawias,end_nawias)



#Wprowadzannie dzialania
dzialanie = input()
sprawdzanie_dzialania_nawiasy(dzialanie)


##MAIN CODE##

#Wyswietl wynik
print("Wynik to  : ", wynik)