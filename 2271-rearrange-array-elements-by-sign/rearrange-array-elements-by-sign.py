class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        n = len(nums)
        arr = []

        for i in range(n):
            if nums[i] > 0:
                arr.insert(pos,nums[i])
                pos +=2
            elif nums[i] < 0:
                arr.insert(neg,nums[i])
                neg +=2
        return arr
                
            