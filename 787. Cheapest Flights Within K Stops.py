from collections import defaultdict
from Queue import PriorityQueue 2

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        pq = PriorityQueue()
        pq.put((0, src, 0)) 

        while not pq.empty():
            cost, city, stops = pq.get()

            if city == dst:
                return cost

            if stops == k + 1:
                continue

            for nei, price in graph[city]:
                new_cost = cost + price
                if new_cost < dist[nei][stops + 1]:
                    dist[nei][stops + 1] = new_cost
                    pq.put((new_cost, nei, stops + 1))

        return -1
