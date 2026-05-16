class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count    = {}
        L        = 0
        max_freq = 0
        longest  = 0

        for R in range(len(s)):

            # Step 1: add new char to frequency map
            count[s[R]] = count.get(s[R], 0) + 1

            # Step 2: update max frequency
            max_freq = max(max_freq, count[s[R]])

            # Step 3: shrink if window invalid
            while (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1

            # Step 4: update longest
            longest = max(longest, R - L + 1)

        return longest