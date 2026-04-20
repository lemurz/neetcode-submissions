class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while(i<j):
            check = numbers[i] + numbers[j]

            if check > target:
                j-=1

            if check < target:
                i+=1
            
            if check==target:
                out = [i+1, j+1]
                break
            
        return out
        