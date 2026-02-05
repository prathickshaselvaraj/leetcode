class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        u=set()
        l=0
        m=0
        for i in range(len(s)):
            while s[i] in u:
                u.remove(s[l])
                l+=1
            u.add(s[i])
            m=max(m,i-l+1)
        return m


            