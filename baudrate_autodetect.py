import serial
device_line = input("Write Serial Line: ")
check_bytes_len = 10

av_baudrates = [
    "1200",
    "1800",
    "2400",
    "4800",
    "9600",
    "19200",
    "38400",
    "57600",
    "115200"
]
CHECKING_SYMBOLS = [
    'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y',
    '0', '2', '4', '6', '8',
    '.', ',', ':', ';', '?', '!', '=',
    ' ', '\t', '\r', '\n'
]

found_baudrates = []
print("Please, wait...")
for checking_baudrate in av_baudrates:
    ser = serial.Serial(device_line, checking_baudrate)
    s = ser.read(check_bytes_len)
    for check_i in CHECKING_SYMBOLS:
        if check_i.encode() in s:
            print(checking_baudrate)
    ser.close()

ser.close()