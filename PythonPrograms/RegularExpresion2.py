
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*%&#@{}"))

import re
def text_match(text):
    patterns ='ab*?'
    if re.search(patterns,text):
        return 'found a match'
    else:
        return ('not matched !')
print(text_match("cd"))
print(text_match("abc"))
print(text_match("abbc"))