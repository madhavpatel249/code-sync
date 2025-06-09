class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
            row.reverse()  # Flip the row horizontally
            for i in range(len(row)):
                row[i] = 1 - row[i]  # Invert the elements (0 -> 1, 1 -> 0)
        
        return image