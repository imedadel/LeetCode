class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low,high = 0,len(S)
        out = []
        
        for c in S:
            if c == "I":
                out.append(low)
                low += 1
            else:
                out.append(high)
                high -= 1
        out.append(low)
        return out
