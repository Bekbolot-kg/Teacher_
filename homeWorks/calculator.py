class Calkulator_2num:
    def init(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def truediv(self):
        return self.num1 / self.num2


class Calkulator_Xnum:
    def init(self, *num):
        self.num = num

    def add(self):
        a = 0
        for i in self.num:
            a += i
        return a
    def sub(self):
        a = self.num[0]
        for i in self.num[1:]:
            a -= i

        return a

    def mul(self):
        a = 1
        for i in self.num:
            a *= i
        return a

    def truediv(self):
        a = 1

        for i in self.num:
            if i != 0:
                a /= i
            else:
                return 'Нельзя делить на 0'
        return a

a = Calkulator_Xnum(1, 3, 5, 0)
print(a.sub())

a = Calkulator_2num(1 , 3)
print(a.sub())