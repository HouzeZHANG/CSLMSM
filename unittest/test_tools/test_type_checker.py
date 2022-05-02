from unittest.unittest_config import *
import cleansky_LMSM.tools.type_checker as tc


class TestTypeChecker:
    def test_attribute_checker(self):
        assert tc.AttributeChecker.type_check(('1', None, 2)) is False
