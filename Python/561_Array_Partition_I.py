class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(x for x in nums[::2])
    
#         Method 2
        # nums.sort()
        # n = len(nums)
        # return sum(nums[x] for x in range(0,n,2))
#         Method 3
        # sum = 0
#         for x in range(0,n,2):
#           sum += nums[x]  
#         return sum
    
        
