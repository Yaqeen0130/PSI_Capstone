from pathlib import Path


def write_report(lines, report_path):
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )