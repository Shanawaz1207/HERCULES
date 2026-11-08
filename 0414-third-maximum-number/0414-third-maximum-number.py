class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        s=sorted(s,reverse=True)
        if len(s)==2:
            return s[0]
        if len(s)==1:
            return s[0]
        elif len(s)>2:
            return s[2]