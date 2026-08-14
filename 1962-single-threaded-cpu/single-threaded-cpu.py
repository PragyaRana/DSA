import heapq
class Solution:
    def getOrder(self, tasks):
        indexed  = [(e,p,i) for i,(e,p)in enumerate(tasks)]
        indexed.sort()

        heap = []
        res =[]
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            if not heap and time < indexed[i][0]:
                time = indexed[i][0]
        
            while i < n and indexed [i][0] <= time:
              e,p,idx = indexed[i]
              heapq.heappush(heap,(p,idx))
              i +=1
            p,idx= heapq.heappop(heap)
            res.append(idx)
            time += p
        return res
        