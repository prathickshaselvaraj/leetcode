class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for k in count:
            if count[k] == 1:
                return k
        