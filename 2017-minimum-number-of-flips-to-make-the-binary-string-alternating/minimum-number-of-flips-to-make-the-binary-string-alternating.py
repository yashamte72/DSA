class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s
        # We'll compare ss[i] to expected chars for two patterns:
        # pattern1: starts with '0' -> "0101..."
        # pattern2: starts with '1' -> "1010..."
        diff1 = diff2 = 0
        ans = n  # upper bound

        for i, ch in enumerate(ss):
            # expected chars at position i for the two patterns:
            expected1 = '0' if (i % 2 == 0) else '1'
            expected2 = '1' if (i % 2 == 0) else '0'

            if ch != expected1:
                diff1 += 1
            if ch != expected2:
                diff2 += 1

            # once window size exceeds n, remove effect of ss[i-n]
            if i >= n:
                left = ss[i - n]
                left_expected1 = '0' if ((i - n) % 2 == 0) else '1'
                left_expected2 = '1' if ((i - n) % 2 == 0) else '0'
                if left != left_expected1:
                    diff1 -= 1
                if left != left_expected2:
                    diff2 -= 1

            # when we've processed a full window of length n, consider answer
            if i >= n - 1:
                ans = min(ans, diff1, diff2)

        return ans