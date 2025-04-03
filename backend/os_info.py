# macos version: sw_vers, system_profiler
# uptime: uptime, sysctl kern.boottime
# memory usage: memory_pressure, vm_stat
# disk: df -h
# cpu usage: top
# python library: psutil
import subprocess
import re


SYS_PROFILER = ["system_profiler", "SPSoftwareDataType", "-detailLevel", "mini"]


def get_macos_version_info() -> str:
    output = subprocess.run(SYS_PROFILER, capture_output=True, text=True)
    
    filtered_output = re.findall(r"System\sVersion:\s(.+)\s\(", output.stdout)

    return filtered_output[0]

def get_uptime_info() -> str:
    output = subprocess.run(SYS_PROFILER, capture_output=True, text=True)

    filtered_output = re.findall(r"Time\ssince\sboot:\s(.+)", output.stdout)[0].split()

    formatted_output = ""
    for i in range(len(filtered_output)):
        if i % 2 == 0: 
            formatted_output += str(int(filtered_output[i]))
        else:
            formatted_output += filtered_output[i][0] + " " 

    return formatted_output.strip() 

def get_memory_usage_info():
    page_size = int(subprocess.run("pagesize", capture_output=True, text=True).stdout)
    output = subprocess.run("memory_pressure", capture_output=True, text=True)

    total_pages = int(re.findall(r"\((\d+)\spages\swith", output.stdout)[0])
    # used_pages: filters out active, speculative, wired down and compressed pages
    used_pages = re.findall(r"Pages\sactive:\s(\d+)|Pages\sspeculative:\s(\d+)|Pages\swired\sdown:\s(\d+)|Pages\sused\sby\scompressor:\s(\d+)", output.stdout)
        
    return used_pages

def get_disk_usage_info() -> str:
    ...

def get_cpu_usage_info() -> str:
    ...

