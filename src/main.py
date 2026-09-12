from src.logic import get_running_processes, analyze_process
from src.utils import write_report

def main():
    processes = get_running_processes()

    report_lines = []
    report_lines.append(f"Found {len(processes)} running processes.\n")

    for process in processes:
        risk, reasons = analyze_process(process)

        if risk == "REVIEW":
            report_lines.append(f"Process: {process.get('name')}")
            report_lines.append(f"PID: {process.get('pid')}")
            report_lines.append(f"Risk: {risk}")
            report_lines.append(f"Reasons: {', '.join(reasons)}")
            report_lines.append("")

    write_report(
        report_lines,
        "reports/process_report.txt"
    )

    print("Report created: reports/process_report.txt")


if __name__ == "__main__":
    main()