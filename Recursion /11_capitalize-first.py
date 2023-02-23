def capitalizeFirst(arr):
    result = []
    result.append(arr[0].title())
    if len(arr) == 1:
        return result
    return result + capitalizeFirst(arr[1:])

arr = ['car', 'taco', 'banana']
print(capitalizeFirst(arr))