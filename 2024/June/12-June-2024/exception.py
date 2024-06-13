def number_division(number1, number2):
    try:
        result = number1 / number2
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except TypeError:
        print("You can't divide by a string!")
    else:
        print(result)
        
number_division(10, 0)


def division(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except TypeError:
        print("You can't divide by a string!")
    else:
        return f"The result is {result}"
    finally:
        print("The function has been executed")
        
print(division(10, 0))
print(division(10, 2))
print(division(10, "2"))
print(division("10", 2))
print(division("10", "2"))
