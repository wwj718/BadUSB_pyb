# keyboard
# https://gist.github.com/wwj718/3d5ffb8d151686fcc14c12c027cf0a5e
PLAIN = 0x00
SHIFT = 0x02
ALT = 0x04
GUI = 0x08 # Win/Apple/Meta key （win/command）

kbmap = dict()
kbmap['a'] = (0x04,PLAIN)
kbmap['b'] = (0x05,PLAIN)
kbmap['c'] = (0x06,PLAIN)
kbmap['d'] = (0x07,PLAIN)
kbmap['e'] = (0x08,PLAIN)
kbmap['f'] = (0x09,PLAIN)
kbmap['g'] = (0x0A,PLAIN)
kbmap['h'] = (0x0B,PLAIN)
kbmap['i'] = (0x0C,PLAIN)
kbmap['j'] = (0x0D,PLAIN)
kbmap['k'] = (0x0E,PLAIN)
kbmap['l'] = (0x0F,PLAIN)
kbmap['m'] = (0x10,PLAIN)
kbmap['n'] = (0x11,PLAIN)
kbmap['o'] = (0x12,PLAIN)
kbmap['p'] = (0x13,PLAIN)
kbmap['q'] = (0x14,PLAIN)
kbmap['r'] = (0x15,PLAIN)
kbmap['s'] = (0x16,PLAIN)
kbmap['t'] = (0x17,PLAIN)
kbmap['u'] = (0x18,PLAIN)
kbmap['v'] = (0x19,PLAIN)
kbmap['w'] = (0x1A,PLAIN)
kbmap['x'] = (0x1B,PLAIN)
kbmap['y'] = (0x1C,PLAIN)
kbmap['z'] = (0x1D,PLAIN)

kbmap['A'] = (0x04,SHIFT)
kbmap['B'] = (0x05,SHIFT)
kbmap['C'] = (0x06,SHIFT)
kbmap['D'] = (0x07,SHIFT)
kbmap['E'] = (0x08,SHIFT)
kbmap['F'] = (0x09,SHIFT)
kbmap['G'] = (0x0A,SHIFT)
kbmap['H'] = (0x0B,SHIFT)
kbmap['I'] = (0x0C,SHIFT)
kbmap['J'] = (0x0D,SHIFT)
kbmap['K'] = (0x0E,SHIFT)
kbmap['L'] = (0x0F,SHIFT)
kbmap['M'] = (0x10,SHIFT)
kbmap['N'] = (0x11,SHIFT)
kbmap['O'] = (0x12,SHIFT)
kbmap['P'] = (0x13,SHIFT)
kbmap['Q'] = (0x14,SHIFT)
kbmap['R'] = (0x15,SHIFT)
kbmap['S'] = (0x16,SHIFT)
kbmap['T'] = (0x17,SHIFT)
kbmap['U'] = (0x18,SHIFT)
kbmap['V'] = (0x19,SHIFT)
kbmap['W'] = (0x1A,SHIFT)
kbmap['X'] = (0x1B,SHIFT)
kbmap['Y'] = (0x1C,SHIFT)
kbmap['Z'] = (0x1D,SHIFT)

kbmap['1'] = (0x1E,PLAIN)
kbmap['2'] = (0x1F,PLAIN)
kbmap['3'] = (0x20,PLAIN)
kbmap['4'] = (0x21,PLAIN)
kbmap['5'] = (0x22,PLAIN)
kbmap['6'] = (0x23,PLAIN)
kbmap['7'] = (0x24,PLAIN)
kbmap['8'] = (0x25,PLAIN)
kbmap['9'] = (0x26,PLAIN)
kbmap['0'] = (0x27,PLAIN)


# 需要转义
# 先用正则替换
# kbmap['space'] = (0x2C,PLAIN) # SPACEBAR
kbmap[' '] = (0x2C,PLAIN) # SPACEBAR
# kbmap['enter'] = (0x28,PLAIN) # 回车
kbmap['\n'] = (0x28,PLAIN) # 回车
#define KEY_MINUS_UNDERSCORE                   
# kbmap['minus'] = (0x2D,PLAIN) # UNDERSCORE (0x2D,SHIFT)
kbmap['-'] = (0x2D,PLAIN) # UNDERSCORE (0x2D,SHIFT)

kbmap['&'] = (0x24,SHIFT)
