# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    cat_word = False
    dog_word = False
    dog_count = 0
    cat_count = 0
    if str == '':
        return True
    
    for i in range(len(str)-2):
        if (str[i:i+3]) == 'cat':
            cat_count += 1
            cat_word = True
                
        if (str[i:i+3]) == 'dog':
            dog_count += 1
            dog_word = True
                

    if cat_word == True and dog_word == True and cat_count == dog_count:
        return True
    else:
        return False
print(cat_dog('dogdogcat'))