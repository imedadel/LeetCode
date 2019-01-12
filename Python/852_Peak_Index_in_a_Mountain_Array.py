class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return A.index(max(A))
        return max(range(len(A)), key=A.__getitem__)
