class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len({''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])) for a in A})
