import math

class Vypocet:
    def __init__(self, a: int, b: int = None):
        if b == None:
            self.b = a
        else:
            self.b = b

        self.a = a

    def obvod(self):
        return 2 * (self.a + self.b)

    def obsah(self):
        return self.a * self.b

    def uhlopricka(self):
        return math.sqrt(self.b**2+self.a**2)

    def pomer(self):
        delitel = math.gcd(self.a, self.b)
        pomer = f"{int(self.a/delitel)}:{int(self.b/delitel)}"
        return pomer


v1 = Vypocet(2,4)
print(v1.uhlopricka())
print(v1.pomer())
