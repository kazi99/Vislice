#Definirajmo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o' 

ZMAGA = 'W'
PORAZ = 'X'

#Definirajmo logicni model kode

class igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo # string
        self.crke = crke # list
        return

    def pravilne_crke(self):
        sez = []
        for i in range(len(self.geslo)):
            if self.geslo[i] in self.crke:
                sez.append(self.geslo[i])
        return sez

    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne.append(crka)
        return napacne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        if self.poraz():
            return False
        else:
            for crka in self.geslo:
                if crka not in self.pravilne_crke():
                    return False
            return True

    def pravilni_del_gesla(self):
        sez_geslo = list(self.geslo)
        sez_rezultat = []
        for crka in sez_geslo:
            if crka in self.pravilne_crke():
                sez_rezultat.append(crka)
            else:
                sez_rezultat.append('_')
        rezultat = ' '.join(sez_rezultat)
        return rezultat


                    


            


  




igrica = igra('abc', ['a','i','j'])
igrica.pravilne_crke()
igrica.napacne_crke()
igrica.poraz()
igrica.zmaga()
igrica.pravilni_del_gesla()