from main import add


def test_add():
    assert add(3, 10) == 13
    assert add(3, 2) == 5
    assert add(5, 6) == 11


if __name__ == "__main__":
    test_add()
