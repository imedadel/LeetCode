class Solution:
    def toLowerCase(self, string):
        """
        :type string: str
        :rtype: str
        """
        return "".join(chr(ord(c) + ord('a') - ord('A')) if 'A' <= c <= 'Z' else c for c in string)
