
n = int(input("Enter the size of the matrix: "))

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
