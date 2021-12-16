from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
class Komentotehdas:
    def __init__(self, io):
        self.io = io

        self.komennot = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly(),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]
        else:
            return False