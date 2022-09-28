"""
Tests for cli_report
"""
import pytest
import os

from report_framework.cli_report import main as main_cli


class TestCliMain:
    """Tests for file_handler module"""

    def setup(self):
        self.func = main_cli
        self.path_to_files = os.path.join(os.getcwd(), 'racing_data')
        self.path_to_files_wrong = os.path.join(os.getcwd(), 'racing_data_wrong')

    # Positive tests
    def test_main_cli_with_folder_arg(self, capfd):
        first = '| 1  |  Sebastian Vettel |          FERRARI          | 0:01:04.415000 |'
        self.func(self.path_to_files)
        captured = capfd.readouterr()
        assert first in captured.out

    def test_main_cli_with_folder_asc_args(self, capfd):
        first = '| 1  |  Sebastian Vettel |          FERRARI          | 0:01:04.415000 |'
        self.func(self.path_to_files, True, False, '')
        captured = capfd.readouterr()
        assert first in captured.out

    def test_main_cli_with_folder_desc_args(self, capfd):
        first = '| 1  |   Lewis Hamilton  |          MERCEDES         | 0:06:47.540000 |'
        self.func(self.path_to_files, False, True, '')
        captured = capfd.readouterr()
        assert first in captured.out

    def test_main_cli_with_folder_asc_driver_args(self, capfd):
        first = '| 19 | Lewis Hamilton | MERCEDES | 0:06:47.540000 |'
        self.func(self.path_to_files, True, False, 'Lewis Hamilton')
        captured = capfd.readouterr()
        assert first in captured.out

    def test_main_cli_with_folder_desc_driver_args(self, capfd):
        first = '| 1 | Lewis Hamilton | MERCEDES | 0:06:47.540000 |'
        self.func(self.path_to_files, False, True, 'Lewis Hamilton')
        captured = capfd.readouterr()
        assert first in captured.out

    # Negative tests
    def test_with_wrong_folder_path(self, capfd):
        data = self.func(self.path_to_files_wrong, False, False, '')
        captured = capfd.readouterr()
        assert 'No such file or directory' in captured.out

    def test_with_asc_desc_args(self, capfd):
        self.func(self.path_to_files, True, True, '')
        answer = 'Cannot use two options together: --asc --desc'
        captured = capfd.readouterr()
        assert answer in captured.out

    def test_with_wrong_driver(self, capfd):
        self.func(self.path_to_files, False, False, 'Joker')
        answer = 'Driver not found'
        captured = capfd.readouterr()
        assert answer in captured.out


