# macos version: sw_vers, system_profiler
# uptime: uptime, sysctl kern.boottime
# memory usage: memory_pressure, vm_stat, sysctl vm.page_pageable_internal_count 
# disk: df -h
# cpu usage: top
# python library: psutil -> will maybe start using this for memory usage 
import subprocess
import re
import psutil


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

def get_memory_usage_info() -> str:
    page_size = int(subprocess.run("pagesize", capture_output=True, text=True).stdout)
    output = subprocess.run("memory_pressure", capture_output=True, text=True)
    app_memory = int(subprocess.run(["sysctl", "-n", "vm.page_pageable_internal_count"], capture_output=True, text=True).stdout)

    total_pages = int(re.findall(r"\((\d+)\spages\swith", output.stdout)[0])

    purgeable_pages = int(re.findall(r"Pages\spurgeable:\s(\d+)", output.stdout)[0])
    app_memory -= purgeable_pages
    wired_down_pages = int(re.findall(r"Pages\swired\sdown:\s(\d+)", output.stdout)[0])
    used_by_compressor_pages = int(re.findall(r"Pages\sused\sby\scompressor:\s(\d+)", output.stdout)[0])

    used_pages = app_memory + wired_down_pages + used_by_compressor_pages

    total_memory = total_pages * page_size // (2**20)
    used_memory = used_pages * page_size // (2**20)

    formatted_output = f"{used_memory}MiB / {total_memory}MiB"
        
    return formatted_output

def get_disk_usage_info() -> str:
    output = psutil.disk_usage("/")

    formatted_output = f"{(output[0] - output[2]) // 2**30}GiB / {output[0] // 2**30}GiB"

    return formatted_output

def get_cpu_usage_info() -> str:
    ...

