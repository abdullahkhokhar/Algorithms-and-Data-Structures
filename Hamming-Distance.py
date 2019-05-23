# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # need to get it the number in binary then compare each element
        binx=format(x,"b") # covert to binary
        biny=format(y,"b") # covert to binary

        if len(binx)>len(biny): #fill up lower bits
            l=len(binx)-len(biny)
            biny=l*str(0)+biny

        elif len(biny)>len(binx): #fill up lower bits
            l=len(biny)-len(binx)
            binx=l*str(0)+binx


        c=0
        for i in range(len(binx)):
            if binx[i]!=biny[i]:
                c=c+1
        return c
        
