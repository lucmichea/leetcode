"""
                Cheapest Flights Within K Stops

Problem:

    There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

    Now given all the cities and flights, together with starting city src and the destination dst, 
    your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
    Input: 
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 1
    Output: 200
    Explanation: 
        The graph looks like this:
                 
                {1}
                / \ 
           100 /   \ 500
              /     \ 
            {0}---->{2}
                100

        The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
    Input: 
        n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0, dst = 2, k = 0
    Output: 500
    Explanation: 
        The graph looks like this:

                {1}
                / \ 
           100 /   \ 500
              /     \ 
            {0}---->{2}
                100

        The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

 

Constraints:

    The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
    The size of flights will be in range [0, n * (n - 1) / 2].
    The format of each flight will be (src, dst, price).
    The price of each flight will be in the range [1, 10000].
    k is in the range of [0, n - 1].
    There will not be any duplicated flights or self cycles.

"""
from typing import List
import numpy as np

class Solution:
    # time limit exceeded for dynamic implementation
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst :
            return 0
        if K < 0 : 
            return -1
        
        l_possible_prices = []
        for flight in flights:
            flight_src, flight_dst, price = flight
            if src == flight_src:
                price_taking_the_flight = self.findCheapestPrice(n, flights, flight_dst, dst, K-1)
                if price_taking_the_flight != -1:
                    l_possible_prices.append(price + price_taking_the_flight)
        
        if l_possible_prices :
            return min(l_possible_prices)
        else :
            return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]],
        src = 0, dst = 2, K = 1))





#### ONLINE ####

# import heapq
# from collections import defaultdict
# class Solution:
#     # DFS
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         if not flights or not flights[0]:
#             return -1
        
#         costs = [float('inf')] * n
        
#         # Initialize grid map
#         grid = collections.defaultdict(list)
#         for s, d, c in flights:
#             grid[s].append([d, c])
        
#         heap = [(0,src,0)] # cost, source, visitedCnt: K
#         while heap:
#             subCost, subSrc, visitedCnt = heap.pop(0)
#             # Varification
#             if costs[subSrc] <= subCost or (visitedCnt > K and subSrc != dst): 
#                 continue

#             costs[subSrc] = subCost
#             # Recursive call
#             for nextDst, nextCost in grid[subSrc]: # Dst to next Src
#                 heap.append((subCost + nextCost, nextDst, visitedCnt + 1))
        
#         return -1 if costs[dst] == float('inf') else costs[dst]

    # Dijkstra
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         if not flights or not flights[0]:
#             return -1
        
#         # Initialize grid map
#         grid = collections.defaultdict(list)
#         for s, d, c in flights:
#             grid[s].append([d, c])
        
#         heap = [(0,src,0)] # cost, source, visitedCnt: K
#         while heap:
#             subCost, subSrc, visitedCnt = heapq.heappop(heap)
#             # Varification
#             if subSrc == dst:
#                 return subCost
#             if visitedCnt > K: # if K == 1 one visited, #### visited
#                 continue
#             # Recursive call
#             for nextDst, nextCost in grid[subSrc]: # Dst to next Src
#                 heapq.heappush(heap, (subCost + nextCost, nextDst, visitedCnt + 1))
        
#         return -1
    
    # Bellman-ford: https://www.youtube.com/watch?v=lyw4FaxrwHg&t=374s
    # For non-stop restriction
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    #     #No limited stop return 200
    #     dist = [float('inf') for i in range(n)]
    #     dist[src] = 0
    #     # for _ in range(n-1): # Why n-1 iteration? 
    #     for (subSrc, subDst, subCost) in flights:
    #         if dist[subSrc] + subCost < dist[subDst]:
    #             dist[subDst] = dist[subSrc] + subCost
    #     # for _ in range(n-1):
    #     for (subSrc, subDst, subCost) in flights:
    #         if dist[subSrc] + subCost < dist[subDst]:
    #             dist[subDst] = float("-inf")        
    #     return dist[dst]
                
        
    # Bellman-ford: https://www.youtube.com/watch?v=lyw4FaxrwHg&t=374s
    # For k stop restriction
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
# #         #K limited stop return 200                
#         dist = [[float('inf') for _ in range(n)] for _ in range(K + 2)]
#         for visitedCnt in range(K + 2):
#             dist[visitedCnt][src] = 0
#         # for _ in range(n-1): # Time limit exceeded
#         for visitedCnt in range(1, K + 2):
#             for (subSrc, subDst, subCost) in flights:
#                 if dist[visitedCnt-1][subSrc] + subCost < dist[visitedCnt][subDst]:
#                     dist[visitedCnt][subDst] = dist[visitedCnt-1][subSrc] + subCost
#         # for _ in range(n-1): # Time limit exceeded
#         for visitedCnt in range(1, K + 2):
#             for (subSrc, subDst, subCost) in flights:
#                 if dist[visitedCnt-1][subSrc] + subCost < dist[visitedCnt][subDst]:
#                     dist[visitedCnt][subDst] = float("-inf")        
#         return dist[K + 1][dst] if dist[K + 1][dst] != float('inf') else -1

    # Floyd Warshall All Pair Shortest Path
    # non stop restrict
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         if not flights or not flights[0]:
#             return -1
        
#         # Initialize grid map
#         grid = [[float('inf')]*n for _ in range(n)]
#         for s, d, c in flights:
#             grid[s][d] = c
        
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
#                     # if (grid[i][j] > grid[i][k] + grid[k][j]):
#                     #     grid[i][j] = grid[i][k] + grid[k][j]
        
#         return grid[src][dst] if grid[src][dst] != float('inf') else -1
    
    # (Not working) Floyd Warshall All Pair Shortest Path
    # k stop restrict
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         if not flights or not flights[0]:
#             return -1
        
#         # Initialize grid map
#         grid = [[[float('inf')]*n for _ in range(n)] for _ in range(K + 2)]
        
#         for visitedCnt in range(K + 2):
#             for s, d, c in flights:
#                 grid[visitedCnt][s][d] = c

#         for l in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     for visitedCnt in range(1, K + 2):
#                         grid[visitedCnt][i][j] = min(grid[visitedCnt][i][j], grid[visitedCnt-1][i][l] + grid[visitedCnt-1][l][j])
#                         # if (grid[i][j] > grid[i][k] + grid[k][j]):
#                         #     grid[i][j] = grid[i][k] + grid[k][j]
        
#         return grid[K+1][src][dst] if grid[K+1][src][dst] != float('inf') else -1