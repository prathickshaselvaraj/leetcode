class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = nums1 + nums2
        l.sort()
        n = len(l)
        if n % 2 == 0:
            median = (l[n//2] + l[(n//2) - 1]) / 2.0 
        else:
            median = float(l[n//2])  
        return median
        