# Problem: How to calculate power of  a number using recursion 

def power(number, times):
    assert number >= 1 and int(times)==times,'The number must be larger than 0 and times must be integer only'
    if times == 0:
        return 1
    elif times < 0:
        return 1/number * power(number, times+1)
    return number * power(number, times-1)

print(power(3,-2))