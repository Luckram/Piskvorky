from random import randrange
import util

def tah_pocitace(pole, symbol = 'o'):
   # symbol = 'o' 
 
    if pole.find("o-o") != -1:
        cislo_policka = pole.find("o-o")
        return util.tah (pole, cislo_policka + 1, 'symbol')

    elif pole.find("-o-") != -1:
        cislo_policka = pole.find("-o-")
        return util.tah (pole, cislo_policka, symbol)

    elif pole.find("oo-") != -1:
        cislo_policka = pole.find("oo-")
        return util.tah (pole, cislo_policka + 2, symbol)

    elif pole.find("-oo") != -1:
        cislo_policka = pole.find("-oo")
        return util.tah (pole, cislo_policka, symbol)
      
    while True:
        cislo_policka = randrange(0, 19)
        if pole[cislo_policka] == "-":
            return util.tah (pole, cislo_policka, symbol)