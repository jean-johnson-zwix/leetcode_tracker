# First Bad Version (LC #278)
# URL: https://leetcode.com/problems/first-bad-version/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : Binary Search
# APPROACH   : This problem uses binary search to efficiently find the first bad version within a range of `n` versions. The search space is iteratively halved by checking the `mid` version: if `mid` is bad, the first bad version could be `mid` or earlier, so we search `[left, mid]`; otherwise, it must be after `mid`, so we search `[mid+1, right]`. The loop continues until `left` and `right` converge, at which point `left` holds the first bad version.
# TIME       : O(log n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: When performing binary search to find the first occurrence of a condition (e.g., first true, first bad version), use `while left < right`, set `right = mid` if `mid` satisfies the condition, and `left = mid + 1` if it doesn't, then return `left`.
# GOTCHAS    : Be careful with off-by-one errors when updating `left` and `right` pointers. The `mid` calculation `left + (right - left) // 2` prevents potential integer overflow compared to `(left + right) // 2` in some languages.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2024-07-30
# ─────────────────────────────────────────
# YOUR INSIGHT:
# When finding a boundary (first true, last false), use while left < right with right = mid and return left

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        while left<right:
            mid=left+(right-left)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return left
