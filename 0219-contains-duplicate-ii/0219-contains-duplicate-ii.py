class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last={}
        for i in range(len(nums)):
            if nums[i] in last and i-last[nums[i]]<=k:
                return True
            last[nums[i]]=i
        return False




        