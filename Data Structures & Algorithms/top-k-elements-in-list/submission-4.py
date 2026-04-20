import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_array = [0 for i in range(2000)]
        n = len(nums)

        for i in range(len(nums)):

            if(nums[i]<=1000):
                temp = nums[i]
            else:
                temp = nums[i] + 2000

            freq_array[temp]+=1          

        heap = []

        for i in range(2000):
            if i<=1000:
                heapq.heappush(heap, (freq_array[i], i))
            else:
                heapq.heappush(heap, (freq_array[i], i-2000))
            
            if len(heap)>k:
                heapq.heappop(heap)
            
        answer = [value for freq, value in heap]

        return answer

        
