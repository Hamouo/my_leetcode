"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""

class Solution:
    def twoSum(self, nums, target):
        for i, i_num in enumerate(nums):
            for j, j_num in enumerate(nums[i+1:]):
                if i_num + j_num == target:
                    return [i, i+j+1]
run = Solution()
print(run.twoSum([2, 7, 11, 15], 9))


