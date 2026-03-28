class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique = len(set(candyType))
        return min(unique, len(candyType) // 2)