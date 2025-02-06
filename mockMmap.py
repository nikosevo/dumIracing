import mmap
import ctypes
import time
import struct
from ctypes import wintypes

MEMMAPFILE = "Local\\IRSDKMemMapFileName"
MEMMAPFILESIZE = 1164 * 1024  # iRacing's memory size

# Create a memory-mapped file
mmf = mmap.mmap(-1, MEMMAPFILESIZE, MEMMAPFILE, mmap.ACCESS_WRITE)

# Example: Write fake telemetry data (speed, RPM, throttle)
def write_fake_telemetry(speed, rpm, throttle):
    data = struct.pack("f f f", speed, rpm, throttle)  # 3 float values
    mmf.seek(0)  # Go to start of the file
    mmf.write(data)

# Simulate telemetry updates
for i in range(100):
    write_fake_telemetry(speed=i * 10, rpm=5000, throttle=0.8 * i)
    print(f"Updated: Speed={i * 10}, RPM=5000, Throttle=0.8")
    time.sleep(1)  # Simulate real-time updates

mmf.close()
