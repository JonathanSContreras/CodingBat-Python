# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
# Note: s.lower() returns the lowercase version of a string.
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
def end_other(a, b):
    numa = len(a)
    numb = len(b)
    b = b.lower()
    a = a.lower()
    if a[:numb] == b:
        return True
    elif b[:numb] == a:
        return True
    if a[-numb:] == b:
        return True
    if b[-numa:] == a:
        return True
    else:
        return False
print(end_other('abc','abXabc'))