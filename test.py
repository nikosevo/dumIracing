#!python3
import irsdk


ir = irsdk.IBT()
# ir = irsdk.IRSDK()
ir.open('ibts/amg.ibt')
while True:
    try:
        print(ir['Speed'])
    except KeyboardInterrupt:
        print('interupted')