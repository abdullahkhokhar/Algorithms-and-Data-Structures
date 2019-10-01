// Students are asked to stand in non-decreasing order of heights for an annual photo.
//
// Return the minimum number of students not standing in the right positions.
// (This is the number of students that must move in order for all students to be
//  standing in non-decreasing order of height.)

class Solution {
    public int heightChecker(int[] heights) {
        // simply clone/copy the array passed in
        // sort it then compare the sorted arraty with the original
        int[] h = heights.clone();
        Arrays.sort(h);
        int ans = 0;
        for (int i = 0; i < h.length; ++i) {
            if (h[i] != heights[i])
                ++ans;
        }
        return ans;
    }
