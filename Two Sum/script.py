class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i, j]


# Testing the object
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
