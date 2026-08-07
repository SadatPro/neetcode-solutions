class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2) :
            return False

        s1_count = [0]*26
        s2_count = [0]*26
        window_size = len(s1)

        for i in range(window_size):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == s2_count:
            return True

        left = 0

        for right in range(window_size,len(s2)):
            new_charecter_index = ord(s2[right]) - ord('a')
            s2_count[new_charecter_index] += 1

            left_charecter_remove = ord(s2[left]) - ord('a')
            s2_count[left_charecter_remove] -= 1

            left += 1
            
            if s1_count == s2_count:
                return True
        return False
