# macos version: sw_vers, system_profiler
# uptime: uptime, sysctl kern.boottime
# memory usage: memory_pressure, vm_stat
# disk: df -h
# cpu usage: top
import subprocess
import re


SYS_PROFILER = ["system_profiler", "SPSoftwareDataType", "-detailLevel", "mini"]


def get_macos_version_info():
    output = subprocess.run(SYS_PROFILER, capture_output=True, text=True)
    
    filtered_output = re.findall(r"System\sVersion:\s(.+)\s\(", output.stdout)

    return filtered_output[0]

def get_uptime_info():
    output = subprocess.run(SYS_PROFILER, capture_output=True, text=True)

    filtered_output = re.findall(r"Time\ssince\sboot:\s(.+)", output.stdout)[0].split()

    formatted_output = ""
    for i in range(len(filtered_output)):
        if i % 2 == 0: 
            formatted_output += str(int(filtered_output[i]))
        else:
            formatted_output += filtered_output[i][0] + " " 

    return formatted_output.strip() 

def get_memory_usage_info() -> str:
    ...

def get_disk_usage_info() -> str:
    ...

def get_cpu_usage_info() -> str:
    ...
