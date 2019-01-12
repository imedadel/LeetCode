class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right+1):
            n = i
            while(n>0):
                if(n%10 == 0 or i%(n%10) != 0): break
                n = n // 10
            if(n == 0): ans.append(i)
                
        return ans
