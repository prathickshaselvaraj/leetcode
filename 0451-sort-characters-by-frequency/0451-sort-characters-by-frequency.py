
from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
            
        return ''.join(c * f for c, f in Counter(s).most_common())