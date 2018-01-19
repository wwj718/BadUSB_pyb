import machine
import pyb
pyb.usb_mode('CDC+HID',hid=pyb.hid_keyboard)