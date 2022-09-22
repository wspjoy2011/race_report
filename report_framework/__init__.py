"""Report framework works with  f1 race data"""
import os
import sys

from report_framework.get_base_dir import get_base_dir
from report_framework.file_handler import read_data_fromfile

fpath = os.path.join(get_base_dir(), 'report_framework')
sys.path.append(fpath)

from report_framework.report import main as main_report
