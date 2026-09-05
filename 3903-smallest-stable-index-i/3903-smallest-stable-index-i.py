class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            in_sc=max(nums[0:i+1])-min(nums[i:n])
            if in_sc<=k:
                return i
        return -1
            
            
                