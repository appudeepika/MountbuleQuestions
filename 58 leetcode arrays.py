# two sum problem
nums=[2,7,11,15]
target=9
n=len(nums)
res=[]
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            res=[i,j]
            break
print(res)        

# Serch insert position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
#return one 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits              
# single number
nums=[4,1,2,1,2]
dict={}
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for i in dict:
    if dict[i]==1:
        print(i)    

# find all numbers disappeared in an array
nums=[1,1]
n=len(nums)
temp=[]
for i in range(1,n+1):
    if i not in nums:
        temp.append(i)
print(temp)

# next generation element
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for num in nums1:
            found=False
            for i in range(len(nums2)):
                if nums2[i]==num:
                    for j in range(i+1,len(nums2)):
                        if nums2[j]>num:
                            res.append(nums2[j])
                            found=True
                            break
                    if not found:
                        res.append(-1)
                    break
        return res   
                













# median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        if n%2==1:
            return float(merged[n//2])
        else:
            mid1=merged[n//2-1]
            mid2=merged[n//2]
            return (mid1+mid2)/2.0
