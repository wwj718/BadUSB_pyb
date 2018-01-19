import pyb
led = pyb.LED(1)
sw = pyb.Switch()
kb = pyb.USB_HID()
buf = bytearray(8)

PLAIN = 0x00
SHIFT = 0x02
kbmap = dict()
# part of second row example
kbmap['e'] = (0x08,PLAIN)
kbmap['h'] = (0x0B,PLAIN)
kbmap['l'] = (0x0F,PLAIN)
kbmap['o'] = (0x12,PLAIN)


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


while 1 :
    if sw() :
        led.toggle()
        string = "hello"
        sendstr(string)
        # Wait for switch to be released
        led.toggle()
    pyb.delay(20)
