class testMean() :
    def __init__(self, kind, name, number) :
        self.kind = kind
        self.name = name
        self.number = number
    
        self.user = []
    
    def __eq__(self, other) :
        if not isinstance(other, testMean) :
            return NotImplemented
        return self.kind == other.kind and self.name == other.name and self.number == other.number

    def addUser(self, user, right) :
        self.user.append([user, right])

    def findAdmin(self) :
        for i in self.user :
            if i[1] == 'admin' :
                return i[0]

class listTestMean() :
    def __init__(self, ltestmean = []) :
        self.ltestmean = ltestmean
        self.index = 0
        
    def addTestMean(self, testmean) :
        if testmean not in self.ltestmean :
            self.ltestmean.append(testmean)

    def findNameTestMean(self, kind) :
        l = set()
        for i in self.ltestmean :
            if i.kind == kind :
                l.add(i.nom)
        return sorted(l)

    def findNumTestMean(self, kind, name) :
        l = []
        for i in self.ltestmean :
            if i.kind == kind and i.name == name :
                l.append(str(i.number))
        return sorted(l)

    def findTestMean(self, name, number) :
        try :
            for i in self.ltestmean :
                if i.name == name and i.number == number :
                    return i
        except :
            print('can\'t find that one')

    def listAdmin(self) :
        ladmin = []
        for i in self.ltestmean :
            if i.findAdmin() :
                ladmin.append([i.findAdmin(), i])
        return ladmin

    def __iter__(self) :
        return self
    
    def __next__(self) :
        try :
            value = self.ltestmean[self.index]
            self.index += 1
            return value
        except IndexError :
            raise StopIteration

class attribute() :
    def __init__(self, testmean, lst_att = []) :
        self.testmean = testmean
        self.lst_att = lst_att
    def addAtt(self, att, unity, value) :
        self.lst_att.append([att, unity, value])
    def findAtt(self, att, unity, value) :
        for i in self.lst_att :
            if i[0] == att and i[1] == unity and i[2] == value :
                return i
    def delAtt(self, att, unity, value) :
        l = self.findAtt(att, unity, value)
        if l :
            self.lst_att.pop(self.lst_att.index(l))
        

class param() :
    def __init__(self, testmean, lst_param = []) :
        self.testmean = testmean
        self.lst_param = lst_param
    def addParam(self, param, unity) :
        self.lst_param.append([param, unity])
    def findParam(self, param, unity) :
        for i in self.lst_param :
            if i[0] == param and i[1] == unity :
                return i
    def delParam(self, param, unity) :
        l = self.findParam(param, unity)
        if l :
            self.lst_param.pop(self.lst_param.index(l))