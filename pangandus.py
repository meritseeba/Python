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

    def vota_raha(self, summa):
        """Võtab raha välja kontolt"""
        if summa <= 0:
            print("Summa peab olema positiivne!")
        elif summa > self.saldo:
            print("Puudub piisav saldo!")
        else:
            self.saldo -= summa
            print(f"Võetud: {summa} EUR")

    def konto_jaak(self):
        """Kuvab konto jäägi"""
        print(f"Konto {self.konto_number} jääk: {self.saldo} EUR")


# Testime süsteemi
konto = Konto("EE123456789", 500)  # Konto loomine 500 EUR algsaldo

konto.konto_jaak()  # Kuvab konto jäägi
konto.lisa_raha(200)  # Lisame raha
konto.vota_raha(100)  # Võtame raha välja
konto.konto_jaak()  # Kuvab uuesti konto jäägi
