from content import Main


def test_sum():
    main = Main()
    result = main.sum(2,5)
    assert result == 7

def test_subtract():
    main = Main()
    result = main.subtract(44,7)
    assert result == 37

def test_multiple():
    main = Main()
    result = main.multiple(3,7)
    assert result == 21
