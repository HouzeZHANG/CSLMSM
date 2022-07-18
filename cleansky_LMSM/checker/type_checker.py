import re
from collections import Iterable


class Checker:
    def __init__(self):
        pass

    @staticmethod
    def type_check(obj) -> bool:
        pass


class AttributeChecker(Checker):
    """attribute数据合法性检查器"""

    @staticmethod
    def type_check(obj) -> bool:
        # 三元数据以可迭代对象传入
        if obj[0] == '':
            # attribute不能为空字符串
            return False

        return True


class TestMeanChecker(Checker):
    """Mean对象数据合法性检查"""

    @staticmethod
    def type_check(obj) -> bool:
        for item in obj:
            if item == '' or item is None:
                return False

        return True


class PosOnTankChecker(Checker):
    @staticmethod
    def type_check(obj) -> tuple:
        if len(obj) != 14:
            return False, "LENGTH: " + str(len(obj)) + "!=14"

        # if re.search(r'.+\-.+', obj[1]) is None:
        #     return False, obj[1]
        if len(obj[1]) > 20:
            return False, "LENGTH OF LOCATION STRING: " + str(len(obj[1])) + ">20"

        for i in range(2, 14):
            n = str(obj[i])
            if re.search(r'^(-?\d+)([.]\d+)?$', n) is None:
                print(n)
                return False, n

        return True, ""

    @staticmethod
    def type_check_line(obj) -> bool:
        for item in obj:
            if item == '':
                return False
        return True


class AttributeTupleChecker(Checker):
    @staticmethod
    def type_check(obj: tuple) -> tuple:
        if len(obj) != 3:
            return False, "ERROR\nATTRIBUTE LEN IS :" + str(len(obj))

        attribute_value = obj[1]
        if re.search(r'^(-?\d+)([.]\d+)?$', attribute_value) is None:
            return False, "SYNTAX ERROR\n" + attribute_value

        if len(attribute_value) > 20:
            return False, "SYNTAX ERROR\n" + attribute_value + " has more than 20 characters"

        return True, ""


class VarcharSyntaxChecker(Checker):
    @staticmethod
    def type_check(obj) -> tuple:
        if isinstance(obj, Iterable):
            for item in obj:
                if len(item)>20:
                    return False, "SYNTAX ERROR\n" + item + " has more than 20 characters"
            return True, ""

        if len(obj) > 20:
            return False, "SYNTAX ERROR\n" + obj + " has more than 20 characters"
        return True, ""
