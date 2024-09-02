from functools import cache
from typing import *
from math import inf
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        if n == 1 or k == 1:
            return nums
        l = 0
        r = 1
        while l <= n - k:
            while r < k:
                if r + 1 == k and nums[l + r] - nums[l + r - 1] == 1:
                    # print(nums[l + r])
                    res.append(nums[l + r])
                    r -= 1
                    break

                if nums[l + r] - nums[l + r - 1] == 1:
                    # print(l + r - 1, l + r, nums[l + r - 1], nums[l + r])
                    r += 1
                else:
                    res += [-1] * r
                    l += r - 1
                    r = 1
                    break
            l += 1
        return res

if __name__ == '__main__':
    s = Solution()
    n = input()
    nums = list(map(int, input().split()))

    res = s.resultsArray([1,7,8], 2)
    print(res)