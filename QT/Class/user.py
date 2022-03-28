class user():
    def __init__(self, uname, fname, lname, orga, tel, email, password=''):
        """ @param :
            information of user
        """
        self.uname = uname
        self.fname = fname
        self.lname = lname
        self.orga = orga
        self.tel = tel
        self.email = email
        self.password = password
        """@param :
            right list of user
        """
        self.right = []

    """ @function :
        check if 2 user are the same
    """

    def __eq__(self, other):
        if not isinstance(other, user):
            return NotImplemented
        return self.uname == other.uname

    """ @function :
        user is allowed to change his password
    """

    def changePassword(self, value):
        self.password = value

    """ @function :
        add right for user
    """

    def addRight(self, kind, name, number, right):
        self.right.append([kind, name, number, right])
        # object.addUser(self, right)


class listUser():
    def __init__(self, luser=[]):
        self.luser = luser
        self.index = 0

    """ @function :
        add user to the list
    """

    def addUser(self, user):
        if user in self.luser:
            # print('{} {} is already in this list'.format(user.fname, user.lname))
            return
        self.luser.append(user)

    """ @function :
        delete user from the list
    """

    def delUser(self, user):
        if user not in self.luser:
            return
        self.luser.pop(self.luser.index(user))

    """ @function :
      return found user from the list
    """

    def findUser(self, value):
        try:
            for i in self.luser:
                if i.uname == value:
                    return i
        except:
            print('can\'t find that one')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self.luser[self.index]
            self.index += 1
            return value
        except IndexError:
            raise StopIteration
