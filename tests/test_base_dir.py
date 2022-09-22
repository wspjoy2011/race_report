"""
Tests for get_base_dir
"""
import pytest
import os

from report_framework.get_base_dir import get_base_dir


class TestFileHandler:
    """Tests for get_base_dir"""

    def setup(self):
        self.func = get_base_dir

    def test_get_project_dir(self):
        assert 'report_framework' in os.listdir(self.func())

    def test_get_project_dir_wrong(self):
        assert '__framework__' not in os.listdir(self.func())

