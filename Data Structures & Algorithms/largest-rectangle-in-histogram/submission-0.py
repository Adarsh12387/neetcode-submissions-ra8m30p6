class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for i in range(len(heights)):
            # FIX 1 + 2: use while and correct comparison
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                # FIX 3: correct width calculation
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                maxarea = max(maxarea, h * w)

            stack.append(i)

        # FIX 4: correct cleanup loop
        while stack:
            h = heights[stack.pop()]

            if not stack:
                w = len(heights)
            else:
                w = len(heights) - stack[-1] - 1

            maxarea = max(maxarea, h * w)

        return maxarea