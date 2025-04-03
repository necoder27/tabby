# macos version: sw_vers
# uptime: uptime, sysctl kern.boottime
# memory usage: memory_pressure, vm_stat
# disk: df -h
# cpu usage: top
import subprocess
import re


def get_macos_version_info():
    output = subprocess.run(["sw_vers"], capture_output=True, text=True)

    return re.findall(r"\t\t(.+)\n", output.stdout)

def get_uptime_info():
    output = subprocess.run("uptime", capture_output=True, text=True)

    days = re.findall(r"up (.+) days", output.stdout)[0]
    hours, minutes = re.findall(r"up.*?(\d+:\d{2})", output.stdout)[0].split(":")

    return f"{days}d {hours}h {int(minutes)}m"

def get_memory_usage_info() -> str:
    ...

def get_disk_usage_info() -> str:
    ...

def get_cpu_usage_info() -> str:
    ...
