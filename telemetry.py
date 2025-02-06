import irsdk
import time

class State:
    ir_connected = False

def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False

        ir.shutdown()
        print('disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('connected')
def loop():
    ir.freeze_var_buffer_latest()
    brake = ir['BrakeRaw']
    print('Brake: ',brake,' %')

if __name__ == '__main__':
    ir = irsdk.IRSDK()
    state = State()

    try:
        while True:
            # check_iracing()

            if state.ir_connected:
                loop()

            time.sleep(1)
    except KeyboardInterrupt:
        pass