"""
Write a recursive function called isPalindrome which returns 
true if the string passed to it is a palindrome (reads the same forward and backward). 
Otherwise it returns false.
Examples
isPalindrome('awesome') # false
isPalindrome('foobar') # false
isPalindrome('tacocat') # true
"""
def isPalindrome(strng):
    if len(strng) == 0:
        return True
    return strng[0] == strng[-1] and isPalindrome(strng[1:-1])

strng = 'abccba'
print(isPalindrome(strng))