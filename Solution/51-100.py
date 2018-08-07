    # 53
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thissum = 0
        maxsum = -2**31

        for i in range(len(nums)):
            if thissum < 0:
                thissum = 0
            thissum += nums[i]
            maxsum = max(maxsum, thissum)
        return maxsum
