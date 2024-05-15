class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cur_score = 0
        for n in s:
            if n =='(':
                stack.append(cur_score)
                cur_score = 0
            else:
                last_score = stack.pop()
                cur_score = last_score + max(2 * cur_score , 1)
        return cur_score














