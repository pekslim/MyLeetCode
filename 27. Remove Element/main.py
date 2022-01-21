from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            else:
                pass
        return k, nums

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([0,1,2,2,3,0,4,2],2))

