import pytest
from diagnostico import es_primo
from diagnostico import weighted_av

@pytest.mark.parametrize("x, esperado", [(2, True), (4, False), (6, False), (9, False), (25, False)])
def test_es_primo(x, esperado):
    assert es_primo(x) == esperado

def test_weighted_av ():
    assert weighted_av([1,2,3,4],[0.2,0.9,0.3,0.3]) == pytest.approx(41/17)
    assert weighted_av([7],[5]) == 7
    with pytest.raises(ValueError):
        weighted_av([10,20],[1,-1])