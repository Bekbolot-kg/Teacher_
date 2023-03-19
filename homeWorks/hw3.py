class Bank:
    def __init__(self, name, balanse):
        self._balanse = balanse
        self._name = name
    def maneyX(self):
        add = float(input('Введите сумму, которую нужно добавить на счет: '))
        self._balanse = self._balanse + add
        print("Новый баланс:", self._balanse)

    def __str__(self):
        return f'{self._name} - {self._balanse}'

    def _kill(self):
        self._balanse = 0
        print("Новый баланс:", self._balanse)
    def __jackpot(self):
        self._balanse = self._balanse * 10
        print("Поздравляем! Ваш баланс:", self._balanse)

    def _OneTwo(self, other):
        self._balanse = self._balanse + other._balanse



class BankTwo(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    def get_balanse(self):
        return self._balanse

    def set_balanse(self, balanse):
        self._balanse = balanse


class BankTree(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)
    @property
    def balanse(self):
        return self._balanse

    @balanse.setter
    def balanse(self, num):
        self._balanse = num

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

bekbolot = BankTwo('Bekbolot', 5000)

print(bekbolot.get_name())
print(bekbolot.get_balanse())


bekbolot.set_name("Nur")
bekbolot.set_balanse(2000)
print(bekbolot.get_name())
print(bekbolot.get_balanse())


print(bekbolot._name)
print(bekbolot._balanse)
bekbolot.name = "Bek"
bekbolot._balanse = 10000
print(bekbolot.name)
print(bekbolot._balanse)






# nurbek = Bank('Nurbek', 10000)
#
# bekbolot._OneTwo(nurbek)
#
# print(bekbolot)
# print(nurbek)