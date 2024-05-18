from add_number import add_number

def test_add_positive_numbers():
    assert add_number(1,2) == 3

def test_add_negative_numbers():
    assert add_number(-1,-2) == -3
    
def test_add_positive_negative_numbers():
    assert add_number(1,-2) == -1