class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "QWERTYUIOP"
        second = "ASDFGHJKL"
        third = "ZXCVBNM"
        ans = []
        
        for word in words:
            if all(c.upper() in first for c in set(word)) or all(c.upper() in second for c in set(word)) or all(c.upper() in third for c in set(word)):
                ans.append(word)
        return ans
