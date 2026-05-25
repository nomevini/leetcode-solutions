/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
  public boolean isPalindrome(int x) {
    String strNumber = String.valueOf(x);
    String strNumberReversed = new StringBuilder(strNumber).reverse().toString();

    return strNumber.equals(strNumberReversed);
  }
}
// @lc code=end
