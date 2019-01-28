class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans =[]
        for index, score in enumerate(ops):
            if score == "D": ans.append(ans[-1]*2)
            elif score == "+": ans.append(ans[-1]+ans[-2])
            elif score == "C": ans.pop()
            else: ans.append(int(score))
        return sum(x for x in ans)
