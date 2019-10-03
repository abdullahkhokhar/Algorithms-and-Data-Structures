def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1:
            return nums[0]
        # first go through the array and make a new one with the sums saved up
        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                nums[i] = nums[i] + nums[i-1]

        # then make another itteration go through the array and do sum[i+k] - sum[i]
        # keep track of the current_largest
        # if sum[i+k] is bigger than len(nums) - 1 --> then break
        current_largest = 0
        i = 0
        while not (i+k > len(nums)-1):
            curr = float((nums[i+k] - nums[i])) / k
            if curr > current_largest:
                current_largest = curr
            i += 1


        # return the current largest
        return current_largest
