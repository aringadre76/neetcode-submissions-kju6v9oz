from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize pointers for the sliding window and other variables
        left = 0
        max_count = 0
        max_length = 0
        char_count = Counter()

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            char_count[s[right]] += 1
            # Update max_count to the most frequent character count in the current window
            max_count = max(max_count, char_count[s[right]])

            # Check if the current window is valid
            if (right - left + 1) - max_count > k:
                # Shrink the window from the left
                char_count[s[left]] -= 1
                left += 1

            # Update the max_length of the valid window
            max_length = max(max_length, right - left + 1)

        return max_length
