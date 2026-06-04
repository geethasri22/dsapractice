class Solution:
    def maxSubstring(self, s):
        # Transform: 0 -> +1, 1 -> -1
        arr = [1 if ch == '0' else -1 for ch in s]
        
        # Kadane's Algorithm
        max_sum = arr[0]
        curr_sum = arr[0]
        
        for i in range(1, len(arr)):
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_sum = max(max_sum, curr_sum)
        
        # If all 1s, result should be -1
        return -1 if max_sum < 0 else max_sum
