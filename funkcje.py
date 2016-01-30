# obliczam powierzchnie 3 okien

def oblicz_powierznie_prostokata(szerokosc, wysokosc):
    powierzchnia = szerokosc * wysokosc
    return powierzchnia


powierzchnia = oblicz_powierznie_prostokata(1.2, 1.2)
print powierzchnia

powierzchnia2 = oblicz_powierznie_prostokata(1.1, 1.3)
print powierzchnia2

powierzchnia3 = oblicz_powierznie_prostokata(1.5, 1.3)
print powierzchnia3

suma_powierzni = powierzchnia + powierzchnia2 + powierzchnia3
print "suma_powierzni = %s" % suma_powierzni