class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(-x)[::-1])
    
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
        