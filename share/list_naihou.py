a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in a]
print(squares)
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [x for row in matrix for x in row]
print(flat)
squared = [[x ** 2 for x in row] for row in matrix]
print(squared)
squared = [x ** 2 for row in matrix for x in row]
print(squared)
