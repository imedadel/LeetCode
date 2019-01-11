class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = bin(x)[2:]
        by = bin(y)[2:]
        
        bx = bx.zfill(len(by))
        by = by.zfill(len(bx))
        
        return sum(bxi != byi for bxi,byi in zip(bx,by))
