import os.path
from pathlib import Path


def vypis_jmeno_bash(nazev):
    with open(nazev, mode="rt") as soubor:
        obsah = soubor.readlines()
    rozdelene = []
    obsah_upraveny = ""
    for i in obsah:
        rozdelene = i.split(":")
        print(f"Uzivatelske jmeno: {rozdelene[0]} Implicitni bash: {rozdelene[-1][:-1]} ")
        obsah_upraveny += f"Uzivatelske jmeno: {rozdelene[0]} Implicitni bash: {rozdelene[-1][:-1]} \n"
    return obsah_upraveny


def zapis_jako_text(obsah, kam):
    with open(kam, mode="wt") as soubor:
        soubor.write(obsah)


def vypis_dir(cesta):
    adresar = Path(cesta)
    for i in adresar.iterdir():
        if os.path.isdir(i):
            print(f"{i}\tdir")
        else:
            print(f"{i}\tfile")


vypis_jmeno_bash("/etc/passwd")
vysledek = vypis_jmeno_bash("/etc/passwd")

zapis_jako_text(vysledek, "./soubor")
vypis_dir("/etc/")