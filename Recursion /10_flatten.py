"""
Write a recursive function called flatten which 
accepts an array of arrays and returns a new array with all values flattened.
Examples
flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]
"""
def flatten(arr):
    if len(arr) == 0:
        return arr
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])

arr = [1,2,3,[4,5]]
print(flatten(arr))