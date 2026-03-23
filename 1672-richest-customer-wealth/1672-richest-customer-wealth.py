class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=len(accounts)
        n=len(accounts[0])
        res=0
        for i in range(m):
            c=0
            j=0
            while j<n:
                c+=accounts[i][j]
                j+=1
            res=max(res,c)
        return res