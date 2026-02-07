import argparse
from tabulate import tabulate

from reports import average_gdp
from utils import read_csv, csvfile

report_choices = {
    "average-gdp": average_gdp,
}


def run(files, report):
    csv_data = read_csv(files)
    report_data, index_range = report_choices[report](csv_data)
    output = tabulate(
        report_data,
        headers="keys",
        showindex=index_range,
        tablefmt="grid",
        floatfmt=".2f",
    )
    print(output)


parser = argparse.ArgumentParser(description="Macroeconomic reports")
parser.add_argument("--files", nargs="+", type=csvfile, help="Input files")
parser.add_argument(
    "--report", type=str, help="Report type", choices=report_choices.keys()
)
args = parser.parse_args()

run(args.files, args.report)
