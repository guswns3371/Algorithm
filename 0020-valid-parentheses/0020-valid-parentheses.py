class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            bracket = s[i]
            if bracket in ("(", "{", "["):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last_b = stack.pop()
                if bracket == ")" and last_b != "(":
                    return False
                elif bracket == "}" and last_b != "{":
                    return False
                elif bracket == "]" and last_b != "[":
                    return False
        return len(stack) == 0
        