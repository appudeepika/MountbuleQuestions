# 1)Write a Python program to print a string.
# 2)Take a string input from the user and print it.
# 3)Find the length of a given string using Python.
# 4)Convert a string to uppercase and lowercase.
# 5)Check if a string contains only alphabets.
# 6)Check if a string contains only digits.
# 7)Remove leading and trailing spaces from a string.
# 8)Count the number of words in a string.
# 9)Reverse a given string.
# 10)Replace all occurrences of a character in a string.

# 2)Take a string input from the user and print it.
def string_input(str):
    newstr=""
    n=input("enter string:")
    newstr+=n
    print(newstr)
string_input(str)   
# # 3)Find the length of a given string using Python. 
def length_string(str):
    len=0
    for char in str:
        len+=1
    return len
str="hello world"
res=length_string(str)
print(res)      

# 4)Convert a string to uppercase and lowercase.
def upper_to_lower(str):
    res=""
    for i in str:
        ascii=ord(i)
        if (ascii>=65 and ascii<=90):
            newascii=ascii+32
            conchar=chr(newascii)
            res=res+conchar
    print(res)
str="DEEPIKA"
upper_to_lower(str)

# 5)Check if a string contains only alphabets.
def check_alphabets(str):
    for char in str:
        if not('A'<=char<='Z' or 'a'<=char<='z'):
            return False
    return True
str="helloworld"
res=check_alphabets(str)
if res:
    print("It contains alphabets")
else:
    print("it does not contains alphabets")        

# 6)Check if a string contains only digits.

def check_nmbrs(str):
    for char in str:
        if char<'0' or char>'9':
            return False
    return True
str="12345678"
res=check_nmbrs(str)
if res:
    print("it contain only didgits")
else:
    print("it does not contain digits")     

# 7)Remove leading and trailing spaces from a string.
def remove_spaces(s):
    newstr=""
    start,end=0,len(s)-1
    while start<=end and s[start]=='':
        start+=1
    while end>=start and s[end]=='':
        end-=1
    for i in range(start,end+1):
        newstr+=s[i]
    return newstr
s="   Alakunta Deepika  "
res=remove_spaces(s)
print(res)  

# 8)Count the number of words in a string.
def count_words(s):
    word_count=0
    in_word=False
    for char in s:
        if char!=' ':
            if not in_word:
                word_count+=1
                in_word=True
        else:
            in_word=False
    return word_count
s="hello world hi good afternoon"
res=count_words(s)
print(res)                

# 9)Reverse a given string    
def reverse(s):
    newstr=""
    for char in s:
        newstr=char+newstr
    return newstr 
s="deepika"
res=reverse(s)
print(res)   

# 10)Replace all occurrences of a character in a string.
def replace_characters(s,target,replace):
    nestr=" "
    for char in s:
        if char==target:
            nestr+=replace
        else:    
            nestr+=char
    return nestr
s="deepika"
target='e'
replace='$'
res=replace_characters(s,target,replace)
print(res)



           
