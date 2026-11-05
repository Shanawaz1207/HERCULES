class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        c=0
        for i in range(len(nums)):
            if nums[i]==target:
                c+=1
        if c==0:
            return False
        else:
            return True