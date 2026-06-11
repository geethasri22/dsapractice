class Solution:
    def findIndex(self, s):
        open = 0
        close = s.count(')')
        
        for i in range(len(s) + 1):
            if open == close:
                return i
            if i < len(s):
                if s[i] == '(':
                    open += 1
                else:
                    close -= 1
        return -1
