class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        r1=set("qwertyuiop")
        r2=set("assdfghjkl")
        r3=set("zxcvbnm")

        for word in words:
            w=set(word.lower())
            if w.issubset(r1) or w.issubset(r2) or w.issubset(r3):
                res.append(word)
        return res 
