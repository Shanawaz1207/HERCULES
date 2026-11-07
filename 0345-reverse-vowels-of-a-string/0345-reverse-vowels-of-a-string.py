class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        chars=list(s)
        right=len(s)-1
        while left<right:
            if chars[left].lower() not in "aeiou" or chars[left].isalnum()==False:
                left+=1
            elif chars[right].lower() not in "aeiou" or chars[right].isalnum()==False:
                right-=1
            else:
                chars[left],chars[right]=chars[right],chars[left]
                left+=1
                right-=1
        return "".join(chars)

        