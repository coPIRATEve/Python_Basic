class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += "\t".join(map(str, row)) + "\n"
        return result

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должный быть одинаковыми")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должный быть одинаковыми")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Кол-во строк одной матрицы должно совпадать с кол-вом столбиков другой")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
