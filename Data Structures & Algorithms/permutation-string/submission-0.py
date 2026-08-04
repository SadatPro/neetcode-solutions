class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer, it's impossible
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase letters
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Count characters of s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # If the first window is already a permutation
        if s1Count == s2Count:
            return True

        # Left pointer of the sliding window
        left = 0

        # Right pointer starts after the first window
        for right in range(len(s1), len(s2)):

            # Add the new character entering the window
            s2Count[ord(s2[right]) - ord('a')] += 1

            # Remove the leftmost character leaving the window
            s2Count[ord(s2[left]) - ord('a')] -= 1

            # Move the window forward
            left += 1

            # Compare frequency arrays
            if s1Count == s2Count:
                return True

        return False