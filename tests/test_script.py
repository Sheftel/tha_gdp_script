"""
Test Cases

1. Returns correct data
2. One of the files doesn't exist
3. Invalid report value
"""
import pytest

from main import run as script_run


def test_script_success(capsys):
    sample_files = ["test.csv"]
    sample_report = "average-gdp"
    script_run(sample_files, sample_report)
    captured = capsys.readouterr()
    assert captured.out == """+----+---------------+----------+
|    | country       |      gdp |
+====+===============+==========+
|  1 | United States | 23923.67 |
+----+---------------+----------+
|  2 | China         | 17810.33 |
+----+---------------+----------+
"""


def test_script_file_doesnt_exist(capsys):
    sample_files = ["no_test.csv", "test.csv"]
    sample_report = "average-gdp"

    script_run(sample_files, sample_report)
    captured = capsys.readouterr()


    assert captured.out == "File [Errno 2] No such file or directory: 'no_test.csv' not found\n"


def test_script_report_doesnt_exist(capsys):
    sample_files = ["test.csv"]
    sample_report = "wrong-report"

    script_run(sample_files, sample_report)
    captured = capsys.readouterr()


    assert captured.out == "Report 'wrong-report' not available\n"
