"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # line sweep 
        mp=defaultdict(int)
        for interval in intervals:
            mp[interval.start]+=1
            mp[interval.end]-=1
        current_meetings=0
        meeting_rooms=0
        for t in sorted(mp.keys()):
            current_meetings+=mp[t]
            meeting_rooms=max(meeting_rooms,current_meetings)
        return meeting_rooms