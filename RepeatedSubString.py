class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        double = s+s #concate itself
        trimmed = double[1:-1] #remove first and last 
        return s in trimmed
