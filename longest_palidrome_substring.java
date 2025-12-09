/*
5. Longest Palindromic Substring
Hint
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
*/



class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        if (n < 2) return s;

        int start = 0, maxLen = 1;

        for (int i = 0; i < n; i++) {
            // odd
            int len1 = expand(s, i, i);
            // even
            int len2 = expand(s, i, i + 1);

            int len = Math.max(len1, len2);
            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }
        return s.substring(start, start + maxLen);
    }

    private int expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return r - l - 1;
    }
}
