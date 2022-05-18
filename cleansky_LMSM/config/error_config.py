class BaseError(Exception):
    """Base Exception"""
    def __init__(self):
        self.expression = None


class DmlError(BaseError):
    def __init__(self):
        pass


class DqlError(BaseError):
    def __init__(self):
        pass


class TclError(BaseError):
    def __init__(self, sql: str):
        self.expression = sql
