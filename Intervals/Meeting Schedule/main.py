"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            in1, in2 = intervals[i], intervals[i+1]
            if in2.start < in1.end:
                return False
        return True


s = Solution()
a = [Interval(0,30),Interval(5,10),Interval(15,20)]
b = [Interval(0,8),Interval(8,10)]
c = [Interval(5,8),Interval(9,15)]
print(s.canAttendMeetings(a))
print(s.canAttendMeetings(b))
print(s.canAttendMeetings(c))

