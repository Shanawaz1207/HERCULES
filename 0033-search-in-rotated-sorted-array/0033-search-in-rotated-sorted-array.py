class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        c=len(nums)+2
        for i in range(len(nums)):
            if nums[i]==target:
                c=i
        if c<len(nums):
            return c
        else:
            return -1