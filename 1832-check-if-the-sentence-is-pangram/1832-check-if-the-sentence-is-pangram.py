class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence)<26:
            return False
        alphabets="abcdefghijklmnopqrstuvwxyz"
        for i in alphabets:
            if i not in sentence:
                return False
        return True