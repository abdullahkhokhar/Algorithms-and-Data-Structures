# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i]
# is even, i is even.

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # we can focus on just adjusting the even indicies to be even values as
        # this will of course automatically make the odd indicies odd values

        # We will do this my going through the odd indicies and if we see that one of them is an even number
        # we will replace with the current odd number while traversing

        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2: # we ran into an even in an odd index
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
