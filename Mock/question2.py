"""
                    Hamming Distance

Problem :

    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.

Note:
    0 ≤ x, y < 2^31.

Example:

    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # we compute XOR between both numbers to get only 1 at bites positions that are different
        z = x ^ y
        count = 0
        # we search inside z to see how many ones 
        while z != 0:
            if (z & 1):
                count += 1
            z = z >> 1
        return count