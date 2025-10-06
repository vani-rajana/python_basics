# to print the index values, where we reach the target value.
nums=[3,4,5,6]
T=7
for i in range(len(nums)):
    res=nums[i]+nums[i+1]
    if res==T:
        print(i,i+1)
        break