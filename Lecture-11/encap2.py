class employee():
    def __init__(self):
        self.maxearn = 50000

    def earn(self):
        print('earning is {}'.format(self.__maxearn))

    def setmaxearn(self, earn):
        self.maxearn = earn

emp1 = employee()
emp1.earn()

emp1.__maxearn = 100000
emp1.earn()

emp1.setmaxearn(100000)
emp1.earn()