import sys

# number = sys.argv[1]
# print(number)

if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) % 2 ==0:
    print ('Error: Wrong usage\nUsage: python section2.py and any ODD (to define starting coordinate) NUMBER')  
    sys.exit()

def generate_matrix(N):
    if N <= 0:
        return []
    
    matrix = [[0] * N for _ in range(N)] #declaration of zero matrix
    center = N // 2 #defining of starting coordinate for 1 in case input is 5 it should be 2,2
    x, y = center, center
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #up,right,down,left movement coordinates

    current_dir = 0
    temp = 1
    steps = 1
    matrix[x][y] = temp #giving 1 to the center point
    temp = 2
    
    while temp <= N * N:
        for _ in range(2):  # direction should  be changed twice  for every step that's why range(2) was used
            x1, y1 = directions[current_dir]
            for _ in range(steps):
                x += x1
                y += y1
                if 0 <= x < N and 0 <= y < N:
                    matrix[x][y] = temp
                    temp += 1
            current_dir = (current_dir + 1) % 4
        steps += 1
    
    return matrix

def calculate_sum(matrix):
    N = len(matrix)
    primary_diagonal = sum(matrix[i][i] for i in range(N))
    secondary_diagonal = sum(matrix[i][N-1-i] for i in range(N))
    return primary_diagonal, secondary_diagonal 

N = int(sys.argv[1])  #we get the size of matrix in case n=5 matrix should be 5,5 quadratic matrix
matrix = generate_matrix(N)
for i in matrix:
    print(i)

primary_sum, secondary_sum = calculate_sum(matrix)
print(f"Primary diagonal: {primary_sum}")
print(f"Secondary diagonal: {secondary_sum}")