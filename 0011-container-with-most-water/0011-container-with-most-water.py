class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a=0
        b=len(height)-1
        m=0
        while a<b:
            h=min(height[a],height[b])
            c_area=h*(b-a)
            m=max(c_area,m)
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
        return m