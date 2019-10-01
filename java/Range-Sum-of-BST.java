/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 class Solution {
     public int rangeSumBST(TreeNode root, int L, int R) {
         if(root == null){
           return 0;
         }
         if(root.value >= L && root.value <= R){
           return value + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L , R);
         }
         else if(root.value < L){
           return rangeSumBST(root.right, L, R);
         }
         else{
           return rangeSumBST(root.left, L, R);
         }
     }
 }
