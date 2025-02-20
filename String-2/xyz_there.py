# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
# So "xxyz" counts but "x.xyz" does not.
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    
    if 'xyz' in str:
        for i in range(len(str) + 5):
            if str[i] == 'x' and str[i+1] == '.':
                return False
            elif str[i] == 'x' and str[i-1] == '.':
                
                return False
        return True
    else:
        return False
print(xyz_there('abc.xyz'))