class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        c=0
        L=[0]
        for i in gain:
            c+=i
            L.append(c)
        return max(L)
        