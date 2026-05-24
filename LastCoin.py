class Solution:
    def coin(self, arr):
        n=len(arr)
        left=0 #start
        right=n-1 #stop
        while left < right:
            if arr[left]> arr[right]: #if num in left is greater than right
                left += 1 #move front
            else:
                right -=1 #or else move back from ending
        return arr[left]
