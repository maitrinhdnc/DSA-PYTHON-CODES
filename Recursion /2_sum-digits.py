# Problem: how to find the sum of digits of a positive integer number using recursion
def sum_digits(number):
    assert number>=0 and int(number) == number,'The number has to be a positive integer only'
    if number == 0:
        return 0
    else:   
        return number%10 + sum_digits(number//10)
print(sum_digits(-1))