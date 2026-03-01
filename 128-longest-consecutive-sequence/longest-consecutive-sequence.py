class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        n = len(nums)


        curr = 1 
        maxx = 1
        for i in range(1 , n):
            if nums[i] == nums[i-1]+1:
                curr +=1
                maxx = max(curr,maxx)
            else:
                curr = 1
        return maxx