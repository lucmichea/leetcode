"""
                Queue Reconstruction by Height

Problem:

    Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
    where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
    Write an algorithm to reconstruct the queue.

Note:
    The number of people is less than 1,100.
 

Example

    Input:
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    Output:
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # first we sort each height in descending order and ascending placement
        sorted_queue = sorted(people, key= lambda x: (-x[0], x[1]))

        # we insert it in our reconstructed queue at the right place
        reconstructed_queue = []
        for height, placement in sorted_queue:
            reconstructed_queue.insert(placement, [height, placement])
        return reconstructed_queue

if __name__ == '__main__':
    q = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    sol = Solution()
    print(sol.reconstructQueue(q))
