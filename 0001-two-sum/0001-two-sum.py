class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        v={}
        for i,num in enumerate(nums):
            s=target-num
            if s in v:
                return [v[s],i]
            v[num]=i
        return []