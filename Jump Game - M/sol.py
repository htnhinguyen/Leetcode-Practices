class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 2
        j = n - 1
        
        while i >= 0:
            if nums[i] + i >= j:
                j = i
            i -= 1
        return j == 0
