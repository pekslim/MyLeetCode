class Solution:
    def isValid(self, s: str) -> bool:
        FILO = []
        for i in s:
            if i in ['(','{','[']:
                FILO.append(i)
            if i in [')', '}', ']'] and FILO == []:
                return False
            if i == '}':
                if FILO[-1] == '{':
                    FILO.pop()
                else: return False
            if i == ')':
                if FILO[-1] == '(':
                    FILO.pop()
                else:
                    return False
            if i == ']':
                if FILO[-1] == '[':
                    FILO.pop()
                else: return False
        if FILO == []:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("(){}}{"))