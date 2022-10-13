"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

示例1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        maxstring = ''
        for i, k in enumerate(s):
            maxstring += k
            for j in s[i+1:]:
                if j not in maxstring:
                    maxstring += j
                else:
                    max_len = max(len(maxstring), max_len)
                    break
            if maxstring:
                max_len = max(len(maxstring), max_len)
                maxstring = ''
        return max_len



