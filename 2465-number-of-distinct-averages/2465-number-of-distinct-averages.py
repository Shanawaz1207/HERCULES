class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=len(nums)/2
        av=[]
        for i in range(s):
            m=min(nums)
            mx=max(nums)
            av.append((m+mx)/2.0)
            nums.remove(m)
            nums.remove(mx)
        return len(set(av))

        