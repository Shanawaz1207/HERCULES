class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=sorted(nums)
        L=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                L.append(i)
        return L
        