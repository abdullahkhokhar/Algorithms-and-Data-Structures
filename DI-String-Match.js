// Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
//
// Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
//
// If S[i] == "I", then A[i] < A[i+1]
// If S[i] == "D", then A[i] > A[i+1]


/**
 * @param {string} S
 * @return {number[]}
 */
var diStringMatch = function(S) {
    let lo = 0;
    let hi = S.length;

    var ans_arr  = [];
    for(let i = 0; i < S.length; i++){
        if(S.charAt(i) == 'I'){
            ans_arr.push(lo);
            lo = lo + 1;
        }
        else{
            ans_arr.push(hi);
            hi = hi-1;
        }
    }
    ans_arr.push(lo)
    return ans_arr;

};
