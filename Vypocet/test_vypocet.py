import pytest
from vypocet import Vypocet

class TestVypocet:
    def test_obvod_spravny(self):
        v1 = Vypocet(1,3)
        v2 = Vypocet(4.2,3)
        v3 = Vypocet(1,2)
        assert v1.obvod() == 8
        assert v2.obvod() == 14.4
        assert v3.obvod() == 6

    def test_obvod_spatne_zadane(self):
        v1 = Vypocet(1,"a")
        with pytest.raises(TypeError):
            v1.obvod()

    def test_obsah_spravny(self):
        v1 = Vypocet(1, 3)
        v2 = Vypocet(4.2, 3)
        v3 = Vypocet(2, 2)
        assert v1.obsah() == 3
        assert v2.obsah() == 12.600000000000001
        assert v3.obsah() == 4
