# Find All Anagrams in a String (LC #438)
# URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# ─────────────────────────────────────────
# DIFFICULTY : Medium
# PATTERN    : Sliding Window, HashMap
# APPROACH   : This solution uses a fixed-size sliding window of length `len(p)`. It maintains frequency maps for the characters in the current window (`s_count`) and the target pattern (`p_count`). As the window slides, it efficiently updates `s_count` by adding the new character and removing the character leaving the window, then checks if `s_count` matches `p_count`.
# TIME       : O(N)
# SPACE      : O(1)
# ─────────────────────────────────────────
# KEY INSIGHT: The core idea is to use a fixed-size sliding window and maintain character frequency counts for the window and the target pattern. Instead of re-calculating frequencies for each substring, efficiently update the window's frequency map by adding the new character and decrementing the count of the character leaving the window.
# GOTCHAS    : Forgetting to handle the initial window check. Incorrectly updating frequency maps (e.g., not removing characters whose count drops to zero). Edge case where `len(p) > len(s)`.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2023-10-27
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Fixed size sliding window with anagram check using frequency map

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_len=len(p)
        if window_len > len(s):
            return []
        # frequence_maps
        p_count={}
        s_count={}
        # initialize window
        for i in range(window_len):
            p_count[p[i]]=p_count.get(p[i],0)+1
            s_count[s[i]]=s_count.get(s[i],0)+1
        result=[]
        if s_count==p_count: # anagram check for first window
            result.append(0)
        # start sliding
        for end_index in range(window_len,len(s)):
            start_index=end_index-window_len
            # add char from right
            new_char=s[end_index]
            s_count[new_char]=s_count.get(new_char,0)+1
            # remove char from left
            old_char=s[start_index]
            s_count[old_char]-=1
            # cleanup for efficiency
            if s_count[old_char]==0:
                del s_count[old_char]
            # anagram check
            if s_count==p_count:
                result.append(start_index+1)
        return result
