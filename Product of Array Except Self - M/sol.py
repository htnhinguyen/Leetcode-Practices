class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)

        for i in range(1,len(nums)):
            l[i] = nums[i-1] * l[i-1]
        for i in range(len(nums)-2,-1,-1):
            r[i] = nums[i+1] * r[i+1]

        res= [1] * len(nums) 
        for i in range(len(nums)):
            res[i] = l[i] * r[i]
        return res
