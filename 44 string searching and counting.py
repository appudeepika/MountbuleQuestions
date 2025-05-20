# String Searching & Counting
# 1)Count the number of vowels in a string.
# 2)Count the number of consonants in a string.
# 3)Find the index of a given character in a string.
# 4)Find the number of occurrences of a substring in a string.
# 5)Check if a string is a palindrome.
# 6)Check if two strings are anagrams.
# 7)Find the first non-repeating character in a string.
# 8)Find the most frequent character in a string.
# 9)Find the last occurrence of a character in a string.
# 10)Check if a string ends with a specific substring.

# 1)Count the number of vowels in a string.
def count_vowels(s):
    count=0
    for char in s:
        if char in "AEIOUaeiou":
            count+=1
    return count
s="deepika"
res=count_vowels(s)
print(res)         

# 2)Count the number of consonants in a string.       
def count_Consonants(s):
    count=0
    for char in s:
        if char not in "AEIOUaeiou":
            count+=1
    return count
s="deepika"
res=count_Consonants(s)
print(res)         
                 
# 3)Find the index of a given character in a string. 
def find_index(s,character):
    index=0
    for i in range(len(s)):
        if s[i]==character:
            return i
    return -1
s="deepika"
character='p'
res=find_index(s,character)
print(res)        

# 4)Find the number of occurrences of a substring in a string.                        