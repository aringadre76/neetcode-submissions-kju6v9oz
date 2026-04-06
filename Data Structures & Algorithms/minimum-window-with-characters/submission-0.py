class Solution:
    def minWindow(self, s: str, t: str) -> str:
        starting_size = len(t)

        if len(s) < len(t):
            return ""

        from collections import Counter
        t_count = Counter(t)  # Frequency map of characters in t

        while starting_size <= len(s):
            l, r = 0, starting_size

            while r <= len(s):
                # Check the current substring
                window = s[l:r]

                # Create a frequency map of the window
                window_count = Counter(window)

                # Check if the window contains all characters of t with correct frequencies
                if all(window_count[char] >= t_count[char] for char in t_count):
                    return window

                l += 1
                r += 1

            # Increment the size of the window
            starting_size += 1

        return ""
