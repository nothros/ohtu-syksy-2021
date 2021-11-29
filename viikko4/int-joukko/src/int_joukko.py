KAPASITEETTI = 5
KASVATUSKOKO = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = KAPASITEETTI
        self.kasvatuskoko = KASVATUSKOKO
        self.int_joukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.int_joukko

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        if self.alkioiden_lkm == len(self.int_joukko):
            self.int_joukko.append([0]*self.kasvatuskoko)
        
        self.int_joukko[self.alkioiden_lkm]=n
        self.alkioiden_lkm += 1
        return True

    def poista(self, poistettava):
        if not self.kuuluu(poistettava):
            return False
        
        self.alkioiden_lkm -= 1
        self.int_joukko.remove(poistettava)
        self.int_joukko.append(0)
        
        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [luku for luku in self.int_joukko[:self.alkioiden_lkm]]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        uusi_joukko = IntJoukko()
        yhdiste = joukko1.to_int_list() + joukko2.to_int_list()
        for luku in yhdiste:
            uusi_joukko.lisaa(luku)
        return uusi_joukko

    @staticmethod
    def leikkaus(joukko1, joukko2):
        uusi_joukko = IntJoukko()

        for luku in joukko1.to_int_list():
            if joukko2.kuuluu(luku):
                uusi_joukko.lisaa(luku)

        return uusi_joukko

    @staticmethod
    def erotus(joukko1, joukko2):
        uusi_joukko = IntJoukko()
        for luku in joukko1.to_int_list():
            if not joukko2.kuuluu(luku):
                uusi_joukko.lisaa(luku)
        return uusi_joukko

    def __str__(self):
        return (f"{{{', '.join(str(luku) for luku in self.to_int_list())}}}")