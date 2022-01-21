class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        l = len(needle)
        lst = [haystack[x:x+l] for x in range(len(haystack)-l+1)]
        for i in range(len(lst)):
            if lst[i] == needle:
                return i



if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("hello","ll"))


#####################################################################

class Solution(object):
    def strStr(self, haystack, needle):

        if len(needle) == 0:
            return 0

        if needle in haystack:
            return haystack.index(needle)

        else:
            return -1