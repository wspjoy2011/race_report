"""
Tests for file_handler module
"""
import pytest
import os

from report_framework.get_base_dir import get_base_dir
from report_framework.file_handler import read_data_fromfile


class TestFileHandler:
    """Tests for file_handler module"""

    def setup(self):
        self.func = read_data_fromfile
        self.path_to_file_abbr = os.path.join(get_base_dir(), 'racing_data', 'abbreviations.txt')
        self.path_to_file_start = os.path.join(get_base_dir(), 'racing_data', 'start.log')
        self.path_to_file_end = os.path.join(get_base_dir(), 'racing_data', 'end.log')
        self.path_to_file_wrong = os.path.join(get_base_dir(), 'WrongData.txt')

    def test_with_abbreviations(self):
        data = self.func(self.path_to_file_abbr)
        assert 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER' in data

    def test_with_start(self):
        data = self.func(self.path_to_file_start)
        assert 'SVF2018-05-24_12:02:58.917' in data

    def test_with_end(self):
        data = self.func(self.path_to_file_end)
        assert 'MES2018-05-24_12:05:58.778' in data

    def test_with_abbreviations_wrong_data(self):
        data = self.func(self.path_to_file_abbr)
        assert 'wRonG!' not in data

    def test_with_wrong_directory(self):
        with pytest.raises(FileNotFoundError) as error:
            self.func(self.path_to_file_wrong)
        assert 'No such file or directory' in str(error.value)


