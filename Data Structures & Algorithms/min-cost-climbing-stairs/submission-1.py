from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def back(curr, summ):
            if curr>=len(cost):
                return summ
            summ+=cost[curr]
            return min(back(curr+1,summ),back(curr+2,summ))
        return min(back(0,0),back(1,0))