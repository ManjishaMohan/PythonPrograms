
'''Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
'''

import re
def match_string(text):
    character=re.compile(r'^[a-zA-Z0-9_]*$')
    text=character.search(text)
    return not bool(character)
print(match_string("This_is_a_number_125"))

import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))

import re
text = "my roll number is 25"
x = re.sub(r"\D","",text)
print(x)


import re

target_string = "Jessa salary is 8000$"

# compile regex pattern
# pattern to match any character
str_pattern = r"\w"
pattern = re.compile(str_pattern)
res = pattern.match(target_string)
# match character
print(res.group())
res = re.sub(r"\s", "-", target_string)
# string after replacement:
print(res)

