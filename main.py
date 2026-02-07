from typing import List

from tabulate import tabulate

from app.settings import report_choices
from app.utils import read_csv
from app.parser import setup_parser


def run(files: List[str], report: str):
    try:
        csv_data = read_csv(files)
    except FileNotFoundError as e:
        print(f"File {e} not found")
        return

    try:
        report_data, index_range = report_choices[report](csv_data)
    except KeyError as e:
        print(f"Report {e} not available")
        return

    output = tabulate(
        report_data,
        headers="keys",
        showindex=index_range,
        tablefmt="grid",
        floatfmt=".2f",
    )
    print(output)


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    run(args.files, args.report)
