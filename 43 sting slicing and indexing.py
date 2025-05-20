# String Indexing & Slicing
# 1)Print the first character of a string.
# 2)Print the last character of a string.
# 3)Extract the first 5 characters of a string.
# 4)Extract the last 5 characters of a string.
# 5)Print every second character in a string.
# 6)Print a string in reverse order using slicing.
# 7)Extract a substring from a given string.
# 8)Swap the first and last character of a string.
# 9)Remove a specific character from a string.
# 10)Check if a string starts with a specific substring.

# 1)Print the first character of a string.
def print_first_char(s):
    newstr=""
    for char in range(len(s)):
        if char==0:
            newstr+=s[char]
            break
    return newstr
s="Akhin"
res=print_first_char(s)
print(res)    

# 2)Print the last character of a string.
def print_first_char(s):
    newstr=""
    for char in range(len(s)):
        if char==len(s)-1:
            newstr+=s[char]
            break
    return newstr
s="Akhil"
res=print_first_char(s)
print(res)    

# 3)Extract the first 5 characters of a string.
def print_first_five(s):
    nestr=''
    for i in range(5):
        if i<len(s):
            nestr+=s[i]
    return nestr
s="alakunta deepika"
res=print_first_five(s)
print(res)    

# 4)Extract the last 5 characters of a string.
def print_first_five(s):
    nestr=''
    n=len(s)
    for i in range(n-5,n):       
        if i>=0:
            nestr+=s[i]
    return nestr
s="alakunta deepika"
res=print_first_five(s)
print(res)      

# 6)Print a string in reverse order using slicing.
def reverse_slicing(s):
    newstr=""
    for i in range(len(s)-1,-1,-1):
        newstr+=s[i]
    return newstr
s="deepika"
res=reverse_slicing(s)
print(res)    

#  7)Extract a substring from a given string.
def extract_substring(s,start,end):
    newstr=""
    for i in range(start,end+1):
        if i<len(s):
            newstr+=s[i]
    return newstr
s="alakunta deepika"
start=2
end=7
res=extract_substring(s,start,end)   
print(res)         

# 8)Swap the first and last character of a string.
def swap_first_last(s):
    if len(s)<=1:
        return s
    newstr=""
    for i in range(len(s)):
        if i==0:
            newstr+=s[len(s)-1]
        elif i==len(s)-1:
            newstr+=s[0]
        else:
            newstr+=s[i]
    return newstr
s="deepika"
res=swap_first_last(s)
print(res)              

# 9)Remove a specific character from a string.
def remove_element(s,remove):
    newstr=""
    for char in s:
        if char!=remove:
            newstr+=char
    return newstr
s="deepika"
remove='p'
res=remove_element(s,remove)
print(res) 
# 10)Check if a string starts with a specific substring.   
def starts_with(s,sub):
    for i in range(len(sub)):
        if s[i]!=sub[i]:
            return False
    return True
s="hello world"
sub='hello'
res=starts_with(s,sub)
# print(res)
if res:
    print("it starts with specific substring")
else:
    print("no it does not startts with specific substing")    
                