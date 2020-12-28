"""
                Power of Two

Problem:

    Given an integer, write a function to determine if it is a power of two.

Example 1:

    Input: 1
    Output: true 
    Explanation: 2^0 = 1

Example 2:

    Input: 16
    Output: true
    Explanation: 2^4 = 16

Example 3:

    Input: 218
    Output: false

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0 
        while n < 2**power:
            if n == 2**power:
                return True
            power += 1
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(158))