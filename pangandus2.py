class Konto:
    def __init__(self, konto_number, saldo=0):
        self.konto_number = konto_number  # Konto number
        self.saldo = saldo  # Konto algsaldo

    def lisa_raha(self, summa):
        """Lisab raha kontole"""
        if summa > 0:
            self.saldo += summa
            print(f"Lisatud: {summa} EUR")
        else:
            print("Summa peab olema positiivne!")
        self.konto_jaak()

    def vota_raha(self, summa):
        """Võtab raha välja kontolt"""
        if summa <= 0:
            print("Summa peab olema positiivne!")
        elif summa > self.saldo:
            print("Puudub piisav saldo!")
        else:
            self.saldo -= summa
            print(f"Võetud: {summa} EUR")
        self.konto_jaak()

    def konto_jaak(self):
        """Kuvab konto jäägi"""
        print(f"Konto {self.konto_number} jääk: {self.saldo} EUR")


# Testime süsteemi
konto = Konto("EE123456789", 500)  # Konto loomine 500 EUR algsaldo
konto.konto_jaak()  # Kuvame konto jäägi

# Kasutaja saab raha juurde panna ja välja võtta
while True:
    toiming = input("Sisesta toiming (lisa, vota, lopeta): ").strip().lower()

    if toiming == "lisa":
        summa = float(input("Sisesta summa, mida soovid lisada: "))
        konto.lisa_raha(summa)
    elif toiming == "vota":
        summa = float(input("Sisesta summa, mida soovid välja võtta: "))
        konto.vota_raha(summa)
    elif toiming == "lopeta":
        print("Programmi lõpetamine.")
        break
    else:
        print("Vale sisend! Kasuta 'lisa', 'vota' või 'lopeta'.")
