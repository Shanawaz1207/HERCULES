class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxone,s=0,0
        for r in range(len(nums)):
            if nums[r]==1:
                s+=1
                maxone=max(maxone,s)
            else:
                s=0
        return maxone
        