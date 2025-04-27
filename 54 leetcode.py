# min difference between highest and lowest b scores(leetcode)
nums=[3,4,8,1,5]
nums.sort()
n=len(nums)
k=3
ans=float("inf")
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(nums[k])
        if len(temp)==k:
            last=temp[-1]
            first=temp[0]
            ans=min(ans,last-first)
print(ans)            

# or
nums=[3,4,8,1,5]
nums.sort()
n=len(nums)
l=0
k=3
ans=float("inf")
for r in range(n):
    if (r-l==k):
        l+=1
    if(r-l+1==k): 
        ans=min(ans,nums[r]-nums[l])
print(ans)         

# minimum cost of buying candies and getting discount
nums=[2,2,5,6,7,9]
nums.sort()
took=0
ans=0
for i in range(len(nums)-1,-1,-1):
    if took==2:
        took=0
    else:
        ans+=nums[i]
        took+=1
print(ans)         
# roman number to number
s = "MCMXCIV"
count=0
dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in s:
    if i in dict:
        temp=(f"{i}->{dict[i]}")
        count+=dict[i]
print(count)        
      
# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold     
def array(arr,k,threshold):
    n=len(arr)
    ans=0
    for i in range(n):
        for j in range(i,n):
            temp=[]
            sum=0
            for h in range(i,j+1):
                temp.append(arr[h])
                sum+=arr[h]
            if len(temp)==k:
                avg=sum/k
                if avg>=threshold:
                    ans+=1
    return ans                    
arr = [2,2,2,2,5,5,5,8]
threshold=4
k=3  
res=array(arr,k,threshold)
print(res)


arr = [2,2,2,2,5,5,5,8]
n=len(arr)
l=0
threshold=4
temp=0
k=3  
res=0
for r in range(n):
    temp+=(arr[r])
    if(r-l==k):
        temp-=arr[l]
        l+=1
    if (r-l+1)==k:
        if (temp/k)>=threshold:
            res+=1
print(res)


# finr the max length of the subarray which has atmost k ones k=2
arr=[0,1,3,1,1,6,7,1,0,1]
n=len(arr)
k=2
l=0
temp=0
ans=0
for r in range(n):
    if(arr[r]==1):
        temp+=1
    while temp>k:
        if(arr[l]==1):
            temp-=1
        l+=1    
    ans=max(ans,r-l+1)
print(ans)      

# return the max no of consecutive 1's in the array if you can flip at most k 0's
arr=[1,1,1,0,0,0,1,1,1,1,0]
n=len(arr)
k=2
l=0
temp=0
ans=0
for r in range(n):
    if arr[r]==0:
        temp+=1
    while temp>k:
        if arr[l]==0:
            temp-=1
        l+=1    
    ans=max(ans,r-l+1)
print(ans)        

# Contains duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1 
        found_duplicates=False              
        for i in d:
            if d[i]>1:
                return True
                found_duplicates=True
                break
        if not found_duplicates:
            return False
                
# or

nums=[1,2,3,1]
seen=set()
for i in nums:
    if i in seen:
        print("true")
    seen.add(i)
print("false")   

# duplicates
nums=[1,2,3,1,2,3]
n=len(nums)
k=2
found=False
for i in range(n):
    for j in range(i+1,n):
        if nums[i]==nums[j] and abs(i-j)<=k:
            print("true")
            found= True 
            break
if not found:
        print("false")
# move all zeros th the end
nums=[0,1,0,3,12]
n=len(nums)
non_zeros=[]
zeros=[]
for i in range(n):
    if nums[i]!=0:
        non_zeros+=[nums[i]]
    else:
        zeros+=[nums[i]]
print(non_zeros+zeros)   

# Remove nth character from a string.
str=input("enter string")
n=int(input("enter the i ndex"))
first_part=str[:n]
second_part=str[n+1:]
print(first_part+second_part)

# upper to lower
str="DEEPIKAdeepika"
res=""
for ch in str:
    if 'A'<=ch<='Z':
        lowe=chr(ord(ch)+32) 
        res+=lowe
    else:
        res+=ch   
print(res)        


width=20
print('deepika'.ljust(width,'-'))
