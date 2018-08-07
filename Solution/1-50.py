# 1 两数之和

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_nums=nums
        target=target
        n=len(list_nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                target_i=list_nums[i]
                target_j=list_nums[j]
                if target==target_i+target_j:
                    pos_num=[i,j]
                    return pos_num
        return True
            
