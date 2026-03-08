class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        point=(0,0)
        dic={
            "U":(0,1),
            "D":(0,-1),
            "R":(1,0),
            "L":(-1,0)
        }
        for i in moves:
            x,y=point
            dx,dy=dic[i]
            point=(x + dx, y + dy)
        return point==(0,0)
