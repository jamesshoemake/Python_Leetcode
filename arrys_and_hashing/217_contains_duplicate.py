# leetcode 217. Contains Duplicate - easy
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
