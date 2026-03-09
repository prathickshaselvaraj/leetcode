class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a1=nums[:n]
        a2=nums[n:]
        s=-1
        for i in range(0,2*n,2):
            s+=1
            nums[i],nums[i+1]=a1[s],a2[s]
        return nums