
import re
text = "Use of python in machine learning"
x = re.findall("in",text)
print(x)

#search

import re
txt="python is one of the most popular langauge around the world"
searchObj= re.search("\s",txt)
print("the first white space character is located in position",searchObj)

import re
txt="python is one of the most popular langauge around the world"
searchObj= re.search("on",txt)
print(searchObj)

#split
import re
txt="python is one of the most popular langauge around the world"
searchObj= re.split("\s",txt)
print(searchObj)
#sub()
import re
txt="python is one of the most popular langauge around the world"
searchObj= re.sub("\s","_", txt)
print(searchObj)