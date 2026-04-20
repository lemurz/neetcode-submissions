import numpy as np

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        store = np.zeros(100000)

        for i in range(n):
            store[nums[i]]+=1

            if(store[nums[i]])>1:
                return True
        
        return False
        
