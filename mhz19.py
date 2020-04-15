import machine
import time

uart = machine.UART(1, 9600, tx=25, rx=26)

uart = machine.UART(1, 9600, tx=25, rx=26)

while True:
    uart.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
    s = uart.read(9)
    #print ({'co2': s[2] * 256 + s[3]})
    print (s)
    time.sleep(5.0)

# if len(s) >= 4 and s[0] == 0xff and s[1] == 0x86:
#	print ({'co2': s[2] * 256 + s[3]})
