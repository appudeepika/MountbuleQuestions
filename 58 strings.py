# string concatenate
a="b"
print(ord(a))
print(ord('a'))

# REVERSE DEGREE OF A STRING
s="abc"
n=len(s)
res=0
for i in range(n):
    res_ind=26-(ord(s[i])-ord('a'))
    res+=res_ind*(i+1)
print(res)    
# check if digits are equal in string after operations
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            new_str=""
            for i in range(len(s)-1):
                a=int(s[i])
                b=int(s[i+1])
                c=(a+b)%10
                new_str+=str(c)
            s=new_str
        return s[0]==s[1]   
        