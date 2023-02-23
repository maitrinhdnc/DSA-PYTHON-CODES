"""
Write a recursive function called capitalizeWords.
Given an array of words, return a new array containing each word capitalized.
Examples
words = ['i', 'am', 'learning', 'recursion']
capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']
"""
def capitalizeWords(arr):
    result = []
    result.append(arr[0].upper()) 
    if len(arr) == 1:
        return result
    return result + capitalizeWords(arr[1:])

arr = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(arr))