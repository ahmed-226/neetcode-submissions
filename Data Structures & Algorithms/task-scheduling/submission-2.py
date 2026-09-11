class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for task in tasks:
            count[ord(task)-ord('A')] +=1
        maxHeap = [-cnt for cnt in count if cnt > 0]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time +=1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt !=0:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
                
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time