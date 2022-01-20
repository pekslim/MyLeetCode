from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                temp = nums[0]
                continue
            if nums[i] == temp:
                nums[i] = '_'
            else:
                temp = nums[i]
        s = nums.count('_')
        nums[:] = [x for x in nums if x != '_']
        nums = nums + s*['_']
        return len(nums)-s, nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

#############################################################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))


#############################################################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0  # pointer one

        for i in range(len(nums)):  # pointer two
            if nums[k] == nums[
                i]:  # here, we`ll check if last pointer value is equvalent to next value(second pointer value) or not
                pass  # if its same we won`t removing it for now.
            else:
                nums[k + 1] = nums[
                    i]  # once we find the different value then the first pointer, we`ll store it next to the last pointer. In that way we`ll make a sorted required series.
                k += 1  # then we`ll increase the first pointer.

        return k + 1