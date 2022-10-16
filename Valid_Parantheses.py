"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        paranthesesTypes = {'(' : ')', '[' : ']', '{' : '}'}
        parantheseList = []
        for i in s:
            if i in paranthesesTypes.keys():
                parantheseList.append(i)
            else:
                if parantheseList == []:
                    return False
                a = parantheseList.pop()
                if i!= paranthesesTypes[a]:
                    return False
        return parantheseList == []
