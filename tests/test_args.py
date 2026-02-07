"""
Test Cases:

1. Everything is correct.
2. Files arg missing.
3. Files - wrong file type.
5. Report arg missing.
6. Report - wrong value.

"""

import pytest
from app.parser import setup_parser

default_err = "usage: pytest [-h] --files FILES [FILES ...] --report {average-gdp}\npytest: error: "


def test_args_success():
    sample_args = ["--files", "test.csv", "--report", "average-gdp"]

    parser = setup_parser()
    args = parser.parse_args(sample_args)

    assert args.files == ["test.csv"]
    assert args.report == "average-gdp"


def test_args_files_missing(capsys):
    sample_args = ["--report", "average-gdp"]

    parser = setup_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(sample_args)

    captured = capsys.readouterr()
    assert (
        captured.err == default_err + "the following arguments are required: --files\n"
    )

    assert excinfo.type is SystemExit


def test_args_files_wrong_file_type(capsys):
    sample_args = ["--files", "test.py", "--report", "average-gdp"]

    parser = setup_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(sample_args)

    captured = capsys.readouterr()
    assert (
        captured.err
        == default_err + "argument --files: argument files must be of type *.csv\n"
    )

    assert excinfo.type is SystemExit


def test_args_report_missing(capsys):
    sample_args = ["--files", "test.csv"]

    parser = setup_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(sample_args)

    captured = capsys.readouterr()
    assert (
        captured.err == default_err + "the following arguments are required: --report\n"
    )

    assert excinfo.type is SystemExit


def test_args_report_wrong_value(capsys):
    sample_args = ["--files", "test.csv", "--report", "wrong-report"]

    parser = setup_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(sample_args)

    captured = capsys.readouterr()
    assert (
        captured.err
        == default_err
        + "argument --report: invalid choice: 'wrong-report' (choose from average-gdp)\n"
    )

    assert excinfo.type is SystemExit
