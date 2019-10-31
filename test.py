tymczasowa_tablica = []
a = "1+2-3*4/6"


def dzialanie(a):
    cyfra = ""
    count = 0
    for i, znak in enumerate(a):
        znak = str(znak)
        if znak == "1" or znak == "2" or znak == "3" or znak == "4" or znak == "5" or znak == "6" or znak == "7" or znak == "8" or znak == "9" or znak == "0":
            cyfra = cyfra + znak
            if i >= (len(a) - 1):
                tymczasowa_tablica.append(int(cyfra))
        if znak == "*" or znak == "/" or znak == "+" or znak == "-":
            tymczasowa_tablica.append(int(cyfra))
            tymczasowa_tablica.append(znak)
            cyfra = ''

    for x in tymczasowa_tablica:
        if x == "*":
            print(count, tymczasowa_tablica[count - 1])
            print(count, tymczasowa_tablica[count])
            print(count, tymczasowa_tablica[count + 1])

            liczba_1 = tymczasowa_tablica[count - 1]
            liczba_2 = tymczasowa_tablica[count + 1]

            liczba_1 = int(liczba_1)
            liczba_2 = int(liczba_2)

            wynik = liczba_1 * liczba_2

            tymczasowa_tablica.__delitem__(count - 1)
            tymczasowa_tablica.__delitem__(count)
            tymczasowa_tablica.__delitem__(count + 1)

            tymczasowa_tablica.

            print(wynik)



        count = count + 1




dzialanie(a)

print(tymczasowa_tablica)
