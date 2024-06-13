class CustomError(Exception):
    pass

class DivisionByNegativeError(CustomError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Division by a negative number: {value}")

def divide(a, b):
    if b < 0:
        raise DivisionByNegativeError(b)
    return a / b

try:
    result = divide(10, -2)
except DivisionByNegativeError as e:
    print(e)


    
    
    