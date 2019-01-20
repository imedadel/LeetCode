class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)
        reverse = "".join(str(1 - int(x)) for x in binary[2::])
        return int(reverse,2)
