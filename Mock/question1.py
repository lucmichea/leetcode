"""
                Nim Game

Problem :

    You are playing the following Nim Game with your friend: There is a heap of stones on the table, 
    each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. 
    You will take the first turn to remove the stones.

    Both of you are very clever and have optimal strategies for the game. 
    Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

    Input: 4
    Output: false 
    Explanation: If there are 4 stones in the heap, then you will never win the game;
                No matter 1, 2, or 3 stones you remove, the last stone will always be 
                removed by your friend.
"""           


class Solution:
    def canWinNim(self, n: int) -> bool:
        if (n <= 3):
            return True
        if (n == 4):
            return False
        
        return not self.canWinNim(n-3) or not self.canWinNim(n-2) or not self.canWinNim(n-1)

    # time limit exceed (the players are perfect, hence next solution)

    def canWinNimSimple(self, n: int) -> bool:
        if (n%4 == 0):
            return False
        else :
            return True