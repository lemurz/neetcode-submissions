class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        n = len(nums)

        for i in range(n-2):

            if i>0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=n-1
            target = -nums[i]

            while(j<k):
                if nums[j]+nums[k] < target:
                    j+=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    ans = list([nums[i], nums[j], nums[k]])
                    res.append(ans)
                    j+=1

                    while nums[j]==nums[j-1] and j<k:
                        j+=1               
            
        return res
            
                

