def count_vowels(str):
    count=0
    for i in str:
        if i in "aeiouAEIOU":
            count+=1
    print(f"the number of vowels present in str are {count}")
str=input("enter the string:")
count_vowels(str)

# replace the vowel with other alphabet
def replace_vowel(str,rep):
    res=""
    for i in str:
        if i in "aeiouAEIOU":
            res=res+rep
        else:
            res=res+i
    print(res)
str=input("enter string:") 
rep=input("enter replace string:") 
replace_vowel(str,rep) 