from random import randrange

pole = '--------------------' 

import util
import ai


def vyhodnot(pole):
    if ("xxx" in pole):
        return "x"
    elif ("ooo" in pole):
        return "o"
    elif ("-" not in pole):
        return "!"
    else:
        return "-"

def tah_hrace(pole):
    symbol = 'x'
    while True: 
        cislo_policka = int(input('Na kterou pozici chces hrat? '))
        if cislo_policka < 0 or cislo_policka > 19:
            print('zadal jsi spatnou pozici')          
        elif pole[cislo_policka] != '-': 
            print('Policko je obsazene')
        else:
            return util.tah(pole, cislo_policka, symbol)

def piskvorky1d():
    pole = "--------------------"
    while True:
        pole = tah_hrace (pole)
        aktualni_stav = vyhodnot(pole)
        if aktualni_stav == '-':
            pole = ai.tah_pocitace (pole)
            print(pole)
            aktualni_stav = vyhodnot(pole)
        if aktualni_stav == '!':
            print ('Remiza')
            break
        elif aktualni_stav == 'x':
            print ('Vyhral clovek')
            break
        elif aktualni_stav == 'o':
            print ('Vyhral pocitac')
            break
    print(pole)