import irsdk
import time
import json

def save_header_to_file(filename="header_info2.json"):
    header_data = ir.decode_header()

    if not header_data:
        print("No header data available.")
        return False

    try:
        with open(filename, "w") as file:
            json.dump(header_data, file, indent=4)
        print(f"Header data saved to {filename}")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False




ir = irsdk.IBT()
ir.open(ibt_file='rawBytes.bin')

brRaw_rec = ir.get_all(key='Sessions')
sample = ir.get_sample(0)

# print(sample)
save_header_to_file()
# brRaw = ir.get(key='BrakeRaw',index=samples - 100)

# samples = len(brRaw_rec)
# print(samples)

# print(brRaw_rec)

# for sample in brRaw_rec:
#     print(sample*3.6)

#     time.sleep(0.016)
