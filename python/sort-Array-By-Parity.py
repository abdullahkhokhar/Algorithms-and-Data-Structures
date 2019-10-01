# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # can loop through and add all evens then loop again and add all ods
        # will be 2n runtime
        final_list = [];
        for num in A:
            if((num % 2) == 0):
                final_list.append(num);
        for num in A:
            if((num % 2) == 1):
                final_list.append(num)

        return final_list
