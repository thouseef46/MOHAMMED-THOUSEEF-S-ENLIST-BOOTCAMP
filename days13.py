import re
def is_allowed_specific_char(string):
    charRe=re.compile(r'[^a-z,A-Z,0-9]')
    string=charRe.search(string)
    return not bool(string)
print (is_allowed_specific_char("ABCDEFabcdf123459"))
print( is_allowed_specific_char("122345@#$$%"))

#-------
def text_match(text):
    patterns='\w*ab./w*'
    if re.search(patterns,text):
          return 'found'
    else:
          return 'not found'
    print(text_match("puyhionik"))
    print(text_match("ababababab"))

#--------
def end_num(string):
    text=re.compile(r".*[0-9]$")
    if text_match(string):
        return True
    else:
        return False
print(end_num('asfftyf33455'))
print(end_num('fdsdfdfd'))

#-----
length=re.finditer(r'.*[0-9]{1,3}','exercise num 1,9,11,ans 222 are important')
print("number 1 to 3")
for n in length:
     print(n.group(0))

#-------
def text_match(text):
    patterns ='^[a-z,A-Z0-9_]*$'
    if re.search(patterns,text):
        return  ' found'
    else:
        return  'not found'

print(text_match("tytytuytuytu"))
print(text_match("DYTFFFHGFGHF"))
     

