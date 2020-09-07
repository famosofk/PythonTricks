import shutil
import psutil

def disk_usage(du):
    if(du >50):
        return True
    return False

du = shutil.disk_usage("/")
print(du)
print(du.free/du.total)
cpuUsage = psutil.cpu_percent(3)
print(cpuUsage)
print(disk_usage(cpuUsage))
