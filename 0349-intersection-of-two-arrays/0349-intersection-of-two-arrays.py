class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        s=set(nums1)
        for i in nums2:
            if i in s:
                res.append(i)
        return list(set(res))