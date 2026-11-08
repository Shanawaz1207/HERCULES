class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        else:
            nums=sorted(nums)
            maxgap=0
            
            for i in range(1,len(nums)):
                
                maxgap=max(nums[i]-nums[i-1],maxgap)
                
            return maxgap

        