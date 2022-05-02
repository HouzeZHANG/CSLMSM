import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.view as view
import cleansky_LMSM.common.controller as controller
import cleansky_LMSM.common.person as person
import cleansky_LMSM.common.model as model
import cleansky_LMSM.db_init.pg_db_initial as pg_db_initial

import unittest as ut
import pytest

# 初始化数据库
import cleansky_LMSM.db_init.pg_db_initial

db_test_object = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
db_test_object.connect()
