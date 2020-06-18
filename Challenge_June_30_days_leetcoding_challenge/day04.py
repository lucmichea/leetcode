"""
                Reverse String

Problem:
    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

 

Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


    # TOO SLOW 
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)%2:
            mid = len(s)//2
        else:
            mid = len(s)//2 -1

        i = 0
        while i < mid:
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
            i += 1
