import mmap
import struct
import threading
import time
from flask import Flask, jsonify

# 1. Create Memory-Mapped File
telemetry_data = struct.pack('fff', 100.5, 7500.0, 0.75)  # (Speed, RPM, Throttle)
with open("fake_telemetry.dat", "wb") as f:
    f.write(telemetry_data)

with open("fake_telemetry.dat", "r+b") as f:
    mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# 2. Fake Event Signal
data_valid_event = threading.Event()

def update_telemetry():
    while True:
        # Update fake telemetry
        new_data = struct.pack('fff', 120.3, 7800.0, 0.80)  # New Speed, RPM, Throttle
        mmapped_file.seek(0)
        mmapped_file.write(new_data)

        # Signal new data
        data_valid_event.set()
        data_valid_event.clear()
        time.sleep(0.1)  # Update every 100ms

threading.Thread(target=update_telemetry, daemon=True).start()

# 3. Fake HTTP API
app = Flask(__name__)

@app.route('/get_sim_status')
def get_sim_status():
    return jsonify({"simStatus": "running:1"})  # Always return "connected"

@app.route('/get_session_info')
def get_session_info():
    return jsonify({
        "SessionNum": 0,
        "SessionLaps": "unlimited",
        "SessionType": "Offline Testing",
        "SessionName": "TESTING"
    })

@app.route('/get_telemetry')
def get_telemetry():
    mmapped_file.seek(0)
    speed, rpm, throttle = struct.unpack('fff', mmapped_file.read(12))
    return jsonify({"Speed": speed, "RPM": rpm, "Throttle": throttle})

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host='127.0.0.1', port=32034, debug=False, use_reloader=False)).start()
