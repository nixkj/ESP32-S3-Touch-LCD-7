# ESP32-S3-Touch-LCD-7
Getting LVGL Micropython going on the Waveshare ESP32-S3 Touch LCD 7".

# Building
```bash
# Clone the repo
git clone https://github.com/lvgl-micropython/lvgl_micropython.git
cd lvgl_micropython
# Modify `builder/esp32.py` to include '3.13' in `ver`, since homebrew is already on Python 3.13.  lvgl-micropython builds successfully with the newer Python.
sed -i -- "s/'3.11', '3.12'/'3.11', '3.12', '3.13'/g" builder/esp32.py
# Build lvgl_micropython
python3.13 make.py esp32 BOARD=ESP32_GENERIC_S3 BOARD_VARIANT=SPIRAM_OCT DISPLAY=rgb_display INDEV=gt911
# Then use one of the suggested commands to flash - change [port] as appropriate.
~/.espressif/python_env/idf5.2_py3.13_env/bin/python -m esptool --chip esp32s3 -p [port] -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 8MB --flash_freq 80m --erase-all 0x0 build/lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin
```

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
