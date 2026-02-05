class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        res = [[0]*n for _ in range(m)]
        
        directions = [-1, 0, 1]
        
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                
                for di in directions:
                    for dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1
                
                res[i][j] = total // count
        
        return res