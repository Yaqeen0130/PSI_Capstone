from processes import get_running_processes, analyze_process


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

    with open("reports/process_report.txt", "w") as report_file:
        report_file.write("\n".join(report_lines))

    print("Report created: reports/process_report.txt")

if __name__ == "__main__":
    main()