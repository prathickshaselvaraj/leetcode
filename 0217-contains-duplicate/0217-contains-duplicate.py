class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers=set()
        for i in nums:
            if i in numbers:
                return True
            else:
                numbers.add(i)
        return False
        