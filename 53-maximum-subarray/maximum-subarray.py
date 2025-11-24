class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, total= nums[0],nums[0]
        for i in range(1,len(nums)):
            if total < 0 and i >0:
                total = 0

            total = total + nums[i]
            if res < total:
                res = total
        return res
        