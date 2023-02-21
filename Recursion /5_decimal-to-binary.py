# How to convert a number from Decimal to Binary 
def dec_to_bin(number):
    if number == 0:
        return 0
    return number % 2 + 10*  dec_to_bin(number//2)
print(dec_to_bin(10))