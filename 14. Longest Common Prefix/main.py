from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for j in range(len(min(strs,key=len))):
            s = [strs[i][j] for i in range(len(strs))]
            if s.count(s[0]) == len(s):
                result += s[0]
            else: break
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["doggy","dog","dogging"]))