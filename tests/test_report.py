"""
Tests for report module
"""
import pytest
import os

from report_framework import file_handler
from report_framework.report import main as main_report
import report_framework.file_handler
print(report_framework.file_handler.__file__)


class TestMainReport:
    """Tests for report module"""

    def setup(self):
        self.func = main_report
        self.path_ta_data = os.path.join(os.getcwd(), 'racing_data')

    def test_with_racing_data(self):
        race_results, abbr_data = self.func(self.path_ta_data)
        assert 'BHS' in race_results
        assert 'BHS' in abbr_data

    def test_with_wrong_contains(self):
        race_results, abbr_data = self.func(self.path_ta_data)
        assert 'BHS!' not in race_results
        assert 'BHS!' not in abbr_data


