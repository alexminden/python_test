class Matrix:
    def __init__(self, matrix_string):
            self.matrix = [[int(i) for i in e.split()] for e in matrix_string.split("\n")]
 
    def row(self, index):
        return self.matrix[index - 1]
        
    def column(self, index):
        return [r[index - 1] for r in self.matrix]

matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")