class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st={}
        ts={}
        for c1,c2 in zip(s,t):
            if c1 in st and st[c1]!=c2:
                return False
            if c2 in ts and ts[c2]!=c1:
                return False
            st[c1]=c2
            ts[c2]=c1
        return True