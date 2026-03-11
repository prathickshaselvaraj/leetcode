class Solution(object):
    def intersect(self, nums1, nums2):
        result = []

        for n in nums1:
            if n in nums2:
                result.append(n)
                nums2.remove(n)
                
        return result