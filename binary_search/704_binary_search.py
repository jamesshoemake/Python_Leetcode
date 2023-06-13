from typing import List

# binary search time: 0(logn)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            # java/c++ could trigger overflow making the mid too large
            # distance formula l + ((r - l) // 2)

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
