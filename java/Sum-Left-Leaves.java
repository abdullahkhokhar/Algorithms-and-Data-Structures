/**
Find the sum of all left leaves in a given binary tree.

 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 class Solution {
    public int sumOfLeftLeaves(TreeNode root) {

        return bsf(root, false);
    }

    private int bsf(TreeNode node, boolean isLeft) {
        int sum = 0;
        if (node == null) {
            return 0;
        }
        if (node.left == null && node.right == null) {
            if (isLeft) {
                sum += node.val;
            }
        }
        sum += bsf(node.left, true);
        sum += bsf(node.right, false);
        return sum;
    }
}
