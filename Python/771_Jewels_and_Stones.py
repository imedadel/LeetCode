class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        myJewels = [*J]
        count = 0
        for stone in S:
            if stone in myJewels: count += 1
        return count
