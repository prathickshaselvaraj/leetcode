class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        rank = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for idx, friend in enumerate(preferences[i]):
                rank[i][friend] = idx
        
        partner = [0]*n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x
        
        unhappy = 0
        
        for x in range(n):
            y = partner[x]
            
            for u in preferences[x]:
                if u == y:
                    break
                
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break
        
        return unhappy