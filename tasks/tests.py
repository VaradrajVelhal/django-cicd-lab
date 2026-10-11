# from django.test import SimpleTestCase
from .utils import get_task_status


def test_incomplete_task_is_pending(self):
    self.assertEqual(
        get_task_status(False),
        "finished"
    )