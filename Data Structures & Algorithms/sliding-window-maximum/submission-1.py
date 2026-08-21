class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        window = deque()
        result = []

        for right in range(len(nums)):

            while window and nums[window[-1]] <= nums[right]:
                window.pop()

            window.append(right)

            left = right - k + 1

            if window[0] < left:
                window.popleft()

            if right >= k - 1:
                result.append(nums[window[0]])

        return result