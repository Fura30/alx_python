def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Using str.format() to print integers without casting to strings
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()

# Test case
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
