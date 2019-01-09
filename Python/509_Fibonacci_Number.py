class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Method 1 (tricky)
        from math import sqrt
        return int(((1+sqrt(5))**N-(1-sqrt(5))**N)/(2**N*sqrt(5)))
        
        # Method 2 (slower)
        # def mem_fib(n, _cache={}):
        #     '''efficiently memorized recursive function, returns a Fibonacci number'''
        #     if n in _cache:
        #         return _cache[n]
        #     elif n > 1:
        #         return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
        #     return n
        # return mem_fib(N)
    
                
            
