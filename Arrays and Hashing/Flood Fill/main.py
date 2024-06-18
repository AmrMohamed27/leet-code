class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        prevColor = image[sr][sc]
        def recur(sr, sc):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != prevColor:
                return
            image[sr][sc] = color
            recur(sr + 1, sc)
            recur(sr - 1, sc)
            recur(sr, sc + 1)
            recur(sr, sc - 1)
        if prevColor != color:
            recur(sr, sc)
        return image
s = Solution()
image, sr, sc, color = [[1,1,1],[1,1,0],[1,0,1]], 1,  1, 2
print(s.floodFill(image, sr, sc, color))

