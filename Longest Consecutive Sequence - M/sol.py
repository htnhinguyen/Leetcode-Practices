class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums.sort()
        count = 1
        biggest = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else: 
                biggest = max(count, biggest)
                count = 1
        return max(count, biggest)
        
