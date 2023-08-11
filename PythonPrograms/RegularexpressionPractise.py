
'''Given a string like :
2004-959-559

Please write the regular expression to fetch only the numbers from the above string'''

import re
t="2004-959-596"
searchObj= re.sub("-","", t) # first method by using sub function
print(searchObj)

import re
t="2004-959-596"
searchObj= re.sub(r"\D","",t) # second method by using \D - it will consider only digit
print(searchObj)


# new string - t="2004-959-559 # This is Phone Number"
import re
t="2004-959-559 # This is Phone Number"
searchObj= re.sub("-","", t)
print(searchObj)


import re
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print( "Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num)
