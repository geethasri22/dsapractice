#leetcode2114: word count in a given sentence

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for s in sentences:
            word = len(s.split())
            if word > max_words:
                max_words = word
                
        return max_words
        
