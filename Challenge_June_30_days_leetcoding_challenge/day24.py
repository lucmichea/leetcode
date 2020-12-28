"""
                Unique Binary Search Trees

Problem:

    Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

       1         3     3      2      1
        \       /     /      / \      \ 
         3     2     1      1   3      2
        /     /       \                 \ 
       2     1         2                 3

"""
# https://en.wikipedia.org/wiki/Catalan_number

from math import factorial

class Solution:
    def numTrees(self, n: int) -> int:
        return int(factorial(2*n)/(factorial(n)*factorial(n)*(n+1)))

if __name__=='__main__':
    n = 3 
    sol = Solution()
    print(sol.numTrees(n))