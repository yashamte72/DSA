class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i == 0:
                count = 0
            else:
                count +=1
            if res < count:
                res = count
        return res