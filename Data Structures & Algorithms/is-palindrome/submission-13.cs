public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0;
        int r = s.Length - 1;

        while (l < r) {
            if (((s[l] >= 'a' && s[l] <= 'z') ||  // s[l] not valid char
                (s[l] >= 'A' && s[l] <= 'Z') ||
                (s[l] >= '0' && s[l] <= '9')) == false) {
                
                l++;
            }
            else if (((s[r] >= 'a' && s[r] <= 'z') || // s[r] not valid char
                (s[r] >= 'A' && s[r] <= 'Z') ||
                (s[r] >= '0' && s[r] <= '9')) == false) {
                
                r--;
            }
            else { // both s[l] and s[r] are valid chars
                if (char.ToLower(s[l]) != char.ToLower(s[r])) {
                    return false;
                }
                l++;
                r--;
            }
        }
        return true;
    }
}
