# basicdisplay.py
#
# Basic example of using Waveshare ESP32-S3 Touch LCD 7" with LVGL MicroPython
#
# Note: must use 13 MHz clock frequency, 16 MHz causes horizontal scrolling
#

# Libraries
import lcd_bus, rgb_display, lvgl as lv
import gt911
from micropython import const
import i2c
import task_handler

# Setup the RGB Bus
rgb_bus = lcd_bus.RGBBus(
    hsync=46,
    vsync=3,
    de=5,
    pclk=7,
    data0=14, data1=38, data2=18, data3=17, data4=10,
    data5=39, data6=0, data7=45, data8=48, data9=47, data10=21,
    data11=1, data12=2, data13=42, data14=41, data15=40,
    freq=13 * 1000 * 1000,
    hsync_front_porch=8,
    hsync_back_porch=8,
    hsync_pulse_width=4,
    vsync_front_porch=8,
    vsync_back_porch=8,
    vsync_pulse_width=4,
    pclk_active_low=True,
)

# Setup the RGB Display
_WIDTH = const(800)
_HEIGHT = const(480)

display = rgb_display.RGBDisplay(
    data_bus=rgb_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    color_space=lv.COLOR_FORMAT.RGB565,
    rgb565_byte_swap=False,
)

# Setup the touch screen
_SDA = const(8)
_SCL = const(9)
_TP_FREQ = const(100000)

i2c_bus = i2c.I2C.Bus(host=0, sda=_SDA, scl=_SCL, freq=_TP_FREQ, use_locks=False)
touch_dev = i2c.I2C.Device(bus=i2c_bus, dev_id=gt911.I2C_ADDR, reg_bits=gt911.BITS)
indev = gt911.GT911(touch_dev)

# Basic slider example
th = task_handler.TaskHandler()

scrn = lv.screen_active()
scrn.set_style_bg_color(lv.color_hex(0x000000), 0)

slider = lv.slider(scrn)
slider.set_size(300, 50)
slider.center()

label = lv.label(scrn)
label.set_text('HELLO WORLD!')
label.align(lv.ALIGN.CENTER, 0, -50)
