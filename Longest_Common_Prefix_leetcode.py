"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""
        if strs is None or len(strs) == 0:
            return lcp

        # Finding minimum length string from the array
        minimumLength = len(strs[0])
        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))

        for i in range(minimumLength):
            getCurrentChar = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != getCurrentChar:
                    return lcp
            lcp += getCurrentChar
        return lcp
