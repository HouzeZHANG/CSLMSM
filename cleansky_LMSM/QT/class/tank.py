class position() :
    def __init__(self, tank, position = []) :
        self.position = position
        self.tank = tank
    def addPos(self, loc, ref, x, y, z, ui, uj, uk, vi, vj, vk, ni, nj, nk) :
        self.position.append([loc, ref, x, y, z, ui, uj, uk, vi, vj, vk, ni, nj, nk])
    def findPos(self, loc) :
        for i in self.position :
            if i[0] == loc :
                return i
    def delPos(self, loc) :
        l = self.findPos(loc)
        if l :
            self.position.pop(self.position.index(l))
