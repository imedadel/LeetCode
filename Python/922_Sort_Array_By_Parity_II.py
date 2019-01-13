class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = [x for x in A if x%2==0]
        odd = [x for x in A if x%2!=0]
        
        even_i = 0
        odd_i = 0
        
        ans = []
        
        for x in range(0,len(A)):
            if x%2==0:
                ans.append(even[even_i])
                even_i += 1
            else:
                ans.append(odd[odd_i])
                odd_i += 1
        return ans
                
