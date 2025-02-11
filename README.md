# ESP32-S3-Touch-LCD-7
Getting LVGL MicroPython going on the Waveshare ESP32-S3 Touch LCD 7". Tested on Homebrew 4.4.17 and Ubuntu 24.04.1.

![basicdisplay](basicdisplay.png)

# Building
```bash
# Clone the repo
git clone https://github.com/lvgl-micropython/lvgl_micropython.git
cd lvgl_micropython
# Modify `builder/esp32.py` to include '3.13' in `ver`, since homebrew is already on Python 3.13.  lvgl-micropython builds successfully with the newer Python.
sed -i -- "s/'3.11', '3.12'/'3.11', '3.12', '3.13'/g" builder/esp32.py
# Build lvgl_micropython
python3 make.py esp32 BOARD=ESP32_GENERIC_S3 BOARD_VARIANT=SPIRAM_OCT DISPLAY=rgb_display INDEV=gt911
# Then use one of the suggested commands to flash - will need to modify the idf and py versions and also change (PORT) as appropriate.
~/.espressif/python_env/(idf5.2_py3.13_env)/bin/python -m esptool --chip esp32s3 -p (PORT) -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 8MB --flash_freq 80m --erase-all 0x0 build/lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin
```

# Notes
- Although time and data consuming, it is often best to start with a completely fresh copy of the lvgl_micropython repository.
- It is necessary to drive the display at 13 MHz and not 16 Mhz.

# Useful resources

- Waveshare Wiki for the ESP32-S3 Touch LCD 7": https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-7
- LVGL MicroPython: https://github.com/lvgl-micropython/lvgl_micropython.git
- Arduino library: [https://github.com/mattlalumiere/Waveshare-ESP32-S3-Touch-LCD-7.0/tree/main](https://github.com/iamfaraz/Waveshare_ST7262_LVGL.git)
  - Pin configurations here: https://github.com/iamfaraz/Waveshare_ST7262_LVGL/blob/57c570fa3136ff933ca23be17e0e741b59dba933/src/ESP_Panel_Board_Custom.h
- Some insight into getting the settings right (e.g. frequency 13 MHz, not 16 MHz, using the GT911 touch sensor, etc)
  - [Glitchy double-buffered display updates ESP32-S3 w/RGB ST7262 LCD](https://github.com/lvgl-micropython/lvgl_micropython/issues/33)
  - [RGBDisplay frame buffer allocation failure on ESP32-S3](https://github.com/lvgl-micropython/lvgl_micropython/issues/20)
- Datasheets:
  - [ST7262 Datasheet](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-4.3/ST7262.pdf)
  - [GT911](https://files.waveshare.com/upload/e/eb/GT911.pdf)  
