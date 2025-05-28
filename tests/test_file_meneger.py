import unittest
from unittest.mock import patch, mock_open
import json
from src.file_manager import FileManeger

sample_vacancy_dict = {
    "id": "123",
    "name": "Python Developer",
    "alternate_url": "http://example.com",
    "salary": {"from": 100000, "to": 150000},
    "snippet": {"requirement": "Python", "responsibility": "Backend development"}
}

class TestFileManager(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_add_file(self, mock_file):
        mgr = FileManeger("test.json")
        mgr.add_file([sample_vacancy_dict])
        mock_file().write.assert_called()

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"123": sample_vacancy_dict}))
    def test_get_data_file(self, mock_file):
        mgr = FileManeger("test.json")
        with patch("json.load", return_value={"123": sample_vacancy_dict}) as mock_json_load:
            data = mgr.get_data_file()
            mock_json_load.assert_called()
            self.assertEqual(data["123"]["name"], "Python Developer")

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"123": sample_vacancy_dict}))
    def test_del_vacancy_id(self, mock_file):
        mgr = FileManeger("test.json")
        with patch("json.load", return_value={"123": sample_vacancy_dict}), \
             patch("json.dump") as mock_json_dump:
            mgr.del_vacancy_id("123")
            mock_json_dump.assert_called()