from day01 import cofre

def test_passa_100_3_vezes_para_no_0():
    resultado, n0 = cofre(90, 'R310')
    assert resultado == 0
    assert n0 == 4

def test_passa_100_20_vez():
    resultado, n0 = cofre(90, 'R1933')
    assert resultado == 23
    assert n0 == 20

def test_passa_100_2_vez():
    resultado, n0 = cofre(90, 'R133')
    assert resultado == 23
    assert n0 == 2

def test_passa_100_1_vez():
    resultado, n0 = cofre(90, 'R33')
    assert resultado == 23
    assert n0 == 1

def test_passa_0_20_vez():
    resultado, n0 = cofre(10, 'L1933')
    assert resultado == 77
    assert n0 == 20

def test_passa_0_2_vez():
    resultado, n0 = cofre(10, 'L133')
    assert resultado == 77
    assert n0 == 2

def test_passa_0_1_vez():
    resultado, n0 = cofre(10, 'L33')
    assert resultado == 77
    assert n0 == 1

def test_para_no_0():
    resultado, n0 = cofre(20, 'L20')
    assert resultado == 0
    assert n0 == 1

def test_para_no_100():
    resultado, n0 = cofre(80, 'R20')
    assert resultado == 0
    assert n0 == 1

def test_passa_100_para_no_0():
    resultado, n0 = cofre(99, 'R101')
    assert resultado == 0
    assert n0 == 2

def test_passa_0_para_no_0():
    resultado, n0 = cofre(8, 'L108')
    assert resultado == 0
    assert n0 == 2