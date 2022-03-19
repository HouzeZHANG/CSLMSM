from test_dir.unittest_config import *


class TestManagementView:
    def test_run_test_view(self):
        management_view = view.ManagementView()
        management_view.run_test_view()

    def test_setup_ui(self):
        management_controller = controller.ManagementController(db_object=db_test_object)
        management_controller.run_view()


if __name__ == '__main__':
    test_object = TestManagementView()
    # test_object.test_run_test_view()
    test_object.test_setup_ui()
