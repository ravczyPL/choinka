def rysuj_choinke(wysokosc):
    for i in range(wysokosc):
        # Rysowanie spacji
        for j in range(wysokosc - i - 1):
            print(" ", end="")
        # Rysowanie gwiazdek
        for k in range(2 * i + 1):
            print("*", end="")
        # Nowa linia po każdym poziomie choinki
        print()

# Przykład użycia
try:
    wysokosc = int(input("Podaj wysokość choinki: "))
    rysuj_choinke(wysokosc)
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą.")