from tuomari import Tuomari

class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()
            if self._onko_ok_siirto(ekan_siirto, tokan_siirto):
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
            else:
                break

        print("Kiitos!")
        print(tuomari)


    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return "k"

    def _onko_ok_siirto(self, ekan_siirto, tokan_siirto):
        siirrot  = ["k", "p", "s"]
        if ekan_siirto in siirrot and tokan_siirto in siirrot:
            return True
        return False
