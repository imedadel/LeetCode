class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        D = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col)-1)): D += 1
        return D
