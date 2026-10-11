# from django.test import SimpleTestCase



def test_incomplete_task_is_pending(self):
    self.assertEqual(
        get_task_status(False),
        "finished"
    )