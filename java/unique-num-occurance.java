/*
Given an array of integers arr, write a function that returns true if and only
if the number of occurrences of each value in the array is unique.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences,
2 has 2 and 3 has 1. No two values have the same number of occurrences.
*/

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        //  Each value should have different number of occurances

        // sort the array list
        // base case if if the length is 2 and both elements not equal then fale

        // set a counter = 1
        // go through array and keep checking if previous and ahead match then increment counter
        // if the counters in the seen list are reapted, reutrn false

        List<Integer> check = new ArrayList<>();
        int count = 1;
        Arrays.sort(arr);

        if(arr.length == 2 && arr[0] != arr[1]){
            return false;
        }

        for(int i = 0; i < arr.length - 1; i++){
            if(arr[i] == arr[i + 1]){
                count++;
            }
            else{
                if(!check.contains(count)){
                    check.add(count);
                    count = 1;
                }
                else{
                    return false;
                }
            }
        }

        return true;
    }
}
