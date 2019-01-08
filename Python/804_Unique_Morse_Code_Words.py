class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        
        for word in words:
            enWord = ""
            for c in word:
                enWord += MORSE[ord(c) - ord("a")]
            trans.add(enWord)
        return len(trans)
