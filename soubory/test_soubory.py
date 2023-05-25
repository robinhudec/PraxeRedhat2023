import pytest
import soubory


@pytest.mark.parametrize("a, b", [("", "adresa")])
def test_zapis_neexistujici_adresa_except(a,b):
    with pytest.raises(Exception):
            soubory.zapis_jako_text(a, b)


@pytest.mark.parametrize("obsah, kam", [("idk", "./testsouboru.txt")])
def test_zapis_souboru_obsah(obsah, kam):
    obsahkontrola=""
    soubory.zapis_jako_text(obsah, kam)
    with open(kam, mode="rt") as soubor:
        obsahkontrola=soubor.read()
    assert obsah == obsahkontrola


@pytest.mark.parametrize("adresar", ["fds"])
def test_vypis_dir_except(adresar):
    with pytest.raises(Exception):
        soubory.vypis_dir(adresar)