/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
*/



class Solution {
    public int numDecodings(String s) {
        // DYNAMIC PROGRAMING ARRAY
        int [] dp = new int[s.length() + 1];
        // DP array will represent the number of ways to decode a string of length x
        // so d[0] means number of ways to decode a string of length 0

        // dp stores maximum number of ways of maping UPTO that index


        // BASE CASE
        dp[0] = 1; // empty string --> one way of decoding '' is doing nothing
        dp[1] = s.charAt(0) == '0' ? 0 : 1;  // we have no maping for the value 0

        // now we want to go through the string
        for(int i = 2; i <= s.length() ; i++){
            // evaluate the digit you are on
            int oneDigit = Integer.valueOf(s.substring(i-1, i)); // get the single current digit
            // now also get the previous digit
            int twoDigit = Integer.valueOf(s.substring(i-2, i));

            // check if they have mapings
            if(oneDigit >= 1){
                // add to our current sub-problem the amount of ways to solve previous subproblem
                dp[i] += dp[i-1];
            }

            if(twoDigit >= 10 && twoDigit <= 26){
                dp[i] += dp[i-2];
            }

        }

        return dp[s.length()];

    }
}
