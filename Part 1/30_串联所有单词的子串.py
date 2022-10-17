"""
给定一个字符串s和一个字符串数组words。words中所有字符串 长度相同。
s中的 串联子串 是指一个包含words中所有字符串以任意顺序排列连接起来的子串。
例如，如果words = ["ab","cd","ef"]， 那么"abcdef"，"abefcd"，"cdabef"，"cdefab"，"efabcd"， 和"efcdab" 都是串联子串。"acdbef" 不是串联子串，因为他不是任何words排列的连接。
返回所有串联字串在s中的开始索引。你可以以 任意顺序 返回答案。

示例 1：
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。
"""
import collections


class Solution:
    def findSubstring(self, s, words):
        cnt, l = len(words), len(words[0])  # 单个单词的数量和长度
        i, j = 0, cnt * l - 1   # i和j分别指向0和words的长度
        ans = []
        check = collections.Counter(words)  # 统计单词的频率
        while j < len(s):
            ss = s[i: j + 1]    # 截取一段words那么长的字符
            tmp = []
            for k in range(0, len(ss), l):  # 逐个单词长度截取子字符串
                tmp.append(ss[k: k + l])
            if collections.Counter(tmp) == check:   # 统计出现词以及词的频率和原单词组是否一致
                ans.append(i)   # 如果是，添加起点
            i += 1  # 窗口滑动
            j += 1
        return ans
