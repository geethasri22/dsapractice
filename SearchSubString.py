class Solution:
    def search(self, a, b):
        
        if not b:
            return []
        n , m = len(a),len(b)
        result = []
        for i in range(n-m+1):
            if a[i:i+m] == b:
                result.append(i)
        return result
        
