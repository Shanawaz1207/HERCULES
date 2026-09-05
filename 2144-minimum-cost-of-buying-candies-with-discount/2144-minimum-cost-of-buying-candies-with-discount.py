class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        tc=0
        for i in range(len(cost)):
            if (i+1)%3!=0:
                tc+=cost[i]
        return tc
        