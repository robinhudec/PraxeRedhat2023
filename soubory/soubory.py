import os.path
from pathlib import Path


def vypis_jmeno_bash():
    with open("/etc/passwd", mode="rt") as soubor:
        obsah = soubor.readlines()
    rozdelene = []
    obsah_upraveny = ""
    for i in obsah:
        rozdelene = i.split(":")
        print(f"Uzivatelske jmeno: {rozdelene[0]} Implicitni bash: {rozdelene[-1][:-1]} ")
        obsah_upraveny += f"Uzivatelske jmeno: {rozdelene[0]} Implicitni bash: {rozdelene[-1][:-1]} \n"
    return obsah_upraveny
    

def zapis_jako_text(obsah, kam):
    if os.path.exists(kam) != True:
        raise Exception
    else:
        with open(kam, mode="wt") as soubor:
            soubor.write(obsah)
        return 0

def vypis_dir(adresar):
    if os.path.exists(adresar) == False:
        raise Exception
    else:
        for i in adresar.iterdir():
            if os.path.isdir(i):
                print(f"{i}\tdir")
            else:
                print(f"{i}\tfile")



