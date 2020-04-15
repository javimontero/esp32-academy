# esp32-academy
ESP32 SoC related
## Micropython installation
[Micropython documentation](https://docs.micropython.org/en/latest/esp32/quickref.html#rmt)

### USB to UART drivers
Download CP210x USB to UART Bridge VCP Drivers from [here](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)

Upon installation, a new tty device appears as `/dev/tty.SLAB_USBtoUART` in OSX Catalina.

We can now erase current flash:  
`esptool.py --port /dev/tty.SLAB_USBtoUART`

And deploy micropython firmware:
` esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 esp32-idf3-20200408-v1.12-351-gbd5633778.bin`

### Hello world sample
We have to take access to the ESP32 file system and run code. We are going to use the `ampy` tool.  
First install ampy
`pip install ampy`

Then run the code with 
`ampy --port /dev/tty.SLAB_USBtoUART run hello.py` 

Set AMPY_PORT environment variable for convenience:
```
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
ampy run hello.py
```
Ampy waits until process finish. With `--no-output` it just run and return (the script continuous to run in esp32.

Access serial REPL with
`screen /dev/tty.SLAB 115200`
Exit screen with `ctrl-a` `:quit`

### Run scripts at start
There are 2 python files that automatically run the micro python firmware on every power on or reset of the board:
- boot.py. Default file exist, take a look at it.  
- main.py. Here is where we can put our script.  