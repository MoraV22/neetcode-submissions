class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(cord):
            return math.sqrt(cord[0]**2 + cord[1]**2)
        for cord in points:
            d= distance(cord)
            cord.append(d)
        
        points.sort(key=lambda x: x[2])
        res=[]
        for i in range(k):
            new= points[i]
            new.pop()
            res.append(new)
        return res
