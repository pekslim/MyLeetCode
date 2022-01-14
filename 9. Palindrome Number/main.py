class Solution:
    def isPalindrome(self, x: int) -> bool:
        xw = str(x)
        if xw == xw[::-1]:
            return True
        else:
            return False