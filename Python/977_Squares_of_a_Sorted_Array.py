class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(x*x for x in A)
