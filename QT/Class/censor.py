import collections


class typeSensor():
    def __init__(self, ref):
        self.ref = ref
        self.user = []

    def addUser(self, user, right):
        self.user.append([user, right])


class listSensor():
    def __init__(self, lsensor={}):
        self.lsensor = lsensor
        self.lsensor = collections.defaultdict(list)
        self.index = 0

    def addSensor(self, sensor, num):
        self.lsensor[sensor] += [num]

    def delSensor(self, sensor, num):
        self.lsensor[sensor].pop(self.lsensor[sensor].index(num))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            y = list(self.lsensor.keys())[self.index]
            value = self.lsensor[y]
            self.index += 1
            return value
        except IndexError:
            raise StopIteration
