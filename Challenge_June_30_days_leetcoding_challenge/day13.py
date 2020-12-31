"""
                Largest Divisible Subset

Problem:

    Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

    Si % Sj = 0 or Sj % Si = 0.

    If there are multiple solutions, return any subset is fine.

Example 1:

    Input: [1,2,3]
    Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

    Input: [1,2,4,8]
    Output: [1,2,4,8]

"""
from typing import List

# we could use the fact that the largest element of a subset could be divided by all of the other elements of this subset.
# Hence when we create our list we check divisibility only with the largest element and not all of them.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        largest_subset = []
        for i in range(len(nums)):
            subset = [nums[i]]
            subset_max = nums[i]
            for j in range(len(nums)):
                if subset_max % nums[j] == 0 or nums[j] % subset_max == 0:
                    if nums[j] not in subset:
                        subset.append(nums[j])

                    if nums[j] > subset_max:
                        subset_max = nums[j]
            
            if len(subset) > len(largest_subset):
                largest_subset = subset
        return largest_subset

            
