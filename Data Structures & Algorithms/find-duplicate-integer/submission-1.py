class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return []
        
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]