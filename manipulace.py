import os.path
from pathlib import Path


class Manipulace:
    def __init__(self, obsah, kam):
        self.obsah = obsah
        self.kam = kam

    @staticmethod
    def vypis_jmeno_bash():
        with open("/etc/passwd", mode="rt") as soubor:
            obsah = soubor.readlines()
        rozdelene = []
        obsah_upraveny = ""
        for i in obsah:
            rozdelene = i.split(":")
            obsah_upraveny += f"Uzivatelske jmeno: {rozdelene[0]} Implicitni bash: {rozdelene[-1][:-1]} \n"
        return obsah_upraveny

    @staticmethod
    def zapis_jako_text(obsah, kam):
        with open(kam, mode="wt") as soubor:
            soubor.write(obsah)

        print(f"Do souboru {kam} bylo zapsáno:\n{obsah}\n")


    def etc_zapis_soubor(self, kam):
        Manipulace.zapis_jako_text(Manipulace.vypis_jmeno_bash(), kam)


    def libovolny_zapis_soubor(self, obsah, kam):
        Manipulace.zapis_jako_text(obsah, kam)

    @staticmethod
    def vypis_dir(cesta):
        adresar = Path(cesta)
        for i in adresar.iterdir():
            if os.path.isdir(i):
                print(f"{i}\tdir")
            else:
                print(f"{i}\tfile")


m = Manipulace("n", "./txt.txt")
m.etc_zapis_soubor("./txt.txt")
