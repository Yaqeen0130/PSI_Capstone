from processes import get_running_processes, analyze_process


def main():
    processes = get_running_processes()

    print(f"Found {len(processes)} running processes.")

    for process in processes[:10]:
        reasons = analyze_process(process)

        print(process)

        if reasons:
            print("  Review:", ", ".join(reasons))
            
if __name__ == "__main__":
    main()