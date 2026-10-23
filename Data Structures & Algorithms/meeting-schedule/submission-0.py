"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        prev=None
        for r in intervals:
            if not prev:
                prev=r
                continue
            #prev.start <= r.start
            if r.start<prev.end:
                return False
            prev=r
        return True
