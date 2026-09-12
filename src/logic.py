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

    name = process.get("name") or ""
    exe = process.get("exe") or ""
    status = process.get("status") or ""

    if not name:
        reasons.append("Missing process name")

    if status != "running":
        reasons.append(f"Process status is {status}")

    suspicious_locations = [
        "\\AppData\\Local\\Temp\\",
        "\\Windows\\Temp\\",
    ]

    for location in suspicious_locations:
        if location.lower() in exe.lower():
            reasons.append("Executable is running from a temporary folder")
            break

    if reasons:
        risk = "REVIEW"
    else:
        risk = "NORMAL"

    return risk, reasons