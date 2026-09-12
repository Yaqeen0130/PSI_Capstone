from processes import get_running_processes, analyze_process


def main():
    processes = get_running_processes()

    print(f"Found {len(processes)} running processes.")

    for process in processes:
        risk, reasons = analyze_process(process)

        if risk == "REVIEW":
            print(process)
            print(f"  Risk: {risk}")
            print(f"  Reasons: {', '.join(reasons)}")


if __name__ == "__main__":
    main()