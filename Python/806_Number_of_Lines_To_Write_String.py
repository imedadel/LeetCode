class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines, width = 1, 0
        
        for c in S:
            w = widths[ord(c) - ord("a")]
            width += w
            if width > 100:
                lines += 1
                width = w
        return [lines, width]
