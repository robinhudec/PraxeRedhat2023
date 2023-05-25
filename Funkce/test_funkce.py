import funkce
import pytest

@pytest.mark.parametrize("a,b,c", [(2, 0, 8), (2, 3, 10), (1.2, 0, 4.8)])
def test_obvod_spravne(a, b, c):
    assert funkce.obvod(a, b) == c


@pytest.mark.parametrize("a", [(-2)])
def test_obvod_minus(a):
    with pytest.raises(Exception):
        funkce.obvod(a)

@pytest.mark.parametrize("a", [("a")])
def test_obvod_str(a):
    with pytest.raises(Exception):
        funkce.obvod(a)

@pytest.mark.parametrize("a", [("a")])
def test_obsah_str(a):
    with pytest.raises(Exception):
        funkce.obsah(a)

@pytest.mark.parametrize("a, b, c", [(2, 0, 4), (2, 3, 6), (1.2, 0, 1.44)])
def test_obsah_spravne(a,b,c):
    assert funkce.obsah(a, b) == c

@pytest.mark.parametrize("a", [(-2)])
def test_obsah_minus(a):
    with pytest.raises(Exception):
        funkce.obsah(a)

@pytest.mark.parametrize("a, b", [(0,1), (4, 24)])
def test_faktorial_spravne(a, b):
    assert funkce.faktorial(a) == b

@pytest.mark.parametrize("a", [(-2), ("idk")])
def test_faktorial_except(a):
    with pytest.raises(Exception):
        funkce.faktorial(a)

@pytest.mark.parametrize("a, b", [({1:3, "a":1.0, 2:3}, 10)])
def test_soucet_spravne(a, b):
    assert funkce.secist(a) == b