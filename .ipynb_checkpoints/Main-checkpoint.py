import psutil
from datetime import datetime

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"CPU Utilization at {current_time}: {cpu_usage}%")

if __name__ == "__main__":
    get_cpu_usage()