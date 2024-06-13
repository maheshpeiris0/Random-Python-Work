def number_division(number1, number2):
    try:
        result = number1 / number2
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except TypeError:
        print("You can't divide by a string!")
    else:
        print(result)
        
        