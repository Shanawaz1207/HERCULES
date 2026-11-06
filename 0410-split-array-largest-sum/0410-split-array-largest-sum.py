class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        def isValid(arr,n,m,mid):
            count=1
            pages=0
            for i in range(n):
                if pages+arr[i]<=mid:
                    pages+=arr[i]
                else:
                    pages=arr[i]
                    count+=1
            return count<=m
        st=max(nums)
        end=sum(nums)
        ans=-1
        while st<=end:
            mid=(st+end)//2
            if isValid(nums,n,k,mid):
                ans=mid
                end=mid-1
            else:
                st=mid+1
        return ans