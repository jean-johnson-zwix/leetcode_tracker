# Balanced Binary Tree (LC #110)
# URL: https://leetcode.com/problems/balanced-binary-tree/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : DFS
# APPROACH   : This solution uses a recursive Depth-First Search (DFS) to calculate the height of each subtree. During the post-order traversal, it checks if the absolute difference between the heights of the left and right subtrees at the current node is greater than 1. A non-local list `heightBalanced` is used to track if any imbalance is found anywhere in the tree.
# TIME       : O(n)
# SPACE      : O(h)
# ─────────────────────────────────────────
# KEY INSIGHT: The key is to combine the height calculation and the balance check into a single recursive DFS traversal. Each node's height is computed, and simultaneously, its balance condition (based on its children's heights) is verified.
# GOTCHAS    : Remember to handle the base case for `None` nodes (height 0). The balance check must occur at every node, not just the root. Using a non-local variable (like a list) is one way to propagate the `False` balance status across recursive calls; an alternative is to return a tuple `(is_balanced, height)`.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Tree with Non-Local Tracker: use list to track if tree is heightBalanced and nested method to recursivelyl computer depth of Tree at each node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heightBalanced=[True]
        def depthOfTree(root):
            if not root:
                return 0
            left_depth=depthOfTree(root.left)
            right_depth=depthOfTree(root.right)
            # check if depth difference greater than 1
            if abs(left_depth-right_depth)>1:
                heightBalanced[0]=False
            return 1+max(left_depth,right_depth)
        depthOfTree(root)
        return heightBalanced[0]
