# obliczam powierzchnie 3 okien

def oblicz_powierznie_prostokata(szerokosc, wysokosc):
    powierzchnia = szerokosc * wysokosc
    return powierzchnia
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
suma_powierzni = 0
suma_powierzni = suma_powierzni + oblicz_powierznie_prostokata(1.2, 1.2)
suma_powierzni = suma_powierzni + oblicz_powierznie_prostokata(1.1, 1.3)
suma_powierzni = suma_powierzni + oblicz_powierznie_prostokata(1.5, 1.3)
print "suma_powierzni = %s" % suma_powierzni

# -------------------------------------------------------------------------
suma_powierzni = 0
for (szerokosc, wysokosc) in [(1.2, 1.2), (1.1, 1.3), (1.5, 1.3)]:
    # print (szerokosc, wysokosc)
    suma_powierzni = suma_powierzni + oblicz_powierznie_prostokata(szerokosc, wysokosc)
print "suma_powierzni = %s" % suma_powierzni