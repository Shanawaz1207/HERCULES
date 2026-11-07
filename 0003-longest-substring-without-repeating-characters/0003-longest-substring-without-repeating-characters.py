class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l=0
        r=0
        L=[]
        k=""
        maxlen=0
        while r<len(s):
            if s[r] in k:
                l+=k.index(s[r])+1
                k=s[l:r+1]
                r+=1
            else:
                k+=s[r]
                r+=1
            maxlen=max(maxlen, len(k))
        return maxlen