from komentotehdas import Komentotehdas
class Peli:
    def __init__(self, io):
        self.io = io
        self.komentotehdas = Komentotehdas(io)

    def suorita(self):        
        while True:
            self.io.kirjoita("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
            )
            vastaus = self.io.lue()
            pelityyppi = self.komentotehdas.hae(vastaus)
            if pelityyppi:
                self.io.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
                pelityyppi.pelaa()
            else:
                break