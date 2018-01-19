import pyb
from utils import kbmap, ALT

led = pyb.LED(1)
sw = pyb.Switch()
kb = pyb.USB_HID()
buf = bytearray(8)


def sendchr(char) :
    if not char in kbmap.keys() :
        print("Unknow char") ; return
    # key down
    buf[2], buf[0] = kbmap[char]
    kb.send(buf)
    pyb.delay(20) #注意 delay时间太短可能出问题
    # key up
    buf[2], buf[0] = 0x00, 0x00
    kb.send(buf)
    pyb.delay(20)

def sendstr(str) :
    for c in str : sendchr(c)

def call_termial():
    # Ubuntu： alt ＋ contrl ＋T
    # windows: GUi + r then cmd\n
    # mymac alt+space  + ter\n
    # other mac: control + space(Spotlight) + ter\n
    # alt+space  + ter\n

    # key down
    buf[2], buf[0] = (0x2C,ALT)
    kb.send(buf)
    pyb.delay(20) #注意 delay时间太短可能出问题
    # key up
    buf[2], buf[0] = 0x00, 0x00
    kb.send(buf)
    pyb.delay(20)

    string = "ter\n"
    sendstr(string)
    pyb.delay(1000) #等待应用打开

while 1 :
    if sw() :
        led.toggle()
        call_termial()
        string = "python\n"
        sendstr(string)
        # Wait for switch to be released
        led.toggle()
    pyb.delay(20)
