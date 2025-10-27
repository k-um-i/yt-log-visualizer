import argparse
from parser import parse_log
from visualizer import render_overview


def main():
    parser = argparse.ArgumentParser(
        description="Generate Youtube log overview from CSV."
    )
    parser.add_argument("csv_file", help="Path to the CSV file to parse.")
    parser.add_argument(
        "-o", "--output", help="Specify output file path.", default="overview.html"
    )

    args = parser.parse_args()

    log_data = parse_log(args.csv_file)
    render_overview(log_data, output_file=args.output)


if __name__ == "__main__":
    main()
