"""
Time Complexity (TC):
    - **O(N log N)**: Dominated by the initial **sorting** of the N intervals 
        and the subsequent N heap operations (push/pop, which are O(log N)).

Space Complexity (SC):
    - **O(N)**: Required to store the end times of meetings in the min-heap. 
        In the worst case (no meetings overlap), the heap will hold N elements.

Approach: Min-Heap (Greedy)
        1. **Sort** the input `intervals` based on their **start times**.
        2. Initialize a **min-heap** to store the **end times** of meetings
           currently occupying a room.
        3. Iterate through the sorted intervals:
           a. If the current meeting's **start time** is greater than or equal to
              the smallest end time in the heap (the earliest free room), 
              **pop** that end time (reuse the room).
           b. **Push** the current meeting's **end time** onto the heap.
        4. The final **size of the heap** represents the maximum number of 
           concurrent meetings, which is the minimum number of rooms required.
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for each in intervals[1:]:
            start, end = each.start, each.end
            heap_top = heap[0]
            
            if start >= heap_top:
                heapq.heappop(heap)

            heapq.heappush(heap, end)                
            
        return len(heap)