"""
                Maximal Square

Problem:

    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example:

    Input: 

        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0

    Output: 4

"""
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        