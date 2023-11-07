class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        # i have a mean heap
        availble_heap = []
        heap = []
        for room in range(n):
            # for each room they will be available at zero
            heappush(heap,(0, room))

        # count of each room is zero
        count = {room:0 for room in range(n)}

        # sort them my start, start is uniq
        meetings.sort()
        print(meetings)
        for start, end in meetings:
            #  see e room, with the lowest availability,
            while heap and start >= heap[0][0]:
                heappush(availble_heap, heappop(heap)[1])
            
            if not availble_heap:
                room_end, room = heappop(heap)
                count[room] += 1
                heappush(heap,(room_end + end - start, room))
            else:
                room = heappop(availble_heap)
                count[room] += 1
                heappush(heap, (end,room))
               
        print(count)
        # max room, max_meetings
        mx_room = 0
        mx_meetings = 0
        for room in range(n):
            print(room)
            # if the crrent rom has greater than mx_meeting room
            if count[room] > mx_meetings:
                print("  ", room)
                mx_meetings = count[room]
                mx_room = room
        return mx_room
