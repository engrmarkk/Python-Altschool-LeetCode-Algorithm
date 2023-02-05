class Solution:
    def isValid(self, s: str) -> bool:
        lis_t = []
        closeAndOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeAndOpen:
                if lis_t and lis_t[-1] == closeAndOpen[c]:
                    lis_t.pop()
                else:
                    return False
            else:
                lis_t.append(c)
        return True if not lis_t else False
