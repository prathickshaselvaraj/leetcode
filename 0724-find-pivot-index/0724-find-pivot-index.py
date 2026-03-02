class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            rs=0 if i==0 else sum(nums[:i])
            ls=0 if i==n-1 else sum(nums[i+1:])
            if rs==ls:
                return i
            else:
                continue
        return -1