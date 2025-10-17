def same_chars (s, n1, n2):
    if n1 >= len(s) or n2 >= len(s):
        return False
    elif s[n1] == s[n2]:
        return True
    else: return False

print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False