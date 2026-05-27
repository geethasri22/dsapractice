class Solution:
    def wifiRange(self, s, x):
        # code here
        n = len(s)
        last_covered = -1
        for i in range(n):
            if s[i] == '1':
                if i-x > last_covered + 1:
                    return False
                last_covered = max(last_covered , i+x)
        return last_covered >= n-1
