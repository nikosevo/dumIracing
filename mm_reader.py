import mmap
import struct
import time
MEMMAPFILE = "Local\\IRSDKMemMapFileName"
MEMMAPFILESIZE = 1164 * 1024  # Example size, match your actual size

# Open the memory-mapped file for reading
mmf = mmap.mmap(-1, MEMMAPFILESIZE, MEMMAPFILE, access=mmap.ACCESS_READ)


for i in range(100):
    # Read the data from memory
    mmf.seek(0)  # Move to the start of the memory-mapped file
    data = mmf.read(12)  # Read the first 12 bytes (for 3 floats)

    # Unpack and print the values (assuming speed, rpm, and throttle are stored as floats)
    speed, rpm, throttle = struct.unpack("f f f", data)
    print(f"Speed: {speed}, RPM: {rpm}, Throttle: {throttle}")
    time.sleep(1)

mmf.close()

