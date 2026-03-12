class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        best=0
        for x in n:
            if x-1 not in n:
                c=x
                count=1
                while c+1 in n:
                    c+=1
                    count+=1
                best=max(count,best)
        return best
                

                
            


            