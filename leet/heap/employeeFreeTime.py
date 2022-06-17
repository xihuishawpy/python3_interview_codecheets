"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
"""
time: nlgn
space: n
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []

        for e in schedule:
            for m in e:
                events.extend(((m.start, 1), (m.end, -1)))
        heapq.heapify(events)

        itv = []
        prev = None
        bal = 0

        while events:
            t, c = heapq.heappop(events)
            if bal == 0 and prev is not None and t != prev:
                itv.append(Interval(prev, t))
            bal += c
            prev = t

        return itv
        
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        for e in schedule:
            for m in e:
                events.extend(((m.start, 1), (m.end, -1)))
        events.sort()
        itv = []
        prev = None
        bal = 0
        for t, c in events:
            if bal == 0 and prev is not None and t != prev:
                itv.append(Interval(prev, t))
            bal += c
            prev = t
        return itv


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = sorted([m for e in schedule for m in e], key=lambda x: x.start)

        end = events[0].end
        rtn = []

        for e in events:
            if e.start > end:
                rtn.append(Interval(end, e.start))
            end = max(end, e.end)

        return rtn