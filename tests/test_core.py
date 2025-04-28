import unittest
from unittest.mock import mock_open, patch
import json
from task_manager import core

class TestTaskManager(unittest.TestCase):

    @patch("task_manager.core.open", new_callable=mock_open, read_data="[]")
    @patch("task_manager.core.json.dump")
    def test_add_task(self, mock_json_dump, mock_file):
        core.add_task("Test Task", 1)
        mock_file.assert_called_with(core.TASKS_FILE, "w")
        self.assertTrue(mock_json_dump.called)

    @patch("task_manager.core.open", new_callable=mock_open, read_data='[{"id": 1, "description": "Test Task", "priority": 1}]')
    @patch("task_manager.core.json.dump")
    def test_delete_task(self, mock_json_dump, mock_file):
        core.delete_task(1)
        mock_file.assert_called_with(core.TASKS_FILE, "w")
        self.assertTrue(mock_json_dump.called)

if __name__ == "__main__":
    unittest.main()
