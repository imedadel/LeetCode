class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        count = {
            "U": 0,
            "D": 0,
            "L": 0,
            "R": 0
        }
        
        for c in moves:
            count[c] += 1
        
        return count["U"] == count["D"] and count["L"] == count["R"]
