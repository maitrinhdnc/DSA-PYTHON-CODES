def reverse_string(strng):
    if len(strng) <= 0:
        return strng
    return strng[len(strng)-1] + reverse_string(strng[:len(strng)-1])

print(reverse_string('abc'))