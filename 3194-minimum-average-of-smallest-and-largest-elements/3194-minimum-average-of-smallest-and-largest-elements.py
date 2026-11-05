class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        av=[]
        s=len(nums)/2
        for i in range(s):
            m=min(nums)
            mx=max(nums)
            nums.remove(m)
            nums.remove(mx)
            av.append((m+mx)/2.0)
        return min(av)
        