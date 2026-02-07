import argparse

from app.settings import report_choices


def setup_parser():
    parser = argparse.ArgumentParser(description="Macroeconomic reports")
    parser.add_argument(
        "--files", nargs="+", type=csvfile, help="Input files", required=True
    )
    parser.add_argument(
        "--report",
        type=str,
        help="Report type",
        choices=report_choices.keys(),
        required=True,
    )

    return parser


def csvfile(value: str):
    if not value.endswith(".csv"):
        raise argparse.ArgumentTypeError("argument files must be of type *.csv")
    return value
