import psutil


def get_running_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "exe", "status", "create_time"]
    ):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

        
    return processes

def analyze_process(process):
    reasons = []

    if not process["name"]:
        reasons.append("Missing process name")

    if not process["exe"]:
        reasons.append("Missing executable path")

    if process["status"] != "running":
        reasons.append(f"Process status is {process['status']}")

    return reasons