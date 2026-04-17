from app import soma, sub, mult, div

def test_soma():
    assert soma(2,3) == 5

def test_sub():
    assert sub(5,2) == 3

def test_mult():
    assert mult(2,4) == 8

def test_div():
    assert div(10,2) == 5

def test_soma_negativo():
    assert soma(-1,1) == 0