class Solution:
    def backtrack(self, i, curr, total, result, target, nums):
        if total == target:
            result.append(curr.copy())
            return
        if i >= len(nums) or total > target:
            return
        
        curr.append(nums[i])
        self.backtrack(i, curr, total + nums[i], result, target, nums)

        curr.pop()
        self.backtrack(i+1, curr, total, result, target, nums)

    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        self.backtrack(0, [], 0, result, target, nums)
        return result