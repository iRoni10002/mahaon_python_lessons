import random

class Qadro_matrix:

    value = list(list())
    count = 0
    size = 0
    def __init__(self, flag_, size_):
        self.size = size_
        Qadro_matrix.count += 1
        self.value = Add_matrix(flag_, size_)

    def Get(self):
        return self.size, Qadro_matrix.count

    def __str__(self, size):
        for i in range(size):
            str1 = str()
            for j in range(size):
                str1 += str(self.value[i][j])
                str1 += " "
            print(str1)

    def Transponirovanie(self, size):
        for i in range(size):
            str1 = str()
            for j in range(size):
                str1 += str(self.value[j][i])
                str1 += " "
            print(str1)

    def Sum_of_main_diagonal(self, size):
        sum = int()
        for i in range(size):
            for j in range(size):
                if i == j:
                    sum += self.value[i][j]
        return sum

    def __lt__(self, other, size_self, size_other):
        sum_self = int()
        sum_other = int()

        for i in range(size_self):
            for j in range(size_self):
                sum_self += self.value[i][j]
        print(sum_self)
        for i in range(size_other):
            for j in range(size_other):
                sum_other += other.value[i][j]
        print(sum_other)
        if sum_self < sum_other:
            return True
        else:
            return False

    def __qe__(self, other, size_self, size_other):
        sum_self = int()
        sum_other = int()

        for i in range(size_self):
            for j in range(size_self):
                sum_self += self.value[i][j]\

        for i in range(size_other):
            for j in range(size_other):
                sum_other += other.value[i][j]

        if sum_self == sum_other:
            return True
        else:
            return False

    def __gt__(self, other, size_self, size_other):
        sum_self = int()
        sum_other = int()

        for i in range(size_self):
            for j in range(size_self):
                sum_self += self.value[i][j]\

        for i in range(size_other):
            for j in range(size_other):
                sum_other += other.value[i][j]

        if sum_self > sum_other:
            return True
        else:
            return False

    def __add__(self, other):
        if self.size == other.size:
            TV = Qadro_matrix(1, self.size)
            for i in range(other.size):
                for j in range(other.size):
                    TV.value[i][j] = self.value[i][j] + other.value[i][j]
            print(TV.__str__(TV.size))
        else:
            print("Error")
# функция создания матрцы
def Add_matrix(flag, size):

    if flag == 1:   # автосоздание
        width = int(input("width of random: "))
        Arr = [[random.randint(0, width)] * size for i in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                Arr[i][j] = random.randint(0, width)
        return Arr
    elif flag == 2:   # задание матрицы вручную
        Arr = [[0] * size for i in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                Arr[i][j] = int(input())
        return Arr
    else:
        print("invalid value, error")

cl2 = Qadro_matrix(1, 2)
CH4 = Qadro_matrix(1, 2)

print(cl2.Get())

print(cl2.__str__(cl2.size))
print(CH4.__str__(CH4.size))

print(cl2.Transponirovanie(cl2.size))

print(cl2.Sum_of_main_diagonal(cl2.size))

print(cl2.__lt__(CH4, cl2.size, CH4.size))

cl2.__add__(CH4)
