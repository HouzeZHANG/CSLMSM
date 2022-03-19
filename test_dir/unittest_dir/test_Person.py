from test_dir.unittest_config import *


class TestPerson(ut.TestCase):
    def test_person_constructor(self):
        my_person = person.Person()
        assert my_person.get_name() is None

    def test_person_constructor_not_none(self):
        my_person2 = person.Person('Tom')
        assert my_person2.get_name() == 'Tom'

    def test_other_class_constructor(self):
        my_person = person.Person()
        my_visitor = person.Visitor(my_person.get_name())
        assert my_visitor.get_name() is None


if __name__ == '__main__':
    obj = TestPerson()
    # obj.test_person_constructor()
    # obj.test_person_constructor_not_none()
    # obj.test_other_class_constructor()
