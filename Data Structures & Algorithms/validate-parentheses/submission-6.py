class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        start = "({["
        if len(s) % 2 != 0: return False
        while s or stack:
            if s:
                if s[0] in start:
                    stack.append(s.pop(0))
                elif (s and not stack) or ((s[0] == ")" and stack[-1] != "(") or (s[0] == "]" and stack[-1] != "[") or (s[0] == "}" and stack[-1] != "{")):
                    return False
                else:
                    stack = stack[:-1]
                    s = s[1:]
            elif stack and not s:
                return False
        return True
        