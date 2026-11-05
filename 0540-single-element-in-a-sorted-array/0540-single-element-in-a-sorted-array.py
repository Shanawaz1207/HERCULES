class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            if len(nums)==1:
                return nums[0]
            mid=(left+right)//2
            if mid==0 and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid==len(nums)-1 and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==0:
                if nums[mid-1]==nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid-1]==nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        
        

        