class carateristic() :
    def __init__(self, coating, carac = []) :
        self.carac = carac
        self.coating = coating
    def addCarac(self, carac, unity, value) :
        self.carac.append([carac, unity, value])
    def findCarac(self, carac, unity, value) :
        for i in self.carac :
            if i[0] == carac and i[1] == unity and i[2] == value :
                return i
    def delCarac(self, carac, unity, value) :
        l = self.findCarac(carac, unity, value)
        if l :
            self.carac.pop(self.carac.index(l))
