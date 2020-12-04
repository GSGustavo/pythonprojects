def fact(value):
    if value == 0 or value == 1:
        return 1
    else:
        return value * fact(value - 1)

number = int(input('Insert a number: '))
print(fact(number))
