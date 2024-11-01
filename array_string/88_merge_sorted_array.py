from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        mi = m - 1
        ni = n - 1
        while i >= 0:
            m = -10e9
            n = -10e9
            if mi >= 0:
                m = nums1[mi]
            if ni >= 0:
                n = nums2[ni]
            if m > n:
                nums1[i] = m
                mi = mi - 1
            else:
                nums1[i] = n
                ni = ni - 1
            i = i - 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
