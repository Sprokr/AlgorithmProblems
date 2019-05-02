
# https://leetcode.com/problems/find-the-difference/
# complexity - O(n)




class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        extraKey = ""
        for x in s:
            if x not in dic.keys():
                dic[x] = 0
            dic[x] += 1
        for x in t:
            if x not in dic.keys() or dic[x] == 0:
                extraKey = x
                break
            dic[x] -= 1
        return extraKey
