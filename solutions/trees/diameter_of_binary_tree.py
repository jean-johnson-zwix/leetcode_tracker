# Diameter of Binary Tree (LC #543)
# URL: https://leetcode.com/problems/diameter-of-binary-tree/
# ─────────────────────────────────────────
# DIFFICULTY : Easy
# PATTERN    : DFS
# APPROACH   : This solution uses a post-order Depth First Search (DFS) traversal. A helper function recursively calculates the maximum depth of each subtree. During this traversal, at each node, it computes the potential diameter passing through that node (sum of left subtree's depth and right subtree's depth) and updates a global maximum diameter tracker.
# TIME       : O(n)
# SPACE      : O(n)
# ─────────────────────────────────────────
# KEY INSIGHT: The diameter of a binary tree is the longest path between any two nodes. This path can be found by, for each node, calculating the sum of the maximum depths of its left and right subtrees. A single DFS traversal can compute both the depth of each subtree and update a global maximum diameter.
# GOTCHAS    : The diameter is the number of edges, not nodes. The diameter might not pass through the root of the entire tree, but rather through a node in a subtree. Ensure the base case for an empty node returns 0 depth.
# ─────────────────────────────────────────
# RATING     : ⭐⭐⭐☆☆ (3/5)
# REVISIT    : 🔁 YES — add to revision list
# DATE       : 2026-03-05
# ─────────────────────────────────────────
# YOUR INSIGHT:
# Tree - Nonlocal tracker: for global properties of tree (diameter, max path sum), use a helper to return depth but track the diameter/max path sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        def depthOfTree(node):
            if not node:
                return 0
            left=depthOfTree(node.left)
            right=depthOfTree(node.right)
            diameter[0]=max(diameter[0],left+right) #diameter
            return 1+max(left,right) #depth
        depthOfTree(root)
        return diameter[0]
