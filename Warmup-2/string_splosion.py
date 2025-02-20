# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    n = ''
    for i in range(len(str)+1):
        n += str[:i] 
    return n
print(string_splosion('Computer'))