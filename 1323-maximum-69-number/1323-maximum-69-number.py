class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=str(num)
        s=nums.replace('6','9',1)    
        return int(s)