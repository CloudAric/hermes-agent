#!/usr/bin/env python3
"""
VPS Health Monitor — outputs JSON status report to stdout.
Exit codes: 0 = healthy/warning, 1 = critical
"""

import psutil
import json
import sys
from datetime import datetime, timezone

def main():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    load = psutil.getloadavg()

    alerts = []
    status = "healthy"

    # CPU thresholds
    if cpu > 90:
        alerts.append(f"CPU usage critical: {cpu}%")
        status = "critical"
    elif cpu > 75:
        alerts.append(f"CPU usage warning: {cpu}%")
        status = "warning" if status != "critical" else "critical"

    # Memory thresholds
    if mem.percent > 90:
        alerts.append(f"Memory usage critical: {mem.percent}%")
        status = "critical"
    elif mem.percent > 75:
        alerts.append(f"Memory usage warning: {mem.percent}%")
        status = "warning" if status != "critical" else "critical"

    # Disk thresholds
    if disk.percent > 90:
        alerts.append(f"Disk usage critical: {disk.percent}%")
        status = "critical"
    elif disk.percent > 75:
        alerts.append(f"Disk usage warning: {disk.percent}%")
        status = "warning" if status != "critical" else "critical"

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": round(cpu, 1),
        "memory_percent": round(mem.percent, 1),
        "disk_percent": round(disk.percent, 1),
        "load_average": [round(x, 2) for x in load],
        "status": status,
        "alerts": alerts,
    }

    print(json.dumps(result, indent=2))

    if status == "critical":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()