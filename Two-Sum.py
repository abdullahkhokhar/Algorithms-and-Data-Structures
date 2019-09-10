#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.


# I will firstly map all elements as well as their indicies into a hash table
# In python, I will use a dictionary
# After maping, will go through each element to see if its complement (target-item) exists
# We traverse the list twice, and lookup for indicies will be constant, so O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        # add all the elements in the dictionary
        for i in range((len(nums) - 1)):
            hash_dict[nums[i]] = i
        # go through and check for composite
        for vals in hash_dict:
            if (target-vals) in hash_dict:
                return [hash_dict[vals], hash_dict[target-vals]]
        
