from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori=[]
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara=0
        for t in self._ostoskori:
            maara += t.lukumaara() 
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        yht_hinta = 0
        for o in self._ostoskori:
            yht_hinta+=o.hinta()
        return yht_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for o in self._ostoskori:
            if o.tuotteen_nimi() == lisattava.nimi():
                o.muuta_lukumaaraa(1)
                return

        self._ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for o in self._ostoskori:
            if o.tuotteen_nimi() == poistettava.nimi():
                o.muuta_lukumaaraa(-1)
                if o.lukumaara() == 0:
                    self._ostoskori.remove(o)
                return

    def tyhjenna(self):
        self._ostoskori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on