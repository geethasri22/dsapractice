class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = sorted(nums1 + nums2)
        n = len(m) #length of the list after merging the sorting arrays
        if n % 2 == 1:  #if the list contains odd no of numbers
            return float(m[n // 2])
        else:  # even length
            mid1, mid2 = m[n // 2 - 1], m[n // 2]
            return (mid1 + mid2) / 2.0
