"""
                    First Bad Version
                    
Problem :

    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
    Since each version is developed based on the previous version, all the versions after a bad version are also bad.
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. 
    You should minimize the number of calls to the API.

Example:

    Given n = 5, and version = 4 is the first bad version.

    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true

    Then 4 is the first bad version. 
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def __init__(self, realbadversion : int):
        self.realbadversion = realbadversion

    def isBadVersion(self, version : int) -> bool :
        if version >= self.realbadversion :
            return True
        else :
            return False

        def firstBadVersion(self, n : int) -> int:
        """
        :type n: int
        :rtype: int
        """
        lb = 1
        hb = n
        # We use dichotomie
        while lb<hb:
            mid = lb + ((hb-lb)//2)
            if self.isBadVersion(mid):
                hb = mid
            else:
                lb = mid+1
                
        return lb


if __name__ == '__main__' :
    sol = Solution(4)
    print(sol.firstBadVersion(5))


