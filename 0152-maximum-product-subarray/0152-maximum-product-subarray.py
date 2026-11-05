class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=1
        maxp=max(nums)
        for i in range(0,len(nums)):
            product=product*nums[i]
            maxp=max(maxp,product)
            
            if product==0:
                product=1
        product=1
        for num in reversed(nums):
            product=product*num
            maxp=max(maxp,product)
            
            if product==0:
                product=1
        return maxp