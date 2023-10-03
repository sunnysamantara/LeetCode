class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        triangle = [[1]]

        for i in range(1, numRows):
            current_row = [1]

            for j in range(1, i):
                current_element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                current_row.append(current_element)

            current_row.append(1)
            triangle.append(current_row)

        return triangle
