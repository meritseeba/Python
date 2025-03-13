import math

class Cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def liitmine(self):  # Liitmine
        return self.a + self.b

    def lahutamine(self):  # Lahutamine
        return self.a - self.b

    def korrutamine(self):  # Korrutamine
        return self.a * self.b

    def jagamine(self):  # Jagamine
        if self.b == 0:  # Kontroll, et ei jagataks nulliga
            return "Jagamine nulliga ei ole lubatud!"
        return self.a / self.b

    def jaak(self):  # Modulo (jäägi leidmine)
        return self.a % self.b

    def ruutjuur(self):  # Ruutjuure leidmine
        if self.a < 0:  # Kontroll, et ei üritaks võtta negatiivset ruutjuurt
            return "Negatiivsete arvude ruutjuur ei ole määratletud!"
        return math.sqrt(self.a)

def menu():
    # Kuvab menüü valikud
    print('1. Liitmine')
    print('2. Lahutamine')
    print('3. Korrutamine')
    print('4. Jagamine')
    print('5. Jäägi leidmine')
    print('6. Ruutjuure leidmine')
    print('0. Väljumine')

# Kasutaja sisendi küsimine
a = int(input("Sisesta esimene number: "))
b = int(input("Sisesta teine number: "))

kalk = Cal(a, b)

while True:
    menu()  # Kuvab menüü
    valik = int(input('Sisesta üks valikutest: '))

    if valik == 1:
        print("Vastus: ", kalk.liitmine())
    elif valik == 2:
        print("Vastus: ", kalk.lahutamine())
    elif valik == 3:
        print("Vastus: ", kalk.korrutamine())
    elif valik == 4:
        print("Vastus: ", kalk.jagamine())
    elif valik == 5:
        print("Vastus: ", kalk.jaak())
    elif valik == 6:
        print("Vastus: ", kalk.ruutjuur())
    elif valik == 0:
        print("Programmi lõpp.")
        break  # Väljub tsüklist ja lõpetab programmi
    else:
        print("Vale valik, palun proovi uuesti.")