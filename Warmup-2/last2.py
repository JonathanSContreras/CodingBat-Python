# Given a string, return the count of the number of times that a substring length 2 
# appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
    count = 0
    if str == '':
        return 0
    if str[0:2] == str[-2:]:
        count -= 1
    
    for i in range(len(str)+1):
        if str[1:3] == str[i:i+2]:
            count += 1

    if str[i:i+2] == str[-2:]:
        count -= 1 
    return count

print(last2('xaxxaxaxx'))