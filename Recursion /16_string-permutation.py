def string_permutation(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for i,let in enumerate(s):
            for perm in string_permutation(s[:i] + s[i+1:]):
                out += [let + perm]
    return out

s = 'abcd'
print(string_permutation(s))