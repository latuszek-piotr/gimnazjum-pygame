import math


def przesuniecie_w_kierunku(odleglosc, kierunek):
    """
    Wylicza przesuniecie dx, dy dla ruchu na dana odleglosc w podanym kierunku
    odleglosc - w punktach sceny (float)
    kierunek  - w stopniach (float)
    """
    dx = odleglosc * math.cos(math.radians(kierunek))
    dy = odleglosc * math.sin(math.radians(kierunek))
    return dx, dy

def odleglosc(start_point, end_point):
    """
    Wylicza odleglosc miedzy punktami
    start_point - para int
    end_point   - para int
    """
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    return math.sqrt(dx*dx + dy*dy)
