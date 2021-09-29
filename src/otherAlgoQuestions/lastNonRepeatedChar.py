# Find the last non-repeated character in a given string
#
# Input: My Name is Ajay
# Output: j

from collections import OrderedDict

def searchLastNonRepeatedChar(string: str) -> str:
    if string is None or len(string) == 0: return
    if len(string) == 1: return string

    characters = OrderedDict()

    for ch in string:
        if ch in characters.keys(): characters[ch] += 1
        else: characters[ch] = 1
    
    return list(characters.keys())[-1]


string: str = "My name is Ajay"
print(f"the last non-repeating character in the string {string} is {searchLastNonRepeatedChar(string)}")