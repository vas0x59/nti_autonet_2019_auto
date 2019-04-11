from RASPI import RASPI
import time

rpi = RASPI(init=True)

rpi.start_enc()

while True:
    print(rpi.read_enc())
    time.sleep(0.2)
rpi.stop_enc()