public class Solution {
    public bool IsValid(string s) {
        List<char> left = new List<char> {'{', '[', '('};
        // List<char> right = new List<char> {'}', ']', ')'};

        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> pairs = new Dictionary<char, char>
                {
                    { '}', '{' },
                    { ']', '[' },
                    { ')', '(' }
                };
        
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];

            if (left.Contains(c)) {
                stack.Push(c);
            }
            else {
                if (stack.Count != 0) {
                    char leftMatch = stack.Pop();
                    if (leftMatch != pairs[c]) {
                        return false;
                    }

                } else {
                    return false;
                }
            }
        }
        if (stack.Count != 0) {
            return false;
        }
        return true;

    }
}
