class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if word[0].isupper()==True and word[1:].islower()==True:
            return True
        elif word.isupper()==True:
            return True
        elif word.islower()==True:
            return True
        return False