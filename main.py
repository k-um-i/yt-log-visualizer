from parser import parse_log
from visualizer import render_overview


def main():
    log_data = parse_log("immersion_logs_269066190796750848.csv")
    render_overview(log_data)


if __name__ == "__main__":
    main()
