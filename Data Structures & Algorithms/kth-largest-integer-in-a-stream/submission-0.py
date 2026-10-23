import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q=[-num for num in nums]
        heapq.heapify(self.q)
        self.safe=self.q.copy()
        self.largest=k
        

    def add(self, val: int) -> int:
        print(self.q,val,self.safe)
        heapq.heappush(self.safe,-val)
        heapq.heappush(self.q,-val)
        num=0
        for i in range(self.largest):
            num= -heapq.heappop(self.q)
        self.q=self.safe.copy()
        return num

        
