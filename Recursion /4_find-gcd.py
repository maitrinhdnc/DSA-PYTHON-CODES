# How to find GCD (Greatest Common Divisor) of two numbers
def find_gcd1(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 >= n2:
        return find_gcd1(n1-n2, n2)
    else:
        return find_gcd1(n1, n2-n1)
"""
Time complexity: O(log(min(a,b))), as it uses the Euclidean algorithm 
which has a time complexity of O(log(min(a,b))). 
Auxiliary Space: O(1), as it only uses a few variables 
and does not require any additional data structures.
"""

def find_gcd(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, 'The number must be integer'
    if n1 < 0:
        n1 = -1 * n1
    if n2 < 0:
        n2 = -1 * n2
    if n2 == 0:
        return n1
    else:
        return find_gcd(n2, n1%n2)
 

print(find_gcd(98,56))

"""
Time complexity:  O(log(min(a,b))), 
as it uses the Euclidean Algorithm for finding the GCD.
Auxiliary Space: O(log(n)), 
as it uses recursion and the maximum depth of recursion is log(n).
"""