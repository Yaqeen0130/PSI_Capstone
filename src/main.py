from processes import get_running_processes


def main():
    processes = get_running_processes()

    print(f"Found {len(processes)} running processes.")

    for process in processes[:10]:
        print(process)


if __name__ == "__main__":
    main()