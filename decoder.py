import irsdk
import time


ir = irsdk.IBT()
ir.open(ibt_file='ibts/m2.ibt')

brRaw_rec = ir.get_all(key='Sessions')
# brRaw = ir.get(key='BrakeRaw',index=samples - 100)

# samples = len(brRaw_rec)
# print(samples)

print(brRaw_rec)

# for sample in brRaw_rec:
#     print(sample*3.6)

#     time.sleep(0.016)
