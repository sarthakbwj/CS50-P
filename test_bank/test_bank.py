from bank import value

def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()

def test_return_zero():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_return_twenty():
    assert value("Hi") == 20
    assert value("hey") == 20

def test_return_hundred():    
    assert value("Good Morning") == 100
    assert value("Moin!") == 100 

if __name__ == "__main__":
    main()