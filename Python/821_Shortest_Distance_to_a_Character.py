class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans =  []
        
        prev = float("-inf")
        
        for i,char in enumerate(S):
            if char == C: prev = i
            ans.append(i - prev)
        
        prev = float("inf")
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)
        
        return ans
