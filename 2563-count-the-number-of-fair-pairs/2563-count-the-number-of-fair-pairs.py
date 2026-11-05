class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans1 = 0

        while left < right:
            s = nums[left] + nums[right]

            if s <= upper:
                ans1 += right - left
                left += 1
            else:
                right -= 1

        left = 0
        right = len(nums) - 1
        ans2 = 0

        while left < right:
            s = nums[left] + nums[right]

            if s <= lower - 1:
                ans2 += right - left
                left += 1
            else:
                right -= 1

        return ans1 - ans2
