---
title: Set-up boards in Arduino IDE
tags: arduino
---

The boards definitions are the definitions that associate a board and it's microcontroller to the configurations files in an Arduino Core. Basically, they tell the Arduino IDE how to interact to your particular board. Some of them are installed by default, but some are not - here we see how to add them.

## Add Additional Board Manager URLs

This adds online resources from where we can fetch board definitions. Go to: `Preferences > Additional Board Manager URLs`

![](assets/preferences.png)

There, add the boards sources. **One line per URL**:

![](assets/boards_json.png)

!!! Note "Recommended setup"

    **For fabacademy/MDEF**, we recommend adding the following:

    ```
    https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
    http://arduino.esp8266.com/stable/package_esp8266com_index.json
    https://adafruit.github.io/arduino-board-index/package_adafruit_index.json
    http://drazzy.com/package_drazzy.com_index.json
    https://www.mattairtech.com/software/arduino/beta/package_MattairTech_index.json
    https://dl.espressif.com/dl/package_esp32_index.json
    ```

## Install the boards

Go to `Tools > Board > Board Manager` and navigate to the Board you want, for instance, `ESP32`. Then press `Install`:

![](assets/boards_manager_show.png)

![](assets/boards_manager.png)

Now, you should find your board in the list:

![](assets/boards_updated.png)

!!! danger
    If you don't find it, make sure that the sources url are fine.

## Extra-ball: setup the IDE nicely

For making our lives easier, you can set up the prefecences in the Arduino IDE like this:

![](assets/preferences-recommended.png)

The important ones are:

- Show verbose output during both, compilation and upload: :heavy_check_mark:
- Display line numbers: :heavy_check_mark:
- Verify code after upload: :heavy_check_mark:
- Enable Code Folding: :heavy_check_mark:
