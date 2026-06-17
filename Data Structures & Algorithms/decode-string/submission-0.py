class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                sub_str = ''
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(sub_str * int(k))
        return ''.join(stack)
