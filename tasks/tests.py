
from django.test import SimpleTestCase
from .utils import get_task_status


class TaskStatusTests(SimpleTestCase):

    def test_incomplete_task_is_pending(self):
        self.assertEqual(
            get_task_status(False),
            "pending"
        )

    def test_completed_task_is_completed(self):
        self.assertEqual(
            get_task_status(True),
            "completed"
        )
