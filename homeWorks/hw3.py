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

bekbolot = Bank('Bekbolot', 5000)
nurbek = Bank('Nurbek', 10000)

bekbolot._OneTwo(nurbek)

print(bekbolot)
print(nurbek)