class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            s=0
            nums=[int(x) for x in str(n)]
            for i in nums:
                s+=(i**2)
            n=s
        return True
            