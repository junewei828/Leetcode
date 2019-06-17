class Solution:
    def maxArea(height):
        head = 0
        tail = len(height)-1
        water = 0

        i = 0
        while i < len(height):
            i += 1
            width = abs(head - tail)

            if height[head] < height[tail]:
                vol = width * height[head]
                head += 1

            else:
                vol = width * height[tail]
                tail -= 1

            if water < vol:
                water = vol

        return water

    list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(list))
