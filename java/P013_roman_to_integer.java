/*
 * @lc app=leetcode id=13 lang=java
 *
 * [13] Roman to Integer
 */

// @lc code=start

import java.util.Map;

class Solution {

  private static final Map<Character, Integer> digits = new HashMap<>();

  static {
    digits.put('I', 1);
    digits.put('V', 5);
    digits.put('X', 10);
    digits.put('L', 50);
    digits.put('C', 100);
    digits.put('D', 500);
    digits.put('M', 1000);
  }

  public int romanToInt(String s) {
    int sum = 0;

    for (int i = 0; i < s.length(); i++) {
      int current = digits.get(s.charAt(i));

      if (i < s.length() - 1 && current < digits.get(s.charAt(i + 1))) {
        sum -= current;
      } else {
        sum += current;
      }
    }

    return sum;
  }
}
// @lc code=end
