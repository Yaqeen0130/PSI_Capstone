import psutil


def get_running_processes():
    processes = []

    for process in psutil.process_iter(["pid", "name", "username"]):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes