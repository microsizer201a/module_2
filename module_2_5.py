def get_matrix(n, m, value):
    matrix = list()
    for i in range(n):
        k = list()
        for j in range(m):
            if value >= 0:
                k.append(None)
            else:
                k.append(value)
        matrix.append(k)
    return matrix
print(get_matrix(4, 2, 0))