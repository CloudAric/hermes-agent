import json
import os
import subprocess
import datetime

def get_cpu_usage():
    # Use top to get CPU usage
    try:
        # Run top in batch mode for one iteration
        out = subprocess.check_output(['top', '-bn1'], stderr=subprocess.DEVNULL).decode('utf-8')
        for line in out.split('\n'):
            if '%Cpu(s):' in line:
                # Typical line: %Cpu(s):  5.0 us,  2.0 sy,  0.0 ni, 93.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
                # We want (100 - idle)
                parts = line.split(',')
                for part in parts:
                    if 'id' in part:
                        idle = float(part.strip().split()[0])
                        return 100.0 - idle
    except Exception as e:
        return None
    return None

def get_memory_usage():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            mem_total = 0
            mem_available = 0
            for line in lines:
                if 'MemTotal:' in line:
                    mem_total = int(line.split(':')[1].strip().split()[0])
                elif 'MemAvailable:' in line:
                    mem_available = int(line.split(':')[1].strip().split()[0])
            
            if mem_total == 0:
                return None
            
            used = mem_total - mem_available
            return (used / mem_total) * 100
    except Exception:
        return None

def get_disk_usage():
    try:
        # Root partition usage
        out = subprocess.check_output(['df', '/', '--output=pcent'], stderr=subprocess.DEVNULL).decode('utf-8')
        # Output: Use%\n 15%
        percent_str = out.split('\n')[1].strip().replace('%', '')
        return float(percent_str)
    except Exception:
        return None

def get_load_average():
    try:
        with open('/proc/loadavg', 'r') as f:
            load = f.read().split()
            return {
                '1m': float(load[0]),
                '5m': float(load[1]),
                '15m': float(load[2])
            }
    except Exception:
        return None

def get_cpu_count():
    try:
        return os.cpu_count() or 1
    except Exception:
        return 1

def main():
    cpu = get_cpu_usage()
    mem = get_memory_usage()
    disk = get_disk_usage()
    load = get_load_average()
    cores = get_cpu_count()
    
    alerts = []
    status = "healthy"
    
    # CPU check
    if cpu is not None:
        if cpu > 90:
            alerts.append(f"CPU usage critical: {cpu:.1f}%")
            status = "critical"
        elif cpu > 80:
            alerts.append(f"CPU usage warning: {cpu:.1f}%")
            if status != "critical": status = "warning"
            
    # Memory check
    if mem is not None:
        if mem > 90:
            alerts.append(f"Memory usage critical: {mem:.1f}%")
            status = "critical"
        elif mem > 80:
            alerts.append(f"Memory usage warning: {mem:.1f}%")
            if status != "critical": status = "warning"
            
    # Disk check
    if disk is not None:
        if disk > 90:
            alerts.append(f"Disk usage critical: {disk:.1f}%")
            status = "critical"
        elif disk > 80:
            alerts.append(f"Disk usage warning: {disk:.1f}%")
            if status != "critical": status = "warning"
            
    # Load check (1m)
    if load is not None:
        load_1m = load['1m']
        if load_1m > cores * 1.0:
            alerts.append(f"Load average critical: {load_1m:.2f} (Cores: {cores})")
            status = "critical"
        elif load_1m > cores * 0.7:
            alerts.append(f"Load average warning: {load_1m:.2f} (Cores: {cores})")
            if status != "critical": status = "warning"

    result = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "cpu_percent": cpu,
        "memory_percent": mem,
        "disk_percent": disk,
        "load_average": load,
        "status": status,
        "alerts": alerts
    }
    
    print(json.dumps(result))
    
    # Exit code based on status
    if status == "critical":
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()
