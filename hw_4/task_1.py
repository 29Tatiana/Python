#Напишите функцию для транспонирования матрицы

def print_matrix(m):
    for item in m:
        print(item)


def trans_matrix(matrix):
    temp = []
    for i in range(len(matrix[0])):
        temp_col = []
        for j in range(len(matrix)):
            temp_col.append(matrix[j][i])
        temp.append(temp_col)
    return temp


matrix = [[5,4,3],
          [3,4,5],
          [10,9,6]]
print_matrix(trans_matrix(matrix))