class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        new=[]
        res=[]
        for r in intervals:
            if not new:
                new=r
                continue
            if r[0]<= new[1]:
                new[1]=max(new[1],r[1])
            else:
                res.append(new)
                new=r
        res.append(new)
        return res