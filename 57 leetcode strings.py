# length of last word
s="   fly me   to   the moon  "
n=len(s)
current_len=0
i=n-1
while i>0 and s[i]==" ":
    i-=1
while i>0 and s[i]!=" ":
    current_len+=1
    i-=1
print(current_len)   

s="abcd"
for i,char in enumerate(s):
    print(i,char)

# max differenece between even and odd frequency
s= "aaaaabbc"
dict={}
for char in s:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1
odd_count=[]
even_count=[]
for i in  dict.values():
    if i%2==0:
        even_count.append(i)
    else:
        odd_count.append(i)  
max_dif=float("-inf")
for odd in odd_count:
    for even in even_count:
        max_dif=max(max_dif,odd-even)          
print(max_dif)    

# FINA AVALID [AIR OF ADJACENT DIGITS IN A STRING]
  def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a != b and freq[a] == int(a) and freq[b] == int(b):
                return a + b
        
        return ""
# check balancing strings

s="24123"
odd_sum=0
even_sum=0
for i in range(0,len(s),2):
    odd_sum+=int(s[i])
for i in range(1,len(s),2):
    even_sum+=int(s[i])    
if odd_sum==even_sum:
    print("True")
else:
    print("False")

# LONGEST COMMON PREFIX
str=["flower","flow","flight"]
prefix=str[0]
for s in str[1:]:
    while not s.startswith(prefix):
        prefix=prefix[:-1]
        if not prefix:
            print("")
print(prefix)

# FIZZBUZZ problem
n=5
res=[]
for i in range(1,n+1):
    if i%3==0 and i%5==0:    
        res.append("FizzBuzz")   
    elif i%3==0:
        res.append("Fizz")
    elif i%5==0:
        res.append("Buzz")
    else:
        res.append(str(i))
print(res)                       

# Get string of first and last 2 chars.
str="resources"
if len(str)<2:
    print("empty strinf")
print(str[0:2]+str[-2:])    

# Replace first char occurrences with $
s="resource"
first_chr=s[0]
res=s[1:].replace(first_chr,"$")
print(first_chr,res)  

# Swap first 2 chars of 2 strings.
str1="abc"
str2="xyz"
res1=str2[:2]+str1[2:]
res2=str1[:2]+str2[2:]
print(res1,",",res2)

# longest word in a string
str="python is fun"
res=str.split()
new_res=""
for word in res:
    if len(word)>len(new_res):
        new_res=word
print(new_res) 

# swap first and last ch
str="deepika"
count=0
for ch in str:
    count+=1
new_str=""
for i in range(count):
    if i==0:
        new_str+=str[count-1]
    elif i==count-1:
        new_str+=str[0]
    else:
        new_str+=str[i]  
print(new_str)     
# Remove the characters which have odd index values of a given string
str="abcdef"
new_str=""
for i in range(len(str)):
    if i%2!=0:
        print(str[i],end=" ")  

# Count word occurrences in a sentence.
str="the quick brown fox jumps over the lazy dog"
res=str.split()
dict={}
for i in res:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)                                 

# REplace the character
s = 'abracadabra' 
position=5
character='k'
index=0
res=""
for ch in s:
    if index==position:
        res+=character
    else:
        res+=ch
    index+=1
print(res)            
