class Solution:
    def subsetRecursion(self, i, nums, subset, result):
        
        if(i==len(nums)):
            result.append(list(subset))
            return

        subset.append(nums[i])
        self.subsetRecursion(i+1, nums, subset, result)

        subset.pop()
        self.subsetRecursion(i+1, nums, subset, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []

        self.subsetRecursion(0, nums, subset, result)

        return result
        