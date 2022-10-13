"""
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果needle 不是 haystack 的一部分，则返回 -1 。

示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
"""


class Solution:
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        return haystack.find(needle)
