"""
                    Permutation in String

Problem :
    Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
    In other words, one of the first string's permutations is the substring of the second string.


Example 1:

    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

    Input: s1= "ab" s2 = "eidboaoo"
    Output: False

 
Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we use the counter of our first string
        cs1 = Counter(s1)

        # we iterate over the string
        for i in range (len(s2)-len(s1)+1):
            # if the counter representation of the sliding window's substring is the same then we return True
            if Counter(s2[i:i+len(s1)]) == cs1:
                return True
        # we didn't find any corresponding substring permutation, we return False
        return False

    def checkInclusionHash(self, s1: str, s2: str) -> bool:
        
        size_1, size_2 = len(s1), len(s2)
        
        if ( size_1 > size_2 ) or ( size_1 * size_2 == 0 ):
            
            # Quick rejection for oversize pattern or empty input string 
            return False
        
        
		# compute signature for s1
        target_signature = sum( map(hash, s1) )
        
		# compute signature initial value in sliding window
        cur_signature = sum( map(hash, s2[:size_1] ) )
        
		# Find match position by sliding window
        for tail_index in range(size_1, size_2 ):
            
            if cur_signature == target_signature:
                # Accept, find one match
                return True
            
            head_index = tail_index - size_1
            
            # update cur_signature for next iteration
            prev_char, next_char = s2[head_index], s2[tail_index]
            cur_signature += ( hash(next_char) - hash(prev_char) )

            
        if cur_signature == target_signature:
            # last comparison after iteraion is completed
            # Accept, find one match
            return True    
        
        else:
            # Reject, no match between s1 and s2
            return False