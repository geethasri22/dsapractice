class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        
        # Trick: s can be rotated into goal if goal is a substring of s+s
        return goal in (s + s)
        
