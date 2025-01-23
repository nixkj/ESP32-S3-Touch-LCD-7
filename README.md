# ESP32-S3-Touch-LCD-7
Getting LVGL Micropython going on the Waveshare ESP32-S3 Touch LCD 7"

# Building
```bash
git clone https://github.com/lvgl-micropython/lvgl_micropython.git
cd lvgl_micropython

```

# Useful resources

- Waveshare Wiki for the ESP32-S3 Touch LCD 7": https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-7
- LVGL MicroPython: https://github.com/lvgl-micropython/lvgl_micropython.git
- Arduino library: [https://github.com/mattlalumiere/Waveshare-ESP32-S3-Touch-LCD-7.0/tree/main](https://github.com/iamfaraz/Waveshare_ST7262_LVGL.git)
  - Pin configurations here: https://github.com/iamfaraz/Waveshare_ST7262_LVGL/blob/57c570fa3136ff933ca23be17e0e741b59dba933/src/ESP_Panel_Board_Custom.h
- Some insight into getting the settings right (e.g. frequency 13 MHz, not 16 MHz, using the GT911 touch sensor, etc)
  - [Glitchy double-buffered display updates ESP32-S3 w/RGB ST7262 LCD](https://github.com/lvgl-micropython/lvgl_micropython/issues/33)
  - [RGBDisplay frame buffer allocation failure on ESP32-S3](https://github.com/lvgl-micropython/lvgl_micropython/issues/20)
