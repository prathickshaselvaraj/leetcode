class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        s=0
        for c in columnTitle:
            s=s*26 +(ord(c)-ord('A')+1)
        return s
