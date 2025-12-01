class Solution:
    def check(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            nums.insert(0,nums[-1])
            del nums[-1]
            if nums == sorted(nums):
                return True
        return False