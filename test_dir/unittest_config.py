"""
因为每一个单元测试基本都需要使用如下组件，为了避免重复，统一在本模块下进行配置
"""

import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.view as view
import cleansky_LMSM.common.controller as controller
import cleansky_LMSM.common.person as person
import cleansky_LMSM.common.model as model

import unittest as ut
import pytest

db_test_object = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
db_test_object.connect()
