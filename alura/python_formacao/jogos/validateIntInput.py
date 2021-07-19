
def validateIntInput(msg, minValue, maxValue, errorMsg):
    value = int(input(msg))
    while(value < minValue or value > maxValue):
        value = int(input(errorMsg))
    return value
