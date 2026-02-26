class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, i = [], 0
    
        while i < len(words):
            j, line_len = i, 0
            
            # collect words for one line
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            
            gaps = j - i - 1
            line = ""
            
            # last line OR single word → left justify
            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = (maxWidth - line_len) // gaps
                extra = (maxWidth - line_len) % gaps
                
                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (spaces + (k < extra))
                
                line += words[j - 1]
            
            res.append(line)
            i = j
        
        return res