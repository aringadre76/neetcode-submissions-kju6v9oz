public class Solution {
    public bool IsValid(string s) {
        var left = new List<char> { '(', '[', '{' };

        var pairs = new Dictionary<char, char>
        {
            { ')', '(' },
            { ']', '[' },
            { '}', '{' }
        };

        Stack<char> stack = new Stack<char>();


        for (int i = 0; i < s.Length; i++) {
            char c = s[i];

            if (left.Contains(c) == true) { // current char is left bracket
                stack.Push(c);
            } else { // current char is right bracket
                if (stack.Count != 0) {
                    char popped = stack.Pop();
                    if (popped != pairs[c]) {
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
