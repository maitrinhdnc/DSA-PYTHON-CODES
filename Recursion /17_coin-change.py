# Given a target amount n and a list of distinct coin values, what's the fewest coins needed
# to make the change amount
import sys, time
def rec_coin(target, coins):
    coins.sort()
    result = 0
    if target in coins:
        return 1
    for i in coins:
        temp = target
        if i < target:
            temp = temp // i
            mod = target % i
            while temp:
                if mod == 0:
                    result = temp
                    break
                else:
                    result = temp + rec_coin(target-temp*i, coins[:i])
                    break
    return  result

def rec_coin1(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
        return min_coins

   
coins = [1,2,5,10]
target = 128222
start = time.time()
print(rec_coin(target, coins))
print(sys.getsizeof(rec_coin(target, coins),'byte'))
print(rec_coin1(target, coins))
print(sys.getsizeof(rec_coin1(target, coins),'byte'))


