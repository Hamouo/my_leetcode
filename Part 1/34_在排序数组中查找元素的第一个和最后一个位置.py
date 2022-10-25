"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

你必须设计并实现时间复杂度为O(log n)的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        def searchLeft(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            if left == len(nums):
                return -1
            return left if nums[left] == target else -1

        def searchRight(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            if right == 0:
                return -1
            return right - 1 if nums[right - 1] == target else -1

        return [searchLeft(nums, target), searchRight(nums, target)]
