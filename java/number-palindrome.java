/*
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

EX)
Input: 121
Output: true
*/

class Solution {
    public boolean isPalindrome(int x) {
        // determine if an interger is a palindrome
        // same element word backards

        // base cases
        if(x < 0) return false; // because the negative sign will not come arround
        if(x == 0) return true; // we know that 0 is always a palindromve

        // now we will deal with the positive case
        int y = x;
        int num = 0; // will be reverse of y

        // let us reverse y
        while(y>0){
            // each iteration we will % 10 to get next digit of y
            // wee wil keep adding to num next number place
            // next number place we get  by multiplying by 10
            num = (num * 10) + (y % 10);
            y = (y / 10); // remove the last  digit
        }
        return (x == num);
    }
}
