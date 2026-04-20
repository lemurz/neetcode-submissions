class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):
            check = target - nums[i]

            if check in map:
                output = [i, map[check]]
                break

            map[nums[i]] = i

        output.sort()
        return output
        
