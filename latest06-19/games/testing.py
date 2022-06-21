from serial import Serial
from time import localtime, strftime

ser = Serial()
ser.port = '/dev/cu.usbmodem14301'
ser.baudrate = 9600
ser.timeout = 0
ser.open()

while True:
    line = ser.readline()
    print("here")
    # .decode()
    # if isinstance(line, str):
    #     print(ser.readline().decode())
    # # if isinstance(ser.read(), bytes):
    # #     line = ser.readline()
    # #     print(line)
    # # else:
    # #     print("nothing here")
          # line = ser.readline()
        # if isinstance(ser.readline().decode(), str):
        #     line = ser.readline()
        # else:
        #     line = b'9'

        # pygame.event.post(pygame.event.Event(EVENT_SERIAL))
