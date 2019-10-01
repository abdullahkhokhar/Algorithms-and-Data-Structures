# In a array A of size 2N, there are N+1 unique elements,
# and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sets=set()
        for i in A:
            if (i in sets):
                return i # because all the other elements are unique, you know the one
                        # that is repeated is the one you want
            else:
                sets.add(i)
        
