# Two Sum II - Input Array Is Sorted (LC #167)
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Two Pointer
# APPROACH   : This approach utilizes two pointers, one starting at the beginning (`left`) and one at the end (`right`) of the sorted array. The sum of elements at these pointers is compared with the target. If the sum is too small, `left` is incremented; if too large, `right` is decremented, effectively narrowing the search space until the target sum is found.
# TIME       : O(n)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: The sorted nature of the input array is crucial, enabling an efficient two-pointer approach. By starting pointers at opposite ends, we can strategically move them inward based on whether the current sum is less than or greater than the target, guaranteeing a linear time solution.
# GOTCHAS    : Remember to return 1-based indices as specified by the problem, not 0-based array indices. The problem guarantees exactly one solution, simplifying error handling.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐⭐☆ (4/5)
# REVISIT    : ✅ No
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Two Pointer: move left pointer for larger sum and right pointer for smaller sum

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            current_sum=numbers[left]+numbers[right]
            if current_sum<target: left+=1# move left
            elif current_sum>target: right-=1# move right
            else: return [left+1,right+1]
