import numpy as np
import pandas as pd


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
    def type_check(obj) -> bool:
        if obj.isna().any():
            return False
        return True

    @staticmethod
    def type_check_line(obj) -> bool:
        for item in obj:
            if item == '':
                return False
        return True


if __name__ == "__main__":
    print(AttributeChecker.type_check(('', 'abc', 1234)))
