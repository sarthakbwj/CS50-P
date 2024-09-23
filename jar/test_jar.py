from jar import Jar

def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity initialization
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    # Test invalid capacity (should raise ValueError)
    try:
        Jar(-1)
    except ValueError:
        assert True
    else:
        assert False


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    # Test deposit over capacity (should raise ValueError)
    try:
        jar.deposit(8)
    except ValueError:
        assert True
    else:
        assert False

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

    # Test withdraw more than size (should raise ValueError)
    try:
        jar.withdraw(6)
    except ValueError:
        assert True
    else:
        assert False
